# Run Polished Dataset Early-Wave Parallel Training Campaign

## Purpose

Operator-facing launcher for the 36-run early-wave `polished_dataset`
retraining batch. The launcher reuses the first 36 configs from the prepared
full-wave campaign and runs them under a dedicated campaign name and queue
root.

This launcher is intended for the workstation that is not currently running
the polished `RCIM Model-Bank Reproduction` campaign.

## Preflight

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1 -PreflightOnly
```

## Local Launch

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1
```

## Enqueue-Only Local Check

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1 -EnqueueOnly
```

## Remote Launch

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1 -Remote
```

## Campaign Manifest

`config/training/polished_dataset_retraining/campaigns/2026-06-25_polished_early_wave_parallel_training/campaign.yaml`
