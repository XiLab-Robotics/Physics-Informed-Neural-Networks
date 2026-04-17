# Wave 1 Residual Campaign Results PDF Table Rebalance And Page Breaks

## Overview

The newly exported `Wave 1` residual-harmonic family campaign results PDF needs
layout refinement in the real rendered output.

The reported defects are:

- the `Test-Side Ranking` table gives too little width to the `Config`,
  `Test MAE [deg]`, `Test RMSE [deg]`, and `Val MAE [deg]` columns;
- the `Validation-Side Snapshot` table needs more room for `Config` and
  `Generalization Gap [deg]`;
- the comparison tables under sections `1`, `4`, and `5` need more room for
  the descriptive identifier columns and slightly less for selected numeric
  columns;
- the `Program-Level Context` and `Recommended Next Actions` sections should
  begin on a new page instead of following the previous content directly.

The task is therefore a report-source and export-layout refinement pass rather
than a content rewrite.

## Technical Approach

The fix should be applied at the canonical Markdown-report and export-layout
level, then verified against the real exported PDF.

The planned approach is:

1. inspect how the current report exporter handles table widths and section page
   breaks;
2. adjust the report source and, if needed, the exporter-recognized table
   layout hints so the requested columns receive more space;
3. force `Program-Level Context` and `Recommended Next Actions` to start on a
   new page in the exported PDF;
4. regenerate the PDF and validate the real rendered output again.

## Involved Components

- `doc/reports/campaign_results/wave1/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md`
  Canonical report source that may need table-layout and page-break hints.
- `doc/reports/campaign_results/wave1/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.pdf`
  Target PDF output that must be regenerated and validated.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF exporter that may already support the needed layout controls.
- `scripts/reports/run_report_pipeline.py`
  Export-and-validation orchestration entry point.
- `.temp/report_pipeline/pdf_validation/`
  Validation raster output used to confirm the real PDF layout.

## Implementation Steps

1. Inspect the current report source and exporter behavior for table-width and
   page-break control.
2. Apply the requested column rebalance to the affected tables.
3. Add page-break control so `Program-Level Context` and `Recommended Next Actions`
   begin on a new page.
4. Regenerate the styled PDF.
5. Validate the real exported PDF and confirm that the updated layout satisfies
   the requested table balance and page-start constraints.
