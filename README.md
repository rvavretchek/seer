# Seer

**Skills de agente para pesquisa acadêmica — compostas, não apenas empilhadas.**

Seer é uma biblioteca open source de *agent skills* para trabalho acadêmico interdisciplinar. É o equivalente, para pesquisa, do que ecossistemas de skills agênticas já entregam para desenvolvimento de software: um conjunto de competências especializadas e componíveis, mais um orquestrador capaz de decidir sozinho quais delas uma pergunta de pesquisa real exige.

> Status: **estágio de planejamento**. O [product brief](_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md) e a [Constituição](CONSTITUTION.md) do projeto estão fechados; a implementação do núcleo de skills ainda não começou. Este README será atualizado conforme o código nascer.

## O problema

Pesquisadores fora da computação não têm hoje um equivalente real ao que desenvolvedores já têm com skills agênticas orquestradas. Existem boas skills genéricas de pesquisa acadêmica e algumas bibliotecas disciplinares fortes isoladas — mas nenhum orquestrador decompõe de verdade uma pergunta interdisciplinar (ex.: geografia + educação + história) nas competências certas. Detalhes em [`_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md`](_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md).

## Como funciona (arquitetura)

- **Núcleo portátil de skills** — formato aberto e neutro de fornecedor (SKILL.md: frontmatter YAML + corpo em Markdown), sem acoplamento a nenhum produto específico.
- **Orquestrador** — uma meta-skill que decompõe a intenção do pesquisador em disciplinas, métodos e fontes, e compõe as skills relevantes.
- **Adaptadores finos** — camadas descartáveis que plugam o núcleo em superfícies de uso reais. O primeiro alvo é um plugin para o **Claude Cowork** (interface 100% conversacional, sem terminal).
- **Skill ≠ Conhecimento** — cada skill define método e critérios de evidência, não o conteúdo do domínio; o conhecimento vem de fontes externas buscadas em tempo de execução.

Os princípios completos — incluindo o que nunca muda — estão em [CONSTITUTION.md](CONSTITUTION.md).

## Escopo do MVP

- Skills CORE de pesquisa acadêmica (revisão bibliográfica, verificação de fontes, citação, escrita acadêmica, revisão por pares).
- Dois pacotes disciplinares: **Geografia** e **Educação**.
- O orquestrador e um adaptador para Claude Cowork.
- Contrato formal de skill, desenhado para que outras disciplinas (matemática, física, química, engenharia, história, geologia etc.) entrem depois como contribuições da comunidade.

## Contribuindo

Novas disciplinas e melhorias são bem-vindas assim que o contrato de skill for publicado. Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o fluxo de branches, o requisito de proveniência/atribuição e o padrão bilíngue de documentação.

## Licença e proveniência

Seer é licenciado sob [MIT](LICENSE). O padrão arquitetural de skills orquestradas é inspirado no [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) (também MIT, copyright BMad Code, LLC) — reuso de ideias e código é permitido sob os termos do MIT, mas o Seer **não é afiliado** ao BMAD e não usa as marcas "BMad"/"BMad Method"/"BMad Core". Toda inspiração, cópia ou adaptação de qualquer projeto upstream é documentada explicitamente no artefato onde aparece — ver Princípio 5 da [Constituição](CONSTITUTION.md).

## Materiais de referência

A pasta [`academic-agent-stack/`](academic-agent-stack/) e os arquivos `GPT_academic-skills.md` / `GEMINI_academic-skills.md` na raiz são material de contexto de uma exploração inicial do problema — preservados como referência histórica, não como plano de implementação.

---

# Seer (English / en-US)

**Agent skills for academic research — composed, not just stacked.**

Seer is an open-source library of agent skills for interdisciplinary academic work. It's the research equivalent of what agentic skill ecosystems already deliver for software development: a set of specialized, composable competencies, plus an orchestrator able to decide on its own which ones a real research question requires.

> Status: **planning stage**. The project's [product brief](_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md) and [Constitution](CONSTITUTION.md) are settled; implementation of the skill core has not started yet. This README will be updated as code lands.

## The problem

Researchers outside computing don't currently have a real equivalent to what developers already have with orchestrated agentic skills. Good generic academic-research skills exist, and a few strong per-discipline libraries exist in isolation — but no orchestrator truly decomposes an interdisciplinary question (e.g. geography + education + history) into the right competencies. Details in [`_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md`](_bmad-output/planning-artifacts/briefs/brief-Seer-2026-08-18/brief.md).

## How it works (architecture)

- **Portable skill core** — open, vendor-neutral format (SKILL.md: YAML frontmatter + Markdown body), with no coupling to any specific product.
- **Orchestrator** — a meta-skill that decomposes the researcher's intent into disciplines, methods, and sources, and composes the relevant skills.
- **Thin adapters** — disposable layers that plug the core into real usage surfaces. The first target is a plugin for **Claude Cowork** (fully conversational interface, no terminal).
- **Skill ≠ Knowledge** — each skill defines method and evidence criteria, not the domain's content; knowledge comes from external sources fetched at run time.

Full principles — including what never changes — are in [CONSTITUTION.md](CONSTITUTION.md).

## MVP scope

- CORE academic-research skills (literature review, source verification, citation, academic writing, peer review).
- Two discipline packs: **Geography** and **Education**.
- The orchestrator and a Claude Cowork adapter.
- A formal skill contract, designed so other disciplines (mathematics, physics, chemistry, engineering, history, geology, etc.) can join later as community contributions.

## Contributing

New disciplines and improvements are welcome once the skill contract is published. See [CONTRIBUTING.md](CONTRIBUTING.md) for the branching flow, the provenance/attribution requirement, and the bilingual documentation standard.

## License and provenance

Seer is licensed under [MIT](LICENSE). The orchestrated-skills architectural pattern is inspired by the [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) (also MIT, copyright BMad Code, LLC) — reuse of ideas and code is permitted under MIT terms, but Seer is **not affiliated** with BMAD and does not use the "BMad"/"BMad Method"/"BMad Core" trademarks. Any inspiration, copy, or adaptation from any upstream project is documented explicitly in the artifact where it appears — see Principle 5 of the [Constitution](CONSTITUTION.md).

## Reference materials

The [`academic-agent-stack/`](academic-agent-stack/) folder and the `GPT_academic-skills.md` / `GEMINI_academic-skills.md` files at the repo root are context material from an early exploration of the problem — preserved as historical reference, not as an implementation plan.
