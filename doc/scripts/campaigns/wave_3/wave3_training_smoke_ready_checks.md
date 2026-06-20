# Wave 5.1 Training-Smoke-Ready Checks

## Purpose

`run_wave3_training_smoke_ready_checks.ps1` validates that the embryonic
`Wave 5.1` harmonic-prior residual skeleton can pass through the shared
one-batch training setup. It is a dry-run validation launcher only.

## Command

```powershell
.\scripts\campaigns\wave_3\run_wave3_training_smoke_ready_checks.ps1
```

## What It Runs

- Python compile check for the Wave 5.1 training-smoke-ready validator.
- Generation of a validation-only complete config from the committed Wave 5.1
  template and a stable Wave 3.3 sequence base config.
- Repository-owned `validate_training_setup.py` one-batch validation.
- Validation artifact output under `output/validation_checks/`.

## Campaign Boundary

This launcher does not enqueue YAML files, launch a campaign, update
`doc/running/active_training_campaign.yaml`, update registries, or run official
`TE Curve Verification Pipeline` verification. Real Wave 5.1 training remains blocked on `Wave 4 series`
results and a later approved campaign plan.
