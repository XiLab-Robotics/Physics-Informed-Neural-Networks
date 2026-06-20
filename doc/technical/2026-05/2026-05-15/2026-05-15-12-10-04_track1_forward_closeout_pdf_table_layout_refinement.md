# RCIM Model-Bank Reproduction Forward Closeout PDF Table Layout Refinement

## Overview

This technical note plans a narrow styled-PDF renderer refinement for the Track
1 forward paper-faithful closeout report. The current Markdown content is
correct, but the PDF table layout needs report-specific column balancing so the
closeout can be read cleanly and future closeout exports inherit the same
layout rules automatically.

The target report is
`doc/reports/campaign_results/track_1/exact_paper/forward/2026-05-15-11-11-35_track1_forward_paper_faithful_grid_search_closeout_report.md`.

## Technical Approach

Update the repository-owned styled PDF renderer instead of editing the report
Markdown to fake column widths. The renderer should recognize the closeout
tables by their headers and assign semantic table classes with dedicated CSS
widths.

The requested layout rules are:

- `Family Results`: narrow `Family`, widen `Run Instance`, make `Mean MAE`,
  `Mean RMSE`, and `Mean MAPE %` equal width, make `Exported ONNX` and
  `Exported PKL` equal width, and render those exported headers on two lines.
- `Benchmark Status`: widen `Table`, and make `Green`, `Yellow`, `Red`, and
  `Total` equal width.
- `Reference Archive Refresh`: narrow `Family`, `Archived Targets`, and
  `Source Runs`, and allocate most remaining width to `Archive Root`.

The renderer change should be reusable for future closeout reports with the
same table shapes.

## Involved Components

- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/reports/campaign_results/track_1/exact_paper/forward/2026-05-15-11-11-35_track1_forward_paper_faithful_grid_search_closeout_report.md`
- `doc/reports/campaign_results/track_1/exact_paper/forward/2026-05-15-11-11-35_track1_forward_paper_faithful_grid_search_closeout_report.pdf`

No subagent is planned for this narrow renderer fix.

## Implementation Steps

1. Add semantic table-class constants and header-detection helpers for the
   three RCIM Model-Bank Reproduction forward closeout table shapes.
2. Add CSS column-width rules matching the requested layout.
3. Extend header normalization so `Exported ONNX` and `Exported PKL` wrap after
   `Exported`.
4. Regenerate the closeout PDF through the repository report pipeline.
5. Validate the real exported PDF and inspect the rasterized pages for table
   fit, header wrapping, and right-edge pressure.
6. Run scoped Python and Markdown checks for the touched files.
