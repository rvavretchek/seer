# Pesquisa: viabilidade de um modo "agent-team" no Tabula Rasa (Cowork)

**Data:** 21/ago/2026. **Resumo:** não é viável hoje. O mecanismo real que o `agent-team` da BMad depende (`SendMessage`, times persistentes endereçáveis por nome) existe no Claude Code, mas é experimental, exige variável de ambiente, exige sessão **interativa de terminal**, e nunca aparece em `allowed-tools` de nenhuma skill deste repositório — porque não é algo que uma skill solicita, é injetado pelo harness só quando um time é criado numa sessão interativa. O modelo Cowork (GUI, sem terminal, per o próprio memlog deste projeto) não tem caminho pra satisfazer nenhuma dessas condições. Recomendação: **(b) — não construível agora com as ferramentas disponíveis pra uma skill de plugin**. Um workaround mais estreito (re-semear o histórico de cada persona a cada rodada) resolve só a autoconsistência de uma persona entre rodadas, não o mecanismo central do `agent-team` (personas se mensageando direto) — vale considerar separadamente, não como "agent-team levinho".

Revalidado de forma independente (busca própria, fora do agente que fez a pesquisa original) — achado bate: [Claude Code Docs, Agent Teams](https://code.claude.com/docs/en/agent-teams) confirma a flag `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, o par `SendMessage`/`ListAgents`, e que subagentes comuns "só reportam pro principal" enquanto agent-teams "compartilham achados e coordenam diretamente" — exatamente a diferença que bloqueia o Tabula Rasa hoje. Uma issue real (`anthropics/claude-code#56449`) mostra o recurso falhando mesmo com a flag ligada em "Claude Code on the web" — reforça que é frágil mesmo nas superfícies que ele oficialmente cobre, antes de chegar no Cowork.

---

# Research: is an "agent-team" mode feasible for Tabula Rasa (Cowork)?

**Date:** 2026-08-21. **Verdict:** not feasible today. Recommendation **(b)**.

## 1. What `Task`/`Agent` actually supports

`code.claude.com/docs/en/agent-sdk/subagents` (current as of this research): the tool was renamed `Task` → `Agent` in Claude Code v2.1.63 (`Task` still works as an alias -- what every skill in this repo declares). A real resume mechanism exists (`session_id` + `agentId`, a second `query()` call with `resume:`), **but it's driven by the SDK host application calling `query()` twice, not something the model can invoke mid-conversation as a tool call.** `anthropics/claude-code#11892` confirms the model's own system prompt still states: *"Each agent invocation is stateless. You will not be able to send additional messages to the agent, nor will the agent be able to communicate with you outside of its final report."* This matches exactly what Tabula Rasa's `subagent` mode already assumes.

## 2. The real gate: agent teams are experimental, interactive-only

`code.claude.com/docs/en/agent-teams`:

- **Disabled by default**: requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in `settings.json` or the environment. Without it, "no team is set up at session start... Claude does not spawn or propose teammates."
- **Interactive-only, explicitly excludes headless/SDK sessions**: "Spawning teammates also requires an interactive session. In non-interactive mode with the `-p` flag, including Agent SDK sessions, Claude doesn't spawn teammates."
- **`SendMessage` is harness-injected at teammate-spawn time**, not a tool a `SKILL.md`'s `allowed-tools:` line can request. Confirmed independently: it does not exist as a callable tool until the env var is set at the shell level before process init (`gh issue view 35240`: multiple reports of `Error: No such tool available: SendMessage` without the flag).
- **No nested teams**: "teammates cannot spawn their own teammates. Only the lead can manage the team." Even in the best case, a Tabula Rasa persona (a dispatched `Task`/`Agent` subagent) could never become a team lead itself.
- The UI concept (arrow-key agent panel, tmux/iTerm2 split panes, messaging a teammate directly) is a terminal concept end to end.

## 3. What a Cowork plugin skill can actually declare

Grepped every `allowed-tools:` line across every skill in this repo (69 files, `skills/*` and `adapters/cowork/skills/*`): the complete union is `Read, Write, Edit, Glob, Grep, Bash, Task`. Zero exceptions -- no skill anywhere, including `orchestrator` and `tabula-rasa` themselves, declares `Agent`, `SendMessage`, `ListAgents`, or any teammate-messaging tool. This matches the documented mechanism: `SendMessage` isn't requestable by a skill, it's injected under conditions (interactive session + experimental flag) a GUI plugin skill has no path to satisfy.

Cross-checked against this project's own earlier finding (party-mode memlog, 2026-08-19): "Cowork usa 'plugins' que empacotam skills+conectores+sub-agentes... sem terminal, GUI apenas, app precisa ficar aberto" -- no terminal, GUI-only. That alone independently rules this out, regardless of the env-var question: the feature's control surface doesn't exist in a chat GUI, and the docs state non-interactive/SDK-hosted sessions don't spawn teammates at all even with the flag set.

## 4. The transcript-reseeding workaround, assessed honestly

Buildable now, with existing tools (`Read`, `Glob`, `Write`, `Edit`, `Task`, no new tool needed): each round, re-invoke a fresh `Task` call per persona, seeded with that persona's own prior turns so it behaves as if it remembers its last round.

**Fixes:** round-to-round self-consistency for one persona (won't contradict or forget its own earlier position).

**Does not fix:**
- **No point-to-point messaging** -- two reseeded subagents still can't talk to each other mid-round; the orchestrating mind must still stage/weave every exchange, exactly as `subagent` mode already does. This is agent-team's *defining* feature, and reseeding doesn't approximate it at all.
- **No live user addressing** -- a researcher can't interrupt and address one standing persona directly across a multi-turn conversation the way agent-team's UI allows.
- **Real, compounding cost** -- each round re-sends that persona's skill procedure + voice + a growing transcript excerpt; bounded if the orchestrator excerpts rather than dumps, but still real added cost per round.
- **Silent state loss** -- anything a subagent "held in mind" but didn't say explicitly is gone next round; a genuinely resumed session doesn't have this gap.

**Verdict:** worth building as an honestly-scoped enhancement to `subagent` mode's per-persona consistency across reruns, *if* that specific problem (a persona forgetting its own prior stance across multiple invocations in one research session) turns out to matter in practice -- but it should never be marketed or designed as "agent-team lite." It fixes thread-memory, not the room-mechanics agent-team actually adds.

## Bottom line

- **(a) not realistic now.** The mechanism agent-team needs is real in Claude Code but experimental, env-var-gated, interactive-terminal-only, and structurally unrequestable from a plugin skill's `allowed-tools`.
- **(b) is the honest read, and this project's recommendation.** What's missing is specific and named -- not a vague "not supported yet."
- **(c) is a real, narrower fallback** worth scoping separately if it ever becomes a practical need, not as a substitute for (a).

Re-check this file if Cowork's runtime model changes, or if a future Claude Code release exposes agent-teams to non-interactive/SDK-hosted sessions -- both would change this verdict.
