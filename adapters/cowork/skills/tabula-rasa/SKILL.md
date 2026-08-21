---
name: tabula-rasa
description: Run a visible round-table where Seer's discipline skills speak in their own voice, to each other and to the researcher, instead of composing silently. Use when the researcher wants to see multiple disciplinary angles argue it out live -- not when a single skill or the silent orchestrator composition already answers the request.
allowed-tools: Read, Glob, Write, Edit, Task

skill_id: "tabula-rasa/tabula-rasa"
domain: "tabula-rasa"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "BMAD Method, party-mode skill (MIT, copyright BMad Code LLC 2025): the session-mode room mechanic (voice every persona inline, one mind behind every voice, in-character disagreement not smoothed into consensus) this generalizes -- mechanism/pattern only, no verbatim text, no 'BMad' trademark used (Constitution, Principle 5)."
input_schema:
  required:
    - field: "research_request"
      type: "string"
      description: "What the researcher wants to discuss or work through, in plain language -- not pre-parsed or simplified."
  optional:
    - field: "project_path"
      type: "string"
      description: "The researcher's project folder. When absent, the room runs without Continuity (see below) -- a single-session conversation only."
output_schema:
  fields:
    - field: "room_transcript"
      type: "string"
      description: "The conversation as it happened -- personas speaking to the researcher and to each other, not a report with a section per discipline."
    - field: "open_threads"
      type: "array"
      description: "What was discussed but not yet decided by the end of the session -- what Continuity (see Procedure) writes into `memoria.md` when `project_path` is given."
chains_well_with: []
license: "CC BY-SA 4.0"
provenance: "original, inspired by: BMAD Method party-mode skill (MIT, BMad Code LLC 2025) -- pattern only, see evidence_sources."
---

# Tabula Rasa

## What This Skill Does

Where the orchestrator composes Seer's skills silently -- discipline angles blended into one answer, the seams invisible by design -- Tabula Rasa does the opposite on purpose: it opens a room where each relevant discipline skill speaks in its own voice, to the researcher and to each other, and lets real disagreement between disciplines surface instead of being resolved before the researcher ever sees it. Same skill roster underneath, same evidence each skill already carries; the difference is whether composition happens behind the scenes or out loud.

This is not a general-purpose chat mode. It exists specifically for the moments a synthesized answer isn't what the researcher needs -- when watching two disciplinary lenses actually contend with each other, live, is itself the useful thing (a real tension between a demographic reading and a policy-mechanism reading is more legible as two voices arguing than as one paragraph noting "there is tension here").

Like the orchestrator, this skill has no `chains_well_with` peers: it isn't a content skill among content skills, it's a second mode of composing the same roster.

## Evidence Foundation

The party-mode pattern this generalizes is itself built on a simple claim: forcing a single synthesized voice too early collapses genuine disagreement before it's been examined, while distinct voices arguing in the open surface objections a single blended narrator would have smoothed over without noticing. Seer's own orchestrator already embodies half of this lesson defensively -- Constitution Principle 6 requires it to flag unresolved tension between skills rather than silently pick a side. Tabula Rasa is the same discipline taken further: instead of flagging the tension after the fact, it lets the tension play out as the primary experience, with the researcher pulled into the argument rather than handed its conclusion.

## Procedure

### 1. Discover the Room

`Glob` for `skills/**/SKILL.md`, `Read` each match's frontmatter (`name`, `domain`, `description`, `chains_well_with`) -- same discovery the orchestrator already uses, excluding this file and the orchestrator itself. Match discovered skills against the `research_request` the same way the orchestrator's Step 3 does. Then `Read` `personas.md` to find each matched domain's voice; a matched skill with no entry there still joins the room, speaking under its own skill title rather than a named persona, until `personas.md` grows to cover it. The room's **Always Present** persona (`personas.md`) joins regardless of what the discovery step matched -- not tied to any domain, present in most sessions by design.

If `project_path` was given, do the Continuity reads (see below) alongside this step, before the room opens.

### 2. Voice Each Persona

Session mode: one mind behind every voice, each persona distinct in how it reasons and what it emphasizes, not just in name. Disagreement between disciplines is not resolved on the room's behalf -- when two personas' readings of the same evidence genuinely conflict, both stand, named, rather than one quietly winning. Personality, humor, and light rivalry between personas are welcome in the room precisely because they help the researcher track *who* holds *which* position -- but nothing about tone changes what a persona actually claims, and the finished, citable output (see Continuity) is never sourced from banter, only from what a persona substantively argued.

### 3. Continuity

Skipped entirely when `project_path` is absent, per `input_schema` -- the session runs single-shot with no read or write below. When present, two artifacts, both single-file-per-project (never split by day or session) and both located relative to `project_path`, self-contained -- no dependency on this repository's own `_bmad/` tooling, which does not ship with the plugin:

- **`{project_path}/.tabula-rasa/memoria.md`** -- hidden. The raw discussion log: what was discussed, and especially what was discussed but not yet decided (open threads). Grows across every Tabula Rasa session for the project. Internal/working file, not meant for the researcher to read directly, though nothing prevents it.
- **`{project_path}/seer_output/ata-do-projeto.md`** -- visible, under `seer_output/` (mirrors this repo's own `_bmad-output/` convention, one layer up, for the same kind of tool-owned-but-legible output). The decisions record: what got closed, adopted methodology, resolved threads -- a living document for the *project*, reorganized as decisions evolve, not append-only the way `memoria.md` is.

**Read (part of Discover the Room, above).** Each file independently, only if it exists; neither existing is not an error, the session simply opens cold on that front. The two files are read differently, because they aren't the same kind of artifact: `ata-do-projeto.md` is a curated, reorganized living document (see below) that stays a reasonable size by construction, so it is always `Read` directly -- its content shapes how the room opens, and a decision already closed there is not relitigated as if it were new. `memoria.md` is the unbounded append-only log, so how it's read is a judgment call, not a fixed rule: on a first session, or whenever the file is absent or still trivially short, just `Read` it directly -- dispatching a subagent for a near-empty file is wasted overhead. Once it's accrued substantial content across sessions, dispatch a `Task` subagent (`general-purpose` type) to read the full file and return a compact, distilled brief -- open threads and whatever color is actually relevant, not a recap or a transcript -- the same discipline `.claude/skills/bmad-party-mode/references/party-memory.md`'s "read it on entry -- distill, don't dump" describes, now using the tool this skill actually has rather than reading the raw log in full every time. Either way, the open threads are raised by Alberico (**Always Present**, `personas.md`) organically, near the start, worked into how he opens the room in character -- never a recited log dump, never "I loaded a file" breaking the fourth wall.

**Write, `ata-do-projeto.md` -- during the session, as decisions close.** The moment something genuinely becomes a closed decision -- resolved thread, adopted methodology, a position the room settled on -- write it then, not held for Wrapping Up; the session could end abruptly before wrap-up is reached. Use `Edit` on the specific existing section a decision updates or supersedes (this is a living document); `Write` a new section only for a decision with no existing home. Constitution Principle 6 applies here exactly as `docs/skill-contract.md`'s Project Context section already applies it to `metodologia.md`: if `ata-do-projeto.md`'s existing content conflicts with what a discipline skill in the room would normally argue, the room flags the tension to the researcher rather than silently overriding either the skill's default or the ata's prior decision.

**Write, `memoria.md` -- once, at Wrapping Up.** Unlike the ata, this is reasonably composed a single time, at Wrapping Up (below) -- its session block is a summary of the whole session's open threads as they stand at the end, so composing it earlier would mean redoing it. `Read` the existing file if present, then `Write` the full file back with the new session's block appended at the end under a dated heading (e.g. `## Sessão {date}`) -- prior content is never overwritten or discarded, only added to. If the file doesn't exist yet, this `Write` creates it under `.tabula-rasa/`.

Both writes are silent -- the room never says "noting this" or "I'll remember this," same discipline as the `party-memory.md` reference above.

**Relationship to `metodologia.md` is deliberately unresolved.** `metodologia.md` (`docs/skill-contract.md`, Project Context) is narrower -- which methodology was adopted -- and read by any skill in Seer, not just this one. `ata-do-projeto.md` is broader -- any project decision -- and is Tabula-Rasa-specific. This version does not merge them, cross-reference them, or make one a subset of the other; a future increment may need to reconcile the two, but that is an open question, not something decided here.

### 4. Wrapping Up

When the researcher signals the session is done, the **Always Present** persona reads back the open threads plainly -- what got settled, what didn't -- and the room returns to normal skill behavior. This is also when `memoria.md`'s session block gets written, if Continuity is active (see above) -- the same open threads just read back, composed into the dated entry. No transcript of the room's banter is ever the deliverable; if the researcher wants a written output from the discussion, that gets composed the same way any skill's `output_schema` would, sourced from what was substantively argued.

## Example

**Input:** `research_request`: "Alberico e Serafim, me ajudem a pensar se dá pra tratar o recorte territorial da minha pesquisa como Geografia pura ou se isso já vira uma questão de política educacional."

**Room (shape, not full transcript):** Alberico opens from what the territorial data actually supports -- and where it stops supporting a claim. Serafim pushes back that the moment funding or curriculum enters the picture, it stops being descriptive Geography and starts being a policy question neither of them can settle alone -- and says so directly, not as a footnote. The disagreement is left standing, named, with both positions attributed, and the researcher is asked which framing she actually needs to answer next.

## Proof of Concept

**#1.** Run on the same real request as the orchestrator's Cowork proof of concept #2 (`skills/orchestrator/SKILL.md`), deliberately reused so the two composition modes are comparable on identical input: *"Analise como a queda da taxa de natalidade no Nordeste brasileiro pode afetar o planejamento educacional regional nos próximos 10 anos."*

Discovery matched `geography/human-geography`, `geography/economic-geography`, and `education/educational-policy` against the request; `personas.md` resolved both geography skills to Alberico and the education skill to Serafim. The room ran for real, grounded in each matched skill's own evidence base, not improvised:

- Alberico opened from `economic-geography`'s scale-mismatch discipline -- decline in natural growth is unlikely to be spatially uniform across the Northeast, and FUNDEB's enrollment-linked funding formula means municipalities with a weaker tax base absorb an enrollment decline harder than better-resourced ones, independent of the raw regional percentage. He argued mapping *where* the decline concentrates has to come before any regional plan.
- Serafim, from `educational-policy`, didn't contest the map -- he contested where it puts the leverage. Ball's finding (policy is reshaped by whoever implements it, and effects stratify even under formally universal rules) means the same demographic map produces different real outcomes depending on municipal incentives: a district dependent on enrollment-linked funding has a structural reason to resist consolidating schools even where demographically justified, and a poorer municipality without a well-resourced district's slack is more likely to lose a school outright than gain smaller class sizes from the same decline.
- Neither position resolved the other's, deliberately -- the room closed by handing the researcher an explicit fork (map the concentration first, or take the concentration as given and design the policy response first) rather than picking one, matching the same tension-preserving discipline `skills/orchestrator/SKILL.md` already applies to composition.

**Real finding, not anticipated when this skill was written:** `personas.md` maps persona-per-*domain*, not persona-per-*skill*. Here two geography skills (`human-geography`, `economic-geography`) both matched, and both were voiced as Alberico -- workable because a single geographer plausibly holds both lenses at once and they agreed in spirit. This would not hold if two same-domain skills genuinely disagreed with *each other* rather than with a different domain's persona -- the room has no mechanism yet to voice that as two distinct positions. Not fixed now; recorded below as an open design question for whenever it actually happens in a real session, not solved speculatively.

**#2.** Continuity validated end to end with two real, separate `claude -p` invocations against the same `project_path` (a scratch test folder), each a full Read/Write/Task-dispatch session, not a simulation.

- **Session 1** (`research_request`: whether a rural school-dropout study should be framed as Geography, acesso físico, or Educação, política de permanência -- deliberately left open): Ubaldo and Serafim argued it in character, converged that the right framing depends on which rural profile the researcher is actually studying, and the session closed with the tension explicitly unresolved. Continuity wrote both files for the first time: `.tabula-rasa/memoria.md` (a dated `## Sessão {date}` block, the open thread stated plainly) and `seer_output/ata-do-projeto.md` (an "Em Aberto" section for the unresolved framing question, "Decisões Fechadas" left empty since nothing had closed).
- **Session 2**, same `project_path`, a deliberately thin prompt ("voltei, me ajudem a avançar") carrying no restated context: Alberico opened *in character* directly from the unresolved framing question -- without narrating that a file had been loaded -- and the room advanced the thread for real (Ubaldo proposed a three-profile typology of rural contexts, each implying a different literature base). `memoria.md` got a second dated block appended below the first, unmodified. `ata-do-projeto.md`'s existing "Em Aberto" section was `Edit`-updated in place with the new typology, not duplicated as a new section -- confirming the living-document behavior the Procedure specifies, distinct from `memoria.md`'s pure append.

This is the strongest evidence yet that Continuity behaves as designed rather than merely as written: real state survived a genuinely separate process invocation, the fourth wall held, and the two files kept their distinct write disciplines (append vs. in-place edit) under an actual second session, not just a read of the Procedure text.

## Known Limitations

- **No hardcoded threshold for "substantial enough to distill."** `memoria.md`'s direct-read-vs-dispatch choice (see Continuity above) is left to the model's judgment each session rather than a precise line-count or token cutoff -- deliberately, matching how the rest of this skill avoids hardcoding thresholds elsewhere, but it does mean two sessions could judge the same file differently.
- **`ata-do-projeto.md` and `metodologia.md` are two distinct, currently-unmerged artifacts** (see Continuity above). The former is Tabula-Rasa-specific and covers any project decision; the latter is skill-agnostic and covers only adopted methodology. Reconciling or cross-referencing them is an open question this version deliberately leaves open.
- **Session mode only.** One mind voices every persona; there is no real parallel dispatch the way the orchestrator's subagents run independently. A future increment may add a dispatched mode for cases where independent reasoning per persona actually changes the outcome.
- **`personas.md` coverage lags the skill roster.** A newly contributed discipline skill joins the room under its own title, not a named persona, until `personas.md` is updated -- this is a deliberate default, not a bug to route around.
- **Persona granularity is per-domain, not per-skill** (see Proof of Concept #1). Two skills from the same domain are voiced by the same persona today; this is untested for the case where they'd genuinely disagree with each other rather than agreeing in spirit.
