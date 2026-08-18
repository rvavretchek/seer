# Contribuindo com o Seer

Obrigado pelo interesse em contribuir. Este documento cobre como o projeto está organizado, o que uma contribuição precisa carregar e como ela chega ao repositório. Os princípios que toda contribuição precisa respeitar estão em [CONSTITUTION.md](CONSTITUTION.md) — vale a pena ler antes de propor algo grande.

> O contrato formal de skill (estrutura exata de metadados, campos obrigatórios de uma skill de disciplina) ainda está em desenho. Este documento descreve o que já está decidido; será expandido assim que o contrato for publicado.

## O que pode ser contribuído

- **Pacotes disciplinares novos** — matemática, física, química, engenharia, história, geologia, geopolítica, geoeconomia etc. — seguindo o mesmo contrato de skill usado por Geografia e Educação.
- **Skills CORE novas ou melhoradas** — competências de pesquisa acadêmica genérica (revisão bibliográfica, verificação de fontes, citação, escrita, revisão por pares).
- **Melhorias no orquestrador** — lógica de decomposição de perguntas de pesquisa em disciplinas/métodos/fontes.
- **Adaptadores de superfície** — novos plugins para outras ferramentas agênticas (o núcleo nunca deve precisar mudar para isso; se precisar, é um sinal de que o adaptador está mal desenhado — ver Constituição, Princípio 2).
- **Documentação e traduções.**

## O que toda contribuição precisa carregar

1. **Proveniência explícita.** Se qualquer parte do que você está contribuindo foi inspirada, copiada ou adaptada de outro projeto — o BMAD Method incluído — isso precisa estar documentado no próprio artefato: fonte, licença, o que foi alterado. Sem isso, o PR não é aceito, independente da qualidade do conteúdo. Ver Constituição, Princípio 5.
2. **Compatibilidade de licença.** O Seer é MIT. Toda contribuição precisa ser compatível com MIT ou declarar explicitamente uma exceção documentada (ex.: uma skill que depende de um dataset sob outra licença).
3. **Aderência a "Skill ≠ Conhecimento".** Uma skill de disciplina descreve método — objetivo, procedimento, critérios de evidência, fontes preferenciais, vieses conhecidos, modos de falha. Não é um resumo do assunto nem uma base de conhecimento embutida.
4. **Documentação bilíngue.** Todo artefato de documentação pública (não necessariamente comentários de código) é escrito em Português do Brasil, seguido da versão completa em inglês (en-US), no mesmo arquivo.

## Fluxo de branches

- `main` — estável, reflete o que está publicado.
- `dev` — branch de integração ativa; contribuições miram aqui, não `main`.
- `feature/*`, `skill/*`, `fix/*` — branches de trabalho, uma por contribuição, a partir de `dev`.

Nenhuma complexidade além disso por enquanto — o projeto está no início.

## Processo de Pull Request

1. Abra a branch a partir de `dev`.
2. Inclua a nota de proveniência (mesmo que seja "conteúdo original, sem inspiração externa direta").
3. Descreva o que a contribuição faz e, se for uma skill nova, com quais outras skills ela se compõe (o orquestrador precisa saber disso).
4. Abra o PR contra `dev`. Revisão verifica: licença, proveniência, aderência ao contrato de skill vigente, e se a documentação (quando aplicável) está bilíngue.

## Código de conduta

Trate colegas contribuidores com respeito profissional. Discordância técnica é bem-vinda e esperada; ataque pessoal não é.

---

# Contributing to Seer (English / en-US)

Thanks for your interest in contributing. This document covers how the project is organized, what a contribution needs to carry, and how it reaches the repository. The principles every contribution must respect live in [CONSTITUTION.md](CONSTITUTION.md) — worth reading before proposing something large.

> The formal skill contract (exact metadata structure, required fields for a discipline skill) is still being designed. This document describes what's already settled; it will expand once the contract is published.

## What can be contributed

- **New discipline packs** — mathematics, physics, chemistry, engineering, history, geology, geopolitics, geoeconomics, etc. — following the same skill contract used by Geography and Education.
- **New or improved CORE skills** — generic academic-research competencies (literature review, source verification, citation, writing, peer review).
- **Orchestrator improvements** — logic for decomposing research questions into disciplines/methods/sources.
- **Surface adapters** — new plugins for other agentic tools (the core should never need to change for this; if it does, that's a sign the adapter is poorly designed — see Constitution, Principle 2).
- **Documentation and translations.**

## What every contribution needs to carry

1. **Explicit provenance.** If any part of what you're contributing was inspired by, copied from, or adapted from another project — the BMAD Method included — it needs to be documented in the artifact itself: source, license, what was changed. Without this, the PR is not accepted, regardless of content quality. See Constitution, Principle 5.
2. **License compatibility.** Seer is MIT. Every contribution needs to be MIT-compatible or explicitly declare a documented exception (e.g. a skill that depends on a dataset under a different license).
3. **Adherence to "Skill ≠ Knowledge".** A discipline skill describes method — objective, procedure, evidence criteria, preferred sources, known biases, failure modes. It is not a subject-matter summary or an embedded knowledge base.
4. **Bilingual documentation.** Every public documentation artifact (not necessarily code comments) is written in Brazilian Portuguese, followed by the complete English (en-US) version, in the same file.

## Branching flow

- `main` — stable, reflects what's published.
- `dev` — active integration branch; contributions target this, not `main`.
- `feature/*`, `skill/*`, `fix/*` — working branches, one per contribution, cut from `dev`.

No more complexity than that for now — the project is at an early stage.

## Pull request process

1. Open your branch from `dev`.
2. Include the provenance note (even if it's "original content, no direct external inspiration").
3. Describe what the contribution does and, if it's a new skill, which other skills it composes with (the orchestrator needs to know this).
4. Open the PR against `dev`. Review checks: license, provenance, adherence to the current skill contract, and — where applicable — whether documentation is bilingual.

## Code of conduct

Treat fellow contributors with professional respect. Technical disagreement is welcome and expected; personal attacks are not.
