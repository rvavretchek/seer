---
name: claim-verification
description: Verify a specific factual claim by decomposing it into sub-claims and searching for evidence across web and academic sources, with an explicit verdict per sub-claim. Use when a specific statement needs to be fact-checked, not a whole source's overall credibility (that's core/source-verification).
allowed-tools: Read, Write, Bash

skill_id: "core/claim-verification"
domain: "core"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "collaborative-deep-research/agent-papers-cli, fact-check skill (Apache-2.0): the decompose -> search -> verify -> assess -> report structure this skill is adapted from."
input_schema:
  required:
    - field: "claim"
      type: "string"
      description: "The specific claim to verify, stated as precisely as possible."
  optional:
    - field: "context"
      type: "string"
      description: "Where the claim came from or why it needs verification -- helps calibrate how much scrutiny it needs."
output_schema:
  fields:
    - field: "sub_claims"
      type: "array"
      description: "The claim decomposed into specific, independently verifiable parts."
    - field: "verdicts"
      type: "array"
      description: "Per sub-claim: Supported, Partially supported, Unsupported, or Uncertain, with the evidence behind each verdict."
    - field: "overall_assessment"
      type: "string"
      description: "The combined verdict across all sub-claims, stated plainly."
chains_well_with:
  - "core/source-verification"
  - "core/literature-review"
  - "core/citation-analysis"
license: "CC BY-SA 4.0"
provenance: "forked:collaborative-deep-research/agent-papers-cli@23a1941 (fact-check skill), adapted to the Seer skill contract"
---

# Claim Verification

## What This Skill Does

Verifies a specific factual claim by breaking it into its verifiable parts, searching for evidence on each, and assigning an explicit verdict — never a bare "true" or "false" without the evidence trail. This is different from `core/source-verification`: that skill asks *is this source credible*; this skill asks *is this specific statement true*, which may draw on multiple sources, credible or not.

## Evidence Foundation

The procedure below generalizes `agent-papers-cli`'s `fact-check` skill, which established the discipline this skill inherits: decompose before searching (a compound claim hides which part is actually in question), prefer primary sources over secondary reports, and distinguish "no evidence found" from "evidence contradicts" — these are different findings that call for different confidence in the verdict, and conflating them is the most common failure mode in informal fact-checking.

## Procedure

1. **Decompose the claim into specific, independently verifiable sub-claims.** List them explicitly before searching — a claim like "Brazil's fertility rate fell below replacement in 2010 due to urbanization" bundles a testable statistic (the rate, the year) with a causal claim (urbanization as the driver) that needs separate, different evidence.
2. **Search for evidence on each sub-claim**, preferring primary sources (original datasets, official statistics, the paper itself) over secondary reports (news summaries, blog posts) about those primary sources.
3. **Verify the sources found, not just the snippets.** Read the actual relevant section of a paper or dataset rather than relying on a search-result summary — summaries can misstate what a source actually says.
4. **Assign a verdict per sub-claim**: **Supported** (strong evidence from multiple reliable sources), **Partially supported** (some evidence, with caveats), **Unsupported** (no evidence found, or evidence contradicts), or **Uncertain** (insufficient evidence either way). Never collapse "no evidence found" and "evidence contradicts" into the same verdict — they imply very different confidence levels.
5. **Report** the original claim, each sub-claim with its verdict and supporting evidence, an overall assessment, and every source cited.

## Example

**Input:** `claim`: "PNAD Contínua shows Brazil's 0-14 population share has been below 20% since 2020."

**Output (abridged):** Decomposed into two sub-claims: (a) the specific threshold and timing ("below 20% since 2020"), (b) the attributed source (PNAD Contínua specifically). Sub-claim (a): **Partially supported** — the 2022 Censo Demográfico reports 19.8%, consistent with "below 20%," but the claim's implied continuous PNAD Contínua annual series doesn't exist at this granularity before the 2022 Censo; the "since 2020" framing overstates what's actually been measured continuously. Sub-claim (b): **Unsupported as stated** — the actual source for the cited 19.8% figure is the 2022 Censo Demográfico, not PNAD Contínua; this is exactly the source-attribution error `geography/geographic-research` flags as a common pitfall. Overall assessment: the numeric claim is roughly right, but the source attribution is wrong — worth correcting before repeating.

## Known Limitations

- **Verifies findability of evidence, not ground truth.** "Unsupported" means no evidence was found or evidence contradicts — it does not prove the claim is false, only that it isn't currently well-evidenced.
- **Quality depends on search coverage** — the same database-coverage gaps flagged in `core/literature-review` (English/Global-North skew) apply here too; a claim about Brazil-specific data may need composing with local sources (IBGE, SciELO) this skill's default search tools don't reach on their own.
- **Does not adjudicate genuinely contested claims** where legitimate sources disagree — surfaces the disagreement explicitly rather than picking a side (Constitution, Principle 6).
