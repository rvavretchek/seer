---
name: pedagogy
description: Diagnose a teacher's pedagogical content knowledge (PCK) gaps for a specific topic and produce a development plan before they teach it. Use when a teacher is preparing to teach unfamiliar content or improving how they teach a topic students consistently struggle with.
allowed-tools: Read, Write

skill_id: "education/pedagogy"
domain: "education"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Shulman (1986, 1987) — original Pedagogical Content Knowledge (PCK) framework: content knowledge and pedagogical knowledge are distinct from a third, teachable capability -- knowing how to make specific content comprehensible to specific learners."
  - "Ball, Thames & Phelps (2008) — Content knowledge for teaching: a teacher's ability to diagnose why a student's wrong answer makes sense predicted student learning gains better than the teacher's own subject proficiency."
  - "Magnusson, Krajcik & Borko (1999) — components of PCK for science teaching, each topic-specific."
  - "Bernstein (1999) — knowledge structures: hierarchical (prerequisite chains), horizontal (disciplinary thinking/representations), and dispositional (real-time noticing) PCK."
  - "Hattie (2009) — Visible Learning: PCK has a substantially larger effect on achievement than raw content knowledge alone."
input_schema:
  required:
    - field: "teaching_context"
      type: "string"
      description: "What the teacher is about to teach: subject, topic, unit."
    - field: "learner_stage"
      type: "string"
      description: "Age range or year group."
    - field: "teacher_background"
      type: "string"
      description: "The teacher's subject training and experience with this specific topic."
  optional:
    - field: "known_student_misconceptions"
      type: "string"
      description: "Misconceptions the teacher is already aware of."
output_schema:
  fields:
    - field: "pck_diagnosis"
      type: "object"
      description: "Likely PCK gaps across hierarchical, horizontal, and dispositional dimensions, plus transferable strengths."
    - field: "misconceptions_map"
      type: "array"
      description: "Documented student misconceptions for this topic/stage, with why each forms and what shifts it."
    - field: "representations"
      type: "array"
      description: "Effective analogies/models for this content, including at least one to avoid."
    - field: "development_plan"
      type: "string"
      description: "Sequenced, actionable steps for the teacher before, during, and after teaching."
chains_well_with:
  - "education/didactics"
  - "education/curriculum-analysis"
  - "education/learning-theory"
license: "CC BY-SA 4.0"
provenance: "forked:GarethManning/education-agent-skills@4be2795, adapted to the Seer skill contract"
---

# Pedagogy

## What This Skill Does

Diagnoses a teacher's pedagogical content knowledge (PCK) gaps for a specific topic and stage, and produces a sequenced plan to close them before teaching begins. Shulman's foundational insight: knowing a subject and knowing how to teach it are genuinely different capabilities. A mathematician who has never taught fractions to nine-year-olds doesn't automatically know which representations work, which misconceptions will form, or where students get stuck. This matters most when a teacher is working outside their primary training, teaching an ambitious new unit, or moving to a new age group.

## Evidence Foundation

Shulman (1986, 1987) distinguished PCK as the blend of content and pedagogy uniquely teachers' province — "the ways of representing and formulating the subject that make it comprehensible to others." Ball, Thames & Phelps (2008) found a teacher's ability to diagnose why a student's wrong answer makes sense was a stronger predictor of student learning than the teacher's own problem-solving ability — content knowledge is necessary but not sufficient; what matters is its transformation into teachable form. Magnusson, Krajcik & Borko (1999) established that PCK is topic-specific, not general — PCK for photosynthesis doesn't transfer to Newtonian mechanics. Bernstein's (1999) framework maps three PCK dimensions: **hierarchical** (prerequisite chains, where students get stuck), **horizontal** (representations and disciplinary thinking — which analogies illuminate vs. mislead), and **dispositional** (real-time noticing of what students actually understand vs. what they've been told).

## Procedure

1. **Diagnose likely gaps** across all three dimensions based on the teacher's stated background and the topic — be specific ("a humanities-trained teacher covering neuroscience content is unlikely to have secure knowledge of the HPA axis"), not generic. Also name transferable strengths the teacher's background brings.
2. **Map the prerequisite chain** for the content, distinguishing hard prerequisites (cannot proceed without) from soft ones, and flag the 2-3 concepts most commonly misunderstood by teachers themselves at this level.
3. **Build a misconceptions map**: for each documented student misconception, state what it is, why it forms, how persistent it is, and what research suggests is needed to shift it — not just "correct it."
4. **Recommend representations**, each with what it illuminates and what it obscures or misleads, including at least one representation to actively avoid.
5. **Produce a sequenced development plan**: what to learn before teaching begins, what to observe during teaching, what develops only through sustained experience afterward.

## Example

**Input:** A humanities-trained teacher (history/politics, no science training) is teaching a Year 9 unit on the neuroscience of stress for the first time.

**Output (abridged):** Hierarchical gap — the teacher likely lacks secure knowledge of the HPA axis (hypothalamus→pituitary→adrenal→cortisol), the central prerequisite for explaining the stress response accurately. Misconception map — "stress is always bad" (high persistence, reinforced by everyday language; shifts by teaching the acute/chronic distinction explicitly). Representation to avoid — "left brain/right brain," which is not supported by neuroimaging evidence. PCK strength to build on — the teacher's strong facilitated-discussion and case-based teaching skills transfer directly to exploring the topic through lived-experience cases ("what happens in your body during an exam?").

## Known Limitations

- **The diagnosis relies on the teacher's self-reported background**, which may over- or under-state actual retained knowledge — for high-stakes accuracy (health/safety content), the teacher should verify independently.
- **Misconception research quality varies by topic** — well-replicated for some (fractions, evolution), thinner for newer or less-studied areas; the skill flags this where relevant.
- **PCK ultimately develops through sustained subject-specific teaching experience, not from reading a diagnosis** — this skill accelerates recognition of what experienced teachers learn slowly; it cannot substitute for the teaching itself.
