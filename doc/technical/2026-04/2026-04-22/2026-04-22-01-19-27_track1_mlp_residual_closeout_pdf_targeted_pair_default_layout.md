# Track 1 MLP Residual Closeout PDF Targeted Pair Default Layout

## Overview

This technical document covers a narrow PDF-layout repair for the residual
`MLP` closeout report:
`doc/reports/campaign_results/track1/exact_paper/2026-04-22-01-08-33_track1_mlp_residual_cell_final_closure_campaign_results_report.pdf`.

The requested outcome is twofold:

- force `Targeted Pair Outcome` onto a new page without introducing an empty
  standalone blank page;
- make the rendered `Targeted Pair Outcome` table use the same default visual
  proportions already accepted in
  `2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report.pdf`.

The second requirement is not only report-local. The repository PDF exporter
must learn this layout as the automatic default for the `Targeted Pair Outcome`
table family, so future exact-paper closeout reports inherit the same balanced
column widths without ad hoc per-report tuning.

## Technical Approach

The implementation will stay inside the repository-owned styled PDF workflow.

The work will proceed in three coordinated steps:

1. inspect the current residual-closeout Markdown plus the existing styled-PDF
   renderer rules that already handle the earlier `MLP` closeout report;
2. update the styled exporter so the `Targeted Pair Outcome` table pattern
   automatically receives the accepted default column sizing used by the
   earlier `2026-04-21-22-19-09` `MLP` family closeout report;
3. add the narrowest possible page-break trigger so `Targeted Pair Outcome`
   starts on a fresh page in the residual-closeout PDF while avoiding a full
   blank spacer page.

The report Markdown will only be changed if a stable, renderer-compatible
page-break marker is required. If the break can be solved entirely in the
exporter logic, prefer that path so future reports also benefit from the same
behavior automatically.

## Involved Components

- `doc/reports/campaign_results/track1/exact_paper/2026-04-22-01-08-33_track1_mlp_residual_cell_final_closure_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-22-01-08-33_track1_mlp_residual_cell_final_closure_campaign_results_report.pdf`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-22/README.md`

## Implementation Steps

1. Inspect the residual-closeout report structure and the existing styled-PDF
   specialization already used for `Targeted Pair Outcome`.
2. Promote the accepted `Targeted Pair Outcome` column balance from the earlier
   `MLP` closeout report into the automatic default renderer rule for this
   table shape.
3. Add the minimal page-break handling needed to start `Targeted Pair Outcome`
   on a fresh page without leaving a fully blank page in the PDF.
4. Regenerate the residual-closeout PDF through the canonical report pipeline.
5. Validate the real exported PDF and confirm:
   - `Targeted Pair Outcome` starts on a new page;
   - no blank full page is introduced;
   - the table uses the same accepted width balance as the earlier
     `2026-04-21-22-19-09` `MLP` report.
6. Run Markdown QA on any touched repository-authored Markdown files.
