# Wave 1 Periodic MLP Explicit Harmonic Tracking Campaign Launcher

## Overview

This launcher runs the approved `Wave 1` periodic MLP explicit harmonic
tracking package. The package compares fixed periodic-feature harmonic banks
for `periodic_mlp` across `global`, `Fw`, and `Bw` direction scopes.

It does not launch `Track 1` paper-faithful workflows, does not change the
pure `feedforward` baseline, and does not define the future `Fourier-Feature
MLP` family. Promotion remains a later closeout decision after scalar and
curve-level review.

## Campaign Package

Prepared campaign root:

- `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign`

Prepared queue count:

- `9` YAML files

Harmonic banks:

- `rcim_sparse`: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- `dense240`: `0..240`
- `dense360`: `0..360`

## Planning Report

This launcher is tied to:

- `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`

## Practical Use

Run the full prepared campaign from the repository root:

```powershell
.\scripts\campaigns\wave1\run_wave1_periodic_mlp_explicit_harmonic_tracking_campaign.ps1
```

Optional Python executable override:

```powershell
.\scripts\campaigns\wave1\run_wave1_periodic_mlp_explicit_harmonic_tracking_campaign.ps1 -PythonExecutable python
```

## Expected Outputs

The shared campaign runner writes campaign artifacts under:

- `output/training_campaigns/wave1/periodic_mlp_explicit_harmonic_tracking/wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49`

Per-run training artifacts are written under each configured
`output/training_runs/<model_family>/` root with immutable run-instance
directories.

## Operator Notes

The launcher clears stale `pending` and `running` queue copies for the prepared
file names before starting. It does not remove completed or failed historical
queue records.
