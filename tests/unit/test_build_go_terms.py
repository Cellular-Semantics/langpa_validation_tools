from src.build_go_terms import parse_terms


def test_parse_terms_extracts_go_ids():
    raw = "Term A (GO:1), Term B"
    parsed = parse_terms(raw)
    assert parsed == [("GO:1", "Term A"), ("", "Term B")]
