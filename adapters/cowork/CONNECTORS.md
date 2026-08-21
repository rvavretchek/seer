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

## Candidatos (pesquisados, ainda não integrados)

Verificar licença, manutenção e comando exato antes de adicionar a `.mcp.json` — mesmo rigor aplicado aos forks em `vendor/PROVENANCE.md`.

| Conector | Por que importa pro Seer | Status da pesquisa |
|---|---|---|
| Zotero (gerenciamento de referências) | Citação/bibliografia — compõe com `core/citation-analysis` e `core/academic-writing` | Existência de skills/projetos de integração já mapeada em pesquisa anterior (`GPT_academic-skills.md`), mas nenhum MCP server específico verificado ainda |
| SciELO (literatura acadêmica em português) | Cobre o viés de idioma que `core/literature-review` já documenta como limitação conhecida | Não pesquisado ainda (tarefa separada) |
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

## Candidates (researched, not yet integrated)

Verify license, maintenance, and exact command before adding to `.mcp.json` -- the same rigor applied to forks in `vendor/PROVENANCE.md`.

| Connector | Why it matters for Seer | Research status |
|---|---|---|
| Zotero (reference management) | Citation/bibliography -- composes with `core/citation-analysis` and `core/academic-writing` | Prior research (`GPT_academic-skills.md`) mapped integration skills/projects, but no specific MCP server verified yet |
| SciELO (Portuguese-language academic literature) | Addresses the language-coverage bias `core/literature-review` already documents as a known limitation | Not researched yet (separate follow-up task) |
| INPE (remote sensing / environmental data) | Primary source for `geography/physical-geography` and `geography/gis` in a Brazil context | Researched (2026-08-21) -- see section above. No trustworthy MCP server found; direct API (WFS/CSV) documented for skills to use directly, no MCP wrapper for now. |

## Rule

No connector goes into `.mcp.json` without real verification (license, exact install command, whether it needs an API key) -- a broken connector is worse than no connector, because it fails silently on a non-technical researcher.
