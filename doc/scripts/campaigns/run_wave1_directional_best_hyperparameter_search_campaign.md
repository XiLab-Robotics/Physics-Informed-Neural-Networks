# Wave 1 Directional Best Hyperparameter Search Campaign Launcher

## Overview

This launcher executes the mixed best-hyperparameter search package for the
`15` directional `Wave 1` winner surfaces.

It is split into two phases:

1. bounded CPU grid execution for `tree` and `harmonic_regression`;
2. GPU-dispatched `Optuna` studies for the three neural families.

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

Explicit Python executable:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_best_hyperparameter_search_campaign.ps1 -PythonExecutable python -GpuIdList 0,1
```
