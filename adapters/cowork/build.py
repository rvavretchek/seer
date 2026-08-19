"""Regenerate adapters/cowork/skills/ -- the flattened, committed copy of skills/
that the Seer plugin actually ships.

Source of truth stays skills/<domain>/<skill-name>/SKILL.md (nested, for the
orchestrator's own Glob-based discovery -- see skills/orchestrator/SKILL.md).
The Claude Code / Cowork plugin loader's documented behaviour scans a single
level (skills/<skill-name>/SKILL.md) under the plugin root, so this script
flattens on generation. Unlike a build artifact, this output IS committed:
the root .claude-plugin/marketplace.json points "Add marketplace" at this
repository directly, and Claude Code clones real files -- it does not run
this script for you. Re-run this after any change under skills/ and commit
the result.

Usage: uv run --no-project python adapters/cowork/build.py
"""

import shutil
from pathlib import Path

ADAPTER_ROOT = Path(__file__).parent
REPO_ROOT = ADAPTER_ROOT.parent.parent
SKILLS_SRC = REPO_ROOT / "skills"
SKILLS_OUT = ADAPTER_ROOT / "skills"


def main() -> None:
    if SKILLS_OUT.exists():
        shutil.rmtree(SKILLS_OUT)
    SKILLS_OUT.mkdir(parents=True)

    seen: dict[str, Path] = {}
    skipped = []
    for skill_md in sorted(SKILLS_SRC.glob("**/SKILL.md")):
        skill_dir = skill_md.parent
        skill_name = skill_dir.name
        if skill_name in seen:
            skipped.append((skill_name, skill_dir, seen[skill_name]))
            continue
        seen[skill_name] = skill_dir
        shutil.copytree(skill_dir, SKILLS_OUT / skill_name)

    print(f"Regenerated {len(seen)} skills into {SKILLS_OUT}")
    if skipped:
        print("WARNING -- name collisions, second occurrence skipped:")
        for name, dupe, kept in skipped:
            print(f"  {name}: kept {kept}, skipped {dupe}")
    print("\nCommit adapters/cowork/skills/ after running this.")


if __name__ == "__main__":
    main()
