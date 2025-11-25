#!/usr/bin/env python3
"""Extract JSON payloads and citation blocks from DeepSearch runs."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from .process_deepsearch import parse_run
from .project_paths import add_project_argument, resolve_paths



def extract_citations(text: str) -> list[dict]:
    citations: list[dict] = []
    pattern = re.compile(r"^\[\^([^\]]+)\]:\s*(\S+)", re.MULTILINE)
    for match in pattern.finditer(text):
        citations.append({"ref_id": match.group(1), "url": match.group(2)})
    return citations


def main() -> None:
def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Extract DeepSearch payloads and citation footnotes for a project.")
    add_project_argument(parser)
    args = parser.parse_args(argv)
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    data_dir = paths.data_dir
    payload_dir = data_dir / "run_payloads"
    citation_dir = data_dir / "run_citations"
    payload_dir.mkdir(parents=True, exist_ok=True)
    citation_dir.mkdir(parents=True, exist_ok=True)

    for folder in sorted(paths.deepsearch_dir.iterdir()):
        if not folder.is_dir():
            continue
        for run_file in sorted(folder.glob("run_*.md")):
            run_name = run_file.stem  # run_1 etc.
            text = run_file.read_text()
            payload = parse_run(run_file)

            rel_folder = payload_dir / folder.name
            rel_folder.mkdir(exist_ok=True)
            payload_path = rel_folder / f"{run_name}.json"
            payload_path.write_text(json.dumps(payload, indent=2))

            citations = extract_citations(text)
            cite_folder = citation_dir / folder.name
            cite_folder.mkdir(exist_ok=True)
            citation_path = cite_folder / f"{run_name}_citations.json"
            citation_path.write_text(json.dumps(citations, indent=2))

            print(
                f"Extracted {folder.name}/{run_name}: payload -> {payload_path}, citations -> {citation_path}"
            )


if __name__ == "__main__":
    main()
