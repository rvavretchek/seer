from pathlib import Path
import argparse,json,shutil,subprocess
ROOT=Path(__file__).resolve().parents[1]
def run(c): print("+"," ".join(c)); subprocess.run(c,check=True)
p=argparse.ArgumentParser(); p.add_argument("--include-large",action="store_true"); p.add_argument("--force",action="store_true"); a=p.parse_args()
if shutil.which("git") is None: raise SystemExit("Git não encontrado no PATH.")
cfg=json.loads((ROOT/"config"/"sources.json").read_text(encoding="utf-8"))
for s in cfg["sources"]:
    if not s.get("enabled",True): print("[SKIP]",s["id"]); continue
    if s.get("large") and not a.include_large: print("[SKIP]",s["id"],"(use --include-large)"); continue
    d=ROOT/"vendor"/s["id"]; d.parent.mkdir(exist_ok=True)
    if (d/".git").exists():
        if a.force: run(["git","-C",str(d),"pull","--ff-only"])
        else: print("[OK]",s["id"],"já existe")
    else:
        if d.exists(): raise SystemExit(f"Destino já existe: {d}")
        run(["git","clone","--depth","1",s["repo"],str(d)])
print("Download concluído.")
