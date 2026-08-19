# Roteiro de teste manual — Seer v1.0.0-rc.1 no Cowork real

Testa os 5 pontos que ainda não tinham validação real (só via `claude` CLI), listados na sessão de design. Cada passo não-preparatório tem um critério de sucesso explícito — "deu certo se X, deu errado se Y".

## Passo 0 — Instalação (preparatório)

1. Abra o Claude Desktop → **Cowork**.
2. `Customize` (barra lateral) → `Plugins` → `Browse plugins` → `Add marketplace`.
3. Digite `rvavretchek/seer`.
4. Selecione o plugin **Seer** → `Install`.

**Checkpoint** (não é teste formal, mas confirme antes de seguir): a tela de detalhes do plugin deve mostrar **23 skills** e o conector **openalex-mcp-server** em MCP servers. Se esse número bater, a instalação replicou exatamente o que validamos via CLI — pode seguir. Se não bater, pare aqui e me chame antes de continuar.

---

## Teste 1 — Invocação automática por conversa

**O que testa:** se o Cowork escolhe a skill certa sozinho, a partir de uma pergunta em português comum — sem você saber (ou precisar saber) que existe uma skill por trás.

**Prompt:**
> Preciso de uma revisão bibliográfica sobre feedback gerado por IA em contextos educacionais.

**Depois da resposta, pergunte diretamente:**
> Internamente, qual skill instalada você usou para montar essa resposta?

**Critério de sucesso:** a resposta segue uma estrutura reconhecível de revisão sistemática (escopo → busca → triagem → leitura → síntese por tema, com referências) **E/OU**, quando perguntado, o Claude nomeia explicitamente `literature-review` (ou `core:literature-review`) como a skill usada.

**Falhou se:** a resposta é um parágrafo genérico sem estrutura de revisão, ou o Claude diz que não usou nenhuma skill instalada.

---

## Teste 2 — Orquestrador despachando dentro do Cowork

**O que testa:** se o mecanismo do orquestrador (decompor a pergunta, compor mais de uma skill, sintetizar) funciona de verdade dentro do Cowork — isso nunca foi testado fora do meu próprio ambiente.

**Prompt:**
> Analise como a queda da taxa de natalidade no Nordeste brasileiro pode afetar o planejamento educacional regional nos próximos 10 anos.

*(Escolhido de propósito por precisar de Geografia — demografia — e Educação — política educacional — juntas; nenhuma skill isolada cobre as duas pontas.)*

**Depois da resposta, pergunte:**
> Quais competências/skills você combinou para chegar nessa resposta?

**Critério de sucesso:** a resposta final é uma síntese coerente que trata **as duas dimensões** (demográfica e educacional) — não duas respostas coladas, uma resposta só. Quando perguntado, o Claude nomeia 2 ou mais skills reais do plugin (ex.: algo como `geographic-research`/`human-geography` + `educational-policy`).

**Falhou se:** a resposta cobre só uma dimensão, trava, ou o Claude não consegue nomear mais de uma skill usada. **Um "falhou" aqui também é uma resposta útil** — confirma a limitação que o próprio `orchestrator/SKILL.md` já assumia como não verificada.

---

## Teste 3 — Conector OpenAlex rodando de verdade

**O que testa:** se o servidor MCP registrado (`openalex-mcp-server`) realmente responde, não só aparece cadastrado.

**Prompt:**
> Busque no OpenAlex 3 artigos publicados entre 2023 e 2025 sobre "cognitive load theory" e me dê título, autores e ano de cada um.

**Verificação extra (faça você mesmo):** pegue um dos títulos retornados e procure no Google Scholar ou no próprio openalex.org. Ele precisa existir de verdade.

**Critério de sucesso:** o Claude retorna 3 referências específicas e verificáveis (título+autor+ano reais, conferidos por você em pelo menos 1 caso).

**Falhou se:** o Claude diz que não tem acesso a uma ferramenta de busca, ou retorna referências que não existem quando você checa.

---

## Teste 4 — Acesso a pasta ("Work in a folder")

**O que testa:** o mecanismo de permissão de arquivo do próprio Cowork (independente do plugin Seer, mas você pediu pra cobrir).

**Preparação:** crie uma pasta de teste em qualquer lugar do seu computador, com um arquivo `.txt` simples dentro (uma frase qualquer).

**Passos:**
1. Clique em "Work in a folder" (canto inferior esquerdo).
2. Selecione a pasta de teste → `Allow`.
3. Prompt: `Liste os arquivos dessa pasta e me diga o que tem dentro do arquivo [nome do arquivo].`

**Critério de sucesso:** o Claude lista o arquivo corretamente e cita o conteúdo real que você escreveu nele.

**Falhou se:** ele não enxerga a pasta, pede permissão de novo sem motivo, ou inventa o conteúdo do arquivo.

---

## Teste 5 — Interface do Cowork em si

Já coberto pelo checkpoint do Passo 0 — a tela de instalação/detalhes do plugin é a parte da interface que faltava ver funcionando de verdade. Se o Passo 0 bateu (23 skills, conector OpenAlex visível), este ponto está validado.

---

## Ao terminar

Me diga, pra cada teste (1 a 4): **passou / falhou**, e cole a resposta que o Claude deu quando você perguntou "qual skill você usou" — isso é o dado mais importante pra eu saber se o orquestrador está funcionando como projetado dentro do Cowork ou não.
