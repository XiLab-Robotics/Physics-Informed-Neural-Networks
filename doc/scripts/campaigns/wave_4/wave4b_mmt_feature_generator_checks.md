# Wave 5.2B MMT Feature Generator Checks

## Purpose

`run_wave4b_mmt_feature_generator_checks.ps1` validates the `Wave 5.2B` MMT
feature-generator skeleton. It is a dry-run check launcher only. It must not
enqueue or launch training.

## Command

```powershell
.\scripts\campaigns\wave_4\run_wave4b_mmt_feature_generator_checks.ps1
```

## What It Runs

- Python compile check for the `Wave 5.2B` feature generator and validator.
- Template metadata validation for `implementation-ready` and
  `not campaign-ready` status.
- Dry-run MMT feature schema generation.
- Sample MMT analytical feature generation from the `Wave 5.2A` diagnostic curve.
- Leakage-boundary validation that target-derived residual fields are not
  exposed as inference features.

## Outputs

The validator writes dry-run artifacts under:

```text
output/validation_checks/wave4b_mmt_feature_generator/
```

The expected files are:

- `wave4b_mmt_feature_schema.csv`;
- `wave4b_mmt_sample_features.csv`;
- `wave4b_mmt_harmonic_features.csv`;
- `wave4b_mmt_feature_generator_summary.yaml`.

## Campaign Boundary

Real `Wave 5.2B` feature-augmented training remains blocked until the separate
`Wave 4.2` quantile / probabilistic campaign is closed out and a new campaign
plan explicitly approves queue size, surfaces, losses, and feature consumers.
