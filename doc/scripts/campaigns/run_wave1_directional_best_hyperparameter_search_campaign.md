# Wave 1 Directional Best Hyperparameter Search Campaign Launcher

## Overview

This launcher executes the mixed best-hyperparameter search package for the
`15` directional `Wave 1` winner surfaces.

It is split into two phases:

1. bounded CPU grid execution for `tree` and `harmonic_regression`;
2. GPU-dispatched `Optuna` studies for the three neural families.

## Terminal Behavior

When launched with a single GPU id such as `-GpuIdList 0`, the neural
`Optuna` phase runs in interactive terminal mode:

- native `PyTorch Lightning` progress bars stay visible in the launching
  terminal;
- `CTRL+C` can stop the active study from that same console session;
- the visible terminal session is also copied into
  `output/training_campaigns/.../launcher_logs/<study>.console.log` and
  mirrored into `<study>.stdout.log`.

When launched with multiple GPU ids such as `-GpuIdList 0,1`, the launcher
falls back to detached parallel study execution. That fallback preserves the
parallel GPU usage, but native terminal progress streaming and direct `CTRL+C`
propagation are not guaranteed in that mode.

## Preparation Dependency

The launcher assumes the campaign package already exists under:

- `config/training/wave1_directional_best_hyperparameter_search/campaigns/2026-05-11_wave1_directional_best_hyperparameter_search_campaign/`

If the package is missing, rebuild it first with:

```powershell
python -B .\scripts\campaigns\wave1\prepare_wave1_directional_best_hyperparameter_search_campaign.py
```

## Planning Report

This launcher is tied to:

- `doc/reports/campaign_plans/wave1/2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md`

## Practical Use

Run the full mixed campaign with two visible GPU slots:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_best_hyperparameter_search_campaign.ps1 -GpuIdList 0,1
```

Minimal single-GPU usage:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_best_hyperparameter_search_campaign.ps1 -GpuIdList 0
```

Single-GPU resume of the neural phase only, with live terminal streaming:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_best_hyperparameter_search_campaign.ps1 -SkipGridPhase -GpuIdList 0
```

Explicit Python executable:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_best_hyperparameter_search_campaign.ps1 -PythonExecutable python -GpuIdList 0,1
```
