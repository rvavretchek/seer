from pathlib import Path
import json,re,shutil,hashlib
ROOT=Path(__file__).resolve().parents[1]; V=ROOT/"vendor"; L=ROOT/"library"
RULES={
"education":["education","pedag","didactic","curriculum","assessment","learning"],
"geography":["geograph","gis","geospatial","cartograph","spatial","remote-sensing"],
"geopolitics":["geopolit","territor","international-relations","strategic","border"],
"geoeconomics":["geoeconom","economic-geograph","trade","energy","infrastructure"],
"history":["histor","historiograph","primary-source","archiv","chronolog"],
"geology":["geolog","geomorph","tectonic","sediment","mineral","petrolog","stratigraph","hydrogeolog"],
"research":["research","literature","review","methodolog","citation","academic","peer-review","fact-check"],
"data":["data","statistic","quantitative","qualitative","analysis"],
"bibliography":["zotero","openalex","crossref","bibliograph","citation","doi"],
"writing":["writing","paper","manuscript","publication"]}
def slug(x): return re.sub("-+","-",re.sub(r"[^a-zA-Z0-9._-]+","-",x.lower())).strip("-") or "skill"
def classify(t):
    t=t.lower(); scores={d:sum(t.count(w) for w in ws) for d,ws in RULES.items()}
    return [d for d,n in sorted(scores.items(),key=lambda x:x[1],reverse=True) if n][:4] or ["research"]
if L.exists(): shutil.rmtree(L)
L.mkdir()
seen=set(); records=[]
for f in V.rglob("SKILL.md"):
    rel=f.relative_to(V); source=rel.parts[0]; raw=f.read_text(encoding="utf-8",errors="ignore")
    title=next((x[2:].strip() for x in raw.splitlines() if x.startswith("# ")),f.parent.name)
    base=slug(f.parent.name); key=base
    if key in seen: key=f"{slug(source)}-{base}"
    if key in seen: key=f"{key}-{hashlib.sha1(str(f).encode()).hexdigest()[:8]}"
    seen.add(key); d=L/key; d.mkdir()
    shutil.copy2(f,d/"SKILL.md")
    records.append({"id":key,"title":title,"source":source,"source_path":str(rel).replace("\\","/"),"domains":classify(title+"\n"+raw[:12000])})
(L/"manifest.json").write_text(json.dumps({"version":1,"skill_count":len(records),"skills":records},indent=2,ensure_ascii=False),encoding="utf-8")
print("Skills catalogadas:",len(records))
