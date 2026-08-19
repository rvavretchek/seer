"""Assemble the installable/testable Seer plugin into adapters/cowork/dist/.

Source of truth stays skills/<domain>/<skill-name>/SKILL.md (nested, for the
orchestrator's own Glob-based discovery -- see skills/orchestrator/SKILL.md).
The Claude Code / Cowork plugin loader's documented example uses a single
level (skills/<skill-name>/SKILL.md); nesting depth beyond that isn't
confirmed to be supported, so this script flattens on assembly rather than
assuming it works nested. Never edit dist/ directly -- it is regenerated,
gitignored, and not the source of truth.

Usage: uv run --no-project python adapters/cowork/build.py
"""

import shutil
from pathlib import Path

ADAPTER_ROOT = Path(__file__).parent
REPO_ROOT = ADAPTER_ROOT.parent.parent
SKILLS_SRC = REPO_ROOT / "skills"
DIST = ADAPTER_ROOT / "dist" / "seer"


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    # Manifest and connectors, copied as-is.
    shutil.copytree(ADAPTER_ROOT / ".claude-plugin", DIST / ".claude-plugin")
    shutil.copy2(ADAPTER_ROOT / ".mcp.json", DIST / ".mcp.json")

    # Skills, flattened from skills/<domain>/<skill-name>/ to skills/<skill-name>/.
    dist_skills = DIST / "skills"
    dist_skills.mkdir()
    seen: dict[str, Path] = {}
    skipped = []
    for skill_md in sorted(SKILLS_SRC.glob("**/SKILL.md")):
        skill_dir = skill_md.parent
        skill_name = skill_dir.name
        if skill_name in seen:
            skipped.append((skill_name, skill_dir, seen[skill_name]))
            continue
        seen[skill_name] = skill_dir
        shutil.copytree(skill_dir, dist_skills / skill_name)

    print(f"Assembled {len(seen)} skills into {dist_skills}")
    if skipped:
        print("WARNING -- name collisions, second occurrence skipped:")
        for name, dupe, kept in skipped:
            print(f"  {name}: kept {kept}, skipped {dupe}")
    print(f"\nTest locally with:\n  claude --plugin-dir {DIST}")


if __name__ == "__main__":
    main()
