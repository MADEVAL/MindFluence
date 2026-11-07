#!/usr/bin/env python3
"""Install the mindfluence skill into a local agent skills directory.

The repository is the source of truth. Installation copies a snapshot from
``skills/mindfluence/``; run the command again after editing the repo to refresh
the copy.

Usage:
    python install.py --target all
    python install.py --target claude
    python install.py --target opencode
    python install.py --target project
    python install.py --list
    python install.py --check
    python install.py --target project --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL_NAME = "mindfluence"
SOURCE = ROOT / "skills" / SKILL_NAME
PAYLOAD = [
    "SKILL.md",
    "references",
    "examples",
    "scenarios",
    "scripts",
    "agents",
]
IGNORE = shutil.ignore_patterns(
    "__pycache__",
    "*.pyc",
    ".git",
    ".gitignore",
    "*.egg-info",
)

TARGETS = {
    "claude": Path.home() / ".claude" / "skills" / SKILL_NAME,
    "opencode": Path.home() / ".config" / "opencode" / "skills" / SKILL_NAME,
    "agents": Path.home() / ".agents" / "skills" / SKILL_NAME,
    "codex": Path.home() / ".codex" / "skills" / SKILL_NAME,
    "project": Path.cwd() / ".opencode" / "skills" / SKILL_NAME,
}
TARGET_HELP = {
    "claude": "Claude Code",
    "opencode": "OpenCode (global)",
    "agents": "portable ~/.agents/skills",
    "codex": "Codex CLI",
    "project": "current project .opencode/skills",
}


def file_hashes(base: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(base)
        if any(part in {"__pycache__", ".git"} for part in rel.parts):
            continue
        if path.suffix == ".pyc":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        hashes[str(rel).replace("\\", "/")] = digest
    return hashes


def source_items() -> list[Path]:
    items = []
    for name in PAYLOAD:
        path = SOURCE / name
        if path.exists():
            items.append(path)
    return items


def install(target: Path, dry_run: bool = False) -> None:
    if dry_run:
        print(f"would install: {target}")
        for item in source_items():
            print(f"  {item.relative_to(SOURCE)}")
        return
    target.mkdir(parents=True, exist_ok=True)
    for item in source_items():
        dest = target / item.name
        if item.is_dir():
            shutil.copytree(item, dest, dirs_exist_ok=True, ignore=IGNORE)
        else:
            shutil.copy2(item, dest)
    print(f"installed: {target}")


def source_hashes() -> dict[str, str]:
    names = {path.name for path in source_items()}
    return {
        rel: digest
        for rel, digest in file_hashes(SOURCE).items()
        if rel.split("/")[0] in names
    }


def check(target: Path) -> bool:
    if not target.exists():
        print(f"missing:   {target}")
        return False
    source = source_hashes()
    installed = file_hashes(target)
    added = sorted(set(installed) - set(source))
    missing = sorted(set(source) - set(installed))
    changed = sorted(
        rel for rel in set(source) & set(installed) if source[rel] != installed[rel]
    )
    if not added and not missing and not changed:
        print(f"in sync:   {target}")
        return True
    print(f"differs:   {target}")
    for rel in missing:
        print(f"  missing: {rel}")
    for rel in changed:
        print(f"  changed: {rel}")
    for rel in added:
        print(f"  extra:   {rel}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Install the mindfluence skill.")
    parser.add_argument(
        "--target",
        choices=[*TARGETS, "all"],
        default="all",
        help="Where to install. Defaults to all global targets.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Show the install targets and whether they exist.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare installed copies with the repository and report differences.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without writing anything.",
    )
    args = parser.parse_args()

    if not (SOURCE / "SKILL.md").exists():
        print(f"error: {SOURCE / 'SKILL.md'} not found", file=sys.stderr)
        return 2

    selected = list(TARGETS) if args.target == "all" else [args.target]

    if args.list:
        for name in selected:
            path = TARGETS[name]
            status = "installed" if path.exists() else "not installed"
            print(f"{name:<9} {status:<14} {path}  ({TARGET_HELP[name]})")
        return 0

    if args.check:
        results = [check(TARGETS[name]) for name in selected]
        return 0 if all(results) else 1

    for name in selected:
        install(TARGETS[name], dry_run=args.dry_run)
    if not args.dry_run:
        print("done. start a new agent session or run /reload if the skill does not appear.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
