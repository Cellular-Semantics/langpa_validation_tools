#!/usr/bin/env python3
"""Generate and cache embeddings for DeepSearch programs."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from dotenv import load_dotenv

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover
    raise SystemExit("openai package is required. Install it in .venv") from exc

from process_deepsearch import parse_run  # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RUN_ROOT = BASE_DIR / "deepsearch"
INDEX_PATH = DATA_DIR / "embeddings_index.csv"
VECTOR_PATH = DATA_DIR / "embeddings_name.npy"
MODEL_NAME = "text-embedding-3-large"
BATCH_SIZE = 32


def load_existing() -> Tuple[pd.DataFrame, np.ndarray]:
    if INDEX_PATH.exists() and VECTOR_PATH.exists():
        index_df = pd.read_csv(INDEX_PATH)
        vectors = np.load(VECTOR_PATH)
    else:
        index_df = pd.DataFrame(columns=["folder", "run_index", "program_index", "program_name"])
        vectors = np.zeros((0, 1), dtype=float)
    return index_df, vectors


def build_text(program: Dict) -> str:
    return program.get("program_name", "") or ""


def gather_programs() -> List[Tuple[str, int, int, str, str]]:
    programs_df = pd.read_csv(DATA_DIR / "deepsearch_programs.csv")
    entries: List[Tuple[str, int, int, str, str]] = []
    cache: Dict[Tuple[str, int], Dict] = {}
    for row in programs_df.itertuples(index=False):
        folder = row.folder
        run_index = int(row.run_index)
        program_index = int(row.program_index)
        key = (folder, run_index)
        if key not in cache:
            run_path = RUN_ROOT / folder / f"run_{run_index}.md"
            cache[key] = parse_run(run_path)
        program = cache[key]["programs"][program_index]
        text = build_text(program)
        entries.append((folder, run_index, program_index, program.get("program_name", ""), text))
    return entries


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set in environment or .env")
    client = OpenAI(api_key=api_key)

    index_df, vectors = load_existing()
    existing_keys = set(
        zip(index_df["folder"], index_df["run_index"], index_df["program_index"])
    )

    pending: List[Tuple[str, int, int, str, str]] = []
    for folder, run_idx, prog_idx, prog_name, text in gather_programs():
        key = (folder, run_idx, prog_idx)
        if key in existing_keys or not text:
            continue
        pending.append((folder, run_idx, prog_idx, prog_name, text))

    if not pending:
        print("No new programs require embeddings.")
        return

    new_vectors: List[List[float]] = []
    new_rows: List[Dict] = []
    for i in range(0, len(pending), BATCH_SIZE):
        batch = pending[i : i + BATCH_SIZE]
        texts = [item[4] for item in batch]
        response = client.embeddings.create(model=MODEL_NAME, input=texts)
        for meta, emb in zip(batch, response.data):
            folder, run_idx, prog_idx, prog_name, _ = meta
            new_vectors.append(emb.embedding)
            new_rows.append(
                {
                    "folder": folder,
                    "run_index": run_idx,
                    "program_index": prog_idx,
                    "program_name": prog_name,
                }
            )
        print(f"Embedded {min(i + BATCH_SIZE, len(pending))}/{len(pending)} programs")

    new_matrix = np.array(new_vectors, dtype=float)
    if vectors.size == 0:
        combined = new_matrix
    else:
        combined = np.vstack([vectors, new_matrix])
    combined_df = pd.concat([index_df, pd.DataFrame(new_rows)], ignore_index=True)

    np.save(VECTOR_PATH, combined)
    combined_df.to_csv(INDEX_PATH, index=False)
    print(f"Stored embeddings for {len(new_rows)} programs. Total cached: {combined_df.shape[0]}")


if __name__ == "__main__":
    main()
