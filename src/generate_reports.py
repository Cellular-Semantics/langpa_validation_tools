#!/usr/bin/env python3
"""
Generate human-readable markdown reports for each DeepSearch run.
Reports include program summaries, citations, and GO comparison tables.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

import re
import sys

import pandas as pd
from .process_deepsearch import parse_run  # type: ignore
from .project_paths import add_project_argument, resolve_paths


def load_run_markdown(run_file: Path) -> Dict:
    return parse_run(run_file)


def extract_numeric_citations(text: str) -> Dict[str, str]:
    """Parse simple numeric citation list: '1. http://...\\n2. http://...'. Return id->url."""
    pattern = re.compile(r"^\\s*(\\d+)\\.\\s*(\\S+)", re.MULTILINE)
    return {m.group(1): m.group(2) for m in pattern.finditer(text)}


def build_citation_map(programs: List[Dict], fallback_urls: Dict[str, str]) -> Dict[str, Dict]:
    """Return a dict of source_id -> citation info."""
    citation_map: Dict[str, Dict] = {}
    for program in programs:
        if not isinstance(program, dict):
            continue
        for section in ("citations", "atomic_biological_processes", "atomic_cellular_components"):
            entries = program.get(section) or []
            for entry in entries:
                if isinstance(entry, dict):
                    cits = entry.get("citation") if section.startswith("atomic") else [entry]
                elif isinstance(entry, str):
                    # support simple "1. url" style strings
                    match = re.match(r"\\s*(\\d+)\\.\\s*(\\S+)", entry)
                    if match:
                        cits = [{"source_id": match.group(1), "url": match.group(2)}]
                    else:
                        cits = []
                else:
                    cits = []
                if cits is None:
                    cits = []
                for cit in cits:
                    source_id = (
                        str(cit.get("source_id")).strip() if cit.get("source_id") is not None else ""
                    )
                    if not source_id:
                        continue
                    entry_map = citation_map.setdefault(
                        source_id,
                        {"notes": [], "url": (cit.get("url") or fallback_urls.get(source_id, "")).strip()},
                    )
                    note = cit.get("notes", "").strip()
                    if note:
                        entry_map["notes"].append(note)
                    if cit.get("url") and not entry_map["url"]:
                        entry_map["url"] = cit["url"]
                    if not entry_map["url"] and source_id in fallback_urls:
                        entry_map["url"] = fallback_urls[source_id]
    return citation_map


def format_atomic_section(title: str, entries: List[Dict]) -> List[str]:
    lines = [f"**{title}:**"]
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name", "")
        genes = entry.get("genes") or []
        cits = entry.get("citation") or []
        cite_ids = [str(c.get("source_id")).strip() for c in cits if c.get("source_id")]
        cite_str = f" (refs: {', '.join(f'[{cid}]' for cid in cite_ids)})" if cite_ids else ""
        lines.append(f"- {name}: {', '.join(genes)}{cite_str}")
    return lines


def render_program(program: Dict) -> str:
    lines = []
    name = program.get("program_name", "Unnamed Program")
    description = program.get("description", "")
    impacts = program.get("predicted_cellular_impact") or []
    genes = program.get("supporting_genes") or []
    lines.append(f"### {name}")
    if description:
        lines.append(description)
    if impacts:
        lines.append("")
        lines.append("**Predicted impacts:**")
        lines.extend([f"- {impact}" for impact in impacts])
    if genes:
        lines.append("")
        lines.append("**Supporting genes:** " + ", ".join(genes))
    citations = program.get("citations") or []
    if citations:
        cite_ids = sorted({str(c.get("source_id")).strip() for c in citations if c.get("source_id")})
        if cite_ids:
            lines.append("")
            lines.append("**References:** " + ", ".join(f"[{cid}]" for cid in cite_ids))
    atomic_bio = program.get("atomic_biological_processes") or []
    if atomic_bio:
        lines.append("")
        lines.extend(format_atomic_section("Biological processes", atomic_bio))
    atomic_cell = program.get("atomic_cellular_components") or []
    if atomic_cell:
        lines.append("")
        lines.extend(format_atomic_section("Cellular components", atomic_cell))
    if citations:
        note_lines = [
            c.get("notes", "").strip()
            for c in citations
            if c.get("source_id") and c.get("notes")
        ]
        if note_lines:
            lines.append("")
            lines.append("**Reference notes:**")
            for note in note_lines:
                lines.append(f"- {note}")
    return "\n".join(lines)


def load_go_tables(data_dir: Path) -> Dict[str, Dict]:
    table_path = data_dir / "comparison_table_rows.csv"
    if not table_path.exists() or table_path.stat().st_size == 0:
        print(f"Warning: no comparison table rows found at {table_path}; GO sections will be skipped.")
        return {}
    try:
        table_rows = pd.read_csv(table_path)
    except pd.errors.EmptyDataError:
        print(f"Warning: empty comparison table at {table_path}; GO sections will be skipped.")
        return {}
    unmatched_path = data_dir / "comparison_unmatched_go_terms.csv"
    if unmatched_path.exists() and unmatched_path.stat().st_size > 0:
        try:
            unmatched = pd.read_csv(unmatched_path)
        except pd.errors.EmptyDataError:
            unmatched = pd.DataFrame(columns=["folder", "gsea_term"])
    else:
        unmatched = pd.DataFrame(columns=["folder", "gsea_term"])
    go_map: Dict[str, Dict] = {}
    for folder, group in table_rows.groupby("folder"):
        go_map.setdefault(folder, {})
        go_map[folder]["table"] = group
    for folder, group in unmatched.groupby("folder"):
        go_map.setdefault(folder, {})
        go_map[folder]["unmatched"] = group
    return go_map


def generate_reports(project: str) -> None:
    paths = resolve_paths(project)
    paths.ensure_output_dirs()
    go_tables = load_go_tables(paths.data_dir)
    mapping = pd.read_csv(paths.mapping_file)

    for _, row in mapping.iterrows():
        folder = paths.deepsearch_dir / row["new_folder"]
        run_files = sorted(folder.glob("*.md"))
        if len(run_files) != 2:
            continue
        for idx, run_file in enumerate(run_files, start=1):
            try:
                raw_text = run_file.read_text()
                data = load_run_markdown(run_file)
            except Exception as exc:  # noqa: BLE001
                print(f"Warning: skipping malformed run file {run_file} ({exc})", file=sys.stderr)
                continue
            programs = data.get("programs", [])
            fallback_urls = extract_numeric_citations(raw_text)
            citation_map = build_citation_map(programs, fallback_urls)
            if not citation_map:
                print(f"Skipping {run_file} due to missing citation source_ids.")
                continue
            folder_out = paths.reports_dir / folder.name
            folder_out.mkdir(parents=True, exist_ok=True)
            out_file = folder_out / f"{run_file.stem}.md"
            ctx = data.get("context", {})
            lines = [
                f"# Report: {folder.name} ({run_file.name})",
                "",
                f"**Cell type:** {ctx.get('cell_type', '')}",
                f"**Disease:** {ctx.get('disease', '')}",
                f"**Tissue:** {ctx.get('tissue', '')}",
                "",
                "## Program Summaries",
            ]
            for program in programs:
                lines.append(render_program(program))
                lines.append("")
            folder_go = go_tables.get(folder.name)
            if folder_go:
                lines.append("## GO Comparison")
                table = folder_go.get("table")
                if table is not None and not table.empty:
                    lines.append("| Program | Similar GO term(s) | Novel aspects |")
                    lines.append("| --- | --- | --- |")
                    for _, row_t in table.iterrows():
                        lines.append(
                            f"| {row_t.get('program_name','')} | "
                            f"{row_t.get('similar_terms_raw','')} | "
                            f"{row_t.get('novel_aspects','')} |"
                        )
                unmatched = folder_go.get("unmatched")
                if unmatched is not None and not unmatched.empty:
                    lines.append("")
                    lines.append("**GO terms not reflected:**")
                    for _, row_u in unmatched.iterrows():
                        lines.append(f"- {row_u.get('gsea_term','')}")
                lines.append("")
            lines.append("## References")
            for cid in sorted(citation_map):
                entry = citation_map[cid]
                notes = entry["notes"]
                url = entry["url"]
                parts = []
                if url:
                    parts.append(url)
                if notes:
                    parts.append("Notes: " + " | ".join(notes))
                reference_line = f"- [{cid}] " + "; ".join(parts)
                lines.append(reference_line.strip())
            out_file.write_text("\n".join(lines).strip() + "\n")
            print(f"Wrote {out_file.relative_to(paths.base_dir)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate per-run reports for a project.")
    add_project_argument(parser)
    args = parser.parse_args()
    generate_reports(args.project)
