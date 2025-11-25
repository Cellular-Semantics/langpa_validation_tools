import json
from pathlib import Path

import pandas as pd

from src.generate_reports import generate_reports
from src.build_master_report import main as master_main
from src.project_paths import resolve_paths

def write_run(folder: Path, name: str, citation=True):
    programs = [{"program_name": name, "supporting_genes": ["G1"], "citations": [{"source_id": "C1"}] if citation else []}]
    payload = {"context": {"cell_type": "ct", "disease": "dz", "tissue": "ts"}, "programs": programs}
    folder.write_text("Prompt\n```json\n" + json.dumps(payload) + "\n```")


def test_generate_reports_and_master(tmp_path, monkeypatch):
    project = "tmp_proj"
    monkeypatch.chdir(tmp_path)
    paths = resolve_paths(project)
    paths.ensure_output_dirs()

    # mapping
    mapping = pd.DataFrame(
        {
            "metamodule": [0],
            "annotation": ["Test"],
            "original_folder": ["geneset_1"],
            "new_folder": ["00_Test"],
        }
    )
    mapping.to_csv(paths.mapping_file, index=False)

    # data stubs for GO tables
    data_dir = paths.data_dir
    data_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(
        {
            "folder": ["00_Test"],
            "program_name": ["Prog"],
            "similar_terms_raw": ["term"],
            "novel_aspects": ["novel"],
        }
    ).to_csv(data_dir / "comparison_table_rows.csv", index=False)
    pd.DataFrame({"folder": ["00_Test"], "gsea_term": ["TermX"]}).to_csv(
        data_dir / "comparison_unmatched_go_terms.csv", index=False
    )

    # deepsearch runs
    run_dir = paths.deepsearch_dir / "00_Test"
    run_dir.mkdir(parents=True, exist_ok=True)
    write_run(run_dir / "run_1.md", "Prog1", citation=True)
    write_run(run_dir / "run_2.md", "Prog2", citation=True)

    generate_reports(project)
    report_path = paths.reports_dir / "00_Test" / "run_1.md"
    assert report_path.exists()

    # minimal CSVs for master report
    pd.DataFrame(
        {
            "folder": ["00_Test", "00_Test"],
            "annotation": ["Test", "Test"],
            "run_index": [1, 2],
            "program_signature": ["sig1", "sig2"],
            "program_count": [1, 2],
        }
    ).to_csv(data_dir / "deepsearch_runs.csv", index=False)
    pd.DataFrame(
        {
            "run_a_id": ["a"],
            "run_b_id": ["b"],
            "program_a_index": [0],
            "program_b_index": [0],
            "program_a_name": ["Prog1"],
            "program_b_name": ["Prog2"],
            "gene_jaccard": [0.5],
            "name_similarity": [0.5],
            "combined_similarity": [0.5],
            "folder": ["00_Test"],
            "metamodule": [0],
            "annotation": ["Test"],
        }
    ).to_csv(data_dir / "deepsearch_program_matches.csv", index=False)
    pd.DataFrame(
        {
            "folder": ["00_Test"],
            "run_index": [1],
            "program_index": [0],
            "program_name": ["Prog1"],
            "supporting_genes": [json.dumps(["G1"])],
        }
    ).to_csv(data_dir / "deepsearch_programs.csv", index=False)
    pd.DataFrame({"folder": ["00_Test"], "component_token": ["tok"], "expanded_name": ["Tok"], "component_key": ["tok"], "annotation": ["Test"], "component_order": [1]}).to_csv(
        data_dir / "component_mapping.csv", index=False
    )
    pd.DataFrame({"folder": ["00_Test"], "component_token": ["tok"], "program_name": ["Prog1"]}).to_csv(
        data_dir / "component_program_matches.csv", index=False
    )
    pd.DataFrame({"folder": ["00_Test"], "annotation": ["Test"], "duplicate": [True]}).to_csv(
        data_dir / "deepsearch_duplicate_runs.csv", index=False
    )
    (paths.analysis_dir / "confusion_heatmaps").mkdir(parents=True, exist_ok=True)
    bubble = paths.analysis_dir / "confusion_heatmaps" / "00_Test_bubble.png"
    bubble.write_bytes(b"fake")

    master_main(["--project", project])
    assert (paths.reports_dir / "master_report.md").exists()
