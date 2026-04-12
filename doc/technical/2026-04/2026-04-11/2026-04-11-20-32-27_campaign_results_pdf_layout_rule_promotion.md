# Campaign Results PDF Layout Rule Promotion

## Overview

This technical document formalizes a new refinement pass for the repository
styled PDF pipeline after another recurring campaign-results PDF review on the
exact-paper faithful reproduction report.

The concrete defect pattern is now clear and repeated enough to justify a
renderer-level promotion instead of another report-local manual correction:

- ranking tables still compress `Config` too aggressively;
- compact columns such as `Rank` and `Target A` are still wider than they need
  to be;
- metric headers with units such as `Curve MAE [deg]` and
  `Curve RMSE [deg]` still need more consistent unit wrapping;
- support-summary tables still over-allocate width to export-state columns and
  under-allocate it to metric and identifier columns.

The goal is to turn these specific preferences into reusable campaign-results
 table rules so future PDFs land closer to the desired layout on the first
 export.

## Technical Approach

The implementation will extend the styled report PDF generator with additional
campaign-results table heuristics instead of relying on one-off Markdown
shortening alone.

The intended direction is:

1. identify the two-table `Comparable Offline Ranking` pattern as a dedicated
   campaign-results table profile;
2. tighten compact categorical columns such as `Rank` and `Target A` while
   giving more early width to `Config`;
3. wrap unit suffixes such as `[deg]` onto a second line for curve-metric
   headers in these campaign-results tables;
4. refine the `Exact-Paper Support Runs` table profile so `ONNX Export` stays
   compact and metric columns like `Mean Component MAPE [%]` and
   `Mean Component MAE` remain balanced;
5. retain the validated output as a generalized rule in the renderer so future
   campaign-results PDFs inherit the same behavior without another manual pass.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report.md`
- `doc/reports/campaign_results/2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report.pdf`
- `doc/technical/2026-04/2026-04-10/2026-04-10-21-24-35_styled_pdf_pipeline_auto_layout_learning.md`

No subagent is planned for this task. The scope is local to the campaign-report
 PDF renderer and report source text.

## Implementation Steps

1. Extend the styled renderer table-profile logic for the two `Comparable
   Offline Ranking` tables and the two `Exact-Paper Support Runs` tables.
2. Encode narrower width targets for `Rank`, `Target A`, and similar compact
   categorical columns in these profiles.
3. Increase the width priority of `Config` and rebalance the remaining numeric
   columns accordingly.
4. Enforce cleaner unit wrapping for curve metrics such as `Curve MAE [deg]`,
   `Curve RMSE [deg]`, `Robot TE RMS [deg]`, and `Cycloidal TE RMS [deg]`.
5. Re-export the exact-paper faithful reproduction campaign report and inspect
   the real PDF validation images.
6. Keep the updated preference as a renderer rule so future campaign-results
   PDFs follow the same layout by default.
