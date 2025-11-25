import os
from pathlib import Path

import pandas as pd

from src.generate_summary_figures import plot_run_consistency, plot_go_coverage


def test_plot_functions(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    out_dir = tmp_path / "analysis"
    data_dir.mkdir()
    out_dir.mkdir()

    # set writable matplotlib cache
    monkeypatch.setenv("MPLCONFIGDIR", str(tmp_path / ".mpl"))
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / ".cache"))

    pd.DataFrame(
        {
            "folder": ["f1", "f1"],
            "annotation": ["ann", "ann"],
            "gene_jaccard": [0.5, 0.6],
            "name_similarity": [0.4, 0.5],
            "combined_similarity": [0.45, 0.55],
        }
    ).to_csv(data_dir / "deepsearch_program_matches.csv", index=False)
    pd.DataFrame({"folder": ["f1"], "annotation": ["ann"], "duplicate": [False]}).to_csv(
        data_dir / "deepsearch_duplicate_runs.csv", index=False
    )

    plot_run_consistency(data_dir, out_dir)
    assert (out_dir / "run_consistency.svg").exists()

    pd.DataFrame(
        {"annotation": ["ann"], "matched_go_terms_estimated": [5], "total_gsea_terms": [10]}
    ).to_csv(data_dir / "comparison_summary.csv", index=False)
    plot_go_coverage(data_dir, out_dir)
    assert (out_dir / "go_coverage.svg").exists()
