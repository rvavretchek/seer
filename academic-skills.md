	Hoje utilizo skills agênticas para desenvolvimento de software e não vejo como trabalhar sem elas. Minha cunhada é escritora e pesquisadora da área de educação, com foco em geografia. Há skills agênticos similares aos de desenvolvimento, porém focados em áreas pertinentes da área acadêmica, com focos em pedagogia, geografia, geopolítica, geologia, geoeconomia, história etc.?


Sim — e a analogia com skills agênticas de desenvolvimento é bastante boa. A diferença é que o ecossistema acadêmico está menos maduro: já existem skills genéricas muito boas para pesquisa, revisão e produção acadêmica, mas ainda há relativamente poucas skills especializadas em Geografia, Geopolítica, Geologia, Educação etc..

O que encontrei indica que já é perfeitamente viável montar para sua cunhada algo muito próximo de um "Academic Agent Stack", inclusive usando skills existentes como base.

1. O equivalente acadêmico mais próximo das skills de desenvolvimento

Existem hoje conjuntos de skills que cobrem praticamente o ciclo:

pergunta → exploração → pesquisa bibliográfica → análise → síntese → escrita → revisão → auditoria

Por exemplo, o projeto AI4S Skills possui skills separadas para:

- `research-explorer` — exploração inicial do tema;
- `literature-survey` — revisão bibliográfica;
- `experiment-suite` — desenho e execução de experimentos;
- `paper-writer` — produção do artigo;
- `integrity-auditor` — auditoria de evidências, números, figuras e lógica;
- `mindmap-render` — estruturação visual do conhecimento.


E possui um ai4s-agent que encadeia essas etapas. É explicitamente projetado para funcionar com Claude Code, Cursor, Codex e Aider. 

[AI4S Skills — GitHub](https://github.com/ai4s-research/ai4s-skills?utm_source=chatgpt.com)

Isso é bastante próximo da filosofia que você já utiliza no desenvolvimento: não pedir ao LLM para "fazer uma coisa", mas dar-lhe um conjunto de capacidades operacionais especializadas que podem ser orquestradas.


---

2. Para Humanidades e Ciências Sociais, já existem skills melhores que o "AI for Science"

Há uma skill particularmente interessante chamada Academic Research Agent Skill, que cobre:

- definição do escopo;
- revisão bibliográfica;
- planejamento da pesquisa;
- verificação de novidade;
- formalização;
- planejamento de experimentos;
- simulação de revisão por pares;
- verificação de afirmações;
- análise das fontes.


Ela também foi concebida para Claude/Codex/Gemini e agentes locais. 

[Academic Research Agent Skill — GitHub](https://github.com/ngtiendong/Academic-Research-Agent-Skill?utm_source=chatgpt.com)

Para o caso da sua cunhada, essa família de skills é provavelmente mais interessante que uma simples "skill de escrever artigos".


---

3. O ponto realmente interessante: transformar isso em "skills de disciplina"

Aqui está a diferença que eu faria.

Em desenvolvimento de software, você tem algo como:

software-engineer
    ├── architecture
    ├── backend
    ├── frontend
    ├── database
    ├── testing
    ├── security
    └── devops

Para uma pesquisadora de Geografia, poderia existir:

academic-researcher
    │
    ├── research-methodology
    ├── literature-review
    ├── source-verification
    ├── academic-writing
    ├── peer-review
    │
    └── geography
          ├── physical-geography
          ├── human-geography
          ├── cartography
          ├── gis
          ├── geospatial-analysis
          ├── regional-geography
          ├── urban-geography
          ├── economic-geography
          ├── political-geography
          └── environmental-geography

E, a partir daí:

political-geography
    ├── geopolitics
    ├── territorial-analysis
    ├── borders
    ├── international-relations
    ├── strategic-studies
    └── geopolitical-analysis

economic-geography
    ├── geoeconomics
    ├── trade
    ├── supply-chains
    ├── infrastructure
    ├── energy
    └── development

earth-sciences
    ├── geology
    ├── geomorphology
    ├── climatology
    ├── hydrology
    └── environmental-science

education
    ├── pedagogy
    ├── didactics
    ├── curriculum
    ├── educational-policy
    ├── learning-theories
    └── assessment

Essa camada disciplinar é justamente a que ainda vejo menos pronta no ecossistema de skills.


---

4. E existe uma skill fundamental para ela: Literature Review

Há várias implementações maduras.

A literature-review do K-Dense, por exemplo, propõe pesquisa sistemática em múltiplas bases, síntese temática, verificação das citações e geração de documentação reproduzível. 

[Scientific Agent Skills — GitHub](https://github.com/K-Dense-AI/scientific-agent-skills?utm_source=chatgpt.com)

Outra implementação interessante é a ai-skill-scholar, baseada no OpenAlex, que fornece:

- busca acadêmica;
- busca por autores/temas/periódicos;
- grafo de citações;
- referências;
- artigos que citam determinado trabalho;
- revisão bibliográfica em duas passagens.


E não exige API key. 

[AI Skill Scholar — GitHub](https://github.com/dsebastien/ai-skill-scholar?utm_source=chatgpt.com)

Para uma pesquisadora, isso é muito mais importante do que simplesmente ter um agente "que escreve bem".


---

5. Há também uma skill que eu considero particularmente adequada ao trabalho acadêmico

O projeto agent-papers-cli separa explicitamente:

research-coordinator
deep-research
literature-review
fact-check

Ou seja, já existe uma concepção de agente coordenador, em vez de simplesmente um chatbot acadêmico. 

[Agent Papers CLI — GitHub](https://github.com/collaborative-deep-research/agent-papers-cli?utm_source=chatgpt.com)

Isso permite algo como:

                ┌────────────────────┐
                │ Research Coordinator│
                └─────────┬──────────┘
                          │
           ┌────────────────┼────────────────┐
           ▼                ▼                ▼
     Deep Research   Literature Review   Fact Check
           │                │                │
           └────────────────┼────────────────┘
                          ▼
                    Academic Writer
                          │
                          ▼
                    Peer Reviewer
                          │
                          ▼
                    Integrity Auditor

Isso já começa a ficar muito parecido com uma equipe virtual de pesquisa.


---

6. Para sua cunhada, eu iria além: criaria um "Geography Research Agent"

E aqui acho que há uma oportunidade muito interessante.

Em vez de procurar uma única "skill de Geografia", eu montaria uma arquitetura composta:

Camada A — competências acadêmicas

research-coordinator
literature-review
deep-research
source-verification
citation-manager
academic-writing
peer-review
fact-check
research-integrity

Camada B — disciplinas

geography
pedagogy
history
geopolitics
geoeconomics
geology
cartography
environmental-science
political-science
economics

Camada C — ferramentas

OpenAlex
Crossref
DOI
Google Scholar
Zotero
World Bank
UN
UNESCO
OECD
IBGE
IPEA
CAPES
SciELO
DataSUS
INPE
Map/OSM

Camada D — métodos

systematic-review
scoping-review
PRISMA
qualitative-analysis
quantitative-analysis
case-study
comparative-analysis
historical-analysis
spatial-analysis
GIS-analysis
statistical-analysis
content-analysis
discourse-analysis

E aí o agente poderia decidir quais competências utilizar.

Por exemplo:

> "Investigue a transformação da fronteira agrícola brasileira entre 1970 e 2025 e suas implicações educacionais."



O coordenador poderia decompor:

research question
       │
       ├── historical analysis
       ├── geography
       ├── agricultural economics
       ├── geopolitics
       ├── education
       ├── spatial analysis
       └── literature review
              │
              ▼
       evidence synthesis
              │
              ▼
       academic paper


---

7. E há uma diferença crucial em relação ao desenvolvimento

Eu não faria uma skill "Geografia" gigantesca.

Faria algo semelhante ao que você vem fazendo em arquitetura de software: skills pequenas, composáveis e especializadas.

Por exemplo:

geography/
├── geographic-research
├── spatial-analysis
├── gis
├── cartography
├── human-geography
├── physical-geography
├── political-geography
├── economic-geography
└── regional-analysis

geopolitics/
├── geopolitical-analysis
├── territorial-analysis
├── border-analysis
├── strategic-analysis
└── international-relations

education/
├── educational-research
├── pedagogy
├── didactics
├── curriculum-analysis
├── educational-policy
└── learning-theory

Cada skill teria instruções, ontologias, métodos, fontes preferenciais, critérios de evidência, vieses conhecidos e ferramentas específicas.

Isso é muito mais poderoso do que simplesmente escrever no prompt:

> "Você é um especialista em Geografia."




---

8. E isso já está começando a aparecer na própria literatura

A área de agentes para educação está crescendo rapidamente. Uma revisão sistemática publicada em 2026 analisou 33 estudos empíricos sobre GenAI agents em educação e encontrou aplicações nos níveis macro, meso e micro da educação. 

Ou seja: não estamos mais falando apenas de "usar ChatGPT para estudar".

Estamos começando a falar de agentes especializados em:

- pesquisa;
- ensino;
- avaliação;
- planejamento;
- descoberta de conhecimento;
- síntese de literatura;
- assistência à produção científica.


---

## Minha avaliação

Eu separaria a situação atual em três níveis:

| Nível                                                                     | Situação em 2026                                          |
| ------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Skills agênticas para pesquisa acadêmica**                              | 🟢 Já existem e estão bastante boas                       |
| **Skills especializadas por disciplina**                                  | 🟡 Existem algumas, mas o ecossistema ainda é fragmentado |
| **"Ecossistema de agentes" completo para Geografia/Educação/Geopolítica** | 🟠 Ainda não existe algo dominante/pronto                 |
| **Construir esse ecossistema a partir das skills existentes**             | 🟢 **Totalmente viável**                                  |


E, particularmente para o perfil que você descreveu, eu não procuraria simplesmente uma "skill de Geografia" pronta.

Eu montaria uma espécie de "Academic Engineering Stack" para Humanidades e Ciências Sociais, reutilizando as skills acadêmicas existentes e adicionando uma camada disciplinar própria.

Isso permitiria inclusive que sua cunhada tivesse algo muito semelhante ao que você tem hoje no desenvolvimento: um conjunto de especialistas agênticos que trabalham sobre o mesmo workspace, compartilham fontes, artefatos, bibliografia, hipóteses e resultados, mas cada um possui um papel metodológico específico.

Se quiser levar isso adiante, o próximo passo mais interessante seria  e, em seguida, mapear quais skills acadêmicas open-source já existem hoje, identificando o que pode ser instalado pronto e o que valeria a pena desenvolver.desenhar uma árvore de skills específica para Geografia + Educação + Geopolítica + História + Geoeconomia


	Se você conseguir fazer isso, pode fazer


Sim. Fiz um levantamento mais direcionado e o resultado é bem melhor do que a minha resposta anterior sugeria. Há hoje um conjunto suficientemente grande de skills para montar um ambiente de pesquisa agêntica bastante sofisticado para ela — e, principalmente, encontrei uma biblioteca de Educação com 165 skills, além de uma biblioteca de pesquisa empírica em Ciências Sociais com milhares de skills e agentes especificamente geoespaciais.

O ponto importante é: não existe um único pacote "Geography Research Agent" maduro que resolva tudo, mas já existe praticamente todo o material para montar um.

1. O mapa que eu montaria

Eu estruturaria o ambiente em 6 camadas:
                   ┌──────────────────────────┐
                   │   ESEARCH ORCHESTRATOR  │
                   └────────────┬─────────────┘
                               │
          ┌──────────────────────┼──────────────────────┐
          │                                        │                                        │
          ▼                                      ▼                                       ▼
   PESQUISA ACADÊMICA       METODOLOGIA                    PRODUÇÃO
          │                                        │                                        │
   literature-review                       qualitative                    academic-writing
   source-discovery                      quantitative                          citation
   citation-analysis                    causal-inference                   peer-review
   fact-checking                          spatial-analysis                  publication
          │                                        │                                        │
          └──────────────────────┼──────────────────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼                        ▼                        ▼
             GEOGRAFIA        EDUCAÇÃO          HISTÓRIA
                  │                        │                         │
                GIS              pedagogia       historiografia
               cartografia       didática        análise documental
               geografia         currículo       temporalidade
               humana            avaliação       fontes primárias
                física            políticas                  etc.
                  │
        ┌─────────┼─────────────┐
        ▼              ▼                       ▼
   GEOPOLÍTICA GEOECONOMIA  GEOLOGIA


E uma sétima camada transversal:

                    EVIDENCE & PROVENANCE
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       fontes           citações         evidências
       primárias        DOI              datasets
       secundárias      bibliografia     mapas

Essa última é fundamental. Para uma pesquisadora, eu não trataria o agente como "escritor"; trataria como sistema de produção de conhecimento com rastreabilidade.


---

2. O achado mais importante: Education Agent Skills

Encontrei algo muito próximo exatamente do que você perguntou:

Education Agent Skills, de Gareth Manning.

É uma biblioteca open source com 165 skills pedagógicas, distribuídas em 20 domínios, explicitamente construída para agentes e compatível com Claude Code, Codex e outros agentes que implementam Agent Skills. 

[Education Agent Skills — GitHub](https://github.com/GarethManning/education-agent-skills?utm_source=chatgpt.com)

Isso muda bastante a avaliação anterior.

Ela já possui coisas como:

- learning science;
- curriculum design;
- assessment;
- instructional design;
- teacher development;
- pedagogical strategies;
- learning theory;
- educational planning;
- student-facing interaction;
- etc.

E há uma característica que considero especialmente boa: as skills são evidence-based, com pesquisas/autores associados e indicação da força da evidência. O projeto inclusive documenta abordagens que deliberadamente não incorpora por falta de evidência, como learning styles/VAK. 

Portanto:

Pedagogia/Educação: 🟢 existe uma base excelente pronta.

Não começaria do zero.


---

3. Para pesquisa acadêmica geral, há uma segunda camada muito madura

O Academic Research Agent Skill cobre o ciclo:

scoping
   ↓
literature review
   ↓
research planning
   ↓
novelty checking
   ↓
formalization
   ↓
experiment/research planning
   ↓
reviewer simulation
   ↓
claim verification

E explicitamente foi projetado para agentes como Claude Code, Codex e outros. 

[Academic Research Agent Skill — GitHub](https://github.com/ngtiendong/Academic-Research-Agent-Skill?utm_source=chatgpt.com)

Eu o colocaria como núcleo metodológico, não como skill de uma disciplina específica.


---

4. Há ainda um catálogo gigantesco de pesquisa em Ciências Sociais

Aqui está outro achado importante.

O projeto Awesome Agent Skills for Empirical Research, mantido pelo ecossistema Stanford REAP/CoPaper, cataloga atualmente 119 repositórios e mais de 23.000 skills, abrangendo oito áreas de Ciências Sociais. 

[Awesome Agent Skills for Empirical Research — GitHub](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research?utm_source=chatgpt.com)

Entre as áreas estão:

- Economics
- Political Science
- Sociology
- Psychology
- Public Health
- Education
- Management
- Finance
- Public Policy

E existem skills para:

- desenho de pesquisa;
- causal inference;
- econometria;
- análise quantitativa;
- análise qualitativa;
- R;
- Python;
- Stata;
- Bayesian analysis;
- pesquisa documental;
- revisão;
- escrita;
- replicabilidade;
- etc.


Isso cobre uma parte enorme de:

Geopolítica + Geoeconomia + Educação + Política Pública + Geografia Humana.


---

5. Geografia é onde a coisa fica realmente interessante

Aqui encontrei algo muito mais específico.

GeoAgent

O GeoAgent, do OpenGeoHub, é uma camada agêntica para ferramentas geoespaciais, incluindo:

- Python geospatial;
- mapas;
- QGIS;
- Leafmap;
- STAC;
- NASA Earthdata;
- análise geoespacial;
- visualização;
- operações sobre dados geográficos.


Ele permite inclusive conectar um agente diretamente a uma sessão QGIS. 

[GeoAgent — GitHub](https://github.com/opengeos/GeoAgent?utm_source=chatgpt.com)

Isso é particularmente interessante para sua cunhada porque deixa de ser apenas:

> "Leia sobre geografia."



e passa a ser:

> "Analise este território."



Por exemplo:

"Compare a expansão urbana de X entre 2000 e 2025."

       ↓

agente

       ↓

dados geoespaciais
       +
imagens
       +
camadas GIS
       +
estatística espacial

       ↓

mapas
       +
tabelas
       +
interpretação


---

6. GISclaw é outro projeto que merece atenção

Encontrei também o GISclaw, um sistema open source de agente LLM para análise geoespacial completa.

Ele possui:

- toolbox com 28 operações;
- execução de operações GIS;
- projetos persistentes;
- journal/log;
- replay;
- memória;
- skills;
- análise multimodal;
- interface web.


O interessante é que ele não é simplesmente um chatbot sobre GIS: o agente realmente executa operações sobre os dados. 

[GISclaw — GitHub](https://github.com/geumjin99/GISclaw?utm_source=chatgpt.com)


---

7. E existe OpenEarthAgent

O OpenEarthAgent é ainda mais interessante conceitualmente.

Ele combina:

LLM
 +
percepção
 +
GIS
 +
sensoriamento remoto
 +
operações espectrais
 +
GeoTIFF
 +
raciocínio espacial

e utiliza um registro de ferramentas que permite ao agente decompor uma tarefa geoespacial em várias operações. 

[OpenEarthAgent — GitHub](https://github.com/mbzuai-oryx/OpenEarthAgent?utm_source=chatgpt.com)

Para Geografia Física, Meio Ambiente, Sensoriamento Remoto e análise territorial, isso é muito relevante.


---

8. O problema de "Geografia" pode então ser decomposto

Em vez de procurar uma única skill:

geography

eu faria:

GEOGRAPHY
│
├── Human Geography
│   ├── population
│   ├── migration
│   ├── urban geography
│   ├── rural geography
│   ├── cultural geography
│   └── economic geography
│
├── Physical Geography
│   ├── geomorphology
│   ├── climatology
│   ├── hydrology
│   ├── biogeography
│   └── environmental geography
│
├── Geospatial
│   ├── GIS
│   ├── cartography
│   ├── spatial statistics
│   ├── remote sensing
│   ├── satellite imagery
│   └── geospatial databases
│
└── Regional
    ├── Brazil
    ├── Latin America
    ├── Amazon
    ├── urban regions
    └── comparative regions

E cada ramo poderia utilizar skills/ferramentas diferentes.


---

9. Para Geopolítica, eu não criaria uma "skill de geopolítica" única

Aqui há uma sutileza importante.

Geopolítica é interdisciplinar.

Eu montaria:

GEOPOLITICS
│
├── Political Geography
│
├── International Relations
│
├── History
│
├── Strategic Studies
│
├── Economics
│
├── Geoeconomics
│
├── Energy
│
├── Trade
│
├── Infrastructure
│
├── Demography
│
├── Military Geography
│
└── Territorial Analysis

E criaria uma skill geopolitical-analysis que orquestra as anteriores.

Assim, por exemplo:

> "Analise a importância geopolítica do corredor bioceânico para o Brasil."



não seria respondido por uma única skill.

O agente poderia acionar:

geopolitical-analysis
       │
       ├── political-geography
       ├── economic-geography
       ├── geoeconomics
       ├── infrastructure
       ├── international-relations
       ├── Brazil
       └── historical-analysis

Isso é muito mais próximo de como um pesquisador humano realmente trabalha.


---

10. Para História, a situação é semelhante

Não encontrei uma biblioteca de Agent Skills de História comparável às 165 skills de Educação.

Então eu classificaria:

História: 🟡 infraestrutura disponível, mas especialização ainda precisa ser construída.

Eu criaria:

history/
├── historiography
├── primary-source-analysis
├── secondary-source-analysis
├── archival-research
├── chronology
├── historical-context
├── comparative-history
├── periodization
├── historical-geography
├── oral-history
└── source-criticism

E particularmente:

source-criticism

deveria ser uma skill obrigatória.

Ela deveria perguntar:

Quem produziu?
Quando?
Onde?
Para quem?
Com qual finalidade?
Qual era o contexto?
Qual evidência sustenta?
Qual evidência contradiz?
Qual é a cadeia de transmissão?
Qual é a interpretação historiográfica?

Isso evita que o agente trate uma fonte histórica como simplesmente mais uma página da web.


---

11. Geologia: também não encontrei um equivalente acadêmico tão pronto

Aqui eu classificaria:

Geologia: 🟡/🟠 — boa infraestrutura científica, pouca especialização como Agent Skill.

Mas há um ponto favorável: a biblioteca científica da K-Dense, por exemplo, já possui 147 skills científicas, incluindo geospatial science e acesso a dezenas de bases científicas. 

Então eu faria:

geology/
├── physical-geology
├── structural-geology
├── geomorphology
├── sedimentology
├── mineralogy
├── petrology
├── tectonics
├── stratigraphy
├── geochemistry
├── hydrogeology
└── geological-mapping

e conectaria isso à camada geoespacial.


---

12. A camada de bibliografia é muito importante

Aqui também já existem soluções excelentes.

O ai-skill-scholar oferece:

- pesquisa no OpenAlex;
- autores;
- periódicos;
- citações;
- referências;
- trabalhos que citam determinado artigo;
- revisão bibliográfica em duas passagens;
- sem API key;
- implementação simples em Python.


[AI Skill Scholar — GitHub](https://github.com/dsebastien/ai-skill-scholar?utm_source=chatgpt.com)

E encontrei uma skill específica de Zotero que permite ao agente:

- pesquisar a biblioteca;
- recuperar referências;
- fazer busca semântica;
- analisar PDFs;
- gerar citações;
- inserir referências em DOCX.


[Zotero Agent Skill — GitHub](https://github.com/drguptavivek/zotero-use?utm_source=chatgpt.com)

Eu consideraria Zotero quase obrigatório para esse ambiente.


---

13. OpenAlex deveria ser uma das fontes básicas

Também encontrei o projeto ondata/skills, que disponibiliza uma skill openalex específica para pesquisa acadêmica. Ela consulta trabalhos, autores e recupera PDFs quando disponíveis. 

[onData Skills — GitHub](https://github.com/ondata/skills?utm_source=chatgpt.com)

Então o agente poderia fazer:

Pergunta
   ↓
OpenAlex
   ↓
Crossref
   ↓
Zotero
   ↓
fontes institucionais
   ↓
bases específicas
   ↓
triagem
   ↓
leitura
   ↓
síntese


---

14. Eu montaria o ambiente dela assim

Minha recomendação concreta seria:

ACADEMIC RESEARCH ENVIRONMENT
│
├── 01 — CORE RESEARCH
│   ├── research-coordinator
│   ├── deep-research
│   ├── literature-review
│   ├── source-verification
│   ├── claim-verification
│   ├── citation-analysis
│   └── research-integrity
│
├── 02 — ACADEMIC PRODUCTION
│   ├── academic-writing
│   ├── outline
│   ├── citation-management
│   ├── peer-review
│   ├── reviewer-simulation
│   └── publication-check
│
├── 03 — EDUCATION
│   └── Education Agent Skills
│       ├── pedagogy
│       ├── learning-science
│       ├── curriculum
│       ├── assessment
│       ├── instructional-design
│       └── educational-policy
│
├── 04 — GEOGRAPHY
│   ├── human-geography
│   ├── physical-geography
│   ├── economic-geography
│   ├── political-geography
│   ├── regional-geography
│   ├── GIS
│   ├── cartography
│   ├── spatial-analysis
│   └── remote-sensing
│
├── 05 — GEOPOLITICS
│   ├── geopolitical-analysis
│   ├── international-relations
│   ├── territorial-analysis
│   ├── strategic-studies
│   ├── geoeconomics
│   ├── energy-geopolitics
│   └── infrastructure-geopolitics
│
├── 06 — HISTORY
│   ├── historiography
│   ├── primary-source-analysis
│   ├── source-criticism
│   ├── historical-analysis
│   └── historical-geography
│
├── 07 — GEOLOGY
│   ├── geology
│   ├── geomorphology
│   ├── tectonics
│   ├── hydrology
│   ├── geological-mapping
│   └── environmental-geology
│
└── 08 — DATA & SOURCES
    ├── Zotero
    ├── OpenAlex
    ├── Crossref
    ├── GIS/QGIS
    ├── OpenStreetMap
    ├── remote sensing
    ├── statistical analysis
    └── government/open data


---

15. O que eu instalaria pronto vs. desenvolveria

Essa é provavelmente a parte mais útil da pesquisa.

| Área                    | Situação     | Estratégia                       |
| ----------------------- | ------------ | -------------------------------- |
| Pesquisa acadêmica      | 🟢 Muito boa | **Instalar**                     |
| Literature review       | 🟢 Muito boa | **Instalar**                     |
| Bibliografia            | 🟢 Muito boa | **Zotero + OpenAlex**            |
| Educação/Pedagogia      | 🟢 Excelente | **Education Agent Skills**       |
| Ciências Sociais        | 🟢 Excelente | **AERS + seleção de skills**     |
| GIS                     | 🟢 Muito boa | **GeoAgent/GISclaw**             |
| Sensoriamento remoto    | 🟢 Boa       | **OpenEarthAgent + ferramentas** |
| Geografia humana        | 🟡           | Compor                           |
| Geografia física        | 🟡           | Compor                           |
| Geopolítica             | 🟡           | **Criar camada orquestradora**   |
| Geoeconomia             | 🟡           | Compor economia + geografia      |
| História                | 🟡           | Criar skills metodológicas       |
| Historiografia          | 🟡           | Criar                            |
| Geologia                | 🟡           | Compor ciência + geoespacial     |
| Cartografia             | 🟢           | Ferramentas GIS existentes       |
| Análise espacial        | 🟢           | GeoAgent/GIS                     |
| Escrita acadêmica       | 🟢           | Instalar                         |
| Peer review             | 🟢           | Instalar                         |
| Auditoria de evidências | 🟢           | Instalar/criar                   |

---

16. E eu faria uma distinção fundamental: Skill ≠ Knowledge

Esse ponto é especialmente importante para o projeto.

Uma skill:

geopolitical-analysis

não deveria conter todo o conhecimento sobre geopolítica.

Ela deveria conter:

OBJETIVO
MÉTODO
ETAPAS
FONTES PREFERENCIAIS
CRITÉRIOS DE EVIDÊNCIA
VIESES
PERGUNTAS DE CONTROLE
FERRAMENTAS
FORMATO DOS ARTEFATOS

O conhecimento deveria vir de:

livros
papers
documentos
bases de dados
mapas
datasets
fontes primárias
fontes governamentais

Isso permite atualizar o conhecimento sem reescrever a skill.


---

17. E existe uma arquitetura ainda melhor para ela

Eu não faria apenas:

LLM → skills → resposta

Faria:

                    PESQUISADORA
                         │
                         ▼
                ┌─────────────────┐
                │   COORDENADOR   │
                │   DE PESQUISA   │
                └────────┬────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      Research       Discipline       Methods
       Agent           Agents          Agents
          │              │              │
          ▼              ▼              ▼
     ┌────────┐    ┌────────────┐   ┌──────────┐
     │Sources │    │ Geography  │   │Qualitative│
     │Papers  │    │ Education  │   │Quantitative│
     │Books   │    │ History    │   │Spatial    │
     └────────┘    │ Geopolitics│   │Statistical│
                   │ Geology    │   └──────────┘
                   └────────────┘
                         │
                         ▼
                 EVIDENCE GRAPH
                         │
                         ▼
                 SYNTHESIS AGENT
                         │
                         ▼
                 WRITING AGENT
                         │
                         ▼
                REVIEWER / AUDITOR

Isso é muito mais interessante que "ChatGPT para pesquisadores".

É uma infraestrutura de pesquisa agêntica.


---

18. Minha conclusão depois do levantamento

Eu corrigiria minha resposta anterior desta forma:

> Sim, já existe hoje massa crítica suficiente para montar um equivalente acadêmico das skills agênticas de desenvolvimento — e, para Educação, o ecossistema já está surpreendentemente maduro.



O que ainda falta não é tecnologia. É principalmente composição e especialização disciplinar.

E para o caso específico que você descreveu, eu faria um pacote próprio, mas não começaria escrevendo 50 skills.

Começaria aproximadamente com 15–20 skills, reutilizando o que já está pronto:

CORE
1. research-coordinator
2. deep-research
3. literature-review
4. source-verification
5. claim-verification
6. citation-analysis
7. academic-writing
8. peer-review

KNOWLEDGE
9. geography-research
10. geopolitical-analysis
11. historical-analysis
12. educational-research
13. geoeconomic-analysis

METHODS
14. qualitative-analysis
15. quantitative-analysis
16. spatial-analysis
17. source-criticism

TOOLS
18. zotero
19. openalex
20. qgis/geospatial-analysis

E só depois expandiria cada domínio.

O resultado seria algo muito próximo de um "Codex/Claude Code para pesquisadores de Geografia, Educação e Ciências Humanas", no sentido arquitetural — não um novo LLM, mas um conjunto de agentes/skills especializados que sabem pesquisar, localizar evidências, analisar fontes, trabalhar com dados espaciais, confrontar hipóteses, escrever e auditar o próprio trabalho.

Há inclusive uma razão forte para preservar o humano no centro: a literatura recente sobre agentes em educação ainda caracteriza o campo como fragmentado e em evolução, enquanto os próprios projetos de skills enfatizam que as skills devem ampliar o pesquisador, não substituir seu julgamento. 

Se a intenção for realmente montar isso para sua cunhada, eu partiria agora para a etapa seguinte: fazer um inventário dos repositórios, selecionar as skills concretas que valem a pena instalar, eliminar redundâncias/inseguras, definir as ~20 skills próprias e entregar uma estrutura de diretórios pronta para Claude Code/Codex, com SKILL.md, dependências e ordem de instalação. Isso já seria, na prática, o projeto de uma Academic Research Agent Stack especializada em Geografia + Educação.


	Crie um script em PowerShell para:

	1. Baixar as bibliotecas de skills necessárias para essa abordagem que você sugeriu por último


	2. Organizar os skills da forma que você colocou


	3. Criar um skill capaz de identificar as especializações necessárias e orquestrar todas para atingir o objetivo



	Pode ser um ou mais scripts, desde que numerados na ordem para fazer isso acontecer. Pode ser em Python, que acho que automatiza melhor.

	Se puder ter uma 4 função, seria criar um instalador que integra as bibliotecas como uma grande biblioteca integrada (se for o caso, me informe e crio um projeto no GitHub para tornar essa nova biblioteca pública e trato isso no VS Code ou no PyCharm com Codex).

Retomei de onde havia parado e gerei o pacote inicial completo, com os quatro estágios.

Download

Baixar Academic Agent Stack — pacote inicial (.zip)

O que foi criado

academic-agent-stack/
├── README.md
├── config/
│   ├── sources.json
│   └── routing.json
├── scripts/
│   ├── 01-download-libraries.py
│   ├── 01-download-libraries.ps1
│   ├── 02-organize-skills.py
│   ├── 02-organize-skills.ps1
│   ├── 03-create-orchestrator.py
│   ├── 03-create-orchestrator.ps1
│   ├── 04-build-integrated-library.py
│   └── 04-build-integrated-library.ps1
└── skills/
    └── orchestrator/
        └── SKILL.md

Execução

No Windows, depois de descompactar:

Set-ExecutionPolicy -Scope Process Bypass

.\scripts\01-download-libraries.ps1
.\scripts\02-organize-skills.ps1
.\scripts\03-create-orchestrator.ps1
.\scripts\04-build-integrated-library.ps1

Para incluir também a biblioteca grande de pesquisa empírica:

.\scripts\01-download-libraries.ps1 -IncludeLarge

Ou tudo diretamente em Python:

python .\scripts\01-download-libraries.py
python .\scripts\02-organize-skills.py
python .\scripts\03-create-orchestrator.py
python .\scripts\04-build-integrated-library.py

O quarto estágio é importante

Eu recomendo criar o projeto GitHub próprio, sim.

Mas não faria um "fork gigante" simplesmente copiando tudo. A arquitetura que coloquei no pacote separa:

vendor/
    upstream repositories

library/
    catálogo normalizado

skills/
    skills próprias

dist/
    distribuição integrada

Isso permite transformar o projeto em algo como:

Academic Research Agent Skills

com proveniência explícita de cada skill e possibilidade de atualizar os upstreams sem perder as customizações.

O orquestrador

A skill criada em:

skills/orchestrator/SKILL.md

não é uma simples skill de "pesquisa". Ela funciona como meta-skill:

objetivo da pesquisadora
        │
        ▼
identificação das subperguntas
        │
        ▼
identificação das disciplinas
        │
        ▼
identificação dos métodos
        │
        ▼
seleção das skills disponíveis
        │
        ▼
seleção das fontes
        │
        ▼
execução/delegação
        │
        ▼
síntese
        │
        ▼
auditoria epistemológica
        │
        ▼
resultado

Ou seja, se ela disser:

> "Quero pesquisar os impactos geopolíticos, econômicos e educacionais da expansão dos corredores bioceânicos brasileiros."



o orquestrador deve descobrir que provavelmente precisará combinar Geografia, Geopolítica, Geoeconomia, infraestrutura, História, Educação, análise documental, análise espacial e pesquisa bibliográfica, em vez de simplesmente escolher uma skill chamada geopolitics.


---

Uma ressalva importante

Este primeiro pacote é um bootstrapper, não ainda a versão final da biblioteca. Ele baixa os upstreams e procura SKILL.md recursivamente, mas não deve ainda ser considerado um resolvedor perfeito de dependências entre skills.

Eu faria a próxima versão com:

1. manifesto de cada skill;
2. detecção de dependências;
3. controle de versões;
4. classificação automática por LLM;
5. deduplicação semântica;
6. matriz de compatibilidade entre skills;
7. avaliação de qualidade;
8. academic-research-orchestrator capaz de consultar o catálogo;
9. testes de skills;
10. instalação específica para Codex + VS Code;
11. eventualmente adaptadores para Claude Code/Cursor.

Isso transformaria o projeto de um simples agregador de repositórios em uma biblioteca agêntica acadêmica propriamente dita.

E, dado o que você propôs, eu recomendo tratar isso como um projeto GitHub próprio e desenvolver a segunda etapa no VS Code/PyCharm com Codex, exatamente como você sugeriu. O GitHub deve ser a camada de governança/proveniência, enquanto vendor/ continua apontando para os projetos originais. ❶



	Como configurar o repositório para desenvolver?



Para esse projeto, eu recomendo configurar o repositório como um produto de software, não como um simples repositório de prompts/skills. A separação entre upstream, skills próprias, catálogo, testes e distribuição será importante desde o início.

1. Estrutura que eu recomendo

Eu evoluiria a estrutura inicial para:

academic-agent-skills/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── pyproject.toml
├── .gitignore
│
├── .github/
│   ├── workflows/
│   │   ├── validate.yml
│   │   └── build.yml
│   └── ISSUE_TEMPLATE/
│
├── config/
│   ├── sources.yaml
│   ├── routing.yaml
│   └── taxonomy.yaml
│
├── scripts/
│   ├── 01-download-libraries.py
│   ├── 02-organize-skills.py
│   ├── 03-create-orchestrator.py
│   └── 04-build-integrated-library.py
│
├── src/
│   └── academic_agent/
│       ├── __init__.py
│       ├── catalog.py
│       ├── discovery.py
│       ├── classifier.py
│       ├── resolver.py
│       ├── orchestrator.py
│       └── provenance.py
│
├── skills/
│   │
│   ├── core/
│   │   ├── research/
│   │   ├── literature-review/
│   │   ├── source-verification/
│   │   ├── claim-verification/
│   │   ├── citation-analysis/
│   │   ├── academic-writing/
│   │   └── peer-review/
│   │
│   ├── education/
│   │   ├── educational-research/
│   │   ├── pedagogy/
│   │   ├── didactics/
│   │   ├── curriculum/
│   │   └── assessment/
│   │
│   ├── geography/
│   │   ├── human-geography/
│   │   ├── physical-geography/
│   │   ├── economic-geography/
│   │   ├── political-geography/
│   │   ├── gis/
│   │   ├── cartography/
│   │   └── spatial-analysis/
│   │
│   ├── geopolitics/
│   │   ├── geopolitical-analysis/
│   │   ├── territorial-analysis/
│   │   ├── strategic-analysis/
│   │   └── international-relations/
│   │
│   ├── geoeconomics/
│   │   ├── geoeconomic-analysis/
│   │   ├── trade/
│   │   ├── infrastructure/
│   │   └── energy/
│   │
│   ├── history/
│   │   ├── historical-analysis/
│   │   ├── historiography/
│   │   ├── primary-source-analysis/
│   │   └── source-criticism/
│   │
│   └── geology/
│       ├── geology/
│       ├── geomorphology/
│       ├── tectonics/
│       └── geological-mapping/
│
├── vendor/
│   └── ... upstreams ...
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── skills/
│   └── fixtures/
│
├── docs/
│   ├── architecture/
│   ├── taxonomy/
│   ├── skills/
│   └── development/
│
└── dist/
    └── .gitkeep

A diferença fundamental em relação ao pacote que gerei antes é a introdução de:

src/
tests/
docs/

Isso permite transformar o projeto em uma biblioteca de software propriamente dita.


---

2. Eu usaria Python como linguagem principal

Aqui concordo com você: Python é melhor para esse projeto.

Não porque as skills sejam Python, mas porque o motor de gerenciamento delas pode fazer coisas como:

Git
 ↓
download
 ↓
parse SKILL.md
 ↓
metadata extraction
 ↓
classification
 ↓
dependency resolution
 ↓
semantic deduplication
 ↓
catalog
 ↓
validation
 ↓
build

Python é muito adequado para isso.

Eu criaria o projeto como pacote Python moderno:

pyproject.toml

e não usaria requirements.txt como mecanismo principal.


---

3. Criaria o repositório no GitHub primeiro

No GitHub:

New repository

Nome que eu sugiro:

academic-agent-skills

ou, se quiser deixar mais explícito:

academic-research-agent-skills

Eu prefiro:

> academic-agent-skills



porque futuramente o projeto pode abranger não apenas research, mas também ensino, análise, produção acadêmica etc.

Descrição:

> Modular agent skills for academic research, education, geography, geopolitics, history, geoeconomics and related disciplines.



Eu deixaria Public.


---

4. Clone no Windows

No PowerShell:

cd C:\Projetos
git clone https://github.com/SEU_USUARIO/academic-agent-skills.git
cd academic-agent-skills

Depois copie o conteúdo do ZIP que gerei para dentro do repositório.

Ou, melhor ainda, posso fazer uma segunda versão do pacote já com a estrutura GitHub que proponho acima.


---

5. Criar ambiente Python

No diretório do projeto:

py -3.12 -m venv .venv

Ative:

.\.venv\Scripts\Activate.ps1

Atualize:

python -m pip install --upgrade pip

Para desenvolvimento:

pip install -e ".[dev]"


---

6. O pyproject.toml

Eu usaria algo nessa linha:

[project]
name = "academic-agent-skills"
version = "0.1.0"
description = "Modular agent skills for academic research and interdisciplinary knowledge work"
requires-python = ">=3.11"
dependencies = [
    "pyyaml>=6.0",
    "pydantic>=2.0",
    "rich>=13.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=5.0",
    "ruff>=0.8",
    "mypy>=1.10",
]

[project.scripts]
academic-agent = "academic_agent.cli:main"

[build-system]
requires = ["setuptools>=70"]
build-backend = "setuptools.build_meta"

Eu não colocaria dependências de LLM ainda.

Primeiro construiria o framework agnóstico.

Depois poderemos ter adaptadores:

LLM Provider
├── OpenAI
├── Anthropic
├── Google
└── Local


---

7. O princípio arquitetural mais importante

Eu evitaria fazer o projeto depender diretamente do Codex.

A arquitetura deveria ser:

Academic Agent Skills
                          │
             ┌────────────┴────────────┐
             │                         │
        Skill System              Skill Runtime
             │                         │
       SKILL.md + metadata       orchestration
             │                         │
             └────────────┬────────────┘
                          │
                    Agent Adapter
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            Codex       Claude       Outro

Assim, o projeto não fica preso a um fornecedor.


---

8. SKILL.md deve ser tratado como uma interface

Esse ponto é crucial.

Eu estabeleceria um contrato próprio.

Por exemplo:

---
name: geopolitical-analysis
version: 0.1.0
category: geopolitics
type: analytical
status: experimental

description: >
  Performs structured geopolitical analysis...

requires:
  - research
  - source-verification

recommends:
  - geography
  - history
  - geoeconomics

tools:
  - web
  - bibliography

outputs:
  - analytical-report
  - evidence-matrix
---

Depois:

# Geopolitical Analysis

## Purpose

...

## Inputs

...

## Procedure

...

## Evidence Requirements

...

## Quality Criteria

...

## Failure Modes

...

## Output

...

Isso permite que o nosso orquestrador descubra automaticamente o que precisa chamar.


---

9. A taxonomia deve virar um artefato formal

Não deixaria a classificação somente no código Python.

Criaria:

config/taxonomy.yaml

Por exemplo:

domains:

  research:
    description: Academic research methodology

  education:
    description: Education and pedagogy

  geography:
    description: Geographic sciences

    subdomains:
      - human-geography
      - physical-geography
      - economic-geography
      - political-geography
      - gis
      - cartography
      - spatial-analysis

  geopolitics:
    subdomains:
      - geopolitical-analysis
      - territorial-analysis
      - strategic-analysis

  geoeconomics:
    subdomains:
      - trade
      - infrastructure
      - energy

  history:
    subdomains:
      - historiography
      - historical-analysis
      - primary-source-analysis

  geology:
    subdomains:
      - geomorphology
      - tectonics
      - stratigraphy

Isso é muito melhor porque futuramente o classificador poderá utilizar esse arquivo.


---

10. O catálogo será o "cérebro estrutural"

O projeto deveria gerar algo como:

catalog.json

com:

{
  "name": "geopolitical-analysis",
  "version": "0.1.0",
  "source": "academic-agent-skills",
  "domains": [
    "geopolitics",
    "geography",
    "international-relations"
  ],
  "requires": [
    "research",
    "source-verification"
  ],
  "recommends": [
    "history",
    "geoeconomics"
  ],
  "tools": [
    "web",
    "openalex"
  ]
}

Então o orquestrador poderá raciocinar sobre skills como componentes, e não simplesmente procurar arquivos.


---

11. O GitHub Actions deve validar tudo

Eu colocaria pelo menos:

Pull Request
     │
     ▼
validate
     │
     ├── YAML válido?
     ├── SKILL.md válido?
     ├── nomes válidos?
     ├── dependências resolvidas?
     ├── referências válidas?
     └── testes Python
             │
             ▼
           BUILD
             │
             ▼
       dist artifact

Isso é especialmente importante porque eventualmente outras pessoas poderão contribuir com skills.


---

12. E eu criaria testes de skills

Não apenas testes Python.

Por exemplo:

tests/skills/geopolitical-analysis/
├── basic.yaml
├── multidisciplinary.yaml
├── insufficient-evidence.yaml
└── conflicting-sources.yaml

Um caso poderia ser:

objective: >
  Analyze the geopolitical implications of a new transoceanic corridor.

expected_domains:
  - geography
  - geopolitics
  - geoeconomics
  - infrastructure

expected_methods:
  - historical-analysis
  - comparative-analysis

must_require:
  - source-verification

Isso permite testar se o orquestrador está selecionando as disciplinas certas.

E isso é uma diferença enorme entre uma coleção de prompts e uma verdadeira plataforma de skills.


---

13. Como eu trabalharia no VS Code + Codex

Eu faria:

VS Code
   │
   ├── Git
   │
   ├── Python
   │
   ├── .venv
   │
   └── Codex
          │
          ├── arquitetura
          ├── implementação
          ├── testes
          ├── revisão
          └── documentação

E o Codex teria como regra:

> Nunca alterar vendor/ diretamente.



Alterações próprias ficam em:

skills/
src/
tests/
config/
docs/


---

14. O fluxo de desenvolvimento

Eu adotaria:

Issue
  ↓
design
  ↓
skill/feature
  ↓
implementation
  ↓
test
  ↓
validation
  ↓
PR
  ↓
GitHub Actions
  ↓
review
  ↓
merge
  ↓
release

Branches:

main
develop
feature/*
fix/*
skill/*

Para o início, main + feature/* já é suficiente. Não criaria complexidade desnecessária.


---

15. Uma decisão importante sobre vendor

Eu não faria commit de todas as bibliotecas upstream dentro do Git, especialmente a biblioteca grande de pesquisa empírica.

Manteria:

vendor/

no .gitignore.

O Git armazenaria:

sources:
  - repository: ...
    ref: ...
    version: ...
    checksum: ...

Assim:

GitHub
   │
   ├── nosso código
   ├── nossas skills
   ├── manifests
   └── versões dos upstreams
             │
             ▼
          vendor/

Isso evita transformar o repositório em um monstro e preserva a licença/proveniência dos projetos externos.


---

16. E sim: eu criaria um projeto público

Acho que há valor real em publicar isso.

Não como:

> "Mais uma coleção de prompts de IA."



Mas como:

> um framework open source para composição e orquestração de Agent Skills para pesquisa acadêmica interdisciplinar.



O diferencial seria:

Skill Registry + Taxonomy + Dependency Resolver + Research Orchestrator + Evidence/Provenance + Tests.

A parte de domínio poderia crescer depois:

v0.1
Research Core

v0.2
Education

v0.3
Geography

v0.4
Geopolitics + Geoeconomics

v0.5
History

v0.6
Geology

v1.0
Interdisciplinary Academic Research Platform

E eu manteria uma separação clara entre framework e skills. Isso permite que, no futuro, alguém possa instalar apenas:

academic-agent-skills
+
geography-pack

ou:

academic-agent-skills
+
education-pack

sem precisar instalar tudo.

Minha recomendação é não começar codificando o orquestrador ainda. Primeiro vale fechar o contrato SKILL.md + taxonomy + manifest + dependency model. Essas quatro coisas serão a "API" do projeto; se forem bem definidas, o orquestrador fica muito mais simples e o ecossistema pode crescer sem virar uma coleção desorganizada de prompts.