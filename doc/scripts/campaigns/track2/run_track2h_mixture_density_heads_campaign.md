# Track 2H Mixture Density Heads Campaign Launcher

## Overview

`scripts/campaigns/track2/run_track2h_mixture_density_heads_campaign.ps1`
runs the approved `Track 2H` mixture-density heads campaign package.

The package contains six queue entries:

| Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `mdn_k2` | `te_track2h_mdn_k2_global` | `te_track2h_mdn_k2_fw` | `te_track2h_mdn_k2_bw` |
| `mdn_k3` | `te_track2h_mdn_k3_global` | `te_track2h_mdn_k3_fw` | `te_track2h_mdn_k3_bw` |

Each candidate predicts mixture logits, component means, and component scales.
The deterministic playback curve used by scalar metrics and later official
`Track 2` verification is the mixture expectation.

## Preflight

Run from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1 -PreflightOnly
```

To include one-batch model/loss validation:

```powershell
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1 -PreflightOnly -RunOneBatchValidation
```

## Local Enqueue Only

```powershell
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1 -EnqueueOnly
```

## Local Training

```powershell
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1
```

## Remote Training

```powershell
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1 -Remote
```

Remote mode delegates to the repository-owned remote campaign launcher and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md`.

## Package Inputs

- queue root:
  `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue`
- planning report:
  `doc/reports/campaign_plans/track2/2026-06-13-10-40-25_track2h_mixture_density_heads_campaign_plan_report.md`
- technical document:
  `doc/technical/2026-06/2026-06-13/2026-06-13-10-40-25_track2h_mixture_density_heads_package.md`
- validator:
  `scripts/campaigns/track2/validate_track2h_mixture_density_heads_package.py`

## Expected Outputs

Training artifacts are written under:

- `output/training_runs/track2h_mixture_density_heads_mdn_k2_global/`
- `output/training_runs/track2h_mixture_density_heads_mdn_k2_fw/`
- `output/training_runs/track2h_mixture_density_heads_mdn_k2_bw/`
- `output/training_runs/track2h_mixture_density_heads_mdn_k3_global/`
- `output/training_runs/track2h_mixture_density_heads_mdn_k3_fw/`
- `output/training_runs/track2h_mixture_density_heads_mdn_k3_bw/`

Campaign-level artifacts are written under:

- `output/training_campaigns/track2h_mixture_density_heads_campaign_2026_06_13/`

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then close the campaign through the normal results report, PDF validation,
registry synchronization, active-state cleanup, backlog/master-summary update,
and only then propose a separate official `Track 2` verification refresh.
