#!/usr/bin/env python3
"""
Parse Perplexity DeepSearch run outputs, extract gene program metadata,
and compute similarity scores between paired runs for each metamodel.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import hashlib
import os

import numpy as np
import pandas as pd

from .project_paths import add_project_argument, resolve_paths

USE_EMBEDDINGS = os.getenv("USE_EMBEDDINGS", "1") not in {"0", "false", "False"}


def compute_signature(programs: List[Dict]) -> str:
    canonical = json.dumps(programs, sort_keys=True, ensure_ascii=False)
    return hashlib.md5(canonical.encode("utf-8")).hexdigest()


def load_embeddings(index_path: Path, vector_path: Path, use_embeddings: bool) -> Dict[Tuple[str, int, int], np.ndarray]:
    if not use_embeddings or not index_path.exists() or not vector_path.exists():
        return {}
    index_df = pd.read_csv(index_path)
    vectors = np.load(vector_path)
    if len(index_df) != len(vectors):
        print("Embedding index and vector count mismatch; ignoring embeddings.")
        return {}
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    normalized = vectors / norms
    mapping: Dict[Tuple[str, int, int], np.ndarray] = {}
    for (folder, run_idx, prog_idx), vec in zip(
        zip(index_df["folder"], index_df["run_index"], index_df["program_index"]),
        normalized,
    ):
        mapping[(folder, int(run_idx), int(prog_idx))] = vec
    return mapping


def load_name_similarity_baseline(calibration_path: Path) -> Optional[float]:
    if not calibration_path.exists():
        return None
    try:
        data = json.loads(calibration_path.read_text())
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to read {calibration_path}: {exc}")
        return None
    mean_value = data.get("mean")
    try:
        return float(mean_value)
    except (TypeError, ValueError):
        return None


def rescale_name_similarity(raw_value: float, baseline: Optional[float]) -> float:
    if baseline is None:
        return raw_value
    denom = max(1e-6, 1.0 - baseline)
    scaled = (raw_value - baseline) / denom
    return max(-1.0, min(1.0, scaled))


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
    """Parse a DeepSearch markdown or JSON file into a structured dict."""
    if file_path.suffix.lower() == ".json":
        return json.loads(file_path.read_text())
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


def get_embedding(program: Dict, embeddings: Dict[tuple, np.ndarray], folder: str) -> np.ndarray | None:
    key = (folder, program.get("_run_index"), program.get("_program_index"))
    return embeddings.get(key)


def compute_program_similarity(
    prog_a: Dict,
    prog_b: Dict,
    embeddings: Dict[tuple, np.ndarray],
    folder: str,
    name_baseline: Optional[float],
) -> Dict:
    genes_a = set(prog_a.get("supporting_genes") or [])
    genes_b = set(prog_b.get("supporting_genes") or [])
    union = len(genes_a | genes_b)
    gene_jaccard = len(genes_a & genes_b) / union if union else 0.0
    vec_a = get_embedding(prog_a, embeddings, folder)
    vec_b = get_embedding(prog_b, embeddings, folder)
    if vec_a is not None and vec_b is not None:
        raw_name_sim = float(np.dot(vec_a, vec_b))
        name_sim = rescale_name_similarity(raw_name_sim, name_baseline)
    else:
        name_a = prog_a.get("program_name", "") or ""
        name_b = prog_b.get("program_name", "") or ""
        raw_name_sim = compute_name_similarity(name_a, name_b)
        name_sim = raw_name_sim
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Process DeepSearch runs for a project and compute run-pair similarities."
    )
    add_project_argument(parser)
    parser.add_argument(
        "--skip-bad",
        action="store_true",
        help="Skip malformed run markdown files instead of failing.",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    paths = resolve_paths(args.project)
    paths.ensure_output_dirs()
    if not paths.mapping_file.exists():
        raise FileNotFoundError(f"Mapping file not found for project '{paths.project}': {paths.mapping_file}")
    if not paths.deepsearch_dir.exists():
        raise FileNotFoundError(f"DeepSearch directory not found for project '{paths.project}': {paths.deepsearch_dir}")

    embed_index = paths.data_dir / "embeddings_index.csv"
    embed_vectors = paths.data_dir / "embeddings_name.npy"
    calibration_stats = paths.analysis_dir / "embedding_calibration_stats.json"

    embeddings = load_embeddings(embed_index, embed_vectors, USE_EMBEDDINGS)
    if USE_EMBEDDINGS and not embeddings:
        print("Embedding files not found or invalid; falling back to name token similarity.")
    name_baseline = load_name_similarity_baseline(calibration_stats)
    if name_baseline is None:
        print("Embedding calibration stats missing; name similarity will not be rescaled.")
    else:
        print(f"Using embedding baseline mean {name_baseline:.3f} for name similarity rescaling.")
    mapping = pd.read_csv(paths.mapping_file)

    run_records: List[Dict] = []
    program_rows: List[Dict] = []
    match_rows: List[Dict] = []
    unmatched_rows: List[Dict] = []
    invalid_program_rows: List[Dict] = []
    duplicate_rows: List[Dict] = []

    skipped_runs: List[Dict] = []

    for _, row in mapping.iterrows():
        folder = paths.deepsearch_dir / row["new_folder"]
        meta = int(row["metamodule"])
        annotation = row["annotation"]
        run_files = sorted(list(folder.glob("*.md")) + list(folder.glob("*.json")))
        if len(run_files) != 2:
            raise RuntimeError(f"Expected 2 run files in {folder}, found {len(run_files)}.")

        run_payloads: List[Dict] = []
        for idx, file in enumerate(run_files, start=1):
            try:
                data = parse_run(file)
            except Exception as exc:  # noqa: BLE001
                if args.skip_bad:
                    skipped_runs.append(
                        {
                            "folder": folder.name,
                            "run_file": file.name,
                            "error": str(exc),
                        }
                    )
                    print(f"Warning: skipping malformed run file {file} ({exc})", file=sys.stderr)
                    continue
                raise RuntimeError(f"Failed parsing {file}") from exc
            run_id = f"{folder.name}_run{idx}"
            signature = compute_signature(data.get("programs", []))
            run_records.append(
                {
                    "metamodule": meta,
                    "annotation": annotation,
                    "folder": folder.name,
                    "run_index": idx,
                    "run_file": file.name,
                    "run_id": run_id,
                    "program_count": len(data.get("programs", [])),
                    "program_signature": signature,
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
                program["_folder"] = folder.name
                program["_run_index"] = idx
                program["_program_index"] = p_idx
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
            run_payloads.append({"id": run_id, "programs": program_list, "signature": signature})

        # compute similarities between the two runs
        if len(run_payloads) != 2:
            if args.skip_bad:
                print(f"Warning: insufficient valid runs for {folder.name}; skipping similarity computation.", file=sys.stderr)
                continue
            raise RuntimeError(f"Insufficient valid runs for {folder.name}")

        run_a, run_b = run_payloads
        duplicate_pair = run_a.get("signature") == run_b.get("signature")
        duplicate_rows.append(
            {
                "folder": folder.name,
                "annotation": annotation,
                "duplicate": bool(duplicate_pair),
            }
        )
        if duplicate_pair:
            print(f"Warning: duplicate DeepSearch runs detected for {folder.name}")
        similarities = []
        for prog_a in run_a["programs"]:
            idx_a = prog_a.get("_parsed_index")
            for prog_b in run_b["programs"]:
                idx_b = prog_b.get("_parsed_index")
                sim = compute_program_similarity(
                    prog_a,
                    prog_b,
                    embeddings,
                    folder.name,
                    name_baseline,
                )
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

    pd.DataFrame(run_records).to_csv(paths.data_dir / "deepsearch_runs.csv", index=False)
    pd.DataFrame(program_rows).to_csv(paths.data_dir / "deepsearch_programs.csv", index=False)
    pd.DataFrame(match_rows).to_csv(paths.data_dir / "deepsearch_program_matches.csv", index=False)
    pd.DataFrame(unmatched_rows).to_csv(paths.data_dir / "deepsearch_unmatched_programs.csv", index=False)
    if invalid_program_rows:
        pd.DataFrame(invalid_program_rows).to_csv(
            paths.data_dir / "deepsearch_invalid_program_entries.csv", index=False
        )
    pd.DataFrame(duplicate_rows).to_csv(
        paths.data_dir / "deepsearch_duplicate_runs.csv", index=False
    )
    if skipped_runs:
        pd.DataFrame(skipped_runs).to_csv(paths.data_dir / "deepsearch_skipped_runs.csv", index=False)
        print(
            f"Skipped {len(skipped_runs)} malformed run files (see {paths.data_dir / 'deepsearch_skipped_runs.csv'}).",
            file=sys.stderr,
        )
    print(f"Processed DeepSearch runs for project '{paths.project}' and wrote CSV outputs in {paths.data_dir}.")


if __name__ == "__main__":
    main()
