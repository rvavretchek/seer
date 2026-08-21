---
name: academic-formatting-abnt
description: Format or check a Brazilian academic document's reference list, in-text citations, and document structure against ABNT (Associação Brasileira de Normas Técnicas) standards -- the regulatory formatting requirement Brazilian institutions hold academic work to, distinct from any general style guide. Use when a researcher needs a TCC, dissertação, tese, or artigo to meet ABNT NBR 6023 (references), NBR 10520 (citations), and NBR 14724 (document structure) before submission. Not for sentence-level prose quality -- use text-revision/line-editing-pt-br for that.
allowed-tools: Read, Write

skill_id: "core/academic-formatting-abnt"
domain: "core"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "ABNT NBR 6023:2018 (with Errata 2, 24.09.2020, and a further corrigenda in 2023) -- Informação e documentação: Referências -- Elaboração. The current standard governing reference-list entry format (books, articles, web sources, theses, etc.), confirmed via multiple 2023-2026 Brazilian university-library sources as still the version in force; the 2018 edition replaced NBR 6023:2002."
  - "ABNT NBR 10520:2023 (2nd edition, published 19.07.2023) -- Informação e documentação: Citações em documentos. Confirmed via multiple independent Brazilian university-library sources (UFRGS, UFMS, UFSCar, PUCRS, among others) as a real, recent revision -- the first in 21 years, replacing the 2002 edition. Governs in-text citation format: direct/indirect quotation, author-date vs. numeric systems, and apud (citation of a citation)."
  - "ABNT NBR 14724:2024 (4th edition, published 16.12.2024) -- Informação e documentação: Trabalhos acadêmicos -- Apresentação. Confirmed via multiple Brazilian university-library sources as the current edition, replacing the 2011 3rd edition. Governs required structural elements (capa, folha de rosto, resumo, sumário), margins, spacing, and pagination for TCCs, dissertations, and theses."
  - "França, J.L. et al. -- Manual para normalização de publicações técnico-científicas (Editora UFMG, multiple editions), a widely-cited secondary reference several Brazilian universities point students to alongside the raw NBR texts -- named here as a real, commonly-used secondary source, not as this skill's primary grounding."
input_schema:
  required:
    - field: "content_to_check"
      type: "string"
      description: "The document, section, reference list, or set of in-text citations to check or format against ABNT -- can be raw source metadata needing formatting, an existing reference list needing a compliance check, or a full document needing a structural review."
  optional:
    - field: "work_type"
      type: "string"
      description: "The kind of academic work -- TCC, dissertação, tese, artigo de periódico -- since NBR 14724's structural requirements (e.g. which pre-textual elements are mandatory vs. optional) vary by work type."
    - field: "citation_system"
      type: "string"
      description: "Author-date or numeric in-text citation system, if the institution or advisor has mandated one. NBR 10520 requires picking one system and using it consistently throughout the work -- never mixing both."
    - field: "institutional_manual"
      type: "string"
      description: "The researcher's own institution's manual de normalização, if one exists and has been supplied -- many Brazilian universities publish their own ABNT-based house style that may add to or narrow the bare NBR requirements, and it takes precedence over this skill's defaults when the two conflict."
output_schema:
  fields:
    - field: "formatted_references"
      type: "array"
      description: "Reference-list entries formatted per NBR 6023, one per source, in the format required for the reference list (not the in-text citation form)."
    - field: "intext_citation_check"
      type: "array"
      description: "Each in-text citation found or produced, checked against NBR 10520 -- direct vs. indirect quotation format, author-date or numeric system consistency, and correct apud usage where a source is cited via a secondary source."
    - field: "structure_check"
      type: "object"
      description: "Document-structure findings against NBR 14724 -- presence/absence and ordering of required pre-textual and post-textual elements, and any margin/spacing/pagination deviations found, each flagged with a confidence level given this skill's own verification limits (see Known Limitations)."
    - field: "verification_flags"
      type: "array"
      description: "Specific figures or clause-level details this skill could not independently confirm against the current paid/licensed NBR text and that the researcher should verify directly -- never silently presented as certain."
chains_well_with:
  - "text-revision/line-editing-pt-br"
  - "core/citation-analysis"
  - "core/academic-writing"
  - "core/literature-review"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Academic Formatting (ABNT)

## What This Skill Does

Checks or formats a Brazilian academic document against ABNT (Associação Brasileira de Normas Técnicas) standards -- the actual regulatory formatting requirement Brazilian institutions hold theses, dissertations, TCCs (trabalhos de conclusão de curso), and journal articles to, not a stylistic preference. This is a document-formatting skill covering three genuinely distinct concerns bundled under "ABNT": how a reference list entry is built (NBR 6023), how an in-text citation is written and how a quotation taken from a source cited by another source is marked (NBR 10520), and how the document itself is structured -- required sections, margins, spacing, pagination (NBR 14724). It is deliberately separate from `text-revision/line-editing-pt-br`, which handles sentence-level PT-BR prose clarity and has nothing to do with citation or document-structure formatting -- a document can be perfectly ABNT-compliant and still read poorly at the sentence level, or vice versa. ABNT is also not a "language/locale variant" the way `line-editing-en-us`/`line-editing-pt-br` are siblings of one another; it is a country-specific regulatory standard, named after the standard it implements, per `docs/skill-contract.md`'s explicit carve-out for exactly this case.

## Evidence Foundation

ABNT is Brazil's national standards body, and NBR 6023, NBR 10520, and NBR 14724 are the specific standards Brazilian universities cite when requiring "formatação ABNT" for academic work -- this isn't a style preference some institutions choose, it's the default regulatory expectation across Brazilian higher education. All three standards have been revised within the last several years, confirmed via web search against multiple independent Brazilian university-library sources (not any single source alone, since the primary NBR texts themselves are commercial/licensed documents, not freely mirrored online in full): NBR 6023 was last revised in 2018 (with an errata in 2020 and a further corrigenda in 2023); NBR 10520 had its first revision in 21 years, published 19 July 2023; NBR 14724 was revised most recently on 16 December 2024, replacing the 2011 3rd edition that most existing informal guidance online still describes. Because the two most recent revisions (NBR 10520:2023 and NBR 14724:2024) are recent enough that a large fraction of existing Brazilian-university guidance material, TCC-writing blog content, and even some institutional pages may still describe the prior edition, currency is the central risk this skill is built to manage -- not just knowing the rules, but knowing which edition's rules apply. This is why `evidence_strength` here is rated **moderate** rather than strong: the standards themselves are authoritative and mandatory, but this skill's grounding is built from corroborated secondary reporting (multiple university libraries' guidance pages, cross-checked against each other) rather than the paid primary NBR text, and some clause-level specifics could not be independently confirmed this way (see Known Limitations).

## Procedure

Treat reference-list formatting, in-text citation formatting, and document-structure checking as three separate passes -- a document can fail any one of them independently.

1. **Confirm which edition applies before doing anything else.** State explicitly that this skill is grounded in NBR 6023:2018 (errata 2020, corrigenda 2023), NBR 10520:2023 (2nd edition), and NBR 14724:2024 (4th edition) -- and flag to the researcher that if their institution's own manual de normalização specifies an older edition (some institutions lag adopting a just-published revision), the institutional manual takes precedence over this skill's defaults.

2. **Format or check the reference list (NBR 6023).** For each source: build the entry as SOBRENOME, Nome (surname in full caps, given name(s) capitalized normally) followed by title, edition (if not the first), place of publication, publisher, and year -- with the specific element order and punctuation varying by source type (book, book chapter, journal article, thesis/dissertation, web source). Flag any source type this skill's grounding couldn't confirm a precise current format for (see Known Limitations) rather than guessing at punctuation or element order.

3. **Format or check in-text citations (NBR 10520).** Determine or confirm the citation system in use (`citation_system` -- author-date or numeric) and apply it consistently; NBR 10520 explicitly prohibits mixing the two systems within one work. For each citation: distinguish direct quotation (verbatim, requiring a page number) from indirect/paraphrase citation; apply the current (2023) convention that both parenthetical and textual author-date citations use initial-cap-only surnames (e.g. `(Freire, 1987, p. 42)`), not the pre-2023 convention of full-caps surnames in parenthetical citations -- flag any source material the researcher supplies that still uses the pre-2023 all-caps parenthetical form as likely following the superseded edition. For a source cited only through another source (the researcher hasn't read the original), apply apud format in the order: original author/date/page, "apud" (italicized), citing author/date/page -- and note that only the actually-consulted (citing) source belongs in the reference list, not the original.

4. **Check document structure (NBR 14724).** Verify presence, required vs. optional status, and ordering of pre-textual elements (e.g. capa, folha de rosto, resumo, sumário) and post-textual elements appropriate to `work_type`, plus commonly-reported physical formatting: margins, line spacing, and pagination placement. Report these with the confidence level this skill can actually support -- treat commonly-reported figures (e.g. margins, spacing) as a strong default corroborated across multiple independent university sources, but flag them in `verification_flags` as worth a final check against the researcher's own institutional manual or the current NBR text directly, per Known Limitations. Note that the 2024 revision specifically requires a work be organized into "seções" (sections), not "capítulos" (chapters) -- flag documents still using "capítulo" headings as following the superseded 2011 structural convention.

5. **Surface institutional variation explicitly, never silently overrule it.** When `institutional_manual` is supplied and conflicts with this skill's ABNT-default output, state the tension and defer to the institutional manual (Constitution, Principle 6) -- Brazilian universities commonly publish their own manual de normalização that adds house-style requirements (e.g. a specific font, a required catalographic-record page) on top of bare ABNT, and a researcher's actual submission requirement is whatever their institution enforces, not this skill's generic default.

6. **Compose with `text-revision/line-editing-pt-br` for the prose itself.** This skill's output covers formatting only -- it does not touch sentence-level clarity, argument structure, or claim hedging; hand the underlying prose to `text-revision/line-editing-pt-br` (sentence-level) or `core/academic-writing` (structure/hedging) separately.

## Example

**Input:** `content_to_check`: raw source metadata -- "Paulo Freire's book *Pedagogia do Oprimido*, 17th edition, published by Paz e Terra in Rio de Janeiro, 1987" -- plus a direct quotation the researcher wants to cite, with `citation_system`: "author-date".

**Output:**

- **Reference-list entry (NBR 6023):**
  `FREIRE, Paulo. Pedagogia do oprimido. 17. ed. Rio de Janeiro: Paz e Terra, 1987.`

- **In-text citation, direct quotation, parenthetical form (NBR 10520:2023):**
  `(Freire, 1987, p. 42)` -- initial-cap surname only, per the current (2023) edition. *Flagged note:* the pre-2023 edition would have required `(FREIRE, 1987, p. 42)` in full caps for the parenthetical form; if the researcher's draft or institutional template still shows full-caps parenthetical citations, that's a signal it's following the superseded 2002 edition of NBR 10520, not an error in this skill's output.

- **In-text citation, textual/narrative form:**
  `Freire (1987, p. 42) afirma que "..."` -- textual-form citations already used initial-cap-only surnames even before 2023, so this form is unchanged by the recent revision.

- **verification_flags:** none for this example -- book reference format and author-date citation format are both well-corroborated across the sources this skill draws on. (A journal-article, web-source, or thesis reference, or an apud chain, would each carry their own specific element-order requirements not walked through in this abridged example.)

## Known Limitations

- **The primary NBR texts are commercial, licensed documents (via ABNT Coleção), not freely and fully mirrored in public search results.** This skill's grounding comes from corroborating multiple independent secondary sources (university library guidance pages, cross-checked against each other for agreement) rather than reading the canonical text directly. Where a specific figure (e.g. an exact margin measurement) is reported consistently across several independent sources, this skill treats it as a strong default -- but "strong default from corroborated secondary sources" is not the same claim as "verified against the primary standard," and the researcher should do that final check themselves, or via their institution's library, before a submission where getting a detail wrong is costly.
- **ABNT standards are revised on no fixed public schedule, and this skill's currency will decay.** NBR 10520 went 21 years (2002-2023) without revision and then changed meaningfully (e.g. the parenthetical-citation capitalization rule); NBR 14724 was revised again just over a year after that (Dec 2024). A future reader of this skill should re-verify the edition years stated here rather than assume they're still current -- this is a standing risk, not a one-time caveat that expires.
- **Institutional variation is real and takes precedence.** Many Brazilian universities (UFRGS, UFMG, FGV, and others) publish their own manual de normalização that layers additional house-style requirements on top of bare ABNT, or that may lag adopting a just-published NBR revision. This skill's output is the ABNT default, not a guarantee of matching a specific institution's actual submission requirements -- always defer to the researcher's own institutional manual when supplied, per the Procedure above.
- **ABNT NBR 14724 does not itself mandate a specific font.** Times New Roman 12 / Arial 12 for body text is overwhelmingly common convention reported by university guidance, not a hard requirement traceable to specific NBR text this skill could confirm -- flagged here rather than stated as a firm rule.
- **Adjacent structural standards are referenced but not fully detailed.** NBR 6027 (sumário/table-of-contents format) and NBR 6024 (numeração progressiva/progressive section numbering) interact with NBR 14724's structural requirements but aren't independently covered in this skill's procedure; a thorough structural check of a full thesis or dissertation should verify against those standards too rather than assuming NBR 14724 alone is sufficient.
- **This skill checks formatting, not the honesty or accuracy of a citation's use.** A citation can be perfectly ABNT-formatted and still misrepresent what the cited source actually says -- compose with `core/citation-analysis` or `core/claim-verification` for that, this skill doesn't check it.
- **Not a substitute for a human final check on formal submissions.** Given the direct cost to a student of an ABNT-formatting error in a thesis or dissertation defense, this skill's output should be treated as a strong draft/checklist pass, not a final sign-off -- a human (the researcher, an advisor, or their institution's library service) should do the final verification pass, per Constitution Principle 6.
