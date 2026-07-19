# Selected Active PDF Layout Fix

## Overview

This document plans a focused layout correction for the selected-active
`TE Curve Verification Pipeline` PDF report bundle generated under
`doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-19]/`.
The immediate target is
`track2_selected_active_polished_actual_values_backward_report.pdf`, with the
same exporter behavior kept reusable for future selected-active exports.

## Technical Approach

The fix will adjust the selected-active Markdown/PDF rendering path so the
`Exact Model Paths` section starts on a fresh PDF page and the three main
tables use explicit column-width rules:

- `Exact Model Paths`: wider `Candidate`, `Family`, `ONNX Model Path`, and
  `Python Model Path`; very narrow `Surface`.
- `Metric Ranking`: narrow `Rank`, wider `Candidate`, and equal-width numeric
  metric columns.
- `Direction Breakdown`: narrow `Direction`, wider `Candidate`, and
  equal-width numeric metric columns.

The preferred implementation is to add semantic table classes or export-facing
metadata in the generated selected-active Markdown, then support those classes
in the styled PDF exporter if required. The real PDF will be regenerated and
validated after the change.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/reports/analysis/build_track2_selected_active_report_bundle.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-19]/`
- `doc/README.md`

## Implementation Steps

1. Inspect the generated Markdown and styled PDF exporter table handling.
2. Add a page-break marker before `Exact Model Paths` for selected-active
   reports.
3. Add or reuse semantic table-width handling for the three requested tables.
4. Regenerate the selected-active Markdown/PDF for the affected report, and
   apply the same future-safe rules to the bundle generator.
5. Validate the real exported PDF and review rasterized pages for table fit,
   page start, and wrapped headers.
6. Run Python and Markdown QA on the touched scope.
