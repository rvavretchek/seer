---
name: source-verification
description: Assess whether a source is credible and appropriate to cite -- not whether a specific claim from it is true (that's core/claim-verification). Use when deciding whether a source is trustworthy enough to build an argument on.
allowed-tools: Read, Write, Bash

skill_id: "core/source-verification"
domain: "core"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Blakeslee, S. (2004) — the CRAAP Test (Currency, Relevance, Authority, Accuracy, Purpose), developed at CSU Chico: the standard information-literacy framework for source credibility this skill's assessment criteria follow."
input_schema:
  required:
    - field: "source_description"
      type: "string"
      description: "The source to assess -- a URL, a citation, or a description of where it came from."
  optional:
    - field: "intended_use"
      type: "string"
      description: "What the source would be used to support -- a factual claim, background context, a methodological choice."
output_schema:
  fields:
    - field: "craap_assessment"
      type: "object"
      description: "Per-criterion rating: Currency, Relevance, Authority, Accuracy, Purpose -- each with the specific finding, not just a score."
    - field: "verdict"
      type: "string"
      description: "Whether the source is appropriate for the stated intended_use -- credibility is relative to purpose, not absolute."
    - field: "citation_notes"
      type: "string"
      description: "Any caveat that should accompany the citation if the source is used (e.g. 'cite with the publication date, since currency is a concern')."
chains_well_with:
  - "core/claim-verification"
  - "core/citation-analysis"
  - "core/literature-review"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Source Verification

## What This Skill Does

Assesses whether a source is trustworthy enough to cite, using the CRAAP framework — Currency, Relevance, Authority, Accuracy, Purpose. This is not the same question as `core/claim-verification` ("is this specific statement true"): a source can be broadly credible and still be wrong about one specific thing, and a source can be biased or dated yet still be the right thing to cite for a specific limited purpose (e.g., citing a company's own report as evidence of *what that company claims*, not as neutral fact). Credibility is relative to intended use, not an absolute score.

## Evidence Foundation

Blakeslee's CRAAP test, developed at CSU Chico in 2004 and now a standard information-literacy framework, evaluates five dimensions: **Currency** (when published/updated — matters more for fast-moving topics than for foundational methodology), **Relevance** (does it actually address the question at hand, at the right level), **Authority** (does the author/publisher have real standing on this subject — credentials, institutional affiliation, track record), **Accuracy** (is the information verifiable, well-cited, and free of the kind of errors that suggest carelessness), and **Purpose** (why was this written — to inform, to persuade, to sell — and does that purpose bias the content). The framework's real value is forcing an explicit judgment on each dimension rather than a vague overall "feels credible" impression, which research on information literacy has repeatedly shown is unreliable on its own.

## Procedure

1. **Currency** — when was it published or last updated? For a fast-moving empirical question (recent demographic data, current events), an old source is a real problem even if otherwise excellent. For foundational methodology (a well-established framework), currency matters less.
2. **Relevance** — does the source actually address the question at hand, at an appropriate level of depth for the intended use? A source can be excellent and still be the wrong source for this specific question.
3. **Authority** — who wrote/published it, and what standing do they have on this specific topic? A government statistics agency has authority on its own official data; the same agency may not have authority on an interpretive claim about what that data means.
4. **Accuracy** — can the claims be cross-checked? Are sources cited? Does the source show signs of carelessness (unsourced statistics, internal inconsistencies) that would predict other errors?
5. **Purpose** — why does this source exist? Institutional reports, advocacy publications, and academic papers carry different, sometimes conflicting, purposes that shape what gets emphasized or omitted — name the purpose explicitly rather than treating all sources as equally neutral.
6. **State the verdict relative to `intended_use`**, not in the abstract — the same source can pass for one use and fail for another.

## Example

**Input:** `source_description`: "OECD Family Database, indicator SF1.4 (population by age of children and youth)." `intended_use`: "Support a claim about the global child population trend."

**Output:** Currency: current (regularly updated dataset). Relevance: **fails for this specific use** — the database covers OECD member/enhanced-engagement countries only, not a global population. Authority: high (OECD is a recognized authority on its own member-country statistics). Accuracy: high, methodologically transparent. Purpose: statistical reporting, low bias risk. **Verdict:** not appropriate for a *global* claim as stated — appropriate only for an OECD-country-specific comparison. Citation note: if used, the claim must be reframed to specify "among OECD countries," not "globally" — this is exactly the source-fit error the orchestrator's proof-of-concept run caught for a near-identical request.

## Known Limitations

- **CRAAP is a structured heuristic, not a certainty test.** A source can pass all five criteria and still be wrong about a specific fact — compose with `core/claim-verification` for that.
- **Authority is field-specific and requires real domain knowledge to judge well** — this skill can ask "does this source have standing on this topic," but answering it accurately depends on the researcher's or a subject-matter skill's knowledge of who the credible voices in a field actually are.
- **Purpose assessment risks false even-handedness** — not every source's bias is equally weighted or equally disclosed; a source with an undisclosed conflict of interest will not flag itself, and this skill can only assess what's stated or inferable, not what's hidden.
