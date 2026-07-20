# Shape-Gate Loss Pilot Campaign Launcher

## Overview

`scripts/campaigns/cross_wave/run_shape_gate_loss_pilot_campaign.ps1`
validates or launches the approved shape-gate loss pilot campaign.

The pilot is intentionally scoped to `polished_dataset` with `setpoints` inputs
and the `Fw` surface. It is not a full promotion campaign. A promotable follow
up must cover `simplified_setpoints`, `polished_setpoints`, and
`polished_actual_values`, each across `global`, `Fw`, and `Bw`.

## Primary Paths

- manifest:
  `config/training/shape_gate_loss_pilot/campaigns/2026-07-20_shape_gate_loss_pilot/campaign.yaml`
- queue config:
  `config/training/shape_gate_loss_pilot/campaigns/2026-07-20_shape_gate_loss_pilot/queue/001_shape_gate_loss_periodic_gru_sequence_fw.yaml`
- planning report:
  `doc/reports/campaign_plans/cross_wave/shape_gate_loss/2026-07-20-19-10-23_shape_gate_loss_pilot_campaign_plan_report.md`
- technical document:
  `doc/technical/2026-07/2026-07-20/2026-07-20-18-10-35_shape_gate_loss_pilot_and_full_surface_campaign.md`

## Preflight

Check that the package paths resolve without launching training:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_pilot_campaign.ps1 -PreflightOnly
```

Run one-batch validation without launching a campaign:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_pilot_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

## Local Launch

Launch the local pilot campaign:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_pilot_campaign.ps1
```

Queue the local pilot without training:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_pilot_campaign.ps1 `
  -EnqueueOnly
```

## Remote Launch

Launch the pilot through the repository-owned remote campaign workflow:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_pilot_campaign.ps1 -Remote
```

The remote path syncs source, config, docs, site metadata, requirements, and
`AGENTS.md` before launch through
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`.

## Closeout Rule

Normal pilot closeout must inspect campaign artifacts and then evaluate the
trained artifact with the calibrated shape-gated reranker. The heavy official
`TE Curve Verification Pipeline` matrix is a separate operator-approved step,
not part of this launcher.
