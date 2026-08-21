---
name: literature-review
description: Conduct a systematic literature review on an academic topic, organized by theme with full citation tracking. Use when the researcher asks for a literature review, a survey of a research area, or a "what does the literature say about X" style question.
allowed-tools: Bash, Read, Glob, Grep, Write

skill_id: "core/literature-review"
domain: "core"
version: "0.1.0"
evidence_strength: "strong"
evidence_sources:
  - "PRISMA 2020 (Page et al., 2021) — reporting standard for systematic reviews and meta-analyses; this skill's scope/search/triage/synthesis structure follows its core logic (though it is not a full PRISMA implementation — no formal risk-of-bias assessment)."
input_schema:
  required:
    - field: "topic"
      type: "string"
      description: "The research question or topic to survey."
  optional:
    - field: "year_range"
      type: "string"
      description: "Publication window to search. Defaults to the last 5 years."
    - field: "target_venues"
      type: "string"
      description: "Specific journals, conferences, or communities to prioritize, if any."
    - field: "desired_paper_count"
      type: "integer"
      description: "Target number of core papers in the final review. Defaults to 15-20."
output_schema:
  fields:
    - field: "field_overview"
      type: "string"
      description: "Narrative summary of the field and how it has evolved."
    - field: "themes"
      type: "array"
      description: "Findings grouped by theme (not by paper), each with the methods/approaches compared and results."
    - field: "open_questions"
      type: "array"
      description: "Gaps and contradictions surfaced across the reviewed literature."
    - field: "references"
      type: "array"
      description: "Full reference list (paper IDs, URLs) with BibTeX entries."
chains_well_with:
  - "core/source-verification"
  - "core/citation-analysis"
  - "core/academic-writing"
  - "core/claim-verification"
license: "CC BY-SA 4.0"
provenance: "forked:collaborative-deep-research/agent-papers-cli@23a1941, adapted to the Seer skill contract"
---

# Literature Review

## What This Skill Does

Conducts a systematic review of the academic literature on `{{topic}}`: defines scope, searches multiple sources with query variation, triages results for relevance, reads the most relevant papers in depth, follows the citation graph to catch what a single search misses, and produces a theme-organized report — never a paper-by-paper list.

## Evidence Foundation

The scope → search → triage → deep-read → citation-graph → thematic-synthesis structure follows the core logic of PRISMA 2020 (Page et al., 2021), the dominant reporting standard for systematic reviews. This is a lightweight application, not a full PRISMA implementation: it does not include formal risk-of-bias assessment or a pre-registered protocol, which matters for a rigorous meta-analysis but is appropriate overhead for the kind of literature-grounding a researcher needs before writing or arguing a position.

## Procedure

### 1. Define Scope

Before searching, clarify:
- Topic boundaries and key terms
- Year range (default: `{{year_range}}`, or last 5 years if not given)
- Target venues or communities: `{{target_venues}}`
- Desired number of core papers: `{{desired_paper_count}}` (default: 15-20)

### 2. Multi-Query Search

Search with multiple query variations to maximize coverage — a single query systematically under-covers a field. Use available academic search backends (e.g. Semantic Scholar, Google Scholar, PubMed) with the main query, a synonym query, and a related-concept query. Deduplicate results by title/paper ID.

### 3. SciELO Direct Access for Portuguese-Language / Brazil-Specific Coverage

For Brazil-focused or Portuguese-language topics, supplement Step 2's search backends with a direct call to SciELO's own **Article Meta API** (`https://articlemeta.scielo.org`) — free, keyless, JSON, maintained by SciELO itself. It exists specifically because Semantic Scholar, Google Scholar, and PubMed under-index Portuguese-language and Latin American scholarship (see Known Limitations) — this is SciELO's own metadata filling that gap directly, not a third party's filtered view of it.

**This API returns metadata only** — title, authors, full abstract, DOI, dates, keywords — never the article's full text. A `200` response means a candidate paper was found for Triage, not that the paper has been retrieved; do not treat it as equivalent to having the PDF in hand.

Useful endpoints:
- `GET https://articlemeta.scielo.org/api/v1/collection/` — list SciELO's national collections (`scl` = Brazil)
- `GET https://articlemeta.scielo.org/api/v1/journal/?collection=scl&issn=<ISSN>` — journal-level metadata
- `GET https://articlemeta.scielo.org/api/v1/article/identifiers/?collection=scl&issn=<ISSN>` — article identifiers (`code`) within a journal, for enumerating what's available
- `GET https://articlemeta.scielo.org/api/v1/article/?collection=scl&code=<code>` — full metadata for one article

```bash
curl "https://articlemeta.scielo.org/api/v1/article/?collection=scl&code=<article-code>"
```

The response uses SciELO's legacy ISIS/CDS-style bibliographic tags rather than named fields — the ones a literature review actually needs:

| Tag | Field |
|---|---|
| `v12` | Title |
| `v10` | Authors — a list of entries, typically split into surname/given-name sub-fields rather than one combined string; parse accordingly |
| `v83` | Abstract |
| `v65` | Publication date, `YYYYMMDD` — the year is the first four digits |
| `v237` | DOI |

`v12`, `v83`, and `v10` were confirmed directly against a live response in this project's connector research (`adapters/cowork/CONNECTORS.md`); `v65` and `v237` follow the same standard ISIS tag scheme SciELO's own `xylose` library documents but weren't independently re-verified here — confirm against an actual response before relying on them for a specific article. Most tags are lists of objects rather than flat strings (ISIS fields can repeat, e.g. once per language) — the text itself is usually under a `_` key, e.g. `article["v12"][0]["_"]` for the primary-language title.

**Does not solve full-text retrieval.** Direct fetches of the reader-facing site (`www.scielo.br/j/.../a/...`) return `403` from bot protection regardless of User-Agent, including with `?format=pdf` — confirmed in `CONNECTORS.md`'s research. Use this API for discovery and triage metadata only; getting the full text of a SciELO-indexed article still requires whatever access the researcher already has (institutional access, the journal's own site, etc.), not this API.

### 4. Triage

For each unique paper found, pull its metadata and skim its abstract/opening. Categorize as **highly relevant** / **somewhat relevant** / **not relevant**.

### 5. Deep Analysis

For highly relevant papers, read introduction, method, results, and conclusion. Take structured notes: problem, method, key results, limitations.

### 6. Citation Graph Exploration

For seminal papers, pull their citations and references to find related work a keyword search would miss. Add anything important discovered this way back into Triage.

### 7. Produce Report

Organize findings **by theme, not by paper**:
- Overview of the field and its evolution
- Key methods and approaches, compared
- Main results and findings
- Open questions and contradictions
- Complete reference list with BibTeX entries

## Example

**Input:** `topic: "AI-generated feedback in secondary education"`, `year_range: "2018-2026"`

**Output (excerpt):**

> **Field overview:** Research on AI-generated feedback has shifted from feasibility studies (can an LLM produce fluent feedback?) to quality studies (is that feedback pedagogically effective?) since around 2022...
>
> **Theme: Positivity bias in LLM feedback.** Multiple studies (Dai et al., 2023; ...) find LLM-generated feedback skews toward excessive positivity and vague suggestions, converging with earlier human-feedback research on the harm of unearned praise (Kluger & DeNisi, 1996)...
>
> **Open questions:** Longitudinal effects of AI feedback on student self-efficacy remain largely unstudied...

## Known Limitations

- **Database coverage is English- and Global-North-skewed.** Semantic Scholar, Google Scholar, and PubMed under-index Portuguese-language and Latin American academic output — a real gap for Brazil-focused research (e.g. Geography Education). Step 3 (SciELO direct access) narrows this specific gap for metadata/discovery — SciELO indexes exactly the Portuguese-language, Brazil-based scholarship those three backends under-index — but it does not close it: the Article Meta API returns metadata only, never full text (direct fetches of `www.scielo.br` article pages return 403 from bot protection, key and User-Agent notwithstanding), and CAPES coverage is still not integrated into this skill's search step at all — cross-check CAPES-indexed Brazilian topics manually until it is.
- **No built-in fact-checking of claims inside the papers themselves** — this skill reports what papers claim, not whether those claims replicate. Compose with a claim-verification skill for that.
- **Requires external search-API access** (the underlying tool layer needs API keys for Semantic Scholar / Serper / Jina-equivalent services) — not zero-configuration; the technical installer needs to provision this once.
- **Breadth-first by design** — this skill optimizes for covering the field, not for exhaustive depth on any single paper. A researcher who needs a deep single-paper critique should use a different skill.
