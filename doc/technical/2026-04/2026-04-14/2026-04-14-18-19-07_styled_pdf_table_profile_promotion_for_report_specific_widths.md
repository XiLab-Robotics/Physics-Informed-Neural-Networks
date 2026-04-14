# Styled PDF Table Profile Promotion For Report-Specific Widths

## Overview

This document defines a permanent renderer-side rule for styled analytical PDFs
that contain dense campaign tables with long identifiers, mixed metric columns,
or before/after summary cells that do not fit the default width presets.

The immediate trigger is the validated manual correction of these tables in the
`Track 1` SVM repair campaign report:

- `Ranked Completed Runs`
- `Table-Level Before Vs After`

The observed behavior is important:

- the old default sizing was materially wrong;
- the newly introduced report-specific width blocks were already close to the
  right answer before any final manual tuning;
- this means the renderer should stop relying on generic fallback behavior for
  these table shapes.

## Technical Approach

The permanent fix should promote a reusable renderer rule:

1. when a report table has a known dense structure and a stable semantic role,
   it should receive its own CSS class and explicit width profile;
2. the resolver `resolve_standard_table_class_name(...)` should be the canonical
   place where those table-specific promotions are declared;
3. future campaign-results reports should not rely on the generic width profile
   for tables that contain long run names, multiple compact metric columns, or
   multi-state before/after cells;
4. when one manually tuned table profile proves nearly correct with only minor
   final adjustment, that tuned profile should replace the previous default for
   that semantic table shape.

Concretely for the current renderer:

- `Ranked Completed Runs`-style tables need a dedicated ranking profile with a
  larger `Run` column and narrower metric columns;
- compact three-column status-comparison tables such as
  `Table-Level Before Vs After` need a dedicated before/after profile with a
  widened `Surface` column;
- the generic profile should remain only a fallback for tables that do not yet
  have an identified semantic class.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/2026-04-14-17-40-47_track1_svm_open_cell_repair_campaign_results_report.md`
- future campaign-results Markdown reports that contain ranking or summary
  tables with similar structure
- `doc/README.md`

## Implementation Steps

1. Add reusable dedicated CSS table profiles for the corrected SVM repair
   tables.
2. Keep the resolver-based report-specific binding as the mandatory path for
   these profiles.
3. Review the current generic and adjacent default ranking profiles against the
   successful manual tuning.
4. Tighten the renderer rule so future similarly shaped tables are promoted to a
   dedicated profile earlier instead of falling back to visibly wrong default
   widths.
5. Regenerate the target PDF and validate the real exported pages after the
   renderer update.
