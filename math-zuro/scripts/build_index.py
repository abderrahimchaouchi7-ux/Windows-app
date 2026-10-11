#!/usr/bin/env python3
"""Build a machine-readable index (JSONL) from the Math ZURO knowledge base.

Each entry in knowledge/*.md must start with a heading of the form:

    ### [TYPE-UNIT-NN] Title

The entry body runs until the next heading (### or ##) or a horizontal rule.
Output: knowledge/index.jsonl, one JSON object per entry.

Usage:  python3 math-zuro/scripts/build_index.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge"
OUT = KNOWLEDGE / "index.jsonl"

HEADING = re.compile(r"^###\s+\[([A-Z]+)-([A-Z]+)-(\d{2})\]\s+(.+?)\s*$")
TYPE_NAMES = {
    "DEF": "تعريف",
    "THM": "مبرهنة",
    "RULE": "قاعدة/خاصية",
    "METH": "منهجية",
    "EX": "مثال محلول",
    "AX": "بديهية",
}


def parse_file(path: pathlib.Path):
    entries = []
    current = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = HEADING.match(raw)
        if m:
            if current:
                entries.append(current)
            kind, unit, num, title = m.groups()
            current = {
                "id": f"{kind}-{unit}-{num}",
                "type": TYPE_NAMES.get(kind, kind),
                "unit": unit,
                "title": title,
                "source_file": path.name,
                "body_lines": [],
            }
            continue
        if current is None:
            continue
        if raw.startswith("## ") or raw.strip() == "---":
            entries.append(current)
            current = None
            continue
        current["body_lines"].append(raw)
    if current:
        entries.append(current)

    for e in entries:
        body = "\n".join(e.pop("body_lines")).strip()
        e["content"] = body
    return entries


def main() -> int:
    files = sorted(p for p in KNOWLEDGE.glob("*.md") if p.name[:2].isdigit())
    if not files:
        print("No knowledge files found", file=sys.stderr)
        return 1

    all_entries = []
    for f in files:
        all_entries.extend(parse_file(f))

    ids = [e["id"] for e in all_entries]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        print(f"Duplicate ids: {dupes}", file=sys.stderr)
        return 2

    with OUT.open("w", encoding="utf-8") as fh:
        for e in all_entries:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    per_type = {}
    for e in all_entries:
        per_type[e["type"]] = per_type.get(e["type"], 0) + 1
    print(f"Wrote {len(all_entries)} entries to {OUT.relative_to(ROOT.parent)}")
    for t, n in sorted(per_type.items()):
        print(f"  {t}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
