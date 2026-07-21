# Pilot Track 2 Curve Plot Report Fix

## Overview

The `parallel_shape_objective_followup_2026_07_21` closeout report currently
contains pilot summary plots, but the intended pilot graphs are Track 2
measured-versus-predicted TE curve plots. The campaign technical plan already
required representative measured-versus-predicted curves, so the current
closeout implementation is incomplete even though the report and PDF render
successfully.

This fix should make future analogous pilot reports include Track 2 curve
evidence when the bounded Track 2 plot artifacts exist or can be generated from
a compact candidate configuration.

## Technical Approach

Use the repository-owned Track 2 plotting path instead of ad hoc metric-bar
plots as the pilot visual evidence source. The primary reusable entry point is
`scripts/reports/analysis/build_track2_candidate_curve_plots.py`, which already
generates bounded truth-versus-prediction PNG files and a
`track2_candidate_curve_plot_summary.yaml` manifest.

The closeout report builder should:

- treat Track 2 measured-versus-predicted plots as the required pilot visual
  bundle;
- embed representative plot images in the Markdown report with report-safe
  relative paths;
- keep scalar metric plots only as secondary diagnostics, or remove their
  primary-report role;
- record a clear warning in the report if Track 2 plot artifacts are missing
  because the bounded Track 2 screen has not yet been run;
- preserve the existing PDF table-width fixes and validate the real exported
  PDF after regeneration.

No subagent is planned. If a subagent becomes useful, the proposed subagent
name, task boundary, and approval requirement must be recorded here before
requesting approval.

## Involved Components

- `scripts/reports/closeout/cross_wave/closeout_parallel_shape_objective_followup_campaign.py`
- `scripts/reports/analysis/build_track2_candidate_curve_plots.py`
- `doc/reports/campaign_results/cross_wave/shape_objective/`
- `doc/reports/campaign_results/track_2/verification_plots/`
- `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/README.md`

## Implementation Steps

1. Inspect the current shape-objective closeout report and any existing Track 2
   candidate plot manifests for this pilot or its immediate predecessor.
2. Update the closeout script so the `Pilot Graphs` section is driven by
   Track 2 curve plot manifests and embeds representative
   measured-versus-predicted TE plots.
3. If the shape-objective follow-up has no Track 2 plot manifest yet, prepare
   the report to state that visual promotion evidence is pending and point to
   the exact bounded Track 2 plot command or launcher needed to create it.
4. Regenerate the campaign closeout Markdown and styled PDF.
5. Validate the exported PDF visually, checking that embedded TE plots are
   readable and not clipped.
6. Run touched Markdown checks and Python compile checks for modified report
   tooling.
