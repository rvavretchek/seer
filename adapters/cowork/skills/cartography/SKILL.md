---
name: cartography
description: Design a map that communicates a specific geographic finding clearly -- choosing projection, classification scheme, and symbology to fit the data and the audience. Use when a finding needs to be shown on a map, not just described in text.
allowed-tools: Read, Write

skill_id: "geography/cartography"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Kent & Vujakovic (eds.) — The Routledge Handbook of Mapping and Cartography: the standard reference for cartographic design principles and classification schemes."
  - "MacEachren (1994) — visualization cube framework: distinguishes maps made to present a known finding (public, low-interaction) from maps made to explore data (private, high-interaction) -- the two have different design rules."
input_schema:
  required:
    - field: "finding"
      type: "string"
      description: "The specific geographic finding or pattern the map needs to communicate."
    - field: "data_type"
      type: "string"
      description: "What kind of data is being mapped -- a continuous variable by region (choropleth candidate), discrete events (point map candidate), flows, or a network."
  optional:
    - field: "audience"
      type: "string"
      description: "Who will read the map -- a specialist reader or a general one; this determines how much can be assumed."
output_schema:
  fields:
    - field: "map_type_recommendation"
      type: "string"
      description: "Choropleth, proportional symbol, dot-density, isoline, or flow map, with justification."
    - field: "classification_scheme"
      type: "string"
      description: "For choropleth maps: equal interval, quantile, natural breaks, or standard deviation -- and why that choice avoids misleading the reader."
    - field: "design_cautions"
      type: "array"
      description: "Specific ways this exact map could mislead if built carelessly."
chains_well_with:
  - "geography/spatial-analysis"
  - "geography/gis"
  - "core/academic-writing"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Cartography

## What This Skill Does

Chooses the right map type and design for a specific finding and audience — a map is an argument, not a neutral picture, and the same data mapped two different ways can suggest two different conclusions. This skill exists because the most common cartographic failure isn't bad drawing, it's an unexamined default: choropleth maps with a poorly chosen classification scheme are the single most frequent way researchers unintentionally mislead readers about geographic patterns.

## Evidence Foundation

MacEachren's (1994) visualization framework distinguishes maps made to *present* an already-known finding to others (public, low-interaction, should minimize ambiguity) from maps made to *explore* data privately in search of a pattern (high-interaction, can tolerate more complexity) — these call for different design choices, and conflating them is a common error (an exploratory map, full of detail meant for the researcher's own eyes, gets published as-is and confuses the reader). Kent & Vujakovic's *Routledge Handbook of Mapping and Cartography* documents that classification scheme choice for choropleth maps is not a neutral technical detail: equal-interval classification can hide clustering that quantile classification would reveal, and natural-breaks (Jenks) classification can visually manufacture a pattern that doesn't reflect the underlying distribution's true shape. The choice must be justified by the data's actual distribution, not defaulted to whatever the mapping software offers first.

## Procedure

1. **Identify the finding's shape**, not just its topic. A continuous variable varying smoothly by region → choropleth. A count of discrete events → proportional symbols or dot density (a choropleth of counts, without normalizing by area/population, is a common and serious error). Movement between places → flow map. A boundary or threshold → isoline.
2. **For choropleth maps, check the data's actual distribution before picking a classification scheme.** Skewed data poorly served by equal intervals; clustered data poorly served by quantiles that force equal counts per class regardless of natural groupings.
3. **Normalize before mapping, when the variable requires it.** Raw counts by region (population, cases) almost always need to be shown as a rate or density, not a raw total — larger regions will otherwise dominate the map regardless of the actual pattern.
4. **State design cautions specific to this map** — not generic advice, but "this classification scheme will visually merge the two highest-growth states into the same color band, understating the contrast the underlying data actually shows."
5. **Match complexity to audience.** A specialist reader can handle a bivariate choropleth or a map with many classes; a general audience needs fewer classes and a clearer legend.

## Example

**Input:** `finding`: "Natural population growth rate by state, North and Northeast Brazil, 2020." `data_type`: "continuous variable (rate) by region — choropleth candidate."

**Output:** Map type: choropleth (correct — the variable is already a rate, not a raw count, so no normalization step is needed). Classification: natural breaks (Jenks) recommended over equal interval, since growth rates likely cluster rather than distribute evenly across the range — check the actual distribution before finalizing. Design caution: with only two macro-regions' states shown, a 5-class scheme will likely leave some classes with only one state — consider 3-4 classes instead, and state explicitly in the caption that this is state-level data (not municipality-level), so a reader doesn't over-read within-state homogeneity that isn't actually shown.

## Known Limitations

- **This skill plans the map's design; it does not render it.** Hands off to a GIS tool (`geography/gis`) or plotting library for actual production.
- **Classification-scheme advice depends on the data's real distribution**, which this skill cannot see without the actual dataset — it can name the right question to ask, not answer it blind.
- **Colorblind-safe and print-safe palette selection is a real, separate design concern** not covered here in depth — flag it as a follow-up when the map is intended for publication.
