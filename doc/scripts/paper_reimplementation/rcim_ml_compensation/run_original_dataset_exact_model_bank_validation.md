# Original-Dataset Exact RCIM Model Bank Validation Script

## Overview

This script runs the direction-specific exact-model-bank workflow built from
the repository dataset under `data/datasets`.

The script is stored in:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`

## Main Role

This workflow exists to rebuild the `Track 1` exact-model-bank branch on top of
the original dataset instead of the recovered forward-only CSV snapshot.

It performs these stages:

1. load the dataset-processing config and resolve `data/datasets`;
2. select exactly one direction, `forward` or `backward`;
3. split the source CSV files at file level with `train / validation / test`;
4. decompose each TE curve into the selected harmonic `A_k` and `phi_k`
   targets;
5. map the repository operating variables to the paper-style feature schema
   `rpm`, `deg`, `tor`;
6. fit one `MultiOutputRegressor` bank per enabled family;
7. evaluate held-out test metrics per family and per target;
8. export one ONNX model per family and per target;
9. save a canonical validation summary and Markdown report.

## Main Components Used

### `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank_support.py`

Provides:

- direction-specific manifest building from the repository dataset;
- harmonic decomposition of TE curves into exact-model-bank targets;
- original-dataset summary and Markdown-report generation.

### `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

Provides:

- family constructors;
- family-bank training through `MultiOutputRegressor`;
- family ranking and target-wise ranking;
- ONNX export helpers.

### `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`

Provides:

- `baseline_forward.yaml`;
- `baseline_backward.yaml`.

These configs define:

- the direction label;
- the harmonic list;
- the `70 / 20 / 10` split settings;
- the family set;
- the temporary `SVR` grid-search bypass.

## Outputs

The script writes its outputs under:

- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/`

Typical artifacts include:

- `training_config.yaml`
- `run_metadata.yaml`
- `validation_summary.yaml`
- `paper_family_model_bank.pkl`
- `onnx_export/`

It also writes a repository-owned Markdown validation report under:

- `doc/reports/analysis/validation_checks/`

## Practical Use

Forward branch:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/baseline_forward.yaml `
  --output-suffix forward_validation
```

Backward branch:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/baseline_backward.yaml `
  --output-suffix backward_validation
```

Use this script when:

- the project needs `Track 1` exact-model banks trained on the original repo
  dataset;
- the team wants separate `Fw` and `Bw` banks with the same harmonic target
  surface;
- the recovered forward-only branch must remain untouched while the
  bidirectional rebuild is stabilized.
