# Targeted Remote Follow-Up Results PDF Layout Rebalance And Page-Break Fix

## Overview

This task applies a narrow follow-up repair to the styled PDF layout of
`2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report.pdf`.
The previous pass over-tightened `Rank` and `Family` in `Ranked Completed Runs`,
over-expanded `Config`, and introduced unwanted blank pages before
`Main Conclusions` and `Artifact References`.

## Technical Approach

The fix will stay renderer-level in
`scripts/reports/generate_styled_report_pdf.py` so the Markdown report remains
canonical and the layout behavior becomes reproducible on regeneration.

The refinement will:

1. rebalance `Ranked Completed Runs` by widening `Rank` and `Family`, reducing
   `Config`, and slightly tightening `Test RMSE [deg]` plus `Val MAE [deg]`;
2. rebalance `Updated Family Bests` by widening `Family` and slightly reducing
   `Best Run After This Campaign`;
3. remove the extra blank-page behavior before `Main Conclusions` and
   `Artifact References` while preserving the intended fresh-page starts;
4. regenerate and validate the real PDF output after the renderer change.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/infrastructure/2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report.pdf`
- `doc/README.md`

## Implementation Steps

1. Adjust the report-specific CSS widths for the two affected tables.
2. Replace the current page-break implementation with a single reliable
   mechanism that does not emit blank spacer pages.
3. Regenerate the campaign-results PDF.
4. Validate the exported PDF pages and confirm the section starts land on the
   intended pages without blank-page regressions.
