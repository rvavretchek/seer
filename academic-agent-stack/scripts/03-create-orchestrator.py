from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
T=ROOT/"skills"/"orchestrator"; T.mkdir(parents=True,exist_ok=True)
routing={"education":["education","pedagogy","didactics","curriculum","assessment"],
"geography":["geography","gis","geospatial","cartography","spatial"],
"geopolitics":["geopolitics","political-geography","international-relations","territorial"],
"geoeconomics":["geoeconomics","economic-geography","trade","energy","infrastructure"],
"history":["history","historiography","historical","source-criticism"],
"geology":["geology","geomorphology","tectonics","sedimentology","hydrogeology"],
"research":["research","literature-review","source-verification","fact-check"],
"bibliography":["zotero","openalex","citation","bibliography"],"writing":["academic-writing","paper","manuscript","peer-review"]}
(ROOT/"config"/"routing.json").write_text(json.dumps(routing,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("Orquestrador e regras de roteamento criados.")
