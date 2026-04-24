# Campaign Results PDF Micro Rebalance Follow-Up

## Overview

This technical document captures one additional micro-rebalance pass on the
campaign-results PDF table rules after the first renderer-level promotion.

The remaining defects are narrower than the previous pass and now focus on two
specific tables in the exact-paper faithful reproduction campaign results PDF:

- in the first `Comparable Offline Ranking` table, `Target A` still needs a
  little more width while `Curve MAE [deg]` can give some width back;
- in the first `Exact-Paper Support Runs` table, `Rank` should be slightly
  wider, `ONNX Export` slightly narrower, `Winner` slightly narrower, and
  `Mean Component MAPE [%]` should match the width of
  `Mean Component MAE`.

The intent is again to promote this into the reusable renderer rules rather
than keep the adjustment as a one-off manual correction.

## Technical Approach

The implementation will not change the report content or ranking logic. It
will only refine the CSS width allocation of the newly introduced campaign
table profiles.

The planned direction is:

1. rebalance the shared-offline ranking table so `Target A` gets slightly more
   space and `Curve MAE [deg]` slightly less;
2. rebalance the exact-support ranking table so the compact categorical
   columns stop taking space from the mean-component metric headers;
3. preserve the existing unit wrapping and `Config` priority rules;
4. re-export and inspect the real PDF validation images to confirm that the
   new widths improve the page-2 table balance without regressing the other
   pages.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report.pdf`
- `doc/technical/2026-04/2026-04-11/2026-04-11-20-32-27_campaign_results_pdf_layout_rule_promotion.md`

No subagent is planned for this task. The scope is the renderer rule layer and
the final exported PDF validation.

## Implementation Steps

1. Update the dedicated campaign-results table-profile width rules inside the
   styled PDF renderer.
2. Re-export the exact-paper faithful reproduction campaign report.
3. Inspect the real PDF validation images with focus on page 2.
4. Keep the successful rebalance in the renderer so future campaign-results
   PDFs inherit the updated width allocation by default.
