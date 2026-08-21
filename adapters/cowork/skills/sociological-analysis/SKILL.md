---
name: sociological-analysis
description: Classify a social phenomenon or research question along sociology's foundational structural/interpretive methodological divide -- and use that classification to recommend the right unit of analysis, method, and data -- before deeper sociological analysis begins. Use when a sociology question needs framing (social fact vs subjective meaning) before choosing how to study it.
allowed-tools: Read, Write

skill_id: "sociology/sociological-analysis"
domain: "sociology"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Durkheim, E. (1895) -- The Rules of Sociological Method: social facts must be studied as external, constraining phenomena -- 'things' observable and comparable independent of any one individual's consciousness of them. The structural/positivist pole of sociology's foundational methodological divide."
  - "Weber, M. (1922, posthumous -- Economy and Society; method set out earlier in his 1904 essay 'Objectivity in Social Science') -- Verstehen and the ideal type: social action must be understood through the subjective meaning the actors themselves attach to it. The interpretive pole of the same divide."
input_schema:
  required:
    - field: "research_question"
      type: "string"
      description: "The sociology question or social phenomenon as first stated."
  optional:
    - field: "unit_of_analysis"
      type: "string"
      description: "If already known: individual, group/network, institution, or whole-society level."
    - field: "available_data"
      type: "string"
      description: "Data the researcher already has or can access -- survey/administrative/register data, interview or ethnographic access, historical/documentary records."
output_schema:
  fields:
    - field: "methodological_classification"
      type: "string"
      description: "Whether the question is best approached as a social fact (external, constraining, comparable across cases) or through Verstehen (the subjective meaning actors attach to their own action), or genuinely needs both -- with justification."
    - field: "unit_of_analysis_check"
      type: "string"
      description: "Which level the question is actually pitched at, flagging any slippage between levels -- e.g. explaining an institutional-level pattern with individual-level data, sociology's version of an ecological-fallacy risk."
    - field: "method_recommendation"
      type: "string"
      description: "Quantitative/comparative (survey, register data, cross-case comparison) or qualitative/interpretive (interview, ethnography, ideal-type construction), or a mixed design -- with reasoning tied to the classification above."
    - field: "reflexivity_note"
      type: "string"
      description: "Where the researcher's own social position may shape what gets noticed or how it's interpreted -- most acute for interpretive work, but not absent from structural work either."
    - field: "next_skills"
      type: "array"
      description: "Which skill(s) this hands off to next, given the classification and method chosen."
chains_well_with:
  - "core/literature-review"
  - "core/source-verification"
  - "political-science/policy-process-analysis"
  - "geography/human-geography"
  - "education/educational-policy"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Sociological Analysis

## What This Skill Does

The front door for a sociology question, in the same spirit as `geography/geographic-research`'s scoping role: before choosing a method or pulling data, a sociological question needs to be classified along the discipline's oldest and still most consequential methodological fault line. Durkheim insisted social facts -- rates, institutions, norms -- exist externally to and constrain any one individual, and should be studied like "things," objectively and comparatively. Weber insisted social action can only be genuinely explained by recovering the subjective meaning the actor attaches to it (*Verstehen*), which a purely external, thing-like observation cannot reach. Neither pole is wrong; they answer different kinds of questions, and picking the wrong one for a given question -- running a structural comparison on a question that's actually about lived meaning, or vice versa -- produces analysis that looks rigorous but answers something other than what was asked. This skill does the classification and handoff; it does not itself run the survey, code the interviews, or build the comparative-historical case.

## Evidence Foundation

Durkheim's *The Rules of Sociological Method* (1895) is the founding text of the structural/positivist tradition: social facts (suicide rates, religious affiliation, division of labor) are to be treated as external and coercive, observable independent of any individual's awareness of them, and explained by other social facts rather than by individual psychology -- the method that makes cross-case, comparative, and eventually quantitative sociology possible. Weber's methodological writing, culminating in *Economy and Society*, argues the opposite starting point is equally necessary for genuinely sociological explanation: social action is meaningful action, and understanding *why* an actor did something requires recovering the meaning they attached to it, not just correlating external variables. Weber's **ideal type** -- a deliberately simplified, internally consistent construct (e.g. "the bureaucracy," "the Protestant ethic") -- is his tool for making interpretive comparison rigorous rather than merely impressionistic. This divide is not resolved by this skill and is not fully resolved by the discipline either -- later work (Bourdieu's habitus, Giddens' structuration theory) attempts to bridge structure and interpretation rather than eliminate the tension, and this skill's job is to name which pole (or genuine mixture) a given question calls for, not to pretend the tension away.

## Procedure

1. **Restate the question and ask what would count as an answer.** A question answerable by a rate, a correlation, or a cross-case comparison ("does neighborhood poverty rate predict school dropout rate?") is pointing toward the structural pole. A question answerable only by recovering how people themselves understand and narrate their situation ("how do long-term unemployed workers make sense of their own status?") is pointing toward the interpretive pole. Many real questions need both, at different stages.
2. **Classify explicitly**, and justify it -- don't leave `methodological_classification` implicit. State which pole the question is pitched at, or state clearly that it needs both, and what each half would contribute.
3. **Check the unit of analysis** against the classification. Structural claims are often pitched at the institutional or societal level (rates, distributions, comparisons across groups or countries) -- verify the available or proposed data is actually at that level, not individual-level data being asked to support an institutional-level claim (or the reverse). This is sociology's version of the ecological-fallacy risk, and it is easy to get wrong silently.
4. **Recommend a method family** tied directly to the classification: structural/comparative questions typically call for survey, administrative/register, or cross-case comparative-historical data and quantitative or systematic comparative methods; interpretive questions typically call for interview, ethnographic, or documentary methods aimed at recovering actors' own meaning-making, often built around Weberian ideal-type comparison. State a mixed design explicitly where the question genuinely needs both, rather than defaulting to whichever method is more convenient.
5. **Flag reflexivity.** For interpretive work especially, the researcher's own social position (class, gender, insider/outsider status relative to the group studied) shapes what gets noticed and how it's read -- name this explicitly rather than let it go unexamined. For structural work, flag the complementary risk Durkheim's critics raised: treating a social fact as a neutral "thing" can itself naturalize or essentialize a pattern that is, on closer interpretive inspection, historically contingent and actively contested by the people living inside it.
6. **Hand off.** State `next_skills` -- which skill(s) should run next given the classification and method (e.g. `core/literature-review` to ground the question in existing findings first, `geography/human-geography` where the question has a strong spatial component, `political-science/policy-process-analysis` where the phenomenon is itself the product of a policy process worth tracing).

## Example

**Input:** `research_question`: "Why do members of a specific religious community in a mid-sized Brazilian city describe long-term unemployment as a test of faith rather than a structural economic failure, even though the surrounding municipality has one of the country's highest unemployment rates?"

**Output (abridged):**

- **Methodological classification:** Genuinely needs both poles, sequenced. The *existence and rate* of high municipal unemployment is a social fact in Durkheim's sense -- external to any individual, measurable, comparable to other municipalities. But the question as asked is really about *why this specific framing* ("test of faith," not "structural failure") is the one the community uses -- that is squarely a Verstehen question about the subjective meaning these actors attach to their own situation, not answerable by the unemployment rate alone.
- **Unit of analysis check:** The structural half is municipal/institutional (comparative unemployment data across municipalities). The interpretive half is individual/group-level (how members narrate their own experience). Flag: a study that pulls only municipal statistics cannot answer the "why this framing" half of the question, and a study that only interviews a handful of community members cannot establish whether the unemployment rate itself is actually unusual -- both halves are needed, not interchangeable.
- **Method recommendation:** Mixed design -- comparative municipal-level unemployment data (structural, quantitative, establishes the "high unemployment rate" premise is real) paired with in-depth interviews or ethnographic fieldwork within the community, read through Weberian ideal-type comparison (e.g. constructing an ideal type of "faith-framed hardship narrative" against which to compare individual accounts).
- **Reflexivity note:** A researcher without the community's own religious background is likely to read "test of faith" as a euphemism or a coping mechanism obscuring "the real" structural cause -- that reading should be held explicitly as an outside interpretation to be checked against the community's own account, not assumed as the correct one going in.
- **Next skills:** `core/literature-review` first, to check whether this framing pattern is already documented in the sociology-of-religion literature on economic hardship; then the interpretive fieldwork itself (outside this skill's scope) informed by the ideal-type comparison named above.

## Known Limitations

- **The Durkheim/Weber divide is a real, foundational, and still-taught frame, but it is a simplification, not the full map of sociological method.** It does not on its own cover critical theory, feminist standpoint epistemology, symbolic interactionism's own distinct lineage, or contemporary computational/network sociology -- this skill classifies against the classic divide as a starting heuristic, not as exhaustive coverage of the discipline's methodological plurality.
- **Treating a "social fact" as a neutral thing carries its own history of misuse** -- structural framings have been used to naturalize patterns (poverty, crime, inequality) that closer interpretive and historical work shows to be contingent and actively contested, not fixed facts of nature. This skill flags that risk in step 5, but flagging it is not the same as resolving it -- the researcher has to actually do the interpretive check.
- **Reflexivity guidance here is a prompt, not a substitute for the researcher's own positionality work.** The skill can ask the question and name the risk; it cannot tell the researcher who they are or how that shapes their reading (Constitution, Principle 6).
- **This skill classifies and scopes; it does not run the survey, code the interview transcripts, or write the comparative-historical narrative itself** -- it hands off to that work via `next_skills` and the researcher's own subsequent analysis.
