# Adaptador — Claude Cowork

Plugin fino que empacota `skills/` (orquestrador + CORE + pacotes disciplinares) como um plugin do Claude Cowork. Cobre o fluxo de uso real de Sônia: 100% conversacional, sem terminal — o "cara da TI" instala o plugin uma vez, ela só conversa.

**Status:** funcional, testado de ponta a ponta de verdade (não só validação de manifesto). `claude plugin marketplace add ./` + `claude plugin install seer@seer` funcionaram no repositório real: 23 skills carregadas, o conector OpenAlex reconhecido. Testado e desfeito (`marketplace remove`) — não deixamos o registro de teste no ambiente.

## Como funciona

Cowork usa **o mesmo formato de plugin do Claude Code** — confirmado na documentação oficial: manifesto JSON + pastas convencionais (`skills/`, `.mcp.json`), sem código, sem passo de build no plugin em si.

Duas peças, na raiz do repositório e aqui:

- **`.claude-plugin/marketplace.json`** (raiz do repo) — permite `Add marketplace` direto do GitHub (`rvavretchek/seer`) de dentro do Cowork ou do Claude Code. Aponta pra este diretório (`./adapters/cowork`) como o plugin.
- **`adapters/cowork/`** — o plugin em si: manifesto, `.mcp.json`, e `skills/`.

### Por que `skills/` está duplicado aqui (decisão corrigida)

Primeira tentativa: gerar `skills/` num `dist/` ignorado pelo git, montado por `build.py`. **Não funciona pro fluxo real** — quando alguém faz `Add marketplace` a partir do GitHub, o Cowork/Claude Code **clona o repositório e lê os arquivos como estão**; ele não roda nenhum script nosso. Se `skills/` só existisse depois de um build local, o plugin instalado por qualquer outra pessoa viria vazio.

Por isso `adapters/cowork/skills/` é uma cópia **achatada e commitada** de `skills/<domínio>/<skill>/` (a fonte da verdade continua na raiz, organizada por domínio para o `Glob` do orquestrador). `build.py` regenera essa cópia — rode e commite depois de qualquer mudança em `skills/`.

## Testar localmente

```bash
uv run --no-project python adapters/cowork/build.py   # regenera adapters/cowork/skills/ a partir de skills/
claude plugin validate adapters/cowork --strict
claude plugin marketplace add ./                       # a partir da raiz do repo
claude plugin install seer@seer
claude plugin details seer@seer                        # confere skills, conectores, custo em tokens
claude plugin marketplace remove seer                   # desfaz o teste
```

Todos os comandos acima já rodaram de verdade nesta sessão — não é hipotético.

## Conectores

Ver [`CONNECTORS.md`](CONNECTORS.md) — apenas conectores reais e verificados entram em `.mcp.json` (mesmo rigor de `vendor/PROVENANCE.md`). Hoje: OpenAlex. Candidatos documentados: IBGE/SIDRA, Zotero, SciELO, INPE.

### Configurar a chave da OpenAlex (Windows)

Desde 13/fev/2026 a OpenAlex exige chave — sem ela, o limite é 100 créditos/dia (estoura em poucas buscas). Ver a seção "Causa raiz" em `CONNECTORS.md`.

1. Crie uma conta grátis em [openalex.org](https://openalex.org) e pegue sua chave em `openalex.org/settings/api`.
2. Defina a variável de ambiente **de forma permanente** (não basta `$env:` numa janela só — o Cowork é um app separado, não herda de um terminal aberto). No PowerShell:
   ```powershell
   setx OPENALEX_API_KEY "sua-chave-aqui"
   ```
3. **Feche e reabra o Claude Desktop/Cowork** — apps já abertos não pegam variável de ambiente nova até reiniciar.
4. Reteste o Teste 3 do roteiro (`tests/manual/cowork-rc1-test-script.md`) — se a busca no OpenAlex retornar sem erro 429, a chave está funcionando.

`adapters/cowork/.mcp.json` já referencia `${OPENALEX_API_KEY}` — a chave nunca fica no repositório, só na sua máquina.

## O que falta pra publicação real

- Testar dentro do app Cowork de verdade (`Add marketplace` com `rvavretchek/seer`, ou upload do plugin como arquivo) — o que validamos até aqui foi via `claude` CLI, que usa o mesmo mecanismo, mas não é o app Cowork em si.
- Pesquisar e verificar os conectores candidatos antes de adicioná-los.
- Decidir se `adapters/cowork/skills/` fica commitado pra sempre (atual) ou se vale a pena, no futuro, um hook de CI que regenera e falha se estiver desatualizado.

---

# Adapter — Claude Cowork (English / en-US)

Thin plugin that packages `skills/` (orchestrator + CORE + discipline packs) as a Claude Cowork plugin. Covers Sônia's real usage flow: fully conversational, no terminal — the "IT person" installs the plugin once, she just talks.

**Status:** functional, tested end to end for real (not just manifest validation). `claude plugin marketplace add ./` + `claude plugin install seer@seer` worked against the real repository: 23 skills loaded, the OpenAlex connector recognized. Tested and torn down (`marketplace remove`) -- we didn't leave the test registration in the environment.

## How it works

Cowork uses **the same plugin format as Claude Code** -- confirmed in the official documentation: a JSON manifest plus conventional folders (`skills/`, `.mcp.json`), no code, no build step for the plugin itself.

Two pieces, at the repo root and here:

- **`.claude-plugin/marketplace.json`** (repo root) -- enables `Add marketplace` directly from GitHub (`rvavretchek/seer`) inside Cowork or Claude Code. Points at this directory (`./adapters/cowork`) as the plugin.
- **`adapters/cowork/`** -- the plugin itself: manifest, `.mcp.json`, and `skills/`.

### Why `skills/` is duplicated here (a corrected decision)

First attempt: generate `skills/` into a gitignored `dist/`, assembled by `build.py`. **Doesn't work for the real flow** -- when someone runs `Add marketplace` from GitHub, Cowork/Claude Code **clones the repository and reads the files as they are**; it doesn't run any script of ours. If `skills/` only existed after a local build, the plugin anyone else installed would arrive empty.

So `adapters/cowork/skills/` is a **flattened, committed** copy of `skills/<domain>/<skill>/` (the source of truth stays at the repo root, organized by domain for the orchestrator's `Glob`). `build.py` regenerates that copy -- run and commit it after any change under `skills/`.

## Test locally

```bash
uv run --no-project python adapters/cowork/build.py   # regenerates adapters/cowork/skills/ from skills/
claude plugin validate adapters/cowork --strict
claude plugin marketplace add ./                       # from the repo root
claude plugin install seer@seer
claude plugin details seer@seer                        # check skills, connectors, token cost
claude plugin marketplace remove seer                   # tear down the test
```

Every command above actually ran in this session -- not hypothetical.

## Connectors

See [`CONNECTORS.md`](CONNECTORS.md) -- only real, verified connectors go into `.mcp.json` (the same rigor as `vendor/PROVENANCE.md`). Today: OpenAlex. Documented candidates: IBGE/SIDRA, Zotero, SciELO, INPE.

### Configuring the OpenAlex key (Windows)

Since 2026-02-13 OpenAlex requires a key -- without one, the limit is 100 credits/day (exhausted within a few searches). See the "Root cause" section in `CONNECTORS.md`.

1. Create a free account at [openalex.org](https://openalex.org) and get your key at `openalex.org/settings/api`.
2. Set the environment variable **permanently** (a one-off `$env:` in a single window isn't enough -- Cowork is a separate app, it doesn't inherit from an open terminal). In PowerShell:
   ```powershell
   setx OPENALEX_API_KEY "your-key-here"
   ```
3. **Close and reopen Claude Desktop/Cowork** -- apps already open don't pick up a new environment variable until restarted.
4. Re-run Test 3 from the script (`tests/manual/cowork-rc1-test-script.md`) -- if the OpenAlex search comes back without a 429, the key is working.

`adapters/cowork/.mcp.json` already references `${OPENALEX_API_KEY}` -- the key never lives in the repository, only on your machine.

## What's left before real publication

- Testing inside the actual Cowork app (`Add marketplace` with `rvavretchek/seer`, or uploading the plugin as a file) -- what we've verified so far is via the `claude` CLI, which uses the same mechanism, but isn't the Cowork app itself.
- Researching and verifying the candidate connectors before adding them.
- Deciding whether `adapters/cowork/skills/` stays committed forever (current) or eventually gets a CI check that regenerates and fails if it's stale.
