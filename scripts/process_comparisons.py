#!/usr/bin/env python3
"""
Parse comparison markdown files aligning DeepSearch programs with GO enrichment results.
Generates structured CSVs capturing program-level mappings and coverage summaries.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
COMPARISON_DIR = BASE_DIR / "Comparisons"
MAPPING_FILE = BASE_DIR / "geneset_folder_mapping.csv"
S10_FILE = BASE_DIR / "media-3 (2).xlsx"

sys.path.append(str(Path(__file__).resolve().parent))
from process_deepsearch import parse_run  # noqa: E402

GO_REGEX = re.compile(r"[^,;]+?\(GO:\d+\)")


def extract_go_terms(text: str) -> List[str]:
    """Extract GO-style terms that include GO identifiers."""
    terms = [term.strip() for term in GO_REGEX.findall(text or "") if term.strip()]
    return terms


def normalize_term(term: str) -> str:
    return term.split("(GO")[0].strip()


def split_gene_set_id(name: str) -> int:
    match = re.search(r"geneset_(\d+)", name)
    if not match:
        raise ValueError(f"Unable to parse geneset id from {name}")
    return int(match.group(1))


def parse_program_table(text: str) -> List[Tuple[str, str, str]]:
    """Return list of (program_name, similar_terms, novel_text)."""
    rows: List[Tuple[str, str, str]] = []
    capture = False
    for line in text.splitlines():
        if line.startswith("|") and "DeepSearch" in line and "Program" in line:
            capture = True
            continue
        if capture:
            if not line.strip():
                break
            if line.startswith("|---"):
                continue
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) >= 4:
                    rows.append((cells[0], cells[2], cells[3]))
                elif len(cells) >= 3:
                    rows.append((cells[0], cells[1], cells[2]))
    return rows


def parse_unmatched_go_terms(text: str) -> List[str]:
    """Extract GO terms not reflected in DeepSearch if explicitly listed."""
    lines = text.splitlines()
    terms: List[str] = []
    capture = False
    for line in lines:
        if "GO enrichment term" in line and "NOT" in line:
            capture = True
            continue
        if capture:
            stripped = line.strip()
            if not stripped or stripped.startswith("<") or stripped.startswith("["):
                break
            if stripped.startswith("-"):
                candidate = stripped.lstrip("- ").strip()
                if candidate:
                    terms.append(candidate)
    if terms:
        return terms
    # handle table format (e.g., columns GO Term | Status | Reason)
    table_rows = []
    capture_table = False
    for line in lines:
        if line.startswith("|") and "GO Term" in line and "Status" in line:
            capture_table = True
            continue
        if capture_table:
            if not line.strip():
                break
            if line.startswith("|---"):
                continue
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if cells:
                    table_rows.append(cells)
    for cells in table_rows:
        if cells and "(" in cells[0]:
            terms.append(cells[0])
    return terms


def parse_unmatched_count(text: str) -> int | None:
    match = re.search(r"GSEA Terms NOT [^()]*\((\d+)\s+terms", text)
    if match:
        return int(match.group(1))
    return None


def ingest_file(
    file_path: Path,
    mapping_row: pd.Series,
    gsea_terms: List[str],
) -> Dict[str, List[Dict]]:
    text = file_path.read_text()
    data = parse_run(file_path)
    programs = [prog for prog in data.get("programs", []) if isinstance(prog, dict)]
    program_map = {prog.get("program_name"): prog for prog in programs}

    table_entries = parse_program_table(text)
    if not table_entries:
        raise ValueError(f"No DeepSearch comparison table found in {file_path.name}")

    normalized_terms = {
        term: {term.lower(), normalize_term(term).lower()}
        for term in gsea_terms
    }

    table_records: List[Dict] = []
    program_term_records: List[Dict] = []
    unmatched_program_records: List[Dict] = []

    for program_name, similar_text, novel_text in table_entries:
        if not program_name or program_name in {":--", "--"}:
            continue
        info = program_map.get(program_name)
        gene_count = len(info.get("supporting_genes", [])) if info else None
        similar_lower = similar_text.lower()
        matched_terms = []
        matched_flag = False
        numeric_match = False
        try:
            numeric_match = float(similar_text) > 0
        except (ValueError, TypeError):
            numeric_match = False
        if numeric_match:
            matched_flag = True
        elif similar_text and similar_lower not in {
            "none",
            "none matched directly",
            "n/a",
            "na",
            "-",
            "[none]",
        }:
            for term, variants in normalized_terms.items():
                if any(variant and variant in similar_lower for variant in variants):
                    matched_terms.append(term)
            if matched_terms:
                matched_flag = True
        table_records.append(
            {
                "metamodule": mapping_row["metamodule"],
                "annotation": mapping_row["annotation"],
                "folder": mapping_row["new_folder"],
                "source_file": file_path.name,
                "program_name": program_name,
                "similar_terms_raw": similar_text,
                "novel_aspects": novel_text,
                "matched_term_count": len(set(matched_terms)) if matched_terms else (1 if matched_flag else 0),
                "supporting_gene_count": gene_count,
            }
        )
        if matched_terms:
            for term in set(matched_terms):
                program_term_records.append(
                    {
                        "metamodule": mapping_row["metamodule"],
                        "annotation": mapping_row["annotation"],
                        "folder": mapping_row["new_folder"],
                        "source_file": file_path.name,
                        "program_name": program_name,
                        "gsea_term": term,
                    }
                )
        elif not matched_flag:
            unmatched_program_records.append(
                {
                    "metamodule": mapping_row["metamodule"],
                    "annotation": mapping_row["annotation"],
                    "folder": mapping_row["new_folder"],
                    "source_file": file_path.name,
                    "program_name": program_name,
                    "supporting_gene_count": gene_count,
                }
            )

    unmatched_terms = parse_unmatched_go_terms(text)
    unmatched_count = len(unmatched_terms)
    if unmatched_count == 0:
        inferred = parse_unmatched_count(text)
        if inferred is not None:
            unmatched_count = inferred

    unmatched_term_records = [
        {
            "metamodule": mapping_row["metamodule"],
            "annotation": mapping_row["annotation"],
            "folder": mapping_row["new_folder"],
            "source_file": file_path.name,
            "gsea_term": term,
        }
        for term in unmatched_terms
    ]

    summary_record = {
        "metamodule": mapping_row["metamodule"],
        "annotation": mapping_row["annotation"],
        "folder": mapping_row["new_folder"],
        "source_file": file_path.name,
        "total_gsea_terms": len(gsea_terms),
        "unmatched_go_terms_reported": unmatched_count,
        "unmatched_go_terms_listed": len(unmatched_terms),
        "matched_go_terms_estimated": max(len(gsea_terms) - unmatched_count, 0),
        "programs_total": len(table_entries),
        "programs_without_go_match": len(unmatched_program_records),
    }

    return {
        "table": table_records,
        "program_term": program_term_records,
        "unmatched_programs": unmatched_program_records,
        "unmatched_go_terms": unmatched_term_records,
        "summary": summary_record,
    }


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    mapping = pd.read_csv(MAPPING_FILE)
    table_s10 = pd.read_excel(S10_FILE, sheet_name="Table S10")

    all_table_rows: List[Dict] = []
    all_program_terms: List[Dict] = []
    all_unmatched_programs: List[Dict] = []
    all_unmatched_go_terms: List[Dict] = []
    summary_rows: List[Dict] = []

    for file in sorted(COMPARISON_DIR.glob("comparison geneset_*.md")):
        gene_set_id = split_gene_set_id(file.name)
        metamodule = gene_set_id - 1
        mapping_row = mapping[mapping["metamodule"] == metamodule].iloc[0]
        s10_row = table_s10[table_s10["MetaModule"] == metamodule].iloc[0]
        gsea_terms = extract_go_terms(str(s10_row["Enriched Pathways"]))
        try:
            records = ingest_file(file, mapping_row, gsea_terms)
        except ValueError as exc:
            print(f"Skipping {file.name}: {exc}")
            continue
        all_table_rows.extend(records["table"])
        all_program_terms.extend(records["program_term"])
        all_unmatched_programs.extend(records["unmatched_programs"])
        all_unmatched_go_terms.extend(records["unmatched_go_terms"])
        summary_rows.append(records["summary"])

    pd.DataFrame(all_table_rows).to_csv(DATA_DIR / "comparison_table_rows.csv", index=False)
    pd.DataFrame(all_program_terms).to_csv(
        DATA_DIR / "comparison_program_term_matches.csv", index=False
    )
    pd.DataFrame(all_unmatched_programs).to_csv(
        DATA_DIR / "comparison_novel_programs.csv", index=False
    )
    pd.DataFrame(all_unmatched_go_terms).to_csv(
        DATA_DIR / "comparison_unmatched_go_terms.csv", index=False
    )
    pd.DataFrame(summary_rows).to_csv(DATA_DIR / "comparison_summary.csv", index=False)
    print("Parsed comparison markdown files.")


if __name__ == "__main__":
    main()
