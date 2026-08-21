---
name: policy-process-analysis
description: Analyze why a policy issue did (or didn't) reach the government's agenda and move toward adoption -- using Kingdon's Multiple Streams Framework (problem, policy, and politics streams converging at a policy window) instead of assuming policy change follows a rational, linear problem-solving sequence. Use for questions about why an issue suddenly gained traction, why an available solution stalled for years, or what would need to align for a policy window to open.
allowed-tools: Read, Write

skill_id: "political-science/policy-process-analysis"
domain: "political-science"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "Kingdon, J.W. (1984; 2nd ed. 1995) -- Agendas, Alternatives, and Public Policies: the Multiple Streams Framework -- three largely independent streams (problem, policy, politics) that must couple, via a policy entrepreneur, at a policy window for agenda change to occur."
  - "Sabatier, P.A. & Jenkins-Smith, H.C. (1988; 1993) -- Advocacy Coalition Framework: a complementary lens for longer time-horizon policy change, driven by competing coalitions' belief systems and policy-oriented learning, used here where MSF's short-window focus doesn't fit the question."
input_schema:
  required:
    - field: "policy_issue"
      type: "string"
      description: "The policy issue or question -- why a proposal advanced or stalled, or what conditions would need to align for it to advance."
  optional:
    - field: "time_horizon"
      type: "string"
      description: "A short-term agenda-setting moment (favors MSF) vs. a longer multi-year/decade view of coalition conflict and belief change (favors ACF)."
    - field: "known_actors"
      type: "string"
      description: "Known policy entrepreneurs, coalitions, or institutional actors involved, if any."
output_schema:
  fields:
    - field: "stream_analysis"
      type: "object"
      description: "Problem stream (how the issue is framed and measured as a problem), policy stream (what alternatives exist and their technical/political feasibility), and politics stream (national mood, organized interests, government turnover) -- each assessed independently before considering coupling."
    - field: "coupling_assessment"
      type: "string"
      description: "Whether and how the three streams have coupled or could couple, and who the policy entrepreneur is or would need to be to do the coupling."
    - field: "window_read"
      type: "string"
      description: "Whether a policy window is open, closing, or absent -- and, if absent, what would need to change to open one."
    - field: "framework_fit_check"
      type: "string"
      description: "Whether MSF is actually the right lens for this question's time horizon, or whether the Advocacy Coalition Framework (or neither) fits better -- stated explicitly, not assumed by default."
chains_well_with:
  - "core/literature-review"
  - "core/source-verification"
  - "core/claim-verification"
  - "geography/political-geography"
  - "education/educational-policy"
  - "sociology/sociological-analysis"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Policy Process Analysis

## What This Skill Does

Answers a question the "rational policy cycle" model (identify problem -> design solution -> adopt -> implement -> evaluate) systematically gets wrong: why do technically sound solutions sit ignored for years, and why does an issue suddenly move when nothing about the underlying problem changed? Kingdon's Multiple Streams Framework (MSF) reframes agenda-setting as three largely independent streams -- problems, policy alternatives, and politics -- that develop on their own timelines and only occasionally converge. When they do converge, in a narrow and often unpredictable "policy window," a policy entrepreneur who has been waiting with a ready-made solution can couple the streams and move an issue onto the actual government agenda. This skill applies that lens to a specific policy question, and names when a longer-horizon question calls for the complementary Advocacy Coalition Framework (ACF) instead.

## Evidence Foundation

Kingdon developed MSF from extended fieldwork and interviews inside U.S. federal health and transportation policymaking, drawing on the earlier "garbage can" model of organizational decision-making (Cohen, March & Olsen) to argue that problems, solutions, and political conditions are not sequentially produced by a rational process but exist as three loosely coupled streams, each with its own actors and logic. A **policy window** -- a brief period when a problem becomes salient and the political climate is receptive -- is when a **policy entrepreneur**, who has usually been shopping a ready-made solution for years waiting for the right moment, can couple all three streams and move an item onto the decision agenda. Sabatier and Jenkins-Smith's Advocacy Coalition Framework (ACF) complements MSF at a different time horizon: rather than a single window, ACF tracks how competing coalitions -- organized around shared belief systems, not just interests -- contest a policy subsystem over a decade or more, with policy change driven by shifting external conditions and by policy-oriented learning within and across coalitions.

Both frameworks are widely taught and applied across public-policy programs and case-study literatures, which is why `evidence_strength` here is set to "moderate" rather than "strong": they are well-established *diagnostic and narrative* apparatus with real explanatory power, but -- unlike, say, Kingdon's own three streams neatly separating in practice -- they are difficult to falsify, function more as an organizing metaphor than a predictive theory, and later scholarship (including retrospectives marking MSF's fortieth anniversary) has specifically flagged this as a persistent methodological weakness rather than a settled strength.

## Procedure

1. **Pick the time horizon and framework.** A single agenda-setting episode (why did this move now?) calls for MSF. A multi-year contest between organized interests over a policy subsystem's direction calls for ACF. State this choice explicitly in `framework_fit_check` rather than defaulting to MSF because it's more familiar.
2. **Assess the problem stream independently.** How is the issue being framed and measured as a problem -- what indicators are cited, and was there a specific focusing event (a crisis, a high-profile case, a damning report) that made the problem newly visible? Note that a "problem" can exist statistically for decades without being politically recognized as one.
3. **Assess the policy stream independently.** What alternatives already exist in circulation -- from advocates, agencies, academics, think tanks -- and how technically and politically feasible is each? Kingdon's point is that solutions often precede the problems they eventually get attached to; look for a proposal that predates the moment it gained traction.
4. **Assess the politics stream independently.** National mood, organized interest group activity, and government/legislative turnover all move on their own logic, separate from the problem's severity or the policy's technical merit.
5. **Assess coupling and identify the policy entrepreneur.** State whether and how the three streams actually connected, and who did the connecting -- an individual or coalition who had a solution ready and recognized (or created) the moment to attach it to a suddenly salient problem and a receptive political climate.
6. **State the window read plainly**, distinguishing what already happened (retrospective, easier to narrate with confidence) from a forward-looking read (prospective, inherently much less certain) -- see Known Limitations.

## Example

**Input:** `policy_issue`: "Why did Brazil's Lei Maria da Penha (Law 11.340/2006), criminalizing domestic violence with specific protective mechanisms, pass in 2006 after years of prior domestic-violence bills stalling in Congress?" `time_horizon`: "A specific, relatively short window around 2005-2006."

**Output (abridged, illustrative -- treat the specific actors and sequencing as a worked example, not a fully source-verified case history):**

- **Stream analysis.** *Problem:* domestic violence against women in Brazil was already a long-documented, high-prevalence issue, but it became sharply, newly salient following the Inter-American Commission on Human Rights' 2001 ruling holding the Brazilian state internationally responsible for its own inaction in the Maria da Penha Fernandes case -- a focusing event that reframed a chronic statistic as an acute, internationally visible state failure. *Policy:* comparative domestic-violence legislation from other countries and draft bills from Brazil's feminist and human-rights movement had already been circulating for years, ready to be attached to a newly salient moment. *Politics:* a government period more receptive to social-rights legislation and an organized, well-networked feminist advocacy coalition provided the political conditions for the issue to move.
- **Coupling assessment:** The IACHR ruling supplied the problem-stream jolt; the feminist legal-advocacy coalition (with Maria da Penha Maia Fernandes herself as a visible, moral-authority figure) acted as the policy entrepreneur, coupling an already-drafted policy alternative to the newly opened window.
- **Window read:** Window opened by the international ruling and stayed open long enough (roughly 2001-2006) for the coupling to complete via sustained coalition advocacy -- consistent with MSF's expectation that windows are often opened by an external focusing event rather than by the policy stream maturing on its own schedule.
- **Framework fit check:** MSF fits well for explaining *why 2006 specifically*, given the clear, dateable focusing event. A question about the following decade's implementation and enforcement gaps would fit ACF better, tracking the sustained coalition conflict over enforcement resources and judicial application rather than a single agenda-setting moment.

## Known Limitations

- **MSF is a heuristic and narrative apparatus, not a predictive or easily falsifiable theory.** The three streams are conceptually distinct but often empirically entangled in practice, and critics (including recent fortieth-anniversary retrospectives on the framework) have specifically flagged this as an unresolved methodological weakness, not a minor caveat -- treat `stream_analysis` as an organizing lens, not a measured decomposition.
- **The framework was built from U.S. federal policymaking** (Kingdon's original interviews centered on U.S. Congress, health, and transportation policy). Applying it to parliamentary systems, coalition presidentialism, subnational government, or multi-party contexts requires real care, since the "politics stream" institutional actors and the mechanics of what counts as a policy window differ meaningfully from the single-executive, two-party U.S. case the framework was built on.
- **Retrospective coupling is far easier to narrate persuasively than prospective prediction.** This skill can explain, after the fact, why a window opened and who coupled the streams -- it is much less reliable at predicting when a future window will open, and `window_read` should say so plainly rather than project false confidence onto a forward-looking case.
- **This skill does not itself verify the specific facts about which actors did what, or confirm the worked example's details against primary sources** -- compose with `core/source-verification` and `core/claim-verification` before treating a `stream_analysis` output as an established historical record rather than an analytical hypothesis.
