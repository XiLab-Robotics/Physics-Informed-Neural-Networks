# Wave 1 High-Order Harmonic Tracking Campaign Launcher

## Overview

This launcher runs the approved `Wave 1` high-order harmonic tracking package.
The package compares new harmonic bases for `harmonic_regression` and
`residual_harmonic_mlp` across `global`, `Fw`, and `Bw` direction scopes.

It does not launch `Track 1` paper-faithful workflows and does not change model
archives directly. Promotion remains a later closeout decision after scalar and
curve-level review.

## Campaign Package

Prepared campaign root:

- `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign`

Prepared queue count:

- `18` YAML files

Harmonic banks:

- `rcim_sparse`: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- `dense240`: `0..240`
- `dense360`: `0..360`

## Planning Report

This launcher is tied to:

- `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`

## Practical Use

Run the full prepared campaign from the repository root:

```powershell
.\scripts\campaigns\wave1\run_wave1_high_order_harmonic_tracking_campaign.ps1
```

Optional Python executable override:

```powershell
.\scripts\campaigns\wave1\run_wave1_high_order_harmonic_tracking_campaign.ps1 -PythonExecutable python
```

## Expected Outputs

The shared campaign runner writes campaign artifacts under:

- `output/training_campaigns/wave1/high_order_harmonic_tracking/wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01`

Per-run training artifacts are written under each configured
`output/training_runs/<model_family>/` root with immutable run-instance
directories.

## Operator Notes

The launcher clears stale `pending` and `running` queue copies for the prepared
file names before starting. It does not remove completed or failed historical
queue records.
