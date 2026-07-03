# TE Curve Verification Pipeline Multi-Model Curve Comparison Report

## Overview

Create a styled `TE Curve Verification Pipeline` PDF report analogous to the completed best-model
collage report, but focused on direct multi-model curve overlays. The report
will compare the measured/original TE curve against selected reference and
Wave 1 models on the same axes so the harmonic tracking differences can be
inspected model-by-model and branch-by-branch.

The report will cover:

- forward reference overlays:
  `original curve`, `paper_original_best_Fw`, `paper_retuned_best_Fw`, and
  `track1_best_Fw`;
- backward reference overlays:
  `original curve`, `paper_retuned_best_Bw`, and `track1_best_Bw`;
- forward Wave 1 overlays:
  `original curve` plus the current Wave 1 family-best forward models;
- backward Wave 1 overlays:
  `original curve` plus the current Wave 1 family-best backward models;
- forward and backward combined overlays:
  `original curve`, the matching `track1_best_Fw` or `track1_best_Bw`, and a
  screened subset of the strongest Wave 1 family-best models.

## Technical Approach

Add a repeatable analysis/report script beside the existing curve-verification collage
builder. The new script will reuse the same model-loading and TE Curve Verification Pipeline dataset
evaluation path already used by
`scripts/reports/analysis/build_track2_best_model_collage_report.py`, but will
plot multiple selected candidates together on each curve instead of one model
per collage.

The implementation will:

- reuse the current curve-verification comparison configuration and candidate metadata
  from the reference-family-vs-feedforward support code;
- reuse current Wave 1 family registries under
  `output/registries/families/`;
- render `original curve` as the measured TE curve with the same dark-gray,
  normal-width style used in the latest TE Curve Verification Pipeline plot refresh;
- generate deterministic representative curve collages for each requested
  comparison group;
- calculate curve-level and group-level metrics for every included model;
- screen the combined RCIM Model-Bank Reproduction plus Wave 1 comparison to keep the strongest
  Wave 1 candidates by `Curve MAE [deg]` within the relevant direction;
- write a dated Markdown report and export the real styled PDF;
- validate the exported PDF with the repository PDF validation tool and inspect
  rasterized pages for line readability, clipping, and page breaks.

## Involved Components

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/plot_wave1_best_model_te_curves.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `output/registries/families/*/latest_family_best.yaml`
- `output/validation_checks/track2_best_model_curve_comparison_report/`
- `doc/reports/analysis/te_curve_verification_pipeline/`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Inspect the existing curve-verification collage builder and the plot styling from
   commit `97c9d9cd1f9971d813c975c0fff058b5aeef0f67`.
2. Add a dedicated report builder for multi-model TE Curve Verification Pipeline curve overlays.
3. Build the requested forward, backward, Wave 1, and screened combined
   comparison groups.
4. Generate deterministic four-curve collages per group and store metrics plus
   plot artifacts under a timestamped validation-check directory.
5. Write the dated Markdown report and add the report to the documentation
   indices and usage guide.
6. Export the styled PDF and validate the real PDF output.
7. Run Python syntax checks, scoped Markdown QA, and the Sphinx documentation
   build before reporting completion.

No subagent use is planned for this task.
