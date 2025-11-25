from src import process_comparisons as pc


def test_extract_go_terms():
    text = "term one (GO:12345), term two (GO:99999)"
    terms = pc.extract_go_terms(text)
    assert terms == ["term one (GO:12345)", "term two (GO:99999)"]


def test_split_gene_set_id():
    assert pc.split_gene_set_id("comparison geneset_10.md") == 10


def test_parse_program_table_simple():
    text = """| DeepSearch Program | Similar | Novel |
|---|---|---|
| Prog A | x | y |
| Prog B | none | z |
"""
    rows = pc.parse_program_table(text)
    assert rows == [("Prog A", "x", "y"), ("Prog B", "none", "z")]


def test_parse_unmatched_go_terms_list():
    text = """Unmatched GO enrichment terms NOT represented:
- Term A (GO:1)
- Term B (GO:2)
"""
    terms = pc.parse_unmatched_go_terms(text)
    assert "Term A (GO:1)" in terms
    assert "Term B (GO:2)" in terms

def test_normalize_term():
    assert pc.normalize_term("Term (GO:123)") == "Term"
