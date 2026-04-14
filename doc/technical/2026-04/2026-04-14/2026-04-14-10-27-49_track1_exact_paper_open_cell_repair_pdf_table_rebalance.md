# Track 1 Exact-Paper Open-Cell Repair PDF Table Rebalance

## Overview

This technical document records a narrow styled-PDF layout repair for the
campaign results report:

- `doc/reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.pdf`

The current PDF export still shows suboptimal width allocation in the two
ranking tables under `Campaign Ranking`.

The requested fix scope is explicit:

- first table:
  - narrow `Rank`;
  - widen `Config`;
  - slightly narrow `Family Scope`;
  - wrap `Harmonics Open` and `Harmonics Partial`;
  - narrow `Met Cells`;
  - widen `Regressions`;
- second table:
  - widen `Config`;
  - narrow `Winner`;
  - render `Mean Component MAPE [%]` on two header lines and narrow its column;
  - narrow `Failed`.

## Technical Approach

The correct fix point is the styled PDF renderer:

- `scripts/reports/generate_styled_report_pdf.py`

The repair should be implemented as a report-specific table profile for this
exact campaign-results report, in the same style already used for other
campaign PDF layout exceptions in the repository.

This avoids manual PDF-only edits and keeps the renderer behavior explicit,
inspectable, and reproducible.

After the renderer update:

1. regenerate the same campaign-results PDF;
2. raster-validate the real exported PDF;
3. inspect the affected table pages for header wrapping, balanced widths, and
   absence of right-edge pressure.

No subagent is planned for this work.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md`
- `doc/reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.pdf`
- `.temp/report_pipeline/pdf_validation/`

## Implementation Steps

1. Add a report-specific table-profile override for the two `Campaign Ranking`
   tables in the styled PDF renderer.
2. Apply the requested column-width rebalance and header wrapping behavior.
3. Regenerate the campaign-results PDF through the standard report pipeline.
4. Validate the exported PDF and inspect the rendered table pages.
5. Run Markdown QA on the touched technical-document scope before closing the
   task.
