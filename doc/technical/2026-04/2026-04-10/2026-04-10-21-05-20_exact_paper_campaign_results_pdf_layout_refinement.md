# Overview

This technical document defines a narrow layout-refinement pass for the exact
paper model-bank campaign results report PDF:

- `doc/reports/campaign_results/track1/exact_paper/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.pdf`

The report content is already complete, but the real exported PDF still shows
layout issues that should be corrected before considering the styled
deliverable fully closed.

The requested corrections are:

- pull the final `Objective And Outcome` winner line back onto the previous
  page if the section can be rebalanced cleanly;
- rebalance the first `Ranked Completed Runs` table so:
  - `Rank` is narrower;
  - `Winner` is narrower;
  - `Config` is wider;
  - `Mean Component MAE` wraps with `MAE` on a second line inside the same
    header cell;
- rebalance the second ranking table so:
  - `Config` is wider;
  - `ONNX Exported` is narrower;
  - `Mean Component MAE` also wraps cleanly with `MAE` on a second line.
- rebalance the `Top Family Ranking Inside The Winning Run` table so:
  - `Rank` is narrower;
  - `Family` is narrower;
  - `Mean Component MAPE [%]` wraps with `MAPE [%]` on a second line;
  - `Mean Component MAE` wraps with `MAE` on a second line;
  - `Mean Component RMSE` wraps with `RMSE` on a second line.

## Technical Approach

This should remain a PDF-first refinement pass rather than a broad content
rewrite.

1. Inspect the current report Markdown and the styled-PDF renderer behavior for
   the affected section and tables.
2. Apply the narrowest safe Markdown-level or renderer-level changes needed to:
   - reduce the vertical spill at the end of `Objective And Outcome`;
   - rebalance the two ranking tables;
   - rebalance the top-family ranking table;
   - keep headers inside their own cells without overflow.
3. Re-export the styled PDF.
4. Validate the real PDF output, not only the Markdown or preview HTML, with
   explicit checks on:
   - page-break cleanliness around `Objective And Outcome`;
   - header wrapping in both ranking tables;
   - header wrapping in the top-family ranking table;
   - identifier-column breathing room for `Config`;
   - right-edge pressure and column crowding.

No Codex subagent use is planned for this refinement pass.

## Involved Components

Primary report sources and deliverables:

- `doc/reports/campaign_results/track1/exact_paper/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.pdf`

Supporting export and validation tooling:

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`

Validation evidence:

- `.temp/report_pipeline/pdf_validation/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report/`

## Implementation Steps

1. Inspect the current report Markdown around `Objective And Outcome` and the
   two ranking tables.
2. Adjust the table source and, if necessary, the styled-PDF renderer behavior
   to achieve the requested width rebalance and header wrapping.
3. Re-export the PDF with the existing styled-report pipeline.
4. Validate the real exported PDF pages and confirm the requested layout
   corrections are visible in the rasterized output.
5. Run the required Markdown checks on every touched repository-owned Markdown
   file before closing the task.
