# Wave 1 Directional Optuna Recovery Micro Campaign Launcher

## Overview

This launcher validates the neural `Optuna` recovery path on one isolated
`feedforward` micro study before the blocked production `Wave 1` directional
HPO campaign is resumed.

## Preparation Dependency

The micro package must exist under:

- `config/training/wave1_directional_optuna_recovery_micro/campaigns/2026-05-12_wave1_directional_optuna_recovery_micro_campaign/`

If it is missing, rebuild it first with:

```powershell
python -B .\scripts\campaigns\wave_1\prepare_wave1_directional_optuna_recovery_micro_campaign.py
```

## Planning Report

This launcher is tied to:

- `doc/reports/campaign_plans/wave_1/2026-05-12-10-49-02_wave1_directional_optuna_recovery_micro_campaign_plan_report.md`

## Practical Use

Run the isolated micro study with one visible GPU slot:

```powershell
.\scripts\campaigns\wave_1\run_wave1_directional_optuna_recovery_micro_campaign.ps1 -GpuId 0
```

Linux Bash equivalent:

```bash
bash scripts/campaigns/wave_1/run_wave1_directional_optuna_recovery_micro_campaign.sh --gpu-id 0
```

Command-resolution dry run without launching the Optuna study:

```bash
bash scripts/campaigns/wave_1/run_wave1_directional_optuna_recovery_micro_campaign.sh \
  --gpu-id 0 \
  --dry-run
```
