# Causal Offset Closeout PDF Table Width Fix

## Overview

The styled PDF
`doc/reports/campaign_results/track_2/campaign_closeouts/2026-07-23-13-18-49_causal_offset_bounded_track2_screen_closeout_report.pdf`
needs table-width corrections in the `Execution Summary`, `Metric Ranking`,
`Shape-Gated Decision`, and `Harmonic Breakdown` sections.

The fix must be permanent for analogous future PDFs, so the preferred change is
to extend the styled PDF table classification and width-control layer instead
of only editing the generated PDF or shortening labels in one Markdown file.
The final layout pass also needs the `Metric Ranking` section to begin on a
fresh PDF page.

## Technical Approach

The implementation will:

- update the causal-offset closeout Markdown column labels to the requested
  units: `Raw MAE [deg]`, `RMSE [deg]`, `Mean Error [%]`, `P95 Error [%]`,
  `Centered MAE [deg]`, `Shape Pass`, `Composite`, `FFT Sim.`,
  `Amp Err. [%]`, and `Phase Err. [deg]`;
- extend the styled PDF exporter to classify these report tables by their
  header signatures;
- add persistent `colgroup` width rules for the relevant table families:
  execution-summary tables, Track 2 metric-ranking tables, shape-gated
  decision tables, and harmonic-breakdown tables;
- add a report-specific forced page break before `Metric Ranking` for this
  closeout report;
- regenerate the Markdown-to-PDF pipeline and validate the real rasterized PDF
  pages for table fit, header wrapping, and right-edge pressure.

## Involved Components

- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-07-23-13-18-49_causal_offset_bounded_track2_screen_closeout_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-07-23-13-18-49_causal_offset_bounded_track2_screen_closeout_report.pdf`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/README.md`

## Implementation Steps

1. Inspect the current closeout Markdown and styled PDF exporter table logic.
2. Add semantic table classes and explicit column widths for the requested
   report table signatures.
3. Update the closeout Markdown labels to the requested unit format.
4. Add the required fresh-page start before `Metric Ranking`.
5. Regenerate the styled PDF with the repository-owned report pipeline.
6. Raster-validate the generated PDF and visually inspect the affected pages.
7. Run Markdown QA on the touched Markdown scope and script syntax checks on
   the modified exporter.
