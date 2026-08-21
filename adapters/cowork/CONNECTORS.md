# Conectores do Plugin Seer

Segue o padrão do plugin oficial `bio-research` em [`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research) — MCP servers reais, verificados antes de entrar em `.mcp.json`, nunca inventados.

## Integrados

| Conector | Servidor | Licença | Chave de API | Status |
|---|---|---|---|---|
| OpenAlex (busca acadêmica geral) | [`cyanheads/openalex-mcp-server`](https://github.com/cyanheads/openalex-mcp-server) | Apache-2.0 | **Obrigatória desde 13/fev/2026** (política da própria OpenAlex mudou — ver abaixo). Grátis. | ⚠️ Causa raiz identificada, correção aplicada em `.mcp.json`, pendente de teste com chave real. |
| IBGE / SIDRA (dados geográficos, demográficos e estatísticos do Brasil) | [`SidneyBissoli/ibge-br-mcp`](https://github.com/SidneyBissoli/ibge-br-mcp) ([`ibge-br-mcp` no npm](https://www.npmjs.com/package/ibge-br-mcp)) | MIT | Nenhuma — consulta as APIs públicas do IBGE diretamente. | ✅ Verificado (ver seção abaixo), com confiança suficiente pra recomendar. **Ainda não está em `.mcp.json`** — a edição automática desse arquivo foi bloqueada nesta sessão (mudanças em `.mcp.json` exigem aprovação humana explícita); entrada pronta pra colar está documentada abaixo. |

### Causa raiz do 429 observado no teste da v1.0.0-rc.1

A OpenAlex **descontinuou o "polite pool"** (o mecanismo antigo, baseado só em enviar um e-mail via `mailto=`, sem cadastro) em 13 de fevereiro de 2026. A partir dessa data:

- **Sem chave**: 100 créditos/dia — na prática, inviável pra uso real (é o que bateu no nosso teste: 5 tentativas já estouraram).
- **Com chave grátis** (criando conta em `openalex.org` e pegando a chave em `openalex.org/settings/api`): 100.000 créditos/dia.

Isso não é uma otimização opcional como a documentação do `openalex-mcp-server` ainda sugere (provavelmente escrita antes da mudança) — **é obrigatório pra qualquer uso real hoje**.

`adapters/cowork/.mcp.json` já referencia `"OPENALEX_API_KEY": "${OPENALEX_API_KEY}"` — expansão de variável de ambiente, nunca a chave em texto puro no repositório. Falta: cada pessoa que instalar o plugin configurar essa variável de ambiente no próprio sistema, com sua própria chave (ver `README.md` deste diretório para o passo a passo no Windows).

### Verificação do `ibge-br-mcp` (IBGE/SIDRA)

Pesquisa dedicada (21/ago/2026) não encontrou nenhum MCP server "oficial" do IBGE, mas encontrou um candidato real e independente que passou no mesmo padrão de rigor do OpenAlex:

- **Mantenedor**: Sidney da Silva Pereira Bissoli, pessoa física identificável (não anônimo), autor de outros pacotes próprios (`@sbissoli/mcp-provenance`, `@sbissoli/mcp-stats`) usados como dependência.
- **Publicado no npm** como `ibge-br-mcp`, versão 3.3.0 publicada em 08/ago/2026 (ativo, não abandonado). Licença MIT.
- **Sem chave de API** — consulta diretamente as APIs públicas do IBGE (SIDRA, Agregados, Localidades, Malhas, Nomes, Censo 2022 etc.) via `servicodados.ibge.gov.br`.
- **Superfície de dependências enxuta**: só `zod` e dois pacotes do próprio autor — um de "provenance" (anexa fonte/endpoint/data de extração/licença em cada resposta, útil pra citação acadêmica) e um de estatísticas, ambos computação local, sem telemetria externa. Sem `postinstall` suspeito.
- **22 ferramentas expostas** (`ibge_sidra`, `ibge_municipios`, `ibge_censo`, `ibge_malhas`, etc.), 460+ testes automatizados com 97%+ de cobertura, TypeScript strict.
- Comparação de escala com o OpenAlex: `openalex-mcp-server` também tem tração pequena (poucas estrelas) — o critério real de confiança aqui é mantenedor identificável + código limpo + licença permissiva + pacote publicado corretamente, não popularidade.

Existe também um projeto muito maior, `mcp-brasil` (~1.7k estrelas, 70 APIs públicas brasileiras incluindo 9 ferramentas de IBGE/SIDRA e 4 de INPE), mas foi **descartado** por agora: mantenedor pseudônimo sem identidade verificável, organização sem membros públicos, superfície de 533 ferramentas (muito além do que o Seer precisa), e dependências incomuns pra um MCP server (SDK da Anthropic, Playwright) que aumentam a área de ataque sem necessidade clara. Vale reconsiderar futuramente se o projeto amadurecer e o mantenedor se identificar.

**Entrada pronta pra `.mcp.json`** (não aplicada automaticamente nesta sessão — precisa de uma pessoa ou de uma sessão com permissão de editar esse arquivo):

```json
"ibge-br-mcp": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "ibge-br-mcp"]
}
```

### INPE: nenhum MCP server adicionado — API direta documentada em vez disso

Diferente do IBGE, o INPE **não tem** uma API REST/JSON simples equivalente à `servicodados.ibge.gov.br`. Os dados de PRODES/DETER (desmatamento) e focos de queimada são expostos assim:

- **PRODES/DETER (desmatamento)**: via GeoServer do TerraBrasilis, protocolo OGC WFS/WMS/WCS — ex.: `https://terrabrasilis.dpi.inpe.br/geoserver/deter-amz/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=deter_public&CQL_FILTER=date BETWEEN '2019-01-01' AND '2019-02-01'&outputFormat=application/json`. Público, sem cadastro nem chave, mas exige entender sintaxe WFS/CQL e sistemas de referência espacial (EPSG) — mais complexo que um REST simples.
- **Queimadas/focos de calor**: arquivos CSV/KML em `https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/{mensal,anual}/Brasil/`, também público e sem chave, mas como download de arquivo particionado por data, não como endpoint de consulta.
- Nenhum MCP server dedicado e confiável foi encontrado: o único achado específico (`bruno-portfolio/agrobr-mcp`) é um agregador agrícola pequeno (26 estrelas) de mantenedor não verificado, com cobertura de INPE vaga (não especifica se é PRODES ou DETER) e sem foco em geografia/clima; e o `mcp-brasil` acima já foi descartado pelos mesmos motivos.

**Decisão**: nenhum MCP server foi adicionado a `.mcp.json` para INPE. As APIs acima são públicas e sem chave, então skills de `geography/physical-geography` e `geography/gis` podem chamá-las diretamente via HTTP quando precisarem — mas isso é trabalho de documentação dentro dessas skills (procedimento com exemplos de query WFS/CQL), não um conector genérico de `.mcp.json`. Um wrapper MCP dedicado pro INPE (que traduza essas queries WFS pra ferramentas simples tipo `inpe_desmatamento(municipio, ano)`) é candidato razoável pra construir sob medida no futuro, mas não existe hoje de forma confiável.

### SciELO: nenhum MCP server confiável encontrado — API oficial de metadados documentada em vez disso

Pesquisa dedicada (21/ago/2026). Dois candidatos a MCP server foram examinados e nenhum passou no rigor aplicado ao IBGE:

- **`leomcamilo/bx-scholar-mcp`** — único hit específico em busca de código no GitHub (`"scielo" "mcp-server"`). Mantenedor identificável (Leonardo Mello Camilo da Silva, `baxijen.com.br`), licença MIT, mas **não publicado em nenhum registro de pacotes** (nem npm nem PyPI — `pip install`/`npx` não funcionam, só clonar o monorepo e rodar via `uv`), **zero estrelas, zero forks**, criado em abril/2026 (~4 meses de idade, sem tração externa). Mais grave: inspecionado o código-fonte (`packages/bx-scholar-core/src/bx_scholar_core/clients/scielo.py`) — o "suporte a SciELO" **não é uma integração real com a API oficial da SciELO**. É a API da OpenAlex filtrada por publicador SciELO, com fallback pra fazer scraping de `search.scielo.org` (busca não-documentada, não uma API pública) quando a consulta à OpenAlex falha. Ou seja: nem resolve nem evita o tipo de fragilidade que já causou os 403 observados — só reduz a chance de precisar dela. Não publicado + zero tração + "integração" que na prática é outra coisa não passa no padrão de rigor (mesmo aplicado ao `mcp-brasil`, descartado por motivos parecidos).
- Nenhum outro candidato específico de SciELO foi encontrado em npm, PyPI, GitHub code search, ou nos diretórios mcpservers.org / smithery.ai / mcp.so.

**API oficial da SciELO, verificada ao vivo**: a rede SciELO mantém a **Article Meta API** (`https://articlemeta.scielo.org`, mantida pela própria SciELO em [`scieloorg/articles_meta`](https://github.com/scieloorg/articles_meta), licença BSD-2-Clause, push mais recente em 13/ago/2026 — ativa) e um provedor **OAI-PMH** ([`scieloorg/oai-pmh`](https://github.com/scieloorg/oai-pmh)) por cima dela. Testado nesta pesquisa:

- `GET https://articlemeta.scielo.org/api/v1/collection/`, `/journal/`, `/article/identifiers/` e `/article/?collection=scl&code=...` — todos responderam **HTTP 200** com JSON real, sem chave nem cadastro.
- Retorna **só metadados** (título, autores, resumo/abstract completo, DOI, datas, palavras-chave) — nunca o texto completo do artigo.
- Formato legado, no estilo ISIS/CDS (tags tipo `v12`=título, `v83`=resumo, `v10`=autores) em vez de campos com nome — a própria SciELO publica a biblioteca Python `xylose` pra traduzir isso; não existe equivalente em JS/TS, e não existe wrapper MCP que já faça essa tradução.
- **Isso explica, e resolve pra descoberta/metadados, o problema dos 403 observado no teste do Cowork**: testado diretamente nesta pesquisa, `https://www.scielo.br/j/rae/a/8gWWSDpsktKM4jHfDpKCGKp/` (página HTML do artigo) retorna **403** tanto com quanto sem User-Agent de navegador — é proteção de bot no site de leitura (`www.scielo.br`), não uma questão de chave/autenticação. Já `articlemeta.scielo.org` é uma API JSON separada, sem essa proteção, e respondeu 200 de forma consistente. **Mas isso não resolve a extração de texto completo**: o mesmo teste com `?format=pdf` na mesma URL também voltou 403 — a API de metadados não dá acesso ao PDF/texto integral, só ao resumo.

**Decisão**: nenhum MCP server foi adicionado a `.mcp.json` para SciELO — nenhum candidato encontrado passa no padrão de rigor (mantenedor com histórico, pacote publicado, dependências limpas). A Article Meta API é real, pública, sem chave e ativa, mas retorna só metadados num formato legado que exige uma camada de tradução — documentá-la como chamada HTTP direta dentro de `core/literature-review` (pra descoberta/triagem de literatura em português, não pra leitura de texto completo) é trabalho razoável de skill, não de conector genérico. Um wrapper MCP dedicado (que traduza os campos `vNN` e talvez componha com OAI-PMH) seria um bom candidato pra construir sob medida no futuro — nenhum existe hoje.

## Candidatos (pesquisados, ainda não integrados)

Verificar licença, manutenção e comando exato antes de adicionar a `.mcp.json` — mesmo rigor aplicado aos forks em `vendor/PROVENANCE.md`.

| Conector | Por que importa pro Seer | Status da pesquisa |
|---|---|---|
| Zotero (gerenciamento de referências) | Citação/bibliografia — compõe com `core/citation-analysis` e `core/academic-writing` | Existência de skills/projetos de integração já mapeada em pesquisa anterior (`GPT_academic-skills.md`), mas nenhum MCP server específico verificado ainda |
| SciELO (literatura acadêmica em português) | Cobre o viés de idioma que `core/literature-review` já documenta como limitação conhecida | Pesquisado (21/ago/2026) — ver seção acima. Nenhum MCP server confiável encontrado; Article Meta API oficial (metadados, sem chave) documentada pra uso direto em skills, sem wrapper MCP por enquanto. |
| INPE (sensoriamento remoto/dados ambientais) | Fonte primária pra `geography/physical-geography` e `geography/gis` em contexto Brasil | Pesquisado (21/ago/2026) — ver seção acima. Nenhum MCP server confiável encontrado; API direta (WFS/CSV) documentada pra uso futuro em skills, sem wrapper MCP por enquanto. |

## Regra

Nenhum conector entra em `.mcp.json` sem verificação real (licença, comando de instalação exato, se exige chave de API) — um conector quebrado é pior que nenhum conector, porque falha silenciosamente pro pesquisador não-técnico.

---

# Seer Plugin Connectors (English / en-US)

Follows the pattern set by the official `bio-research` plugin in [`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research) — real, verified MCP servers, never invented, before anything lands in `.mcp.json`.

## Integrated

| Connector | Server | License | API key | Status |
|---|---|---|---|---|
| OpenAlex (general academic search) | [`cyanheads/openalex-mcp-server`](https://github.com/cyanheads/openalex-mcp-server) | Apache-2.0 | **Required as of 2026-02-13** (OpenAlex's own policy changed -- see below). Free. | ⚠️ Root cause identified, fix applied in `.mcp.json`, pending a test with a real key. |
| IBGE / SIDRA (Brazilian geographic, demographic and statistical data) | [`SidneyBissoli/ibge-br-mcp`](https://github.com/SidneyBissoli/ibge-br-mcp) ([`ibge-br-mcp` on npm](https://www.npmjs.com/package/ibge-br-mcp)) | MIT | None -- queries IBGE's public APIs directly. | ✅ Verified (see section below), confident enough to recommend. **Not yet in `.mcp.json`** -- this session's automatic edit to that file was blocked (changes to `.mcp.json` require explicit human approval); a ready-to-paste entry is documented below. |

### Root cause of the 429 observed in the v1.0.0-rc.1 test

OpenAlex **discontinued the "polite pool"** (the old mechanism -- just sending an email via `mailto=`, no account needed) on February 13, 2026. Since then:

- **No key**: 100 credits/day -- in practice, unviable for real use (exactly what our test hit: 5 attempts already exhausted it).
- **With a free key** (create an account at `openalex.org`, get the key at `openalex.org/settings/api`): 100,000 credits/day.

This isn't an optional optimization the way `openalex-mcp-server`'s own docs still suggest (likely written before the policy changed) -- **it's required for any real use today**.

`adapters/cowork/.mcp.json` already references `"OPENALEX_API_KEY": "${OPENALEX_API_KEY}"` -- environment-variable expansion, never the raw key in the repository. What's left: anyone installing the plugin needs to set that environment variable on their own system, with their own key (see this directory's `README.md` for the Windows walkthrough).

### Verification of `ibge-br-mcp` (IBGE/SIDRA)

Dedicated research (2026-08-21) found no "official" IBGE MCP server, but did find a real, independent candidate that clears the same bar applied to OpenAlex:

- **Maintainer**: Sidney da Silva Pereira Bissoli, an identifiable real person (not anonymous), also author of the two small utility packages it depends on (`@sbissoli/mcp-provenance`, `@sbissoli/mcp-stats`).
- **Published on npm** as `ibge-br-mcp`, latest version 3.3.0 published 2026-08-08 (active, not abandoned). MIT license.
- **No API key** -- queries IBGE's public APIs directly (SIDRA, Agregados, Localidades, Malhas, Nomes, 2022 Census, etc.) via `servicodados.ibge.gov.br`.
- **Lean dependency surface**: just `zod` plus two packages by the same author -- one adds a "provenance" block (source, endpoint, extraction date, license) to every tool response, useful for academic citation; the other computes stats locally. Both are local-only, no external telemetry. No suspicious `postinstall` script.
- **22 tools exposed** (`ibge_sidra`, `ibge_municipios`, `ibge_censo`, `ibge_malhas`, etc.), 460+ automated tests at 97%+ coverage, strict TypeScript.
- Scale comparison with OpenAlex: `openalex-mcp-server` itself also has low star count -- the actual trust criterion here is an identifiable maintainer + clean code + a permissive license + a properly published package, not popularity.

A much larger project, `mcp-brasil` (~1.7k stars, 70 Brazilian public APIs including 9 IBGE/SIDRA tools and 4 INPE tools), was also found but **rejected** for now: pseudonymous maintainer with no verifiable identity, an organization with no public members, a 533-tool surface (far beyond what Seer needs), and unusual dependencies for an MCP server (the Anthropic SDK, Playwright) that widen the attack surface without a clear reason. Worth reconsidering later if the project matures and the maintainer identifies themselves.

**Ready-to-paste `.mcp.json` entry** (not applied automatically this session -- needs a person, or a session with permission to edit that file):

```json
"ibge-br-mcp": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "ibge-br-mcp"]
}
```

### INPE: no MCP server added -- direct API documented instead

Unlike IBGE, INPE does **not** have a simple REST/JSON API equivalent to `servicodados.ibge.gov.br`. PRODES/DETER deforestation data and fire-hotspot data are exposed like this instead:

- **PRODES/DETER (deforestation)**: via TerraBrasilis's GeoServer, OGC WFS/WMS/WCS protocol -- e.g. `https://terrabrasilis.dpi.inpe.br/geoserver/deter-amz/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=deter_public&CQL_FILTER=date BETWEEN '2019-01-01' AND '2019-02-01'&outputFormat=application/json`. Public, no registration or key, but requires understanding WFS/CQL query syntax and spatial reference systems (EPSG) -- more complex than a plain REST call.
- **Fire hotspots (queimadas)**: CSV/KML files at `https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/{mensal,anual}/Brasil/`, also public and keyless, but as date-partitioned file downloads rather than a query endpoint.
- No dedicated, trustworthy MCP server was found: the one INPE-specific hit (`bruno-portfolio/agrobr-mcp`) is a small agriculture aggregator (26 stars) from an unverified maintainer, with vague INPE coverage (doesn't specify PRODES vs. DETER) and no geography/climate focus; and `mcp-brasil` above was already rejected for the reasons listed.

**Decision**: no MCP server was added to `.mcp.json` for INPE. The APIs above are public and keyless, so `geography/physical-geography` and `geography/gis` skills can call them directly over HTTP when they need to -- but that's documentation work inside those skills (a procedure with WFS/CQL query examples), not a generic `.mcp.json` connector. A dedicated INPE MCP wrapper (translating these WFS queries into simple tools like `inpe_deforestation(municipality, year)`) is a reasonable candidate to build later, but nothing trustworthy exists today.

### SciELO: no trustworthy MCP server found -- SciELO's own metadata API documented instead

Dedicated research (2026-08-21). Two MCP-server candidates were examined and neither cleared the bar applied to IBGE:

- **`leomcamilo/bx-scholar-mcp`** -- the only SciELO-specific hit from a GitHub code search (`"scielo" "mcp-server"`). Identifiable maintainer (Leonardo Mello Camilo da Silva, `baxijen.com.br`), MIT license, but **not published to any package registry** (no npm, no PyPI -- `npx`/`pip install` don't work; it's clone-the-monorepo-and-run-via-`uv` only), **zero stars, zero forks**, created April 2026 (~4 months old, no external traction). More important: inspecting the actual source (`packages/bx-scholar-core/src/bx_scholar_core/clients/scielo.py`) shows its "SciELO support" **is not a real integration with SciELO's own API**. It's the OpenAlex API filtered to SciELO-published works, with a fallback that scrapes `search.scielo.org` (an undocumented search endpoint, not a public API) when the OpenAlex query fails. That doesn't fix or avoid the class of fragility that produced the 403s already observed -- it just reduces how often you'd hit it. Unpublished + zero traction + a "SciELO integration" that's actually something else fails the same bar `mcp-brasil` was rejected on.
- No other SciELO-specific candidate turned up on npm, PyPI, GitHub code search, or the mcpservers.org / smithery.ai / mcp.so directories.

**SciELO's own API, verified live**: the SciELO network runs the **Article Meta API** (`https://articlemeta.scielo.org`, maintained by SciELO itself at [`scieloorg/articles_meta`](https://github.com/scieloorg/articles_meta), BSD-2-Clause license, most recent push 2026-08-13 -- active) plus an **OAI-PMH** provider on top of it ([`scieloorg/oai-pmh`](https://github.com/scieloorg/oai-pmh)). Tested directly during this research:

- `GET https://articlemeta.scielo.org/api/v1/collection/`, `/journal/`, `/article/identifiers/`, and `/article/?collection=scl&code=...` all returned **HTTP 200** with real JSON, no API key or registration.
- Returns **metadata only** (title, authors, full abstract, DOI, dates, keywords) -- never the article's full text.
- Legacy ISIS/CDS-style format (tags like `v12`=title, `v83`=abstract, `v10`=authors) rather than named fields -- SciELO itself publishes a Python library, `xylose`, to translate this; there's no JS/TS equivalent, and no MCP wrapper does this translation today.
- **This explains, and fixes for discovery/metadata, the 403 problem observed in the Cowork test**: tested directly in this research, `https://www.scielo.br/j/rae/a/8gWWSDpsktKM4jHfDpKCGKp/` (the article's HTML reader page) returned **403 with and without a browser User-Agent** -- that's bot protection on the reader-facing site (`www.scielo.br`), not an auth/key issue. `articlemeta.scielo.org` is a separate JSON API without that protection, and answered 200 consistently. **But it does not solve full-text extraction**: the same URL with `?format=pdf` also came back 403 -- the metadata API gives you the abstract, not the PDF or full text.

**Decision**: no MCP server was added to `.mcp.json` for SciELO -- no candidate found clears the bar (maintainer with a track record, published package, clean dependencies). The Article Meta API is real, public, keyless, and actively maintained, but returns metadata only in a legacy format that needs a translation layer -- documenting it as a direct HTTP call inside `core/literature-review` (for Portuguese-language literature discovery/triage, not full-text reading) is reasonable skill-level work, not a generic connector. A dedicated MCP wrapper (translating the `vNN` tag fields, possibly composing with OAI-PMH) would be a good candidate to build later -- nothing like that exists today.

## Candidates (researched, not yet integrated)

Verify license, maintenance, and exact command before adding to `.mcp.json` -- the same rigor applied to forks in `vendor/PROVENANCE.md`.

| Connector | Why it matters for Seer | Research status |
|---|---|---|
| Zotero (reference management) | Citation/bibliography -- composes with `core/citation-analysis` and `core/academic-writing` | Prior research (`GPT_academic-skills.md`) mapped integration skills/projects, but no specific MCP server verified yet |
| SciELO (Portuguese-language academic literature) | Addresses the language-coverage bias `core/literature-review` already documents as a known limitation | Researched (2026-08-21) -- see section above. No trustworthy MCP server found; SciELO's own Article Meta API (metadata, keyless) documented for skills to call directly, no MCP wrapper for now. |
| INPE (remote sensing / environmental data) | Primary source for `geography/physical-geography` and `geography/gis` in a Brazil context | Researched (2026-08-21) -- see section above. No trustworthy MCP server found; direct API (WFS/CSV) documented for skills to use directly, no MCP wrapper for now. |

## Rule

No connector goes into `.mcp.json` without real verification (license, exact install command, whether it needs an API key) -- a broken connector is worse than no connector, because it fails silently on a non-technical researcher.
