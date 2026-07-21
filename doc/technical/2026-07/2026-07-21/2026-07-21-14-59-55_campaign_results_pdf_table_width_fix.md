# Campaign Results PDF Table Width Fix

## Overview

This document defines the implementation plan for repairing the styled PDF
layout of the completed shape-gate loss v2 campaign results report and making
the table-width rules reusable for future analogous campaign-results PDFs.

The immediate layout corrections are:

- `Metric Breakdown`: render all three columns with equal width.
- `Pilot Comparison`: widen `Family` and `Decision`, narrow `Surface`, and keep
  `Validation MAE` and `Test MAE` at equal width.

## Technical Approach

The fix will be implemented in the repository-owned styled PDF renderer instead
of hand-editing only the generated PDF or shortening table text. The renderer
already assigns semantic table classes and emits `colgroup` elements, so the
durable correction should add report-table classification and width rules for
campaign-results metric and pilot-comparison tables.

The implementation will:

- add semantic detection for the two table shapes used by this report class;
- assign dedicated table classes during Markdown-to-HTML rendering;
- update the CSS/column-width mapping so future reports with the same headers
  inherit the same PDF-safe layout;
- regenerate the affected campaign results PDF;
- validate the real exported PDF through the existing report pipeline and
  rasterized page inspection.

No subagent is planned for this task.

## Involved Components

- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/reports/campaign_results/cross_wave/shape_gate_loss_v2/2026-07-21-14-48-36_shape_gate_loss_v2_checkpoint_selection_pilot_campaign_results_report.md`
- `doc/reports/campaign_results/cross_wave/shape_gate_loss_v2/2026-07-21-14-48-36_shape_gate_loss_v2_checkpoint_selection_pilot_campaign_results_report.pdf`
- `doc/README.md`

## Implementation Steps

1. Inspect the current styled PDF table-class resolution and `colgroup`
   rendering code.
2. Add campaign-results table classifiers for the metric-breakdown and
   pilot-comparison header signatures.
3. Add permanent column-width rules:
   `Metric Breakdown` = `33.333% / 33.333% / 33.333%`;
   `Pilot Comparison` = wider `Family` and `Decision`, narrow `Surface`, equal
   metric columns for `Validation MAE` and `Test MAE`.
4. Regenerate the affected campaign results PDF with the repository report
   pipeline.
5. Validate the real exported PDF and inspect the rasterized pages for table
   fit, header wrapping, identifier pressure, and right-edge clipping.
6. Run Python and Markdown QA on the touched implementation and documentation
   scope.
