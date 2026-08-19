---
name: political-geography
description: Analyze how political power, territory, borders, and the state relate to geographic space. Use for questions about territorial disputes, administrative boundaries, electoral geography, or state power expressed spatially.
allowed-tools: Read, Write

skill_id: "geography/political-geography"
domain: "geography"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Cox, K.R. (2002) — Political Geography: Territory, State and Society (Wiley-Blackwell): the standard framework for territoriality, state power, and identity politics in geographic context."
input_schema:
  required:
    - field: "scoped_question"
      type: "string"
      description: "The scoped political-geography question."
  optional:
    - field: "territorial_scale"
      type: "string"
      description: "The scale at which political-geographic power operates for this question -- local, state/provincial, national, or international."
    - field: "historical_context"
      type: "string"
      description: "Relevant history shaping current territorial/political arrangements, if known."
output_schema:
  fields:
    - field: "territoriality_analysis"
      type: "string"
      description: "How territory is being claimed, contested, or administered in this case, and by which actors."
    - field: "scale_of_power"
      type: "string"
      description: "Which level(s) of political authority are actually relevant -- a common source of confusion in political-geography questions."
    - field: "normative_framing_check"
      type: "string"
      description: "Whether the question's framing carries unstated assumptions about legitimacy or sovereignty that should be made explicit."
chains_well_with:
  - "geography/geographic-research"
  - "geography/human-geography"
  - "geography/economic-geography"
  - "core/source-verification"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Political Geography

## What This Skill Does

Analyzes how political power and territory intersect spatially — administrative boundaries, contested borders, electoral geography, or the spatial expression of state authority. Political-geography questions carry a specific risk other geography subfields don't: territorial claims are rarely neutral, and a framing that seems purely descriptive ("the border between X and Y") can silently encode a contested political position. This skill's job includes surfacing that risk, not just answering the surface question.

## Evidence Foundation

Cox (2002) frames political geography around territoriality — the strategy of controlling people and resources by controlling geographic area — and establishes that territorial arrangements are historically produced and often actively contested, not natural or fixed. His framework distinguishes the *state* (a territorially bounded political institution) from the *nation* (a claimed community, not always territorially coincident with a state's borders) — conflating the two is a common source of confused political-geography analysis. Cox also emphasizes that political-geographic questions operate at multiple, often mismatched scales simultaneously: a local land-use dispute, a state-level administrative boundary, and a national or international sovereignty claim can all be present in what looks like a single question, and analysis that picks only one scale can miss what's actually at stake.

## Procedure

1. **Identify the actors making or contesting a territorial claim**, and at what scale each operates — a municipality, a state, a national government, an international body.
2. **Distinguish state from nation where relevant.** A question about "who controls this territory" (state) is different from "whose homeland is this" (nation) — conflating them produces analysis that answers the wrong question.
3. **Check whether the question's own framing carries an unstated normative assumption** — e.g. describing a boundary using only one claimant's terminology already takes a position. Name this explicitly rather than silently adopting or avoiding it.
4. **State the scale(s) of power actually relevant**, since political-geography questions frequently involve mismatched scales (a local dispute with national-level stakes, or vice versa).
5. **Ground claims in verifiable sources** — territorial and political claims are exactly the kind of statement that needs `core/source-verification`, not assertion.

## Example

**Input:** `scoped_question`: "How are Brazilian state (estado) administrative boundaries used in education-policy planning, and does this scale match how education needs actually vary geographically?"

**Output:** Territoriality analysis: Brazilian states are administrative/political units with real fiscal and policy authority over education (not just descriptive geography) — this is a state-territoriality question, not a nation/identity question. Scale of power: state-level for most education-policy authority in Brazil, but municipal-level for direct school administration in many cases — flag this two-level structure explicitly, since a policy question framed only at state scale may miss the municipal level where implementation actually happens. Normative framing check: none flagged — administrative boundaries are not contested territory in this case, unlike an international border example would require.

## Known Limitations

- **This skill is not equipped to adjudicate contested sovereignty claims** — it can name that a claim is contested and by whom, per verifiable sources, but taking a position on a live territorial dispute is outside what any Seer skill should do (Constitution, Principle 6 — human judgment stays central, especially here).
- **Requires composing with `core/source-verification`** for any factual territorial claim — political geography is an area where unverified claims carry unusually high stakes.
- **Scale mismatches are easy to miss** — a question phrased at one scale (national) may actually be governed by decisions made at another (municipal), and this skill's diagnosis is only as good as the researcher's own knowledge of which institutions actually hold the relevant authority.
