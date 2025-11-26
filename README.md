# DeepSearch multi-project analysis

Pipeline for parsing Perplexity DeepSearch outputs, comparing pseudo-enrichment programs to GO results, and generating figures/reports per project. The current default project is `glioblastoma_perplexity_manual`, but the layout supports multiple projects via per-project subdirectories.

[![Tests](https://github.com/Cellular-Semantics/langpa_validation_tools/actions/workflows/tests.yml/badge.svg)](https://github.com/Cellular-Semantics/langpa_validation_tools/actions/workflows/tests.yml)
![coverage](https://raw.githubusercontent.com/Cellular-Semantics/langpa_validation_tools/main/badges/coverage.svg)

## Layout
- `projects/<project>/`: mapping files (`geneset_folder_mapping.csv`, `run_file_mapping.csv`), source spreadsheet (e.g., `media-3 (2).xlsx`), `description.md`.
- Inputs: `deepsearch/<project>/run_*.md`, `Comparisons/<project>/comparison geneset_*.md`, `schemas/<project>/` (placeholder).
- Outputs: `data/<project>/`, `analysis/<project>/`, `reports/<project>/`, `notebooks/<project>/`.
- Code: `src/` package (CLI entrypoints), `tests/` scaffold (unit/integration).

## Running the pipeline
```bash
# activate your venv first (requires pandas, numpy, matplotlib, etc.)
PROJECT=glioblastoma_perplexity_manual make master_report
make test         # run pytest
make coverage     # pytest with coverage report

# New project scaffold
python -m src.init_project --project my_project
# then fill projects/my_project/description.md and geneset_folder_mapping.csv,
# add runs under deepsearch/my_project/, comparisons under Comparisons/my_project/,
# and run with PROJECT=my_project make master_report
```
Targets: `data` (parse runs), `comparisons` (parse GO tables), `figures`, `heatmaps`, `run_reports`, `master_report`. Environment variables `MPLCONFIGDIR` and `XDG_CACHE_HOME` default to repo-local caches.

## Development rules
- Always pass a project name (CLI `--project` or `PROJECT` env/Make variable); keep inputs/outputs confined to that project’s directories.
- Do not modify other projects’ data. Prefer deterministic scripts over ad hoc edits. Avoid deleting user data or overwriting inputs.
- Tests: aim for high coverage as functionality grows (>80% target). Add unit tests for utilities and integration smoke tests for pipeline entrypoints when changing behavior.
- Network/API calls (embedding scripts) are opt-in and should be stubbed/mocked in tests. Provide clear env var requirements (e.g., `OPENAI_API_KEY`).
- Keep caches writable and local (use repo `.mpl-cache` / `.cache`). Respect existing naming conventions (`run_*.md`, `comparison geneset_*.md`).
- Governance: see `AGENTS.md` for guard rails and `AGENTS_legacy.md` for prior context. Summarize new projects in `projects/<project>/description.md`.
