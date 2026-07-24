# Reduced Non-MMT TE Curve Verification Reports Launcher

## Overview

This launcher prepares the next cross-wave comparison after the decision to
defer MMT. It evaluates six direction-separated cells:

- polished setpoints, forward and backward;
- simplified setpoints, forward and backward;
- polished actual values, forward and backward.

The launcher is evaluation-only. It does not train models, change the accepted
program baseline, or generate an official promotion decision.

The following work remains paused:

- `global` evaluation;
- MMT candidates;
- best-model collages;
- multi-model overlays;
- dataset-difference reports;
- broad full-directional matrix regeneration.

## Dry Run

Print the six-cell execution plan without evaluating candidates:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1
```

The remote flag is also safe without `-Run`; it prints the remote plan and
does not connect to the workstation:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 -Remote
```

## Local Run

Run the six cells locally:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 -Run
```

Resume from a named cell without recomputing earlier cells:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 `
  -Run `
  -ResumeFromStep 05_matrix_polished_actual_values_forward
```

The valid step names are:

1. `01_matrix_polished_setpoints_forward`;
2. `02_matrix_polished_setpoints_backward`;
3. `03_matrix_simplified_setpoints_forward`;
4. `04_matrix_simplified_setpoints_backward`;
5. `05_matrix_polished_actual_values_forward`;
6. `06_matrix_polished_actual_values_backward`.

## Remote Run

Run the same six cells on the configured LAN workstation:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 `
  -Remote `
  -Run
```

The launcher uses `xilab-remote` by default. Override the repository path or
environment when necessary:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 `
  -Remote `
  -Run `
  -RemoteRepositoryPath "C:\path\to\remote\repository" `
  -RemoteCondaEnvironmentName "pinns_env"
```

Before remote execution, the launcher synchronizes the required scripts,
matrix configurations, launcher documentation, campaign state, and selected
model archives. The remote polished and simplified dataset roots must already
exist. After completion, the launcher synchronizes the six reports, matrix
artifacts, and operator logs back into the local canonical repository.

## Candidate Matrices

The launcher uses three dataset- and input-mode-specific matrices:

- `selected_active_track2_polished_setpoints_matrix.yaml`;
- `selected_active_track2_simplified_setpoints_matrix.yaml`;
- `selected_active_track2_polished_actual_values_matrix.yaml`.

All six cells include these active cross-wave candidates:

- `periodic_gru_sequence`;
- `periodic_mlp_harmonic`;
- `wave4_1_mae_robust_loss`;
- `wave4_2_quantile_p10_p50_p90`.

The compact anchor set is:

- `feedforward`;
- `tree`;
- `harmonic_regression`.

The polished actual-value cells additionally include:

- `residual_harmonic_gru_sequence_sparse_rcim`;
- `residual_harmonic_lstm_sequence_sparse_rcim`.

Candidate interpretation must follow the canonical multi-index curve-first
policy. Scalar `MAE` or matrix rank alone cannot promote a model.

## Expected Outputs

Final Markdown reports are moved into:

- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[YYYY-MM-DD]/`.

The filenames include dataset, input mode, and direction so polished setpoint
and actual-value reports cannot overwrite each other.

Validation summaries and per-condition metrics remain under:

- `output/validation_checks/track2_reference_comparison/`.

Operator logs and the artifact sync manifest are written under:

- `output/validation_checks/track2_operator_launch_logs/`.

After the operator reports successful completion, inspect the six report cells
under the multi-index curve-first policy before deciding whether an official
verification refresh or any promotion work is justified.
