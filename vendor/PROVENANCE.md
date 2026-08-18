# Proveniência dos Forks em `vendor/`

Registro obrigatório por Princípio 5 e 8 da [Constituição](../CONSTITUTION.md). Cada entrada nesta tabela corresponde a uma subpasta trazida via `git subtree` — nunca editada diretamente ali.

| Pasta | Fonte | Licença original | Commit/ref importado | Data | Papel no Seer |
|---|---|---|---|---|---|
| `education-agent-skills/` | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | CC BY-SA 4.0 | `main` @ import | 2026-08-18 | Base do pacote disciplinar `skills/education/` — 165 skills, 20 domínios, evidence-based. |
| `agent-papers-cli/` | [collaborative-deep-research/agent-papers-cli](https://github.com/collaborative-deep-research/agent-papers-cli) | Apache-2.0 | `main` @ import | 2026-08-18 | Base estrutural de `skills/core/` e `skills/orchestrator/` — padrão coordinator → deep-research/literature-review/fact-check. |

## Atualizando um fork

```bash
git subtree pull --prefix=vendor/<pasta> <url-do-repo> main --squash
```

Isso traz mudanças novas do upstream sem tocar no que já foi adaptado em `skills/`. Depois de um `pull`, revise manualmente se algo em `skills/` precisa ser realinhado.

## Regra

Conteúdo sob licença *NonCommercial* nunca entra aqui por fork ou cópia — ver Constituição, Princípio 8. Ideias de projetos assim (ex.: `Imbad0202/academic-research-skills`, CC-BY-NC 4.0) podem inspirar uma reimplementação original documentada em `skills/`, nunca uma cópia de texto ou código.

---

# Provenance of Forks in `vendor/` (English / en-US)

Required record per Principles 5 and 8 of the [Constitution](../CONSTITUTION.md). Each row in this table corresponds to a subfolder brought in via `git subtree` — never edited directly there.

| Folder | Source | Original license | Imported commit/ref | Date | Role in Seer |
|---|---|---|---|---|---|
| `education-agent-skills/` | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | CC BY-SA 4.0 | `main` @ import | 2026-08-18 | Base for the `skills/education/` discipline pack — 165 skills, 20 domains, evidence-based. |
| `agent-papers-cli/` | [collaborative-deep-research/agent-papers-cli](https://github.com/collaborative-deep-research/agent-papers-cli) | Apache-2.0 | `main` @ import | 2026-08-18 | Structural base for `skills/core/` and `skills/orchestrator/` — coordinator → deep-research/literature-review/fact-check pattern. |

## Updating a fork

```bash
git subtree pull --prefix=vendor/<folder> <repo-url> main --squash
```

This brings in new upstream changes without touching what's already been adapted in `skills/`. After a `pull`, manually review whether anything in `skills/` needs realignment.

## Rule

Content under a *NonCommercial* license is never brought in here by fork or copy — see Constitution, Principle 8. Ideas from such projects (e.g. `Imbad0202/academic-research-skills`, CC-BY-NC 4.0) may inspire a documented original reimplementation in `skills/`, never a copy of text or code.
