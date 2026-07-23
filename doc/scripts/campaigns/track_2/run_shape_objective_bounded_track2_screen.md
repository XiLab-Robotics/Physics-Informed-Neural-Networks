# Shape-Objective Bounded TE Curve Verification Screen

## Overview

`scripts/campaigns/track_2/run_shape_objective_bounded_track2_screen.ps1`
launches the approved bounded `TE Curve Verification Pipeline` screen for the
`shape_objective_periodic_mlp_harmonic_fw` checkpoint. It evaluates only
`polished_dataset`, setpoint inputs, and the forward (`Fw`) surface.

This launcher is a screening gate. It does not promote the model or update the
accepted program baseline by itself.

The screen is standalone once its matrix configuration, model inventories,
registered shape-objective family artifact, and launcher note are present. It
may run after a previously prepared active campaign state has been closed; in
that case the launcher reports the current active-state status and continues
from its own bounded-screen contract.

## Candidate Matrix

The launcher uses
`config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_objective_bounded_track2_screen_polished_setpoints_fw_matrix.yaml`.
The matrix includes the shape-objective registry candidate and the two required
polished-setpoint forward baselines:

- `shape_objective_periodic_mlp_harmonic_Fw`
- `polished_setpoints_periodic_gru_sequence_Fw`
- `polished_setpoints_periodic_mlp_harmonic_Fw`

## Commands

Run a local preflight without launching the matrix:

```powershell
.\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1 `
    -PreflightOnly
```

Run the bounded screen locally:

```powershell
.\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1
```

Run the bounded screen on the remote LAN workstation:

```powershell
.\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1 `
    -Remote
```

Run a remote preflight only:

```powershell
.\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1 `
    -Remote `
    -PreflightOnly
```

The default remote Conda environment is `pinns_env`, matching the validated
LAN workstation environment.

## Outputs

The local and remote paths use the suffix
`shape_objective_bounded_track2_screen_polished_setpoints_fw`. Expected outputs
include:

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
  `doc/reports/campaign_results/track_2/verification_plots/shape_objective_bounded_track2_screen_polished_setpoints_fw/`.

The launcher runs the bounded Track 2 plot builder explicitly after the matrix
and shape-gated reranker steps. It generates up to two measured-versus-predicted
TE curve overlays per candidate for compact pilot review.

## Operating Notes

After the run completes, inspect the generated curve-first evidence before
deciding whether to expand the shape-objective periodic MLP harmonic family
into a broader full-matrix or Fw/Bw campaign.

Remote sync output is intentionally quiet. The terminal reports the
repository-owned sync stage and per-path source summary instead of raw `scp`
progress bars, and the temporary artifact bundle is removed locally after it is
expanded.
