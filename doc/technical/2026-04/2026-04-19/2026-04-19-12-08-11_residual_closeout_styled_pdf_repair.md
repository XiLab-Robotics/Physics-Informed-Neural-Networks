# Residual Closeout Styled PDF Repair

## Overview

The final closeout report for the `2026-04-19` Track 1 residual cellwise
closure campaign currently has a non-canonical PDF artifact. The Markdown
report is correct, but the PDF was produced through a local fallback path after
the styled export pipeline failed.

The repository-standard deliverable for campaign closeout reports is the styled
PDF generated through `scripts/reports/generate_styled_report_pdf.py`. This
task restores that canonical export path for the residual closeout report so
the final PDF matches the same visual direction as the other campaign results
reports.

## Technical Approach

Inspect and repair the styled PDF export pipeline around the headless browser
handoff in `generate_styled_report_pdf.py`, focusing on the Chrome profile and
`print-to-pdf` execution path that failed for this report in the current
session.

After the export path is repaired, regenerate the residual closeout report PDF
through the canonical styled pipeline, validate the real exported PDF with the
repository PDF validation workflow, and replace the temporary fallback PDF with
the styled canonical artifact.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report.pdf`
- `doc/technical/2026-04/2026-04-19/README.md`
- `doc/README.md`

## Implementation Steps

1. Reproduce the styled export failure with the canonical report and isolate
   the failing browser invocation path.
2. Repair the styled export pipeline so the residual closeout report can again
   be rendered through the repository-standard Chrome/Edge export flow.
3. Regenerate the final residual closeout PDF with
   `generate_styled_report_pdf.py`.
4. Validate the real exported PDF with `validate_report_pdf.py` and check the
   rasterized output for layout quality.
5. Run Markdown QA on the touched Markdown scope and keep the repaired PDF as
   the canonical closeout artifact.
