#!/usr/bin/env python3
"""Embed canonical GO terms from Table S10."""
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
SOURCE = DATA_DIR / "go_terms.csv"
INDEX_PATH = DATA_DIR / "go_embeddings_index.csv"
VECTOR_PATH = DATA_DIR / "go_embeddings.npy"
MODEL_NAME = "text-embedding-3-large"
BATCH_SIZE = 32


def load_existing() -> tuple[pd.DataFrame, np.ndarray]:
    if INDEX_PATH.exists() and VECTOR_PATH.exists():
        return pd.read_csv(INDEX_PATH), np.load(VECTOR_PATH)
    return pd.DataFrame(columns=["annotation", "go_id", "go_term"]), np.zeros((0, 1), dtype=float)


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set")
    client = OpenAI(api_key=api_key)

    go_terms = pd.read_csv(SOURCE)
    base_df = go_terms[["annotation", "go_id", "go_term"]].drop_duplicates()

    index_df, vectors = load_existing()
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
    np.save(VECTOR_PATH, combined_vectors)
    combined_index.to_csv(INDEX_PATH, index=False)
    print(f"Stored embeddings for {len(new_rows)} GO terms. Total cached: {combined_index.shape[0]}")


if __name__ == "__main__":
    main()
