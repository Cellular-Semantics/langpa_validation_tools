PYTHON ?= .venv/bin/python
SYSTEM_PYTHON ?= python3
PROJECT ?= glioblastoma_perplexity_manual

all: data comparisons figures heatmaps run_reports master_report

.PHONY: data
data:
	$(PYTHON) -m src.process_deepsearch --project $(PROJECT)

.PHONY: comparisons
comparisons: data
	$(PYTHON) -m src.process_comparisons --project $(PROJECT)

.PHONY: heatmaps
heatmaps: data figures
	$(PYTHON) -m src.generate_heatmaps --project $(PROJECT)

.PHONY: figures
figures: data comparisons
	$(PYTHON) -m src.generate_summary_figures --project $(PROJECT)

.PHONY: run_reports
run_reports: data
	$(PYTHON) -m src.generate_reports --project $(PROJECT)

.PHONY: master_report
master_report: figures heatmaps run_reports
	$(PYTHON) -m src.build_master_report --project $(PROJECT)
