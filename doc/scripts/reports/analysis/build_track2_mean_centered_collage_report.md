# TE Curve Verification Pipeline Mean-Centered Collage Diagnostics Report Builder

## Overview

`scripts/reports/analysis/build_track2_mean_centered_collage_report.py` builds
the `TE Curve Verification Pipeline` mean-centered collage diagnostics report from the existing
best-model collage selections.

The script is evaluation-only. It does not train models, does not modify the
dataset structure, and does not supply future curve samples to the model path.

## Main Role

The report builder tests whether persistent vertical prediction offsets hide
better `TE` waveform tracking in the current `TE Curve Verification Pipeline` collage candidates. For
each candidate and selected curve, it subtracts the truth curve mean from the
truth curve and the prediction curve mean from the prediction curve, then
recomputes curve `MAE` and `RMSE`.

This produces a shape-first diagnostic view that separates:

- mean offset error;
- residual waveform-shape error after mean-centering;
- the percentage improvement obtained by removing each curve's own mean.

The mean-centered metrics are not a deployment rule. They are a diagnostic
signal for future training losses, calibration checks, and candidate triage.

## Inputs

By default, the script reads:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `output/validation_checks/track2_best_model_collage_report/2026-05-28-13-37-39__track2_best_model_collage_report/track2_best_model_collage_summary.yaml`

The source collage summary provides the deterministic four-curve selection per
candidate so the new centered collages remain directly comparable with the
offsets observed in the original `TE Curve Verification Pipeline` best-model collage PDF.

## Outputs

The script writes machine-readable artifacts under:

- `output/validation_checks/track2_mean_centered_collage_report/<run_instance_id>/`

The artifact bundle contains:

- `track2_mean_centered_candidate_metrics.csv`
- `track2_mean_centered_per_curve_metrics.csv`
- `track2_mean_centered_collage_summary.yaml`
- mean-centered collage PNG files grouped by candidate section

The dated Markdown report is written under:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/mean_centered_collage_report/[YYYY-MM-DD]/`

## Practical Use

Run the default diagnostic from the repository root:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_mean_centered_collage_report.py
```

Refresh a dated report bundle:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_mean_centered_collage_report.py `
  --report-date 2026-06-02
```

Use a different source collage summary:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_mean_centered_collage_report.py `
  --source-collage-summary "output/validation_checks/track2_best_model_collage_report/<run_instance_id>/track2_best_model_collage_summary.yaml"
```

## Notes

- The runtime input contract remains causal: current point, optional short
  causal history, or derived causal features only.
- Full curves are used only after prediction as the diagnostic comparison
  surface.
- Mean-centering subtracts each curve's measured and predicted means
  separately after inference.
- A large improvement indicates that candidate shape tracking may be stronger
  than its raw offset collage suggests.
- A small improvement indicates that the residual waveform shape remains poor
  even after removing the vertical offset.
