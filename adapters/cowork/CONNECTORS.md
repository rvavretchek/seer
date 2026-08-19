# Conectores do Plugin Seer

Segue o padrão do plugin oficial `bio-research` em [`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research) — MCP servers reais, verificados antes de entrar em `.mcp.json`, nunca inventados.

## Integrados

| Conector | Servidor | Licença | Chave de API | Status |
|---|---|---|---|---|
| OpenAlex (busca acadêmica geral) | [`cyanheads/openalex-mcp-server`](https://github.com/cyanheads/openalex-mcp-server) | Apache-2.0 | Opcional (funciona anônimo, chave grátis só melhora limite de taxa) | ⚠️ Em `.mcp.json`, mas com achado real do teste da v1.0.0-rc.1: **5 tentativas seguidas retornaram HTTP 429** (limite de taxa) no acesso anônimo. O Claude contornou de forma honesta (buscou os mesmos dados via web + Crossref, sem tentar bypass via curl/bash), então o teste de "conector funcionando" falhou mesmo com o resultado final correto. Ação recomendada: obter uma chave grátis da OpenAlex e configurar `OPENALEX_API_KEY` localmente (não commitada — vai em `.claude/settings.local.json` ou equivalente, nunca no `.mcp.json` do repositório) até confirmarmos se o limite anônimo é viável pra uso real. |

## Candidatos (pesquisados, ainda não integrados)

Verificar licença, manutenção e comando exato antes de adicionar a `.mcp.json` — mesmo rigor aplicado aos forks em `vendor/PROVENANCE.md`.

| Conector | Por que importa pro Seer | Status da pesquisa |
|---|---|---|
| IBGE / SIDRA (dados demográficos e territoriais do Brasil) | Fonte primária pra praticamente toda pergunta de Geografia/Educação com recorte Brasil — usado no exemplo real da Sônia | Nenhum MCP server real verificado ainda; precisa de busca dedicada |
| Zotero (gerenciamento de referências) | Citação/bibliografia — compõe com `core/citation-analysis` e `core/academic-writing` | Existência de skills/projetos de integração já mapeada em pesquisa anterior (`GPT_academic-skills.md`), mas nenhum MCP server específico verificado ainda |
| SciELO (literatura acadêmica em português) | Cobre o viés de idioma que `core/literature-review` já documenta como limitação conhecida | Não pesquisado ainda |
| INPE (sensoriamento remoto/dados ambientais) | Fonte primária pra `geography/physical-geography` e `geography/gis` em contexto Brasil | Não pesquisado ainda |

## Regra

Nenhum conector entra em `.mcp.json` sem verificação real (licença, comando de instalação exato, se exige chave de API) — um conector quebrado é pior que nenhum conector, porque falha silenciosamente pro pesquisador não-técnico.

---

# Seer Plugin Connectors (English / en-US)

Follows the pattern set by the official `bio-research` plugin in [`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research) — real, verified MCP servers, never invented, before anything lands in `.mcp.json`.

## Integrated

| Connector | Server | License | API key | Status |
|---|---|---|---|---|
| OpenAlex (general academic search) | [`cyanheads/openalex-mcp-server`](https://github.com/cyanheads/openalex-mcp-server) | Apache-2.0 | Optional (works anonymously; a free key only improves rate limits) | ⚠️ In `.mcp.json`, but with a real finding from the v1.0.0-rc.1 test: **5 consecutive attempts returned HTTP 429** (rate limit) on anonymous access. Claude handled it honestly (found the same data via web search + Crossref, without trying to bypass via curl/bash), so the deliverable was still correct but the "connector actually works" test failed. Recommended action: get a free OpenAlex API key and set `OPENALEX_API_KEY` locally (not committed -- goes in `.claude/settings.local.json` or equivalent, never in the repo's `.mcp.json`) until we confirm whether the anonymous limit is viable for real use. |

## Candidates (researched, not yet integrated)

Verify license, maintenance, and exact command before adding to `.mcp.json` -- the same rigor applied to forks in `vendor/PROVENANCE.md`.

| Connector | Why it matters for Seer | Research status |
|---|---|---|
| IBGE / SIDRA (Brazilian demographic and territorial data) | Primary source for almost any Brazil-scoped Geography/Education question -- used in Sonia's own real example | No real MCP server verified yet; needs a dedicated search |
| Zotero (reference management) | Citation/bibliography -- composes with `core/citation-analysis` and `core/academic-writing` | Prior research (`GPT_academic-skills.md`) mapped integration skills/projects, but no specific MCP server verified yet |
| SciELO (Portuguese-language academic literature) | Addresses the language-coverage bias `core/literature-review` already documents as a known limitation | Not researched yet |
| INPE (remote sensing / environmental data) | Primary source for `geography/physical-geography` and `geography/gis` in a Brazil context | Not researched yet |

## Rule

No connector goes into `.mcp.json` without real verification (license, exact install command, whether it needs an API key) -- a broken connector is worse than no connector, because it fails silently on a non-technical researcher.
