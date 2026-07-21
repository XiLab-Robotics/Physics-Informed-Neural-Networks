# Parallel Shape-Objective Follow-Up Launcher

## Overview

`scripts/campaigns/cross_wave/run_parallel_shape_objective_followup_campaign.ps1`
is the operator-facing launcher for the approved three-arm
`polished_dataset` setpoint `Fw` shape-objective follow-up.

The campaign compares:

- a windowed `periodic_gru_sequence` objective with stronger centered,
  derivative, amplitude, and harmonic pressure;
- a non-windowed `periodic_mlp_harmonic` objective;
- a curve-aware residual objective related to the robust-loss reference family.

## Local Commands

Preflight only:

```powershell
.\scripts\campaigns\cross_wave\run_parallel_shape_objective_followup_campaign.ps1 `
  -PreflightOnly
```

One-batch validation:

```powershell
.\scripts\campaigns\cross_wave\run_parallel_shape_objective_followup_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

Local launch:

```powershell
.\scripts\campaigns\cross_wave\run_parallel_shape_objective_followup_campaign.ps1
```

## Remote Command

```powershell
.\scripts\campaigns\cross_wave\run_parallel_shape_objective_followup_campaign.ps1 `
  -Remote
```

The `-Remote` path delegates source synchronization, remote execution, and
artifact sync-back to
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`.

## Expected Artifacts

- Campaign output:
  `output/training_campaigns/parallel_shape_objective_followup_2026_07_21/`
- Training runs:
  `output/training_runs/shape_objective_followup/`
- Queue state:
  `config/training/queue/shape_objective_followup/parallel_shape_objective_followup_2026_07_21/`
- Family registries:
  `output/registries/families/shape_objective_*_fw/`

## Closeout Requirement

The campaign is not complete until a final campaign-results report includes
pilot graph evidence. The expected graph bundle should include
measured-versus-predicted TE curves, residual/error curves, per-condition
error distributions or heatmaps, and a compact comparison against
`polished_setpoints_periodic_gru_sequence_Fw` and
`polished_setpoints_periodic_mlp_harmonic_Fw`.
