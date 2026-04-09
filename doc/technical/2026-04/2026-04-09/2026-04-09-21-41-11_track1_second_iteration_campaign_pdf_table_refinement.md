# Track1 Second Iteration Campaign PDF Table Refinement

## Overview

This document covers the layout refinement requested for the styled PDF
artifact:

- `doc/reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.pdf`

The immediate issue is the `Ranked Completed Runs` table. The user requested a
more efficient column balance:

- shrink `Rank`
- shrink `Harmonic Set`
- widen `Config`
- widen `Feature Set`
- widen `Test MAE`
- wrap the unit label in `Test MAE [deg]` so `[deg]` stays on a second line

The task also records a broader repository preference learned from repeated PDF
reviews:

- when narrow metric columns include unit labels, prefer wrapping the unit to a
  second line rather than keeping the full header on one line or compressing
  the column excessively

## Technical Approach

The fix should be applied in the styled report generator rather than by manual
editing of the exported PDF.

The expected implementation path is:

1. inspect the report-specific table-class assignment for the campaign-results
   table;
2. add or refine report-specific width guidance for the `Ranked Completed Runs`
   table in the styled PDF generator;
3. update header rendering or report-source formatting so `Test MAE [deg]`
   wraps cleanly with the unit on a second line;
4. keep the real exported PDF as the validation target and re-check the
   rendered pages after export.

The broader convention should be encoded in the generator or in the report
source formatting pattern so future narrow metric columns naturally prefer:

- metric name on the first line
- unit on the second line

## Involved Components

- `doc/reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.md`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/README.md`

If the implementation also needs a durable repository rule, the follow-up touch
point is:

- `AGENTS.md`

## Implementation Steps

1. inspect the current Markdown report and styled-PDF generator logic for the
   campaign ranking table
2. refine the report-specific table layout so `Rank` and `Harmonic Set` become
   narrower and `Config`, `Feature Set`, and `Test MAE` receive more width
3. force or enable clean unit wrapping for `Test MAE [deg]`
4. regenerate the PDF
5. validate the real exported PDF raster output
6. run Markdown warning checks on the touched Markdown scope
7. if the user wants the learned layout rule to become explicit policy,
   formalize it in a follow-up repository rule update
