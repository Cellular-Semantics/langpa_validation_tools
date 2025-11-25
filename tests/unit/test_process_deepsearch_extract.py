import json
from pathlib import Path

import pytest

from src.process_deepsearch import parse_run


def test_parse_run_extracts_json_block(tmp_path):
    payload = {"context": {"a": 1}, "programs": [{"program_name": "X"}]}
    f = tmp_path / "run.md"
    f.write_text("header\n```json\n" + json.dumps(payload) + "\n```\n")
    parsed = parse_run(f)
    assert parsed["context"]["a"] == 1
    assert parsed["programs"][0]["program_name"] == "X"
