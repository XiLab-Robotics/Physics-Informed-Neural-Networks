# Wave 4 series Dispersion-Aware Modeling Campaign Package

This package materializes the approved first Wave 4.1 robust-loss
probe. It contains 9 runnable queue entries: three robust pointwise
losses across `global`, `Fw`, and `Bw` surfaces.

The MSE pointwise-control baseline is the already verified Wave 3.3
pointwise-control set. Runtime input remains causal point or
short-history sequence input.

## Queue Files

- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/01_mae_robust_global.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/02_mae_robust_fw.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/03_mae_robust_bw.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/04_smooth_l1_robust_global.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/05_smooth_l1_robust_fw.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/06_smooth_l1_robust_bw.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/07_log_cosh_robust_global.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/08_log_cosh_robust_fw.yaml`
- `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/09_log_cosh_robust_bw.yaml`

## Launch Commands

```powershell
.\scripts\campaigns\track_2\run_track2h_dispersion_aware_modeling_campaign.ps1 -PreflightOnly
.\scripts\campaigns\track_2\run_track2h_dispersion_aware_modeling_campaign.ps1
.\scripts\campaigns\track_2\run_track2h_dispersion_aware_modeling_campaign.ps1 -Remote
```
