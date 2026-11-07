#!/usr/bin/env python3
"""Deterministic checks for the 13 MindFluence anti-patterns.

Implements the mechanical parts of the detection rules in ``SKILL.md``.
AP-9 (wrong-source halo) stays a human-review finding: whether the audience
trusts a given source cannot be decided by a regex.

Usage:
    python scripts/anti_patterns.py output.md --tier standard
    python scripts/anti_patterns.py output.md --tier extended --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

VAGUE = r"\b(thousands|many|lots of|countless|numerous)\b"
CUSTOMER = r"\b(customers?|users?|teams?|clients?|companies|businesses)\b"
FEAR = r"\b(fail|fails|failure|risk|threat|danger|bankrupt|collapse|obsolete|replac(e|ed|es|ing)|miss out|left behind|die)\b"
SOLUTION = r"\b(fix|solution|start|try|step|guide|tool|template|checklist|avoid|plan|system|switch|learn)\b"
FRAME = r"(isn'?t\b.{1,140}\b(it'?s|it is)\b|\bnot\b.{1,140}\bbut\b|this is not\b.{1,140}\bit is\b)"
ANCHOR = r"(\$\d|\d+\s?(%|hours?|days?|weeks?|months?|minutes?|users?|customers?|teams?))"
AUTH = r"\b(studies show|research indicates|experts say|science proves|data confirms)\b"
SOURCE = r"(\[\s*Source|\b(19|20)\d{2}\b)"
GIFT = r"\b(free|gift|checklist|template|guide|ebook|lead magnet)\b"
ASK = r"\b(book|demo|call|reply|click|sign up|buy|order|schedule)\b"
SCARCITY = r"\b(only \d+ (left|seats?|spots?)|limited time|closing soon|ends in \d+|\d+ (hours?|days?) left)\b"
WHY = r"\b(because|since|capacity|team of|we cap|max|constraint)\b"
SUNK = r"\b(you'?ve come this far|you have come this far|you'?ve already|you have already|don'?t waste)\b"
INGROUP = r"\b(like-minded|community of|people who care)\b"
IDENTITY = r"\b(for|join)\s+[A-Z][a-z]+|\bwho\b.{0,40}\b(built|shipped|scaled|run|running)\b"
HALO = r"\b(as seen on|featured in|trusted by)\b"
INSULT = r"\bmost people\b.{0,40}\b(are wrong|don'?t know|fail|ignore)\b"
VISUAL = r"\b(imagine|picture this)\b"
SENSORY = r"(\d{1,2}(:\d{2})?\s?(am|pm)|\b(red|blue|green|black|white|cold|warm|hot|loud|quiet|smell|sound|taste|texture)\b)"
BLAME = r"\byou\b.{0,40}\b(say|claim)\b.{0,40}\bbut\b|\byou\b.{0,40}\byet you\b"
STATS = r"(\d+%|\bN=\d+\b|\bmedian\b|\baverage\b|\bpercent\b)"
NARRATIVE = r"(\[illustrative\]|\"[^\"]{10,}\"|said|told us)"
META_LINE = re.compile(r"^\[[A-Z][A-Z /-]*:.*\]$")


@dataclass
class Finding:
    id: str
    name: str
    severity: str  # "fail" or "review"
    detail: str


def _body(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not META_LINE.match(line.strip()))


def _has(pattern: str, text: str) -> bool:
    return bool(re.search(pattern, text, re.I | re.S))


def check(text: str, tier: str = "standard") -> list[Finding]:
    body = _body(text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    findings: list[Finding] = []

    def add(ap_id: str, name: str, detail: str, severity: str = "fail") -> None:
        findings.append(Finding(ap_id, name, severity, detail))

    if _has(VAGUE, body) and _has(CUSTOMER, body):
        add("AP-1", "Vague Social Proof", "vague quantity near a customer claim")
    if any(_has(FEAR, p) and not _has(SOLUTION, p) for p in paras):
        add("AP-2", "Fear Without an Exit", "fear trigger without a solution in the same paragraph")
    if any(_has(FRAME, p) and not _has(ANCHOR, p) for p in paras):
        add("AP-3", "Framing Without Anchoring", "reframe without a quantified anchor in the same paragraph")
    if _has(AUTH, body) and not _has(SOURCE, body):
        add("AP-4", "Authority Without Proof", "authority claim without source/year")
    if any(_has(GIFT, p) and _has(ASK, p) for p in paras):
        add("AP-5", "Transactional Reciprocity", "free value and ask in the same paragraph")
    if any(_has(SCARCITY, p) and not _has(WHY, p) for p in paras):
        add("AP-6", "Fake Scarcity", "scarcity without an explained constraint in the same paragraph")
    if paras and _has(SUNK, paras[0]):
        add("AP-7", "Premature Sunk Cost", "sunk-cost language in the opening paragraph")
    if _has(INGROUP, body) and not _has(IDENTITY, body):
        add("AP-8", "Empty In-Group", "in-group phrase without a named identity")
    if _has(HALO, body):
        add("AP-9", "Wrong-Source Halo", "halo source needs a human audience-fit review", "review")
    if _has(INSULT, body):
        add("AP-10", "Insulting Confirmation", "reader implied to be in the wrong group")
    if _has(VISUAL, body) and len(re.findall(SENSORY, body, re.I)) < 3:
        add("AP-11", "Abstract Availability", "visual prompt with fewer than 3 sensory details")
    if _has(BLAME, body):
        add("AP-12", "Blaming Dissonance", "dissonance blames the reader, not the system")
    if tier in ("standard", "extended") and _has(STATS, body) and not _has(NARRATIVE, body):
        add("AP-13", "Statistical-Only Fallacy", "aggregate statistics without a compliant narrative")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check MindFluence anti-patterns.")
    parser.add_argument("path", help="Output file to check, or - for stdin")
    parser.add_argument("--tier", choices=["compact", "standard", "extended"], default="standard")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    text = sys.stdin.read() if args.path == "-" else Path(args.path).read_text(encoding="utf-8")
    findings = check(text, args.tier)

    if args.json:
        print(json.dumps([asdict(f) for f in findings], ensure_ascii=False, indent=2))
    else:
        if not findings:
            print("PASS: no anti-patterns detected")
        for f in findings:
            print(f"[{f.severity.upper()}] {f.id} {f.name}: {f.detail}")
    return 1 if any(f.severity == "fail" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
