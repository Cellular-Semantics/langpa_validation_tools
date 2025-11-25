#!/usr/bin/env python3
"""Build component tokens and expansions for gene-set annotations."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd

from .project_paths import add_project_argument, resolve_paths

EXPANSIONS = {
    "ac": (
        "Astrocyte-like malignant program",
        "Described as astrocyte lineage mimicry in de Jong et al. 2025",
    ),
    "opc": (
        "Oligodendrocyte precursor-like malignant program",
        "Matches oligodendrocyte precursor states described in de Jong et al. 2025",
    ),
    "npc": (
        "Neural progenitor-like proliferative program",
        "Reflects neural progenitor-like programs highlighted in de Jong et al. 2025",
    ),
    "gliosis": (
        "Reactive gliosis and inflammatory response",
        "Summarizes the reactive gliosis signatures detailed in de Jong et al. 2025",
    ),
    "hypoxia": (
        "Hypoxic and angiogenic adaptation program",
        "Captures the hypoxia-driven angiogenic responses described in de Jong et al. 2025",
    ),
    "proliferative": (
        "Proliferative cycling and mitotic program",
        "Corresponds to the proliferative trajectories reported in de Jong et al. 2025",
    ),
    "neuronal": (
        "Neuronal differentiation and signaling program",
        "Summarizes neuronal signaling features in de Jong et al. 2025",
    ),
}


def tokenize(annotation: str) -> list[str]:
    tokens = re.sub(r"-", " ", annotation).split()
    cleaned: list[str] = []
    for token in tokens:
        tok = token.strip()
        if not tok:
            continue
        if tok.lower() == "like":
            continue
        if tok.isdigit():
            continue
        cleaned.append(tok)
    return cleaned


def main() -> None:
    parser = argparse.ArgumentParser(description="Build component token mapping for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    if not paths.s10_file.exists():
        raise FileNotFoundError(f"Project spreadsheet not found: {paths.s10_file}")
    if not paths.mapping_file.exists():
        raise FileNotFoundError(f"Mapping file not found: {paths.mapping_file}")

    table = pd.read_excel(paths.s10_file, sheet_name="Table S10")
    folder_map = pd.read_csv(paths.mapping_file)
    annotation_to_folder = dict(zip(folder_map["annotation"], folder_map["new_folder"]))
    rows = []
    for ann in table["annotation"].dropna().unique():
        folder = annotation_to_folder.get(ann)
        components = tokenize(ann)
        for order, token in enumerate(components, start=1):
            key = token.lower()
            expanded, note = EXPANSIONS.get(
                key,
                (token, "No expansion available; token retained as-is."),
            )
            rows.append(
                {
                    "annotation": ann,
                    "folder": folder,
                    "component_token": token,
                    "component_key": key,
                    "component_order": order,
                    "expanded_name": expanded,
                    "source_note": note,
                }
            )
    df = pd.DataFrame(rows).sort_values(["folder", "component_order", "component_token"])
    output = paths.data_dir / "component_mapping.csv"
    df.to_csv(output, index=False)
    print(f"Wrote component mapping to {output}")


if __name__ == "__main__":
    main()
