# Targeted Remote Follow-Up Results PDF Layout Refinement

## Overview

This task refines the styled PDF layout of the campaign results artifact
`2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report.pdf`.
The requested changes focus on the table fit of `Ranked Completed Runs` and
`Updated Family Bests`, plus cleaner section starts for `Main Conclusions` and
`Artifact References`.

## Technical Approach

The fix will stay in the repository-owned styled PDF renderer rather than
editing the report content to compensate for layout problems. The refinement
will:

1. rebalance the `Ranked Completed Runs` table so `Rank` and `Family` give more
   width back to `Config`;
2. force clean wrapped headers for `Test MAE [deg]`, `Test RMSE [deg]`, and
   `Val MAE [deg]` so `[deg]` remains inside each metric cell;
3. rebalance the `Updated Family Bests` table by widening `Family` and
   `Best Run After This Campaign` while tightening `Test MAE [deg]`;
4. force `Main Conclusions` and `Artifact References` to start on fresh pages
   when exported.

No subagent is planned for this implementation. The work is local to the PDF
export path and tightly coupled to the repository renderer and validation flow.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report.md`
- `doc/reports/campaign_results/2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report.pdf`
- `doc/README.md`

## Implementation Steps

1. Update the report-specific table layout profile in the styled PDF renderer.
2. Add the requested page-break controls for `Main Conclusions` and
   `Artifact References`.
3. Regenerate the target PDF.
4. Validate the real exported PDF, not only the Markdown or HTML.
5. Run the required Markdown checks on the touched Markdown scope.
6. Report completion and wait for explicit approval before creating the commit.
