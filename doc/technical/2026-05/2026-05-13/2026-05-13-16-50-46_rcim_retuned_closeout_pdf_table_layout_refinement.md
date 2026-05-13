# RCIM Retuned Closeout PDF Table Layout Refinement

## Overview

This document plans a narrow styled-PDF refinement for the recovered-original
`RCIM` retuned reference closeout report. The current report content is valid,
but several table layouts need renderer-level tuning so the exported PDF is
more readable and consistent.

The target PDF is:

`doc/reports/analysis/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.pdf`

The requested refinements are:

- rebalance the `Archive Completeness` table columns;
- make `MSE`, `RMSE`, `MAE`, and `MAPE` equal-width in
  `Mean Evaluation Metrics`;
- make harmonic metric columns equal-width in retuned Tables `2`-`5`;
- render numeric harmonic headers in white instead of black.

## Technical Approach

The implementation will use semantic PDF-renderer table classes rather than
manual Markdown spacing. This keeps the source report clean and makes future
regeneration preserve the intended layout.

The renderer will recognize the relevant tables by section and header shape,
then apply dedicated CSS rules:

- `Archive Completeness`: reduce `Direction` and `Family`, equalize `ONNX`,
  `PKL`, and `Exported Errors`, wrap the `Exported Errors` header onto two
  lines, and set `Eval Bundle` and `Export Bundle` to match `Retune Bundle`.
- `Mean Evaluation Metrics`: set `MSE`, `RMSE`, `MAE`, and `MAPE` to identical
  widths.
- Retuned Tables `2`-`5`: keep the `Model` column separate and distribute all
  harmonic columns evenly. Numeric harmonic headers will be styled as white
  text inside the table header.

No model archive, training artifact, metric value, or benchmark logic will be
changed.

## Involved Components

- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/closeout/closeout_rcim_retuned_reference_archive.py`
- `doc/reports/analysis/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.md`
- `doc/reports/analysis/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.pdf`
- `output/validation_checks/reports/rcim_retuned_reference_closeout_pdf_validation/`

No subagent is planned for this implementation.

## Implementation Steps

1. Add semantic table-class detection for the three affected table families in
   the styled PDF generator.
2. Add scoped CSS width rules for the `Archive Completeness`,
   `Mean Evaluation Metrics`, and retuned harmonic-metric matrix tables.
3. Update the closeout report generator header from `Export Errors` to
   `Exported Errors` if needed so the requested wording is stable when the
   report is regenerated.
4. Regenerate the closeout Markdown, HTML, and PDF through the repository-owned
   report tooling.
5. Validate the exported PDF by rasterizing the real PDF output and inspecting
   the affected pages.
6. Run Python compile checks, Markdown QA for touched Markdown files, and the
   Sphinx portal build if the report source remains part of the portal surface.
