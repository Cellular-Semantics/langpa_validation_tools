#!/usr/bin/env python3
"""
Assemble a master markdown report combining the global summary, user-supplied summary,
and per-gene-set sections referencing bubble plots and run reports for a project.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import pandas as pd

from .project_paths import add_project_argument, resolve_paths


def load_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def load_duplicate_rows(data_dir: Path) -> pd.DataFrame:
    dup_path = data_dir / "deepsearch_duplicate_runs.csv"
    if dup_path.exists():
        df = pd.read_csv(dup_path)
        return df[df["duplicate"]]
    return pd.DataFrame(columns=["folder", "annotation", "duplicate"])


def parse_genes(cell: str):
    if isinstance(cell, float) and pd.isna(cell):
        return []
    if not cell:
        return []
    try:
        return json.loads(cell)
    except json.JSONDecodeError:
        return []


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Build master report for a project.")
    add_project_argument(parser)
    args = parser.parse_args(argv)
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()

    analysis_report = paths.reports_dir / "deepsearch_report.md"
    summary_snippet = paths.reports_dir / "summary_intro.md"
    master_report = paths.reports_dir / "master_report.md"
    bubble_dir = paths.analysis_dir / "confusion_heatmaps"
    run_report_root = paths.reports_dir
    data_dir = paths.data_dir

    content: list[str] = []
    if summary_snippet.exists():
        content.append(load_text(summary_snippet).strip())
        content.append("")
    else:
        content.append("<!-- TODO: insert summary by editing reports/summary_intro.md -->")
        content.append("")
    analysis_text = load_text(analysis_report).strip()
    # rewrite analysis asset paths to include project subdir
    analysis_text = analysis_text.replace("analysis/", f"analysis/{paths.project}/")
    content.append(analysis_text)
    content.append("")
    duplicate_rows = load_duplicate_rows(data_dir)
    duplicate_folders = set(duplicate_rows["folder"].tolist())
    if not duplicate_rows.empty:
        content.append("## Duplicated runs")
        for _, row in duplicate_rows.iterrows():
            content.append(
                f"- {row['annotation']} ({row['folder']}): DeepSearch runs are identical; only run_1 is shown."
            )
        content.append("")
    matches = pd.read_csv(data_dir / "deepsearch_program_matches.csv")
    run_counts = pd.read_csv(data_dir / "deepsearch_runs.csv").pivot(
        index="folder", columns="run_index", values="program_count"
    )
    program_catalog = pd.read_csv(
        data_dir / "deepsearch_programs.csv",
        usecols=["folder", "run_index", "program_index", "program_name", "supporting_genes"],
    )
    component_map = pd.read_csv(data_dir / "component_mapping.csv")
    component_matches = pd.read_csv(data_dir / "component_program_matches.csv")

    program_catalog["gene_set"] = program_catalog["supporting_genes"].apply(parse_genes)
    gene_lookup = {
        (row.folder, int(row.run_index), int(row.program_index)): set(row.gene_set)
        for row in program_catalog.itertuples(index=False)
    }

    def overlap_genes(folder_name: str, run_a: int, idx_a: int, run_b: int, idx_b: int) -> int:
        genes_a = gene_lookup.get((folder_name, run_a, idx_a), set())
        genes_b = gene_lookup.get((folder_name, run_b, idx_b), set())
        return len(genes_a & genes_b)

    report_folders = sorted(run_report_root.glob("[0-9][0-9]_*/"))
    for folder in report_folders:
        bubble = bubble_dir / f"{folder.name}_bubble.png"
        run_dir = run_report_root / folder.name
        run_links = []
        for idx in (1, 2):
            report_path = run_dir / f"run_{idx}.md"
            if report_path.exists():
                rel_path = report_path.relative_to(master_report.parent)
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
            table_rows: list[dict] = []
            if smaller_idx == 1:
                best_idx = folder_matches.groupby("program_a_index")["combined_similarity"].idxmax()
                best_rows = folder_matches.loc[best_idx]
                best_map = {row["program_a_index"]: row for _, row in best_rows.iterrows()}
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
                        overlap = overlap_genes(folder.name, 1, prog_idx, 2, int(match_row["program_b_index"]))
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
                best_idx = folder_matches.groupby("program_b_index")["combined_similarity"].idxmax()
                best_rows = folder_matches.loc[best_idx]
                best_map = {row["program_b_index"]: row for _, row in best_rows.iterrows()}
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
                        overlap = overlap_genes(folder.name, 2, prog_idx, 1, int(match_row["program_a_index"]))
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

            table_rows = sorted(table_rows, key=lambda item: item.get("combined_val", -1.0), reverse=True)
            if table_rows:
                content.append("| Smaller set | Matched set | Gene overlap | Gene Jaccard | Name sim | Combined |")
                content.append("| --- | --- | --- | --- | --- | --- |")
                for row in table_rows:
                    content.append(
                        f"| {row['small_name']} | {row['other_name']} | {row['overlap']} | "
                        f"{row['gene']} | {row['name']} | {row['combined']} |"
                    )
                content.append("")
            else:
                content.append("_No program matches available._")
                content.append("")

            # component coverage table
            folder_components = component_map[component_map["folder"] == folder.name]
            folder_component_matches = component_matches[component_matches["folder"] == folder.name]
            if not folder_components.empty:
                content.append("**Component coverage:**")
                for _, comp_row in folder_components.iterrows():
                    matched_programs = folder_component_matches[
                        folder_component_matches["component_token"] == comp_row["component_token"]
                    ]["program_name"].unique()
                    programs_str = ", ".join(matched_programs) if len(matched_programs) else "(none)"
                    content.append(f"- {comp_row['component_token']}: {programs_str}")
        content.append("")

        if bubble.exists():
            rel_path = Path(os.path.relpath(bubble, master_report.parent))
            content.append(f"![Program similarity bubble plot]({rel_path.as_posix()})")
            content.append("")
        if run_links:
            content.append("Runs: " + " | ".join(run_links))
            content.append("")

    master_report.parent.mkdir(parents=True, exist_ok=True)
    master_report.write_text("\n".join(content).strip() + "\n")
    print(f"Wrote {master_report.relative_to(paths.base_dir)}")


if __name__ == "__main__":
    main()
