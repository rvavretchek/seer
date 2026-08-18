# Constituição do Seer

> Princípios fundadores do projeto. Não é um guia de estilo — é o que não muda quando tudo o resto mudar. Toda decisão de design, toda skill aceita, todo adaptador construído deve ser avaliável contra estes princípios.

## 1. Skill ≠ Conhecimento

Uma skill descreve **método**: objetivo, procedimento, critérios de evidência, fontes preferenciais, vieses conhecidos, modos de falha, formato de saída. Uma skill **não** carrega o conteúdo do domínio dentro de si.

O conhecimento — o fato histórico, o dado do IBGE, o artigo científico — vem de fontes externas, buscadas em tempo de execução. Isso mantém as skills pequenas, revisáveis e atualizáveis sem reescrever nada quando o conhecimento do mundo muda.

## 2. Portabilidade por Desenho

O núcleo de skills do Seer é escrito num formato aberto e neutro de fornecedor. Nenhuma skill do núcleo é escrita contra a API, o formato de plugin ou as particularidades de um produto específico.

Superfícies de uso (Claude Cowork, ou o que vier depois — Manus, Gemini, ChatGPT) recebem **adaptadores finos**: camadas descartáveis e substituíveis. Se um adaptador precisar ser reescrito do zero, isso nunca deve exigir tocar no núcleo. Se tocar, o design falhou neste princípio.

## 3. Piso de Acessibilidade Zero-CLI

O produto precisa ser inteiramente utilizável por alguém que nunca abriu um terminal e nunca vai abrir. Essa é a régua mínima de qualquer funcionalidade voltada ao usuário final — não uma persona entre outras, um **piso**.

Isso não significa simplificar para o menor denominador comum: pesquisadores tecnicamente fluentes continuam livres para configurar, estender e operar o Seer diretamente. O piso não pode virar teto.

## 4. Composição, Não Coleção

O valor do Seer não está em ter muitas skills — está em um orquestrador capaz de decompor uma pergunta de pesquisa real em disciplinas, métodos e fontes, e compor as skills certas para respondê-la. Uma skill nova só se justifica se o orquestrador souber quando e como usá-la em conjunto com as demais.

## 5. Proveniência Explícita, Sempre

Toda ideia, estrutura ou trecho inspirado, copiado ou adaptado de qualquer projeto upstream — o BMAD Method incluído — é documentado com atribuição e licença, no próprio artefato onde aparece, não só num arquivo central esquecível.

O BMAD Method é licenciado sob MIT (copyright BMad Code, LLC, 2025). Isso autoriza reuso, modificação e redistribuição do código e do padrão arquitetural, com atribuição. **Isso não autoriza usar as marcas "BMad", "BMad Method" ou "BMad Core"** para nomear, descrever ou promover o Seer. O Seer é um produto inspirado, não um produto afiliado.

## 6. Julgamento Humano no Centro

Skills ampliam o pesquisador; não substituem o julgamento dele. Nenhuma skill do núcleo deve ser desenhada para produzir uma conclusão de pesquisa como verdade assumida — toda saída carrega evidência rastreável, e a decisão final sobre o que ela significa é de quem pesquisa.

## 7. Bilíngue por Padrão

Toda documentação pública do projeto — README, CONTRIBUTING, esta Constituição, briefs, specs — é publicada em Português do Brasil seguido da versão completa em inglês (en-US), no mesmo documento. Isso não é cortesia: é a condição para que a comunidade de pesquisa lusófona e a comunidade internacional de contribuidores técnicos consigam usar e mantar o mesmo projeto sem depender de tradução de terceiros.

## 8. MIT, Sem Meias-Palavras

O Seer é licenciado sob MIT. Toda skill contribuída ao núcleo precisa ser compatível com MIT ou explicitamente documentada quando isso não for possível (por exemplo, uma skill que depende de dado ou biblioteca sob outra licença deve declarar isso na própria skill).

---

*Uma mudança nesta Constituição é, por definição, uma mudança de identidade do projeto — não uma atualização de rotina. Deve ser proposta e debatida abertamente, nunca silenciosa.*

---

# Constitution (English / en-US)

> Founding principles of the project. This is not a style guide — it is what does not change when everything else does. Every design decision, every accepted skill, every adapter built should be evaluable against these principles.

## 1. Skill ≠ Knowledge

A skill describes **method**: objective, procedure, evidence criteria, preferred sources, known biases, failure modes, output format. A skill does **not** carry the domain's content within itself.

Knowledge — the historical fact, the IBGE dataset, the research paper — comes from external sources, fetched at run time. This keeps skills small, reviewable, and updatable without rewrites whenever real-world knowledge changes.

## 2. Portability by Design

Seer's skill core is written in an open, vendor-neutral format. No core skill is written against the API, plugin format, or quirks of a specific product.

Usage surfaces (Claude Cowork, or whatever comes next — Manus, Gemini, ChatGPT) get **thin adapters**: disposable, replaceable layers. If an adapter needs to be rewritten from scratch, that should never require touching the core. If it does, the design has failed this principle.

## 3. Zero-CLI Accessibility Floor

The product must be fully usable by someone who has never opened a terminal and never will. That is the minimum bar for any user-facing feature — not one persona among others, a **floor**.

This does not mean simplifying to the lowest common denominator: technically fluent researchers remain free to configure, extend, and operate Seer directly. The floor must never become a ceiling.

## 4. Composition, Not Collection

Seer's value is not in having many skills — it's in an orchestrator able to decompose a real research question into disciplines, methods, and sources, and compose the right skills to answer it. A new skill only earns its place if the orchestrator knows when and how to use it alongside the others.

## 5. Explicit Provenance, Always

Any idea, structure, or fragment inspired by, copied from, or adapted from any upstream project — the BMAD Method included — is documented with attribution and license, in the very artifact where it appears, not just in one forgettable central file.

The BMAD Method is MIT-licensed (copyright BMad Code, LLC, 2025). This permits reuse, modification, and redistribution of the code and the architectural pattern, with attribution. **It does not permit using the "BMad", "BMad Method", or "BMad Core" trademarks** to name, describe, or promote Seer. Seer is an inspired product, not an affiliated one.

## 6. Human Judgment at the Center

Skills amplify the researcher; they do not replace their judgment. No core skill should be designed to produce a research conclusion as assumed truth — every output carries traceable evidence, and the final call on what it means belongs to the person doing the research.

## 7. Bilingual by Default

All public project documentation — README, CONTRIBUTING, this Constitution, briefs, specs — is published in Brazilian Portuguese followed by the complete English (en-US) version, in the same document. This is not courtesy: it is the condition for both the Portuguese-speaking research community and the international community of technical contributors to use and maintain the same project without depending on third-party translation.

## 8. MIT, No Half-Measures

Seer is MIT-licensed. Every skill contributed to the core must be MIT-compatible or explicitly documented when that is not possible (for example, a skill that depends on data or a library under a different license must declare that within the skill itself).

---

*A change to this Constitution is, by definition, a change to the project's identity — not a routine update. It must be proposed and debated openly, never silently.*
