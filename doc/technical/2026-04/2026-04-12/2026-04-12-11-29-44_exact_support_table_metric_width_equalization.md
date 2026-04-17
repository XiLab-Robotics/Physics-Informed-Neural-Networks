# Exact Support Table Metric Width Equalization

## Overview

This technical document captures one final narrow layout correction on the
exact-paper faithful reproduction campaign-results PDF.

The remaining defect is limited to the first `Exact-Paper Support Runs` table:

- `ONNX Export` is still slightly wider than necessary;
- `Winner` is still slightly wider than necessary;
- `Mean Component MAPE [%]` still needs more width;
- `Mean Component MAPE [%]` should visually match
  `Mean Component MAE`.

The purpose is to store this as a reusable renderer rule refinement rather
than a report-local manual tweak.

## Technical Approach

The implementation will only adjust the dedicated CSS width profile used by the
first `Exact-Paper Support Runs` table. No report content, ranking logic, or
selection policy will change.

The intended direction is:

1. reduce `ONNX Export`;
2. reduce `Winner`;
3. give the recovered width to `Mean Component MAPE [%]`;
4. make `Mean Component MAPE [%]` match `Mean Component MAE`;
5. re-export and inspect the real PDF validation image for page 2.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report.pdf`

No subagent is planned for this task. The scope is only the renderer rule and
the exported PDF validation pass.

## Implementation Steps

1. Adjust the exact-support ranking table width profile in the styled PDF
   renderer.
2. Re-export the exact-paper faithful reproduction campaign-results PDF.
3. Inspect the page-2 raster validation image.
4. Keep the successful width equalization as the default renderer rule for
   future campaign-results PDFs.
