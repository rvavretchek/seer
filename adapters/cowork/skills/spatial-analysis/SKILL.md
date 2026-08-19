---
name: spatial-analysis
description: Analyze spatial patterns, relationships, and processes in geographic data -- point patterns, spatial autocorrelation, clustering -- with explicit attention to scale sensitivity. Use once geographic-research has scoped a quantitative or spatial question and it's time to actually analyze the data.
allowed-tools: Read, Write, Bash

skill_id: "geography/spatial-analysis"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "O'Sullivan & Unwin (2010, 2nd ed.) — Geographic Information Analysis (Wiley): the standard reference for point-pattern analysis, spatial autocorrelation (Moran's I), and area-data statistics."
  - "Clifford, Cope, Gillespie & French (2023) — Key Methods in Geography, 4th ed. (Sage): quantitative and spatial methods chapters."
input_schema:
  required:
    - field: "scoped_question"
      type: "string"
      description: "The already-scoped question, ideally the output of geography/geographic-research."
    - field: "data_description"
      type: "string"
      description: "What spatial data is available -- points, areas (polygons), or continuous fields; what variable is being analyzed."
  optional:
    - field: "boundary_definition"
      type: "string"
      description: "How the analysis units (regions, grid cells) were drawn."
output_schema:
  fields:
    - field: "pattern_diagnosis"
      type: "string"
      description: "Whether the pattern is clustered, dispersed, or random, and by which test."
    - field: "scale_sensitivity_check"
      type: "string"
      description: "Whether the result would change under a different boundary definition (MAUP)."
    - field: "interpretation_caveats"
      type: "array"
      description: "What the statistical pattern does and does not imply."
chains_well_with:
  - "geography/geographic-research"
  - "geography/gis"
  - "geography/regional-analysis"
  - "core/citation-analysis"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Spatial Analysis

## What This Skill Does

Analyzes the spatial pattern in a dataset that has already been scoped by `geography/geographic-research` — is a phenomenon clustered, dispersed, or randomly distributed across space, and is that pattern statistically real or an artifact of how the boundaries were drawn? This skill exists because spatial data breaks a core assumption of ordinary statistics: observations that are close together in space tend to be more similar than observations far apart (spatial autocorrelation) — treating spatial data as if observations were independent produces confidently wrong conclusions.

## Evidence Foundation

O'Sullivan & Unwin (2010) establish spatial autocorrelation as the central fact any spatial analysis must confront: Tobler's First Law of Geography ("everything is related to everything else, but near things are more related than distant things") is not a nuisance to be corrected away — it is the object of study. Point-pattern analysis (nearest-neighbor statistics, quadrat counts) tests whether a distribution of events is more clustered or more dispersed than random chance would produce. Moran's I and related area-data statistics test the same question for data already aggregated into regions. Clifford et al. (2023) reinforce that the choice of spatial method must follow from the data type (points, areas, continuous fields) and the research question set during scoping — not the reverse.

## Procedure

1. **Confirm the scoped question and data type.** Points (discrete events), areas (data aggregated by region), or continuous fields (e.g. temperature surfaces) call for different tests — do not proceed without knowing which.
2. **Choose the appropriate pattern test.** Point data: nearest-neighbor or quadrat analysis. Area data: Moran's I or local indicators of spatial association (LISA). State the test and why it fits the data type.
3. **Run the diagnosis.** Report whether the pattern is significantly clustered, significantly dispersed, or not distinguishable from random, with the statistic and its significance.
4. **Run the scale-sensitivity check.** State explicitly: if the analysis units were redrawn at a different scale (state instead of municipality, 1km grid instead of 5km grid), would the result likely hold? This directly operationalizes the MAUP caveat `geography/geographic-research` flags at the scoping stage — don't let it go unchecked here.
5. **State interpretation caveats.** A statistically significant cluster is a pattern, not an explanation — it says *where*, not *why*. Explaining why requires composing with a human- or physical-geography skill, or a causal/qualitative method, not this one.

## Example

**Input:** Following `geography/geographic-research`'s scoping of Sônia's demographic question, a follow-up: does natural population growth cluster geographically within the Northeast region, or is it evenly spread across states?

**Output:** Moran's I computed on state-level natural growth rates shows significant positive spatial autocorrelation (clustering) — high-growth states are adjacent to other high-growth states more often than chance would predict. **Scale-sensitivity check:** re-running at the municipality level would very likely reveal within-state heterogeneity this state-level view averages out — flagged as a follow-up, not run here. **Interpretation caveat:** clustering tells us *where* growth is concentrated, not *why* — that requires a human-geography or demographic-economic explanation, composed separately.

## Known Limitations

- **Detects pattern, not cause.** A cluster is a description of the data's geometry, not an explanation. Composing with `geography/human-geography` or `geography/economic-geography` is usually the next step, not optional.
- **MAUP has no clean fix.** This skill can flag scale sensitivity; it cannot determine the "true" scale, because spatial processes often operate at multiple scales simultaneously.
- **Requires genuinely spatial data with defined coordinates or boundaries.** A dataset with only regional labels and no boundary geometry needs `geography/gis` first to establish the spatial reference before this skill can run.
