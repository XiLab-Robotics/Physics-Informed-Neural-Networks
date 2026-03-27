---
name: styled-report-pdf-qa
description: Use when preparing, exporting, validating, or repairing styled analytical PDFs and model-report PDFs in StandardML - Codex. This skill is for real PDF QA, not Markdown-only cleanup.
---

# Styled Report PDF QA

Run repository-specific QA for styled report exports with emphasis on the real
PDF output, not only the source Markdown or HTML.

## Use This Skill For

- analytical report export preparation;
- styled PDF layout review and repair;
- post-export PDF validation;
- table-balance and page-break fixes;
- coordination between report Markdown and `scripts/reports/` tooling.

## Do Not Use This Skill For

- generic Markdown linting with no PDF implications;
- finalizing a PDF task without validating the exported PDF;
- editing protected campaign files without explicit approval.

## Required Checks

1. Read the relevant report Markdown and export scripts under `scripts/reports/`.
2. Treat the real exported PDF as the deliverable to validate.
3. Compare the result against the repository golden standard:
   `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`.
4. Explicitly review:
   clipped borders, wrapped headers, table fit, crushed identifier columns,
   oversized numeric columns, right-edge pressure, and bad section page starts.
5. If the validation evidence is inconclusive, keep the task open.

## Repository PDF Priorities

- white page background with restrained blue-accent styling;
- rounded section cards and readable A4-safe margins;
- balanced tables with wrapped headers that remain inside their own cells;
- vertically centered cell content by default;
- clean section starts that do not break awkwardly across pages.

## Commands And Tools To Prefer

```powershell
python -B scripts/reports/run_report_pipeline.py
python -B scripts/reports/generate_styled_report_pdf.py
python -B scripts/reports/validate_report_pdf.py
```

## Validation Output Pattern

Prefer this structure:

1. Exported artifact checked.
2. Layout findings.
3. Fixes applied or still required.
4. Remaining risks, if any.

## File Targets To Read First

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- relevant report Markdown in `doc/reports/` or `doc/guide/`
- the exported PDF artifact under the task output folder
