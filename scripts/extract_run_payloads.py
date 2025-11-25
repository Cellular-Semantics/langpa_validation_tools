#!/usr/bin/env python3
"""Extract JSON payloads and citation blocks from DeepSearch runs."""
from __future__ import annotations

import json
import re
from pathlib import Path

from process_deepsearch import parse_run

BASE_DIR = Path(__file__).resolve().parent.parent
RUN_ROOT = BASE_DIR / "deepsearch"
DATA_DIR = BASE_DIR / "data"
PAYLOAD_DIR = DATA_DIR / "run_payloads"
CITATION_DIR = DATA_DIR / "run_citations"

PAYLOAD_DIR.mkdir(parents=True, exist_ok=True)
CITATION_DIR.mkdir(parents=True, exist_ok=True)


def extract_citations(text: str) -> list[dict]:
    citations: list[dict] = []
    pattern = re.compile(r"^\[\^([^\]]+)\]:\s*(\S+)", re.MULTILINE)
    for match in pattern.finditer(text):
        citations.append({"ref_id": match.group(1), "url": match.group(2)})
    return citations


def main() -> None:
    for folder in sorted(RUN_ROOT.iterdir()):
        if not folder.is_dir():
            continue
        for run_file in sorted(folder.glob("run_*.md")):
            run_name = run_file.stem  # run_1 etc.
            text = run_file.read_text()
            payload = parse_run(run_file)

            rel_folder = PAYLOAD_DIR / folder.name
            rel_folder.mkdir(exist_ok=True)
            payload_path = rel_folder / f"{run_name}.json"
            payload_path.write_text(json.dumps(payload, indent=2))

            citations = extract_citations(text)
            cite_folder = CITATION_DIR / folder.name
            cite_folder.mkdir(exist_ok=True)
            citation_path = cite_folder / f"{run_name}_citations.json"
            citation_path.write_text(json.dumps(citations, indent=2))

            print(f"Extracted {folder.name}/{run_name}: payload -> {payload_path}, citations -> {citation_path}")


if __name__ == "__main__":
    main()
