# Adaptador — Claude Cowork

Plugin fino que empacota `skills/` (orquestrador + CORE + pacotes disciplinares) como um plugin do Claude Cowork. Cobre o fluxo de uso real de Sônia: 100% conversacional, sem terminal — o "cara da TI" instala o plugin uma vez, ela só conversa.

**Status:** funcional e validado. Manifesto (`.claude-plugin/plugin.json`), conector real (`OpenAlex` via `.mcp.json`) e script de montagem (`build.py`) no lugar. `claude plugin validate` passa limpo, inclusive com `--strict`.

## Como funciona

Cowork usa **o mesmo formato de plugin do Claude Code** — confirmado na documentação oficial: manifesto JSON + pastas convencionais (`skills/`, `.mcp.json`), sem código, sem passo de build no plugin em si. `skills/` deste repositório já nasceu nesse formato (contrato do Seer = camada portável Agent Skills + extensão acadêmica), então o adaptador não reescreve nada — só empacota.

A única complicação real: nosso `skills/` é organizado por `<domínio>/<skill>/` (pra descoberta do orquestrador via `Glob`), mas o exemplo oficial de plugin usa um nível só (`skills/<skill>/`). `build.py` achata a estrutura na montagem — a fonte da verdade continua sendo `skills/` na raiz do repo, nunca editada aqui.

## Montar e testar localmente

```bash
uv run --no-project python adapters/cowork/build.py
claude plugin validate adapters/cowork/dist/seer --strict
claude --plugin-dir adapters/cowork/dist/seer
```

`dist/` é gerado e ignorado pelo git (`.gitignore`) — nunca editar diretamente, sempre regenerar com `build.py`.

## Conectores

Ver [`CONNECTORS.md`](CONNECTORS.md) — apenas conectores reais e verificados entram em `.mcp.json` (mesmo rigor de `vendor/PROVENANCE.md`). Hoje: OpenAlex. Candidatos documentados: IBGE/SIDRA, Zotero, SciELO, INPE.

## O que falta pra publicação real

- Testar dentro do Cowork de verdade (só validamos via `claude plugin validate` e a estrutura documentada — nunca rodou dentro do app Cowork em si).
- Pesquisar e verificar os conectores candidatos antes de adicioná-los.
- Decidir estratégia de distribuição: marketplace próprio, ou instalação direta via `claude.com/plugins` / `--plugin-dir` de um `.zip`.

---

# Adapter — Claude Cowork (English / en-US)

Thin plugin that packages `skills/` (orchestrator + CORE + discipline packs) as a Claude Cowork plugin. Covers Sônia's real usage flow: fully conversational, no terminal — the "IT person" installs the plugin once, she just talks.

**Status:** functional and validated. Manifest (`.claude-plugin/plugin.json`), a real connector (`OpenAlex` via `.mcp.json`), and an assembly script (`build.py`) are in place. `claude plugin validate` passes clean, including with `--strict`.

## How it works

Cowork uses **the same plugin format as Claude Code** -- confirmed in the official documentation: a JSON manifest plus conventional folders (`skills/`, `.mcp.json`), no code, no build step for the plugin itself. This repo's `skills/` was already born in that format (Seer's contract = the portable Agent Skills layer + academic extension), so the adapter rewrites nothing -- it just packages.

The one real complication: our `skills/` is organized as `<domain>/<skill>/` (for the orchestrator's `Glob`-based discovery), but the official plugin example uses a single level (`skills/<skill>/`). `build.py` flattens on assembly -- the source of truth stays `skills/` at the repo root, never edited here.

## Build and test locally

```bash
uv run --no-project python adapters/cowork/build.py
claude plugin validate adapters/cowork/dist/seer --strict
claude --plugin-dir adapters/cowork/dist/seer
```

`dist/` is generated and gitignored -- never edit it directly, always regenerate with `build.py`.

## Connectors

See [`CONNECTORS.md`](CONNECTORS.md) -- only real, verified connectors go into `.mcp.json` (the same rigor as `vendor/PROVENANCE.md`). Today: OpenAlex. Documented candidates: IBGE/SIDRA, Zotero, SciELO, INPE.

## What's left before real publication

- Testing inside the actual Cowork app (so far only verified via `claude plugin validate` and the documented structure -- never run inside Cowork itself).
- Researching and verifying the candidate connectors before adding them.
- Deciding a distribution strategy: a dedicated marketplace, or direct install via `claude.com/plugins` / a `--plugin-dir` `.zip`.
