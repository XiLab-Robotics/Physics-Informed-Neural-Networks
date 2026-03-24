# Wave 1 Structured Baseline Recovery Campaign Launcher

## Overview

This launcher is a short PowerShell wrapper for the Wave 1 structured-baseline recovery campaign.

It exists to avoid retyping the full campaign runner command while keeping the same terminal behavior, queue handling, per-run logs, and campaign artifacts.

## Main Role

The launcher:

1. changes to the repository root;
2. removes stale pending or running recovery YAML files from earlier failed launcher attempts;
3. assembles the approved recovery campaign YAML list;
4. forwards those YAML files to `scripts/training/run_training_campaign.py`;
5. preserves live terminal output and the campaign log files created by the underlying runner.

## Practical Use

Run the full recovery campaign from the repository root:

```powershell
.\scripts\campaigns\run_wave1_structured_baseline_recovery_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\campaigns\run_wave1_structured_baseline_recovery_campaign.ps1 -PythonExecutable python
```

