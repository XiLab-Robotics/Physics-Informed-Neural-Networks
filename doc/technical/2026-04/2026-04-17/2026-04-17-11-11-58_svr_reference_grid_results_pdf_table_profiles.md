# SVR Reference-Grid Results PDF Table Profiles

## Overview

This document defines a focused renderer update for the styled PDF export of
the campaign results report:

- `doc/reports/campaign_results/2026-04-17-11-00-54_track1_svr_reference_grid_search_repair_campaign_results_report.md`

The current PDF export uses generic table handling for three report tables:

- `Ranked Completed Runs`
- `Export Surface`
- `Gap Versus Paper`

Those tables have stable semantic shapes and currently fall back to generic
width distribution, which makes them harder to rebalance precisely. The goal of
this task is to introduce three dedicated table profiles in the PDF generator so
their column widths, spacing, and header wrapping can be tuned explicitly and
reused whenever the same table shapes appear again.

No subagent is planned for this task. The change is local to the styled report
renderer and does not require delegated implementation work.

## Technical Approach

The update will be implemented in
`scripts/reports/generate_styled_report_pdf.py`.

The renderer already supports report-table specialization through:

- dedicated CSS class constants;
- reusable header-pattern helpers;
- `resolve_standard_table_class_name(...)`;
- report-specific header normalization.

The three target tables currently do not match existing reusable profiles:

1. `Ranked Completed Runs`
   - current header:
     `Rank | Run | Scope | Paper Cells | Mean Gap Ratio | Max Gap Ratio | Failed Exports`
2. `Export Surface`
   - current header:
     `Completed Runs | Exported ONNX Files | Failed Exports | Surrogate Exports`
3. `Gap Versus Paper`
   - current header:
     `Harmonic / Metric | Paper Target | Repository Result | Gap | Status`

The implementation will therefore:

- add three new table-class constants;
- add three reusable header-cell tuples and predicate helpers;
- add three CSS blocks with explicit column widths and header behavior;
- extend `resolve_standard_table_class_name(...)` so these tables no longer
  fall back to the generic profile.

The scope is intentionally narrow: no Markdown content changes, no pipeline
runner changes, and no report-logic changes outside the renderer.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
  - new table class constants;
  - new header-pattern tuples/helpers;
  - new stylesheet rules;
  - new resolver branches.
- `doc/technical/2026-04/2026-04-17/README.md`
  - day-local technical index entry for this document.

The following files are inspection references but are not expected to change in
this task:

- `scripts/reports/run_report_pipeline.py`
- `doc/reports/campaign_results/2026-04-17-11-00-54_track1_svr_reference_grid_search_repair_campaign_results_report.md`

## Implementation Steps

1. Add a dedicated technical-document index for `2026-04-17` and register this
   task.
2. Introduce three new dedicated table class constants for:
   - `Ranked Completed Runs`
   - `Export Surface`
   - `Gap Versus Paper`
3. Add reusable header-cell definitions and resolver helpers for the three
   table shapes.
4. Add CSS blocks in `REPORT_STYLESHEET` with explicit width allocation and
   clean wrapped-header behavior for each table.
5. Extend `resolve_standard_table_class_name(...)` so the three tables resolve
   to their dedicated profiles instead of `GENERIC_TABLE_CLASS_NAME`.
6. Regenerate the report PDF and validate the real exported PDF with emphasis
   on:
   - header wrapping staying inside the correct cells;
   - balanced numeric columns;
   - identifier-column fit;
   - right-edge pressure;
   - vertical centering consistency.
7. Run Markdown warning checks on the touched Markdown scope before closing the
   task.
