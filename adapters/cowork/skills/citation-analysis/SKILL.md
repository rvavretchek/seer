---
name: citation-analysis
description: Analyze a paper or body of work's citation network -- who cites it, what it cites, and what that reveals about its influence and intellectual lineage. Use to gauge a source's standing in the field, or to find related work a keyword search would miss.
allowed-tools: Read, Write, Bash

skill_id: "core/citation-analysis"
domain: "core"
version: "0.1.0"
evidence_strength: "moderate"
evidence_sources:
  - "Garfield, E. — foundational citation-indexing and bibliometrics work establishing citation counts and citation networks as a (partial, contestable) proxy for scholarly influence."
  - "collaborative-deep-research/agent-papers-cli (Apache-2.0): the vendored paper-search tool layer already exposes the underlying citation-graph operations (citations, references, details) this skill's procedure is written against -- see vendor/PROVENANCE.md."
input_schema:
  required:
    - field: "target"
      type: "string"
      description: "The paper, author, or body of work whose citation network is being analyzed."
  optional:
    - field: "analysis_goal"
      type: "string"
      description: "Why the citation analysis is being done -- gauge influence, find related work, trace intellectual lineage, or check whether a claim is well-supported by follow-on research."
output_schema:
  fields:
    - field: "citation_summary"
      type: "object"
      description: "Citation count, citing venues/fields, and trend over time if available."
    - field: "influence_read"
      type: "string"
      description: "What the citation pattern suggests about the work's standing -- with explicit caution about what citation count does and doesn't mean."
    - field: "related_work_found"
      type: "array"
      description: "Relevant papers surfaced via the citation graph (citing or cited-by) that a keyword search alone would likely miss."
chains_well_with:
  - "core/literature-review"
  - "core/source-verification"
  - "core/claim-verification"
license: "CC BY-SA 4.0"
provenance: "original"
---

# Citation Analysis

## What This Skill Does

Analyzes a work's citation network — what it cites (its intellectual lineage) and what cites it (its influence and reception) — to answer questions a keyword search can't: how well-established is this finding, has it been contested or built on, what closely related work exists that doesn't share obvious keywords. This composes tightly with `core/literature-review`'s citation-graph-exploration step, but is its own skill because citation analysis is also useful standalone — e.g. to sanity-check a single source's standing before relying on it.

## Evidence Foundation

Citation analysis traces to Garfield's foundational bibliometric work establishing that citation counts and citation networks carry real signal about scholarly influence and intellectual lineage — but the signal is partial and contestable, not a direct measure of correctness or quality. A highly-cited paper may be influential because it's right, because it's foundational (even if later superseded), because it's controversial and frequently cited to be criticized, or because of field size and citation-culture differences unrelated to the paper's merit. This skill's job is producing the citation pattern and reading it cautiously, not treating citation count as a quality score. The underlying mechanics — pulling a paper's citing works, its references, and its metadata — are already real, working tooling in `vendor/agent-papers-cli` (the `paper-search semanticscholar citations/references/details` operations), not something this skill needs to build from scratch.

## Procedure

1. **Pull the target's citation metadata**: citation count, what it cites (references), and what cites it (citations) — using the citation-graph tool layer already vendored (`paper-search semanticscholar citations/references/details`, or the equivalent operation available in the execution environment).
2. **Read the citation trend**, not just the total — a paper cited heavily immediately after publication and then rarely since reads differently than one with steadily growing citations, or one recently spiking after years of obscurity.
3. **Check *how* it's cited when possible**, not just citation count alone — being cited as foundational support reads differently than being cited as an example of a superseded or contested claim; a full citation-context read is expensive, so do this selectively for the specific claims that matter most to `analysis_goal`.
4. **Follow the citation graph for related work**, not just influence — papers that cite or are cited by the target frequently share relevant context a keyword search misses entirely, especially across disciplinary-terminology differences (the same phenomenon named differently in geography vs. demography vs. economics literature, for instance).
5. **State the influence read cautiously**, naming what citation count does and doesn't establish for the specific `analysis_goal` — "well-cited" is not the same claim as "well-supported" or "still considered correct."

## Example

**Input:** `target`: "Kalyuga et al. (2003), the expertise reversal effect paper cited in education/learning-theory." `analysis_goal`: "Check whether this finding is still considered solid, or has been contested/superseded."

**Output:** Citation summary: substantial and sustained citation count across cognitive-load-theory and instructional-design literature since publication, rather than an early spike followed by decline — a pattern consistent with a finding that became an accepted part of the field's core framework rather than one that was proposed and later abandoned. Influence read: high citation count here plausibly does track genuine acceptance, since the pattern (sustained, not spiking-then-fading) is the more informative signal than the raw count. Related work found: following the citation graph surfaces later work applying expertise reversal specifically to AI-generated instructional scaffolds — directly relevant to Seer's own `education/pedagogy` and `education/didactics` skills, not found by a keyword search on "expertise reversal" alone.

## Known Limitations

- **Citation count is a lagging, field-dependent, and gameable signal.** Fast-moving fields, preprint cultures, and citation-circle practices all distort raw counts differently — never state a citation count as a quality judgment without the trend and context that make it interpretable.
- **Depends on the underlying citation database's coverage**, which shares the same English/Global-North skew flagged in `core/literature-review` — a Portuguese-language or Brazil-specific work may show an artificially low citation count that reflects database coverage, not actual influence.
- **A full citation-context read (how each citation actually uses the target) doesn't scale to every citation** — this skill samples selectively for high-stakes claims rather than promising exhaustive context analysis.
