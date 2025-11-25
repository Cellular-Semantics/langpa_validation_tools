from src.build_component_mapping import tokenize


def test_tokenize_removes_like_and_digits():
    assert tokenize("AC-like 1 program") == ["AC", "program"]
    assert tokenize("OPC-NPC-like") == ["OPC", "NPC"]
