# Campaign PDF Section Page-Break Rules

## Overview

The current shape-objective campaign PDF includes the correct Track 2
measured-versus-predicted pilot plots, but the report layout still needs two
permanent PDF rules for this report family and future analogous campaign
closeouts:

- `Execution Summary` must start on a new PDF page.
- `Pilot Graphs` must start on a new PDF page, and the first two Track 2 plots
  must remain on that same page with the `Pilot Graphs` heading.

This work should update repository-owned report generation and PDF styling so
the fix is repeatable, not a one-off manual edit to the generated PDF.

## Technical Approach

Implement semantic page-break support in the Markdown-to-styled-PDF pipeline
and use it from the shape-objective closeout report. The preferred approach is
to add report-local HTML markers or classes emitted by the closeout script and
handled by `scripts/reports/pdf/generate_styled_report_pdf.py`.

The PDF exporter should support:

- a forced page break before selected second-level sections;
- a keep-together block for the `Pilot Graphs` introduction plus the first two
  measured-versus-predicted Track 2 images;
- existing campaign table-width rules for `Metric Breakdown` and
  `Pilot Comparison`;
- normal rendering of later candidate plots across following pages.

The closeout report should remain valid Markdown/HTML input and should not
depend on manual PDF post-processing. No subagent is planned. If a subagent
becomes useful, the proposed subagent name, task boundary, and approval
requirement must be recorded here before requesting approval.

## Involved Components

- `scripts/reports/closeout/cross_wave/closeout_parallel_shape_objective_followup_campaign.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/reports/campaign_results/cross_wave/shape_objective/2026-07-21-19-31-21_parallel_shape_objective_followup_campaign_results_report.md`
- `doc/reports/campaign_results/cross_wave/shape_objective/2026-07-21-19-31-21_parallel_shape_objective_followup_campaign_results_report.pdf`
- `doc/reports/campaign_results/track_2/verification_plots/shape_objective_followup_polished_setpoints_fw/`
- `doc/README.md`

## Implementation Steps

1. Inspect the generated HTML/PDF structure for the campaign closeout report
   and identify the safest section markers for `Execution Summary` and
   `Pilot Graphs`.
2. Add persistent styled-PDF support for forced section page breaks and a
   keep-together pilot-graph opening block.
3. Update the closeout script so regenerated campaign reports emit the
   required page-break and keep-together markers.
4. Regenerate the campaign Markdown and styled PDF.
5. Raster-validate the real exported PDF and visually confirm that
   `Execution Summary` begins a page, `Pilot Graphs` begins a page, and the
   first two Track 2 plots stay with the `Pilot Graphs` heading.
6. Run Python compile checks, Markdown checks on touched Markdown, PDF
   pipeline validation, and `git diff --check`.
