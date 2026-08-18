---
name: curriculum-analysis
description: Audit a curriculum framework against a statutory, accreditation, or standards requirement list -- producing a coverage table and honest gap summary. Use when checking whether a curriculum actually addresses required content, not just assuming it does.
allowed-tools: Read, Write

skill_id: "education/curriculum-analysis"
domain: "education"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "Webb, N.L. (1997) — Criteria for Alignment of Expectations and Assessments in Mathematics and Science Education (CCSSO): the canonical alignment framework (categorical concurrence, depth-of-knowledge, range, balance) this skill's match-strength classification follows."
  - "Porter, A.C. et al. (2002) — Measuring the content of instruction: uses in research and practice, Educational Researcher 31(7): the row-per-requirement curriculum-mapping methodology this skill's coverage table is based on."
input_schema:
  required:
    - field: "framework"
      type: "string"
      description: "The curriculum framework being audited -- competencies, learning targets, or units."
    - field: "requirements"
      type: "string"
      description: "The statutory, accreditation, or standards requirement list to audit against, each requirement identifiable by number or label."
  optional:
    - field: "framework_name"
      type: "string"
      description: "Human-readable name of the framework."
    - field: "requirements_source"
      type: "string"
      description: "Name of the statutory or accreditation body."
output_schema:
  fields:
    - field: "coverage_table"
      type: "string"
      description: "One row per requirement: what covers it (if anything), and evidence strength -- direct, partial, indirect, or none."
    - field: "gap_summary"
      type: "string"
      description: "Prose summary of requirements with no or only indirect coverage, grouped thematically."
    - field: "coverage_statistics"
      type: "object"
      description: "Counts: total, directly covered, partially covered, indirectly covered, not covered."
chains_well_with:
  - "education/pedagogy"
  - "core/source-verification"
license: "CC BY-SA 4.0"
provenance: "forked:GarethManning/education-agent-skills@4be2795, adapted to the Seer skill contract"
---

# Curriculum Analysis

## What This Skill Does

Audits a curriculum framework — any school's programme of study or competency framework — against an external requirement list (statutory, accreditation, or standards-based, e.g. Brazil's BNCC) and produces a structured coverage table showing which framework content addresses each requirement and how strongly. It is framework-agnostic and deliberately conservative: it classifies matches as direct, partial, indirect, or none, and is explicit that "coverage" here means topical presence in documentation, not confirmation that the content is taught, assessed, or enacted at the required depth.

## Evidence Foundation

Webb (1997) establishes categorical concurrence — do the framework and the requirement address the same topic at all — as the foundational alignment question, distinct from his further depth-of-knowledge dimension (whether the cognitive demand matches), which this skill deliberately does not attempt and flags as a human-judgment task. Porter et al. (2002) establish the row-per-requirement approach used here: mapping framework content onto each requirement, rather than organizing around what the framework already covers, so that true gaps (requirements with no matching content) stay visible rather than getting absorbed into a generally positive-looking summary.

## Procedure

1. **List every requirement with a stable identifier** before searching the framework at all — this ordering matters, so gaps don't get quietly skipped.
2. **For each requirement, classify the match**: **direct** (framework explicitly and substantively addresses it — a teacher could cite this without qualification), **partial** (related content exists but framing/depth/scope differs), **indirect** (only tangentially related content exists), or **none** (no framework content touches it — a gap row).
3. **Classify conservatively.** A match requiring an inferential leap beyond what the framework text directly states should be partial or indirect, not direct — the goal is an honest starting point for professional review, not a maximized-looking coverage score.
4. **Produce the coverage table and a gap summary** that groups related gaps thematically and states the total count of gap/indirect rows explicitly, not buried in prose.
5. **State the coverage statistics** (total, direct, partial, indirect, none) as a headline for quick scanning.

## Example

**Input:** A school's wellbeing/health curriculum audited against a statutory relationships-and-health-education requirement list.

**Output (abridged):** Of 8 requirements sampled, 3 show no coverage — clustering around a specific sub-topic (e.g. a content area entirely absent from the framework, not spread thin across many areas) — and 1 is only indirectly covered. One requirement is partially met but at an earlier developmental stage than the standard specifies, meaning the intended stage is effectively uncovered. The gap summary names this pattern explicitly rather than reporting an overall "mostly covered" impression that would obscure it.

## Known Limitations

- **Topical coverage is not depth equivalence.** A "direct" match means the topic is present in documentation — not that it's taught at the required cognitive depth, assessed appropriately, or actually delivered in classrooms. This is a starting point for professional review, not a conclusion.
- **Audits documentation against documentation** — it cannot determine whether the written framework is what's actually enacted in classrooms; accreditors typically want evidence of enacted curriculum, which this skill does not supply.
- **Requires human professional review before any accreditation or compliance claim** — classifications come from pattern-matching against text, not a qualified reviewer's judgment in the relevant regulatory domain.
