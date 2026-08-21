---
name: academic-project-planning
description: Plan and track the deliverables/deadlines dimension of an academic research project -- schedule, milestones, and risk register for the research work itself, plus submission-window and peer-review-turnaround tracking for the publication pipeline. Use when a researcher needs to sequence project phases against real dates or flag a schedule risk, never for choosing a research method (that's the discipline skill's job) or for the substance of writing/reviewing a manuscript (that's core/academic-writing and core/peer-review).
allowed-tools: Read, Write

skill_id: "project-management/academic-project-planning"
domain: "project-management"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "Project Management Institute -- A Guide to the Project Management Body of Knowledge (PMBOK Guide), 8th Edition (released November 2025, current as of this skill's writing in August 2026): 6 core principles, 7 performance domains (Governance, Scope, Schedule, Finance, Stakeholders, Resources, Risk), and 5 Focus Areas (Initiating, Planning, Executing, Monitoring and Controlling, Closing) containing 40 non-prescriptive processes. This skill's schedule/milestone procedure is grounded in the Schedule performance domain; its risk procedure in the Risk performance domain; its deliverable-acceptance framing in the Governance performance domain. Confirmed via multiple independent 2025-2026 sources (Project Management Academy, Learning Tree, BrainBOK, StarAgile) as the edition that superseded the 7th Edition's (2021) 12-principles/8-performance-domains structure -- the primary PMBOK text itself is a commercial/licensed PMI publication, not freely mirrored, so this grounding rests on corroborated secondary reporting rather than the canonical text directly (see Known Limitations)."
input_schema:
  required:
    - field: "project_activities"
      type: "string"
      description: "The research project's phases and deliverables in whatever rough form the researcher has them -- e.g. a list of planned activities (fieldwork, data collection, analysis, writing), each with a known or approximate duration."
  optional:
    - field: "fixed_dates"
      type: "array"
      description: "Dates the researcher does not control -- funding-cycle deadlines, a thesis defense date, a conference submission window, an advisor's committee meeting -- that the schedule must plan around."
    - field: "publication_target"
      type: "object"
      description: "The venue(s) the work is headed toward -- journal or conference name, known submission window, typical peer-review turnaround, and revision deadline conventions, if known."
    - field: "known_risks"
      type: "array"
      description: "Risks to the schedule the researcher has already identified -- e.g. dependency on a collaborator's data, access to a field site, equipment availability -- to fold into the risk register rather than rediscover from scratch."
    - field: "team_size"
      type: "string"
      description: "Solo researcher, small team, or larger group -- PMBoK's governance and resource-management guidance was built for organizational teams, and its transfer to a solo or two-person academic project is not one-to-one (see Known Limitations)."
output_schema:
  fields:
    - field: "schedule_plan"
      type: "array"
      description: "The research project's phases sequenced against a timeline, with milestones (a phase's defined completion point, per PMBoK's Schedule performance domain) marked distinctly from ordinary activities."
    - field: "risk_register"
      type: "array"
      description: "Identified risks to the schedule, each with a likelihood/impact assessment and a mitigation or contingency, per PMBoK's Risk performance domain -- never a research-methodology risk (e.g. sampling bias), only a schedule/deliverable risk (e.g. a dependency slipping, a review cycle running long)."
    - field: "publication_deadline_tracker"
      type: "array"
      description: "Submission windows, expected peer-review turnaround, and revision deadlines for the publication pipeline -- deadline dates only, never feedback on manuscript quality or review substance."
    - field: "schedule_conflicts"
      type: "array"
      description: "Points where the research-project schedule and the publication-pipeline deadlines collide or leave too little slack -- e.g. a submission window falling before a dependent analysis phase is scheduled to finish -- flagged explicitly rather than silently absorbed into the plan."
chains_well_with:
  - "core/academic-writing"
  - "core/peer-review"
  - "core/literature-review"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Academic Project Planning

## What This Skill Does

Manages the **deliverables-and-deadlines** dimension of an academic research project -- a schedule, a set of milestones, and a risk register for the research work itself, plus deadline tracking for the publication pipeline it feeds into. This skill applies PMBoK's project-management discipline (schedule, milestones, risk) to academic work; it does **not** apply research methodology.

This boundary is the single most important thing to get right, so it is stated here explicitly and up front: **this skill never recommends how to research something.** Study design, sampling strategy, data-collection method, and analytical approach are the responsibility of the discipline researcher and the discipline skills (`geography/*`, `education/*`, `sociology/*`, and so on) -- never this skill's job, and never something this skill will offer even if asked, because a "project manager" persona is exactly the kind of thing a researcher might expect methodology advice from and exactly the kind of thing PMBoK itself does not provide. If a fieldwork phase needs a duration estimate, this skill can help sequence and track that duration against a deadline; it has no opinion on whether the fieldwork should use structured interviews or participant observation.

The same discipline applies to the publication pipeline: this skill tracks *when* things are due -- submission windows, peer-review turnaround cycles, revision deadlines -- never the substance of what is submitted or reviewed. Manuscript quality, argument structure, and claim-hedging are `core/academic-writing`'s job; the actual content of a peer review is `core/peer-review`'s job. This skill only tracks the calendar those two skills' work has to fit inside.

## Evidence Foundation

PMBoK (the Project Management Institute's Guide to the Project Management Body of Knowledge) is the standard reference for project-management discipline, and its 8th Edition (released November 2025, the current edition as of this skill's writing) structures the discipline around 6 core principles and 7 performance domains -- Governance, Scope, Schedule, Finance, Stakeholders, Resources, and Risk -- worked through 5 Focus Areas (Initiating, Planning, Executing, Monitoring and Controlling, Closing) containing 40 non-prescriptive processes. This is a real structural change from the 7th Edition (2021), which used 12 principles and 8 performance domains; the 7th edition was itself a shift away from the older 6th edition's 5 process groups / 10 knowledge areas. Despite the relabeling across editions, the substance each edition organizes -- a schedule needs milestones, milestones need dependencies tracked, and dependencies carry risk that needs a register and a mitigation plan -- has stayed intact and been carried forward each time, which is the sense in which PMBoK is a comparatively stable, additive framework: later editions have tended to restructure and rename rather than invalidate the prior edition's good practice. This skill grounds its schedule/milestone procedure in the 8th Edition's **Schedule** performance domain, its risk procedure in the **Risk** performance domain, and its deliverable-acceptance framing in the **Governance** performance domain.

`evidence_strength` is rated **moderate**, not strong, for two compounding reasons. First, as with `core/academic-formatting-abnt`'s treatment of ABNT, the primary PMBoK text is a commercial, licensed PMI publication, not freely mirrored -- this skill's grounding rests on corroborating multiple independent secondary sources describing the just-released 8th Edition (Project Management Academy, Learning Tree, BrainBOK, StarAgile), not on reading the canonical text directly, and a framework only months old at time of writing carries more currency risk than a long-settled one. Second, and specific to this skill rather than to ABNT: PMBoK was built for organizational, often large-team projects, and applying it to a solo or small-team academic research project is a genuine stretch beyond its original target domain, not a direct transfer -- see Known Limitations.

## Procedure

Treat the research project's own schedule/risk and the publication pipeline's deadlines as two distinct passes -- a project can be on track on one and at risk on the other, and collapsing them hides that.

### Pass 1 -- Research-Project Schedule and Risk

1. **Break `project_activities` into phases with milestones**, per the Schedule performance domain. A milestone is a phase's defined completion point (e.g. "fieldwork complete," "coding of interview data complete"), not just an end-of-week status; state each phase's dependencies on the phases before it explicitly, since a slip in an early phase propagates forward.
2. **Anchor the schedule against `fixed_dates`** -- dates the researcher does not control (funding-cycle deadlines, a thesis defense, a committee meeting). Work backward from these to check whether the phase sequence in step 1 actually fits, rather than only working forward from today.
3. **Build a risk register**, per the Risk performance domain. Start from any `known_risks` supplied, then add schedule risks visible in the phase structure itself -- a phase depending on a collaborator's data, on field-site access, on equipment or ethics-board approval with its own turnaround. For each risk: state likelihood, impact on the schedule specifically (not on data quality -- that is a methodology concern, out of scope here), and a mitigation or contingency.
4. **Flag deliverable-acceptance points explicitly**, per the Governance performance domain -- who or what decides a phase is actually done (an advisor's sign-off, a committee review, a co-author's approval) is itself a schedule dependency, and treating it as automatic when it is not is a common source of silent slippage.
5. **Never let this pass drift into method advice.** If a phase's duration is uncertain because the researcher hasn't decided *how* they'll collect the data, name that as an open input this skill needs from the researcher (or the relevant discipline skill), not something this skill will resolve itself.

### Pass 2 -- Publication-Pipeline Deadline Tracking

6. **Record the deadline structure of `publication_target`**, if supplied: submission window (a fixed date or a recurring cycle), typical peer-review turnaround for that venue, and the revision deadline convention (many venues give a fixed window, e.g. 30 or 60 days, to return a revision). Where the researcher doesn't know these figures, flag them as needed inputs rather than guessing at a specific venue's actual turnaround.
7. **Track deadlines only, never review substance.** This pass produces dates -- when a submission is due, when a decision is expected back, when a revision is due -- not feedback on the manuscript itself (`core/academic-writing`) or the review's content (`core/peer-review`). If asked to also assess the manuscript's quality, hand that off rather than absorbing it into this skill's output.
8. **Cross-check the publication deadline tracker against the Pass 1 schedule.** A submission window that falls before the dependent analysis or writing phase is scheduled to finish is a schedule conflict, not a minor note -- surface it in `schedule_conflicts` explicitly, with the specific dates that collide, rather than leaving the researcher to notice it later.
9. **Re-run this pass after a revision request lands.** A "minor revision" or "major revision" decision resets the deadline clock (per the venue's stated revision window) and can reopen a conflict with the Pass 1 schedule that a "submitted, awaiting decision" state didn't have -- treat this as a real replanning trigger, not a formality.

## Example

**Input:** A researcher planning a multi-phase field study: (1) survey-instrument piloting, ~3 weeks; (2) field data collection, ~8 weeks, dependent on (1) and on a local partner institution's ethics approval; (3) data analysis, ~6 weeks, dependent on (2); (4) writing, ~4 weeks, dependent on (3). `fixed_dates`: a thesis committee check-in in 14 weeks. `publication_target`: a mid-tier conference with a submission deadline in 16 weeks and a typical 8-week review turnaround before the conference itself.

**Output (abridged):**

- **schedule_plan:** Phase 1 (weeks 1-3) -> Phase 2 (weeks 4-11, contingent on partner-institution ethics approval landing by week 4) -> Phase 3 (weeks 12-17) -> Phase 4 (weeks 18-21). Milestone flagged at week 3: "piloted instrument approved," gating Phase 2's start.
- **risk_register:** (1) Partner-institution ethics approval timeline is external and not confirmed -- likelihood: moderate, impact: high (delays the entire chain downstream), mitigation: request confirmation now, hold week 4 as a soft rather than hard start date. (2) Phase 3 (analysis) has no slack before the committee check-in -- likelihood: moderate, impact: check-in may show incomplete analysis, mitigation: consider a partial-analysis interim update for the committee rather than treating week 14 as an analysis-complete deadline.
- **schedule_conflicts:** The conference submission deadline (week 16) falls *before* Phase 4 (writing) is scheduled to finish (week 21) under the current plan -- flagged as a direct conflict, not a minor gap. This is a scheduling fact only; this skill does not recommend which deadline to prioritize or how to compress the writing phase's content -- that judgment call, and any decision to submit a shorter/earlier version of the work, belongs to the researcher (and, for the writing itself, to `core/academic-writing`).
- **publication_deadline_tracker:** Submission: week 16. Expected decision: approximately week 24 (8-week turnaround, per venue convention supplied). Revision deadline, if requested: per venue's own stated window, not yet known -- flagged as an input to confirm once a decision arrives.

## Known Limitations

- **The methodology boundary is a hard limit, not a soft default.** This skill will not suggest a sampling approach, a data-collection instrument, or an analytical method even when a schedule question (e.g. "how long should Phase 2 take") seems to invite it -- that pulls toward methodology, which belongs to the discipline researcher and the relevant discipline skill. A researcher who wants that kind of guidance from a "project manager" persona will not get it here, by design, and should be redirected rather than accommodated.
- **PMBoK was built for organizational, often large-team projects, and its transfer to a solo or small-team academic project is not one-to-one.** The Governance and Resources performance domains in particular assume structures (a sponsor, a PMO, a resource pool to draw on) that a single graduate student or a two-person research team usually doesn't have; this skill applies the schedule/milestone/risk logic that does transfer, but a researcher should not expect every PMBoK performance domain to map cleanly onto a solo academic project, and this skill does not force a fit where one isn't natural.
- **This skill's PMBoK grounding is built from corroborated secondary reporting on a recently released edition (8th, November 2025), not the primary licensed PMI text.** As with `core/academic-formatting-abnt`'s treatment of ABNT, a future reader should re-verify the current edition and its structure rather than assume this skill's description of it is still current -- PMI has changed this structure twice in recent years (6th to 7th, 7th to 8th) and there is no fixed revision schedule.
- **Publication-pipeline turnaround figures (typical peer-review duration, revision windows) are venue-specific and this skill does not have them pre-loaded.** It tracks whatever figures the researcher supplies via `publication_target`; where those aren't known, this skill flags the gap rather than estimating a plausible-sounding number, since a wrong turnaround estimate is worse than an explicit unknown.
- **A risk register is only as good as the risks named into it.** This skill surfaces schedule risks visible in the phase structure and dependencies the researcher describes, but it has no independent way to discover a risk the researcher hasn't mentioned and that isn't structurally obvious (e.g. a collaborator's unstated availability constraints) -- it is a structuring tool for known and inferable risks, not a substitute for the researcher's own situational awareness.
- **Does not replace the researcher's or advisor's own judgment on tradeoffs.** Where a schedule conflict is flagged (e.g. a submission deadline versus a writing phase not yet finished), this skill states the conflict; deciding which deadline to prioritize, whether to submit a shorter or earlier version of the work, or whether to request an extension remains the researcher's decision (Constitution, Principle 6).
