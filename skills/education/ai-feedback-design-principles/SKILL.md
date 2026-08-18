---
name: ai-feedback-design-principles
description: Audit and redesign AI-generated feedback for pedagogical quality, timing, and learning impact. Use when building or reviewing automated feedback in digital learning tools.
allowed-tools: Read, Write

skill_id: "education/ai-feedback-design-principles"
domain: "education"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Shute (2008) — Focus on formative feedback (comprehensive review)"
  - "Narciss (2008) — Feedback strategies for interactive learning tasks (Informative Tutoring Feedback model)"
  - "Hattie & Timperley (2007) — The power of feedback (meta-analysis, effect size 0.73)"
  - "Dai et al. (2023) — Can large language models provide useful feedback on research papers? A large-scale empirical analysis"
  - "Kluger & DeNisi (1996) — The effects of feedback interventions on performance: a historical review and a meta-analysis"
input_schema:
  required:
    - field: "feedback_scenario"
      type: "string"
      description: "The specific context in which AI will deliver feedback — what the student has done and what kind of feedback is needed."
    - field: "current_feedback_design"
      type: "string"
      description: "The current or proposed AI feedback approach — what the system currently says or plans to say in response to student work."
  optional:
    - field: "student_level"
      type: "string"
      description: "Age/year group and proficiency level."
    - field: "subject_area"
      type: "string"
      description: "The curriculum subject."
    - field: "feedback_goals"
      type: "string"
      description: "What the feedback should achieve — error correction, motivation, deeper thinking, self-regulation."
    - field: "system_constraints"
      type: "string"
      description: "Technical or practical constraints — character limits, timing requirements, format restrictions."
output_schema:
  fields:
    - field: "feedback_evaluation"
      type: "object"
      description: "Analysis of the current feedback design against research criteria."
    - field: "improved_feedback"
      type: "object"
      description: "A redesigned version of the feedback addressing identified weaknesses."
    - field: "feedback_type_analysis"
      type: "object"
      description: "Classification of feedback components by type (verification, elaboration, strategic, self) with effectiveness."
    - field: "implementation_guidance"
      type: "object"
      description: "Practical advice for deploying the improved feedback."
chains_well_with:
  - "education/formative-assessment-loop-designer"
  - "education/intelligent-tutoring-dialogue-designer"
  - "education/self-explanation-prompt-designer"
license: "CC BY-SA 4.0"
provenance: "forked:GarethManning/education-agent-skills@4be2795, adapted to the Seer skill contract"
---

# AI Feedback Design Principles

## What This Skill Does

Evaluates a proposed AI feedback design against research criteria for effective automated feedback and produces a redesigned, actionable version. Most AI feedback fails in one of two ways: too vague to act on ("Good effort! Try to improve your argument.") or so specific it does the student's thinking for them. Effective feedback lives in the narrow space between — specific enough to act on, without bypassing the cognitive work that produces learning. This matters more, not less, at AI scale: bad feedback delivered to every student is worse than no feedback at all.

## Evidence Foundation

Hattie & Timperley (2007) found feedback has an average effect size of 0.73 on learning — one of the most powerful known influences — but with enormous variance: the deciding factor is not whether feedback is given, but what kind. Their model distinguishes task, process, self-regulation, and self-level feedback; task and process feedback work, self-level praise ("Good job!") is least effective and sometimes harmful. Shute (2008) found effective feedback is specific, timely, task-focused, and that elaborated feedback (why + what to do next) generally outperforms simple verification — but can overwhelm novices if overdone. Narciss's (2008) Informative Tutoring Feedback model ties the right feedback type to the error type: conceptual errors need elaboration, careless slips need simple verification. Kluger & DeNisi (1996) found feedback directing attention to the self rather than the task can *decrease* performance — directly implicating AI systems that default to encouraging-but-empty praise. Dai et al. (2023) found LLM-generated feedback specifically trends toward excessive positivity and vague suggestions — precisely the pattern the earlier research identifies as least effective.

## Procedure

Evaluate the feedback design for:

- **Feedback scenario:** `{{feedback_scenario}}`
- **Current feedback design:** `{{current_feedback_design}}`
- **Student level:** `{{student_level}}` — if not given, infer from the scenario.
- **Subject area:** `{{subject_area}}` — if not given, infer from the scenario.
- **Feedback goals:** `{{feedback_goals}}` — if not given, assume improving the work while preserving the student's ownership of the thinking.
- **System constraints:** `{{system_constraints}}` — if not given, assume none significant.

Apply these principles:

1. **Must be specific and actionable.** If a student can't read it and know exactly what to do next, it has failed.
2. **Distinguish verification, elaboration, and strategic feedback**, and match the type to the error type — conceptual errors need elaboration, careless slips need verification, recurring patterns need a strategic note.
3. **Avoid the positivity trap.** Praise before naming a fundamental error contradicts the corrective message. Praise only when earned and specific.
4. **Don't do the student's thinking.** Close the gap between current and desired performance by showing *where* the gap is, not by writing the fix for them.
5. **Match complexity to student level.** Novices need one or two focused points; more overloads rather than helps.

Then produce, in order: a **Diagnosis** (quoting and explaining what's wrong, citing the principle violated), a **Feedback Type Analysis** table (component → type → effectiveness → issue), the **Improved Feedback Design** (the exact replacement text), a **Design Rationale** (what changed and why), and **Implementation Notes** (deployment guidance, edge cases).

## Example

**Input:** A Year 9 student wrote a persuasive essay against school uniforms using only personal anecdotes — no evidence, no counterargument. The current AI feedback: *"Great essay! You clearly feel strongly about this topic. To improve, try adding some evidence and considering the other side. A solid effort — keep it up! 7/10"*

**Diagnosis (excerpt):** Opens with "Great essay!" while the essay has fundamental structural gaps — a contradictory signal (Kluger & DeNisi, 1996). "Try adding some evidence" doesn't say what evidence, where, or how much — too vague to act on (Shute, 2008). The 7/10 score contradicts the need for fundamental revision; the student will anchor on the score and dismiss the prose.

**Improved feedback (excerpt):** *"Your writing voice is confident and direct — hold onto that. The main issue: every paragraph makes a claim and supports it with personal experience — that's assertion, not argument. Pick your strongest paragraph and find ONE piece of evidence that supports it. Then choose the strongest argument against your position and write a paragraph that acknowledges it and explains why your position still holds."*

**Design rationale (excerpt):** Task-level praise replaces self-level praise; the "assertion vs. argument" framing names the underlying conceptual gap rather than listing surface symptoms; one concrete, achievable next action replaces a list of vague suggestions, matching Shute's (2008) complexity-to-level principle.

## Known Limitations

- **Evaluates feedback design, not feedback delivery.** The same text can help or harm depending on timing and the student's emotional state — this skill does not model that.
- **The LLM-feedback evidence base is still emerging.** Dai et al. (2023) is among the first large-scale studies of its kind; the human-feedback research it builds on (Shute, Narciss, Hattie & Timperley) is well-established, but its direct transfer to AI-generated feedback is theoretically sound rather than comprehensively validated.
- **Reflects Western educational-research norms.** Direct, task-focused feedback may land differently in other cultural contexts; Narciss's (2008) model was developed primarily in European/North American settings — worth flagging explicitly for a Brazilian classroom context, not assumed to transfer unchanged.
- **Does not model individual student self-efficacy.** Kluger & DeNisi (1996) found feedback can harm performance when it threatens self-concept; for students with low self-efficacy, "no empty praise" needs human judgment to balance against that risk.
