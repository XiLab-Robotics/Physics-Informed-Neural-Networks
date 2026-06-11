# Wave 3 Training-Smoke-Ready Checks

## Purpose

`run_wave3_training_smoke_ready_checks.ps1` validates that the embryonic
`Wave 3` harmonic-prior residual skeleton can pass through the shared
one-batch training setup. It is a dry-run validation launcher only.

## Command

```powershell
.\scripts\campaigns\wave3\run_wave3_training_smoke_ready_checks.ps1
```

## What It Runs

- Python compile check for the Wave 3 training-smoke-ready validator.
- Generation of a validation-only complete config from the committed Wave 3
  template and a stable Track 2G sequence base config.
- Repository-owned `validate_training_setup.py` one-batch validation.
- Validation artifact output under `output/validation_checks/`.

## Campaign Boundary

This launcher does not enqueue YAML files, launch a campaign, update
`doc/running/active_training_campaign.yaml`, update registries, or run official
`Track 2` verification. Real Wave 3 training remains blocked on `Track 2H`
results and a later approved campaign plan.
