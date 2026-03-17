# Training Smoke-Test Script

## Overview

This script runs a minimal Lightning smoke test for the current TE training workflow.

The script is stored in:

- `scripts/training/run_training_smoke_test.py`

## Main Role

The script provides a lightweight batch-level fit verification for a registered model family without launching a full training run.

It verifies:

1. config loading;
2. datamodule and model instantiation;
3. one minimal Lightning `fit` path through `fast_dev_run`;
4. manual checkpoint save;
5. checkpoint reload through `load_from_checkpoint`.

## Main Output

The script writes:

- `smoke_test_summary.yaml`
- `smoke_test_checkpoint.ckpt`

under a dedicated smoke-test artifact directory such as:

- `output/smoke_tests/feedforward/2026-03-17-20-05-11__te_feedforward_trial_wave0_smoke_test/`

The smoke-test output folder is now separated from normal training runs so quick infrastructure checks remain easy to distinguish from real experiments.

## Practical Use

Typical usage:

```powershell
conda run -n standard_ml_codex_env python scripts/training/run_training_smoke_test.py `
  --config-path config/training/feedforward/presets/trial.yaml `
  --output-suffix wave0_smoke_test `
  --fast-dev-run-batches 1
```

Use this script when:

- a new model family has just been added;
- the training infrastructure was refactored;
- a minimal checkpoint save/reload verification is needed before a campaign.
