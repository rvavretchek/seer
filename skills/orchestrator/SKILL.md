---
name: orchestrator
description: Decompose an interdisciplinary academic research request and compose the right combination of Seer skills to answer it. Use when a request plausibly needs more than one discipline or method skill working together -- not when a single skill's description already matches the request directly.
allowed-tools: Read, Glob, Grep, Write, Task

skill_id: "orchestrator/orchestrator"
domain: "orchestrator"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "collaborative-deep-research/agent-papers-cli, research-coordinator skill (Apache-2.0): the analyze -> dispatch -> synthesize pattern this orchestrator generalizes. Its fixed 3-workflow table is replaced here with runtime discovery over skills/**/SKILL.md, since Seer's skill roster grows by community contribution and can't be hardcoded -- this generalization is original design, not itself evidence-backed by the source pattern."
input_schema:
  required:
    - field: "research_request"
      type: "string"
      description: "The researcher's request in plain language, exactly as stated -- not pre-parsed or simplified."
  optional:
    - field: "output_format"
      type: "string"
      description: "The deliverable shape the researcher wants -- a written report, a data table/spreadsheet, a map, or unspecified (infer from the request)."
output_schema:
  fields:
    - field: "composition_plan"
      type: "object"
      description: "Which skills were selected, in what order or parallel grouping, and why -- kept internal/loggable, not necessarily shown to the researcher unless the plan is large or ambiguous enough to need confirmation."
    - field: "synthesized_answer"
      type: "string"
      description: "The single, coherent deliverable -- reads as one answer, not a stitched report labeled by which skill produced which section."
    - field: "evidence_trail"
      type: "array"
      description: "Internal record of which skill/evidence_sources contributed to which claim, for provenance and auditability -- not necessarily surfaced verbatim to the researcher."
chains_well_with: []
license: "CC BY-SA 4.0"
provenance: "forked:collaborative-deep-research/agent-papers-cli@23a1941 (research-coordinator skill), adapted to the Seer skill contract with dynamic skill discovery"
---

# Orchestrator

## What This Skill Does

The meta-skill that makes Seer's skills into a *system* rather than a pile of independently useful but disconnected files. Given a research request, it decides which combination of Seer skills the request actually needs, runs them in the right order (or in parallel when independent), and synthesizes their outputs into one coherent answer — without the composition itself ever becoming something the researcher has to manage. This is Seer's core value proposition, per the product brief: composition, not collection.

Unlike every other skill in `skills/`, this one deliberately has no `chains_well_with` peers — it isn't a peer among content skills, it's what discovers and sequences them at runtime. Content skills stay independently useful when invoked directly (any Agent Skills-compatible tool can match a single skill by its own `description` without this orchestrator ever running); this skill exists specifically for requests spanning more than one.

## Why Runtime Discovery, Not a Fixed Table

`agent-papers-cli`'s `research-coordinator` — the real pattern this generalizes — works from a **fixed table** of exactly three workflows, hardcoded in its prompt. That's the right choice for a repo with three stable skills. It's the wrong choice for Seer: the whole point of the Constitution's composability principle is that new discipline packs (and new skills within existing packs) arrive by community contribution, unknown in advance. An orchestrator hardcoded to today's 18 skills would need a manual edit — and a new PR to this very file — every time a contributor added a skill. That defeats the purpose of a skill contract in the first place.

## Procedure

### 1. Analyze the Request

Read the `research_request` as given — don't pre-simplify it. Identify what it plausibly needs: which discipline(s) (`geography`, `education`, `core`, future packs), which methods (quantitative, qualitative, spatial, mixed), and whether it needs a single skill or several composed together. If the request is genuinely ambiguous or too broad to scope confidently, ask the researcher to clarify **in plain language**, before proceeding — never in terms of "which skill should I invoke," since that exposes the mechanism to a researcher who shouldn't need to know it exists (Sônia's zero-CLI floor applies here too: the *question back to her* should read like a colleague asking a clarifying question, not a system prompt).

### 2. Discover Available Skills

`Glob` for `skills/**/SKILL.md`, `Read` each match's frontmatter (`name`, `domain`, `description`, `chains_well_with`, `evidence_strength`) — **excluding this file itself** (`domain: orchestrator` is never a candidate; it is the discoverer, not something to discover). This is a full scan, not a cached index — at the current skill count (under 20) this is cheap. See Known Limitations for when this stops being true.

### 3. Build the Composition Plan

Match the request against discovered skills' `description` and `domain`. For a discipline the request touches, prefer starting from that discipline's foundational/scoping skill when one exists (`geography/geographic-research`, `education/educational-research`) — they exist specifically to be entered first. From there, follow `chains_well_with` to pick genuinely relevant complementary skills — do not add a skill just because it exists in a touched domain; each addition to the plan should trace to something the request actually asked for. Mark which selected skills are **sequential** (one's output feeds another's input — e.g. `geography/geographic-research`'s scoping output feeding `geography/spatial-analysis`) versus **independent** (can run in parallel, e.g. a `geography/human-geography` angle and an `education/educational-research` angle on the same underlying question).

If the resulting plan is large (many skills) or the request was ambiguous enough that step 1 required a clarifying question, confirm the plan with the researcher before dispatching — again, in plain outcome-oriented language ("vou olhar isso pelo lado geográfico e educacional, cruzando com dados do IBGE — pode seguir?"), never by naming internal skill IDs to a non-technical researcher.

### 4. Dispatch

For each skill in the plan: `Read` its full `SKILL.md`, and spawn a `Task` subagent (`general-purpose` type) with that skill's procedure as its prompt, filling the skill's own `input_schema` fields from the request (and, for sequential skills, from the prior skill's output). Run independent skills' subagents in parallel; run sequential chains in order.

### 5. Synthesize

Combine the dispatched skills' outputs into **one coherent answer** — not a report with a section per skill. Resolve any genuine contradiction between skills explicitly rather than silently picking one side (Constitution, Principle 6 — human judgment stays central; a real unresolved tension between, say, a demographic finding and a policy-mechanism finding should be surfaced to the researcher, not smoothed over). Every substantive claim should trace back to a skill's evidence base — keep that trail in `evidence_trail` even when the researcher-facing answer doesn't spell it out inline.

## Example

**Input:** `research_request`: "Verifique os índices de crescimento vegetativo das regiões Norte e Nordeste entre 1980–2020, por faixa etária, e o que isso significa para o planejamento educacional regional."

**Composition plan:** `geography/geographic-research` (scope: macro-region, human/demographic branch, quantitative method, IBGE source — per its own worked example) → `geography/spatial-analysis` (test whether growth clusters geographically within the Northeast) → `geography/human-geography` (interpret the demographic pattern, with positionality flagged) → `education/educational-policy` (the "what does this mean for regional education planning" half of the request, composing the demographic finding with education-funding/policy mechanisms). Sequential: geographic-research feeds both spatial-analysis and human-geography; human-geography's interpretation feeds educational-policy.

**Synthesized answer (shape, not full content):** One report combining the demographic pattern (with its MAUP caveat), the spatial clustering finding, and the education-planning implication — written as a single narrative with an evidence trail underneath, not four labeled sections from four skills.

## Known Limitations

- **Full-scan discovery doesn't scale indefinitely.** At today's skill count this is cheap; `education-agent-skills` itself needed a `registry.json` + bundled index once it reached 165 skills (see `vendor/education-agent-skills/CLAUDE.md`'s build workflow). When Seer's roster grows substantially, this orchestrator will need an equivalent pre-built catalog rather than a live `Glob`+`Read` scan every time — not built now, flagged for when the skill count justifies the added complexity.
- **Dispatch via the `Task` tool is verified in Claude Code today; not yet verified in the Claude Cowork adapter.** Cowork's own documentation states it "breaks complex work into smaller tasks and coordinates parallel workstreams," suggesting an equivalent mechanism exists, but this orchestrator's exact dispatch step hasn't been tested against Cowork's actual plugin-execution environment — a question for the `adapters/cowork/` build, not resolved here.
- **Cannot adjudicate a genuine disagreement between two skills' findings** — it can and should surface the tension; resolving it is the researcher's call (Constitution, Principle 6).
- **Plan quality depends on `chains_well_with` being accurate and current** in every skill's frontmatter — a skill contributed without honest composability metadata will be invisible to this orchestrator's planning step even if it would have been relevant.
