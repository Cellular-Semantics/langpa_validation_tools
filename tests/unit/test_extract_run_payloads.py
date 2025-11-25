import json
from pathlib import Path

from src.extract_run_payloads import extract_citations, main
from src.project_paths import resolve_paths


def test_extract_citations_parses_footnotes():
    text = """Body
[^1]: http://example.com
[^ref]: https://foo
"""
    cites = extract_citations(text)
    assert {c['ref_id'] for c in cites} == {'1', 'ref'}
    assert any(c['url'] == 'http://example.com' for c in cites)


def test_extract_run_payloads_main(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    project = "tmp_extract"
    paths = resolve_paths(project)
    paths.ensure_output_dirs()
    run_dir = paths.deepsearch_dir / "00_Test"
    run_dir.mkdir(parents=True, exist_ok=True)
    payload = {"context": {}, "programs": [{"program_name": "X"}]}
    content = "Prompt\n```json\n" + json.dumps(payload) + "\n```\n[^1]: http://example.com"
    (run_dir / "run_1.md").write_text(content)

    main(["--project", project])

    payload_path = paths.data_dir / "run_payloads" / "00_Test" / "run_1.json"
    citation_path = paths.data_dir / "run_citations" / "00_Test" / "run_1_citations.json"
    assert payload_path.exists()
    assert citation_path.exists()
    saved = json.loads(payload_path.read_text())
    assert saved["programs"][0]["program_name"] == "X"
    citations = json.loads(citation_path.read_text())
    assert citations[0]["ref_id"] == "1"
