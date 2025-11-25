#!/usr/bin/env python3
"""Match component embeddings to program embeddings for each run."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from .project_paths import add_project_argument, resolve_paths


def normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return vectors / norms


def main() -> None:
    parser = argparse.ArgumentParser(description="Match component embeddings to program embeddings for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    data_dir = paths.data_dir

    comp_map = pd.read_csv(data_dir / "component_mapping.csv")
    comp_index = pd.read_csv(data_dir / "component_embeddings_index.csv")
    comp_vectors = normalize(np.load(data_dir / "component_embeddings.npy"))
    comp_vec_map = {row.component_key: comp_vectors[idx] for idx, row in comp_index.iterrows()}

    prog_index = pd.read_csv(data_dir / "embeddings_index.csv")
    prog_vectors = normalize(np.load(data_dir / "embeddings_name.npy"))

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
    output_path = data_dir / "component_program_matches.csv"
    output_df.to_csv(output_path, index=False)
    print(f"Wrote component-program matches to {output_path}")


if __name__ == "__main__":
    main()
