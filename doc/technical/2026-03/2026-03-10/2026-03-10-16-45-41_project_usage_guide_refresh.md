# Project Usage Guide Refresh

## Overview

This document defines the refresh of `doc/guide/project_usage_guide.md` so it matches the current repository state after the recent PyTorch Lightning baseline and dataset-workflow changes.

The current guide is outdated because it still states that training is not implemented as a runnable project workflow, while the repository now includes:

- a runnable feedforward training entry point;
- a modular `models/` package;
- a modular `training/` package with a Lightning datamodule and regression module;
- a dedicated training configuration file;
- clarified dataset-header handling for the validated TE CSV files.

The goal of this update is to make the usage guide accurate, detailed, and directly useful for current project operation.

## Technical Approach

The guide refresh will stay focused on real, runnable repository functionality rather than planned future architecture.

The updated guide should:

- keep the existing dataset-processing and visualization sections;
- add a dedicated section for the current feedforward PyTorch Lightning training workflow;
- document the role of:
  - `training/train_feedforward_network.py`
  - `training/transmission_error_datamodule.py`
  - `training/transmission_error_regression_module.py`
  - `models/feedforward_network.py`
  - `models/model_factory.py`
  - `config/feedforward_network_training.yaml`
- explain the training outputs written under `output/training_runs/feedforward/`;
- explain the current baseline assumptions:
  - point-wise training on TE curve samples;
  - normalization based on training-split statistics;
  - checkpointing and early stopping on validation metrics;
- clarify that recurrent models, LSTM-based models, and PINNs are still planned, but the feedforward baseline is already implemented and runnable.

The guide should also reflect the dataset-header clarification:

- the original CSV files contain the literal typo `Poisition_Output_Reducer_Fw`;
- the loader handles that original header and normalizes it internally.

The refreshed guide should remain procedural and explicit, with concrete commands that match the repository structure and current Conda environment.

## Involved Components

- `doc/technical/2026-03/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md`
- `doc/guide/project_usage_guide.md`
- `README.md`
- `doc/README.md`
- `training/train_feedforward_network.py`
- `config/feedforward_network_training.yaml`
- `doc/scripts/training/train_feedforward_network.md`

## Implementation Steps

1. Add this technical document and reference it from the documentation indexes.
2. After user approval, update `doc/guide/project_usage_guide.md` so it reflects the current runnable training workflow.
3. Add practical usage commands for the feedforward Lightning baseline.
4. Align the guide wording with the current dataset-header clarification and current repository folder structure.
5. Verify that the guide no longer claims training is unavailable.
6. Create a Git commit summarizing the usage-guide refresh.
