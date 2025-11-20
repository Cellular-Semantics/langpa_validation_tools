#!/usr/bin/env python3
"""
Parse Perplexity DeepSearch run outputs, extract gene program metadata,
and compute similarity scores between paired runs for each metamodel.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MAPPING_FILE = BASE_DIR / "geneset_folder_mapping.csv"
DATA_DIR = BASE_DIR / "data"


def extract_json_block(text: str) -> str:
    """Return the JSON block containing the DeepSearch payload."""
    matches = list(re.finditer(r"\{\s*\"context\"\s*:", text))
    if not matches:
        raise ValueError("Unable to locate JSON payload.")
    start_idx = matches[-1].start()
    depth = 0
    in_string = False
    escape = False
    for idx in range(start_idx, len(text)):
        ch = text[idx]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start_idx : idx + 1]
    raise ValueError("JSON block not terminated properly.")


def parse_run(file_path: Path) -> Dict:
    """Parse a DeepSearch markdown file into a structured dict."""
    text = file_path.read_text()
    payload = extract_json_block(text)
    payload = re.sub(r'";\s*(?=[}\]])', '"', payload)
    payload = re.sub(r"\n\s*//.*", "", payload)
    payload = re.sub(r",(?=\s*[\]}])", "", payload)
    payload = re.sub(r"\[\^[^\]]+\]", "", payload)
    data = json.loads(payload)
    return data


def sanitize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def normalize_name(text: str) -> List[str]:
    """Return normalized tokens for a program name."""
    clean = re.sub(r"[^A-Za-z0-9]+", " ", text.lower())
    tokens = [tok for tok in clean.split() if tok]
    return tokens


def compute_name_similarity(name_a: str, name_b: str) -> float:
    tokens_a = set(normalize_name(name_a))
    tokens_b = set(normalize_name(name_b))
    if not tokens_a or not tokens_b:
        return 0.0
    union = len(tokens_a | tokens_b)
    return len(tokens_a & tokens_b) / union if union else 0.0


def compute_program_similarity(prog_a: Dict, prog_b: Dict) -> Dict:
    genes_a = set(prog_a.get("supporting_genes") or [])
    genes_b = set(prog_b.get("supporting_genes") or [])
    union = len(genes_a | genes_b)
    gene_jaccard = len(genes_a & genes_b) / union if union else 0.0
    name_a = prog_a.get("program_name", "") or ""
    name_b = prog_b.get("program_name", "") or ""
    name_sim = compute_name_similarity(name_a, name_b)
    combined = 0.5 * gene_jaccard + 0.5 * name_sim
    return {
        "gene_jaccard": gene_jaccard,
        "name_similarity": name_sim,
        "combined_similarity": combined,
    }


@dataclass
class ProgramRef:
    run_id: str
    program_idx: int


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    mapping = pd.read_csv(MAPPING_FILE)

    run_records: List[Dict] = []
    program_rows: List[Dict] = []
    match_rows: List[Dict] = []
    unmatched_rows: List[Dict] = []
    invalid_program_rows: List[Dict] = []

    for _, row in mapping.iterrows():
        folder = BASE_DIR / row["new_folder"]
        meta = int(row["metamodule"])
        annotation = row["annotation"]
        run_files = sorted(folder.glob("*.md"))
        if len(run_files) != 2:
            raise RuntimeError(f"Expected 2 run files in {folder}, found {len(run_files)}.")

        run_payloads: List[Dict] = []
        for idx, file in enumerate(run_files, start=1):
            try:
                data = parse_run(file)
            except Exception as exc:  # noqa: BLE001
                raise RuntimeError(f"Failed parsing {file}") from exc
            run_id = f"{folder.name}_run{idx}"
            run_records.append(
                {
                    "metamodule": meta,
                    "annotation": annotation,
                    "folder": folder.name,
                    "run_index": idx,
                    "run_file": file.name,
                    "run_id": run_id,
                    "program_count": len(data.get("programs", [])),
                }
            )
            raw_programs = data.get("programs", [])
            program_list = []
            for p_idx, entry in enumerate(raw_programs):
                if not isinstance(entry, dict):
                    invalid_program_rows.append(
                        {
                            "run_id": run_id,
                            "metamodule": meta,
                            "annotation": annotation,
                            "folder": folder.name,
                            "run_index": idx,
                            "program_index": p_idx,
                            "raw_entry": str(entry),
                        }
                    )
                    continue
                program = dict(entry)
                program["_parsed_index"] = p_idx
                program_list.append(program)
                program_rows.append(
                    {
                        "run_id": run_id,
                        "metamodule": meta,
                        "annotation": annotation,
                        "folder": folder.name,
                        "run_index": idx,
                        "program_index": p_idx,
                        "program_name": program.get("program_name"),
                        "description": sanitize_whitespace(
                            program.get("description", "")
                        ),
                        "supporting_genes": json.dumps(
                            program.get("supporting_genes") or []
                        ),
                        "supporting_gene_count": len(program.get("supporting_genes") or []),
                        "significance_score": program.get("significance_score"),
                        "predicted_impacts": json.dumps(
                            program.get("predicted_cellular_impact") or []
                        ),
                    }
                )
            run_payloads.append({"id": run_id, "programs": program_list})

        # compute similarities between the two runs
        run_a, run_b = run_payloads
        similarities = []
        for prog_a in run_a["programs"]:
            idx_a = prog_a.get("_parsed_index")
            for prog_b in run_b["programs"]:
                idx_b = prog_b.get("_parsed_index")
                sim = compute_program_similarity(prog_a, prog_b)
                similarities.append(
                    {
                        "run_a_id": run_a["id"],
                        "run_b_id": run_b["id"],
                        "program_a_index": idx_a,
                        "program_b_index": idx_b,
                        "program_a_name": prog_a.get("program_name"),
                        "program_b_name": prog_b.get("program_name"),
                        "gene_jaccard": sim["gene_jaccard"],
                        "name_similarity": sim["name_similarity"],
                        "combined_similarity": sim["combined_similarity"],
                        "folder": folder.name,
                        "metamodule": meta,
                        "annotation": annotation,
                    }
                )

        similarities.sort(key=lambda item: item["combined_similarity"], reverse=True)
        matched_a: set = set()
        matched_b: set = set()
        min_threshold = 0.15
        for candidate in similarities:
            a_idx = candidate["program_a_index"]
            b_idx = candidate["program_b_index"]
            if (
                candidate["combined_similarity"] < min_threshold
                or a_idx in matched_a
                or b_idx in matched_b
            ):
                continue
            matched_a.add(a_idx)
            matched_b.add(b_idx)
            match_rows.append(candidate)

        # collect unmatched program references
        for prog in run_a["programs"]:
            idx_a = prog.get("_parsed_index")
            if idx_a not in matched_a:
                unmatched_rows.append(
                    {
                        "run_id": run_a["id"],
                        "program_index": idx_a,
                        "program_name": prog.get("program_name"),
                        "folder": folder.name,
                        "metamodule": meta,
                        "annotation": annotation,
                    }
                )
        for prog in run_b["programs"]:
            idx_b = prog.get("_parsed_index")
            if idx_b not in matched_b:
                unmatched_rows.append(
                    {
                        "run_id": run_b["id"],
                        "program_index": idx_b,
                        "program_name": prog.get("program_name"),
                        "folder": folder.name,
                        "metamodule": meta,
                        "annotation": annotation,
                    }
                )

    pd.DataFrame(run_records).to_csv(DATA_DIR / "deepsearch_runs.csv", index=False)
    pd.DataFrame(program_rows).to_csv(DATA_DIR / "deepsearch_programs.csv", index=False)
    pd.DataFrame(match_rows).to_csv(DATA_DIR / "deepsearch_program_matches.csv", index=False)
    pd.DataFrame(unmatched_rows).to_csv(DATA_DIR / "deepsearch_unmatched_programs.csv", index=False)
    if invalid_program_rows:
        pd.DataFrame(invalid_program_rows).to_csv(
            DATA_DIR / "deepsearch_invalid_program_entries.csv", index=False
        )
    print("Processed DeepSearch runs and wrote CSV outputs in data/.")


if __name__ == "__main__":
    main()
