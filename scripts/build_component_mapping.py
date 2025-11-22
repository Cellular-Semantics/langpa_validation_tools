#!/usr/bin/env python3
"""Build component tokens and expansions for gene-set annotations."""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
S10_FILE = BASE_DIR / "media-3 (2).xlsx"
FOLDER_MAP = BASE_DIR / "geneset_folder_mapping.csv"
OUTPUT = BASE_DIR / "data" / "component_mapping.csv"

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
    table = pd.read_excel(S10_FILE, sheet_name="Table S10")
    folder_map = pd.read_csv(FOLDER_MAP)
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
    df = pd.DataFrame(rows).sort_values(
        ["folder", "component_order", "component_token"]
    )
    df.to_csv(OUTPUT, index=False)
    print(f"Wrote component mapping to {OUTPUT}")


if __name__ == "__main__":
    main()
