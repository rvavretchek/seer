---
name: cognitive-bias-analysis
description: Identify which cognitive biases are plausibly shaping a specific judgment, decision, or piece of reasoning -- grounded in Kahneman & Tversky's heuristics-and-biases program -- and assess how well-evidenced each flagged bias actually is, rather than reflexively naming a bias to explain any disagreement or error. Use to audit a decision process, a study/survey design, or an argument for likely systematic distortion.
allowed-tools: Read, Write

skill_id: "cognitive-psychology/cognitive-bias-analysis"
domain: "cognitive-psychology"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Tversky, A. & Kahneman, D. (1974) -- Judgment under Uncertainty: Heuristics and Biases, Science 185(4157): 1124-1131: the foundational identification of the representativeness, availability, and anchoring-and-adjustment heuristics and the systematic biases each produces."
  - "Kahneman, D. & Tversky, A. (1979) -- Prospect Theory: An Analysis of Decision under Risk, Econometrica 47(2): 263-291: loss aversion and the systematic effect of gain/loss framing on choice under risk, work recognized in Kahneman's 2002 Nobel Memorial Prize in Economic Sciences."
  - "Kahneman, D. (2011) -- Thinking, Fast and Slow (Farrar, Straus and Giroux): the dual-process System 1 (fast, associative, heuristic-driven) / System 2 (slow, effortful, rule-based) synthesis this skill's diagnostic procedure follows, building on Stanovich & West's (2000) dual-process terminology."
input_schema:
  required:
    - field: "reasoning_or_decision"
      type: "string"
      description: "The judgment, decision, argument, or process being examined for bias."
  optional:
    - field: "decision_context"
      type: "string"
      description: "Stakes, time pressure, and information available at the time -- affects which biases are plausible, since System 1 dominance is more likely under time pressure or high cognitive load."
    - field: "domain_of_judgment"
      type: "string"
      description: "What kind of judgment this is -- probability estimate, risk/loss-framed choice, causal attribution, frequency judgment -- since specific biases attach to specific judgment types."
output_schema:
  fields:
    - field: "biases_flagged"
      type: "array"
      description: "Each candidate bias, the specific textual or behavioral evidence pointing to it, and how strong the match is -- never a generic, unanchored list of possible biases."
    - field: "system_read"
      type: "string"
      description: "Whether the reasoning shows signs of System 1 (fast, heuristic) dominance without visible System 2 correction, and what conditions -- time pressure, cognitive load, high expertise, low stakes -- plausibly explain that."
    - field: "evidence_strength_per_bias"
      type: "array"
      description: "For each flagged bias, how well-replicated its evidence base is and how directly it applies to this case -- distinguishing robust, heavily replicated effects from popularized but weaker or more contested ones."
    - field: "debiasing_note"
      type: "string"
      description: "What, if anything, evidence-based debiasing research suggests could counter the specific bias flagged, with explicit caution about how modest most debiasing effects actually are."
chains_well_with:
  - "core/peer-review"
  - "core/claim-verification"
  - "core/academic-writing"
  - "education/learning-theory"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Cognitive Bias Analysis

## What This Skill Does

Examines a specific judgment, decision, or piece of reasoning for signs of systematic cognitive bias, grounded in the Kahneman & Tversky heuristics-and-biases research program rather than in the much looser, popularized "list of 180 cognitive biases" that circulates outside the original science. The point is not to reflexively attach a bias name to any reasoning the analyst disagrees with -- that itself is a bias-flavored error -- but to identify the *specific* heuristic plausibly at work, point to the *specific* textual or behavioral evidence for it, and be honest about how strong the underlying evidence for that particular effect actually is. This is useful for auditing a decision-making process (a review panel, a policy choice), a study or survey design for likely respondent or researcher bias, or an argument for a specific, nameable reasoning shortcut rather than a vague "this seems biased."

## Evidence Foundation

Tversky & Kahneman's 1974 *Science* paper established that people routinely judge probability and frequency using a small set of heuristics -- representativeness (judging by resemblance to a prototype, ignoring base rates), availability (judging frequency by how easily examples come to mind), and anchoring-and-adjustment (insufficiently adjusting away from an initial reference value) -- each of which is efficient in general but produces predictable, systematic errors in specific circumstances. Kahneman & Tversky's 1979 prospect theory paper extended this to choice under risk, establishing loss aversion (losses loom larger than equivalent gains) and framing effects (the same outcome, described as a gain vs. a loss, changes the choice people make) as robust, replicable phenomena -- work later recognized with the 2002 Nobel Memorial Prize in Economic Sciences. Kahneman's 2011 synthesis, *Thinking, Fast and Slow*, organizes this program under the dual-process System 1 / System 2 framing (building on earlier dual-process terminology from Stanovich & West): System 1 is fast, automatic, and heuristic-driven; System 2 is slow, effortful, and rule-based, and typically only engages -- and typically only *corrects* System 1's output -- under specific conditions (motivation, time, low load). `evidence_strength` is set to "strong" because the core program (anchoring, framing/loss aversion, availability) has held up unusually well across large-scale, pre-registered replication efforts, unlike some other social-psychology findings from the same era -- but see Known Limitations for where that strength does and does not extend.

## Procedure

1. **Identify the judgment type first.** Different heuristics attach to different kinds of judgment: representativeness to categorization and probability-from-resemblance judgments; availability to frequency or likelihood judgments based on how easily instances come to mind; anchoring to numeric estimation tasks; loss aversion and framing to choices under risk. Use `domain_of_judgment` to narrow which biases are even plausible before looking for evidence of any of them.
2. **Look for the specific signature, not the vibe.** For each candidate bias, point to the exact textual or behavioral evidence -- the specific number that functioned as an anchor, the specific vivid-but-unrepresentative example that was overweighted, the specific way a choice was framed as a loss rather than a gain. A bias flagged without a specific pointer to the evidence for it is not a finding.
3. **Assess System 1 vs. System 2 involvement** using `decision_context`. Time pressure, high cognitive load, low stakes, and high confidence going in are all conditions under which System 1 output is more likely to go uncorrected; deliberate, slow, high-stakes review with adequate time is more consistent with System 2 engagement, even if a heuristic still shaped the initial impression.
4. **Rate evidence strength per bias, not just once for the whole analysis.** Anchoring and loss-aversion/framing effects are among the most heavily replicated findings in the whole heuristics-and-biases literature; some biases that circulate in popular "bias list" culture are extensions, rebrandings, or considerably thinner-evidenced derivatives of the original program. Say explicitly which category a flagged bias falls into.
5. **State a debiasing note cautiously.** Evidence-based interventions exist (consider-the-opposite prompts, structured checklists, blinded review, forced delay before deciding) and have real but typically modest, inconsistent, context-dependent effects -- never imply that naming a bias reliably fixes it.
6. **Explicitly separate "this looks biased" from "this judgment happens to be wrong for other reasons."** A judgment can be wrong, or one the analyst disagrees with, without any specific heuristic being demonstrably at work -- state when the evidence doesn't clearly support a bias-based explanation rather than defaulting to one because it's available (itself a mild irony worth noticing).

## Example

**Input:** `reasoning_or_decision`: "A grant review panel rejected a proposal as 'unlikely to work,' a judgment reached in discussion within the first few minutes of reading the opening paragraphs, which described an unconventional experimental method; the panel's written notes do not reference the proposal's preliminary data, presented three pages later, which showed a significant positive effect using that method." `decision_context`: "Panel reviewed twelve proposals in one afternoon session; each proposal had a fixed 15-minute discussion slot."

**Output (abridged):**

- **Biases flagged:** (1) *Anchoring* -- the panel's judgment formed within minutes of an early, unconventional-methods framing and shows no evidence of adjustment after later, contradicting evidence (the positive preliminary data) appeared; the early impression functioned as an anchor the rest of the read didn't move. (2) *Representativeness* -- "unconventional method" likely made the proposal a poor match to the panel's implicit prototype of a "fundable proposal," inviting a probability judgment ("unlikely to work") based on resemblance to type rather than on the actual evidence presented.
- **System read:** Conditions (twelve proposals, fixed 15-minute slots, single afternoon session) are a textbook trigger for System 1 dominance -- time pressure and volume both push toward fast, heuristic-driven judgment with reduced System 2 correction, consistent with a judgment locked in before the full proposal, including its strongest evidence, was actually weighed.
- **Evidence strength per bias:** Anchoring is one of the most heavily and consistently replicated effects in the entire heuristics-and-biases literature -- high confidence in the general mechanism, though this specific case is an inference from the panel's process and written notes, not a direct measurement of any individual reviewer's cognition. Representativeness is also well-established but harder to pin down precisely here without knowing the panel's actual implicit prototype.
- **Debiasing note:** Structured review protocols that require reviewers to log an initial rating *and* a rating after reading preliminary data separately, or that require the full proposal to be read before any rating is entered, are evidence-supported partial mitigations for exactly this pattern -- but debiasing effects at the panel level are typically modest, not a guarantee the same pattern won't recur.

## Known Limitations

- **Bias attribution from text or behavior alone is inferential, not a direct measurement of anyone's actual cognition.** This skill flags a plausible pattern consistent with a named bias; it cannot prove what happened inside a specific person's mind, and a flagged bias should never be presented as a diagnosed fact about the reasoner rather than an evidenced inference.
- **Not all "cognitive biases" in popular circulation carry the same evidence weight as the original Kahneman & Tversky program.** Anchoring, loss aversion, and framing effects have replicated robustly, including in large-scale, pre-registered replication projects; many entries in the popularized "cognitive bias list" that has grown well beyond the original research are derivative, thinner-evidenced, or in some cases specifically contested -- this skill should say which category applies rather than treating the whole catalog as uniformly well-established.
- **Heuristics that produce errors on laboratory tasks are often adaptively accurate in natural environments** -- the ecological-rationality critique (associated with Gigerenzer and others) is a real, unresolved tension within the field, not a fringe objection: flagging that a heuristic was used is not automatically evidence that the resulting judgment was wrong.
- **Real-world decisions are rarely explained by a single bias in clean isolation**, and this skill's per-bias evidence ratings describe the general research literature's strength, not a certainty about this specific case -- treat `biases_flagged` as the most defensible reading available, not a settled verdict.
- **Debiasing research shows most interventions produce small, inconsistent, and context-dependent effects.** This skill should never imply that naming a bias, on its own, reliably corrects it.
