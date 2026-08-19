---
name: geographic-research
description: Scope a geography research question before any analysis begins -- determine the right scale, branch (physical/human/integrated), method family, and data sources. Use when the researcher has a geography question and needs it framed rigorously before diving into data or literature.
allowed-tools: Read, Write

skill_id: "geography/geographic-research"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Clifford, Cope, Gillespie & French (2023) — Key Methods in Geography, 4th ed. (Sage): the standard reference for qualitative, quantitative, and spatial methods spanning physical and human geography."
  - "Kitchin & Tate — Conducting Research in Human Geography: Theory, Methodology and Practice (Routledge): the end-to-end research process, from framing a question through positionality to presenting findings."
input_schema:
  required:
    - field: "research_question"
      type: "string"
      description: "The question or topic as the researcher first states it -- often too broad or too vague to act on directly."
  optional:
    - field: "geographic_scope"
      type: "string"
      description: "Region or scale already in mind (e.g. 'North and Northeast Brazil', 'a single municipality', 'global')."
    - field: "time_period"
      type: "string"
      description: "Historical window, if relevant."
    - field: "discipline_branch"
      type: "string"
      description: "If already known: human, physical, or integrated (spanning both)."
    - field: "available_data_sources"
      type: "string"
      description: "Any data sources the researcher already has access to or is required to use."
output_schema:
  fields:
    - field: "scoped_question"
      type: "string"
      description: "The research question rewritten with an explicit scale and boundary."
    - field: "scale_and_boundary_rationale"
      type: "string"
      description: "Why this scale/boundary was chosen and what changes if it were drawn differently (MAUP risk)."
    - field: "branch_classification"
      type: "string"
      description: "human / physical / integrated, with justification."
    - field: "method_recommendation"
      type: "string"
      description: "Qualitative, quantitative, spatial/GIS, or mixed -- and why."
    - field: "data_source_plan"
      type: "array"
      description: "Candidate sources, prioritized, flagging known coverage gaps."
    - field: "next_skills"
      type: "array"
      description: "Which other skills this composes with next (see chains_well_with)."
chains_well_with:
  - "core/literature-review"
  - "core/source-verification"
  - "geography/spatial-analysis"
  - "geography/human-geography"
  - "geography/physical-geography"
  - "education/educational-research"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Geographic Research

## What This Skill Does

The front door of the Geography pack. Before any literature review, data pull, or spatial analysis starts, a geography question needs to be scoped: at what scale, within what boundary, in which branch of the discipline, with what method family, and from what data. Skipping this step is the single most common way geography research goes wrong — not from bad data or bad analysis, but from an unexamined choice of scale or boundary that quietly determines the answer before the real work begins. This skill does the scoping; it does not do the analysis itself — it hands off to the right combination of other skills (`next_skills`).

## Evidence Foundation

Clifford, Cope, Gillespie & French (2023) frame geography's methodological breadth as its central challenge: a discipline that spans physical processes (measurable, often quantitative) and human processes (interpretive, often qualitative) needs a scoping step that decides which evidentiary logic applies *before* choosing a method — applying a physical-geography method to a human-geography question (or vice versa) produces answers that look rigorous but answer the wrong kind of question.

Kitchin & Tate's *Conducting Research in Human Geography* establishes two principles this skill operationalizes directly. First, **scale is not neutral**: the same question answered at the municipal, state, and national level can yield different or even contradictory findings — the Modifiable Areal Unit Problem (MAUP), a well-documented artifact of how analysts draw boundaries, not a property of the underlying reality. Second, **positionality matters** in human-geography research: the researcher's own social position shapes what gets noticed and how it gets interpreted, which is not a flaw to eliminate but a factor to make explicit.

## Procedure

1. **Restate the question with an explicit scale.** If `{{geographic_scope}}` was not given, ask: what is the smallest and largest boundary at which this question would still make sense? Flag if the researcher's phrasing implies a scale they haven't stated (e.g. "the Northeast" is a scale choice, not a neutral description).

2. **Classify the branch.** Physical geography questions concern measurable natural processes (climate, terrain, hydrology). Human geography questions concern population, culture, economy, and politics. Many real questions are **integrated** — e.g. how a physical process (drought, terrain) shapes human settlement or agricultural practice. State which one `{{discipline_branch}}` is, or classify it if not given, and justify the classification — this determines which method family is appropriate next.

3. **Recommend a method family.** Physical-geography-leaning questions usually call for quantitative or spatial/GIS methods. Human-geography-leaning questions often call for qualitative or mixed methods — with positionality made explicit per Kitchin & Tate. Integrated questions typically need a mixed-methods plan combining both.

4. **Name candidate data sources, prioritized.** For Brazil-focused topics, prioritize IBGE (demographic and territorial data), INPE (remote sensing/environmental), and SciELO (Portuguese-language academic literature) before defaulting to English-language-only sources — see Known Limitations on this exact gap in `core/literature-review`. Flag any source with known coverage gaps for the stated scope.

5. **Note the MAUP risk explicitly.** State what would change about the likely findings if the boundary were drawn one level up or one level down. This isn't optional — it's the single highest-leverage caveat in scale-based geography research.

6. **Hand off.** Output `next_skills`: which skill(s) should run next given the branch and method chosen (e.g. `geography/spatial-analysis` for a quantitative/spatial question, `core/literature-review` to ground the question in existing research first, `geography/human-geography` for a qualitative human-geography question).

## Example

**Input:** `research_question: "Verifique os índices de crescimento vegetativo das regiões Norte e Nordeste entre 1980–2020, por faixa etária."` *(Check the vegetative-growth indices for Brazil's North and Northeast regions between 1980–2020, by age bracket.)*

**Output:**

- **Scoped question:** Natural population growth (births minus deaths, excluding migration) in Brazil's North and Northeast macro-regions, 1980–2020, disaggregated by age bracket — a demographic/human-geography question at the macro-region scale.
- **Scale and boundary rationale:** "Região Norte" and "Região Nordeste" are IBGE's own macro-region boundaries — a defensible, institutionally standard choice, not an arbitrary one. Flag: results at the state level within each region would likely show substantial internal variation this macro-region view will average out (MAUP) — worth a follow-up at state scale if the finding needs to inform a specific local claim.
- **Branch classification:** Human geography (demography) — no physical-process variable in the question as stated.
- **Method recommendation:** Quantitative, time-series demographic analysis. No qualitative or GIS component needed unless the researcher wants to visualize the result spatially.
- **Data source plan:** IBGE (Censo Demográfico, SIDRA time series) as the primary and authoritative source for this exact statistic; cross-check totals against DataSUS for the vital-statistics (birth/death) components underlying "crescimento vegetativo."
- **Next skills:** none from Geography needed beyond this scoping — hand off directly to a quantitative-analysis skill (not yet built) to compute and chart the series, then to `core/academic-writing` (not yet built) to draft the finding.

## Known Limitations

- **This skill scopes; it doesn't analyze.** It will not compute a statistic, run a spatial model, or read a dataset — it decides what should happen next and by which skill.
- **MAUP has no clean fix, only disclosure.** Naming the scale sensitivity is the best this skill can do; it cannot tell the researcher the "correct" scale, because there often isn't one independent of the question being asked.
- **Data-source recommendations reflect Brazil-context knowledge as of this skill's authoring** and will go stale — source availability and access terms for IBGE/INPE/SciELO-equivalent institutions in other countries need to be researched fresh per project, not assumed from this list.
- **Positionality guidance is a prompt, not a substitute for the researcher's own reflection.** This skill can ask the question; it cannot answer who the researcher is or how that shapes their interpretation — that judgment stays with the human (Constitution, Principle 6).
