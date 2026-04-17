# Track 1 SVM Repair PDF Table Rebalance

## Overview

This document defines a narrow styled-PDF layout correction for the campaign
results report:

- `doc/reports/campaign_results/track1/svm/2026-04-14-17-40-47_track1_svm_open_cell_repair_campaign_results_report.md`

The goal is to rebalance only these two report tables:

- `Ranked Completed Runs`
- `Table-Level Before Vs After`

The change must stay report-specific and must not alter the generic table
profile used by unrelated reports.

## Technical Approach

The repository already uses report-specific table-class resolution inside
`scripts/reports/generate_styled_report_pdf.py`. The correct fix is therefore:

1. add one dedicated table class for the `Ranked Completed Runs` table in the
   SVM repair report;
2. add one dedicated table class for the `Table-Level Before Vs After` table in
   the same report;
3. add CSS width and padding rules only for those two classes;
4. bind the classes through `resolve_standard_table_class_name(...)` using the
   report stem, section slug, subsection slug, and exact header cells.

This keeps the layout correction local to the intended report and prevents
regressions in the existing `generic`, `ranking`, or `track1_full_matrix_*`
profiles.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/track1/svm/2026-04-14-17-40-47_track1_svm_open_cell_repair_campaign_results_report.md`
- `doc/README.md`

## Implementation Steps

1. Introduce two new table-class constants for the SVM repair report.
2. Add dedicated CSS rules for the ranking table and the before/after summary
   table.
3. Extend `resolve_standard_table_class_name(...)` so the two target tables use
   those classes only inside the SVM repair campaign results report.
4. Run a parser check on the Python renderer script.
5. Run Markdown QA on the touched Markdown scope.
6. Regenerate the report PDF and validate the exported pages that contain the
   adjusted tables.
