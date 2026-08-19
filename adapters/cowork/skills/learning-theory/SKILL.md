---
name: learning-theory
description: Analyze a learning task for cognitive load problems -- intrinsic, extraneous, and germane -- and recommend specific design fixes. Use when a task overwhelms students, instructions feel complex, or materials need simplifying without losing rigor.
allowed-tools: Read, Write

skill_id: "education/learning-theory"
domain: "education"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Sweller (1988, 1994) — Cognitive Load Theory: working memory holds roughly 4-7 elements; learning fails when total load exceeds capacity."
  - "Paas & van Merriënboer (1994) — instructional control of cognitive load: reducing extraneous load consistently improves learning outcomes."
  - "Sweller et al. (2019) — Cognitive Architecture and Instructional Design: 20 Years Later (updated CLT)."
  - "Kalyuga et al. (2003) — the expertise reversal effect: scaffolds that help novices can increase load for advanced learners."
input_schema:
  required:
    - field: "task_description"
      type: "string"
      description: "The learning task, instruction set, or resource to analyze."
    - field: "student_level"
      type: "string"
      description: "Age/year group and expertise level (novice/intermediate/advanced)."
  optional:
    - field: "task_materials"
      type: "string"
      description: "Actual text/worksheet/instructions being used, if available."
output_schema:
  fields:
    - field: "load_breakdown"
      type: "object"
      description: "Intrinsic, extraneous, and germane load, each rated with specific reasoning."
    - field: "problem_areas"
      type: "array"
      description: "Specific design elements creating unnecessary load."
    - field: "modification_suggestions"
      type: "array"
      description: "Concrete, specific fixes -- not generic 'simplify the task' advice."
    - field: "expertise_reversal_check"
      type: "string"
      description: "Whether scaffolds appropriate for novices would be counterproductive at the stated expertise level."
chains_well_with:
  - "education/didactics"
  - "education/pedagogy"
license: "CC BY-SA 4.0"
provenance: "forked:GarethManning/education-agent-skills@4be2795, adapted to the Seer skill contract"
---

# Learning Theory

## What This Skill Does

Analyzes a learning task for cognitive load across three dimensions — intrinsic (the content's inherent complexity), extraneous (unnecessary difficulty from poor design), and germane (productive effort that builds understanding) — and produces specific, actionable design fixes. This requires simultaneously judging content complexity, instructional design quality, and learner expertise, a combination most teachers haven't had formal training in.

## Evidence Foundation

Sweller (1988, 1994) established Cognitive Load Theory: human working memory holds roughly 4–7 elements simultaneously, and instruction fails when total load exceeds that capacity. Intrinsic load is set by element interactivity — how many things must be held and related in memory at once — and can't be reduced without changing the content itself. Extraneous load is caused by design choices, not content, and is where this skill's fixes concentrate: split-attention (information split across physically separate sources that must be mentally integrated), redundancy (the same information presented twice with no added value), and unclear goal structures that push students toward search-and-copy rather than understanding. Kalyuga et al. (2003) found the "expertise reversal effect" — scaffolds that reduce load for novices (worked examples, integrated diagrams) can increase load for advanced learners by forcing them to process redundant information, meaning any recommendation must be calibrated to the stated expertise level, not applied uniformly.

## Procedure

1. **Assess intrinsic load** — count roughly how many elements must be held simultaneously, and whether they can be learned in isolation or must be understood in relation to each other.
2. **Identify extraneous load sources**, each named against the specific CLT effect it violates: split-attention (separated information sources requiring mental integration), redundancy (duplicated information with no learning benefit), or an unclear/overly complex goal structure.
3. **Assess germane load** — does the task direct effort toward building understanding (schema construction, comparison, self-explanation), or toward locating information (which is extraneous, not germane, however much "work" it looks like)?
4. **Run the expertise-reversal check.** For intermediate/advanced learners, verify that scaffolds recommended for novices wouldn't instead introduce redundant load.
5. **Give specific, actionable fixes** — each naming the problem, the CLT principle it violates, and the exact change to make — never generic advice like "simplify."

## Example

**Input:** Novice Year 7 students read a 2-page text on the water cycle on one sheet, label a blank diagram on a second sheet, and answer 10 comprehension questions on a third — all simultaneously.

**Output (abridged):** Extraneous load is high — three separated sheets create a textbook split-attention problem, forcing students to search, hold, and switch, consuming working memory on navigation rather than learning. Fix: integrate short labels directly onto the diagram, eliminating the separate text sheet; sequence activities instead of running them in parallel (study a fully labeled worked example first, then a partially blank version, then fully blank from memory). Expertise reversal check: this sequencing is correct for novices; for advanced students revising the same content, skip the worked example and go straight to blank-diagram retrieval practice, since a worked example would be redundant for them.

## Known Limitations

- **Cannot observe actual student behavior** — this analyzes task design, not lived experience; two students may experience identical load differently depending on prior knowledge. Teacher observation (task abandonment, procedural rather than content questions) remains essential.
- **Intrinsic load cannot be reduced without changing the content itself** — for genuinely complex content, the fix is often breaking it across multiple lessons, not simplifying within one.
- **Recommendations are expertise-dependent by design** — if the stated student level is inaccurate, the modifications may be counterproductive; calibrate to actual, not assumed, prior knowledge.
