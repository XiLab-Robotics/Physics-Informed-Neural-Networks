# CVP 1.4 PDF Table Layout Rules

## Overview

This document plans a PDF layout correction for the `CVP 1.4 Mean-Offset
Full-Matrix Audit` report and a reusable styled-PDF generator rule for future
reports with the same diagnostic table structure.

The current `CVP 1.4` PDF is valid, but the operator-facing layout should be
improved before closeout. The report should start `Diagnostic Label Counts` on
a new page, and the diagnostic ranking tables should use a stable column-width
profile that favors the long candidate identifiers while keeping compact rank
and surface columns.

## Technical Approach

The implementation should update the report Markdown/generator path and the
styled PDF generator so future reports of this type inherit the same layout.

Required report layout changes:

- insert a page break before `Diagnostic Label Counts`;
- for `CVP 1.4 Diagnostic Ranking`, `Surface Leaders`, and `Largest
  Mean-Offset Improvements`:
  - narrow `Rank`;
  - narrow `Surface`;
  - widen `Candidate`;
  - give `Raw MAE`, `Centered MAE`, `Offset`, `Gain [%]`, and `Label` the same
    width;
  - render `Raw MAE` and `Centered MAE` with a line break before `MAE`.

Required generator behavior:

- add a dedicated styled-PDF table profile for CVP 1.4 mean-offset audit
  tables or equivalent future reports using the same headers;
- keep the rule scoped to matching table headers so unrelated reports are not
  affected;
- preserve the machine-readable CSV/YAML metrics unchanged.

## Involved Components

Expected implementation surfaces:

- `scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`
- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.pdf`
- `doc/README.md`

Validation surfaces:

- real PDF export through `scripts/reports/pdf/run_report_pipeline.py`;
- PDF raster validation images under `.temp/report_pipeline/pdf_validation/`;
- scoped Markdown QA for touched authored Markdown files;
- Python compile checks for touched scripts.

## Implementation Steps

1. Add page-break markup before `Diagnostic Label Counts` in the CVP 1.4
   report generation path.
2. Update the CVP 1.4 table headers so `Raw MAE` and `Centered MAE` break
   across two lines in the rendered PDF while remaining readable in Markdown.
3. Add a dedicated table-layout profile in the styled PDF generator for tables
   matching the CVP 1.4 diagnostic headers.
4. Regenerate the CVP 1.4 report from the final merged metrics with
   `--merge-only`.
5. Export and validate the real PDF.
6. Inspect the rasterized PDF pages that contain the affected tables.
7. Run scoped Python and Markdown QA on touched files.
