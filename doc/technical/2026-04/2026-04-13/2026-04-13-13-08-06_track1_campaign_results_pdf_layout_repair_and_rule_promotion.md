# Track 1 Campaign Results PDF Layout Repair And Rule Promotion

## Overview

This document defines the corrective work required to repair the exported PDF
layout of the overnight `Track 1` campaign results report and to promote the
same layout rules into the styled report renderer so future campaign-result
exports do not repeat the same defects.

The immediate target artifact is:

- `doc/reports/campaign_results/track1/harmonic_wise/forward/2026-04-13-12-37-15_track1_overnight_gap_closure_campaign_results_report.pdf`

The user requested three concrete layout repairs:

- start `Ranked Completed Runs` on a new page;
- rebalance the three campaign tables with better identifier-column room and
  tighter metric/block columns;
- enforce cleaner multi-line headers for compact unit-bearing metrics and for
  the baseline-delta header.

No subagent is planned or required for this implementation.

## Technical Approach

The repair will be implemented at the renderer level, not as a one-off manual
Markdown workaround. The styled PDF exporter will receive report-specific table
profiles for this `Track 1` campaign-results report, plus a report-specific
forced page break on the `Ranked Completed Runs` section.

The renderer will also be improved so identifier-like columns such as `Config`
and `Best Config` receive semantic wrap handling even when they are not the
first column of a table. This closes one of the root causes behind repeated
column-pressure problems in similar reports.

The actual exported PDF will then be regenerated and validated against the real
pages to confirm:

- the section starts on a clean new page;
- headers stay inside their own cells;
- identifier columns have enough width;
- metric columns are compressed without clipping;
- the `Interpretation` column gets adequate room in the block summary table.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/track1/harmonic_wise/forward/2026-04-13-12-37-15_track1_overnight_gap_closure_campaign_results_report.md`
- `doc/reports/campaign_results/track1/harmonic_wise/forward/2026-04-13-12-37-15_track1_overnight_gap_closure_campaign_results_report.pdf`
- `doc/technical/2026-04/2026-04-13/README.md`

## Implementation Steps

1. Register this technical document in the day-local technical index.
2. Add report-specific table classes for the overnight `Track 1` campaign
   results report.
3. Add a report-specific forced page break so `Ranked Completed Runs` begins on
   a new page.
4. Promote semantic identifier wrapping beyond first-column-only handling for
   `Config`-style columns.
5. Add report-specific header normalization for the baseline delta header and
   reuse unit wrapping for the `[deg]` metric headers.
6. Regenerate the styled PDF from the canonical Markdown report.
7. Validate the real exported PDF pages and confirm the requested layout
   corrections.
8. Run Markdown QA on the touched Markdown scope before closing the task.
