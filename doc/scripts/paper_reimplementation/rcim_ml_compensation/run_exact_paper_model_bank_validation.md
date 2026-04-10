# Exact RCIM Paper Model Bank Validation Script

## Overview

This script runs the strict paper-faithful RCIM family-bank validation branch
implemented from the recovered paper assets.

The script is stored in:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

## Main Role

This workflow exists to recreate the original paper model bank inside the
repository with repository-owned artifact discipline.

It performs these stages:

1. load the recovered exact-paper dataframe;
2. keep the exact paper input schema `rpm`, `deg`, `tor`;
3. select the `20` recovered `ampl_k` and `phase_k` targets;
4. split with `test_size = 0.20` and `random_state = 0`;
5. fit the exact paper family bank through `MultiOutputRegressor`;
6. evaluate family-level aggregate metrics and per-target metrics;
7. export one ONNX model per family and per target;
8. compare the generated ONNX surface against the recovered exact release;
9. save a canonical validation summary and Markdown report.

## Main Components Used

### `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

Provides:

- dataframe loading and exact target resolution;
- recovered family constructors with paper-derived hyperparameters;
- family-bank training through `MultiOutputRegressor`;
- family ranking and target-wise ranking;
- ONNX export helpers;
- canonical validation-summary and Markdown-report generation.

### `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`

Provides:

- the recovered dataframe path;
- the recovered exact ONNX reference root;
- the enabled exact paper family set;
- deterministic split settings;
- ONNX export settings.

## Outputs

The script writes its outputs under:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`

Typical artifacts include:

- `training_config.yaml`
- `run_metadata.yaml`
- `validation_summary.yaml`
- `paper_family_model_bank.pkl`
- `onnx_export/`

It also writes a repository-owned Markdown validation report under:

- `doc/reports/analysis/validation_checks/`

## Practical Use

Typical usage from the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml `
  --output-suffix exact_paper_validation
```

Use this script when:

- the project needs the exact recovered paper family-bank baseline;
- the team wants a per-family and per-target reference before re-implementing
  the final paper winner assembly;
- the generated ONNX bank must be compared against the recovered exact ONNX
  release.

Operational note:

- this script is still an offline paper-faithful validation path;
- it does not yet execute the online compensation loop or the final `Table 9`
  benchmark branch.
