#!/usr/bin/env python3
"""Extract GO terms from Table S10."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd

from .project_paths import add_project_argument, resolve_paths


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
    parser = argparse.ArgumentParser(description="Extract GO terms from Table S10 for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    if not paths.s10_file.exists():
        raise FileNotFoundError(f"Project spreadsheet not found: {paths.s10_file}")
    table = pd.read_excel(paths.s10_file, sheet_name="Table S10")
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
    output = paths.data_dir / "go_terms.csv"
    df.to_csv(output, index=False)
    print(f"Wrote GO terms to {output}")


if __name__ == "__main__":
    main()
