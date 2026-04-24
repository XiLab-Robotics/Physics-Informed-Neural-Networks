# Residual Closeout PDF Table Micro Rebalance

## Overview

The residual closeout report PDF needs a narrow table-layout rebalance in the
two closeout tables:

- `Family Recovery Outcome`
- `Aggregate Ranking`

The requested adjustments are strictly visual and do not change the report
content, campaign bookkeeping, or benchmark conclusions.

## Technical Approach

Reuse the existing closeout table profiles already applied to the residual
closeout report and adjust only the relevant column widths in
`scripts/reports/generate_styled_report_pdf.py`.

For `Family Recovery Outcome`:

- make `Amplitude Run`, `Phase Run`, and `Best Run` the same width;
- widen `Best Scope`;
- widen `Best Closure Score`.

For `Aggregate Ranking`:

- widen `Rank` slightly;
- reduce `Run` correspondingly.

No Markdown table content changes are required for this rebalance unless the
rendered PDF still shows a secondary wrap issue after the width update.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report.pdf`
- `doc/technical/2026-04/2026-04-19/README.md`
- `doc/README.md`

## Implementation Steps

1. Update the `TRACK1_FINAL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME` column widths so
   the three run columns share the same width.
2. Redistribute the recovered width into `Best Scope` and `Best Closure Score`.
3. Update the `TRACK1_FINAL_CLOSEOUT_AGGREGATE_TABLE_CLASS_NAME` widths so
   `Rank` is slightly wider and `Run` slightly narrower.
4. Regenerate the residual closeout PDF through the canonical styled pipeline.
5. Validate the exported PDF images to confirm the rebalance materially improves
   the real layout.
6. Run Markdown warning checks on the touched Markdown scope before closing the
   task.
