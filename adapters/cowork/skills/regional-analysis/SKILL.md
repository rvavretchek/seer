---
name: regional-analysis
description: Synthesize findings from other geography skills (spatial, human, physical, political, economic) into a coherent regional profile or comparison. Use when a research question needs the full picture of a region, or when comparing two or more regions.
allowed-tools: Read, Write

skill_id: "geography/regional-analysis"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Clifford, Cope, Gillespie & French (2023) — Key Methods in Geography, 4th ed. (Sage): regional geography and synthesis methods."
  - "Kitchin & Tate — Conducting Research in Human Geography: Theory, Methodology and Practice (Routledge): synthesis and presentation of multi-method findings."
input_schema:
  required:
    - field: "region_definition"
      type: "string"
      description: "The region(s) under analysis, with their boundary basis stated explicitly (administrative, physical, or functional)."
    - field: "component_findings"
      type: "string"
      description: "Findings already produced by other geography skills (spatial-analysis, human-geography, physical-geography, political-geography, economic-geography) to be synthesized."
  optional:
    - field: "comparison_regions"
      type: "string"
      description: "One or more other regions to compare against, if this is a comparative analysis."
output_schema:
  fields:
    - field: "regional_profile"
      type: "string"
      description: "The synthesized account of the region across whichever dimensions (physical, human, political, economic) were analyzed."
    - field: "cross_dimension_tensions"
      type: "array"
      description: "Places where findings from different geography skills point in different directions or need reconciling, rather than being silently smoothed over."
    - field: "comparison_summary"
      type: "string"
      description: "If comparison_regions was given: what genuinely differs and what is similar, avoiding false equivalence between regions of very different scale or context."
chains_well_with:
  - "geography/geographic-research"
  - "geography/human-geography"
  - "geography/physical-geography"
  - "geography/political-geography"
  - "geography/economic-geography"
  - "core/academic-writing"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Regional Analysis

## What This Skill Does

The synthesis skill of the Geography pack — takes findings already produced by other geography skills (spatial, human, physical, political, economic) about a region and combines them into a coherent regional profile, or compares two or more regions on a like-for-like basis. This is not a skill that generates new primary findings; it is where the Geography pack's division of labor comes back together, and its main discipline is refusing to let genuinely conflicting findings get silently smoothed into a falsely tidy narrative.

## Evidence Foundation

Clifford et al. (2023) treat regional geography as inherently synthetic — the point of a regional study is precisely that physical, human, political, and economic dimensions interact within a bounded area, and a regional account that only reports one dimension misses what makes regional analysis distinct from single-topic geography. Kitchin & Tate note that synthesizing multi-method findings (quantitative pattern, qualitative interpretation, historical context) into a single coherent account is itself a skilled task with a documented failure mode: the temptation to resolve every tension into a single clean narrative, when an honest regional account sometimes has to report that the economic-geography finding and the political-geography finding point in different directions, and both are real.

## Procedure

1. **Confirm the region's boundary basis explicitly** — administrative (state, municipality), physical (a watershed, a biome), or functional (a labor-market or trade area) — since component findings from different geography skills may have used different boundary logics that need reconciling before synthesis.
2. **Assemble the component findings** from whichever geography skills already ran (spatial-analysis, human-geography, physical-geography, political-geography, economic-geography) — this skill does not re-derive them.
3. **Look explicitly for cross-dimension tensions** before writing the synthesis — does the economic-geography finding about a region's development trajectory sit comfortably with the human-geography finding about its demographic pattern, or is there a genuine tension worth naming rather than hiding?
4. **Write the regional profile** organized by dimension, with explicit cross-references where dimensions interact (e.g. "the physical-geography finding on land-cover change directly informs the economic-geography finding on agricultural expansion above").
5. **If comparing regions, check for false equivalence.** Two regions compared on the same metric can be misleading if they differ substantially in scale, population, or context — state those differences before presenting the comparison, not after.

## Example

**Input:** `region_definition`: "Brazil's North and Northeast macro-regions (IBGE administrative definition)." `component_findings`: spatial-analysis found clustered natural-growth-rate patterns within the Northeast; human-geography found the pattern likely relates to fertility-education-urbanization linkages; economic-geography found regional infrastructure-investment inequality tied to municipal tax base.

**Output:** Regional profile synthesizing all three: demographic growth pattern (spatial/human) sits within a broader economic-geography context of uneven infrastructure investment — the same municipalities showing higher natural growth may also be the ones with historically lower education infrastructure investment, which is itself a testable follow-up question, not yet confirmed here. **Cross-dimension tension flagged:** the human-geography finding attributes the growth pattern partly to education-access differentials, while the economic-geography finding attributes infrastructure gaps to fiscal structure rather than population size — these are compatible, not contradictory, but the synthesis should state both mechanisms rather than picking one as "the" explanation.

## Known Limitations

- **Only as good as its component findings.** This skill cannot correct or verify what `geography/human-geography`, `geography/economic-geography`, etc. already produced — garbage in the components produces garbage in the synthesis.
- **The temptation to over-synthesize is real and this skill's main failure mode.** A regional profile that resolves every tension into one clean story is often less honest than one that reports an unresolved tension explicitly.
- **Regional boundaries chosen for administrative convenience (e.g. IBGE macro-regions) may not match the boundary that best explains the phenomenon being studied** — this is the same MAUP concern `geography/geographic-research` raises at the scoping stage, and it doesn't go away at the synthesis stage.
