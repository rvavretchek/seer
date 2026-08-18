---
name: educational-research
description: Scope and design an education research study -- choosing between qualitative, quantitative, or mixed methods, and matching the design to what the question actually asks. Use before data collection begins on a question about teaching, learning, or educational systems.
allowed-tools: Read, Write

skill_id: "education/educational-research"
domain: "education"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Cohen, Manion & Morrison (2018, 8th ed.) — Research Methods in Education (Routledge): the standard reference spanning research design, methodology, and data collection/analysis for education research specifically."
input_schema:
  required:
    - field: "research_question"
      type: "string"
      description: "The education question as initially stated."
  optional:
    - field: "context"
      type: "string"
      description: "The educational setting -- a classroom, a school, a system/policy level."
    - field: "available_access"
      type: "string"
      description: "What access the researcher has -- classroom observation, student work samples, teacher/student interviews, administrative data."
output_schema:
  fields:
    - field: "scoped_question"
      type: "string"
      description: "The question restated with an explicit unit of analysis (student, class, school, system)."
    - field: "method_recommendation"
      type: "string"
      description: "Qualitative, quantitative, or mixed methods, with justification tied to the question type."
    - field: "ethics_flags"
      type: "array"
      description: "Consent, safeguarding, or power-dynamic considerations specific to researching in an educational setting with minors or vulnerable participants."
chains_well_with:
  - "core/literature-review"
  - "education/curriculum-analysis"
  - "geography/geographic-research"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Educational Research

## What This Skill Does

Scopes an education research question before data collection starts — the education-domain counterpart to `geography/geographic-research`. Education research carries specific design and ethical considerations a generic research-methods approach won't surface on its own: the unit of analysis (an individual student, a classroom, a whole school, a system) changes what counts as valid evidence, and research involving students — frequently minors, in a setting with an inherent power imbalance between researcher/teacher and student — has consent and safeguarding implications that need to be named explicitly at the scoping stage, not discovered mid-study.

## Evidence Foundation

Cohen, Manion & Morrison (2018) frame education research design around matching method to question type: questions about *effect* or *prevalence* ("does intervention X improve outcome Y, and by how much?") call for quantitative or experimental/quasi-experimental design; questions about *experience* or *meaning* ("how do students experience this classroom practice?") call for qualitative methods; many real education questions need both, sequenced (mixed methods). They also establish that the unit of analysis is a first-order design decision, not an afterthought — a finding true at the classroom level (this teacher's approach works) does not automatically generalize to the school or system level, and conflating levels is a common design error. Ethical considerations specific to educational settings — informed consent (or assent, for minors, alongside guardian consent), safeguarding, and the researcher's own power position relative to students — are treated as integral to the research design, not a separate compliance afterthought.

## Procedure

1. **Restate the question with an explicit unit of analysis.** Is this about one student, a class, a school, a district/system? A question phrased generally ("does this teaching approach work?") needs this made explicit before method selection.
2. **Classify as effect-seeking, meaning-seeking, or both**, and recommend method accordingly — quantitative/quasi-experimental for effect questions, qualitative for meaning questions, mixed for questions needing both.
3. **Name the researcher's position relative to participants explicitly** when the researcher is also the teacher or has direct power over participants (grading, discipline) — this shapes what students may feel able to say and needs to be accounted for in design, not just disclosed after the fact.
4. **Flag consent, assent, and safeguarding considerations** specific to the setting — research involving minors typically needs guardian consent plus student assent, and any data involving identifiable students needs a stated approach to confidentiality.
5. **State what evidence would actually answer the question**, distinguishing correlational findings from causal claims — a common failure in education research is claiming an intervention "improved" an outcome from a design that can only show association.

## Example

**Input:** `research_question`: "Does incorporating local geographic case studies (e.g. regional agricultural land-use change) improve student engagement in geography classes, compared to standard textbook material?"

**Output:** Scoped question: unit of analysis is the classroom/lesson level (not individual student outcomes, unless individual engagement measures are specifically planned). Method recommendation: mixed methods — a quantitative engagement measure (e.g. structured observation checklist, comparing lesson types) paired with qualitative student interviews or reflections to capture *why* engagement differs, since "engagement improved" without an account of why is a thin finding for a teaching-practice question. Ethics flags: if the researcher is also the students' teacher, name this explicitly — students may report higher engagement to please their teacher, which needs to be accounted for in the interview design (e.g. an independent interviewer, or written anonymous reflections) rather than assumed away.

## Known Limitations

- **This skill scopes; it doesn't itself collect or analyze data** — hands off to appropriate qualitative/quantitative analysis skills or methods once the design is set.
- **Ethics guidance here is a prompt to plan for, not a substitute for institutional ethics review** — research involving minors in most contexts requires formal ethics/IRB-equivalent approval that this skill cannot provide or replace.
- **Mixed-methods integration is harder than running two separate studies and reporting both** — Cohen, Manion & Morrison note that genuine integration (where the qualitative and quantitative findings inform each other, not just sit side by side) requires deliberate design, which this skill can recommend but not guarantee happens well in execution.
