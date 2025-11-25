Test scaffolding

- `tests/unit/`: fast checks for utilities (e.g., path resolution, CLI arg parsing).
- `tests/integration/`: pipeline-level smoke tests to validate Make targets per project without external API calls.
- TODO: add pytest configuration and fixtures; target >80% coverage as functionality grows.
