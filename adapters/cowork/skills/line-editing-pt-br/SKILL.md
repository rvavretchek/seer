---
name: line-editing-pt-br
description: Perform a sentence-level revision pass on a Brazilian-Portuguese (PT-BR) draft -- diagnosing genuine vices of style (prolixidade, obscuridade, ambiguity, buried emphasis) rather than mechanically imposing English norms like avoid-the-passive, and rewriting for clarity while respecting PT-BR academic prose's much higher native tolerance for nominalization and passive constructions. Use as the final polish pass on PT-BR prose whose structure and claims are already settled, standalone or after core/academic-writing. For US English-language prose, use text-revision/line-editing-en-us instead; a text-revision/line-editing-pt-pt sibling for European Portuguese doesn't yet exist -- European and Brazilian Portuguese diverge enough in register and idiom that this skill's Garcia-based diagnostics shouldn't be assumed to transfer.
allowed-tools: Read, Write

skill_id: "text-revision/line-editing-pt-br"
domain: "text-revision"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "Garcia, O.M. (2010, 27th ed.; 1st ed. 1967) -- Comunicação em Prosa Moderna (Editora FGV): the diagnostic method this skill's procedure follows -- the sentence's primary virtues (clareza, precisão, coerência, ênfase -- clarity, precision, coherence, emphasis) checked against its classic vices of style (vícios de linguagem: prolixidade, obscuridade, ambiguidade, cacófato, pleonasmo -- wordiness, obscurity, ambiguity, cacophony, redundancy). The canonical Brazilian reference for sentence- and paragraph-level revision, still assigned in Brazilian university writing courses (e.g. USP's Letras program) as of this skill's authoring."
input_schema:
  required:
    - field: "draft"
      type: "string"
      description: "The Brazilian-Portuguese (PT-BR) prose to line-edit, sentence by sentence or paragraph by paragraph."
  optional:
    - field: "register"
      type: "string"
      description: "The target register or venue, if it should constrain how far to simplify -- an official/legal register (linguagem jurídica or redação oficial) tolerates a formality and periphrasis that an academic-journal register would not, and core/academic-writing may already have decided what's appropriate for the genre."
output_schema:
  fields:
    - field: "edited_draft"
      type: "string"
      description: "The revised prose, with only sentence-level changes applied."
    - field: "diagnostics"
      type: "array"
      description: "For each substantively changed sentence: which vício de linguagem it exhibited (prolixidade, obscuridade, ambiguidade, ênfase mal colocada, etc.), and what changed and why -- explicitly not flagging plain passive voice or nominalization as a defect on their own, since PT-BR tolerates both natively."
    - field: "untouched_notes"
      type: "string"
      description: "Explicit confirmation of what this pass did NOT touch -- argument structure, claim hedging, genre moves -- marking the boundary with core/academic-writing and core/peer-review."
chains_well_with:
  - "core/academic-writing"
  - "core/peer-review"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Line Editing (Portuguese / PT-BR)

## What This Skill Does

Performs the sentence-level revision pass on a Brazilian-Portuguese draft: taking prose that is already structurally sound and argumentatively complete, and making each sentence say what it means as directly as its own language's conventions call for -- not as directly as English would demand. This is deliberately narrower than `core/academic-writing`, which handles genre structure, move analysis, and calibrating a claim's hedging to its evidence; line editing assumes those decisions are already made and correct. Its job is exclusively the sentence: is it needlessly padded (prolixidade), does it leave the reader unsure what a pronoun or a phrase like "o processo mencionado" actually refers to (obscuridade), does it say the same thing twice (pleonasmo/redundância), and does its real point land where the reader's attention falls (ênfase). This skill exists as a sibling to, not a Portuguese "mode" of, `text-revision/line-editing-en-us`: PT-BR academic prose has its own real stylistic tradition, with its own diagnostic vocabulary for what counts as a defect, and mechanically importing an English clarity norm (e.g. treating all passive voice or nominalization as suspect) misdiagnoses prose that is, by PT-BR's own standard, perfectly fine.

## Evidence Foundation

Othon M. Garcia's *Comunicação em Prosa Moderna* (1st ed. 1967; the widely-cited 27th edition, Editora FGV, 2010) is the classic and still-assigned Brazilian reference for sentence-level revision -- built on Garcia's premise that learning to write well requires first learning to organize thought, and that a sentence's problems are usually thinking problems wearing a grammatical disguise. Garcia names the sentence's primordial virtues as **clareza** (clarity -- the reader gets the intended meaning without re-reading), **precisão** (precision -- words chosen for their exact sense, not an approximate one), **coerência** (coherence -- the sentence's parts and the paragraph's sentences hang together logically), and **ênfase** (emphasis -- the sentence's real point occupies a position of prominence, not a subordinate afterthought) -- a structure that maps onto Williams & Bizup's clarity/cohesion/emphasis triad for English, but developed independently, for Portuguese, from Portuguese prose. Against these virtues, Garcia catalogs the concrete **vícios de linguagem** (vices of style) that undermine them: **prolixidade** (padding a simple idea in redundant words and periphrasis -- classic Brazilian *burocratês*, bureaucratic circumlocution), **obscuridade** (vague antecedents, buried referents, syntax so tangled the reader loses the thread), **ambiguidade** (a construction that genuinely supports two readings), **cacófato** (an accidental, distracting sound produced where two words meet), and **pleonasmo**/redundância (saying the same thing twice without added precision). Critically, Garcia's diagnostic apparatus does not include "avoid the passive voice" or "avoid nominalization" as vices -- both are native, unmarked constructions in Portuguese academic and official registers, and this skill inherits that boundary deliberately rather than importing it from the English-language tradition.

## Procedure

1. **Check clareza and precisão first**: read the sentence for whether a first-pass reader would get the intended meaning without re-reading, and whether each word choice is exact rather than approximate. Do not flag passive voice (`foi analisado`, `foi constatado`) or a nominalization (`a análise`, `a constatação`) as a problem on their own -- both are unmarked in PT-BR academic registers; only flag them if they specifically obscure who is doing what and that ambiguity matters to the sentence's meaning.
2. **Check for prolixidade** (padding): look for periphrastic constructions that wrap a simple action in extra verbal layers -- "foi realizada uma análise no sentido de se verificar a possibilidade de..." instead of "analisou-se se..." -- and for stock bureaucratic filler ("tendo em vista o fato de que," "no sentido de," "com o objetivo de proceder a"). Cut or compress; this is the single most common vício in Brazilian academic and institutional prose.
3. **Check for obscuridade** (unclear referents): flag any pronoun, demonstrative, or vague noun phrase ("o referido processo," "a matéria em questão," "tal fato") whose antecedent isn't unambiguous from context, and either name the referent concretely or flag it back to the writer if the ambiguity might be intentional/load-bearing.
4. **Check for ambiguidade and cacófato**: read the sentence for a genuine double reading (a modifier that could attach to either of two nouns, an ellipsis that drops necessary information) and for accidental cacophonous word-boundary collisions (e.g. "por cada" strings that produce an unintended word); fix both, since neither is stylistically defensible in any register.
5. **Check ênfase**: find the sentence's real point and see whether it's stranded in a subordinate clause (a common pattern: the actual finding trails off after "tendo em vista que...") while a minor detail occupies the sentence's prominent position. Restructure so the point lands where the reader's attention actually is, per Garcia's coerência/ênfase pairing -- without imposing the English convention that this position must always be the sentence's literal end; PT-BR syntax has more flexibility here.
6. **Do not touch anything above the sentence, and do not "fix" what isn't broken by PT-BR's own standard.** Do not reorder paragraphs, do not add or remove a claim, do not change a hedge, and do not convert a passive or nominalized construction to active voice unless it is also implicated in an actual vício (prolixidade, obscuridade) diagnosed above -- if in doubt whether a construction is a real vício or simply idiomatic PT-BR density, flag rather than silently rewrite. Report the boundary explicitly in `untouched_notes`.
7. **Explain each substantive change** by naming the specific vício it addressed (prolixidade, obscuridade, ambiguidade, cacófato, pleonasmo, ênfase mal colocada), not just presenting a diff -- the writer needs the diagnostic vocabulary to self-correct next time, not just a cleaned-up sentence.

## Example

**Input:** `draft`: "Foi realizada, por parte da comissão, uma análise no sentido de se verificar a possibilidade da realização de uma reavaliação do processo de avaliação anteriormente mencionado, tendo em vista o fato de que não houve, até o presente momento, um posicionamento definitivo a respeito da matéria em questão."

*(Literal gloss: "An analysis was carried out, on the part of the committee, in the sense of verifying the possibility of the carrying-out of a reassessment of the aforementioned evaluation process, given the fact that there has not been, up to the present moment, a definitive position with respect to the matter in question.")*

**Output (abridged):**

- **Edited draft:** "A comissão analisou se seria possível reavaliar o processo, já que ainda não houve posicionamento definitivo sobre o caso."

  *(Gloss: "The committee examined whether it would be possible to reassess the process, since there has not yet been a definitive position on the matter.")*

- **Diagnostics:** (1) **Prolixidade** -- "foi realizada, por parte da comissão, uma análise no sentido de se verificar a possibilidade da realização de uma reavaliação" wraps a single action (a comissão analisou se seria possível reavaliar) in four nested layers of nominalization and periphrasis, classic *burocratês*; compressed to the direct verb form. Note this is *not* "passive voice is bad" -- the original's problem is the padding, not that "foi realizada" is passive; a tighter passive construction would have been left alone. (2) **Obscuridade** -- "o processo de avaliação anteriormente mencionado" and "a matéria em questão" are vague back-references; since the antecedent is recoverable from context here, both were replaced with the concrete "o processo" and "o caso" rather than left as filler cross-references. (3) **Ênfase** -- the sentence's real point (no definitive position exists yet) was stranded in a trailing "tendo em vista o fato de que" clause; tightened into a direct causal clause ("já que...") that still trails the main clause, per PT-BR's own syntactic norm -- not forced into English's stress-final-position convention.
- **Untouched notes:** No claim was added, removed, or re-hedged -- the committee's action (examining feasibility, not yet deciding) is preserved exactly. No passive construction or nominalization was removed simply for being passive or nominalized; both are unmarked in this register and only the genuinely padded, four-layer version was compressed. Structure and genre (this reads as an internal institutional note) were not altered.

## Known Limitations

- **This skill is scoped to Brazilian-Portuguese (PT-BR) prose and doesn't transfer to English or to other Portuguese varieties.** European Portuguese (PT-PT) and other national varieties have their own stylistic norms that Garcia's method, developed specifically from Brazilian usage, was not built to diagnose; for US English drafts, use `text-revision/line-editing-en-us` instead -- these are deliberate siblings, not one method with a language switch. A PT-PT sibling would need its own real grounding from a European-Portuguese reference, not this skill relabeled.
- **The core risk this skill exists to prevent is over-correction toward an English norm** -- treating PT-BR's native tolerance for nominalization and the passive voice as a defect. Every diagnostic step above is written to catch a genuine vício (prolixidade, obscuridade, ambiguidade) rather than a construction that is simply idiomatic PT-BR density; when a change can't be pinned to one of Garcia's named vices, the default is to flag it to the writer rather than rewrite it.
- **Garcia's most recent edition is from 2010 (the work itself dates to 1967)** and its harsher judgments on some colloquialisms or newer usages may be more conservative than a specific contemporary venue wants (a blog, a preprint, an interdisciplinary journal with looser conventions); treat Garcia's vices as a strong default, not an inflexible rule, and flag a genre mismatch rather than enforce silently.
- **This skill has no way to check whether the sentence it just made clearer is actually true or well-supported.** A clean, direct sentence stating a false or unsupported claim is now a clean, direct, *more persuasive* false or unsupported claim -- compose with `core/peer-review` or `core/claim-verification` rather than treating a line-edited draft as validated.
- **Style has a genuine subjective component.** A writer's voice and rhythm preferences can legitimately override this skill's suggestions; the diagnostics explain a defensible reading of what's working against the reader by PT-BR's own stylistic tradition, not an objectively "correct" sentence (Constitution, Principle 6).
