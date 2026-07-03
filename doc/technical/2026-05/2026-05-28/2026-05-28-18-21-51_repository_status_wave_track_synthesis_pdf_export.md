# Repository Status Wave Track Synthesis PDF Export

## Overview

Plan the styled PDF export for
`doc/reports/analysis/project_status/current/Repository Status Wave Track Synthesis.md`.

The deliverable will be a repository-owned PDF companion for the completed
analysis report. The PDF must be generated through repository tooling and
validated as a real exported artifact before the task is considered complete.

## Technical Approach

Use the repository PDF workflow rather than an ad hoc converter. The work will
inspect the report Markdown and the PDF scripts, generate the styled PDF, then
validate the exported file for layout defects.

The validation pass will check:

- clipped borders;
- table overflow or right-edge pressure;
- wrapped headers that escape cells;
- crushed identifier columns;
- oversized numeric columns;
- awkward page starts or section breaks;
- general alignment with the repository styled-report visual standard.

No subagent is planned. If a subagent becomes useful later, its scope will be
declared and explicit approval will be requested before launch.

## Involved Components

Input report:

- `doc/reports/analysis/project_status/current/Repository Status Wave Track Synthesis.md`

Expected output:

- `doc/reports/analysis/project_status/current/Repository Status Wave Track Synthesis.pdf`

Repository PDF tooling:

- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`

Index and QA components:

- `doc/README.md`
- repository Markdown QA scripts

## Implementation Steps

1. Inspect the PDF export tooling command-line interface and current report
   Markdown.
2. Generate the styled PDF companion for the report.
3. Validate the real exported PDF with repository PDF validation tooling.
4. If validation reveals layout issues, adjust the Markdown or export settings
   with minimal churn and regenerate the PDF.
5. Register the PDF companion in `doc/README.md` if the index needs an
   explicit deliverable entry.
6. Run Markdown QA on touched Markdown files:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
7. Report the PDF path, validation result, and any residual risk. Do not create
   a Git commit without explicit commit approval.
