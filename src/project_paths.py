from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path

DEFAULT_PROJECT = "glioblastoma_perplexity_manual"


def project_from_env() -> str:
    return os.getenv("PROJECT", DEFAULT_PROJECT)


def add_project_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--project",
        default=project_from_env(),
        help=f"Project name (default: {DEFAULT_PROJECT} or $PROJECT)",
    )


@dataclass
class ProjectPaths:
    base_dir: Path
    project: str
    projects_root: Path
    project_dir: Path
    deepsearch_dir: Path
    comparisons_dir: Path
    data_dir: Path
    analysis_dir: Path
    reports_dir: Path
    schemas_dir: Path
    notebooks_dir: Path

    @property
    def mapping_file(self) -> Path:
        return self.project_dir / "geneset_folder_mapping.csv"

    @property
    def run_file_mapping(self) -> Path:
        return self.project_dir / "run_file_mapping.csv"

    @property
    def s10_file(self) -> Path:
        return self.project_dir / "media-3 (2).xlsx"

    @property
    def description_file(self) -> Path:
        return self.project_dir / "description.md"

    @property
    def bubble_dir(self) -> Path:
        return self.analysis_dir / "confusion_heatmaps"

    def ensure_output_dirs(self) -> None:
        for path in (
            self.projects_root,
            self.project_dir,
            self.schemas_dir,
            self.notebooks_dir,
            self.data_dir,
            self.analysis_dir,
            self.reports_dir,
            self.bubble_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)


def resolve_paths(project: str | None = None) -> ProjectPaths:
    base_dir = Path(__file__).resolve().parent.parent
    project_name = project or project_from_env()
    projects_root = base_dir / "projects"
    project_dir = projects_root / project_name
    return ProjectPaths(
        base_dir=base_dir,
        project=project_name,
        projects_root=projects_root,
        project_dir=project_dir,
        deepsearch_dir=base_dir / "deepsearch" / project_name,
        comparisons_dir=base_dir / "Comparisons" / project_name,
        data_dir=base_dir / "data" / project_name,
        analysis_dir=base_dir / "analysis" / project_name,
        reports_dir=base_dir / "reports" / project_name,
        schemas_dir=base_dir / "schemas" / project_name,
        notebooks_dir=base_dir / "notebooks" / project_name,
    )
