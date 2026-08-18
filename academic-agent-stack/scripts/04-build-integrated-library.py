from pathlib import Path
import json,shutil,argparse
ROOT=Path(__file__).resolve().parents[1]; L=ROOT/"library"; D=ROOT/"dist"; O=ROOT/"skills"/"orchestrator"
p=argparse.ArgumentParser(); p.add_argument("--clean",action="store_true"); a=p.parse_args()
if a.clean and D.exists(): shutil.rmtree(D)
(D/"skills").mkdir(parents=True,exist_ok=True)
if not L.exists(): raise SystemExit("Execute 02-organize-skills.py primeiro.")
for x in L.iterdir():
    if x.is_dir(): shutil.copytree(x,D/"skills"/x.name,dirs_exist_ok=True)
shutil.copytree(O,D/"skills"/"academic-research-orchestrator",dirs_exist_ok=True)
m=json.loads((L/"manifest.json").read_text(encoding="utf-8"))
out={"version":1,"type":"integrated-academic-agent-library","skill_count":len(m["skills"])+1,"orchestrator":"academic-research-orchestrator","skills":m["skills"]}
(D/"library-manifest.json").write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding="utf-8")
(D/"INSTALL.md").write_text("""# Integrated Academic Agent Library

`skills/` é a distribuição integrada.

Recomendação: publicar esta distribuição em um repositório GitHub próprio,
mantendo `vendor/` como upstream e o manifest para rastreabilidade. Não edite
manual e diretamente as cópias upstream.
""",encoding="utf-8")
print("Distribuição criada:",D,"| skills:",out["skill_count"])
