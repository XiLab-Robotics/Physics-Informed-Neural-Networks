# Shape-First Distillation Bounded TE Curve Verification Screen

## Overview

`scripts/campaigns/track_2/run_shape_first_distillation_bounded_track2_screen.ps1`
launches the approved bounded `TE Curve Verification Pipeline` screen for the
completed shape-first training-rule distillation pilot. It evaluates only
`polished_dataset`, setpoint inputs, and the forward (`Fw`) surface.

This launcher is a screening gate. It does not promote either shape-first
candidate or update the accepted program baseline by itself.

## Candidate Matrix

The launcher uses
`config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_first_distillation_bounded_track2_screen_polished_setpoints_fw_matrix.yaml`.
The matrix includes the two required polished-setpoint forward baselines and
the two completed pilot candidates:

- `polished_setpoints_periodic_gru_sequence_Fw`
- `polished_setpoints_periodic_mlp_harmonic_Fw`
- `shape_first_distilled_periodic_gru_sequence_Fw`
- `shape_first_distilled_periodic_mlp_harmonic_Fw`

## Commands

Run a local preflight without launching the matrix:

```powershell
.\scripts\campaigns\track_2\run_shape_first_distillation_bounded_track2_screen.ps1 `
    -PreflightOnly
```

Run the bounded screen locally:

```powershell
.\scripts\campaigns\track_2\run_shape_first_distillation_bounded_track2_screen.ps1
```

Run a remote preflight only:

```powershell
.\scripts\campaigns\track_2\run_shape_first_distillation_bounded_track2_screen.ps1 `
    -Remote `
    -PreflightOnly
```

Run the bounded screen on the remote LAN workstation:

```powershell
.\scripts\campaigns\track_2\run_shape_first_distillation_bounded_track2_screen.ps1 `
    -Remote
```

The default remote Conda environment is `pinns_env`, matching the validated
LAN workstation environment.

## Outputs

The local and remote paths use the suffix
`shape_first_distillation_bounded_track2_screen_polished_setpoints_fw`.
Expected outputs include:

- reference-family comparison artifacts under
  `output/validation_checks/track2_reference_comparison/`;
- shape-gated reranker artifacts under
  `output/validation_checks/shape_gated_te_curve_reranker/`;
- run logs under `output/validation_checks/track2_operator_launch_logs/`;
- matrix reports under
  `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`;
- reranker reports under
  `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-22]/`;
- measured-versus-predicted TE curve plot manifests under
  `doc/reports/campaign_results/track_2/verification_plots/shape_first_distillation_bounded_track2_screen_polished_setpoints_fw/`.

## Operating Notes

After the run completes, inspect the generated curve-first evidence before
deciding whether the non-windowed scalar winner should be promoted, rejected,
or kept as a controlled exploratory candidate. The time-windowed candidate
must remain visible in the same screen because the pilot showed better offset
and amplitude behavior for that branch.
