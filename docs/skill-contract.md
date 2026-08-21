# Contrato de Skill do Seer

Todo `SKILL.md` sob `skills/` segue este contrato. É a fusão de dois padrões reais já em produção — ver `vendor/PROVENANCE.md`:

- A camada **portável** vem do formato nativo Agent Skills (`name`, `description`, `allowed-tools`) usado por `vendor/agent-papers-cli/` — entendido diretamente por Claude Code, Codex e ferramentas compatíveis, sem tradução.
- A camada **acadêmica** vem do schema estendido de `vendor/education-agent-skills/` — evidência nomeada, schema de entrada/saída, composabilidade explícita (`chains_well_with`), limitações conhecidas.

Isso não é invenção — é o que já funciona nos dois projetos mais próximos do que o Seer precisa, generalizado além de "Educação" e "CLI de papers" para qualquer disciplina.

**Sobre idioma:** ao contrário da documentação pública do projeto (Princípio 7 da Constituição — sempre PT-BR + EN-US), o *conteúdo de skill* — frontmatter, prompt, procedimento, exemplos — fica só em **inglês**. Decisão deliberada, não uma lacuna: o material de origem que estamos herdando por fork já é em inglês, duplicar o prompt executável em duas línguas arrisca ambiguidade dentro da própria instrução que o modelo segue, e é o idioma comum de quem mais deve contribuir skills novas por fork daqui pra frente.

## Frontmatter

```yaml
---
# camada portável — entendida nativamente por Claude Code / Codex / Gemini CLI
name: <slug-em-kebab-case>
description: <uma frase — quando usar esta skill>
allowed-tools: <opcional — lista de ferramentas permitidas>

# camada acadêmica do Seer
skill_id: "<domain>/<slug>"          # ex.: "core/literature-review"
domain: "core | education | geography | <futuro pacote>"
version: "0.1.0"
evidence_strength: "strong | moderate | emerging | original"
evidence_sources:
  - "Autor (Ano) — achado, OU nome do método/norma reconhecida (ex.: PRISMA 2020)"
input_schema:
  required:
    - field: "<nome>"
      type: "string | object | ..."
      description: "<o que é>"
  optional: []
output_schema:
  fields:
    - field: "<nome>"
      type: "..."
      description: "<o que é>"
chains_well_with:
  - "<outra-skill-que-compõe-bem-com-esta>"
license: "CC BY-SA 4.0"              # conteúdo de skill — Constituição, Princípio 8
provenance: "original | forked:<repo>@<commit>, adapted"
---
```

## Corpo

1. **O Que Esta Skill Faz** — objetivo em 1-2 parágrafos.
2. **Fundamento de Evidência** — por que o método funciona; cita as `evidence_sources`. Omitida só quando `evidence_strength: original` e não há literatura a citar (raro — nesse caso, declare isso explicitamente).
3. **Procedimento** — os passos reais, executáveis. Para skills que envolvem um prompt de LLM embutido, incluir o prompt completo, com placeholders `{{campo}}` batendo com `input_schema`.
4. **Exemplo** — pelo menos um caso de uso completo, entrada→saída.
5. **Limitações Conhecidas** — obrigatória. Onde o método falha, vieses conhecidos, quando um humano precisa decidir em vez da skill (Constituição, Princípio 6).

## Regras de admissão

- `evidence_strength: original` exige justificativa no corpo — por que não há literatura a citar, e por que o método é ainda assim confiável.
- `chains_well_with` não é decorativo — é o que o orquestrador usa para montar planos. Uma skill sem nenhuma entrada aqui é, por padrão, suspeita de estar isolada demais para ser útil.
- `provenance: forked:...` exige uma linha correspondente em `vendor/PROVENANCE.md` apontando para o commit de origem.
- Skill sem `Limitações Conhecidas` não é aceita — ver Constituição, Princípio 6.

## Variantes de idioma/localidade

Quando uma skill depende de uma tradição estilística ou metodológica específica de idioma — o caso mais claro é revisão de texto (`text-revision`) — cada variante de idioma/localidade é uma skill irmã própria, nunca um único `SKILL.md` com lógica condicional por idioma escondida dentro.

- **Nomenclatura:** `<slug-base>-<localidade>`, localidade em minúsculas, formato `idioma-REGIÃO` (ex.: `line-editing-en-us`, `line-editing-en-uk`, `line-editing-pt-br`, `line-editing-pt-pt`). Nunca usar só o código de idioma (`-en`, `-pt`) quando variantes regionais divergem o suficiente para importar — o `-us`/`-uk` ou `-br`/`-pt` é o que permite a comunidade contribuir novas variantes sem colisão de nome.
- **Cada variante tem sua própria fundamentação real** (`evidence_sources`) — nunca a mesma fonte usada por outra variante só traduzida ou "adaptada de ouvido". Se a variante ainda não existe, a skill existente deve dizer isso explicitamente (não fingir cobertura que não tem) e apontar o nome esperado da irmã que falta, convidando a contribuição.
- **`chains_well_with` deve listar as irmãs existentes**, mesmo que elas não componham operacionalmente entre si — é a forma de quem descobre uma variante achar as outras.
- **Isso é distinto de uma norma regulatória específica de um país** (ex.: ABNT no Brasil) — uma norma regulatória não é uma "variante de idioma", é sua própria skill, nomeada pelo padrão que ela implementa, não por sufixo de localidade.

## Contexto de Projeto (opcional)

Uma skill pode consultar contexto declarado a nível de projeto de pesquisa, quando existir. Isto não é memória — é leitura de um documento que o próprio projeto já mantém, editável pelo pesquisador ou pelas skills que o atualizam quando algo vira decisão.

- **Onde procurar:** arquivo `metodologia.md` (ou equivalente) na raiz da pasta do projeto de pesquisa corrente — caminho configurável, nunca hardcoded a um nome único.
- **O que ler:** qual metodologia foi adotada para este projeto (ex.: estudo de caso, análise de amostras, abordagem empírica) e sua bibliografia própria — não instruções novas de procedimento, só *qual* das opções já fundamentadas na skill se aplica aqui.
- **Distinto da ata do Tabula Rasa** (`.tabula-rasa/memoria.md` / `seer_output/ata-do-projeto.md`, ver `skills/tabula-rasa/SKILL.md`): a ata é acompanhamento interno do processo da sala, não é lida por outras skills nem pensada pra virar texto publicado. `metodologia.md` é o oposto — escrito com a intenção de poder alimentar diretamente a seção de Metodologia da publicação final (tese, paper, livro), por isso os dois arquivos nunca se fundem.
- **Se não existir:** a skill segue seu comportamento padrão, sem perguntar nem exigir. Ausência de contexto de projeto nunca bloqueia a skill.
- **Se existir e conflitar** com o que a skill normalmente recomendaria: a skill sinaliza a tensão ao pesquisador em vez de decidir silenciosamente (Constituição, Princípio 6) — mesma regra que o orquestrador já aplica entre skills.

## Exemplos de referência

Duas skills já aplicam este contrato como prova de conceito:

- [`skills/core/literature-review/SKILL.md`](../skills/core/literature-review/SKILL.md) — adaptada de `vendor/agent-papers-cli/.claude/skills/literature-review/` (Apache-2.0).
- [`skills/education/ai-feedback-design-principles/SKILL.md`](../skills/education/ai-feedback-design-principles/SKILL.md) — adaptada de `vendor/education-agent-skills/skills/ai-learning-science/ai-feedback-design-principles/` (CC BY-SA 4.0).

---

# Seer Skill Contract (English / en-US)

Every `SKILL.md` under `skills/` follows this contract. It is the fusion of two real production patterns — see `vendor/PROVENANCE.md`:

- The **portable** layer comes from the native Agent Skills format (`name`, `description`, `allowed-tools`) used by `vendor/agent-papers-cli/` — understood natively by Claude Code, Codex, and compatible tools, no translation needed.
- The **academic** layer comes from the extended schema in `vendor/education-agent-skills/` — named evidence, input/output schema, explicit composability (`chains_well_with`), known limitations.

**On language:** unlike the project's public documentation (Constitution Principle 7 — always PT-BR + en-US), *skill content* — frontmatter, prompt, procedure, examples — is **English-only**. A deliberate decision, not a gap: the source material being inherited by fork is already in English, duplicating the executable prompt in two languages risks ambiguity inside the very instruction the model follows, and English is the common language of whoever is most likely to contribute new skills by fork going forward.

This isn't invention — it's what already works in the two projects closest to what Seer needs, generalized beyond "Education" and "papers CLI" to any discipline.

## Frontmatter

```yaml
---
# portable layer — understood natively by Claude Code / Codex / Gemini CLI
name: <kebab-case-slug>
description: <one sentence — when to use this skill>
allowed-tools: <optional — list of permitted tools>

# Seer's academic layer
skill_id: "<domain>/<slug>"          # e.g. "core/literature-review"
domain: "core | education | geography | <future pack>"
version: "0.1.0"
evidence_strength: "strong | moderate | emerging | original"
evidence_sources:
  - "Author (Year) — finding, OR name of a recognized method/standard (e.g. PRISMA 2020)"
input_schema:
  required:
    - field: "<name>"
      type: "string | object | ..."
      description: "<what it is>"
  optional: []
output_schema:
  fields:
    - field: "<name>"
      type: "..."
      description: "<what it is>"
chains_well_with:
  - "<another-skill-that-composes-well-with-this-one>"
license: "CC BY-SA 4.0"              # skill content — Constitution, Principle 8
provenance: "original | forked:<repo>@<commit>, adapted"
---
```

## Body

1. **What This Skill Does** — objective in 1-2 paragraphs.
2. **Evidence Foundation** — why the method works; cites `evidence_sources`. Only omitted when `evidence_strength: original` and there is no literature to cite (rare — in that case, state so explicitly).
3. **Procedure** — the actual, executable steps. For skills wrapping an embedded LLM prompt, include the full prompt, with `{{field}}` placeholders matching `input_schema`.
4. **Example** — at least one complete use case, input→output.
5. **Known Limitations** — mandatory. Where the method fails, known biases, when a human needs to decide instead of the skill (Constitution, Principle 6).

## Admission rules

- `evidence_strength: original` requires justification in the body — why there's no literature to cite, and why the method is trustworthy regardless.
- `chains_well_with` is not decorative — it's what the orchestrator uses to build plans. A skill with nothing listed here is, by default, suspect of being too isolated to be useful.
- `provenance: forked:...` requires a matching row in `vendor/PROVENANCE.md` pointing to the source commit.
- A skill without **Known Limitations** is not accepted — see Constitution, Principle 6.

## Language/locale variants

When a skill depends on a language- or locale-specific stylistic or methodological tradition — the clearest case is text revision (`text-revision`) — each language/locale variant is its own sibling skill, never a single `SKILL.md` with hidden per-language conditional logic inside.

- **Naming:** `<base-slug>-<locale>`, locale lowercase, `language-REGION` format (e.g. `line-editing-en-us`, `line-editing-en-uk`, `line-editing-pt-br`, `line-editing-pt-pt`). Never use a bare language code (`-en`, `-pt`) when regional variants diverge enough to matter — the `-us`/`-uk` or `-br`/`-pt` suffix is what lets the community contribute new variants without name collisions.
- **Each variant needs its own real grounding** (`evidence_sources`) — never the same source used by another variant, just translated or "adapted by ear." If a variant doesn't exist yet, the existing skill should say so explicitly (not pretend coverage it doesn't have) and name the expected sibling slug, inviting the contribution.
- **`chains_well_with` should list existing siblings**, even when they don't operationally compose with each other — it's how someone who finds one variant finds the others.
- **This is distinct from a country-specific regulatory standard** (e.g. ABNT in Brazil) — a regulatory standard isn't a "language variant," it's its own skill, named after the standard it implements, not tagged with a locale suffix.

## Project Context (optional)

A skill may consult context declared at the research-project level, when it exists. This is not memory — it's reading a document the project itself already maintains, editable by the researcher or by whichever skills update it once something becomes a decision.

- **Where to look:** a `metodologia.md` file (or equivalent) at the root of the current research project's folder — configurable path, never hardcoded to one fixed name.
- **What to read:** which methodology was adopted for this project (e.g. case study, sample analysis, empirical approach) and its own bibliography — not new procedural instructions, just *which* of the skill's already-grounded options applies here.
- **Distinct from Tabula Rasa's ata** (`.tabula-rasa/memoria.md` / `seer_output/ata-do-projeto.md`, see `skills/tabula-rasa/SKILL.md`): the ata is internal tracking of the room's own process, never read by other skills and not meant to become published text. `metodologia.md` is the opposite -- written with the intent that it could feed directly into the final publication's own Methodology section (a thesis, paper, or book), which is why the two files are never merged.
- **If it doesn't exist:** the skill falls back to its default behavior, without asking or requiring it. Absence of project context never blocks a skill.
- **If it exists and conflicts** with what the skill would normally recommend: the skill flags the tension to the researcher instead of silently deciding (Constitution, Principle 6) — the same rule the orchestrator already applies across skills.

## Reference examples

Two skills already apply this contract as proof of concept:

- [`skills/core/literature-review/SKILL.md`](../skills/core/literature-review/SKILL.md) — adapted from `vendor/agent-papers-cli/.claude/skills/literature-review/` (Apache-2.0).
- [`skills/education/ai-feedback-design-principles/SKILL.md`](../skills/education/ai-feedback-design-principles/SKILL.md) — adapted from `vendor/education-agent-skills/skills/ai-learning-science/ai-feedback-design-principles/` (CC BY-SA 4.0).
