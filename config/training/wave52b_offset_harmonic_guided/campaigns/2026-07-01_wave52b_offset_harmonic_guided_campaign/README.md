# Wave 5.2B Offset And Harmonic Guided Campaign Package

This package materializes the approved Wave 5.2B campaign on `polished_dataset`.
It contains 12 runnable queue entries: four ablation profiles across
`global`, `Fw`, and `Bw` surfaces.

## Manifest

- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/campaign.yaml`

## Queue Files

- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/001_pointwise_control_global.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/002_pointwise_control_fw.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/003_pointwise_control_bw.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/004_offset_head_global.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/005_offset_head_fw.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/006_offset_head_bw.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/007_offset_centered_shape_global.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/008_offset_centered_shape_fw.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/009_offset_centered_shape_bw.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/010_offset_centered_shape_harmonic_global.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/011_offset_centered_shape_harmonic_fw.yaml`
- `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/012_offset_centered_shape_harmonic_bw.yaml`

## Launch Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -Remote
```
