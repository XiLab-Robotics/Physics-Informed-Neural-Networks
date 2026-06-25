# Polished RCIM Runtime Log Wording

## Overview

The polished `RCIM Model-Bank Reproduction` campaign reuses the historical
exact-paper runner located under the legacy original-dataset package path. The
runner correctly consumes `polished_dataset` configs, but several runtime log
messages still say `original-dataset exact`, which makes operator monitoring
ambiguous.

## Technical Approach

Keep the historical package and function names for reproducibility, but make
runtime log messages dataset-aware. When `dataset.name` is `polished_dataset`,
the runner should identify the workflow as `Polished-dataset RCIM Model-Bank
Reproduction` and print the resolved dataset root, direction, split sizes,
feature schema, and target count before fitting.

Also add a clear exception boundary at the command entry point so failed runs
print a traceback and exit non-zero instead of leaving only partial progress
logs.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
- `doc/README.md`

## Implementation Steps

1. Add a small helper that resolves a dataset-aware runtime label from the
   training config.
2. Replace legacy progress-log text in the validation runner with the resolved
   label.
3. Print resolved dataset root, dataset config path, direction, row counts,
   feature names, and target count after bundle construction.
4. Add command-entry traceback logging for unexpected exceptions.
5. Register this technical note in `doc/README.md`.
6. Validate Python syntax and the backward polished bundle-only path before
   committing.
