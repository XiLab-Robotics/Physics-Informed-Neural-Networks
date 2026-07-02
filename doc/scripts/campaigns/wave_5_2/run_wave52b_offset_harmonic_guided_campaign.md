# Wave 5.2B Offset And Harmonic Guided Campaign Launcher

## Overview

`scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.ps1`
runs the approved Wave 5.2B offset and harmonic guided campaign on
`polished_dataset`.

The package contains 12 queue entries:

| Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `pointwise_control` | `te_wave52b_offset_harmonic_guided_pointwise_control_global` | `te_wave52b_offset_harmonic_guided_pointwise_control_fw` | `te_wave52b_offset_harmonic_guided_pointwise_control_bw` |
| `offset_head` | `te_wave52b_offset_harmonic_guided_offset_head_global` | `te_wave52b_offset_harmonic_guided_offset_head_fw` | `te_wave52b_offset_harmonic_guided_offset_head_bw` |
| `offset_centered_shape` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_global` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_fw` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_bw` |
| `offset_centered_shape_harmonic` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` |

Each candidate keeps a direct base head, an explicit residual offset head, and
an optional sparse RCIM harmonic branch. The ablation profile decides which
branch contributions and curve-aware loss terms are active.

## Preflight

Run from the repository root:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -PreflightOnly
```

To include one-batch model/loss validation:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -PreflightOnly -RunOneBatchValidation
```

## Local Enqueue Only

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -EnqueueOnly
```

## Local Training

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1
```

## Remote Training

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -Remote
```

Remote mode delegates to the repository-owned remote campaign launcher and
syncs `scripts`, `config`, `doc`, `site`, `requirements.txt`, and `AGENTS.md`.

## Package Inputs

- manifest:
  `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/campaign.yaml`
- queue root:
  `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue`
- planning report:
  `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- technical document:
  `doc/technical/2026-07/2026-07-01/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_preparation.md`
- model report:
  `doc/reports/analysis/wave5_2/Wave 5.2B Offset And Harmonic Guided Model.md`
- validator:
  `scripts/campaigns/wave_5_2/validate_wave52b_offset_harmonic_guided_campaign.py`

## Expected Outputs

Training artifacts are written under the 12
`output/training_runs/wave52b_offset_harmonic_guided_*` family directories.

Campaign-level artifacts are written under:

- `output/training_campaigns/wave52b_offset_harmonic_guided_campaign_2026_07_01/`

## Boundary

This launcher does not run the `TE Curve Verification Pipeline`. After the
campaign completes, close out the training campaign first, then prepare a
separate operator-approved verification refresh if the results justify it.
