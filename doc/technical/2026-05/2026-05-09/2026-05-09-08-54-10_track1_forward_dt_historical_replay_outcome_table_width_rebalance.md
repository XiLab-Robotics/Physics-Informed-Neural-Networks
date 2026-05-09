# Track1 Forward DT Historical Replay Outcome Table Width Rebalance

## Overview

The styled PDF for the `forward + DT` paper-faithful subset closeout currently
renders the `Historical Replay Outcome` table with metric columns that are not
balanced and a `Scope` column that is too narrow. The requested refinement is
to keep `Mean MAE`, `Mean RMSE`, and `Mean MAPE %` at the same width while
widening `Scope`.

## Technical Approach

Apply a narrow styled-PDF renderer refinement for this specific report-table
surface without changing the report content, mathematical workflow, or generic
training logic. The implementation should prefer a semantic hook in the PDF
renderer rather than editing Markdown content to fake layout.

## Involved Components

- `doc/reports/campaign_results/track1/exact_paper/2026-05-08-19-53-19_track1_forward_dt_paper_faithful_search_campaign_results_report.md`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/2026-05-08-19-53-19_track1_forward_dt_paper_faithful_search_campaign_results_report.pdf`
- `doc/technical/2026-05/2026-05-09/README.md`
- `doc/README.md`

## Implementation Steps

1. Register this narrow PDF-layout refinement in the daily and canonical
   technical indices.
2. Inspect the existing styled-PDF semantic table hooks and add a dedicated
   width rule for the `Historical Replay Outcome` table in this exact report.
3. Regenerate the report PDF and validate the real exported PDF.
4. Re-run Markdown QA on the touched Markdown scope before closing the task.
