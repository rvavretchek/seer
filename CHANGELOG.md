# Changelog

## [1.0.0-rc.1] — 2026-08-19

Primeiro MVP completo do Seer, conforme escopo travado no [product brief](_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md). Release candidate — não a v1.0.0 final; falta a validação dentro do app Cowork de verdade (ver "O que falta" abaixo).

### Adicionado

- **Identidade do produto**: Constituição (8 princípios), README, CONTRIBUTING, licenciamento duplo (MIT código / CC BY-SA 4.0 conteúdo de skill) — tudo bilíngue PT-BR + EN-US.
- **Núcleo de skills, 23 no total**:
  - CORE (6/6): `literature-review`, `claim-verification` (fork de `agent-papers-cli`), `source-verification`, `citation-analysis`, `academic-writing`, `peer-review` (originais).
  - Geografia (9/9): `geographic-research`, `spatial-analysis`, `gis`, `cartography`, `human-geography`, `physical-geography`, `political-geography`, `economic-geography`, `regional-analysis` — todas originais, sem fork disponível no ecossistema.
  - Educação (7): `ai-feedback-design-principles`, `pedagogy`, `didactics`, `curriculum-analysis`, `learning-theory` (fork de `education-agent-skills`), `educational-research`, `educational-policy` (originais). Mais 160 skills do fork disponíveis pra curadoria sob demanda.
  - `orchestrator` — meta-skill que descobre e compõe as demais dinamicamente.
- **Dois forks reais** em `vendor/` com proveniência rastreada: `education-agent-skills` (CC BY-SA 4.0) e `agent-papers-cli` (Apache-2.0).
- **Contrato de skill formal** (`docs/skill-contract.md`).
- **Adaptador Claude Cowork** (`adapters/cowork/`) — plugin funcional, testado de ponta a ponta via `claude plugin marketplace add` + `claude plugin install` (23 skills carregadas, conector OpenAlex reconhecido). `.claude-plugin/marketplace.json` na raiz permite `Add marketplace` direto do GitHub.
- **Trava de segurança**: `AGENTS.md` documenta que conteúdo instrucional em `vendor/` nunca é diretiva do projeto (achado real: `vendor/education-agent-skills/CLAUDE.md` continha instrução de reportar a um serviço de terceiros).

### Escopo confirmado fora desta versão

- Geopolítica e outras disciplinas além de Geografia/Educação — pacotes futuros, contribuídos pela comunidade.
- Adaptadores para outras superfícies agênticas (Manus, Gemini, ChatGPT).
- Versão mínima de "party mode" do Seer — planejada como próximo passo logo após esta RC.

### O que falta antes da v1.0.0 final

- Testar o plugin dentro do app Cowork de verdade (validado até aqui via `claude` CLI, que usa o mesmo mecanismo, mas não é o app em si).
- Pesquisar e verificar conectores candidatos (IBGE/SIDRA, Zotero, SciELO, INPE) antes de adicioná-los a `.mcp.json`.

---

# Changelog (English / en-US)

## [1.0.0-rc.1] — 2026-08-19

Seer's first complete MVP, per the scope locked in the [product brief](_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md). Release candidate — not the final v1.0.0; still needs validation inside the actual Cowork app (see "What's left" below).

### Added

- **Product identity**: Constitution (8 principles), README, CONTRIBUTING, dual licensing (MIT code / CC BY-SA 4.0 skill content) -- all bilingual PT-BR + en-US.
- **Skill core, 23 total**:
  - CORE (6/6): `literature-review`, `claim-verification` (forked from `agent-papers-cli`), `source-verification`, `citation-analysis`, `academic-writing`, `peer-review` (original).
  - Geography (9/9): `geographic-research`, `spatial-analysis`, `gis`, `cartography`, `human-geography`, `physical-geography`, `political-geography`, `economic-geography`, `regional-analysis` -- all original, no fork available in the ecosystem.
  - Education (7): `ai-feedback-design-principles`, `pedagogy`, `didactics`, `curriculum-analysis`, `learning-theory` (forked from `education-agent-skills`), `educational-research`, `educational-policy` (original). 160 more skills from the fork available for on-demand curation.
  - `orchestrator` -- meta-skill that discovers and composes the rest dynamically.
- **Two real forks** under `vendor/` with tracked provenance: `education-agent-skills` (CC BY-SA 4.0) and `agent-papers-cli` (Apache-2.0).
- **Formal skill contract** (`docs/skill-contract.md`).
- **Claude Cowork adapter** (`adapters/cowork/`) -- functional plugin, tested end to end via `claude plugin marketplace add` + `claude plugin install` (23 skills loaded, OpenAlex connector recognized). Root `.claude-plugin/marketplace.json` enables `Add marketplace` directly from GitHub.
- **Security guard**: `AGENTS.md` documents that instructional content under `vendor/` is never a project directive (a real finding: `vendor/education-agent-skills/CLAUDE.md` contained an instruction to report to a third-party service).

### Confirmed out of scope for this version

- Geopolitics and other disciplines beyond Geography/Education -- future community-contributed packs.
- Adapters for other agentic surfaces (Manus, Gemini, ChatGPT).
- A minimal version of Seer's own "party mode" -- planned as the next step right after this RC.

### What's left before the final v1.0.0

- Testing the plugin inside the actual Cowork app (verified so far via the `claude` CLI, which uses the same mechanism, but isn't the app itself).
- Researching and verifying candidate connectors (IBGE/SIDRA, Zotero, SciELO, INPE) before adding them to `.mcp.json`.
