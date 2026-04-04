# Remote Training Campaign Results PDF Layout Refinement

## Overview

The first repair pass for
`2026-04-03-22-35-07_remote_training_validation_campaign_results_report.pdf`
improved the target tables and forced `Campaign Winner` onto a new page, but
the user requested one additional refinement pass on the real exported PDF.

The requested follow-up adjustments are:

1. in `Ranked Completed Runs`, re-expand `Family` slightly and recover some
   width by tightening `Test MAE [deg]`, ideally wrapping `[deg]` onto a second
   line as already happens successfully for `Test RMSE [deg]`;
2. in `Failed Run`, re-expand `Runtime` slightly and recover the needed width by
   shrinking `Outcome` a bit;
3. force `Recommended Next Actions` onto a new page.

## Technical Approach

This refinement should remain in the styled-report renderer rather than in the
report Markdown. The existing report-specific table classes added for the first
repair pass should be tuned with slightly different width allocations, and the
report-specific forced-page-break set should be extended to include
`Recommended Next Actions`.

If needed, the completed-run table should also explicitly relax header wrapping
for the metric columns so `[deg]` can wrap cleanly inside the header cell
without causing neighboring-column spill.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/2026-04-03-22-35-07_remote_training_validation_campaign_results_report.pdf`
- `doc/technical/2026-04/2026-04-04/2026-04-04-10-42-25_remote_training_campaign_results_pdf_layout_refinement.md`
- `doc/README.md`

## Implementation Steps

1. Tune the report-specific CSS widths for the completed-run and failed-run
   tables.
2. Add a report-specific new-page rule for `Recommended Next Actions`.
3. Regenerate the styled PDF from the canonical Markdown source.
4. Validate the real exported PDF pages after the refinement.
5. Re-run the repository Markdown checks on the touched Markdown scope.
