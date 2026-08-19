---
name: physical-geography
description: Analyze natural physical processes -- climate, terrain, hydrology, land cover -- and how they shape or are shaped by geographic space. Use for questions about the physical/environmental side of a geography question, distinct from human/social patterns.
allowed-tools: Read, Write, Bash

skill_id: "geography/physical-geography"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Clifford, Cope, Gillespie & French (2023) — Key Methods in Geography, 4th ed. (Sage): physical-geography methods chapters (climatology, geomorphology, hydrology, remote sensing)."
input_schema:
  required:
    - field: "scoped_question"
      type: "string"
      description: "The scoped physical-geography question, ideally from geography/geographic-research."
  optional:
    - field: "available_data"
      type: "string"
      description: "Remote sensing/satellite data, ground station records, field measurements, or modeled data."
    - field: "time_period"
      type: "string"
      description: "The window relevant to the physical process being studied."
output_schema:
  fields:
    - field: "process_identification"
      type: "string"
      description: "Which physical process(es) the question actually concerns -- climatic, geomorphological, hydrological, or land-cover."
    - field: "data_and_method_plan"
      type: "string"
      description: "What data and analysis method fits, distinguishing measured/observed data from modeled/derived data."
    - field: "human_interaction_flag"
      type: "string"
      description: "Whether and how this physical process interacts with human activity -- flagged for composition with geography/human-geography when relevant."
chains_well_with:
  - "geography/geographic-research"
  - "geography/gis"
  - "geography/spatial-analysis"
  - "geography/human-geography"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Physical Geography

## What This Skill Does

Analyzes the natural-process side of a geography question — climate, terrain, hydrology, land cover — as distinct from the human/social side. Many real research questions are integrated (a physical process shaping human settlement, or human activity altering a physical process), and this skill's job is specifically to handle the physical-process component rigorously and flag explicitly when the question needs to compose with `geography/human-geography` to be complete, rather than silently treating a physical measurement as the whole answer to an integrated question.

## Evidence Foundation

Clifford et al. (2023) treat physical geography's methods as evidence-driven in a different sense than human geography's: climatology, geomorphology, and hydrology rely on measured or remotely sensed physical quantities (temperature, precipitation, elevation, vegetation index) rather than interpretive social data, and the central methodological discipline is distinguishing directly observed/measured data from modeled or derived data (e.g. a satellite-derived vegetation index is a proxy, not a direct measurement of vegetation health, and needs to be treated with the corresponding caution). Physical-geography findings frequently interact with human patterns — climate shaping agriculture, terrain shaping settlement, land-cover change reflecting human land use — and treating a physical-geography result as the complete answer to what is actually an integrated question is a common analytical error this skill exists to prevent.

## Procedure

1. **Identify which physical process(es) the question actually concerns.** Climatic (temperature, precipitation, seasonal patterns), geomorphological (terrain, erosion, landform), hydrological (rivers, groundwater, drainage), or land-cover (vegetation, land use as observed from remote sensing).
2. **Distinguish measured from modeled/derived data explicitly.** A ground weather station reading is measured; a satellite-derived precipitation estimate is modeled and carries its own uncertainty — state which kind of data is being used and its known error characteristics if available.
3. **Analyze the physical process on its own terms first** — trend, magnitude, spatial pattern — before considering any human dimension.
4. **Flag human-interaction explicitly.** If the physical process plausibly shapes or is shaped by human activity (settlement patterns, agriculture, land-use change, migration), state this and route to `geography/human-geography` for that half of the analysis rather than speculating about human causes or effects within this skill.

## Example

**Input:** `scoped_question`: "Has forest cover in a given Northeast Brazil municipality changed over 2000–2020, and does the pattern relate to agricultural expansion?"

**Output:** Process identification: land-cover change (physical) with an explicit human-interaction question built in. Data and method plan: INPE land-cover classification time series (modeled/derived from satellite imagery, not directly measured — flag the classification-accuracy caveat) analyzed via change detection (compose with `geography/gis` for the actual raster operations). Human-interaction flag: the question as stated explicitly asks about agricultural expansion as a driver — this needs composition with `geography/human-geography` and/or `geography/economic-geography` for the land-use-change driver analysis; this skill's output is the physical land-cover change pattern only, not the causal story behind it.

## Known Limitations

- **Remote-sensing-derived data is a proxy, not ground truth.** Classification accuracy varies by sensor, resolution, and land-cover type — a stated finding should note the data's known accuracy limitations, not treat satellite classification as error-free.
- **This skill deliberately stops short of explaining human causes of a physical pattern** — that boundary is intentional (Constitution, Principle 4: composition, not one skill trying to do everything), not an oversight.
- **Physical processes often operate on timescales and cycles longer than typical research-project data windows** — a 20-year land-cover time series may not capture a longer climatic or geomorphological cycle relevant to interpreting the trend correctly.
