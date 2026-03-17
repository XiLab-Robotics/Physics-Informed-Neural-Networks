# Training Setup Validation Script

## Overview

This script runs a one-batch validation check for the current TE training setup.

The script is stored in:

- `scripts/training/validate_training_setup.py`

## Main Role

The script verifies the training wiring before a longer run or before a new model family is introduced.

It checks:

1. config loading;
2. datamodule initialization;
3. model instantiation through the shared training infrastructure;
4. batch retrieval from the training split;
5. tensor-shape consistency;
6. finite loss and metric computation on one batch.

## Main Output

The script writes:

- `validation_summary.yaml`

under a run-suffixed output directory such as:

- `output/feedforward_network/te_feedforward_trial_validation_check/`

## Practical Use

Typical usage:

```powershell
conda run -n standard_ml_codex_env python scripts/training/validate_training_setup.py `
  --config-path config/training/feedforward/presets/trial.yaml `
  --output-suffix wave0_validation
```

Use this script when:

- a new training config is added;
- a new model family is registered in the model factory;
- the datamodule or regression module wiring is changed;
- a quick pre-campaign sanity check is needed.
