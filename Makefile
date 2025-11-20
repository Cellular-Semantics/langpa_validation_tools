PYTHON ?= .venv/bin/python
SYSTEM_PYTHON ?= python3

all: data comparisons heatmaps run_reports master_report

.PHONY: data
data:
	$(PYTHON) scripts/process_deepsearch.py

.PHONY: comparisons
comparisons:
	$(PYTHON) scripts/process_comparisons.py

.PHONY: heatmaps
heatmaps: data
	$(PYTHON) scripts/generate_heatmaps.py

.PHONY: run_reports
run_reports: data
	$(PYTHON) scripts/generate_reports.py

.PHONY: master_report
master_report: heatmaps run_reports
	$(PYTHON) scripts/build_master_report.py
