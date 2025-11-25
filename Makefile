PYTHON ?= .venv/bin/python
SYSTEM_PYTHON ?= python3
PROJECT ?= glioblastoma_perplexity_manual
MPLCONFIGDIR ?= $(PWD)/.mpl-cache
XDG_CACHE_HOME ?= $(PWD)/.cache
ENV_VARS = MPLCONFIGDIR=$(MPLCONFIGDIR) XDG_CACHE_HOME=$(XDG_CACHE_HOME)

CACHE_DIRS = $(MPLCONFIGDIR) $(XDG_CACHE_HOME)/fontconfig

all: cache_dirs data comparisons figures heatmaps run_reports master_report

.PHONY: cache_dirs
cache_dirs:
	@mkdir -p $(CACHE_DIRS)

.PHONY: data
data: cache_dirs
	$(ENV_VARS) $(PYTHON) -m src.process_deepsearch --project $(PROJECT)

.PHONY: comparisons
comparisons: data cache_dirs
	$(ENV_VARS) $(PYTHON) -m src.process_comparisons --project $(PROJECT)

.PHONY: heatmaps
heatmaps: data figures cache_dirs
	$(ENV_VARS) $(PYTHON) -m src.generate_heatmaps --project $(PROJECT)

.PHONY: figures
figures: data comparisons cache_dirs
	$(ENV_VARS) $(PYTHON) -m src.generate_summary_figures --project $(PROJECT)

.PHONY: run_reports
run_reports: data cache_dirs
	$(ENV_VARS) $(PYTHON) -m src.generate_reports --project $(PROJECT)

.PHONY: master_report
master_report: figures heatmaps run_reports cache_dirs
	$(ENV_VARS) $(PYTHON) -m src.build_master_report --project $(PROJECT)
