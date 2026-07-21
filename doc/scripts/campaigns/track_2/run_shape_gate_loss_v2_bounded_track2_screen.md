# Shape-Gate Loss v2 Bounded TE Curve Verification Screen

## Overview

`scripts/campaigns/track_2/run_shape_gate_loss_v2_bounded_track2_screen.ps1`
launches the approved bounded `TE Curve Verification Pipeline` screen for the
`shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` checkpoint.
It is intentionally narrower than the official full matrix: it evaluates only
`polished_dataset`, setpoint inputs, and the forward (`Fw`) surface.

## Candidate Matrix

The launcher uses
`config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw_matrix.yaml`.
The matrix includes the shape-gate loss v2 registry candidate, the previous
shape-gate loss pilot candidate, and the polished-setpoint forward exported
baselines for feedforward, tree, harmonic regression, periodic MLP harmonic,
periodic GRU sequence, Wave 4.1 robust loss, and Wave 4.2 quantile heads.

## Commands

Run a local preflight without launching the matrix:

```powershell
.\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1 `
    -PreflightOnly
```

Run the bounded screen locally:

```powershell
.\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1
```

Run the bounded screen on the remote LAN workstation:

```powershell
.\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1 `
    -Remote
```

The default remote Conda environment is `pinns_env`, matching the validated
LAN workstation environment.

Run a remote preflight only:

```powershell
.\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1 `
    -Remote `
    -PreflightOnly
```

## Outputs

The local and remote paths use the suffix
`shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw`.
Expected outputs include reference-family comparison artifacts under
`output/validation_checks/track2_reference_comparison/`, reranker artifacts
under `output/validation_checks/shape_gated_te_curve_reranker/`, run logs under
`output/validation_checks/track2_operator_launch_logs/`, and the reranker
report under
`doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-21]/`.

## Operating Notes

This launcher is a screening gate, not an automatic promotion workflow. After
the run completes, inspect the generated curve-first and shape-gated evidence
before deciding whether to expand shape-gate loss v2 into a full matrix.
