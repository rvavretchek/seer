---
name: academic-writing
description: Draft or revise academic prose -- structuring an argument, framing a claim with appropriate hedging, and matching register to the target venue. Use when turning research findings into a written deliverable, not when doing the research itself.
allowed-tools: Read, Write

skill_id: "core/academic-writing"
domain: "core"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Swales, J.M. & Feak, C.B. (2012, 3rd ed.) — Academic Writing for Graduate Students: Essential Tasks and Skills (University of Michigan Press): the standard reference for academic genre structure, move analysis, and hedging conventions this skill follows."
input_schema:
  required:
    - field: "content_to_write"
      type: "string"
      description: "What needs to be written -- the findings, argument, or section to draft, in whatever rough form the researcher has it."
  optional:
    - field: "target_venue"
      type: "string"
      description: "Where this will be read/published -- a journal article, a thesis chapter, a report for a non-academic audience -- since register and structure expectations differ."
    - field: "evidence_trail"
      type: "string"
      description: "The evidence base backing the claims, ideally from core/literature-review, core/claim-verification, or core/citation-analysis."
output_schema:
  fields:
    - field: "structured_draft"
      type: "string"
      description: "The drafted or revised prose, organized per the target genre's expected moves."
    - field: "hedging_check"
      type: "array"
      description: "Claims flagged where the hedging (or lack of it) doesn't match the strength of the underlying evidence."
    - field: "register_notes"
      type: "string"
      description: "Whether the prose's formality/terminology matches the target venue."
chains_well_with:
  - "core/literature-review"
  - "core/claim-verification"
  - "core/peer-review"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Academic Writing

## What This Skill Does

Turns research findings into structured academic prose — this is the drafting/writing skill, distinct from the research skills that produce the findings it writes up. Its central discipline, per Swales & Feak, is matching the *strength of a claim's phrasing* to the *strength of its actual evidence* — a finding from one small study should not be written with the same confidence as a well-replicated result, and getting this wrong (over-claiming or under-claiming) is one of the most common and most consequential academic-writing errors.

## Evidence Foundation

Swales & Feak's genre-analysis framework identifies that academic writing follows recognizable "moves" specific to genre and section — an introduction typically establishes a territory, identifies a gap, and states how the work fills it; a discussion section typically restates findings, situates them against prior work, and states limitations — and that violating the expected move structure (e.g. an introduction that doesn't establish why the gap matters) makes writing read as weak even when the underlying research is sound. Their work also establishes **hedging** as a core academic-writing skill, not a weakness: appropriate hedges ("suggests," "is consistent with," "may indicate") calibrate a claim's certainty to its actual evidentiary support, while both under-hedging (stating a tentative finding as established fact) and over-hedging (burying a well-supported finding in unnecessary qualification) are genre errors that readers — especially peer reviewers — notice immediately.

## Procedure

1. **Identify the target genre and its expected structure** — a journal article, a thesis chapter, and a policy report for a non-specialist audience all have different move structures; state which genre applies before drafting.
2. **Draft or revise following that genre's expected moves** — don't impose one generic structure on every kind of academic writing.
3. **Check hedging against the actual evidence trail.** For every substantive claim, ask: does the evidence (from `evidence_trail`, or from the skills that produced the underlying research) support this exact level of certainty? Flag claims that are over- or under-hedged relative to their support.
4. **Match register to the target venue** — a journal article's terminology and formality differs from a report meant for a general audience or a policymaker; note where the draft's register doesn't fit the stated `target_venue`.
5. **Never introduce a claim not present in the underlying research** — this skill writes up findings, it does not generate new findings; anything not traceable to the evidence trail should be flagged, not silently included.

## Example

**Input:** `content_to_write`: "Rough notes: Brazil's 0-14 population share fell from 38% to 20% since 1980. This proves urbanization causes fertility decline." `target_venue`: "A report for Sônia's academic use, citing evidence appropriately."

**Output (abridged):** Structured draft states the demographic trend as directly supported (the 38%→20% figures are well-evidenced, per the orchestrator's proof-of-concept research) but flags the causal claim ("proves urbanization causes fertility decline") as **critically over-hedged in the wrong direction** — the underlying evidence trail supports a *correlation* between Brazil's fertility transition and broader socioeconomic change, not a proven single-cause mechanism ("proves... causes" is a much stronger claim than the evidence trail can support). Revised phrasing: "is consistent with the well-documented association between urbanization, education access, and fertility decline" — hedged appropriately to what demographic research actually establishes, not overclaiming a single causal mechanism.

## Known Limitations

- **This skill checks hedging against a supplied evidence trail — it cannot independently verify claims itself.** Compose with `core/claim-verification` or `core/source-verification` first if the evidence trail's own reliability hasn't been checked.
- **Genre conventions vary by field and language, not just by document type** — academic writing conventions in Portuguese-language Brazilian academic contexts may differ from the English-language genre analysis this skill is grounded in; flag this explicitly when drafting for a Brazilian academic venue rather than assuming direct transfer.
- **Does not replace the researcher's own voice and judgment on framing.** It structures and calibrates; the intellectual argument and its emphasis remain the researcher's (Constitution, Principle 6).
