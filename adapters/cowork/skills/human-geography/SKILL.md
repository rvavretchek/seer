---
name: human-geography
description: Analyze how population, culture, economy, or social structure vary across and shape space -- with explicit attention to researcher positionality. Use for questions about people, settlement, migration, or social patterns in geographic context.
allowed-tools: Read, Write

skill_id: "geography/human-geography"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Kitchin & Tate — Conducting Research in Human Geography: Theory, Methodology and Practice (Routledge): positionality, qualitative/mixed-methods design for human-geography questions."
  - "Clifford, Cope, Gillespie & French (2023) — Key Methods in Geography, 4th ed. (Sage): human-geography methods chapters."
input_schema:
  required:
    - field: "scoped_question"
      type: "string"
      description: "The scoped human-geography question, ideally from geography/geographic-research."
  optional:
    - field: "researcher_positionality"
      type: "string"
      description: "The researcher's own relevant social position relative to the population studied, if known."
    - field: "available_data"
      type: "string"
      description: "Quantitative data (census, survey), qualitative material (interviews, documents), or both."
output_schema:
  fields:
    - field: "method_plan"
      type: "string"
      description: "Qualitative, quantitative, or mixed, with justification tied to the question type."
    - field: "positionality_note"
      type: "string"
      description: "How the researcher's position may shape what gets noticed or how it's interpreted -- made explicit, not eliminated."
    - field: "interpretation"
      type: "string"
      description: "The substantive finding, framed with its methodological basis."
chains_well_with:
  - "geography/geographic-research"
  - "geography/economic-geography"
  - "geography/political-geography"
  - "education/educational-research"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Human Geography

## What This Skill Does

Analyzes questions about population, migration, settlement, culture, or social structure as they relate to space — how a demographic or social pattern is distributed geographically, and why. Unlike `geography/spatial-analysis` (which tests whether a pattern is statistically real), this skill interprets what a human-geography pattern *means*, which requires engaging with the social and historical context a purely statistical test cannot supply on its own.

## Evidence Foundation

Kitchin & Tate establish that human-geography research sits differently from physical-geography research: the object of study (people, culture, institutions) is itself interpretive, and the researcher's own social position — nationality, class, gender, disciplinary training — shapes what gets noticed and how findings get read. This is not a flaw to eliminate through more rigorous method; it is a factor that responsible human-geography research states explicitly (positionality), so a reader can weigh the interpretation knowing where it came from. Clifford et al. (2023) note human geography's methodological range spans purely quantitative demographic analysis (population pyramids, migration rates) to purely qualitative work (interviews, ethnography) — the right choice depends on whether the question is about *pattern* (often quantitative) or *meaning* (often qualitative or mixed).

## Procedure

1. **Classify the question as pattern-seeking or meaning-seeking** (or both). "How is X distributed?" leans quantitative. "Why do people experience X this way?" leans qualitative. Most real research questions need both, sequenced.
2. **State positionality explicitly when the question involves interpretation of another group's experience.** This is not optional disclosure — Kitchin & Tate treat it as part of the method, because it shapes the reliability and limits of the interpretation offered.
3. **Select data accordingly.** Census/demographic data for pattern questions; interviews, documents, or participatory methods for meaning questions.
4. **Interpret with the social/historical context made explicit** — a demographic pattern (e.g. migration toward a region) needs a causal or contextual account (economic opportunity, environmental pressure, policy change), not just a description of the pattern itself; that account is where this skill's judgment work happens.
5. **Flag where interpretation is contested or uncertain**, rather than presenting one reading as the only possible one — human-geography phenomena are frequently open to more than one defensible interpretation.

## Example

**Input:** `scoped_question`: "Why has natural population growth remained higher in parts of the Northeast than the national average, and what does that mean for regional education planning?"

**Output:** Pattern-and-meaning question, needing both quantitative confirmation (already established via `geography/spatial-analysis`) and qualitative/contextual interpretation. Interpretation must engage documented regional factors — fertility-rate differentials linked to income, education access, and urbanization rates across Brazilian regions — rather than treating the demographic pattern as self-explanatory. **Positionality note:** if the researcher is not from the region studied, that distance is worth naming explicitly when drawing policy implications for local education planning — a Northeast-based researcher and an outside researcher may weight the same data differently, and Sônia's brief-stated research area is Geography *Education*, suggesting the natural next composition is with an education-policy angle, not a purely demographic one.

## Known Limitations

- **This skill interprets; it does not itself run the underlying statistics** — compose with `geography/spatial-analysis` for the quantitative pattern test first.
- **Positionality guidance is a prompt to reflect, not a resolution.** The skill can ask who the researcher is relative to the population studied; it cannot supply that reflection for them (Constitution, Principle 6).
- **Interpretation of social phenomena is frequently contested among researchers themselves** — this skill should surface competing readings when they exist in the literature, not present a single interpretation as settled fact.
