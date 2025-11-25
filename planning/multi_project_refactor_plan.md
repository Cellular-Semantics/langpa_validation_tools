## Multi-project refactor plan (target project: `glioblastoma_perplexity_manual`)

Objectives: make the pipeline project-aware (multiple DeepSearch datasets + schemas), keep scripts reusable, and introduce guardrails/tests scaffolding.

### Architecture and directory layout
- Project-scoped data: `deepsearch/<project>/`, `Comparisons/<project>/`, `data/<project>/`, `analysis/<project>/`, `reports/<project>/`, `notebooks/<project>/` (optional per-project notebooks), `schemas/<project>/` (placeholder for future schema processing), `projects/<project>/description.md` (human-readable project definition/metadata).
- Shared code: rename `scripts/` → `src/` (Python package). Keep shared assets like Makefile, requirements, pyproject at repo root.
- Mappings: move `geneset_folder_mapping.csv`, `run_file_mapping.csv`, and similar mapping tables into `projects/<project>/` to avoid cross-project collisions. Provide a small registry (e.g., `projects/projects.yaml` or README) listing available project names.

### Makefile and entrypoints
- Add `PROJECT ?= glioblastoma_perplexity_manual` default. All phony targets accept `PROJECT` and direct outputs to project-scoped paths.
- Wrap Python invocations as `$(PYTHON) -m src.process_deepsearch --project $(PROJECT)` etc., and ensure temp/cache paths respect project root.
- Consider a convenience target to list projects and validate existence (`projects/<project>/description.md` + mapping files).

### Code refactor (src package)
- Introduce a path resolver utility (e.g., `src/project_paths.py`) that, given `project`, returns paths to deepsearch/comparisons/data/analysis/reports/schemas/mappings. Deprecate hardcoded BASE_DIR references to flat dirs.
- Update all scripts to accept `--project` CLI arg/env var; fall back to default. Ensure inter-script imports use the `src` package namespace.
- Preserve current behaviors (run matching, comparison parsing, figures, master report) but scoped within a project directory; handle missing optional files gracefully.
- Adjust build_master_report/go figures/notebook writers to read project-scoped CSVs and emit project-scoped outputs.

### Migration of existing dataset
- Create `projects/glioblastoma_perplexity_manual/` with mapping CSVs and description.
- Move current DeepSearch runs, comparison markdowns, data outputs, analysis artifacts, reports, and notebooks into the corresponding project subdirectories. Update references in code/Makefile accordingly.
- Keep legacy AGENTS instructions archived (e.g., `AGENTS_legacy.md`) and add new `AGENTS.md` with repo aims + guardrails (>80% coverage goal, project-aware operations).

### Testing scaffolding
- Add `tests/unit/` and `tests/integration/` with initial smoke placeholders (e.g., path resolver + CLI arg parsing). Plan for future coverage expansion once functions are modularized.

### Risks and mitigations
- Path churn could break parsing of comparison tables or notebooks; mitigate by centralizing path resolution and adding validation of required files per project.
- Backward compatibility: ensure default project name maps to migrated legacy data; provide clear error if `PROJECT` missing or invalid.
- Makefile dependency order: confirm per-project data/figures/reports still recompute correctly and don’t mix outputs across projects.
- Large file moves: risk of accidental overwrites; prefer move with verification and keep archival copies if needed.
