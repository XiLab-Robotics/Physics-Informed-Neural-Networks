# Run Wave 5.2R Stage 11 Uncertainty Trust Calibration

## Purpose

This launcher prepares, validates, and executes the bounded Stage 11
uncertainty and physics-trust calibration campaign. It compares operating
support, analytical disagreement, dense-model disagreement, K01 ensemble
spread, a validation-fitted composite estimator, and matched controls without
changing the frozen K01 mean prediction.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 `
  -PreflightOnly
```

## Local Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 `
  -Run
```

## Remote Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 `
  -Remote -PreflightOnly
```

## Remote Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 `
  -Remote -Run
```

The remote path synchronizes source, configuration, documentation, the frozen
Stage 5 H04 artifacts, the primary Stage 9 K01 checkpoint, and the Stage 10 R00
dense model before execution. It retrieves campaign output, per-candidate
calibration artifacts, ensemble checkpoints, analysis evidence, configuration
state, and active-campaign state after completion.

## Outputs

- `config/training/uncertainty_physics_trust_calibration/`
- `output/training_runs/uncertainty_physics_trust_calibration/`
- `output/training_campaigns/*wave52r_stage11_uncertainty_trust_calibration*`
- `output/analysis/wave_5_2r/stage11_uncertainty_physics_trust_calibration/`
- `doc/running/active_training_campaign.yaml`

## Interpretation

A passing Stage 11 component localizes empirical K01 error using causal
signals. It does not establish a mechanistic probability distribution, promote
K01, or authorize Wave 6.
