# Remove Feedforward Legacy Backward Compatibility

## Overview

The repository still writes and partially searches for two feedforward-specific legacy artifact names:

- `feedforward_network_training.yaml`
- `training_test_metrics.yaml`

These files were originally useful during the transition from the old feedforward-only layout to the shared training artifact schema. After the completed output migration, the canonical runtime format is now:

- `training_config.yaml`
- `metrics_summary.yaml`

The remaining legacy compatibility code now adds duplication to new runs and keeps campaign/report utilities aware of a format that is no longer required by the active workflow.

## Technical Approach

The cleanup should remove runtime production and runtime lookup of legacy feedforward snapshots while preserving already committed historical artifacts on disk.

The implementation should:

1. stop writing legacy feedforward duplicate snapshots for newly produced runs;
2. stop preferring or scanning legacy snapshot names in campaign utilities;
3. remove dead helper code that only exists to support the legacy filenames;
4. update usage and script documentation so the canonical artifact set is unambiguous;
5. leave historical files in old run folders untouched unless a document path must be clarified.

This keeps historical reproducibility while simplifying the active training pipeline.

## Involved Components

- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/run_training_campaign.py`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/training/train_feedforward_network.md`
- `doc/scripts/training/run_training_campaign.md`
- `README.md`
- `doc/README.md`

## Implementation Steps

1. Remove the legacy feedforward config and metrics snapshot constants from the shared training infrastructure if they are no longer needed by active code.
2. Update `save_training_config_snapshot(...)` and `save_common_metrics_snapshot(...)` so they only emit canonical artifact names.
3. Remove any dead legacy snapshot helper from `train_feedforward_network.py` that is no longer used in the active flow.
4. Update `run_training_campaign.py` so config and metrics discovery only target canonical artifact names.
5. Rewrite script documentation and usage guidance to present only `training_config.yaml` and `metrics_summary.yaml` as active outputs.
6. Keep historical technical notes and campaign-result reports intact except where a statement would incorrectly describe the current runnable behavior.
7. Run a lightweight verification pass such as `py_compile` on modified Python files.
