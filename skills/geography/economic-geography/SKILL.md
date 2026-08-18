---
name: economic-geography
description: Analyze how economic activity -- production, trade, labor, investment -- is distributed across and shapes geographic space. Use for questions about regional development, industry location, trade patterns, or economic inequality expressed geographically.
allowed-tools: Read, Write

skill_id: "geography/economic-geography"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Coe, Kelly & Yeung (2020, 3rd ed.) — Economic Geography: A Contemporary Introduction (Wiley-Blackwell): the standard framework for spatial analysis of production networks, uneven development, and regional economies."
input_schema:
  required:
    - field: "scoped_question"
      type: "string"
      description: "The scoped economic-geography question."
  optional:
    - field: "available_data"
      type: "string"
      description: "Economic indicators available -- GDP/income by region, employment data, trade flows, firm location data."
output_schema:
  fields:
    - field: "spatial_economic_pattern"
      type: "string"
      description: "How the economic activity/outcome is distributed geographically."
    - field: "uneven_development_check"
      type: "string"
      description: "Whether the pattern reflects known structural drivers of regional inequality, or needs further investigation to explain."
    - field: "scale_of_analysis"
      type: "string"
      description: "Local, regional, national, or global -- economic-geography explanations often require a different scale than the one initially stated."
chains_well_with:
  - "geography/geographic-research"
  - "geography/human-geography"
  - "geography/political-geography"
  - "geography/spatial-analysis"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Economic Geography

## What This Skill Does

Analyzes how economic activity — production, trade, employment, investment — is distributed geographically and why some regions develop differently than others. Economic-geography questions are a common bridge point for Sônia's Geography Education work: regional inequality, industry location, and development patterns are frequently the underlying "why" behind a demographic or educational-access pattern observed elsewhere in the Geography or Education packs.

## Evidence Foundation

Coe, Kelly & Yeung (2020) frame economic geography around the insight that economic activity is never spatially neutral: firms locate where they do for reasons tied to labor cost, infrastructure, agglomeration effects (firms clustering near other firms in the same industry), and historical path-dependency — not simply "wherever is most efficient" in the abstract. This produces **uneven development**: regional economic inequality is not a random or purely natural outcome but a structural pattern with identifiable drivers (colonial-era infrastructure investment, resource extraction geography, transport-network history, policy choices) that persist and compound over time. A key methodological point: economic-geography explanations frequently require examining a *different* scale than the one the question was originally posed at — a municipal income gap may only make sense in light of state- or national-level investment history.

## Procedure

1. **Map the economic pattern spatially** — where is the activity/outcome concentrated, and at what scale is that concentration meaningful?
2. **Check for known structural drivers before assuming a novel explanation.** Uneven development in most regions has a documented history (infrastructure investment patterns, resource geography, historical trade routes, policy legacies) — check whether the pattern observed matches known drivers before proposing a new one.
3. **State the scale mismatch explicitly when present.** If the question is posed at municipal scale but the real driver operates at state or national scale (e.g. federal infrastructure investment history), say so — this is often the single most important move in economic-geography analysis.
4. **Distinguish correlation from the actual causal mechanism.** A region being poorer and having less school infrastructure are correlated; economic geography's job is naming the mechanism connecting them (tax-base dependency on local income, historical investment patterns), not just noting the correlation.

## Example

**Input:** `scoped_question`: "Why does educational infrastructure investment vary so much between municipalities within the same Northeast Brazilian state?"

**Output:** Spatial economic pattern: educational infrastructure investment likely correlates with municipal tax base, which correlates with local economic activity — a plausible mechanism, not yet confirmed for this specific case. Uneven-development check: this pattern matches a well-documented structural driver in economic geography — municipal-level public-service funding tied to local tax base produces persistent regional inequality independent of state-level policy intent, because poorer municipalities cannot raise equivalent local revenue even under identical formal policy. Scale of analysis: the real explanatory scale may be state-level fiscal transfer policy (does the state redistribute revenue to compensate poorer municipalities, or not?), not purely municipal — flag this as the next question to check before concluding the pattern is simply "some municipalities invest more."

## Known Limitations

- **Uneven-development explanations can become deterministic if applied uncritically** — a known structural driver being *plausible* is not the same as it being *confirmed* for the specific case; state findings as hypotheses pending verification, not settled conclusions.
- **Requires real economic data to move past pattern description into mechanism** — without income, tax-base, or investment data, this skill can state the expected mechanism from the literature but cannot confirm it applies here.
- **Scale-mismatch diagnosis depends on knowing the relevant institutional/fiscal structure**, which varies by country and needs verification per project, not assumed from this skill's general framework.
