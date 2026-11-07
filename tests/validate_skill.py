#!/usr/bin/env python3
"""Structural validator for MindFluence.

Stdlib only. Run from the repository root or from any directory:

    python tests/validate_skill.py

Exits 1 if any hard check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "mindfluence"
SKILL = SKILL_DIR / "SKILL.md"
CHANGELOG = ROOT / "CHANGELOG.md"
README = ROOT / "README.md"
README_RU = ROOT / "README.ru.md"

REQUIRED_SECTIONS = [
    "Bias Quick-Reference Card",
    "Role",
    "Refusal Policy",
    "Data Provenance Policy",
    "When Not to Use",
    "Operating Modes",
    "Bias Selection Router",
    "Scenario Quick-Reference",
    "Bias Catalog",
    "Power Bias Combinations",
    "Bias Conflict Detector",
    "Cultural Quick-Reference",
    "Anti-Patterns (13)",
    "Narrative Depth Requirements",
    "Reference Files",
    "Output Contract",
    "Post-Generation Verification",
]

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(end, i + len(start))
    return text[i:j] if j >= 0 else text[i:]


def table_rows(block: str) -> list[str]:
    rows = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or set(cells[0]) <= {"-", ":", " "}:
            continue
        if cells[0].lower() in {"#", "audience", "lang", "style", "region", "bias", "scenario", "id"}:
            continue
        rows.append(line)
    return rows


def main() -> int:
    text = read(SKILL)
    changelog = read(CHANGELOG)
    readme = read(README)
    readme_ru = read(README_RU)

    if not text.startswith("---"):
        fail("SKILL.md must start with YAML frontmatter")
        return report()

    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("unterminated YAML frontmatter")
        return report()
    raw = match.group(1)

    top = dict(re.findall(r"^([a-z_]+):\s*(.+)$", raw, re.M))
    meta = dict(re.findall(r"^  ([a-z_]+):\s*(.+)$", raw, re.M))

    if top.get("name") != "mindfluence":
        fail(f"frontmatter name must be 'mindfluence', got {top.get('name')!r}")
    description = top.get("description", "").strip().strip('"')
    if not 80 <= len(description) <= 1024:
        fail(f"description length must be 80..1024, got {len(description)}")
    if "DO NOT use" not in description:
        fail("description must include negative triggers ('DO NOT use')")
    for skill in ("RankWise", "AngleCraft", "human-ai"):
        if skill not in description:
            fail(f"description must name the handoff skill {skill!r}")
    if top.get("license") != "MIT":
        fail("frontmatter license must be MIT")
    if not top.get("compatibility"):
        fail("frontmatter compatibility is required")

    version = meta.get("version", "").strip().strip('"')
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"metadata.version must be semver, got {version!r}")
    elif f"[{version}]" not in changelog:
        fail(f"CHANGELOG.md has no entry for {version}")
    if version and version not in readme:
        fail(f"README.md does not mention version {version}")
    if version and version not in readme_ru:
        fail(f"README.ru.md does not mention version {version}")

    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            fail(f"missing section: ## {section}")

    biases = [int(n) for n in re.findall(r"^### (\d+)\. ", between(text, "## Bias Catalog", "## Social Contracts"), re.M)]
    if biases != list(range(1, 21)):
        fail(f"bias catalog must contain headings 1..20, got {biases}")

    router = table_rows(between(text, "### Master Router Table", "### Router Procedure"))
    if len(router) != 38:
        fail(f"bias router must have 38 rows, got {len(router)}")

    combos = table_rows(between(text, "## Power Bias Combinations", "## Bias Conflict Detector"))
    if len(combos) != 14:
        fail(f"power combinations must have 14 rows, got {len(combos)}")

    anti_patterns = [int(n) for n in re.findall(r"^### AP-(\d+): ", text, re.M)]
    if anti_patterns != list(range(1, 14)):
        fail(f"anti-patterns must be numbered 1..13, got {anti_patterns}")

    tones = table_rows(between(text, "## Tone-of-Voice Switcher", "### Hybrid Tones"))
    if len(tones) != 7:
        fail(f"tone switcher must have 7 rows, got {len(tones)}")

    regions = table_rows(between(text, "### Regional Quick-Card", "### Dimension-Specific"))
    if len(regions) != 12:
        fail(f"regional quick-card must have 12 rows, got {len(regions)}")

    checks = re.findall(r"^\d+\. □ ", between(text, "## Post-Generation Verification", "## Few-Shot Examples"), re.M)
    if len(checks) != 7:
        fail(f"post-generation verification must have 7 checks, got {len(checks)}")

    examples = sorted((SKILL_DIR / "examples").glob("*.md"))
    scenarios = sorted((SKILL_DIR / "scenarios").glob("*.md"))
    if len(examples) != 7:
        fail(f"examples/ must contain 7 files, found {len(examples)}")
    if len(scenarios) != 13:
        fail(f"scenarios/ must contain 13 files, found {len(scenarios)}")

    if "examples//" in text:
        fail("SKILL.md contains a double slash ('examples//')")
    for needle in ("TODO", "FIXME"):
        if needle in text:
            fail(f"SKILL.md contains forbidden string: {needle!r}")

    paths = set(re.findall(r"`((?:references|scenarios|examples)/[^`]+)`", text))
    paths |= set(re.findall(r"\]\(((?:references|scenarios|examples)/[^)]+)\)", text))
    for rel in sorted(paths):
        if not (SKILL_DIR / rel).exists():
            fail(f"SKILL.md points to a missing path: {rel}")

    for linked in re.findall(r"\]\(([^)]+)\)", text):
        if linked.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = linked.split("#", 1)[0]
        if target and not (SKILL_DIR / target).exists():
            fail(f"SKILL.md links to a missing path: {linked}")

    if "]()" in readme:
        fail("README.md contains an empty link ']()'")

    return report()


def report() -> int:
    if errors:
        print("MindFluence validator")
        print("\nErrors:")
        for message in errors:
            print(f"  - {message}")
        print(f"\nFAILED: {len(errors)} error(s)")
        return 1
    print("MindFluence validator")
    print("OK: all structural checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
