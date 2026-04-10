# Exact Paper Model Bank Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the first batch
campaign of the strict RCIM exact-paper branch.

It orchestrates multiple exact-paper validation runs through:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

## Included Runs

The dedicated launcher forwards these YAML files:

1. `01_exact_full_bank_diagnostic_continue.yaml`
2. `02_exact_full_bank_strict_reference.yaml`
3. `03_exact_svr_export_diagnostic.yaml`
4. `04_exact_non_svr_export_reference.yaml`

All files live under:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-10_exact_paper_model_bank_campaign/`

## Purpose Of Each Block

### Full Exact Bank Diagnostic

This run keeps the full recovered family bank together and lets export issues
be serialized without crashing the whole batch.

### Full Exact Bank Strict Reference

This run is the intended clean exact-paper reference once the diagnostic path
shows the export surface is stable.

### SVR Export Diagnostic

This run isolates the `SVR` branch, which is the branch that first exposed the
modern ONNX export failure.

### Non-SVR Export Reference

This run gives a clean baseline for the rest of the recovered family bank
independently of the special-case `SVR` path.

## Practical Use

Run the canonical exact-paper campaign launcher from the repository root:

```powershell
.\scripts\campaigns\run_exact_paper_model_bank_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\campaigns\run_exact_paper_model_bank_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

Each run writes under:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`

Each run also produces a validation report under:

- `doc/reports/analysis/validation_checks/`

The launcher writes per-run console logs under:

- `output/training_campaigns/exact_paper_model_bank_campaign_2026_04_10_17_04_41/logs/`

## Related Documents

- `doc/reports/campaign_plans/2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-10/2026-04-10-17-00-06_exact_paper_validation_fix_and_campaignization.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.md`
