# Plan: Semantic Embedding Upgrade

## 1. Dependencies
- Install `openai` (or `anthropic` if switching providers) within `.venv`.
- Ensure `OPENAI_API_KEY` is available in the environment. Consider `.env` + `python-dotenv` for local dev.
- Because embeddings can be expensive, add a config flag (env var) to disable the feature by default.

## 2. Data Preparation
- Source data: `data/deepsearch_programs.csv`.
- For each program, create two payloads:
  - `name_text = program_name`
  - `desc_text = f"{program_name}. {description}"`
- Deduplicate with `(folder, run_id, program_index)` to avoid redundant API calls.

## 3. Embedding Script (`scripts/embed_programs.py`)
1. Read the program catalog.
2. For each entry, check if an embedding already exists (persist as JSON or NPZ indexed by run/program ID).
3. Batch requests (<= 32 entries per API call).
4. Store embeddings in `data/embeddings_name.npy` / `data/embeddings_full.npy` plus an index CSV mapping program IDs to row numbers.

## 4. Similarity Update
- Modify `scripts/process_deepsearch.py`:
  - Load cached embeddings at startup.
  - Replace the current name heuristic with cosine similarity on the name embeddings.
  - Optionally add a second cosine term for name+description; combine as `combined = 0.5 * gene_jaccard + 0.25 * name_cos + 0.25 * fulltext_cos`.
  - Allow toggling between heuristic mode and embedding mode via CLI flag/env var.

## 5. Regenerate Outputs
- Re-run `process_deepsearch.py` to refresh `data/deepsearch_*`.
- Re-run `process_comparisons.py` (unchanged) so GO stats reflect the new matches.
- Update notebook plots (`analysis/deepsearch_consistency.ipynb`) and `analysis/deepsearch_report.md` to describe the embedding-based similarity.

## 6. Validation
- Compare new combined scores against heuristic ones (scatter plot).
- Manually inspect a few edge cases where names differ but descriptions match (e.g., immune programs).
- Ensure thresholds for matching (e.g., 0.15) still make sense; cosine tends to produce higher baselines.

## 7. Documentation
- Expand `AGENTS.md` or README with instructions on:
  - Setting `OPENAI_API_KEY`.
  - Running `scripts/embed_programs.py`.
  - Switching between heuristic and embedding modes.
