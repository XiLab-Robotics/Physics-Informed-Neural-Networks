# Track 1 Full-Matrix PDF Table Specific Width Rebalance

## Overview

This document covers a narrow renderer-only PDF layout update for the completed
`Track 1` full-matrix family reproduction campaign results report.

The requested change is intentionally limited to two specific tables in the
styled PDF export path:

- `Ranked Completed Runs`
- `Campaign-Wide Cell Totals`

The goal is to keep the generic table profile untouched while introducing
report-local, table-specific width rules for these two surfaces only.

## Technical Approach

The PDF renderer currently routes both target tables through the generic
`report-table-generic` CSS profile. That is too broad for this request because
the user wants table-specific width tuning without affecting other reports.

The change will therefore:

- add one dedicated CSS class for `Ranked Completed Runs`;
- add one dedicated CSS class for `Campaign-Wide Cell Totals`;
- route only those two tables in the specific campaign-results report to the
  new classes through `resolve_standard_table_class_name(...)`;
- leave all generic width rules unchanged.

Requested width target for `Ranked Completed Runs`:

- `Rank`: `6%`
- `Run`: `14%`
- `Family`: `6%`
- `Scope`: `14%`
- `Targets`: `7%`
- `Met`: `10%`
- `Near`: `6%`
- `Open`: `8%`
- `Closure Score`: `12%`

These values sum to `83%`, so the implementation pass must rebalance to `100%`
while preserving the user rule:

- if any column must be tightened, tighten `Met`;
- if any column must be widened, widen `Run`.

Requested width target for `Campaign-Wide Cell Totals`:

- widen `Surface`;
- make `Green`, `Yellow`, and `Red` equal-width columns.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-14-14-35-29_track1_full_matrix_family_reproduction_campaign_results_report.md`

No Markdown report content change is required for this task.

## Implementation Steps

1. Add two new table-class constants in the styled PDF renderer.
2. Add CSS rules for the two new classes inside `REPORT_STYLESHEET`.
3. Extend `resolve_standard_table_class_name(...)` so only the target report
   and target tables use the new classes.
4. Keep the generic table profile unchanged.
5. Run Markdown QA on this new technical document and its index entry.
6. Stop after the script change and report the exact manual PDF regeneration
   command to the user.
