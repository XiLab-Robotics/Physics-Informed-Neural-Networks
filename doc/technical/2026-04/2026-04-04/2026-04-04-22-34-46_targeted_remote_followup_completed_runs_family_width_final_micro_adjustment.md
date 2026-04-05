# Targeted Remote Follow-Up Completed Runs Family Width Final Micro Adjustment

## Overview

This task applies one last narrow refinement to the
`Ranked Completed Runs` table in
`2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report.pdf`.
The remaining requested change is to widen `Family` a little more by reducing
`Val MAE [deg]`.

## Technical Approach

The adjustment will remain report-specific in
`scripts/reports/generate_styled_report_pdf.py` so the Markdown report stays
canonical and the layout change remains reproducible on regeneration.

The refinement will:

1. slightly reduce the `Val MAE [deg]` column width in the targeted remote
   follow-up completed-runs table;
2. move the recovered width into `Family`;
3. regenerate and validate the real PDF output.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report.pdf`
- `doc/README.md`

## Implementation Steps

1. Update the report-specific CSS widths for `Ranked Completed Runs`.
2. Regenerate the campaign-results PDF.
3. Validate the exported PDF pages and confirm the family-column balance on the
   real PDF.
