# Wave 3 Harmonic Prior Residual Campaign Package

This package materializes the approved first real Wave 3 campaign.
It contains 6 runnable queue entries: deterministic pointwise control
and Smooth L1 structured pressure across `global`, `Fw`, and `Bw`
surfaces.

The model predicts the recovered paper harmonic set, reconstructs a
structured base TE curve, and adds a learned causal residual curve.
MDN is not used as the default Wave 3 loss in this package.

## Queue Files

- `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/01_pointwise_control_global.yaml`
- `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/02_pointwise_control_fw.yaml`
- `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/03_pointwise_control_bw.yaml`
- `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/04_smooth_l1_structured_global.yaml`
- `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/05_smooth_l1_structured_fw.yaml`
- `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/06_smooth_l1_structured_bw.yaml`

## Launch Commands

```powershell
.\scripts\campaigns\wave3\run_wave3_harmonic_prior_residual_campaign.ps1 -PreflightOnly
.\scripts\campaigns\wave3\run_wave3_harmonic_prior_residual_campaign.ps1
.\scripts\campaigns\wave3\run_wave3_harmonic_prior_residual_campaign.ps1 -Remote
```
