---
name: line-editing-en-us
description: Perform a sentence-level revision pass on a US English-language draft -- diagnosing why a sentence reads as dense or confusing (buried actions, missing character-subjects, misplaced emphasis, needless words) and rewriting it for clarity, without touching argument structure, claim hedging, or genre conventions. Grounded in US style references; British English has its own idiosyncrasies (-ise/-ize, differing register conventions) this skill doesn't diagnose -- see text-revision/line-editing-en-uk if one exists, or contribute one. Use as the final polish pass on English prose whose structure and claims are already settled, standalone or after core/academic-writing. For Brazilian-Portuguese prose, use text-revision/line-editing-pt-br instead.
allowed-tools: Read, Write

skill_id: "text-revision/line-editing-en-us"
domain: "text-revision"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Williams, J.M. & Bizup, J. (2017, 12th ed.) -- Style: Lessons in Clarity and Grace (Pearson): the diagnostic method this skill's procedure follows -- locate a sentence's real characters and actions, check its old-to-new information flow (cohesion), and place its point in the stress position (emphasis)."
  - "Strunk, W. & White, E.B. (1979, 3rd ed.) -- The Elements of Style (Macmillan): the classic complementary rules this skill also applies -- omit needless words, prefer the active voice, put statements in positive form."
input_schema:
  required:
    - field: "draft"
      type: "string"
      description: "The English-language prose to line-edit, sentence by sentence or paragraph by paragraph."
  optional:
    - field: "register"
      type: "string"
      description: "The target register or venue, if it should constrain how far to simplify -- a technical/legal register may need to keep some density that core/academic-writing already decided was appropriate for the genre."
output_schema:
  fields:
    - field: "edited_draft"
      type: "string"
      description: "The revised prose, with only sentence-level changes applied."
    - field: "diagnostics"
      type: "array"
      description: "For each substantively changed sentence: what made it dense or unclear (buried action, missing character-subject, broken cohesion, misplaced emphasis, needless words), and what changed and why."
    - field: "untouched_notes"
      type: "string"
      description: "Explicit confirmation of what this pass did NOT touch -- argument structure, claim hedging, genre moves -- marking the boundary with core/academic-writing and core/peer-review."
chains_well_with:
  - "core/academic-writing"
  - "core/peer-review"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Line Editing (English, US)

## What This Skill Does

Performs the sentence-level revision pass on an English-language draft: the work of taking prose that is already structurally sound and argumentatively complete, and making each sentence say what it means as directly as possible. This is deliberately narrower than `core/academic-writing`, which handles genre structure, move analysis, and calibrating a claim's hedging to its evidence. Line editing assumes those decisions are already made and correct -- its job is exclusively the sentence: is the actor doing the action named as the subject and verb, does each sentence hand off cleanly to the next, does the sentence's real point land where a reader's attention actually falls, and is every word in the sentence earning its place. A draft can pass a full peer review on structure and evidence and still read as exhausting to get through -- that gap is this skill's job to close. This skill is scoped to US English prose specifically -- grounded in US style references (Williams & Bizup, Strunk & White), not British, Australian, or other English-variant conventions, which have their own real idiosyncrasies this skill doesn't diagnose. For Brazilian-Portuguese academic prose, see `text-revision/line-editing-pt-br`, which is grounded in its own real diagnostic tradition rather than this method applied mechanically to a different language.

## Evidence Foundation

Williams & Bizup's *Style: Lessons in Clarity and Grace* supplies this skill's diagnostic core: readers process a sentence more easily when its grammatical subject names the sentence's real "character" and its main verb names that character's real "action" -- prose gets dense specifically when actions are buried inside abstract nouns (nominalizations: "there was a *reduction* in enrollment" instead of "enrollment *fell*") and the grammatical subject becomes something abstract instead of the actual agent. Williams & Bizup add two further diagnostics this skill applies: **cohesion** (each sentence should open with information the reader already has and close with what's new, so a paragraph reads as a chain rather than a list) and **emphasis** (a sentence's most important point should land in its final "stress position," not be buried mid-sentence). Strunk & White's *The Elements of Style* supplies the complementary, older, more aphoristic layer this skill also applies -- omit needless words, prefer the active voice, put statements in positive form -- rules that remain a reasonable default for concision even though Williams & Bizup's method is the more systematic diagnostic for *why* a specific sentence isn't working.

## Procedure

1. **Read for the sentence's real character and action**, not just its grammatical subject and verb. If the subject is abstract ("the implementation of the policy resulted in...") and the actual agent and action are buried in a nominalization further in, that's the first thing to fix: surface the real actor as subject, the real action as verb.
2. **Check cohesion across sentence boundaries.** Each sentence should generally open with something the previous sentence already established and introduce new information toward its end. Where a paragraph jumps between unrelated grammatical subjects sentence to sentence, the reader has to work to reconnect the thread -- flag and fix.
3. **Check emphasis.** Find the sentence's actual point and see where it falls. If it's buried in a subordinate clause or the middle of a long sentence while the end trails off on something minor, restructure so the point lands in the stress position (the sentence's end).
4. **Apply concision rules**: cut needless words, prefer active voice unless the passive is doing real work (e.g. correctly de-emphasizing an unknown or unimportant agent), replace a string of prepositional phrases with a more direct construction where possible.
5. **Do not touch anything above the sentence.** Do not reorder paragraphs, do not add or remove a claim, do not change a hedge ("suggests" vs "shows") even if the line editor's ear wants to -- if a claim's hedging looks wrong, that's a finding to hand back, not a change to make silently inside a line-editing pass. Report this boundary explicitly in `untouched_notes`.
6. **Explain each substantive change**, not just present a diff -- the writer needs to see *why* a sentence was rewritten (buried action, broken cohesion, misplaced emphasis, excess words) to internalize the pattern, not just receive a cleaned-up version.

## Example

**Input:** `draft`: "A determination was made by the committee that further consideration of the proposal would be beneficial, given the fact that there was insufficient information provided regarding the methodology in the version that was originally submitted."

**Output (abridged):**

- **Edited draft:** "The committee decided the proposal needed further review, because the original submission didn't describe the methodology in enough detail."
- **Diagnostics:** (1) Buried action -- "a determination was made by the committee" nominalizes "decided" and pushes the real actor (the committee) out of subject position; restored to "the committee decided." (2) Needless words -- "given the fact that," "there was... provided regarding" both cut per Strunk & White's omit-needless-words rule. (3) Cohesion/emphasis -- the original's real point (methodology wasn't described in enough detail) was buried in a trailing subordinate clause; moved to a direct causal clause that lands the point instead of trailing off on "the version that was originally submitted."
- **Untouched notes:** No claim was added, removed, or re-hedged -- "needed further review" preserves exactly the committee's stated judgment, not a stronger or weaker one. Structure and genre (this reads as an internal committee note, not a journal-article move) were not altered.

## Known Limitations

- **This skill is built specifically for US English prose** (Williams & Bizup and Strunk & White are both US style references) and doesn't transfer mechanically to other English varieties or other languages. British, Australian, and other English conventions have their own real register and spelling idiosyncrasies this skill doesn't diagnose -- a `text-revision/line-editing-en-uk` sibling would need its own real grounding, not this skill relabeled. For Brazilian-Portuguese academic prose specifically -- which tolerates nominalization and passive constructions far more comfortably than the English standard this skill is grounded in -- use `text-revision/line-editing-pt-br` instead.
- **Simplifying a sentence can accidentally remove real technical precision.** Some density is load-bearing -- legal, statistical, and technical claims sometimes need a qualifier or a nominalization that a line editor without domain expertise might cut in the name of clarity. When in doubt, flag rather than silently simplify.
- **This skill has no way to check whether the sentence it just made clearer is actually true or well-supported.** A clean, direct sentence stating a false or unsupported claim is now a clean, direct, *more persuasive* false or unsupported claim -- compose with `core/peer-review` or `core/claim-verification` rather than treating a line-edited draft as validated.
- **Style has a genuine subjective component.** A writer's voice and rhythm preferences can legitimately override this skill's suggestions; the diagnostics explain a defensible reading of what's working against the reader, not an objectively "correct" sentence (Constitution, Principle 6).
