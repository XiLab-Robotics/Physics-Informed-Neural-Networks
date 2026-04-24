# Track 1 Closeout PDF Table Layout Rebalance

## Overview

This task repairs two already exported `Track 1` exact-paper campaign result
reports whose PDF tables still need a report-specific layout rebalance.

The requested changes are not scientific-content edits. They are PDF
presentation repairs focused on:

- forcing selected sections to start on a new page;
- tightening a few narrow identifier/count columns;
- widening long run-name and scope columns;
- wrapping selected headers such as `Paper Cell` and `Closure Score` more
  cleanly.

The affected reports are:

- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-18-11-14-50_track1_remaining_family_partial_closeout_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-18-16-34-18_track1_remaining_family_final_closeout_campaign_results_report.md`

## Technical Approach

The repair should stay report-specific rather than changing the shared
`Track 1` full-matrix ranking profile globally.

The planned implementation is:

1. add report-specific forced page breaks in the styled PDF renderer so:
   - `Completed Family Closeout` starts on a new page in the partial-closeout
     report;
   - `Family Recovery Outcome` starts on a new page in the final-closeout
     report;
2. introduce report-specific table-class resolution in
   `scripts/reports/generate_styled_report_pdf.py` for the two affected report
   stems and their two affected sections;
3. create narrow dedicated width profiles for:
   - partial-closeout family table;
   - partial-closeout aggregate ranking table;
   - final-closeout family recovery table;
   - final-closeout aggregate ranking table;
4. update the relevant Markdown table headers where cleaner line wrapping is
   explicitly requested, for example:
   - `Paper Cell`
   - `Closure Score`
   - `Best Closure Score`
5. re-export both PDFs and validate the real PDF output against the repository
   styled-report standard.

No subagent is planned for this task. The scope is local and does not justify
delegation.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-18-11-14-50_track1_remaining_family_partial_closeout_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-18-16-34-18_track1_remaining_family_final_closeout_campaign_results_report.md`
- the two exported PDF artifacts under the same folder

## Implementation Steps

1. Add report-specific page-break slugs for the two requested sections.
2. Add dedicated table profiles in the PDF renderer with the exact column
   emphasis requested by the user.
3. Update the two Markdown reports so the wrapped headers match the new layout
   contract.
4. Re-export both report PDFs.
5. Run repository Markdown QA on the touched Markdown files.
6. Run PDF validation on both regenerated files and inspect the result for page
   starts, header wrapping, balanced numeric columns, and right-edge pressure.
