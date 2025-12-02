#!/usr/bin/env python3
"""Generate bubble heatmaps for run-to-run program overlaps."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent.parent / ".mpl-cache"))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from .project_paths import add_project_argument, resolve_paths


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 0.0, 0
    overlap = len(sa & sb)
    union = len(sa | sb)
    return (overlap / union if union else 0.0), overlap


def render_plot(
    folder_name,
    annotation,
    run1,
    run2,
    output_dir: Path,
    match_map: dict[tuple[int, int], float],
) -> bool:
    row_ids = [f"R1-{i+1}" for i in range(len(run1))]
    col_ids = [f"R2-{j+1}" for j in range(len(run2))]
    x_vals = []
    y_vals = []
    overlaps = []
    sim_vals = []
    missing_pairs = 0
    for i, r in run1.iterrows():
        for j, c in run2.iterrows():
            key = (int(r["program_index"]), int(c["program_index"]))
            sim_val = match_map.get(key)
            if sim_val is None:
                missing_pairs += 1
                continue
            jac, overlap = jaccard(r["genes"], c["genes"])
            if overlap == 0:
                continue
            x_vals.append(j)
            y_vals.append(i)
            overlaps.append(overlap)
            sim_vals.append(sim_val)

    if not x_vals:
        print(
            f"Warning: no valid combined similarity pairs for {folder_name}; skipping bubble plot.",
            file=sys.stderr,
        )
        return False
    if missing_pairs:
        print(
            f"Warning: missing {missing_pairs} combined similarity pairs for {folder_name}; plotting available matches only.",
            file=sys.stderr,
        )

    width = 1.6 * max(4, len(run2)) + 4
    height = 1.6 * max(4, len(run1))
    fig = plt.figure(figsize=(width, height))
    gs = fig.add_gridspec(1, 2, width_ratios=[3, 1])
    ax = fig.add_subplot(gs[0, 0])
    legend_ax = fig.add_subplot(gs[0, 1])
    scatter = ax.scatter(
        x_vals,
        y_vals,
        s=[max(60, o * 80) for o in overlaps],
        c=sim_vals,
        cmap="viridis",
        vmin=0,
        vmax=1,
        edgecolors="k",
        alpha=0.9,
    )
    ax.set_xticks(range(len(run2)))
    ax.set_yticks(range(len(run1)))
    ax.set_xticklabels(
        [f"{cid}\n({len(set(run2.loc[idx, 'genes']))} genes)" for idx, cid in enumerate(col_ids)],
        rotation=45,
        ha="right",
        color="tab:blue",
    )
    ax.set_yticklabels(
        [f"{rid} ({len(set(run1.loc[idx, 'genes']))} genes)" for idx, rid in enumerate(row_ids)],
        color="tab:orange",
    )
    ax.set_xlabel("Run 2 programs")
    ax.set_ylabel("Run 1 programs")
    ax.set_title(
        f"{annotation} ({folder_name})\nBubble size = overlap gene count, color = Combined similarity",
        fontsize=12,
    )
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
    cbar = fig.colorbar(scatter, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Combined similarity")

    legend_ax.set_xlim(0, 1)
    legend_ax.set_ylim(0, 1)
    legend_ax.axis("off")
    legend_lines = ["Row IDs (Run 1, orange text; axis label shows run ID and gene count):\n"]
    legend_lines.extend([f"{rid}: {run1.loc[idx, 'program_name']}" for idx, rid in enumerate(row_ids)])
    legend_lines.append("\nColumn IDs (Run 2, blue text; axis label shows run ID and gene count):\n")
    legend_lines.extend([f"{cid}: {run2.loc[idx, 'program_name']}" for idx, cid in enumerate(col_ids)])
    legend_text = "\n".join(legend_lines)
    legend_ax.text(0, 1, legend_text, va="top", fontsize=9)
    size_y = 0.05
    legend_ax.scatter(
        [0.1, 0.3, 0.5],
        [size_y] * 3,
        s=[max(60, s * 80) for s in [1, 5, 10]],
        color="gray",
        edgecolors="k",
    )
    for x, size in zip([0.1, 0.3, 0.5], [1, 5, 10]):
        legend_ax.text(x, size_y - 0.02, f"{size}", ha="center", va="top", fontsize=8)
    legend_ax.text(0.1, size_y + 0.05, "Bubble size = overlap genes", fontsize=8)
    plt.tight_layout()
    fig.savefig(output_dir / f"{folder_name}_bubble.png", dpi=200)
    plt.close(fig)


def generate_heatmaps(project: str) -> None:
    paths = resolve_paths(project)
    paths.ensure_output_dirs()
    data_dir = paths.data_dir
    output_dir = paths.analysis_dir / "confusion_heatmaps"
    output_dir.mkdir(parents=True, exist_ok=True)

    programs = pd.read_csv(data_dir / "deepsearch_programs.csv")
    programs["genes"] = programs["supporting_genes"].apply(json.loads)
    match_map_all = {}
    matches_path = data_dir / "deepsearch_program_matches.csv"
    if matches_path.exists() and matches_path.stat().st_size > 0:
        try:
            match_df = pd.read_csv(matches_path)
            for row in match_df.itertuples(index=False):
                key = (row.folder, int(row.program_a_index), int(row.program_b_index))
                match_map_all[key] = float(row.combined_similarity)
        except Exception as exc:  # noqa: BLE001
            print(f"Warning: failed to load match map from {matches_path}: {exc}")
            match_map_all = {}
    duplicates_path = data_dir / "deepsearch_duplicate_runs.csv"
    duplicate_folders: set[str] = set()
    if duplicates_path.exists():
        dup_df = pd.read_csv(duplicates_path)
        duplicate_folders = set(dup_df[dup_df["duplicate"]]["folder"].tolist())

    for (folder_name, annotation), grp in programs.groupby(["folder", "annotation"]):
        run1 = grp[grp["run_index"] == 1].sort_values("program_index").reset_index(drop=True)
        run2 = grp[grp["run_index"] == 2].sort_values("program_index").reset_index(drop=True)
        if run1.empty or run2.empty:
            continue
        if folder_name in duplicate_folders:
            fig, ax = plt.subplots(figsize=(6, 3))
            ax.axis("off")
            ax.text(0.5, 0.5, "Duplicate runs detected\n(no overlap plot)", ha="center", va="center", fontsize=12)
            plt.tight_layout()
            fig.savefig(output_dir / f"{folder_name}_bubble.png", dpi=200)
            plt.close(fig)
            continue
        folder_match_map = {
            (int(r.program_a_index), int(r.program_b_index)): float(r.combined_similarity)
            for r in match_df[match_df["folder"] == folder_name].itertuples(index=False)
        } if "match_df" in locals() else {}
        if not folder_match_map:
            print(
                f"Warning: no combined similarity entries for {folder_name}; skipping bubble plot.",
                file=sys.stderr,
            )
            continue
        if not render_plot(folder_name, annotation, run1, run2, output_dir, folder_match_map):
            continue


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate run overlap heatmaps for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    generate_heatmaps(args.project)


if __name__ == "__main__":
    main()
