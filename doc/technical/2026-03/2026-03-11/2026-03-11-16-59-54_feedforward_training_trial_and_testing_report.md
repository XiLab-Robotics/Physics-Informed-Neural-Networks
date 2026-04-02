# Feedforward Training Trial And Testing Report

## Overview

The user requested a proof training run of the current feedforward baseline, followed by model testing and a report that summarizes the resulting quality indicators.

Local repository inspection on March 11, 2026 shows that:

- the current baseline training workflow already supports `fit` plus a final `validate` pass;
- the current `TransmissionErrorRegressionModule` does not expose `test_step`;
- the current `TransmissionErrorDataModule` exposes only train and validation datasets;
- there is no dedicated report artifact that consolidates split sizes, best checkpoint, validation metrics, and testing metrics for one executed run.

Because of that gap, the requested work should not be treated as a pure execution-only task. A small extension of the current Lightning workflow is required so the repository can produce a reproducible test phase and an explicit result report instead of relying only on terminal output.

## Technical Approach

The implementation should stay narrow and preserve the current feedforward baseline, dataset semantics, and TwinCAT-oriented simplicity.

The proposed approach is:

1. extend the dataset split configuration so the pipeline supports a dedicated held-out test subset in addition to the current training and validation subsets;
2. extend the Lightning datamodule so it builds `train`, `validation`, and `test` datasets from the directional file manifest while preserving the existing operating-condition metadata and directional samples;
3. extend the regression module with a `test_step` that reuses the same denormalized TE metrics already used for validation, so the reported results stay directly interpretable in Transmission Error units;
4. update the feedforward training entry point so it:
   - runs training as it does today;
   - reloads the best checkpoint;
   - runs a final validation pass and a held-out test pass on the best checkpoint;
   - writes a compact machine-readable and human-readable result summary;
5. create an execution report artifact for the requested proof run, including:
   - resolved configuration values;
   - dataset split counts;
   - normalization summary reference;
   - best checkpoint path;
   - final validation metrics;
   - final test metrics;
   - a short interpretation of whether the proof training appears numerically stable and useful as a baseline.

This approach is preferred over calling the current validation pass a "test" because that would weaken the quality claim. A distinct held-out test subset is the minimal defensible way to evaluate the resulting model after training.

The report artifact should be saved under the run output directory so it remains tied to the exact executed experiment, for example under:

- `output/training_runs/feedforward/<run_instance_id>/training_test_report.md`
- `output/training_runs/feedforward/<run_instance_id>/training_test_metrics.yaml`

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index aligned with the technical-document set.
- `config/dataset_processing.yaml`
  Dataset split configuration that currently exposes only `validation_split`.
- `config/feedforward_network_training.yaml`
  Training configuration used for the proof run.
- `training/transmission_error_datamodule.py`
  DataModule that must expose a true test split and test dataloader.
- `training/transmission_error_regression_module.py`
  Lightning regression module that must expose testing metrics.
- `training/train_feedforward_network.py`
  Training entry point that must execute final validation, testing, and report generation.
- `doc/guide/project_usage_guide.md`
  User-facing guide that must be updated before the final commit because the runnable training workflow will gain explicit testing/report behavior.
- `output/training_runs/feedforward/`
  Run artifact root where the proof-run checkpoints, logs, and result report will be stored.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, extend the dataset split configuration with an explicit held-out test share while keeping reproducibility through the existing random seed.
3. Update the Lightning datamodule to create `train_dataset`, `validation_dataset`, and `test_dataset`, plus the related dataloaders and summary counts.
4. Add `test_step` support to the Lightning regression module by reusing the existing normalized-loss and denormalized-metric path.
5. Update the feedforward training entry point so it loads the best checkpoint after fitting, runs final validation and test evaluation, and writes a compact report artifact under the run output directory.
6. Execute one proof training run with the repository baseline configuration, unless local runtime constraints require a lighter approved configuration for the first verification pass.
7. Execute the held-out test phase on the best checkpoint produced by that run.
8. Review the resulting metrics and write the requested report with a concise technical interpretation of training quality.
9. Update `doc/guide/project_usage_guide.md` so the explicit testing/report workflow is documented.
10. Create the required Git commit immediately after the approved modifications and run artifacts are completed.
