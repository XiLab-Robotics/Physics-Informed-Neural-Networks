# 2026-04-24-15-05-52 Track1 Interrupted Svm Partial Closeout Candidate Scientific Gains Pdf Table Rebalance

## Overview

The interrupted `SVM` partial-closeout report PDF needs a narrow layout fix in
the two `Candidate Scientific Gains` tables.

The requested visual change is:

- reduce `MAE` strongly;
- keep `MAE` the same width as `RMSE`;
- reduce `Candidate`;
- widen `Run Instance` substantially;
- widen `Notes` substantially.

The user wants the fix applied in the shared styled-PDF script, then they will
rerun the normal report-export command manually.

## Technical Approach

Do not change the Markdown report content.

The two affected tables currently fall back to the generic table profile,
because the report-specific table-class resolver does not yet recognize the
`Candidate Scientific Gains` header shape:

- `("Candidate", "Run Instance", "MAE", "RMSE", "Notes")`

The correct fix is therefore:

1. introduce a dedicated reusable table class for this exact 5-column shape;
2. map that class only for the interrupted `SVM` partial-closeout report inside
   the `candidate-scientific-gains` section;
3. rebalance only the column widths in CSS, keeping the rest of the shared PDF
   pipeline unchanged.

This keeps the change narrow and avoids unintended drift in unrelated generic
tables.

## Involved Components

- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-24-12-39-24_track1_remaining_yellow_cell_interrupted_svm_partial_closeout_campaign_results_report.md`
- `scripts/reports/generate_styled_report_pdf.py`
- `doc/technical/2026-04/2026-04-24/2026-04-24-15-05-52_track1_interrupted_svm_partial_closeout_candidate_scientific_gains_pdf_table_rebalance.md`
- `doc/technical/2026-04/2026-04-24/README.md`
- `doc/README.md`

## Implementation Steps

1. Add a dedicated styled-table class for the `Candidate Scientific Gains`
   table shape in `generate_styled_report_pdf.py`.
2. Register a report/section-specific resolver branch so only the interrupted
   `SVM` partial-closeout report uses that class for the two affected tables.
3. Set the widths so `MAE` and `RMSE` match, `Candidate` is reduced, and `Run
   Instance` plus `Notes` are widened substantially.
4. Run Python parse validation on the touched script.
5. Run scoped Markdown QA on the touched technical-document/index scope.
6. Stop and hand the user the normal report-export command so they can
   regenerate the PDF manually.
