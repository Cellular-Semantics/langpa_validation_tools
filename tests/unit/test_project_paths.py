import os
from pathlib import Path

import pytest

from src.project_paths import DEFAULT_PROJECT, resolve_paths


def test_resolve_paths_defaults():
    paths = resolve_paths()
    base = Path(__file__).resolve().parents[2]
    assert paths.project == DEFAULT_PROJECT
    assert paths.data_dir == base / "data" / DEFAULT_PROJECT
    assert paths.deepsearch_dir == base / "deepsearch" / DEFAULT_PROJECT


def test_resolve_paths_custom(monkeypatch, tmp_path):
    # Temporarily adjust working directory to a temp root to ensure dirs create successfully
    monkeypatch.chdir(tmp_path)
    project = "test_proj"
    paths = resolve_paths(project)
    assert paths.project == project
    paths.ensure_output_dirs()
    for p in (
        paths.projects_root,
        paths.project_dir,
        paths.schemas_dir,
        paths.notebooks_dir,
        paths.data_dir,
        paths.analysis_dir,
        paths.reports_dir,
        paths.bubble_dir,
    ):
        assert p.exists() and p.is_dir()
