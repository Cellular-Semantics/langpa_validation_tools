#!/usr/bin/env python3
"""Embed canonical GO terms from Table S10."""
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
BATCH_SIZE = 32


def load_existing(index_path: Path, vector_path: Path) -> tuple[pd.DataFrame, np.ndarray]:
    if index_path.exists() and vector_path.exists():
        return pd.read_csv(index_path), np.load(vector_path)
    return pd.DataFrame(columns=["annotation", "go_id", "go_term"]), np.zeros((0, 1), dtype=float)


def main() -> None:
    parser = argparse.ArgumentParser(description="Embed canonical GO terms for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    data_dir = paths.data_dir

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set")
    client = OpenAI(api_key=api_key)

    go_terms = pd.read_csv(data_dir / "go_terms.csv")
    base_df = go_terms[["annotation", "go_id", "go_term"]].drop_duplicates()

    index_df, vectors = load_existing(data_dir / "go_embeddings_index.csv", data_dir / "go_embeddings.npy")
    existing = set(zip(index_df["annotation"], index_df["go_term"]))
    pending = base_df[
        ~base_df.apply(lambda row: (row["annotation"], row["go_term"]) in existing, axis=1)
    ]
    if pending.empty:
        print("No new GO terms require embeddings.")
        return

    new_vectors: list[list[float]] = []
    new_rows: list[dict] = []
    for i in range(0, len(pending), BATCH_SIZE):
        batch = pending.iloc[i : i + BATCH_SIZE]
        texts = [f"GO term: {term}" for term in batch["go_term"]]
        response = client.embeddings.create(model=MODEL_NAME, input=texts)
        for meta, emb in zip(batch.itertuples(index=False), response.data):
            new_vectors.append(emb.embedding)
            new_rows.append(
                {
                    "annotation": meta.annotation,
                    "go_id": meta.go_id,
                    "go_term": meta.go_term,
                }
            )
        print(f"Embedded {min(i + BATCH_SIZE, len(pending))}/{len(pending)} GO terms")

    new_matrix = np.array(new_vectors, dtype=float)
    combined_vectors = new_matrix if vectors.size == 0 else np.vstack([vectors, new_matrix])
    combined_index = pd.concat([index_df, pd.DataFrame(new_rows)], ignore_index=True)
    np.save(data_dir / "go_embeddings.npy", combined_vectors)
    combined_index.to_csv(data_dir / "go_embeddings_index.csv", index=False)
    print(f"Stored embeddings for {len(new_rows)} GO terms. Total cached: {combined_index.shape[0]}")


if __name__ == "__main__":
    main()
