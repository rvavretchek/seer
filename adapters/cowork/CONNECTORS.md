# Conectores do Plugin Seer

Segue o padrão do plugin oficial `bio-research` em [`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research) — MCP servers reais, verificados antes de entrar em `.mcp.json`, nunca inventados.

## Integrados

| Conector | Servidor | Licença | Chave de API | Status |
|---|---|---|---|---|
| OpenAlex (busca acadêmica geral) | [`cyanheads/openalex-mcp-server`](https://github.com/cyanheads/openalex-mcp-server) | Apache-2.0 | **Obrigatória desde 13/fev/2026** (política da própria OpenAlex mudou — ver abaixo). Grátis. | ⚠️ Causa raiz identificada, correção aplicada em `.mcp.json`, pendente de teste com chave real. |

### Causa raiz do 429 observado no teste da v1.0.0-rc.1

A OpenAlex **descontinuou o "polite pool"** (o mecanismo antigo, baseado só em enviar um e-mail via `mailto=`, sem cadastro) em 13 de fevereiro de 2026. A partir dessa data:

- **Sem chave**: 100 créditos/dia — na prática, inviável pra uso real (é o que bateu no nosso teste: 5 tentativas já estouraram).
- **Com chave grátis** (criando conta em `openalex.org` e pegando a chave em `openalex.org/settings/api`): 100.000 créditos/dia.

Isso não é uma otimização opcional como a documentação do `openalex-mcp-server` ainda sugere (provavelmente escrita antes da mudança) — **é obrigatório pra qualquer uso real hoje**.

`adapters/cowork/.mcp.json` já referencia `"OPENALEX_API_KEY": "${OPENALEX_API_KEY}"` — expansão de variável de ambiente, nunca a chave em texto puro no repositório. Falta: cada pessoa que instalar o plugin configurar essa variável de ambiente no próprio sistema, com sua própria chave (ver `README.md` deste diretório para o passo a passo no Windows).

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
| OpenAlex (general academic search) | [`cyanheads/openalex-mcp-server`](https://github.com/cyanheads/openalex-mcp-server) | Apache-2.0 | **Required as of 2026-02-13** (OpenAlex's own policy changed -- see below). Free. | ⚠️ Root cause identified, fix applied in `.mcp.json`, pending a test with a real key. |

### Root cause of the 429 observed in the v1.0.0-rc.1 test

OpenAlex **discontinued the "polite pool"** (the old mechanism -- just sending an email via `mailto=`, no account needed) on February 13, 2026. Since then:

- **No key**: 100 credits/day -- in practice, unviable for real use (exactly what our test hit: 5 attempts already exhausted it).
- **With a free key** (create an account at `openalex.org`, get the key at `openalex.org/settings/api`): 100,000 credits/day.

This isn't an optional optimization the way `openalex-mcp-server`'s own docs still suggest (likely written before the policy changed) -- **it's required for any real use today**.

`adapters/cowork/.mcp.json` already references `"OPENALEX_API_KEY": "${OPENALEX_API_KEY}"` -- environment-variable expansion, never the raw key in the repository. What's left: anyone installing the plugin needs to set that environment variable on their own system, with their own key (see this directory's `README.md` for the Windows walkthrough).

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
