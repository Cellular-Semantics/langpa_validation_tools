#!/usr/bin/env python3
"""Scaffold a new project with required directories and template files."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Support running as a module (python -m src.init_project) or as a script (python src/init_project.py)
try:
    from .project_paths import add_project_argument, resolve_paths  # type: ignore
except ImportError:  # pragma: no cover
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    from src.project_paths import add_project_argument, resolve_paths

TEMPLATE_MAPPING = """metamodule,annotation,original_folder,new_folder
# edit rows as needed
"""

TEMPLATE_DESCRIPTION = """## Project: {name}

- Add a short description and data provenance here.
- Place your source spreadsheet (e.g., media-3 (2).xlsx) in this folder.
- Update geneset_folder_mapping.csv with metamodule -> folder mappings.
"""


def scaffold(project: str) -> None:
    paths = resolve_paths(project)
    paths.ensure_output_dirs()

    # project metadata
    if not paths.description_file.exists():
        paths.description_file.write_text(TEMPLATE_DESCRIPTION.format(name=project).strip() + "\n")
    mapping_path = paths.mapping_file
    if not mapping_path.exists():
        mapping_path.write_text(TEMPLATE_MAPPING)

    # create placeholder spreadsheet path
    paths.s10_file.touch(exist_ok=True)

    # ensure input dirs exist
    paths.deepsearch_dir.mkdir(parents=True, exist_ok=True)
    paths.comparisons_dir.mkdir(parents=True, exist_ok=True)
    paths.schemas_dir.mkdir(parents=True, exist_ok=True)

    print(f"Initialized project '{project}'.")
    print(f"- Metadata: {paths.description_file}")
    print(f"- Mapping: {paths.mapping_file}")
    print(f"- Spreadsheet placeholder: {paths.s10_file}")
    print(f"- DeepSearch runs dir: {paths.deepsearch_dir}")
    print(f"- Comparisons dir: {paths.comparisons_dir}")
    print(f"- Schemas dir: {paths.schemas_dir}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scaffold a new DeepSearch analysis project.")
    add_project_argument(parser)
    return parser


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    scaffold(args.project)


if __name__ == "__main__":
    main()
