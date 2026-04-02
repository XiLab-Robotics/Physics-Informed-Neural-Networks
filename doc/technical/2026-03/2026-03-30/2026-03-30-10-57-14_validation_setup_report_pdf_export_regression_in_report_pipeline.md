# Validation Setup Report PDF Export Regression In Report Pipeline

## Overview

The validation-setup report generated during the skill operational test exposed
a real regression in the styled report export workflow.

Observed artifacts:

- the current PDF at
  `doc/reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report.pdf`
  renders as a browser error page with `ERR_FILE_NOT_FOUND`;
- a preview HTML artifact was left behind at
  `doc/reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report_preview.html`.

The task is to diagnose and repair this export regression, regenerate the PDF,
revalidate the real PDF output, and remove any debug-only HTML artifact unless
it is explicitly intended to remain.

## Technical Approach

The Markdown report source is valid, and the preview HTML artifact is valid,
which means the failure happens during or around the browser-based HTML-to-PDF
export path.

The most relevant workflow components are:

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`

The investigation should focus on the difference between:

- the direct exporter path;
- the orchestrated report-pipeline path.

In particular, the fix should verify whether:

- the temporary HTML preview path is being removed too early;
- the browser print-to-PDF call is returning before the final render is stable;
- the pipeline is overwriting a previously correct PDF with a broken later run;
- preview HTML persistence is being handled inconsistently.

The repair should keep the repository rule unchanged:

- the real exported PDF must be validated;
- the task remains open until the PDF is visually correct.

## Involved Components

- `README.md`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report.md`
- `doc/reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report.pdf`
- `doc/reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report_preview.html`
- `doc/technical/2026-03/2026-03-30/2026-03-30-10-57-14_validation_setup_report_pdf_export_regression_in_report_pipeline.md`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before implementing the export regression fix.
3. Inspect the direct exporter path and the orchestrated report-pipeline path.
4. Repair the regression so the exported PDF contains the report content rather
   than the browser error page.
5. Regenerate the validation-setup report PDF.
6. Validate the real exported PDF visually and structurally.
7. Remove the leftover preview HTML artifact unless it is intentionally kept.
8. Run scoped Markdown checks on touched repository-owned Markdown files and
   confirm normal final-newline state before reporting completion.
