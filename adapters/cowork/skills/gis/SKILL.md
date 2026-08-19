---
name: gis
description: Plan and structure a GIS (Geographic Information Systems) workflow -- what layers, projections, and operations are needed to answer a spatial question, and which tool (QGIS, geemap, etc.) fits. Use when a question needs mapping, spatial joins, or geoprocessing, not just statistical spatial analysis.
allowed-tools: Read, Write, Bash

skill_id: "geography/gis"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "O'Sullivan & Unwin (2010, 2nd ed.) — Geographic Information Analysis (Wiley): the vector/raster data model distinctions and geoprocessing logic this skill's planning step follows."
  - "Clifford, Cope, Gillespie & French (2023) — Key Methods in Geography, 4th ed. (Sage): GIS and remote-sensing methods chapters."
input_schema:
  required:
    - field: "scoped_question"
      type: "string"
      description: "The scoped question this GIS workflow needs to answer."
    - field: "available_layers"
      type: "string"
      description: "What geographic data layers exist or are obtainable (administrative boundaries, land use, points of interest, imagery, etc.)."
  optional:
    - field: "target_output"
      type: "string"
      description: "What the final artifact should be -- a map, a joined dataset, a statistic derived from spatial overlay."
output_schema:
  fields:
    - field: "data_model_plan"
      type: "string"
      description: "Vector or raster, and which layers are needed, with projection/CRS considerations."
    - field: "operation_sequence"
      type: "array"
      description: "The ordered geoprocessing steps (e.g. reproject, clip, buffer, spatial join, overlay)."
    - field: "tool_recommendation"
      type: "string"
      description: "Which real tool fits -- QGIS for desktop GIS work, a Python geospatial stack (geopandas/rasterio) for scripted/reproducible pipelines, or a GeoAgent/QGIS-plugin-style connector for conversational use."
chains_well_with:
  - "geography/geographic-research"
  - "geography/spatial-analysis"
  - "geography/cartography"
license: "CC BY-SA 4.0"
provenance: "original"
---

# GIS

## What This Skill Does

Plans a GIS workflow — the data layers, coordinate reference system, and sequence of geoprocessing operations needed to answer a spatial question — before any tool gets opened. This skill does not run the GIS software itself; it produces the operation plan a human (or a tool-execution layer, such as a `GeoAgent`/QGIS-plugin connector) then carries out. Seer deliberately does not fork any GIS *tool* — `opengeos/GeoAgent` already provides a real, actively maintained connector layer to QGIS and Python geospatial libraries (see `vendor/PROVENANCE.md`); this skill's job is deciding *what* to ask that connector to do.

## Evidence Foundation

O'Sullivan & Unwin (2010) establish the foundational GIS distinction this skill's planning step is built on: **vector data** (points, lines, polygons — discrete features with attributes) versus **raster data** (continuous grids — imagery, elevation, climate surfaces). Choosing the wrong model for the question — e.g. treating a continuous field like temperature as discrete points — produces geoprocessing that runs without error but answers the wrong question. Reprojection (matching every layer to a common coordinate reference system before any overlay) is a documented, common failure point: overlaying layers in mismatched projections silently produces measurements that are wrong, not obviously wrong.

## Procedure

1. **Classify each available layer as vector or raster**, and identify the operations that follow from that (vector: buffer, clip, spatial join, dissolve; raster: reclassify, zonal statistics, map algebra).
2. **Check coordinate reference systems (CRS).** Flag if layers are in different projections — this must be resolved before any spatial operation, not after.
3. **Sequence the operations** needed to reach `target_output` from `available_layers`, in order, naming each geoprocessing step explicitly (not "process the data" — "clip administrative boundaries to the study region, then spatial-join point-of-interest data to the clipped regions").
4. **Recommend the execution tool.** QGIS for interactive/desktop work a human will drive directly; a Python geospatial stack (geopandas, rasterio) for a reproducible, scriptable pipeline; a conversational connector (e.g. GeoAgent/OpenGeoAgent) when the researcher wants to describe the task in natural language rather than run code or click through a GUI — the right choice for Sônia's zero-CLI floor.
5. **Flag data-availability gaps** explicitly rather than assuming a layer exists — Brazilian administrative boundaries and land-use layers are available from IBGE and INPE, but not every layer a researcher wants exists at the resolution or currency needed.

## Example

**Input:** `scoped_question`: "Where has agricultural land use expanded into forested areas in a given Northeast Brazil municipality between 2000 and 2020?" `available_layers`: "INPE land-use/land-cover raster time series; IBGE municipal boundary vector."

**Output:** Data model plan — raster (land-cover classification) clipped by a vector boundary. Operation sequence: (1) reproject both layers to a common CRS (SIRGAS 2000, Brazil's standard); (2) clip the land-cover rasters to the municipal boundary for 2000 and 2020; (3) reclassify both rasters into a simplified forest/agriculture/other scheme; (4) compute a change-detection raster (2020 minus 2000 classification); (5) compute zonal statistics to quantify hectares changed. Tool recommendation: Python geospatial stack for reproducibility across the full time series, or a GeoAgent-style connector if the researcher wants to drive this conversationally rather than review code.

## Known Limitations

- **This skill plans; it does not execute.** It has no access to actual geospatial data or a GIS engine — it hands off to a tool (QGIS, a Python stack, or a connector like GeoAgent) that does.
- **Data availability assumptions need per-project verification.** Layer names, resolutions, and update frequency for IBGE/INPE-equivalent sources in other countries were not verified here and go stale — check at execution time, not from this skill's memory.
- **CRS mismatches are the most common real-world failure mode in GIS work** and are easy to miss visually (misaligned layers can look "close enough" on screen while being systematically offset) — this skill flags the check but cannot verify actual data without running the tool.
