# Academic Research Agent Stack

Stack agêntica para pesquisa acadêmica, inicialmente orientada a Geografia,
Educação/Pedagogia, Geopolítica, Geoeconomia, História e Geologia.

## Execução

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\01-download-libraries.ps1
.\scripts\02-organize-skills.ps1
.\scripts\03-create-orchestrator.ps1
.\scripts\04-build-integrated-library.ps1
```

Use `--include-large` no primeiro script para baixar também o repositório grande
de skills de pesquisa empírica.

## Arquitetura

- `vendor/`: repositórios upstream, preservando proveniência.
- `library/`: catálogo normalizado das SKILL.md encontradas.
- `skills/orchestrator/`: skill própria.
- `dist/`: biblioteca integrada publicável.
- `config/`: fontes e regras de roteamento.

A recomendação é publicar `dist/`/`skills/` em um repositório GitHub próprio,
mas manter os upstreams como dependências rastreadas, não como cópias sem origem.
