# Run Wave 5.2R Stage 8 Weak Forward Compliance Priors

## Purpose

The launcher prepares, validates, and optionally runs the Stage 8
forward-only campaign. It builds a training-only compliance bootstrap and
compares weak sign, broad-bound, confidence, temperature, curriculum,
adaptive, shuffled, and hard-equation formulations above H04.

## Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -Run
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -Remote -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -Remote -Run
```

The remote path synchronizes the required source, configuration, documents,
H04 checkpoint, Phase 3 evidence, campaign outputs, immutable runs, Stage 8
analysis, generated configuration, and persistent campaign state.

## Outputs

- campaign configuration under
  `config/training/weak_forward_compliance_priors/`;
- bootstrap and preflight evidence under
  `output/analysis/wave_5_2r/stage8_weak_forward_compliance_priors/`;
- immutable runs under
  `output/training_runs/weak_forward_compliance_priors/`;
- campaign bookkeeping under `output/training_campaigns/`;
- persistent state in `doc/running/active_training_campaign.yaml`.
