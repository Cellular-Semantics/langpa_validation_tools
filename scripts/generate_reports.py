#!/usr/bin/env python3
"""
Generate human-readable markdown reports for each DeepSearch run.
Reports include program summaries, citations, and GO comparison tables.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd
from process_deepsearch import parse_run  # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent
RUN_ROOT = BASE_DIR / "deepsearch"
REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)


def load_run_markdown(run_file: Path) -> Dict:
    return parse_run(run_file)


def build_citation_map(programs: List[Dict]) -> Dict[str, Dict]:
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
                else:
                    cits = []
                for cit in cits:
                    source_id = (
                        str(cit.get("source_id")).strip() if cit.get("source_id") is not None else ""
                    )
                    if not source_id:
                        continue
                    entry = citation_map.setdefault(
                        source_id,
                        {"notes": [], "url": (cit.get("url") or "").strip()},
                    )
                    note = cit.get("notes", "").strip()
                    if note:
                        entry["notes"].append(note)
                    if cit.get("url") and not entry["url"]:
                        entry["url"] = cit["url"]
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


def load_go_tables() -> Dict[str, Dict]:
    table_rows = pd.read_csv(BASE_DIR / "data" / "comparison_table_rows.csv")
    unmatched_path = BASE_DIR / "data" / "comparison_unmatched_go_terms.csv"
    if unmatched_path.exists() and unmatched_path.stat().st_size > 0:
        try:
            unmatched = pd.read_csv(unmatched_path)
        except pd.errors.EmptyDataError:
            unmatched = pd.DataFrame(columns=["folder", "gsea_term"])
    else:
        unmatched = pd.DataFrame(columns=["folder", "gsea_term"])
    go_map = {}
    for folder, group in table_rows.groupby("folder"):
        go_map.setdefault(folder, {})
        go_map[folder]["table"] = group
    for folder, group in unmatched.groupby("folder"):
        go_map.setdefault(folder, {})
        go_map[folder]["unmatched"] = group
    return go_map


def generate_reports() -> None:
    go_tables = load_go_tables()
    mapping = pd.read_csv(BASE_DIR / "geneset_folder_mapping.csv")

    for _, row in mapping.iterrows():
        folder = RUN_ROOT / row["new_folder"]
        run_files = sorted(folder.glob("*.md"))
        if len(run_files) != 2:
            continue
        for idx, run_file in enumerate(run_files, start=1):
            data = load_run_markdown(run_file)
            programs = data.get("programs", [])
            citation_map = build_citation_map(programs)
            if not citation_map:
                print(f"Skipping {run_file} due to missing citation source_ids.")
                continue
            folder_out = REPORT_DIR / folder.name
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
            print(f"Wrote {out_file.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    generate_reports()
