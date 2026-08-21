# Changelog

## [1.3.0] — 2026-08-21

Tabula Rasa ganha despacho paralelo real entre personas.

### Adicionado

- **`dispatch_mode: "subagent"`** no Tabula Rasa (padrão continua `"session"`, comportamento inalterado). Cada persona relevante vira um subagente `Task` de verdade — mesmo mecanismo que o orquestrador já roda em produção — em vez de uma mente só simulando todos os lados. A discordância entre personas em modo despachado é um sinal mais forte: são dois processos de raciocínio genuinamente separados chegando a conclusões diferentes, não uma mente narrando dois pontos de vista.
- Validado ao vivo, duas vezes, de forma independente — a segunda rodada achou um limite real: uma skill de síntese (`regional-analysis`) despachada em paralelo não consegue de fato sintetizar as outras personas porque nunca vê os outputs delas. Documentado no procedimento como tradeoff real, não escondido.
- Limitações conhecidas atualizadas: custo real de latência/token do modo despachado, e o fato de que subagentes despachados não recebem contexto da Continuity (`memoria.md`/`ata-do-projeto.md`) por padrão de projeto.

### O que fica para depois

- Paridade total com o `bmad-party-mode` (modos `auto`, `agent-team`) — segue adiada pra v2.0/v3.0.
- Passar um resumo destilado da Continuity pro prompt de cada subagente despachado, se a lacuna atual (subagente não vê decisão já fechada) se mostrar um problema real na prática.

## [1.2.0] — 2026-08-21

Fecha a prioridade "conectores" do roadmap pós-v1.1.0 e resolve o problema de granularidade de persona da Geografia.

### Adicionado

- **Conector IBGE/SIDRA** (`ibge-br-mcp`) — dados geográficos, demográficos e estatísticos do Brasil, sem chave de API. Mantenedor identificável, dependências enxutas, verificado de forma independente antes de entrar em `.mcp.json`.
- **Conector Zotero** (`zotero-mcp-server`), em modo Web API — gerenciamento de referências, funciona sem o app desktop do Zotero aberto (único modo realista pro fluxo da Sonia). Único conector do plugin que roda em Python/`uvx` em vez de Node/`npx` — documentado no `README.md` do adaptador.
- **INPE e SciELO documentados dentro das próprias skills** (não só no `CONNECTORS.md`): `geography/physical-geography` e `geography/gis` sabem consultar a API WFS/CQL do TerraBrasilis (PRODES/DETER) direto via HTTP; `core/literature-review` ganhou um passo de procedimento novo pra API de metadados da SciELO, deixando explícito que é só metadado, nunca texto completo.
- **Geografia quebrada em oito personas** — nova camada `By Skill` em `personas.md` (prioridade sobre `By Domain`), reservada pra domínios que realmente precisam, não um padrão novo geral. Ubaldo continua em `geographic-research`; Prudêncio, Cremilda, Bonifácio, Maria, Odorico, Catarina e Altamira assumem as outras oito skills de Geografia.
- **Relação entre `ata-do-projeto.md` e `metodologia.md` resolvida**: ficam separados de propósito — a ata é acompanhamento interno da sala, `metodologia.md` é candidato a virar parte da publicação final.

### O que fica para depois

- Despacho paralelo real entre personas do Tabula Rasa (próxima MINOR).
- Paridade total com o `bmad-party-mode` — adiada pra v2.0/v3.0.
- Zotero em modo local (app desktop aberto), como alternativa ao modo Web API.

## [1.1.0] — 2026-08-21

Fecha o roadmap pós-MVP planejado desde a v1.0.0-rc.1: as duas disciplinas do Tabula Rasa que exigiam pesquisa real, sem fork equivalente, agora estão prontas. O elenco de personas do Tabula Rasa está completo conforme desenhado.

### Adicionado

- **`project-management/academic-project-planning`** — cronograma, marcos e registro de risco para o projeto de pesquisa em si, mais rastreamento de prazos do pipeline de publicação (janela de submissão, ciclo de revisão). Nunca opina sobre metodologia de pesquisa (isso é das skills de disciplina) nem sobre o conteúdo de uma revisão por pares (isso é do `core/peer-review`). Fundamentado no PMBoK 8ª edição (PMI, lançada em novembro de 2025).
- **`research-finance/grant-budget-and-accountability`** — formação de orçamento, acompanhamento financeiro durante a execução e prestação de contas, cobrindo os padrões gerais de CAPES, CNPq e FAPESP. Fundamentado em fontes primárias reais (página oficial do CNPq, normas vigentes da FAPESP, Portaria CAPES nº 37/2026), com sinalização explícita do que não pôde ser confirmado em vez de inventado — variação por edital tratada como limitação estrutural, não nota de rodapé.
- **Elenco do Tabula Rasa completo**: Alberico agora também é a voz de `project-management` (mesmo nome e característica de sempre — coordenador de projeto é literalmente gestão de projeto aplicada à sala), continuando presente na maioria das sessões (`Always Present`). Quitéria assume `research-finance`. Ubaldo permanece em Geografia, papel que já ocupava.
- **32 skills** no plugin buildado.

### O que fica para depois

- Conectores candidatos ainda não pesquisados: IBGE/SIDRA, Zotero, SciELO, INPE.
- Relação entre `ata-do-projeto.md` (Tabula Rasa) e `metodologia.md` (Contexto de Projeto, `docs/skill-contract.md`) permanece deliberadamente não resolvida.
- Tabula Rasa segue em modo sessão apenas — sem despacho paralelo real entre personas.
- Bug de plataforma no Cowork (ver v1.0.0) continua sem correção conhecida.

## [1.0.0] — 2026-08-21

Primeira versão final do Seer, cobrindo o MVP original (v1.0.0-rc.1) mais tudo que o roadmap já previa como "logo em seguida": a versão mínima do Tabula Rasa (party mode do próprio Seer) com memória entre sessões, seis skills novas de disciplina e a normalização ABNT.

### Adicionado desde a v1.0.0-rc.1

- **Tabula Rasa** (`skills/tabula-rasa/`) — sala visível onde as skills de disciplina discutem em personagem em vez de compor silenciosamente. Seis personas fechadas (`personas.md`): Alberico (Coordenador de Projeto, sempre presente), Ubaldo (Geografia), Serafim (Educação), Ludovico (Sociologia), Asdrubal (Ciência Política), Epaminondas (Psicologia Cognitiva), Clotilde (Revisão de Texto). Validado de ponta a ponta duas vezes (Provas de Conceito #1 e #2 no próprio `SKILL.md`), incluindo um pedido idêntico ao usado para validar o orquestrador, para comparação direta entre os dois modos de composição.
- **Continuity** — memória entre sessões do Tabula Rasa, por projeto de pesquisa (não por sessão nem por dia): `.tabula-rasa/memoria.md` (log bruto, inclusive fios discutidos e ainda não decididos) e `seer_output/ata-do-projeto.md` (documento vivo de decisões fechadas). Validada com dois processos `claude -p` reais e separados contra o mesmo projeto — a sala retomou um fio em aberto em personagem, sem quebrar a quarta parede, na segunda sessão.
- **Seis skills novas**: `sociology/sociological-analysis` (Durkheim/Weber), `political-science/policy-process-analysis` (Kingdon MSF + Sabatier ACF), `cognitive-psychology/cognitive-bias-analysis` (Tversky & Kahneman), `core/academic-formatting-abnt` (NBR 6023:2018, 10520:2023, 14724:2024), e a divisão de `text-revision/line-editing` em irmãs por idioma/localidade — `line-editing-en-us` (Williams & Bizup + Strunk & White) e `line-editing-pt-br` (Othon Garcia) — junto com uma convenção de nomenclatura documentada (`docs/skill-contract.md`) para a comunidade contribuir novas variantes (`en-uk`, `pt-pt`, etc.) sem colisão.
- **23 → 30 skills** no plugin buildado (`adapters/cowork/skills/`) — essa também é a primeira versão em que o Tabula Rasa está de fato incluído no plugin (nunca tinha sido buildado antes).
- **Conector OpenAlex confirmado funcionando de verdade**: causa raiz do 429 identificada (OpenAlex descontinuou o polite pool gratuito em fev/2026, chave grátis agora obrigatória), `.mcp.json` corrigido para usar `OPENALEX_API_KEY` via variável de ambiente, e testado com sucesso via `claude` CLI — busca real retornou dado real (OpenAlex Work ID e contagem de citações).

### Limitação conhecida e importante: bug de plataforma no Cowork

A instalação via **terminal** (`claude plugin marketplace add` + `claude plugin install`) funciona de forma confiável e é o caminho usado para validar tudo acima. A instalação pela **GUI do Cowork** (app desktop ou browser) tem um problema real e documentado do lado da Anthropic, não do Seer: marketplaces pessoais/via GitHub (como este) são aceitos na instalação mas removidos silenciosamente pelo `RemotePluginManager` no próximo ciclo de sincronização — tipicamente sobrevivendo à sessão em que foram instalados, mas não a um reinício do app. Depois disso, o app pode recusar reinstalar ("marketplace já adicionado") mesmo sem nenhuma skill disponível. Confirmado em issues públicas do `anthropics/claude-code`: [#39274](https://github.com/anthropics/claude-code/issues/39274), [#40475](https://github.com/anthropics/claude-code/issues/40475), [#40600](https://github.com/anthropics/claude-code/issues/40600). Sem correção conhecida até a data desta release. Se as skills do Seer pararem de responder no Cowork depois de ter funcionado antes, o caminho é remover e readicionar o marketplace — e, se isso também travar, usar a validação via terminal como alternativa enquanto a Anthropic não corrige.

### O que fica para a próxima versão

- As duas disciplinas mais difíceis do Tabula Rasa, deliberadamente adiadas por exigirem pesquisa real sem fork equivalente disponível: **Gerente de Projetos** (rigor metodológico/científico) e **Especialista em Finanças** (prestação de contas CAPES/CNPQ/FAPESP).
- Conectores candidatos ainda não pesquisados: IBGE/SIDRA, Zotero, SciELO, INPE.

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

## [1.3.0] — 2026-08-21

Tabula Rasa gets real parallel dispatch between personas.

### Added

- **`dispatch_mode: "subagent"`** in Tabula Rasa (default stays `"session"`, unchanged behavior). Each relevant persona becomes a real `Task` subagent -- the same mechanism the orchestrator already runs in production -- instead of one mind simulating every side. Disagreement between personas in dispatched mode is a stronger signal: two genuinely separate reasoning processes reaching different conclusions, not one mind narrating two viewpoints.
- Validated live, twice, independently -- the second pass surfaced a real limitation: a synthesis-type skill (`regional-analysis`) dispatched in parallel can't actually synthesize the other personas' outputs, since it never sees them. Documented in the procedure as a real tradeoff, not hidden.
- Known Limitations updated: the real latency/cost of dispatched mode, and the fact that dispatched subagents don't receive Continuity context (`memoria.md`/`ata-do-projeto.md`) by design.

### What's left for later

- Full parity with `bmad-party-mode` (`auto`, `agent-team` modes) -- still deferred to v2.0/v3.0.
- Passing a distilled Continuity brief into each dispatched subagent's prompt, if the current gap (a subagent not seeing an already-closed decision) proves to be a real problem in practice.

## [1.2.0] — 2026-08-21

Closes the "connectors" priority from the post-v1.1.0 roadmap and resolves Geography's persona-granularity problem.

### Added

- **IBGE/SIDRA connector** (`ibge-br-mcp`) -- Brazilian geographic, demographic, and statistical data, no API key. Identifiable maintainer, lean dependencies, verified independently before landing in `.mcp.json`.
- **Zotero connector** (`zotero-mcp-server`), in Web API mode -- reference management, works without the Zotero desktop app open (the only mode realistic for Sonia's workflow). The only plugin connector running on Python/`uvx` instead of Node/`npx` -- documented in the adapter's `README.md`.
- **INPE and SciELO documented inside the relevant skills themselves** (not just `CONNECTORS.md`): `geography/physical-geography` and `geography/gis` now know how to query TerraBrasilis's WFS/CQL API (PRODES/DETER) directly over HTTP; `core/literature-review` gained a new procedure step for SciELO's metadata API, stating plainly that it's metadata only, never full text.
- **Geography split into eight personas** -- a new `By Skill` tier in `personas.md` (overrides `By Domain`), reserved for domains that actually need it, not a new general default. Ubaldo keeps `geographic-research`; Prudêncio, Cremilda, Bonifácio, Maria, Odorico, Catarina, and Altamira take the other eight Geography skills.
- **`ata-do-projeto.md` vs. `metodologia.md` relationship resolved**: kept separate by design -- the ata is internal room tracking, `metodologia.md` is written to potentially feed the final publication.

### What's left for later

- Real parallel dispatch between Tabula Rasa personas (next MINOR).
- Full parity with `bmad-party-mode` -- deferred to v2.0/v3.0.
- Zotero local mode (desktop app open), as an alternative to Web API mode.

## [1.1.0] — 2026-08-21

Closes the post-MVP roadmap planned since v1.0.0-rc.1: the two Tabula Rasa disciplines that needed real research, with no fork equivalent, are now ready. Tabula Rasa's persona cast is complete as designed.

### Added

- **`project-management/academic-project-planning`** -- schedule, milestones, and risk register for the research project itself, plus publication-pipeline deadline tracking (submission windows, review cycles). Never opines on research methodology (that's the discipline skills' job) or peer-review substance (that's `core/peer-review`'s). Grounded in PMBoK 8th Edition (PMI, released November 2025).
- **`research-finance/grant-budget-and-accountability`** -- budget formation, execution tracking, and prestação de contas, covering the general patterns shared by CAPES, CNPq, and FAPESP. Grounded in real primary sources (CNPq's official page, FAPESP's current norms, CAPES's Portaria nº 37/2026), with explicit flags for what couldn't be confirmed rather than fabricated -- edital-specific variation treated as a structural limitation, not a footnote.
- **Tabula Rasa's cast is now complete**: Alberico also voices `project-management` (same name and trait as always -- a project coordinator is literally project management applied to the room itself), while remaining present in most sessions (`Always Present`). Quitéria takes `research-finance`. Ubaldo stays on Geography, the role he already held.
- **32 skills** in the built plugin.

### What's left for later

- Candidate connectors not yet researched: IBGE/SIDRA, Zotero, SciELO, INPE.
- The relationship between `ata-do-projeto.md` (Tabula Rasa) and `metodologia.md` (Project Context, `docs/skill-contract.md`) remains deliberately unresolved.
- Tabula Rasa is still session-mode only -- no real parallel dispatch between personas.
- The Cowork platform bug (see v1.0.0) still has no known fix.

## [1.0.0] — 2026-08-21

Seer's first final release, covering the original MVP (v1.0.0-rc.1) plus everything the roadmap already called "right after that": Seer's own minimal Tabula Rasa (party mode) with cross-session memory, six new discipline skills, and ABNT formatting.

### Added since v1.0.0-rc.1

- **Tabula Rasa** (`skills/tabula-rasa/`) -- a visible room where discipline skills argue in character instead of composing silently. Six personas locked (`personas.md`): Alberico (Project Coordinator, always present), Ubaldo (Geography), Serafim (Education), Ludovico (Sociology), Asdrubal (Political Science), Epaminondas (Cognitive Psychology), Clotilde (Text Revision). Validated end to end twice (Proof of Concept #1 and #2 in the `SKILL.md` itself), including an identical request to the one used to validate the orchestrator, for direct comparison between the two composition modes.
- **Continuity** -- cross-session memory for Tabula Rasa, per research project (never per session or per day): `.tabula-rasa/memoria.md` (raw log, including threads discussed but not yet decided) and `seer_output/ata-do-projeto.md` (living decisions document). Validated with two real, separate `claude -p` processes against the same project -- the room picked up an open thread in character, without breaking the fourth wall, on the second session.
- **Six new skills**: `sociology/sociological-analysis` (Durkheim/Weber), `political-science/policy-process-analysis` (Kingdon MSF + Sabatier ACF), `cognitive-psychology/cognitive-bias-analysis` (Tversky & Kahneman), `core/academic-formatting-abnt` (NBR 6023:2018, 10520:2023, 14724:2024), and `text-revision/line-editing` split into language/locale siblings -- `line-editing-en-us` (Williams & Bizup + Strunk & White) and `line-editing-pt-br` (Othon Garcia) -- with a documented naming convention (`docs/skill-contract.md`) so the community can contribute new variants (`en-uk`, `pt-pt`, etc.) without collisions.
- **23 → 30 skills** in the built plugin (`adapters/cowork/skills/`) -- also the first version where Tabula Rasa is actually included in the plugin (it had never been built in before).
- **OpenAlex connector confirmed genuinely working**: root cause of the 429 identified (OpenAlex discontinued the free polite pool in Feb 2026, a free key is now required), `.mcp.json` fixed to use `OPENALEX_API_KEY` via environment variable, and verified successfully via the `claude` CLI -- a real query returned real data (an OpenAlex Work ID and citation count).

### Known limitation worth flagging: a Cowork platform bug

Installing via **terminal** (`claude plugin marketplace add` + `claude plugin install`) works reliably and is the path used to validate everything above. Installing via the **Cowork GUI** (desktop app or browser) hits a real, documented bug on Anthropic's side, not Seer's: personal/GitHub-based marketplaces (like this one) install successfully but get silently removed by `RemotePluginManager` on the next sync cycle -- typically surviving the session they were installed in, but not an app restart. After that, the app may refuse to reinstall ("marketplace already added") even with no skill actually available. Confirmed against public issues on `anthropics/claude-code`: [#39274](https://github.com/anthropics/claude-code/issues/39274), [#40475](https://github.com/anthropics/claude-code/issues/40475), [#40600](https://github.com/anthropics/claude-code/issues/40600). No known fix as of this release. If Seer's skills stop responding in Cowork after previously working, remove and re-add the marketplace -- and if that also gets stuck, terminal-based validation remains a working alternative until Anthropic fixes this.

### What's left for the next version

- Tabula Rasa's two hardest disciplines, deliberately deferred since they need real research with no fork equivalent available: **Project Manager** (academic/scientific methodological rigor) and **Finance Specialist** (grant-compliance accounting for Brazilian funding agencies -- CAPES/CNPQ/FAPESP).
- Candidate connectors not yet researched: IBGE/SIDRA, Zotero, SciELO, INPE.

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
