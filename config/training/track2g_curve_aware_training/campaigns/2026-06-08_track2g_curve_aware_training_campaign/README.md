# Track 2G Curve-Aware Training Campaign Package

This package materializes the approved Track 2G curve-aware training
campaign. It contains 12 runnable queue entries: four loss profiles
across `global`, `Fw`, and `Bw` surfaces.

Runtime input remains point or short-history causal. Curve grouping is
used only for training-loss aggregation and offline verification.

## Queue Files

- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/01_pointwise_control_global.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/02_pointwise_control_fw.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/03_pointwise_control_bw.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/04_raw_centered_shape_global.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/05_raw_centered_shape_fw.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/06_raw_centered_shape_bw.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/07_raw_offset_global.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/08_raw_offset_fw.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/09_raw_offset_bw.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/10_full_curve_composite_global.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/11_full_curve_composite_fw.yaml`
- `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/12_full_curve_composite_bw.yaml`

## Launch Commands

```powershell
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1 -PreflightOnly
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1 -Remote
```
