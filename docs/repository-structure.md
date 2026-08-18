# Estrutura do Repositório

Como o Seer está organizado e por quê. Reflete diretamente os Princípios 1, 2 e 5 da [Constituição](../CONSTITUTION.md): skill separada de conhecimento, núcleo portátil, proveniência explícita.

```
Seer/
├── vendor/           # Forks reais de projetos upstream, com histórico git preservado.
│                     # Nunca editado diretamente — só atualizado via `git subtree pull`.
│                     # Cada subpasta tem proveniência (fonte, licença, versão) em vendor/PROVENANCE.md.
│
├── skills/           # O núcleo de skills do Seer — o que o orquestrador realmente carrega.
│   ├── orchestrator/ # A meta-skill: decompõe a pergunta de pesquisa e compõe as skills certas.
│   ├── core/          # Skills de pesquisa acadêmica genérica (revisão bibliográfica, citação,
│   │                  # verificação de fontes, escrita, revisão por pares). Curadas a partir de
│   │                  # vendor/agent-papers-cli/, adaptadas ao contrato de skill do Seer.
│   ├── education/     # Pacote disciplinar Educação. Curado a partir de
│   │                  # vendor/education-agent-skills/.
│   └── geography/     # Pacote disciplinar Geografia. Sem fork de conteúdo disponível no
│                      # ecossistema (ver vendor/PROVENANCE.md) — construído majoritariamente
│                      # original, usando GeoAgent/QGIS como conector de ferramenta, não como
│                      # fonte de conteúdo de skill.
│
├── adapters/         # Camadas finas que plugam o núcleo em superfícies de uso reais.
│   └── cowork/        # Plugin para Claude Cowork (primeiro adaptador, MVP).
│
├── docs/             # Este arquivo, arquitetura, contrato de skill (quando publicado), taxonomia.
│
├── tests/            # Testes do orquestrador e das skills (formato ainda a definir).
│
├── _bmad/, _bmad-output/, .claude/, .bmad-loop/  # Ferramental de desenvolvimento (BMAD Method +
│                                                   # bmad-loop) usado para *construir* o Seer.
│                                                   # Não faz parte do produto Seer em si.
│
├── CONSTITUTION.md   # Princípios fundadores — o que nunca muda.
├── CONTRIBUTING.md   # Como contribuir.
├── README.md
└── LICENSE           # MIT (código). Conteúdo de skill é CC BY-SA 4.0 — ver Constituição, Princípio 8.
```

## Por que `vendor/` existe separado de `skills/`

Um fork honesto precisa manter o material original rastreável e atualizável — não copiado e imediatamente reescrito sem deixar rastro. `vendor/` é o espelho do upstream (via `git subtree`, preservando histórico); `skills/` é o que o Seer realmente expõe ao orquestrador, já adaptado ao contrato de skill do projeto. Quando o upstream lança uma versão nova, `git subtree pull` atualiza `vendor/` sem tocar nas adaptações que já vivem em `skills/`.

## Por que `academic-agent-stack/`, `GPT_academic-skills.md` e `GEMINI_academic-skills.md` não estão nesta árvore

São material de contexto de uma exploração inicial do problema, preservados na raiz do repositório como referência histórica — não fazem parte da arquitetura do produto e não são importados por nada em `skills/` ou `vendor/`.

---

# Repository Structure (English / en-US)

How Seer is organized and why. Directly reflects Principles 1, 2, and 5 of the [Constitution](../CONSTITUTION.md): skill separated from knowledge, portable core, explicit provenance.

```
Seer/
├── vendor/           # Real forks of upstream projects, with git history preserved.
│                     # Never edited directly — only updated via `git subtree pull`.
│                     # Each subfolder has provenance (source, license, version) in vendor/PROVENANCE.md.
│
├── skills/           # Seer's actual skill core — what the orchestrator really loads.
│   ├── orchestrator/ # The meta-skill: decomposes the research question and composes the right skills.
│   ├── core/          # Generic academic-research skills (literature review, citation,
│   │                  # source verification, writing, peer review). Curated from
│   │                  # vendor/agent-papers-cli/, adapted to Seer's skill contract.
│   ├── education/     # Education discipline pack. Curated from
│   │                  # vendor/education-agent-skills/.
│   └── geography/     # Geography discipline pack. No content fork available in the
│                      # ecosystem (see vendor/PROVENANCE.md) — built mostly original,
│                      # using GeoAgent/QGIS as a tool connector, not a skill-content source.
│
├── adapters/         # Thin layers that plug the core into real usage surfaces.
│   └── cowork/         # Claude Cowork plugin (first adapter, MVP).
│
├── docs/             # This file, architecture, skill contract (once published), taxonomy.
│
├── tests/            # Orchestrator and skill tests (format still to be defined).
│
├── _bmad/, _bmad-output/, .claude/, .bmad-loop/  # Development tooling (BMAD Method +
│                                                   # bmad-loop) used to *build* Seer.
│                                                   # Not part of the Seer product itself.
│
├── CONSTITUTION.md   # Founding principles — what never changes.
├── CONTRIBUTING.md   # How to contribute.
├── README.md
└── LICENSE           # MIT (code). Skill content is CC BY-SA 4.0 — see Constitution, Principle 8.
```

## Why `vendor/` exists separately from `skills/`

An honest fork needs to keep the original material traceable and updatable — not copied and immediately rewritten without a trace. `vendor/` mirrors upstream (via `git subtree`, preserving history); `skills/` is what Seer actually exposes to the orchestrator, already adapted to the project's skill contract. When upstream ships a new version, `git subtree pull` updates `vendor/` without touching the adaptations already living in `skills/`.

## Why `academic-agent-stack/`, `GPT_academic-skills.md`, and `GEMINI_academic-skills.md` aren't in this tree

They're context material from an early exploration of the problem, preserved at the repository root as historical reference — not part of the product architecture, and not imported by anything in `skills/` or `vendor/`.
