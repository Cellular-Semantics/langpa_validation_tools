import json

import numpy as np
import pytest

from src import process_deepsearch as pdh


def test_extract_json_block_simple():
    text = "prefix {\"context\": {}} suffix"
    assert pdh.extract_json_block(text) == '{"context": {}}'


def test_compute_signature_stable():
    sig1 = pdh.compute_signature([{"a": 1, "b": 2}])
    sig2 = pdh.compute_signature([{"b": 2, "a": 1}])
    assert sig1 == sig2


def test_rescale_name_similarity_with_baseline():
    assert pdh.rescale_name_similarity(0.4, 0.2) == pytest.approx((0.4 - 0.2) / (1 - 0.2))


def test_compute_name_similarity_tokens():
    sim = pdh.compute_name_similarity("Astrocyte Program", "astrocyte program")
    assert sim == 1.0
    sim2 = pdh.compute_name_similarity("Astrocyte Program", "Neuronal")
    assert sim2 == 0.0


def test_compute_program_similarity_without_embeddings():
    prog_a = {"program_name": "A", "supporting_genes": ["G1", "G2"]}
    prog_b = {"program_name": "A Program", "supporting_genes": ["G2", "G3"]}
    sim = pdh.compute_program_similarity(prog_a, prog_b, embeddings={}, folder="f", name_baseline=None)
    assert 0 < sim["gene_jaccard"] < 1
    assert sim["combined_similarity"] >= sim["gene_jaccard"] * 0.5


def test_compute_program_similarity_with_embeddings():
    vec = np.array([1.0, 0.0])
    embeddings = {("f", None, None): vec / np.linalg.norm(vec)}
    prog_a = {"program_name": "A", "supporting_genes": ["G1"], "_run_index": None, "_program_index": None}
    prog_b = {"program_name": "B", "supporting_genes": ["G1"], "_run_index": None, "_program_index": None}
    sim = pdh.compute_program_similarity(prog_a, prog_b, embeddings=embeddings, folder="f", name_baseline=0.0)
    assert sim["name_similarity"] == pytest.approx(1.0)


def test_sanitize_whitespace():
    assert pdh.sanitize_whitespace(" a   b\n c \t") == "a b c"
