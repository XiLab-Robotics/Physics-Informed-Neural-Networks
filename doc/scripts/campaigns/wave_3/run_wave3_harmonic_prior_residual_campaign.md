# Wave 3 Harmonic Prior Residual Campaign Launcher

## Overview

`scripts/campaigns/wave_3/run_wave3_harmonic_prior_residual_campaign.ps1`
runs the approved first real `Wave 3` harmonic-prior residual campaign.

The package contains six queue entries:

| Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `pointwise_control` | `te_wave3_harmonic_prior_residual_pointwise_control_global` | `te_wave3_harmonic_prior_residual_pointwise_control_fw` | `te_wave3_harmonic_prior_residual_pointwise_control_bw` |
| `smooth_l1_structured` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_fw` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_bw` |

Each candidate predicts a structured harmonic-prior curve and a learned
residual curve. The deterministic playback curve is the final structured plus
residual TE prediction.

## Preflight

Run from the repository root:

```powershell
.\scripts\campaigns\wave_3\run_wave3_harmonic_prior_residual_campaign.ps1 -PreflightOnly
```

To include one-batch model/loss validation:

```powershell
.\scripts\campaigns\wave_3\run_wave3_harmonic_prior_residual_campaign.ps1 -PreflightOnly -RunOneBatchValidation
```

## Local Enqueue Only

```powershell
.\scripts\campaigns\wave_3\run_wave3_harmonic_prior_residual_campaign.ps1 -EnqueueOnly
```

## Local Training

```powershell
.\scripts\campaigns\wave_3\run_wave3_harmonic_prior_residual_campaign.ps1
```

## Remote Training

```powershell
.\scripts\campaigns\wave_3\run_wave3_harmonic_prior_residual_campaign.ps1 -Remote
```

Remote mode delegates to the repository-owned remote campaign launcher and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md`.

## Package Inputs

- queue root:
  `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue`
- planning report:
  `doc/reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- technical document:
  `doc/technical/2026-06/2026-06-14/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_package.md`
- validator:
  `scripts/campaigns/wave_3/validate_wave3_harmonic_prior_residual_campaign.py`

## Expected Outputs

Training artifacts are written under:

- `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_global/`
- `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_fw/`
- `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_bw/`
- `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/`
- `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_fw/`
- `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_bw/`

Campaign-level artifacts are written under:

- `output/training_campaigns/wave3_harmonic_prior_residual_campaign_2026_06_14/`

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then close the campaign through the normal results report, PDF validation,
registry synchronization, active-state cleanup, backlog/master-summary update,
and only then propose a separate official `Track 2` verification refresh.
