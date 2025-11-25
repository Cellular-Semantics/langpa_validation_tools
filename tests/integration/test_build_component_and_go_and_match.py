import json
import os

import numpy as np
import pandas as pd

from src.build_component_mapping import main as build_components_main
from src.build_go_terms import main as build_go_terms_main
from src.match_components import main as match_components_main
from src.project_paths import resolve_paths


def setup_project(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    project = "tmp_proj"
    paths = resolve_paths(project)
    paths.ensure_output_dirs()
    return project, paths


def test_build_component_mapping_and_go_terms_main(tmp_path, monkeypatch):
    project, paths = setup_project(monkeypatch, tmp_path)
    # create Table S10
    df = pd.DataFrame(
        {
            "MetaModule": [0],
            "annotation": ["OPC-like 1"],
            "Enriched Pathways": ["Term A (GO:1), Term B (GO:2)"],
        }
    )
    df.to_excel(paths.s10_file, sheet_name="Table S10", index=False)
    # mapping file
    pd.DataFrame(
        {
            "metamodule": [0],
            "annotation": ["OPC-like 1"],
            "original_folder": ["geneset_1"],
            "new_folder": ["00_Test"],
        }
    ).to_csv(paths.mapping_file, index=False)

    build_components_main(["--project", project])
    build_go_terms_main(["--project", project])

    comp_path = paths.data_dir / "component_mapping.csv"
    go_path = paths.data_dir / "go_terms.csv"
    assert comp_path.exists()
    assert go_path.exists()
    comp_df = pd.read_csv(comp_path)
    go_df = pd.read_csv(go_path)
    assert not comp_df.empty
    assert set(go_df["go_term"]) == {"Term A", "Term B"}


def test_match_components_main(tmp_path, monkeypatch):
    project, paths = setup_project(monkeypatch, tmp_path)
    data_dir = paths.data_dir
    data_dir.mkdir(parents=True, exist_ok=True)

    # component mapping
    pd.DataFrame(
        {
            "annotation": ["Test"],
            "folder": ["00_Test"],
            "component_token": ["tok"],
            "component_key": ["tok"],
            "component_order": [1],
            "expanded_name": ["token name"],
            "source_note": ["note"],
        }
    ).to_csv(data_dir / "component_mapping.csv", index=False)

    # component embeddings (single vector)
    np.save(data_dir / "component_embeddings.npy", np.array([[1.0, 0.0]]))
    pd.DataFrame(
        {
            "component_key": ["tok"],
            "component_token": ["tok"],
            "expanded_name": ["token name"],
        }
    ).to_csv(data_dir / "component_embeddings_index.csv", index=False)

    # program embeddings (one program in run 1)
    np.save(data_dir / "embeddings_name.npy", np.array([[1.0, 0.0]]))
    pd.DataFrame(
        {
            "folder": ["00_Test"],
            "run_index": [1],
            "program_index": [0],
            "program_name": ["Prog"],
        }
    ).to_csv(data_dir / "embeddings_index.csv", index=False)

    match_components_main(["--project", project])
    out_path = data_dir / "component_program_matches.csv"
    df = pd.read_csv(out_path)
    assert not df.empty
    assert df.iloc[0]["similarity"] >= 0.99
