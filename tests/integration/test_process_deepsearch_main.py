import json
from pathlib import Path

import pandas as pd

from src.process_deepsearch import main
from src.project_paths import resolve_paths


def write_run(path: Path, programs):
    payload = {"context": {}, "programs": programs}
    path.write_text("Prompt\n```json\n" + json.dumps(payload) + "\n```")


def test_process_deepsearch_main(tmp_path, monkeypatch):
    # Create fake project structure
    project = "tmp_proj"
    base = tmp_path
    monkeypatch.chdir(base)
    paths = resolve_paths(project)
    paths.ensure_output_dirs()
    deepsearch_dir = paths.deepsearch_dir
    deepsearch_dir.mkdir(parents=True, exist_ok=True)
    mapping = pd.DataFrame(
        {
            "metamodule": [0],
            "annotation": ["Test"],
            "original_folder": ["geneset_1"],
            "new_folder": ["00_Test"],
        }
    )
    mapping.to_csv(paths.mapping_file, index=False)
    folder = deepsearch_dir / "00_Test"
    folder.mkdir(parents=True, exist_ok=True)
    write_run(folder / "run_1.md", [{"program_name": "A", "supporting_genes": ["G1"]}])
    write_run(folder / "run_2.md", [{"program_name": "B", "supporting_genes": ["G1", "G2"]}])

    # Run main
    main(["--project", project])

    runs = pd.read_csv(paths.data_dir / "deepsearch_runs.csv")
    assert len(runs) == 2
    matches = pd.read_csv(paths.data_dir / "deepsearch_program_matches.csv")
    assert not matches.empty
