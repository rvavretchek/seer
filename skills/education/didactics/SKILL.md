---
name: didactics
description: Build a complete explicit-instruction sequence (I Do / We Do / You Do) from teacher modeling through guided practice to independent work. Use when teaching a new skill, procedure, or concept through direct instruction.
allowed-tools: Read, Write

skill_id: "education/didactics"
domain: "education"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Rosenshine (2012) — Principles of Instruction: research-based strategies synthesized across decades of instructional research."
  - "Pearson & Gallagher (1983) — the gradual release of responsibility model (I Do / We Do / You Do)."
  - "Archer & Hughes (2011) — Explicit Instruction: Effective and Efficient Teaching -- modeling must include articulated reasoning, not just demonstration."
  - "Hattie (2009) — Visible Learning: direct instruction effect size 0.59."
input_schema:
  required:
    - field: "skill_to_teach"
      type: "string"
      description: "The specific skill or concept to teach through explicit instruction."
    - field: "student_level"
      type: "string"
      description: "Year group and prior-knowledge level."
    - field: "lesson_time"
      type: "string"
      description: "Available lesson time in minutes."
  optional:
    - field: "common_misconceptions"
      type: "string"
      description: "Known errors or misconceptions students make with this skill."
output_schema:
  fields:
    - field: "i_do"
      type: "object"
      description: "Teacher modeling phase with scripted think-aloud at each decision point."
    - field: "we_do"
      type: "object"
      description: "Guided practice with structured, high-interaction teacher-student work."
    - field: "you_do"
      type: "object"
      description: "Independent practice sequenced from similar-to-model toward varied, with monitoring plan."
    - field: "cfu_points"
      type: "array"
      description: "Checking-for-understanding moments at each transition."
chains_well_with:
  - "education/pedagogy"
  - "education/learning-theory"
license: "CC BY-SA 4.0"
provenance: "forked:GarethManning/education-agent-skills@4be2795, adapted to the Seer skill contract"
---

# Didactics

## What This Skill Does

Generates a complete gradual-release-of-responsibility sequence for teaching a specific skill: a scripted "I Do" (teacher models with think-aloud), a structured "We Do" (guided practice with real student contribution, not passive watching), and a designed "You Do" (independent practice sequenced from similar-to-the-model toward varied, with a monitoring plan). Effective explicit instruction requires making invisible expert thinking visible — decomposing a skill the teacher performs automatically into discrete steps with articulated reasoning, which is exactly where most explicit instruction falls short.

## Evidence Foundation

Rosenshine (2012) synthesized instructional research into principles including: present new material in small steps with practice after each, provide models, guide practice with a high success rate before releasing students, and check for understanding throughout. Pearson & Gallagher (1983) formalized gradual release: the teacher carries all cognitive load at first (I Do), progressively shares it (We Do), then transfers it fully (You Do). Archer & Hughes (2011) emphasize that modeling must include *why*, not just *what* — students need to hear the decision-making reasoning behind each step, not just observe it performed. Hattie (2009) found direct instruction among the highest-impact approaches measured (effect size 0.59).

## Procedure

1. **I Do — model with think-aloud.** Demonstrate the complete skill, articulating reasoning at every decision point ("I'm choosing X because…"). Show a common error and explain why it's wrong. Keep this phase to roughly 20% of lesson time — brief; students learn by doing, not watching.
2. **We Do — guided practice with real interaction.** Work a new example together; the teacher does the early steps, students progressively take over. Use frequent checks (cold-calling, "what should I do next and why?"). This is not a second demonstration — students must actively contribute. Aim for 80%+ success before releasing to independent work.
3. **You Do — independent practice with monitoring.** Sequence problems from very similar to the modeled example toward varied. Build in an early checkpoint (a quick whole-class check after the first few minutes) and a specific monitoring plan for which students to check first.
4. **Embed checking-for-understanding at every transition** — between I Do and We Do, and between We Do and You Do — not just at the end.
5. **Address misconceptions during modeling**, not left for students to discover on their own — show the common error and explain why it's wrong as part of the "I Do" phase.

## Example

**Input:** `skill_to_teach`: "Writing an analytical (not descriptive) topic sentence in English Literature." `student_level`: "Year 9, can write paragraphs but topic sentences default to plot description." `lesson_time`: "50 minutes."

**Output (abridged):** I Do (10 min) models the shift from "Lady Macbeth is very ambitious" (description) to "Shakespeare presents Lady Macbeth's ambition as more ruthless and calculated than Macbeth's own, using her soliloquy…" (analytical claim), narrating the reasoning at each revision. We Do (15 min) has the class co-construct a topic sentence for a new scene, with the teacher eliciting stronger analytical verbs from students rather than supplying them. You Do (20 min) sequences four practice prompts from same-text to cross-text transfer, with a monitoring plan prioritizing the students who signaled uncertainty at the CFU checkpoint.

## Known Limitations

- **Best suited to skills with identifiable steps and clear success criteria** — open-ended tasks with multiple valid approaches (creative writing, open problem-solving) fit this rigid sequence poorly; the modeling phase should then show a decision-making process, not a single "correct" path.
- **Quality depends entirely on the teacher delivering the think-aloud authentically**, not reading a script verbatim — an authentic, slightly less polished think-aloud beats a robotically read one.
- **Risk of over-scaffolding in We Do** — if the teacher does too much and students contribute too little, guided practice collapses into a second demonstration; productive struggle is appropriate as long as the success rate stays high.
