---
name: peer-review
description: Review an academic draft the way a rigorous, constructive peer reviewer would -- checking argument structure, evidence support, and methodological soundness, never just surface polish. Use to critique a draft before submission, not to write it (that's core/academic-writing).
allowed-tools: Read, Write

skill_id: "core/peer-review"
domain: "core"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "COPE (Committee on Publication Ethics) — Ethical Guidelines for Peer Reviewers: the standard for reviewer conduct (unbiased, constructive, respecting intellectual property, flagging misconduct) this skill's review stance follows."
input_schema:
  required:
    - field: "draft"
      type: "string"
      description: "The academic draft or section to review."
  optional:
    - field: "evidence_trail"
      type: "string"
      description: "The evidence base the draft claims to rest on, if available, to check claims against support."
    - field: "review_focus"
      type: "string"
      description: "Where to concentrate scrutiny -- methodology, argument structure, evidence support, or a full review across all three."
output_schema:
  fields:
    - field: "structural_review"
      type: "array"
      description: "Findings about argument structure and organization -- does the piece build its case in the right order, does each section do its expected job."
    - field: "evidence_review"
      type: "array"
      description: "Findings about whether claims are adequately supported and appropriately hedged relative to their evidence."
    - field: "verdict"
      type: "string"
      description: "Overall assessment -- ready, needs minor revision, needs major revision -- with the reasoning, never just a bare label."
chains_well_with:
  - "core/academic-writing"
  - "core/claim-verification"
  - "core/citation-analysis"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Peer Review

## What This Skill Does

Reviews an academic draft the way a rigorous, constructive peer reviewer does: checking whether the argument is structurally sound, whether claims are adequately supported, and whether the methodology holds up — never limited to surface-level line editing (that overlaps with `core/academic-writing`'s revision role, not this skill's). A review that only fixes prose while leaving an unsupported claim or a structural gap untouched has not done its job.

## Evidence Foundation

COPE's Ethical Guidelines for Peer Reviewers establish the professional stance this skill takes: reviews must be unbiased, constructive, and objective — critical without being dismissive, specific without being merely a list of complaints. COPE also establishes that reviewers act as a safeguard against research misconduct and unsupported claims, not just a quality filter on prose — flagging where a claim outruns its evidence, where a method doesn't support the conclusion drawn from it, or where a citation is used to support something it doesn't actually show, are core reviewer responsibilities, not optional extras.

## Procedure

1. **Assess argument structure first**, before any line-level feedback. Does the draft build its case in a defensible order — is the claim stated, is it motivated, is evidence presented before conclusions are drawn from it? A structurally sound draft with weak prose is a smaller problem than a well-written draft with a broken argument.
2. **Check each substantive claim against its evidence trail**, when available. Flag claims that outrun their support (overclaiming) and claims that are supported but stated too tentatively (underclaiming) — both are real problems, not just the former.
3. **Check methodology, when applicable**, against the method's own known limitations — did the draft acknowledge the MAUP risk if using scale-sensitive geographic data, the database-coverage gap if relying on English-language sources for a Brazil-specific topic, the small-sample caveat if generalizing from limited data? A methodologically aware draft names its own limitations; a review should flag where it doesn't.
4. **Be specific, never just "this needs more support."** Name exactly which claim, quote it, and say what kind of evidence or qualification would fix it.
5. **Give a verdict with reasoning** — not just a label, but the specific things that would need to change to move from "needs major revision" to "ready," so the feedback is actionable.

## Example

**Input:** `draft` (excerpt): "Brazil's fertility decline since 1980 proves that urbanization directly causes falling birth rates, and this pattern will inevitably repeat in every developing region." `evidence_trail`: the orchestrator proof-of-concept's real demographic findings (Brazil fertility 4.35→1.57, 1980–2023; compressed/faster version of the global pattern).

**Output (abridged):** Structural review: the causal claim ("proves... directly causes") is stated before any competing explanation is considered or ruled out — a reviewer would flag this as asserting causation from correlation without the argument work to support it. Evidence review: the underlying evidence trail supports a *documented association* and a *shape-similarity* to the global pattern (compressed, faster), not a proven direct causal mechanism, and certainly not a universal prediction ("will inevitably repeat in every developing region") — this significantly overclaims relative to the evidence. Verdict: **needs major revision** — the causal and predictive claims need to be either supported with actual causal-inference evidence (not present in the current evidence trail) or rehedged to match what a correlational demographic comparison can actually establish.

## Known Limitations

- **Reviews the argument on the page, not the underlying research itself** — if the original data collection or analysis has a flaw not visible in the draft's own presentation, this skill won't catch it; compose with `core/claim-verification` or `core/source-verification` to check the evidence trail independently.
- **"Constructive" does not mean "lenient."** Per COPE's standard, a review that softens a real structural or evidentiary problem to avoid discouraging the researcher has failed at the actual job — flag real problems plainly, alongside what's working.
- **Methodological review depends on this skill (or the researcher) knowing the relevant method's known failure modes** — it can check against limitations already documented in Seer's own skills (MAUP, database coverage gaps, etc.), but a method entirely outside Seer's current skill roster won't have that grounding available.
