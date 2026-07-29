# Run Wave 5.2R Stage 9 Temporal Analytical-Residual Models

## Purpose

The launcher prepares, validates, and optionally runs the Stage 9
forward-only campaign. It compares the accepted periodic GRU replay, a new
causal periodic GRU, matched data-only recurrence, PF-A/H04 point and
coefficient residuals, mean/shape decomposition, context curriculum, and
shuffled angular order.

## Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -Run
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -Remote -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -Remote -Run
```

The remote path synchronizes source, configuration, documents, Stage 0 split
evidence, PF-A/H04 artifacts, the accepted periodic-GRU checkpoint, campaign
outputs, immutable runs, Stage 9 analysis, generated configuration, and
persistent campaign state.

## Outputs

- campaign configuration under
  `config/training/temporal_analytical_residual_models/`;
- preflight and accepted-GRU replay evidence under
  `output/analysis/wave_5_2r/stage9_temporal_analytical_residual_models/`;
- immutable runs under
  `output/training_runs/temporal_analytical_residual_models/`;
- campaign bookkeeping under `output/training_campaigns/`;
- persistent state in `doc/running/active_training_campaign.yaml`.
