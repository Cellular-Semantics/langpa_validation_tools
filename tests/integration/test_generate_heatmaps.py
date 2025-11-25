import json
import os
from pathlib import Path
import tempfile

import pandas as pd

from src.generate_heatmaps import generate_heatmaps
from src.project_paths import resolve_paths


def test_generate_heatmaps(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    project = "tmp_heatmap"
    paths = resolve_paths(project)
    paths.ensure_output_dirs()

    pd.DataFrame(
        {
            "folder": ["00_Test", "00_Test"],
            "annotation": ["Test", "Test"],
            "run_index": [1, 2],
            "program_index": [0, 0],
            "program_name": ["A", "B"],
            "supporting_genes": [json.dumps(["G1", "G2"]), json.dumps(["G2"])],
        }
    ).to_csv(paths.data_dir / "deepsearch_programs.csv", index=False)

    pd.DataFrame({"folder": ["00_Test"], "annotation": ["Test"], "duplicate": [False]}).to_csv(
        paths.data_dir / "deepsearch_duplicate_runs.csv", index=False
    )

    monkeypatch.setenv("MPLCONFIGDIR", str(tmp_path / ".mpl"))
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / ".cache"))

    generate_heatmaps(project)
    assert (paths.analysis_dir / "confusion_heatmaps" / "00_Test_bubble.png").exists()
