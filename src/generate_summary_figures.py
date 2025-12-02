#!/usr/bin/env python3
"""Generate summary figures for run consistency and GO coverage."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import matplotlib

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent.parent / ".mpl-cache"))
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .project_paths import add_project_argument, resolve_paths


def plot_run_consistency(data_dir: Path, out_dir: Path) -> None:
    matches = pd.read_csv(data_dir / "deepsearch_program_matches.csv")
    dup_path = data_dir / "deepsearch_duplicate_runs.csv"
    duplicate_annotations: set[str] = set()
    if dup_path.exists():
        dup_df = pd.read_csv(dup_path)
        duplicate_annotations = set(dup_df[dup_df["duplicate"]]["annotation"].tolist())
    summary = (
        matches.groupby("annotation")
        .agg(
            avg_gene=("gene_jaccard", "mean"),
            avg_name=("name_similarity", "mean"),
            avg_combined=("combined_similarity", "mean"),
        )
        .reset_index()
        .sort_values("annotation")
    )
    if duplicate_annotations:
        summary = summary[~summary["annotation"].isin(duplicate_annotations)]
    labels = summary["annotation"].tolist()
    x = np.arange(len(labels))
    width = 0.25

    fig, ax = plt.subplots(figsize=(max(10, len(labels) * 0.9), 4))
    ax.bar(x - width, summary["avg_gene"], width, label="Gene Jaccard")
    ax.bar(x, summary["avg_name"], width, label="Name overlap")
    ax.bar(x + width, summary["avg_combined"], width, label="Combined")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_ylabel("Average similarity")
    ax.set_xlabel("Gene set annotation")
    ax.set_ylim(0, 1)
    ax.set_title("Run-to-run similarity by metric")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "run_consistency.svg")
    plt.close(fig)


def plot_go_coverage(data_dir: Path, out_dir: Path) -> None:
    summary_path = data_dir / "comparison_summary.csv"
    if not summary_path.exists() or summary_path.stat().st_size == 0:
        print(f"Skipping GO coverage plot: no comparison summary at {summary_path}")
        return
    try:
        summary = pd.read_csv(summary_path)
    except pd.errors.EmptyDataError:
        print(f"Skipping GO coverage plot: empty comparison summary at {summary_path}")
        return
    summary["go_match_pct"] = (
        summary["matched_go_terms_estimated"] / summary["total_gsea_terms"] * 100
    )
    summary = summary.sort_values("annotation")
    fig, ax = plt.subplots(figsize=(max(10, len(summary) * 0.8), 4))
    ax.bar(summary["annotation"], summary["go_match_pct"], color="#55A868")
    ax.set_ylabel("% GO terms matched")
    ax.set_xlabel("Gene set annotation")
    ax.set_ylim(0, 110)
    ax.set_title("GO coverage reported in comparison files")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(out_dir / "go_coverage.svg")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate summary figures for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    plot_run_consistency(paths.data_dir, paths.analysis_dir)
    plot_go_coverage(paths.data_dir, paths.analysis_dir)


if __name__ == "__main__":
    main()
