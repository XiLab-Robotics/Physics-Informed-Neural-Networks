# Track 2H-L Latent-State Hysteresis Campaign Package

This package materializes the approved Track 2H-L latent-state /
hysteresis-aware probe. It contains 6 runnable queue entries:
`gru_offset_residual` and `causal_tcn_offset_residual` across
`global`, `Fw`, and `Bw` surfaces.

All entries use `sequence_target_position: last` and
`readout_position: last`, so the latent state is estimated only from
the current and previous operating-state samples in the window.

## Queue Files

- `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/01_gru_offset_residual_global.yaml`
- `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/02_gru_offset_residual_fw.yaml`
- `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/03_gru_offset_residual_bw.yaml`
- `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/04_causal_tcn_offset_residual_global.yaml`
- `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/05_causal_tcn_offset_residual_fw.yaml`
- `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/06_causal_tcn_offset_residual_bw.yaml`

## Launch Commands

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1 -PreflightOnly
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_campaign.ps1 -Remote
```
