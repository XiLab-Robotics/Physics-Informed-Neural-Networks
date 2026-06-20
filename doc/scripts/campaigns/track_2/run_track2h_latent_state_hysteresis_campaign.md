# Wave 4.4 Latent-State Hysteresis Campaign Launcher

## Overview

`scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_campaign.ps1`
runs the approved `Wave 4.4` latent-state / hysteresis-aware campaign
package.

The package contains six queue entries:

| Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `gru_offset_residual` | `te_track2h_l_gru_offset_residual_global` | `te_track2h_l_gru_offset_residual_fw` | `te_track2h_l_gru_offset_residual_bw` |
| `causal_tcn_offset_residual` | `te_track2h_l_causal_tcn_offset_residual_global` | `te_track2h_l_causal_tcn_offset_residual_fw` | `te_track2h_l_causal_tcn_offset_residual_bw` |

Each candidate consumes a sequence window ending at the predicted point. The
window contract is causal: `sequence_target_position: last` and
`readout_position: last`.

## Preflight

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1 -PreflightOnly
```

To include one-batch model/loss validation:

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1 -PreflightOnly -RunOneBatchValidation
```

## Local Enqueue Only

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1 -EnqueueOnly
```

## Local Training

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1
```

## Remote Training

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1 -Remote
```

Remote mode delegates to the repository-owned remote campaign launcher and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md`.

## Package Inputs

- queue root:
  `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue`
- planning report:
  `doc/reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- technical document:
  `doc/technical/2026-06/2026-06-16/2026-06-16-16-00-57_track2h_latent_state_hysteresis_package.md`
- validator:
  `scripts/campaigns/track_2/validate_track2h_latent_state_hysteresis_package.py`

## Expected Outputs

Training artifacts are written under:

- `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/`
- `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_fw/`
- `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_bw/`
- `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_global/`
- `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw/`
- `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw/`

Campaign-level artifacts are written under:

- `output/training_campaigns/track2h_latent_state_hysteresis_campaign_2026_06_16/`

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then close the campaign through the normal results report, PDF validation,
registry synchronization, active-state cleanup, backlog/master-summary update,
and only then propose a separate official `TE Curve Verification Pipeline` verification refresh.
