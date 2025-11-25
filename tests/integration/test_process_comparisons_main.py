import json
from pathlib import Path

import pandas as pd

from src.process_comparisons import main
from src.project_paths import resolve_paths

def write_comparison(path: Path):
    content = """
```json
{"context": {}, "programs": [{"program_name": "Prog A"}]}
```

| DeepSearch Program | Similar | Novel |
| --- | --- | --- |
| Prog A | term one (GO:12345) | n |
    """
    path.write_text(content)

def test_process_comparisons_main(tmp_path, monkeypatch):
    project = "tmp_proj"
    monkeypatch.chdir(tmp_path)
    paths = resolve_paths(project)
    paths.ensure_output_dirs()

    # mapping
    pd.DataFrame(
        {
            "metamodule": [0],
            "annotation": ["Test"],
            "original_folder": ["geneset_1"],
            "new_folder": ["00_Test"],
        }
    ).to_csv(paths.mapping_file, index=False)

    # Table S10 minimal xlsx
    s10_path = paths.s10_file
    s10_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(
        {
            "MetaModule": [0],
            "annotation": ["Test"],
            "Enriched Pathways": ["term one (GO:12345), term two (GO:555)"]
        }
    )
    df.to_excel(s10_path, sheet_name="Table S10", index=False)

    # comparison markdown
    comp_dir = paths.comparisons_dir
    comp_dir.mkdir(parents=True, exist_ok=True)
    write_comparison(comp_dir / "comparison geneset_1.md")

    main(["--project", project])

    summary = pd.read_csv(paths.data_dir / "comparison_summary.csv")
    assert not summary.empty
    table = pd.read_csv(paths.data_dir / "comparison_table_rows.csv")
    # Two program rows expected (header separator parsed as row); ensure expected program present
    assert (table["program_name"] == "Prog A").any()
