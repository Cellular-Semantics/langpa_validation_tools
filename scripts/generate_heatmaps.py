#!/usr/bin/env python3
import json
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent.parent / ".mpl-cache"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_DIR = Path("data")
OUTPUT_DIR = Path("analysis/confusion_heatmaps")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
programs = pd.read_csv(DATA_DIR / "deepsearch_programs.csv")
programs["genes"] = programs["supporting_genes"].apply(json.loads)
duplicates_path = DATA_DIR / "deepsearch_duplicate_runs.csv"
duplicate_folders: set[str] = set()
if duplicates_path.exists():
    dup_df = pd.read_csv(duplicates_path)
    duplicate_folders = set(dup_df[dup_df["duplicate"]]["folder"].tolist())


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 0.0, 0
    overlap = len(sa & sb)
    union = len(sa | sb)
    return (overlap / union if union else 0.0), overlap


def truncate(name, max_len):
    return name if len(name) <= max_len else name[: max_len - 1] + '…'


def render_plot(folder_name, annotation, run1, run2):
    row_ids = [f"R1-{i+1}" for i in range(len(run1))]
    col_ids = [f"R2-{j+1}" for j in range(len(run2))]
    x_vals = []
    y_vals = []
    overlaps = []
    jac_vals = []
    for i, r in run1.iterrows():
        for j, c in run2.iterrows():
            jac, overlap = jaccard(r["genes"], c["genes"])
            if overlap == 0:
                continue
            x_vals.append(j)
            y_vals.append(i)
            overlaps.append(overlap)
            jac_vals.append(jac)

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
        c=jac_vals,
        cmap="viridis",
        vmin=0,
        vmax=1,
        edgecolors="k",
        alpha=0.9,
    )
    ax.set_xticks(range(len(run2)))
    ax.set_yticks(range(len(run1)))
    ax.set_xticklabels(
        [
            f"{cid}\n({len(set(run2.loc[idx, 'genes']))} genes)"
            for idx, cid in enumerate(col_ids)
        ],
        rotation=45,
        ha="right",
        color="tab:blue",
    )
    ax.set_yticklabels(
        [
            f"{rid} ({len(set(run1.loc[idx, 'genes']))} genes)"
            for idx, rid in enumerate(row_ids)
        ],
        color="tab:orange",
    )
    ax.set_xlabel("Run 2 programs")
    ax.set_ylabel("Run 1 programs")
    ax.set_title(
        f"{annotation} ({folder_name})\nBubble size = overlap gene count, color = Jaccard overlap",
        fontsize=12,
    )
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
    cbar = fig.colorbar(scatter, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Jaccard overlap")

    legend_ax.set_xlim(0, 1)
    legend_ax.set_ylim(0, 1)
    legend_ax.axis("off")
    legend_lines = [
        "Row IDs (Run 1, orange text; axis label shows run ID and gene count):\n"
    ]
    legend_lines.extend(
        [f"{rid}: {run1.loc[idx, 'program_name']}" for idx, rid in enumerate(row_ids)]
    )
    legend_lines.append(
        "\nColumn IDs (Run 2, blue text; axis label shows run ID and gene count):\n"
    )
    legend_lines.extend(
        [f"{cid}: {run2.loc[idx, 'program_name']}" for idx, cid in enumerate(col_ids)]
    )
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
    fig.savefig(OUTPUT_DIR / f"{folder_name}_bubble.png", dpi=200)
    plt.close(fig)


for (folder_name, annotation), grp in programs.groupby(["folder", "annotation"]):
    run1 = grp[grp["run_index"] == 1].sort_values("program_index").reset_index(drop=True)
    run2 = grp[grp["run_index"] == 2].sort_values("program_index").reset_index(drop=True)
    if run1.empty or run2.empty:
        continue
    if folder_name in duplicate_folders:
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.axis("off")
        ax.text(
            0.5,
            0.5,
            "Duplicate runs detected\n(no overlap plot)",
            ha="center",
            va="center",
            fontsize=12,
        )
        plt.tight_layout()
        fig.savefig(OUTPUT_DIR / f"{folder_name}_bubble.png", dpi=200)
        plt.close(fig)
        continue
    render_plot(folder_name, annotation, run1, run2)
