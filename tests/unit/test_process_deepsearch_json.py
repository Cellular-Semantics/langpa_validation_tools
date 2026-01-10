import json
from pathlib import Path

from src.process_deepsearch import parse_run


def test_parse_run_json(tmp_path):
    payload = {"context": {"cell_type": "ct"}, "programs": [{"program_name": "P1"}]}
    f = tmp_path / "run_1.json"
    f.write_text(json.dumps(payload))
    parsed = parse_run(f)
    assert parsed["context"]["cell_type"] == "ct"
    assert parsed["programs"][0]["program_name"] == "P1"
