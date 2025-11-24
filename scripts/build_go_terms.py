#!/usr/bin/env python3
"""Extract GO terms from Table S10."""
from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
S10_FILE = BASE_DIR / "media-3 (2).xlsx"
OUTPUT = BASE_DIR / "data" / "go_terms.csv"


def parse_terms(raw: str) -> list[tuple[str, str]]:
    parts = [part.strip() for part in raw.split(",") if part.strip()]
    results: list[tuple[str, str]] = []
    for part in parts:
        match = re.match(r"(.+?)\s*\((GO:\d+)\)$", part)
        if match:
            term = match.group(1).strip()
            go_id = match.group(2)
        else:
            term = part
            go_id = ""
        results.append((go_id, term))
    return results


def main() -> None:
    table = pd.read_excel(S10_FILE, sheet_name="Table S10")
    rows = []
    for annotation, raw in zip(table["annotation"], table["Enriched Pathways"]):
        if not isinstance(raw, str):
            continue
        for idx, (go_id, term) in enumerate(parse_terms(raw), start=1):
            rows.append(
                {
                    "annotation": annotation,
                    "go_term": term,
                    "go_id": go_id,
                    "order": idx,
                }
            )
    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT, index=False)
    print(f"Wrote GO terms to {OUTPUT}")


if __name__ == "__main__":
    main()
