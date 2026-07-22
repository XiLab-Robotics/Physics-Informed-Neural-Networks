# Causal Offset Mean Calibration Pilot Launcher

## Overview

`scripts/campaigns/cross_wave/run_causal_offset_mean_calibration_pilot_campaign.ps1`
validates or launches the approved two-arm causal offset / mean calibration
pilot.

The pilot is scoped to `polished_dataset` with `setpoints` inputs and the `Fw`
surface. It keeps both a time-windowed candidate and a non-windowed harmonic
candidate active, then requires a later bounded `TE Curve Verification
Pipeline` screen before any promotion decision.

## Primary Paths

- manifest:
  `config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/campaign.yaml`
- queue configs:
  `config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/queue/001_causal_offset_mean_gru_sequence_fw.yaml`
  `config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/queue/002_causal_offset_mean_periodic_mlp_harmonic_fw.yaml`
- planning report:
  `doc/reports/campaign_plans/cross_wave/causal_offset_mean_calibration/2026-07-22-17-42-11_causal_offset_mean_calibration_pilot_plan_report.md`
- technical document:
  `doc/technical/2026-07/2026-07-22/2026-07-22-17-38-44_causal_offset_mean_calibration_pilot.md`
- model report:
  `doc/reports/analysis/model_development_waves/wave_5_2/causal_offset_mean_calibration/[2026-07-22]/causal_offset_mean_calibration_pilot_model_report.md`

## Preflight

Check that the package paths resolve without launching training:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
  -PreflightOnly
```

Run one-batch validation without launching a campaign:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

## Local Launch

Launch the local pilot campaign:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1
```

Queue the local pilot without training:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
  -EnqueueOnly
```

## Remote Launch

Launch the pilot through the repository-owned remote campaign workflow:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
  -Remote
```

The remote path syncs source, config, docs, site metadata, requirements, and
`AGENTS.md` before launch through
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`.

## Closeout Rule

Normal pilot closeout must inspect campaign artifacts and then evaluate the
trained artifacts with a bounded curve-first screen against both the accepted
windowed GRU and best non-windowed harmonic forward baselines.
