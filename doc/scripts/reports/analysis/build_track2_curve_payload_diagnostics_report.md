# TE Curve Verification Pipeline Curve Payload Diagnostics Report Builder

## Overview

`scripts/reports/analysis/build_track2_curve_payload_diagnostics_report.py`
builds the `CVP 1.2` curve-payload diagnostics report for a screened candidate
set.

The script is evaluation-only. It does not train models, does not modify the
dataset structure, and does not provide future curve samples to model inputs.

## Main Role

The report builder reuses the existing `TE Curve Verification Pipeline` candidate loader and held-out
curve records with curve payload export enabled. It computes diagnostics that
explain curve-following quality beyond aggregate `MAE`, `RMSE`, and mean
percentage error.

The main diagnostics are:

- peak-to-peak amplitude error;
- residual peak-to-peak ratio;
- selected-harmonic amplitude error;
- selected-harmonic wrapped phase error;
- local derivative `RMSE`;
- residual smoothness;
- residual lag-one autocorrelation;
- per-revolution closure mismatch;
- deterministic stitched-boundary mismatch surrogate.

## Inputs

By default, the script reads:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`

The default screened candidate set is encoded in the script and can be
overridden with repeated `--candidate-id` arguments.

The default selected harmonic orders are:

- `1`, `2`, `3`, `4`, `5`, `6`, `8`, `10`, `12`, `19`

These can be overridden with repeated `--harmonic-order` arguments.

## Outputs

The script writes machine-readable artifacts under:

- `output/validation_checks/track2_curve_payload_diagnostics/<run_instance_id>/`

The artifact bundle contains:

- `candidate_payload_diagnostics.csv`
- `curve_payload_diagnostics.csv`
- `curve_payload_samples.jsonl`
- `track2_curve_payload_diagnostics_summary.yaml`

The JSONL payload samples are downsampled for repository-size control. The
diagnostics themselves are computed on the full curves.

The dated Markdown report is written under:

- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_payload_diagnostics_report/[YYYY-MM-DD]/`

## Practical Use

Run the default screened diagnostic set from the repository root:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_curve_payload_diagnostics_report.py
```

Refresh the canonical dated report bundle:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_curve_payload_diagnostics_report.py `
  --report-date 2026-05-28
```

Run a smaller candidate set:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_curve_payload_diagnostics_report.py `
  --candidate-id periodic_gru_sequence_Bw `
  --candidate-id harmonic_regression_Bw
```

## Notes

- The runtime input contract remains causal: current point, optional short
  causal history, or derived causal features only.
- Full curves are used only after prediction as the validation and promotion
  surface.
- The diagnostic score is an analysis aid, not a registry-promotion rule.
- Candidate promotion or retraining still requires a separate approved step.
