#!/usr/bin/env python3
"""Embed expanded component names for later matching."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import numpy as np
import pandas as pd
from dotenv import load_dotenv

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover
    raise SystemExit("openai package is required. Install it in .venv") from exc

from .project_paths import add_project_argument, resolve_paths

MODEL_NAME = "text-embedding-3-large"
BATCH_SIZE = 16


def load_existing(index_path: Path, vector_path: Path) -> tuple[pd.DataFrame, np.ndarray]:
    if index_path.exists() and vector_path.exists():
        return pd.read_csv(index_path), np.load(vector_path)
    return pd.DataFrame(columns=["component_key", "component_token", "expanded_name"]), np.zeros((0, 1), dtype=float)


def main() -> None:
    parser = argparse.ArgumentParser(description="Embed expanded component names for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    data_dir = paths.data_dir
    source = data_dir / "component_mapping.csv"
    index_path = data_dir / "component_embeddings_index.csv"
    vector_path = data_dir / "component_embeddings.npy"

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set in environment or .env")
    client = OpenAI(api_key=api_key)

    mapping = pd.read_csv(source)
    base_df = mapping[["component_key", "component_token", "expanded_name"]].drop_duplicates()

    index_df, vectors = load_existing(index_path, vector_path)
    existing = set(index_df["component_key"])
    pending = base_df[~base_df["component_key"].isin(existing)]
    if pending.empty:
        print("No new components require embeddings.")
        return

    new_vectors: list[list[float]] = []
    new_rows: list[dict] = []
    for i in range(0, len(pending), BATCH_SIZE):
        batch = pending.iloc[i : i + BATCH_SIZE]
        texts = batch["expanded_name"].tolist()
        response = client.embeddings.create(model=MODEL_NAME, input=texts)
        for meta, emb in zip(batch.itertuples(index=False), response.data):
            new_vectors.append(emb.embedding)
            new_rows.append(
                {
                    "component_key": meta.component_key,
                    "component_token": meta.component_token,
                    "expanded_name": meta.expanded_name,
                }
            )
        print(f"Embedded {min(i + BATCH_SIZE, len(pending))}/{len(pending)} components")

    new_matrix = np.array(new_vectors, dtype=float)
    combined_vectors = new_matrix if vectors.size == 0 else np.vstack([vectors, new_matrix])
    combined_index = pd.concat([index_df, pd.DataFrame(new_rows)], ignore_index=True)
    np.save(vector_path, combined_vectors)
    combined_index.to_csv(index_path, index=False)
    print(f"Stored embeddings for {len(new_rows)} components. Total cached: {combined_index.shape[0]}")


if __name__ == "__main__":
    main()
