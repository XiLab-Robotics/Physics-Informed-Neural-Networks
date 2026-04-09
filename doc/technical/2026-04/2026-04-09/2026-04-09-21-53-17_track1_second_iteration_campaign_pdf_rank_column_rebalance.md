# Track1 Second Iteration Campaign PDF Rank Column Rebalance

## Overview

This document covers a narrow follow-up refinement for the styled PDF:

- `doc/reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.pdf`

The remaining issue is inside the `Ranked Completed Runs` table:

- the `Rank` column is now too narrow;
- the requested fix is to widen `Rank` slightly;
- the balancing reduction should come from `Test MAE`.

The rest of the table should remain unchanged because the previous refinement
already stabilized the broader layout.

## Technical Approach

The fix should stay in the styled report generator so the export remains
repeatable.

The expected change is:

1. slightly increase the width assigned to the `Rank` column in the report-
   specific table class;
2. reduce the width assigned to `Test MAE` by the same small amount;
3. keep the current unit wrapping for `Test MAE [deg]`;
4. regenerate and validate the real PDF.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.md`
- `doc/reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.pdf`
- `scripts/reports/validate_report_pdf.py`
- `doc/README.md`

## Implementation Steps

1. adjust the report-specific CSS widths for the `Ranked Completed Runs` table
2. regenerate the styled PDF
3. rasterize and inspect the real exported PDF
4. run Markdown warning checks on the touched Markdown scope
