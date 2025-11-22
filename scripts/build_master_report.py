#!/usr/bin/env python3
"""
Assemble a master markdown report combining the global summary, user-supplied summary,
and per-gene-set sections referencing bubble plots and run reports.
"""
from __future__ import annotations

from pathlib import Path
import json
import os
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
ANALYSIS_REPORT = BASE_DIR / "reports" / "deepsearch_report.md"
SUMMARY_SNIPPET = BASE_DIR / "reports" / "summary_intro.md"
MASTER_REPORT = BASE_DIR / "reports" / "master_report.md"
BUBBLE_DIR = BASE_DIR / "analysis" / "confusion_heatmaps"
RUN_REPORT_ROOT = BASE_DIR / "reports"
DATA_DIR = BASE_DIR / "data"


def load_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""

def load_duplicate_rows():
    dup_path = DATA_DIR / "deepsearch_duplicate_runs.csv"
    if dup_path.exists():
        df = pd.read_csv(dup_path)
        return df[df["duplicate"]]
    return pd.DataFrame(columns=["folder","annotation","duplicate"])

def main() -> None:
    content = []
    if SUMMARY_SNIPPET.exists():
        content.append(load_text(SUMMARY_SNIPPET).strip())
        content.append("")
    else:
        content.append("<!-- TODO: insert summary by editing reports/summary_intro.md -->")
        content.append("")
    content.append(load_text(ANALYSIS_REPORT).strip())
    content.append("")
    duplicate_rows = load_duplicate_rows()
    duplicate_folders = set(duplicate_rows["folder"].tolist())
    name_only = pd.read_csv(DATA_DIR / "deepsearch_runs.csv")[
        ["folder", "annotation", "run_index", "program_signature"]
    ]
    if not duplicate_rows.empty:
        content.append("## Duplicated runs")
        for _, row in duplicate_rows.iterrows():
            content.append(
                f"- {row['annotation']} ({row['folder']}): DeepSearch runs are identical; only run_1 is shown."
            )
        content.append("")
    matches = pd.read_csv(DATA_DIR / "deepsearch_program_matches.csv")
    run_counts = pd.read_csv(DATA_DIR / "deepsearch_runs.csv").pivot(
        index="folder", columns="run_index", values="program_count"
    )
    program_catalog = pd.read_csv(
        DATA_DIR / "deepsearch_programs.csv",
        usecols=["folder", "run_index", "program_index", "program_name", "supporting_genes"],
    )

    def parse_genes(cell: str):
        if isinstance(cell, float) and pd.isna(cell):
            return []
        if not cell:
            return []
        try:
            return json.loads(cell)
        except json.JSONDecodeError:
            return []

    program_catalog["gene_set"] = program_catalog["supporting_genes"].apply(parse_genes)
    gene_lookup = {
        (row.folder, int(row.run_index), int(row.program_index)): set(row.gene_set)
        for row in program_catalog.itertuples(index=False)
    }

    def overlap_genes(folder_name: str, run_a: int, idx_a: int, run_b: int, idx_b: int) -> int:
        genes_a = gene_lookup.get((folder_name, run_a, idx_a), set())
        genes_b = gene_lookup.get((folder_name, run_b, idx_b), set())
        return len(genes_a & genes_b)
    report_folders = sorted((BASE_DIR / "reports").glob('[0-9][0-9]_*/'))
    for folder in report_folders:
        bubble = BUBBLE_DIR / f"{folder.name}_bubble.png"
        run_dir = RUN_REPORT_ROOT / folder.name
        run_links = []
        for idx in (1, 2):
            report_path = run_dir / f"run_{idx}.md"
            if report_path.exists():
                rel_path = report_path.relative_to(MASTER_REPORT.parent)
                run_links.append(f"[Run {idx}]({rel_path.as_posix()})")
        if not run_links and not bubble.exists():
            continue
        content.append(f"## {folder.name}")
        content.append("")
        
        folder_matches = matches[matches["folder"] == folder.name]
        if folder.name in duplicate_folders:
            content.append("_Duplicate run outputs; see run_1 report only._")
            content.append("")
            if run_links:
                run_links = [link for link in run_links if "Run 1" in link]
            content.append("Top matches: _skipped due to duplicate runs_")
            content.append("")
        else:
            try:
                counts = run_counts.loc[folder.name]
                count_run1 = counts.get(1, 0)
                count_run2 = counts.get(2, 0)
            except KeyError:
                count_run1 = count_run2 = 0
            smaller_idx = 1 if count_run1 <= count_run2 else 2
            catalog_subset = (
                program_catalog[
                    (program_catalog["folder"] == folder.name)
                    & (program_catalog["run_index"] == smaller_idx)
                ]
                .sort_values("program_index")
            )
            folder_matches = matches[matches["folder"] == folder.name]
            table_rows = []
            if smaller_idx == 1:
                best_idx = folder_matches.groupby("program_a_index")[
                    "combined_similarity"
                ].idxmax()
                best_rows = folder_matches.loc[best_idx]
                best_map = {
                    row["program_a_index"]: row for _, row in best_rows.iterrows()
                }
                for _, prog_row in catalog_subset.iterrows():
                    prog_idx = int(prog_row["program_index"])
                    match_row = best_map.get(prog_idx)
                    if match_row is None:
                        table_rows.append(
                            {
                                "small_name": prog_row["program_name"],
                                "other_name": "(no match)",
                                "overlap": "-",
                                "gene": "-",
                                "name": "-",
                                "combined": "-",
                                "combined_val": -1.0,
                            }
                        )
                    else:
                        overlap = overlap_genes(
                            folder.name,
                            1,
                            prog_idx,
                            2,
                            int(match_row["program_b_index"]),
                        )
                        table_rows.append(
                            {
                                "small_name": prog_row["program_name"],
                                "other_name": match_row["program_b_name"],
                                "overlap": str(overlap),
                                "gene": f"{match_row['gene_jaccard']:.2f}",
                                "name": f"{match_row['name_similarity']:.2f}",
                                "combined": f"{match_row['combined_similarity']:.2f}",
                                "combined_val": match_row["combined_similarity"],
                            }
                        )
            else:
                best_idx = folder_matches.groupby("program_b_index")[
                    "combined_similarity"
                ].idxmax()
                best_rows = folder_matches.loc[best_idx]
                best_map = {
                    row["program_b_index"]: row for _, row in best_rows.iterrows()
                }
                for _, prog_row in catalog_subset.iterrows():
                    prog_idx = int(prog_row["program_index"])
                    match_row = best_map.get(prog_idx)
                    if match_row is None:
                        table_rows.append(
                            {
                                "small_name": prog_row["program_name"],
                                "other_name": "(no match)",
                                "overlap": "-",
                                "gene": "-",
                                "name": "-",
                                "combined": "-",
                                "combined_val": -1.0,
                            }
                        )
                    else:
                        overlap = overlap_genes(
                            folder.name,
                            2,
                            prog_idx,
                            1,
                            int(match_row["program_a_index"]),
                        )
                        table_rows.append(
                            {
                                "small_name": prog_row["program_name"],
                                "other_name": match_row["program_a_name"],
                                "overlap": str(overlap),
                                "gene": f"{match_row['gene_jaccard']:.2f}",
                                "name": f"{match_row['name_similarity']:.2f}",
                                "combined": f"{match_row['combined_similarity']:.2f}",
                                "combined_val": match_row["combined_similarity"],
                            }
                        )
            if table_rows:
                table_rows.sort(key=lambda row: row["combined_val"], reverse=True)
                content.append(
                    "| Run 1 program | Run 2 program | Overlap genes | Gene Jaccard | Name overlap | Combined |"
                )
                content.append("| --- | --- | --- | --- | --- | --- |")
                for row in table_rows:
                    content.append(
                        f"| {row['small_name']} | {row['other_name']} | {row['overlap']} | {row['gene']} | {row['name']} | {row['combined']} |"
                    )
                content.append("")
        
        if bubble.exists():
            rel_img = Path(os.path.relpath(bubble, MASTER_REPORT.parent))
            content.append(f"![{folder.name} overlap plot]({rel_img.as_posix()})")
            content.append("")
        if run_links:
            content.append("Reports: " + " | ".join(run_links))
            content.append("")
    MASTER_REPORT.write_text("\n".join(content).strip() + "\n")
    print(f"Master report written to {MASTER_REPORT}")


if __name__ == "__main__":
    main()
