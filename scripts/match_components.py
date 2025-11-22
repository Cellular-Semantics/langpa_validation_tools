#!/usr/bin/env python3
"""Match component embeddings to program embeddings for each run."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
COMPONENT_MAP = DATA_DIR / "component_mapping.csv"
COMP_INDEX = DATA_DIR / "component_embeddings_index.csv"
COMP_VECTORS = DATA_DIR / "component_embeddings.npy"
PROG_INDEX = DATA_DIR / "embeddings_index.csv"
PROG_VECTORS = DATA_DIR / "embeddings_name.npy"
OUTPUT = DATA_DIR / "component_program_matches.csv"


def normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return vectors / norms


def main() -> None:
    comp_map = pd.read_csv(COMPONENT_MAP)
    comp_index = pd.read_csv(COMP_INDEX)
    comp_vectors = normalize(np.load(COMP_VECTORS))
    comp_vec_map = {
        row.component_key: comp_vectors[idx] for idx, row in comp_index.iterrows()
    }

    prog_index = pd.read_csv(PROG_INDEX)
    prog_vectors = normalize(np.load(PROG_VECTORS))

    rows: list[dict] = []
    for comp in comp_map.itertuples(index=False):
        vec = comp_vec_map.get(comp.component_key)
        if vec is None:
            continue
        for run_idx in (1, 2):
            mask = (prog_index["folder"] == comp.folder) & (prog_index["run_index"] == run_idx)
            if not mask.any():
                continue
            subset = prog_index[mask].reset_index(drop=True)
            subset_vecs = prog_vectors[mask.to_numpy()]
            scores = subset_vecs @ vec
            order = np.argsort(scores)[::-1][:2]
            for rank, pos in enumerate(order, start=1):
                rows.append(
                    {
                        "annotation": comp.annotation,
                        "folder": comp.folder,
                        "component_token": comp.component_token,
                        "component_key": comp.component_key,
                        "expanded_name": comp.expanded_name,
                        "run_index": run_idx,
                        "match_rank": rank,
                        "program_index": int(subset.loc[pos, "program_index"]),
                        "program_name": subset.loc[pos, "program_name"],
                        "similarity": float(scores[pos]),
                    }
                )
    output_df = pd.DataFrame(rows)
    output_df.to_csv(OUTPUT, index=False)
    print(f"Wrote component-program matches to {OUTPUT}")


if __name__ == "__main__":
    main()
