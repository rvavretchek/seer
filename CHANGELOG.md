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

### Validação real no app Cowork (2026-08-19, pós-tag)

Roteiro completo (`tests/manual/cowork-rc1-test-script.md`) rodado no Cowork real, não em ambiente proxy:

- ✅ **Invocação automática por conversa** — `seer:literature-review` acionada sozinha a partir de um pedido em português; o modelo explicou corretamente por que não usou `academic-writing`/`ai-feedback-design-principles`.
- ✅ **Orquestrador dentro do Cowork** — confirmado de verdade, resolvendo a limitação que ainda estava em aberto no `orchestrator/SKILL.md`. Despacho **paralelo** real de `human-geography` + `economic-geography`, aplicação direta de `educational-policy` sem sub-agente quando os insumos já estavam prontos, e a tensão entre duas leituras dos dados foi sinalizada explicitamente em vez de escondida.
- ⚠️ **Conector OpenAlex** — falhou no teste: 5 tentativas retornaram HTTP 429 (limite de taxa no acesso anônimo). O Claude não tentou contornar via curl/bash e entregou os mesmos dados via busca web + Crossref, verificados. Achado real, ação identificada: configurar `OPENALEX_API_KEY` (chave grátis) localmente. Ver `adapters/cowork/CONNECTORS.md`.
- ✅ **Acesso a pasta** — funcionou, inclusive detectando que um arquivo enviado (CV) destoava do conteúdo esperado dos demais.

### O que falta antes da v1.0.0 final

- Confirmar se `OPENALEX_API_KEY` resolve o 429 observado, ou se o conector precisa de outra estratégia (retry/backoff, fonte alternativa).
- Pesquisar e verificar os demais conectores candidatos (IBGE/SIDRA, Zotero, SciELO, INPE) antes de adicioná-los a `.mcp.json`.

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

### Real validation in the Cowork app (2026-08-19, post-tag)

Full script (`tests/manual/cowork-rc1-test-script.md`) run inside the real Cowork app, not a proxy environment:

- ✅ **Automatic invocation from conversation** -- `seer:literature-review` triggered on its own from a plain-language request; the model correctly explained why it didn't use `academic-writing`/`ai-feedback-design-principles`.
- ✅ **Orchestrator inside Cowork** -- confirmed for real, resolving the open question that was still in `orchestrator/SKILL.md`. Real **parallel** dispatch of `human-geography` + `economic-geography`, direct application of `educational-policy` without a subagent once its inputs were already in hand, and the tension between two readings of the data was flagged explicitly rather than hidden.
- ⚠️ **OpenAlex connector** -- failed the test: 5 attempts returned HTTP 429 (anonymous-access rate limit). Claude didn't try to bypass it via curl/bash and delivered the same, verified data via web search + Crossref instead. Real finding, action identified: configure `OPENALEX_API_KEY` (free key) locally. See `adapters/cowork/CONNECTORS.md`.
- ✅ **Folder access** -- worked, including catching that an uploaded file (a CV) didn't match the expected content of the others.

### What's left before the final v1.0.0

- Confirm whether `OPENALEX_API_KEY` resolves the observed 429, or whether the connector needs a different strategy (retry/backoff, alternate source).
- Research and verify the remaining candidate connectors (IBGE/SIDRA, Zotero, SciELO, INPE) before adding them to `.mcp.json`.
