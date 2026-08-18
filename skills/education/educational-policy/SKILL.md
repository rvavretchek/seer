---
name: educational-policy
description: Analyze an education policy -- what problem it targets, who it actually affects, and whether its stated intent matches its likely on-the-ground effect. Use for questions about curriculum mandates, funding formulas, accreditation requirements, or other education policy instruments.
allowed-tools: Read, Write

skill_id: "education/educational-policy"
domain: "education"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Ball, S.J. — Education Policy and Social Class: policy is not neutrally implemented -- it is interpreted, translated, and often altered by the people enacting it (teachers, schools), and its effects are frequently stratified by social class even when the policy text is formally universal."
  - "Fowler, F.C. — Policy Studies for Educational Leaders: An Introduction (Pearson): the standard policy-analysis framework -- problem definition, actors and institutions, and the gap between intended and actual policy effects."
input_schema:
  required:
    - field: "policy_description"
      type: "string"
      description: "The policy, mandate, or funding/accreditation mechanism being analyzed."
  optional:
    - field: "affected_population"
      type: "string"
      description: "Who the policy is formally intended to affect."
    - field: "implementation_context"
      type: "string"
      description: "The institutional context where the policy is actually enacted, if known."
output_schema:
  fields:
    - field: "problem_definition"
      type: "string"
      description: "What problem the policy is formally framed as solving, and by whom."
    - field: "actor_analysis"
      type: "string"
      description: "Who actually implements the policy day to day, and where their interpretation may diverge from the policy's stated intent."
    - field: "distributional_check"
      type: "string"
      description: "Whether the policy's effects are likely to be evenly distributed or stratified by social class, region, or other factors, even if the policy text is formally universal."
chains_well_with:
  - "education/curriculum-analysis"
  - "geography/political-geography"
  - "geography/economic-geography"
  - "core/source-verification"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Educational Policy

## What This Skill Does

Analyzes an education policy — a curriculum mandate, a funding formula, an accreditation requirement — by separating what the policy formally says from what it's likely to actually do once it reaches classrooms and schools. Education policy analysis has a specific, well-documented failure mode: treating a policy's text as equivalent to its effect, when in practice policy is interpreted and often substantially altered by the teachers and institutions implementing it, and its real-world effects are frequently distributed unevenly even when the policy's language is formally universal ("all schools will…").

## Evidence Foundation

Ball's work on education policy establishes that policy is not neutrally implemented — it passes through a chain of interpretation (national policy → regional/state administration → school leadership → individual teacher) at each stage of which it can be reshaped, partially adopted, or resisted, and that its effects are frequently stratified by social class and resourcing even when the formal policy text applies equally to everyone. A well-resourced school and an under-resourced school implementing the identical mandate can produce very different outcomes, and this stratification is not a side effect but a central, recurring finding across education-policy research. Fowler's policy-analysis framework structures the analysis around problem definition (what problem does the policy claim to solve, and whose framing of the problem won out over competing framings), the actors and institutions actually responsible for implementation, and the gap between intended and enacted policy — closely paralleling this skill's procedure below.

## Procedure

1. **State the policy's formal problem definition** — what problem is it framed as solving, and note if competing framings of the same underlying issue existed and lost out (whose definition of the problem shaped the policy that resulted).
2. **Identify the actors who actually implement the policy day to day** — typically several steps removed from whoever wrote it — and flag where their incentives, capacity, or interpretation may diverge from the policy's stated intent.
3. **Run the distributional check explicitly.** Even a formally universal policy ("all schools will implement X") can have stratified effects if implementation requires resources, training, or capacity unevenly distributed across schools or regions — name this risk rather than assuming uniform application, per Ball's central finding.
4. **Distinguish intended from likely actual effect**, and state both — a policy analysis that only restates the policy's stated goals hasn't actually analyzed anything.
5. **Ground claims about a policy's likely effects in verifiable evidence** (existing research on similar policies, comparable jurisdictions) rather than speculation — compose with `core/source-verification`.

## Example

**Input:** `policy_description`: "A state mandate requiring all schools to incorporate a minimum number of hours of environmental/geographic field-based learning per year."

**Output:** Problem definition: framed as addressing low student engagement with environmental content taught only from textbooks — a reasonable framing, though it assumes the engagement problem is primarily pedagogical rather than resource-based. Actor analysis: implementation depends on individual schools' access to transport budgets, nearby field sites, and teacher training in field-based pedagogy — actors several steps removed from the state-level policy writers. Distributional check: a formally universal "all schools" mandate is likely to produce highly uneven actual field-learning hours between well-resourced urban/private schools (with transport budgets and staff capacity) and under-resourced rural or public schools (without them) — this is the central risk to flag, following Ball's finding that formally universal policy frequently reproduces or widens existing inequality rather than closing it, unless implementation resourcing is addressed alongside the mandate itself.

## Known Limitations

- **This skill analyzes; it does not predict with certainty.** The distributional and implementation-gap risks it names are well-documented patterns in education-policy research generally, not a guaranteed forecast for this specific policy — verify against comparable real cases where possible.
- **Requires real institutional knowledge of the specific system being analyzed** to be more than generic — this skill's framework is general-purpose; the actor analysis and distributional check are only as accurate as the researcher's actual knowledge of how that specific education system (Brazilian state/municipal education governance, in Sônia's likely use case) actually functions.
- **Does not adjudicate whether a policy is good or bad** — it analyzes mechanism and likely distributional effect; the normative judgment of whether that tradeoff is acceptable stays with the human (Constitution, Principle 6).
