#!/usr/bin/env python3
"""Embed expanded component names for later matching."""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pandas as pd
from dotenv import load_dotenv

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover
    raise SystemExit("openai package is required. Install it in .venv") from exc

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SOURCE = DATA_DIR / "component_mapping.csv"
INDEX_PATH = DATA_DIR / "component_embeddings_index.csv"
VECTOR_PATH = DATA_DIR / "component_embeddings.npy"
MODEL_NAME = "text-embedding-3-large"
BATCH_SIZE = 16


def load_existing() -> tuple[pd.DataFrame, np.ndarray]:
    if INDEX_PATH.exists() and VECTOR_PATH.exists():
        return pd.read_csv(INDEX_PATH), np.load(VECTOR_PATH)
    return pd.DataFrame(columns=["component_key", "component_token", "expanded_name"]), np.zeros(
        (0, 1), dtype=float
    )


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set in environment or .env")
    client = OpenAI(api_key=api_key)

    mapping = pd.read_csv(SOURCE)
    base_df = mapping[["component_key", "component_token", "expanded_name"]].drop_duplicates()

    index_df, vectors = load_existing()
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
    combined_vectors = (
        new_matrix if vectors.size == 0 else np.vstack([vectors, new_matrix])
    )
    combined_index = pd.concat([index_df, pd.DataFrame(new_rows)], ignore_index=True)
    np.save(VECTOR_PATH, combined_vectors)
    combined_index.to_csv(INDEX_PATH, index=False)
    print(f"Stored embeddings for {len(new_rows)} components. Total cached: {combined_index.shape[0]}")


if __name__ == "__main__":
    main()
