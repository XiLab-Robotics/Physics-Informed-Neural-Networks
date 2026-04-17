# Remote Training Campaign Results PDF Layout Repair

## Overview

The styled PDF export for the remote training validation campaign results report
needs a targeted layout repair. The user requested three concrete adjustments in
the final PDF artifact
`2026-04-03-22-35-07_remote_training_validation_campaign_results_report.pdf`:

1. in the `Ranked Completed Runs` table, widen `Config`, `Test MAE [deg]`, and
   `Val MAE [deg]`, while shrinking `Rank` and `Family`;
2. in the `Failed Run` table, widen `Config` and `Outcome`, while shrinking
   `Family` and strongly shrinking `Runtime`;
3. force `Campaign Winner` to start on a new page.

The intent is to improve the real exported PDF layout, not only the Markdown
source, and to keep the result aligned with the repository's styled-report
golden standard.

## Technical Approach

The repair should be implemented at the styled-report exporter layer rather than
through ad hoc Markdown hacks. The report already uses semantic section titles
and generic Markdown tables, so the cleanest fix is:

- inspect how the exporter assigns CSS classes to this specific report table
  shape;
- add a report-specific table class or width override for the two target
  tables;
- add a report-specific forced page break for the `Campaign Winner` section;
- regenerate the PDF and validate the real exported pages to confirm the table
  fit and section start behavior.

If the existing class-resolution logic is insufficiently specific for these two
tables, it should be extended in a narrow report-local way so other styled
reports are not unintentionally perturbed.

No subagent is currently planned for this work. The scope is small and bounded
to local report-export tooling plus the affected report source.

## Involved Components

- `doc/reports/campaign_results/infrastructure/2026-04-03-22-35-07_remote_training_validation_campaign_results_report.md`
- `doc/reports/campaign_results/infrastructure/2026-04-03-22-35-07_remote_training_validation_campaign_results_report.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/README.md`

## Implementation Steps

1. Inspect the current styled-export rules for ranking/result tables and report
   specific page-break controls.
2. Add narrowly scoped layout rules for the two target tables in this report.
3. Force `Campaign Winner` onto a new page through the report-specific section
   page-break rules.
4. Regenerate the styled PDF from the canonical Markdown source.
5. Validate the real exported PDF pages for table balance, header fit, and page
   start quality.
6. Run the repository Markdown checks on the touched Markdown scope before
   closing the task.
