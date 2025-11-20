#!/usr/bin/env python3
"""
Assemble a master markdown report combining the global summary, user-supplied summary,
and per-gene-set sections referencing bubble plots and run reports.
"""
from __future__ import annotations

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ANALYSIS_REPORT = BASE_DIR / "reports" / "deepsearch_report.md"
SUMMARY_SNIPPET = BASE_DIR / "reports" / "summary_intro.md"
MASTER_REPORT = BASE_DIR / "reports" / "master_report.md"
BUBBLE_DIR = BASE_DIR / "analysis" / "confusion_heatmaps"
RUN_REPORT_ROOT = BASE_DIR / "reports"


def load_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def main() -> None:
    content = []
    if SUMMARY_SNIPPET.exists():
        content.append(load_text(SUMMARY_SNIPPET).strip())
        content.append("")
    else:
        content.append("<!-- TODO: insert summary by editing reports/summary_intro.md -->")
        content.append("")
    content.append(load_text(ANALYSIS_REPORT).strip())
    content.append("")
    report_folders = sorted((BASE_DIR / "reports").glob('[0-9][0-9]_*/'))
    for folder in report_folders:
        bubble = BUBBLE_DIR / f"{folder.name}_bubble.png"
        run_dir = RUN_REPORT_ROOT / folder.name
        run_links = []
        for idx in (1, 2):
            report_path = run_dir / f"run_{idx}.md"
            if report_path.exists():
                rel_path = report_path.relative_to(MASTER_REPORT.parent)
                run_links.append(f"[Run {idx}]({rel_path.as_posix()})")
        if not run_links and not bubble.exists():
            continue
        content.append(f"## {folder.name}")
        content.append("")
        if bubble.exists():
            rel_img = Path(os.path.relpath(bubble, MASTER_REPORT.parent))
            content.append(f"![{folder.name} overlap plot]({rel_img.as_posix()})")
            content.append("")
        if run_links:
            content.append("Reports: " + " | ".join(run_links))
            content.append("")
    MASTER_REPORT.write_text("\n".join(content).strip() + "\n")
    print(f"Master report written to {MASTER_REPORT}")


if __name__ == "__main__":
    main()
