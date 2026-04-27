# Track 1 Bidirectional Original-Dataset Smoke Validation Launcher

## Overview

This launcher executes the lightweight structural smoke-validation wave for the
refactored `Track 1` original-dataset exact-model-bank branch.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_smoke_validation.ps1`

## Main Role

The launcher runs the `20` family-direction smoke validations:

- `10` exact-paper families;
- `forward` and `backward` separately;
- no grid search;
- reduced file counts per split;
- full runner path preserved.

The smoke wave exists only to validate the workflow after the taxonomy
refactor. It is not a scientific benchmark campaign.

## Inputs

Generated smoke configs:

- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/*.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/*.yaml`

Underlying runner:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`

## Practical Use

Generate the configs first:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/generate_original_dataset_exact_smoke_configs.py
```

Run the smoke wave:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_original_dataset_smoke_validation.ps1
```
