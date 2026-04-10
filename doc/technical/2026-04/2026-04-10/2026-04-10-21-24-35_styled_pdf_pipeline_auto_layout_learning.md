# Styled PDF Pipeline Auto Layout Learning

## Overview

This technical document formalizes the next refinement step for the
repository-owned styled PDF pipeline. The immediate trigger is the successful
manual repair of the exact-paper campaign results PDF, where the desired layout
direction became clearer:

- identifier-style columns such as `Config` should receive space early instead
  of being compressed by numeric fields;
- compact categorical columns such as `Rank` and `Winner` should stay narrow;
- long metric headers such as `Mean Component MAPE [%]`, `Mean Component MAE`,
  and `Mean Component RMSE` should wrap inside their own cells in a controlled
  way;
- section text should avoid awkward single-line spillovers onto the next page
  when a small wording reduction or clean keep-together rule can prevent it.

The goal is to promote these learned layout choices into the renderer so future
styled analytical PDFs land closer to the expected quality without requiring a
manual corrective pass each time.

## Technical Approach

The implementation will extend the styled report export pipeline with reusable
layout heuristics instead of depending only on one-off report-specific CSS.
The planned direction is:

1. classify more tables by structural intent, especially ranking-style tables
   that mix identifier, categorical, and metric columns;
2. encode width-allocation heuristics that prioritize long identifier columns
   before numeric metric columns;
3. normalize common long metric headers into controlled two-line forms inside
   their own header cells;
4. promote page-break discipline for section starts and short trailing lines so
   small avoidable spillovers are corrected automatically when feasible;
5. preserve report-specific escape hatches for cases where a canonical
   structure still needs a dedicated profile.

This keeps the pipeline aligned with the project golden standard while still
respecting the repository rule that the real exported PDF, not the Markdown
source alone, is the deliverable that must validate cleanly.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
- `doc/reports/campaign_results/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md`
- `doc/reports/campaign_results/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.pdf`

No subagent is planned for this task. The implementation scope is local to the
repository renderer and validation workflow.

## Implementation Steps

1. Inspect the current table-classification and header-normalization path in
   the styled PDF generator.
2. Extract the successful exact-paper layout choices into reusable renderer
   rules instead of keeping them only as narrow ad hoc adjustments.
3. Add a clearer internal structure for ranking-style table profiles so future
   campaign-results tables inherit better defaults with less report-local CSS.
4. Review whether section-level keep-together or paragraph compaction hooks are
   appropriate for preventing isolated page spillovers without overfitting.
5. Re-export and validate representative PDFs, including the exact-paper
   campaign report, to confirm the new defaults improve the real output.
6. Run Markdown checks on the touched Markdown scope before closing the task.
