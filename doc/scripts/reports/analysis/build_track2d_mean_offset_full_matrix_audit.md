# CVP 1.4 Mean-Offset Full-Matrix Audit Builder

## Overview

`scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py`
builds the `CVP 1.4` full-matrix diagnostic report for mean-offset and
centered-shape behavior.

The script is evaluation-only. It does not train models, does not update
registries, does not change the dataset, and does not pass future curve
samples to a runtime model.

## Main Role

The builder evaluates every direction-valid candidate from the official
`TE Curve Verification Pipeline` matrix through the normal causal prediction path, then decomposes the
curve residuals into:

- raw `MAE` and `RMSE`;
- signed and absolute curve-bias / `DC` offset;
- mean-centered `MAE` and `RMSE`;
- raw-to-centered improvement;
- peak-to-peak amplitude error;
- selected sparse-`RCIM` harmonic amplitude and phase error;
- condition-stratified summaries by direction, speed, torque, and oil
  temperature.

The generated diagnostic labels are analysis aids only. They are not automatic
promotion decisions.

## Inputs

By default, the script reads:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- model archives and registries referenced by the curve-verification matrix config
- the canonical held-out TE curve records resolved by the TE Curve Verification Pipeline support code

Optional CLI filters can restrict execution to one or more candidate ids.

## Outputs

The script writes machine-readable artifacts under:

- `output/validation_checks/track2d_mean_offset_full_matrix_audit/<run_instance_id>/`

The artifact bundle contains:

- `track2d_per_curve_metrics.csv`
- `track2d_candidate_summary.csv`
- `track2d_surface_leaderboard.csv`
- `track2d_condition_stratified_summary.csv`
- `track2d_mean_offset_full_matrix_audit_summary.yaml`

The dated Markdown report is written under:

- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[YYYY-MM-DD]/`

## Practical Use

Run the default full-matrix audit:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py
```

Refresh a dated report bundle:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py `
  --report-date 2026-06-03
```

Run a filtered smoke check:

```powershell
python -B scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py `
  --candidate-id harmonic_regression_global `
  --report-date 2026-06-03
```

Run a chunk of the full candidate matrix:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py `
  --candidate-start-index 1 `
  --candidate-end-index 12 `
  --report-date 2026-06-03
```

Merge completed chunks into the final report without re-running inference:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py `
  --merge-only `
  --report-date 2026-06-03
```

## Notes

- Full curves are used only after inference as the diagnostic surface.
- Mean-centering subtracts each curve's measured and predicted means
  separately after inference.
- A large raw-to-centered improvement indicates an offset-limited candidate.
- A small raw-to-centered improvement with high centered error indicates a
  centered-shape, amplitude, or phase limitation.
- `Fw`, `Bw`, and `global` surfaces must remain parallel interpretation
  branches.
