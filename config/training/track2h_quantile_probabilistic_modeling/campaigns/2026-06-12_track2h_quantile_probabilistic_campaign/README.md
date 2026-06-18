# Track 2H Quantile Probabilistic Campaign Package

This package materializes the approved second Track 2H
dispersion-aware probe. It contains 6 runnable queue entries:
`quantile_p10_p50_p90` and `gaussian_nll` across `global`, `Fw`,
and `Bw` surfaces.

Deterministic Track 2 playback uses `p50` for quantile runs and
`mu` for Gaussian runs. The extra channels are training and
calibration diagnostics, not future-looking inference inputs.

## Queue Files

- `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/01_quantile_p10_p50_p90_global.yaml`
- `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/02_quantile_p10_p50_p90_fw.yaml`
- `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/03_quantile_p10_p50_p90_bw.yaml`
- `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/04_gaussian_nll_global.yaml`
- `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/05_gaussian_nll_fw.yaml`
- `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/06_gaussian_nll_bw.yaml`

## Launch Commands

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1 -PreflightOnly
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1 -Remote
```
