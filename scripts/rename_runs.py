#!/usr/bin/env python3
"""
Rename each DeepSearch run markdown to run_1.md / run_2.md within its folder.
Writes a CSV mapping original filenames to new names.
"""
from __future__ import annotations

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RUN_ROOT = BASE_DIR / "deepsearch"
MAPPING_FILE = BASE_DIR / "run_file_mapping.csv"


def rename_runs() -> None:
    records = []
    for folder in sorted(RUN_ROOT.glob("[0-9][0-9]_*/")):
        run_files = sorted(folder.glob("*.md"))
        if len(run_files) != 2:
            print(f"Skipping {folder} (expected 2 .md files, found {len(run_files)})")
            continue
        for idx, run_file in enumerate(run_files, start=1):
            new_name = folder / f"run_{idx}.md"
            if run_file.name == new_name.name:
                records.append(
                    {"folder": folder.name, "old_name": run_file.name, "new_name": new_name.name}
                )
                continue
            if new_name.exists():
                raise FileExistsError(f"Target {new_name} already exists")
            run_file.rename(new_name)
            print(f"Renamed {run_file} -> {new_name}")
            records.append(
                {"folder": folder.name, "old_name": run_file.name, "new_name": new_name.name}
            )
    with MAPPING_FILE.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["folder", "old_name", "new_name"])
        writer.writeheader()
        writer.writerows(records)
    print(f"Mapping written to {MAPPING_FILE}")


if __name__ == "__main__":
    rename_runs()
