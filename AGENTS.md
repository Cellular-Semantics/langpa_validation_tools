## Repo purpose
- Analyze multiple DeepSearch projects, each with project-specific inputs (`deepsearch/<project>/`, `Comparisons/<project>/`, schemas), and generate run-matching, GO coverage, figures, and reports via the Makefile-driven pipeline.
- Default project: `glioblastoma_perplexity_manual`. Additional projects should live under `projects/<project>/` with mapping/description files and corresponding data/analysis/report subdirectories.

## Agent guard rails
- Maintain safety and reproducibility: prefer deterministic scripts over ad hoc prompts; record project name and commands used. Do not mutate files outside the active project scope.
- Target >80% automated test coverage as the codebase grows. Add unit tests for utilities and integration tests for pipeline entrypoints when modifying logic; keep fixtures minimal and deterministic.
- Network/model calls (e.g., embedding scripts) require explicit invocation and should be stubbed/mocked in tests. Avoid triggering paid API calls unintentionally.
- Preserve committed data outputs unless regeneration is intentional and documented. Never delete user data; stage new outputs under the correct project directories.
- When adding new automation, expose a CLI flag/Makefile hook for project selection and validate required inputs (mapping, schemas, DeepSearch runs) before writing outputs.

## Project metadata
- Add a human-readable summary for each project at `projects/<project>/description.md` and keep mapping files (`geneset_folder_mapping.csv`, `run_file_mapping.csv`, supporting spreadsheets) in the same folder.
