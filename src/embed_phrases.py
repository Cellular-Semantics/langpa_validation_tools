#!/usr/bin/env python3
"""Embed a set of test phrases to inspect cosine similarity distribution."""
from __future__ import annotations

import argparse
import json
import os
from bisect import bisect_left

import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
from scipy.cluster.hierarchy import leaves_list, linkage
from scipy.spatial.distance import squareform

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover
    raise SystemExit("openai package is required. Install it in .venv") from exc

from .project_paths import add_project_argument, resolve_paths

TEST_PHRASES = [
    "angiogenesis signaling",
    "synaptic vesicle fusion",
    "lipid raft remodeling",
    "immune checkpoint blockade",
    "astrocyte calcium wave",
    "myelin sheath development",
    "ferroptosis regulation",
    "autophagy initiation",
    "epigenetic chromatin silencing",
    "neuronal axon guidance",
    "cytotoxic T cell activation",
    "mesenchymal stem cell migration",
    "DNA damage checkpoint",
    "glutamate excitotoxic response",
    "hypoxia inducible factor",
    "cholesterol efflux",
    "vascular smooth muscle contraction",
    "microglial synaptic pruning",
    "mitochondrial biogenesis",
    "glycolytic switch",
    "random control phrase",
    "urban traffic modeling",
    "quantum circuit synthesis",
    "climate carbon sequestration",
]
MODEL_NAME = "text-embedding-3-large"
BATCH_SIZE = 16


def main() -> None:
    parser = argparse.ArgumentParser(description="Embed calibration phrases and compute similarity stats for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    paths = resolve_paths(args.project)
    OUTPUT_DIR = paths.analysis_dir
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STATS_PATH = OUTPUT_DIR / "embedding_calibration_stats.json"

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set")
    client = OpenAI(api_key=api_key)

    vectors = []
    for i in range(0, len(TEST_PHRASES), BATCH_SIZE):
        batch = TEST_PHRASES[i : i + BATCH_SIZE]
        response = client.embeddings.create(model=MODEL_NAME, input=batch)
        vectors.extend([item.embedding for item in response.data])
    vectors = np.array(vectors, dtype=float)
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    normalized = vectors / norms

    sims = []
    for i in range(len(TEST_PHRASES)):
        for j in range(i + 1, len(TEST_PHRASES)):
            sims.append(float(np.dot(normalized[i], normalized[j])))
    sims = np.array(sims)
    mean_cosine = float(sims.mean())
    median_cosine = float(np.median(sims))
    std_cosine = float(sims.std())
    min_cosine = float(sims.min())
    max_cosine = float(sims.max())
    stats_text = [
        f"Pairwise cosine count: {len(sims)}",
        f"Mean: {mean_cosine:.3f}",
        f"Median: {median_cosine:.3f}",
        f"Std: {std_cosine:.3f}",
        f"Min: {min_cosine:.3f}",
        f"Max: {max_cosine:.3f}",
    ]

    hist, bins = np.histogram(sims, bins=10, range=(-1, 1))
    hist_lines = [f"[{left:+.2f}, {right:+.2f}]: {count}" for count, left, right in zip(hist, bins[:-1], bins[1:])]

    stats_payload = {
        "model": MODEL_NAME,
        "phrase_count": len(TEST_PHRASES),
        "pairwise_count": len(sims),
        "mean": mean_cosine,
        "median": median_cosine,
        "std": std_cosine,
        "min": min_cosine,
        "max": max_cosine,
        "phrases": TEST_PHRASES,
    }
    STATS_PATH.write_text(json.dumps(stats_payload, indent=2))

    md_path = OUTPUT_DIR / "embedding_calibration.md"
    matrix_path = OUTPUT_DIR / "embedding_confusion_matrix.csv"

    matrix = np.zeros((len(TEST_PHRASES), len(TEST_PHRASES)))
    for i in range(len(TEST_PHRASES)):
        for j in range(len(TEST_PHRASES)):
            if i == j:
                matrix[i, j] = 1.0
            elif i < j:
                matrix[i, j] = float(np.dot(normalized[i], normalized[j]))
            else:
                matrix[i, j] = matrix[j, i]
    np.savetxt(matrix_path, matrix, delimiter=",", fmt="%.4f", header=",".join(TEST_PHRASES), comments="")

    # Cluster rows/columns using cosine-derived distances
    distance_matrix = 1.0 - matrix
    np.fill_diagonal(distance_matrix, 0.0)
    condensed = squareform(distance_matrix, checks=False)
    linkage_matrix = linkage(condensed, method="average")
    ordering = leaves_list(linkage_matrix)

    ordered_matrix = matrix[np.ix_(ordering, ordering)]
    ordered_labels = [TEST_PHRASES[idx] for idx in ordering]

    heatmap_path = OUTPUT_DIR / "embedding_confusion_heatmap.svg"
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(ordered_matrix, cmap="viridis", vmin=-0.2, vmax=1.0)
    ax.set_xticks(range(len(ordered_labels)))
    ax.set_xticklabels(ordered_labels, rotation=90, fontsize=8)
    ax.set_yticks(range(len(ordered_labels)))
    ax.set_yticklabels(ordered_labels, fontsize=8)
    ax.set_title("Cosine Similarity Heatmap (Clustered)")
    fig.colorbar(im, ax=ax, label="Cosine similarity")
    fig.tight_layout()
    fig.savefig(heatmap_path, dpi=300)
    plt.close(fig)

    pair_scores = []
    for i in range(len(TEST_PHRASES)):
        for j in range(i + 1, len(TEST_PHRASES)):
            pair_scores.append((matrix[i, j], TEST_PHRASES[i], TEST_PHRASES[j]))

    top_pairs = sorted(pair_scores, key=lambda item: item[0], reverse=True)[:10]

    sorted_pairs = sorted(pair_scores, key=lambda item: item[0])
    sorted_scores = [item[0] for item in sorted_pairs]

    def slice_around(target: float) -> tuple[list[tuple[float, str, str]], list[tuple[float, str, str]]]:
        idx = bisect_left(sorted_scores, target)
        below = sorted_pairs[max(0, idx - 3) : idx]
        above = sorted_pairs[idx : idx + 3]
        return below, above

    mean_below, mean_above = slice_around(mean_cosine)
    median_below, median_above = slice_around(median_cosine)

    with md_path.open("w") as fh:
        fh.write("# Embedding Similarity Calibration\n\n")
        fh.write("## Phrase list\n")
        for phrase in TEST_PHRASES:
            fh.write(f"- {phrase}\n")
        fh.write("\n## Statistics\n")
        for line in stats_text:
            fh.write(f"- {line}\n")
        fh.write("\n## Histogram (bins: [-1,1] split into 10)\n")
        for line in hist_lines:
            fh.write(f"- {line}\n")
        fh.write("\n## Top Similar Phrase Pairs\n")
        fh.write("| Rank | Phrase A | Phrase B | Cosine |\n")
        fh.write("| --- | --- | --- | --- |\n")
        for idx, (score, phrase_a, phrase_b) in enumerate(top_pairs, start=1):
            fh.write(f"| {idx} | {phrase_a} | {phrase_b} | {score:.3f} |\n")

        def write_side_table(
            title: str,
            below: list[tuple[float, str, str]],
            above: list[tuple[float, str, str]],
            target: float,
            descriptor: str,
        ) -> None:
            fh.write(f"\n## {title} (value = {target:.3f})\n")
            fh.write("| Side | Phrase A | Phrase B | Cosine |\n")
            fh.write("| --- | --- | --- | --- |\n")
            for score, phrase_a, phrase_b in reversed(below):
                fh.write(f"| Below {descriptor} | {phrase_a} | {phrase_b} | {score:.3f} |\n")
            for score, phrase_a, phrase_b in above:
                fh.write(f"| Above {descriptor} | {phrase_a} | {phrase_b} | {score:.3f} |\n")

        write_side_table("Pairs Around Mean Cosine", mean_below, mean_above, mean_cosine, "mean")
        write_side_table("Pairs Around Median Cosine", median_below, median_above, median_cosine, "median")
        fh.write(f"\nConfusion matrix saved to `{matrix_path.relative_to(paths.base_dir)}`\n")
        heatmap_relative = heatmap_path.relative_to(md_path.parent)
        fh.write(f"\n![Cosine similarity heatmap]({heatmap_relative})\n")

    print(f"Wrote calibration markdown to {md_path}")
    print(f"Wrote cosine matrix to {matrix_path}")
    print(f"Wrote heatmap to {heatmap_path}")
    print(f"Wrote calibration stats to {STATS_PATH}")


if __name__ == "__main__":
    main()
