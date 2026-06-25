# Run Polished Dataset RCIM Model-Bank Reproduction Campaign

## Purpose

Operator-facing launcher for a prepared `polished_dataset` retraining campaign.

## Preflight

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1 -PreflightOnly
```

## Local Launch

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1
```

## Local Surface Launch

Use `-Surface fw` or `-Surface bw` to run only one measured direction. This is
the preferred recovery path after an interruption that completed one surface
and stopped before the other surface finished.

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1 -Surface fw
```

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1 -Surface bw
```

Local surface runs write per-surface logs under:

`output/training_campaigns/cross_wave/polished_dataset/rcim_model_bank_reproduction/polished_dataset_rcim_model_bank_reproduction_2026_06_22/logs/`

## Remote Launch

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1 -Remote
```

## Remote Surface Launch

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1 -Remote -Surface bw
```

## Campaign Manifest

`config/paper_reimplementation/rcim_ml_compensation/polished_dataset_rcim_model_bank_reproduction/campaigns/2026-06-22_polished_rcim_model_bank_reproduction/campaign.yaml`
