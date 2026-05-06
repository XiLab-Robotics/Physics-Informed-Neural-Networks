# Wave 1 Directional Retraining Campaign Launcher

## Overview

This launcher wraps the approved `Wave 1` directional retraining package that
replays the current best configuration of each implemented family under three
explicit data scopes:

1. `global`
2. `Fw`
3. `Bw`

It does not prepare `Track 1` assets and it does not modify the currently
running protected campaign state.

## Main Role

The launcher:

1. changes to the repository root;
2. removes stale pending or running queue copies for the same `Wave 1`
   directional package;
3. assembles the `15` approved queue YAML files;
4. forwards those YAML files to `scripts/training/run_training_campaign.py`;
5. preserves the normal campaign logs, queue movement, and leaderboard writes
   produced by the shared runner.

## Preparation Dependency

The launcher assumes the campaign package has already been prepared under:

- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/`

If the package is missing, rebuild it first with:

```powershell
python -B .\scripts\campaigns\wave1\prepare_wave1_directional_retraining_campaign.py
```

## Planning Report

This launcher is tied to:

- `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`

## Practical Use

Run the full campaign from the repository root:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_retraining_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_retraining_campaign.ps1 -PythonExecutable python
```
