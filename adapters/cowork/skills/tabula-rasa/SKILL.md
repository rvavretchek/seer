---
name: tabula-rasa
description: Run a visible round-table where Seer's discipline skills speak in their own voice, to each other and to the researcher, instead of composing silently. Use when the researcher wants to see multiple disciplinary angles argue it out live -- not when a single skill or the silent orchestrator composition already answers the request.
allowed-tools: Read, Glob, Write

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
      description: "What was discussed but not yet decided by the end of the session -- the seam Continuity writes through once built (see Known Limitations)."
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

### 2. Voice Each Persona

Session mode: one mind behind every voice, each persona distinct in how it reasons and what it emphasizes, not just in name. Disagreement between disciplines is not resolved on the room's behalf -- when two personas' readings of the same evidence genuinely conflict, both stand, named, rather than one quietly winning. Personality, humor, and light rivalry between personas are welcome in the room precisely because they help the researcher track *who* holds *which* position -- but nothing about tone changes what a persona actually claims, and the finished, citable output (see Continuity) is never sourced from banter, only from what a persona substantively argued.

### 3. Continuity

Not implemented in this version -- documented here as the seam the next increment attaches to, so this version doesn't have to be reshaped to fit it later. When built: a single per-project ata (append-only, growing across every Tabula Rasa session for that `project_path`, mirroring the pattern this skill's own planning sessions were run under) captures what was discussed and decided, and -- more importantly -- what was discussed but left undecided, read back in distilled form at the start of the next session. Decisions and adopted methodology that graduate out of the ata belong in the project's own editable documentation (see `docs/skill-contract.md`, Project Context), never left to live only in the ata. Both artifacts live entirely inside `project_path`, self-contained -- no dependency on this repository's own `_bmad/` tooling, which does not ship with the plugin.

### 4. Wrapping Up

When the researcher signals the session is done, the **Always Present** persona reads back the open threads plainly -- what got settled, what didn't -- and the room returns to normal skill behavior. No transcript of the room's banter is ever the deliverable; if the researcher wants a written output from the discussion, that gets composed the same way any skill's `output_schema` would, sourced from what was substantively argued.

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

## Known Limitations

- **No continuity between sessions in this version.** Every session starts cold; open threads from a prior session are not recovered. See Continuity above for the deferred design.
- **Session mode only.** One mind voices every persona; there is no real parallel dispatch the way the orchestrator's subagents run independently. A future increment may add a dispatched mode for cases where independent reasoning per persona actually changes the outcome.
- **`personas.md` coverage lags the skill roster.** A newly contributed discipline skill joins the room under its own title, not a named persona, until `personas.md` is updated -- this is a deliberate default, not a bug to route around.
- **Persona granularity is per-domain, not per-skill** (see Proof of Concept #1). Two skills from the same domain are voiced by the same persona today; this is untested for the case where they'd genuinely disagree with each other rather than agreeing in spirit.
