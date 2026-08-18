---
title: "Product Brief: Seer"
status: draft
created: 2026-08-18
updated: 2026-08-18
---

# Product Brief: Seer

## Resumo Executivo

Seer é uma biblioteca open source de *agent skills* para pesquisa acadêmica — o equivalente, para o trabalho acadêmico, do que ecossistemas como o BMAD Method já entregam para desenvolvimento de software: um conjunto de competências especializadas e componíveis, orquestradas por um agente capaz de decidir sozinho quais delas uma pergunta de pesquisa exige.

O problema que resolve não é falta de tecnologia. Já existem boas skills genéricas de pesquisa acadêmica (revisão bibliográfica, citação, revisão por pares) e algumas bibliotecas disciplinares fortes (uma biblioteca de Educação com 165 skills, projetos agênticos de geoprocessamento/GIS). O que falta é a camada de **composição**: um orquestrador capaz de olhar para uma pergunta interdisciplinar — geografia, educação, história, geopolítica juntas — e decidir sozinho quais competências acionar, em vez de forçar o pesquisador a escolher manualmente entre dezenas de ferramentas soltas.

O Seer nasce com um caso de uso real e uma pessoa real por trás dele: Sônia, professora doutora e pesquisadora da Faculdade de Educação da USP (Geografia + Educação), 68 anos, sem afinidade com linha de comando. O produto é desenhado para que ela — e qualquer acadêmico no mesmo perfil — simplesmente converse em linguagem natural, sem nunca precisar rodar um comando. Mas o projeto nasce público e open source desde o primeiro commit, porque o objetivo declarado é maior que um caso de uso: virar um repositório vivo de skills acadêmicas, capaz de crescer por contribuição — novas disciplinas (matemática, física, química, engenharia, história, geologia etc.) entrando como "pacotes" que seguem o mesmo contrato.

## O Problema

Pesquisadores acadêmicos fora da computação não têm hoje um equivalente real ao que desenvolvedores de software já têm com skills agênticas: um conjunto de competências especializadas, orquestradas, que amplificam o trabalho intelectual sem exigir conhecimento técnico do usuário final.

O que existe está fragmentado em três níveis:

- **Pesquisa acadêmica genérica** (revisão bibliográfica, verificação de fontes, escrita acadêmica) — já madura, mas dispersa em vários projetos sem padrão comum.
- **Bibliotecas por disciplina** — existem ilhas fortes (Educação, geoprocessamento/GIS) e lacunas reais (Geopolítica, Geoeconomia, História, Geologia têm pouca ou nenhuma skill dedicada).
- **Orquestração interdisciplinar** — praticamente inexistente. Nenhum projeto encontrado decompõe uma pergunta de pesquisa real ("os impactos geopolíticos, econômicos e educacionais da expansão de um corredor bioceânico") nas competências certas automaticamente.

Uma tentativa preliminar de resolver isso manualmente — via conversas soltas com assistentes generativos, tentando "enxertar" bibliotecas de terceiros — evidenciou o problema em vez de resolvê-lo: gerou uma estrutura de pastas plausível na superfície, mas sem download real de conteúdo, sem controle de proveniência/licença, e sem nenhuma garantia de que as skills compostas realmente funcionassem juntas. Esse material está preservado no repositório como referência do problema, não como plano a seguir.

O custo do status quo, para uma pesquisadora como Sônia: ou ela usa um chat genérico sem repertório metodológico específico da sua área, ou depende de alguém tecnicamente fluente montar e manter uma solução ad hoc — o que não escala nem para ela, nem para a comunidade acadêmica mais ampla que enfrenta o mesmo problema em outras disciplinas.

## A Solução

Seer é um **núcleo portátil de skills acadêmicas**, escrito num formato aberto e neutro de fornecedor (SKILL.md — frontmatter YAML + corpo em Markdown, a convenção de fato já usada por Claude Code, Codex, Cursor, Aider, Gemini CLI), mais um **orquestrador** (uma meta-skill) que decompõe a intenção do pesquisador em disciplinas, métodos e fontes necessárias, e compõe as skills relevantes para executar.

Sobre esse núcleo, adaptadores finos plugam o Seer em superfícies de uso reais. O primeiro é um plugin para o **Claude Cowork** — que já resolve, de fábrica, exatamente o que um pesquisador não-técnico precisa: interface 100% conversacional, sem terminal, com acesso a arquivos locais, navegação e conectores (Drive, planilhas etc.), e execução de tarefas multi-etapa até um entregável (ex.: um relatório em Excel). O Seer não reconstrói esse motor — ele entra como a camada de conhecimento metodológico e disciplinar que o motor do Cowork ainda não tem.

Como o formato de plugin de qualquer produto é, por natureza, mais volátil que o núcleo de conhecimento, a arquitetura mantém as duas camadas deliberadamente separadas: o núcleo de skills nunca fica acoplado ao formato de um único fornecedor. Isso deixa em aberto adaptadores futuros para outras superfícies agênticas (Manus, agentes do Gemini, ChatGPT) sem reescrever o conteúdo.

## O Que Torna Isso Diferente

- **Composição, não coleção.** Muitos projetos empilham skills; poucos têm um orquestrador que decide quais usar para uma pergunta interdisciplinar real. Esse é o núcleo do valor do Seer, não um recurso secundário.
- **Skill ≠ Conhecimento.** Cada skill define método, critérios de evidência, fontes preferenciais e modos de falha — não o conteúdo do domínio em si. O conhecimento vem de fontes externas buscadas em tempo de execução, o que mantém as skills pequenas, revisáveis e atualizáveis sem reescrever nada.
- **Portabilidade por desenho, não por acidente.** O núcleo nunca é escrito contra o formato de plugin de um fornecedor específico; adaptadores são a única camada descartável.
- **Proveniência explícita como regra, não como detalhe.** Qualquer ideia, estrutura ou trecho inspirado, copiado ou adaptado — do BMAD Method ou de qualquer outro projeto upstream — é documentado com atribuição e licença, em todo lugar onde aparece. O BMAD Method é MIT (BMad Code, LLC); a marca "BMad" nunca é usada para nomear ou promover o Seer.
- **Não é uma cópia gigante de outros repositórios.** A tentativa anterior de "baixar e enxertar" SKILL.md de terceiros foi descartada deliberadamente — gera problema de licença, de qualidade e de manutenção sem gerar valor real.

## A Quem Isso Serve

**Usuária primária — persona-piso, não teto:** Sônia, 68 anos, professora doutora e pesquisadora da Faculdade de Educação da USP (Geografia da Educação), escritora, sem afinidade com linha de comando ou scripts. O uso diário dela precisa ser 100% conversa em linguagem natural — nenhuma etapa do fluxo do dia a dia pode exigir instalação, comando ou configuração. Um técnico ("o cara da TI") faz a instalação inicial uma única vez.

Essa persona define o **piso** de acessibilidade do produto — não o teto. Parte real da comunidade acadêmica é tecnicamente fluente e vai preferir configurar e estender o Seer diretamente; o design não pode excluir nem um grupo nem o outro.

**Usuária/contribuidor secundário:** a comunidade acadêmica open source mais ampla — pesquisadores de outras disciplinas que queiram *usar* pacotes já existentes, e desenvolvedores/pesquisadores tecnicamente fluentes que queiram *contribuir* novos pacotes disciplinares (matemática, física, química, engenharia, história, geologia etc.), seguindo o contrato de skill definido pelo núcleo.

## Critérios de Sucesso

O critério de sucesso funcional, definido pela própria equipe de design deste brief: Sônia pergunta algo como *"verifique os índices de crescimento vegetativo das regiões Norte e Nordeste entre 1980–2020, por faixa etária"*, em linguagem natural — e o Seer, através do Cowork, decide sozinho quais competências acionar (geografia, séries históricas, análise quantitativa), busca o que cada uma precisa, executa a análise e entrega um relatório pronto (ex.: Excel), sem que a orquestração nunca apareça para ela como uma decisão que ela precisou tomar.

Sinais de sucesso do produto:

- Sônia consegue completar uma tarefa de pesquisa real do início ao fim sem nenhuma intervenção técnica de terceiros, além da instalação inicial.
- Pelo menos uma disciplina além de Geografia+Educação é contribuída por alguém de fora do time original, seguindo o contrato de skill sem precisar de suporte direto.
- Nenhuma skill do núcleo precisa ser reescrita quando um novo adaptador de superfície é adicionado — prova de que a separação núcleo/adaptador se sustenta na prática.
- [ASSUMPTION] Toda skill nova aceita no repositório carrega um registro de proveniência (fonte, licença, o que foi alterado) — verificável em revisão de PR, não apenas de boa vontade.

## Escopo

**Dentro do escopo (v0.1 / MVP):**

- Núcleo de skills CORE de pesquisa acadêmica: revisão bibliográfica, verificação de fontes, análise de citações, escrita acadêmica, revisão por pares, verificação de afirmações.
- Dois pacotes disciplinares: **Geografia** e **Educação**.
- O orquestrador (meta-skill) capaz de decompor uma pergunta interdisciplinar dentro desse escopo e compor as skills certas.
- Um adaptador (plugin) para Claude Cowork, cobrindo o fluxo de uso real de Sônia.
- Contrato formal de skill (estrutura, metadados obrigatórios, critérios de evidência) desenhado desde já para permitir que outras disciplinas entrem depois sem redesenho.
- Documentação bilíngue (PT-BR + EN-US) desde o primeiro commit: README, CONTRIBUTING, CONSTITUTION (princípios do projeto) e este brief.
- Licenciamento MIT, com mecanismo explícito de atribuição/proveniência para qualquer conteúdo inspirado em terceiros.

**Fora do escopo (por ora, explicitamente adiado):**

- Outras disciplinas (Geopolítica, Geoeconomia, História, Geologia, e futuramente Matemática, Física, Química, Engenharia etc.) — viram pacotes contribuídos depois que o contrato de skill estiver validado com Geografia+Educação.
- Adaptadores para outras superfícies agênticas (Manus, Gemini, ChatGPT) — arquitetura deixa a porta aberta, mas nenhum é construído no MVP.
- Qualquer interface própria (app, site, GUI) — o MVP depende inteiramente da interface do Cowork; não se constrói front-end próprio.
- "Baixar e enxertar" skills de repositórios de terceiros de forma automatizada — descartado como abordagem.

**Logo após o MVP (não no MVP em si):** uma versão mínima de um "party mode" do Seer — múltiplas personas disciplinares (Geografia, Educação) conversando entre si e com a pesquisadora de forma visível, ao contrário da composição silenciosa do orquestrador — reaproveitando o mesmo elenco de skills já construído, em modo `session` simples (sem sub-agentes, sem memória persistente, sem sistema de customização dinâmico). A versão com paridade total ao `bmad-party-mode` (múltiplos modos de execução, memória, customização dinâmica) exigiria construir do zero uma infraestrutura de configuração genérica que o Seer ainda não tem — fica deliberadamente adiada para depois da entrega do MVP.

## Visão

Se o Seer der certo, ele se torna para a pesquisa acadêmica interdisciplinar o que o BMAD Method é hoje para desenvolvimento de software: não um produto fechado, mas um **padrão comunitário** — um contrato de skill estável o suficiente para que qualquer pesquisador, de qualquer disciplina, possa contribuir uma competência nova sem precisar entender o motor por trás, e qualquer superfície agêntica nova (seja da Anthropic, do Google, da OpenAI ou de quem vier depois) possa ganhar um adaptador fino sem tocar no núcleo.

Em 2-3 anos, o teste real de sucesso não é quantas disciplinas o Seer cobre sozinho — é quantas foram contribuídas por pessoas que nunca conversaram com o time original, porque o contrato era claro o suficiente para isso acontecer sem elas precisarem perguntar.

---

# Product Brief: Seer (English / en-US)

## Executive Summary

Seer is an open-source library of agent skills for academic research — the academic-work equivalent of what ecosystems like the BMAD Method already deliver for software development: a set of specialized, composable competencies, orchestrated by an agent able to decide on its own which ones a given research question requires.

The problem it solves is not a lack of technology. Good generic academic-research skills already exist (literature review, citation, peer review), and a few strong per-discipline libraries exist (a 165-skill Education library, geospatial/GIS agent projects). What's missing is the **composition** layer: an orchestrator able to look at an interdisciplinary question — geography, education, history, geopolitics together — and decide on its own which competencies to invoke, instead of forcing the researcher to manually pick among dozens of disconnected tools.

Seer is being built with a real use case and a real person behind it: Sônia, a PhD professor and researcher at USP's Faculdade de Educação (Geography Education), 68 years old, with no affinity for the command line. The product is designed so that she — and any academic in the same profile — can simply talk in natural language, never needing to run a command. But the project is public and open source from the first commit, because the stated goal is bigger than one use case: to become a living repository of academic skills that grows by contribution — new disciplines (mathematics, physics, chemistry, engineering, history, geology, etc.) entering as "packs" that follow the same contract.

## The Problem

Academic researchers outside computing don't currently have a real equivalent to what software developers already have with agentic skills: a set of specialized, orchestrated competencies that amplify intellectual work without requiring technical knowledge from the end user.

What exists today is fragmented across three levels:

- **Generic academic research** (literature review, source verification, academic writing) — already mature, but scattered across many projects with no shared standard.
- **Per-discipline libraries** — strong islands exist (Education, geospatial/GIS) and real gaps remain (Geopolitics, Geoeconomics, History, Geology have little to no dedicated skill work).
- **Interdisciplinary orchestration** — practically nonexistent. No project found decomposes a real research question ("the geopolitical, economic, and educational impacts of a bioceanic corridor's expansion") into the right competencies automatically.

A preliminary attempt to solve this manually — through loose conversations with generative assistants, trying to "graft" third-party libraries together — surfaced the problem rather than solving it: it produced a folder structure that looked plausible on the surface, but with no real content downloaded, no provenance/license control, and no guarantee the composed skills would actually work together. That material is preserved in the repository as evidence of the problem, not as a plan to follow.

The cost of the status quo, for a researcher like Sônia: either she uses a generic chat assistant with no discipline-specific methodological repertoire, or she depends on someone technically fluent to build and maintain an ad hoc solution — which scales for neither her nor the wider academic community facing the same problem in other disciplines.

## The Solution

Seer is a **portable core of academic skills**, written in an open, vendor-neutral format (SKILL.md — YAML frontmatter plus a Markdown body, the de facto convention already used by Claude Code, Codex, Cursor, Aider, and Gemini CLI), plus an **orchestrator** (a meta-skill) that decomposes the researcher's intent into the disciplines, methods, and sources needed, and composes the relevant skills to execute.

On top of this core, thin adapters plug Seer into real usage surfaces. The first is a **Claude Cowork** plugin — which already solves, out of the box, exactly what a non-technical researcher needs: a fully conversational interface, no terminal, local file and browser access, connectors (Drive, spreadsheets, etc.), and multi-step task execution through to a deliverable (e.g., an Excel report). Seer doesn't rebuild that engine — it plugs in as the methodological and disciplinary knowledge layer the Cowork engine doesn't have on its own.

Because any single product's plugin format is, by nature, more volatile than a knowledge core, the architecture deliberately keeps the two layers separate: the skill core is never coupled to one vendor's format. This leaves the door open for future adapters to other agentic surfaces (Manus, Gemini agents, ChatGPT) without rewriting the content.

## What Makes This Different

- **Composition, not collection.** Many projects stack up skills; few have an orchestrator that decides which ones to use for a real interdisciplinary question. That's Seer's core value, not a side feature.
- **Skill ≠ Knowledge.** Each skill defines method, evidence criteria, preferred sources, and failure modes — not the domain content itself. Knowledge comes from external sources fetched at run time, which keeps skills small, reviewable, and updatable without rewrites.
- **Portability by design, not by accident.** The core is never written against one vendor's specific plugin format; adapters are the only disposable layer.
- **Explicit provenance as a rule, not a detail.** Any idea, structure, or fragment inspired by, copied from, or adapted from the BMAD Method or any other upstream project is documented with attribution and license, everywhere it appears. The BMAD Method is MIT-licensed (BMad Code, LLC); the "BMad" trademark is never used to name or promote Seer.
- **Not a giant copy of other repositories.** The earlier "download and graft" approach to third-party SKILL.md files was deliberately discarded — it creates license, quality, and maintenance problems without creating real value.

## Who This Serves

**Primary user — floor persona, not ceiling:** Sônia, 68, PhD professor and researcher at USP's Faculdade de Educação (Geography Education), writer, with no affinity for the command line or scripts. Her day-to-day use has to be 100% natural-language conversation — no step in the daily flow can require installation, commands, or configuration. A technical person ("the IT guy") does the initial setup once.

This persona defines the product's accessibility **floor** — not its ceiling. A real part of the academic community is technically fluent and will prefer to configure and extend Seer directly; the design cannot exclude either group.

**Secondary user/contributor:** the wider open-source academic community — researchers in other disciplines who want to *use* existing packs, and technically fluent developers/researchers who want to *contribute* new discipline packs (mathematics, physics, chemistry, engineering, history, geology, etc.), following the skill contract defined by the core.

## Success Criteria

The functional success criterion, as defined by the design team behind this brief: Sônia asks something like *"check the vegetative-growth indices for Brazil's North and Northeast regions between 1980–2020, by age bracket"*, in plain language — and Seer, through Cowork, decides on its own which competencies to invoke (geography, historical series, quantitative analysis), fetches what each one needs, runs the analysis, and delivers a ready report (e.g., Excel) — with the orchestration never surfacing to her as a decision she had to make.

Product success signals:

- Sônia can complete a real research task start to finish with no third-party technical intervention beyond the initial install.
- At least one discipline beyond Geography+Education is contributed by someone outside the original team, following the skill contract without needing direct support.
- No core skill needs to be rewritten when a new surface adapter is added — proof that the core/adapter separation holds up in practice.
- [ASSUMPTION] Every new skill accepted into the repository carries a provenance record (source, license, what was changed) — verifiable at PR review, not just taken on good faith.

## Scope

**In scope (v0.1 / MVP):**

- CORE academic-research skill set: literature review, source verification, citation analysis, academic writing, peer review, claim verification.
- Two discipline packs: **Geography** and **Education**.
- The orchestrator (meta-skill) able to decompose an interdisciplinary question within this scope and compose the right skills.
- A Claude Cowork adapter (plugin), covering Sônia's real usage flow.
- A formal skill contract (structure, required metadata, evidence criteria) designed from day one to let other disciplines join later without a redesign.
- Bilingual documentation (PT-BR + en-US) from the first commit: README, CONTRIBUTING, CONSTITUTION (project principles), and this brief.
- MIT licensing, with an explicit attribution/provenance mechanism for any content inspired by third parties.

**Out of scope (explicitly deferred for now):**

- Other disciplines (Geopolitics, Geoeconomics, History, Geology, and eventually Mathematics, Physics, Chemistry, Engineering, etc.) — become contributed packs once the skill contract is validated with Geography+Education.
- Adapters for other agentic surfaces (Manus, Gemini, ChatGPT) — the architecture leaves the door open, but none is built in the MVP.
- Any dedicated interface (app, website, GUI) — the MVP relies entirely on Cowork's interface; no proprietary front-end is built.
- Automated "download and graft" of skills from third-party repositories — discarded as an approach.

**Right after the MVP (not in the MVP itself):** a minimal-version "party mode" for Seer — multiple discipline personas (Geography, Education) talking to each other and to the researcher visibly, the opposite of the orchestrator's silent composition — reusing the same skill roster already built, in a simple `session` mode (no sub-agents, no persistent memory, no dynamic customization system). Full parity with `bmad-party-mode` (multiple execution modes, memory, dynamic customization) would require building a generic configuration infrastructure Seer doesn't have yet from scratch — deliberately deferred until after the MVP ships.

## Vision

If Seer succeeds, it becomes for interdisciplinary academic research what the BMAD Method is today for software development: not a closed product, but a **community standard** — a skill contract stable enough that any researcher, in any discipline, can contribute a new competency without needing to understand the engine behind it, and any new agentic surface (whether from Anthropic, Google, OpenAI, or whoever comes next) can gain a thin adapter without touching the core.

In 2-3 years, the real test of success isn't how many disciplines Seer covers on its own — it's how many were contributed by people who never talked to the original team, because the contract was clear enough for that to happen without them needing to ask.
