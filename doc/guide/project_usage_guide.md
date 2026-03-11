# Project Usage Guide

## Overview

This guide explains how to use the runnable workflows currently available in the repository.

At the moment, the implemented workflows are:

- dataset processing through the validated TE dataset utilities;
- dataset visualization through the TE plotting script;
- feedforward neural-network training, validation, held-out testing, and per-run reporting through a PyTorch Lightning baseline.

Recurrent models, LSTM-based models, inference/export flows, and PINN-specific training are still planned future extensions. They are not yet exposed as runnable project workflows.

## Prerequisites

Before using the scripts, make sure the project environment is installed and activated.

If the environment is not ready yet, install the tracked project dependencies first:

```powershell
python -m pip install torch --index-url https://download.pytorch.org/whl/cu130
python -m pip install -r requirements.txt
```

This keeps the dependency installation aligned with `requirements.txt` while still pulling the CUDA-enabled `torch` build from the official PyTorch wheel index for the current Windows setup.

### 1. Activate The Conda Environment

```powershell
conda activate standard_ml_codex_env
```

### 2. Verify The Main Dependencies

```powershell
python -c "import torch, lightning, pandas, matplotlib, colorama; print(torch.__version__); print(lightning.__version__)"
```

### 3. Check The Dataset Path

The current dataset path is configured in:

- `config/dataset_processing.yaml`

The default repository setting is:

```yaml
paths:
  dataset_root: data/datasets
```

This path is interpreted relative to the repository root.

If the dataset is moved in the future, update this YAML file before running the scripts.

## Relevant Project Paths

The current usage flow mainly relies on these folders:

- `scripts/datasets/`
  Dataset processing and visualization utilities.

- `training/`
  PyTorch Lightning training entry point, datamodule, and regression module.

- `models/`
  Neural-network backbones and the model factory.

- `config/`
  YAML files for dataset processing, visualization, and training configuration.

- `data/datasets/`
  Validated Transmission Error CSV dataset.

- `output/`
  Generated artifacts such as plots, logs, and model checkpoints.

- `doc/`
  Technical, script-level, and user-facing documentation.

## Dataset Processing

## What The Processing Module Does

The dataset-processing logic lives in:

- `scripts/datasets/transmission_error_dataset.py`

This module:

- loads the validated TE CSV files already available in `data/datasets`;
- parses metadata from the file names and folder names;
- builds forward and backward directional samples;
- creates PyTorch `Dataset` and `DataLoader` objects;
- keeps helper functions ready for future raw-data TE reconstruction using:
  - `TE = theta_out - 81 * theta_in`
  - `DataValid` masks

Important dataset note:

- the CSV files currently present in the repository are already validated TE files;
- they do not contain raw encoder columns or `DataValid Forward` / `DataValid Backward` flags;
- the forward-position CSV header contains the original typo `Poisition_Output_Reducer_Fw`;
- the loader keeps compatibility with that original header and normalizes it internally to `position_output_reducer_fw_deg`.

## Dataset Processing Configuration

The processing settings are stored in:

- `config/dataset_processing.yaml`

Current configurable sections:

- `paths.dataset_root`
  Root folder of the CSV dataset, relative to the project root.

- `dataset.reduction_ratio`
  Reducer ratio used by the raw TE helper path.

- `dataset.angular_window_deg`
  Output-position window expected for valid rotation.

- `directions.use_forward_direction`
  Enables forward curves.

- `directions.use_backward_direction`
  Enables backward curves.

- `split.validation_split`
  Train/validation file split ratio.

- `split.test_split`
  Held-out test file split ratio.

- `split.random_seed`
  Seed used for split reproducibility.

- `dataloader.batch_size`
  Batch size used by the generated curve dataloaders.

- `dataloader.num_workers`
  Number of PyTorch dataloader workers.

## Use The Processing Module From Python

The most direct way to use the processing utilities is from Python.

### Example: Build Train, Validation, And Test Dataloaders From Config

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset'])); print(len(bundle['test_dataset']))"
```

What this does:

- reads `config/dataset_processing.yaml`;
- collects CSV files from the configured dataset root;
- creates forward and backward directional samples;
- splits the files into train, validation, and test sets;
- returns a dictionary containing:
  - `train_dataset`
  - `validation_dataset`
  - `test_dataset`
  - `train_dataloader`
  - `validation_dataloader`
  - `test_dataloader`

### Example: Inspect One Training Batch

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); batch=next(iter(bundle['train_dataloader'])); print(batch['input_tensor'].shape); print(batch['target_tensor'].shape); print(batch['valid_mask'].shape)"
```

Expected batch content:

- `input_tensor`
  Padded tensor with features per point.

- `target_tensor`
  Padded tensor with TE targets.

- `angular_position_deg`
  Padded output-position tensor.

- `valid_mask`
  Boolean mask for valid points inside the padded batch.

- `sequence_length`
  Original sequence length for each curve.

- metadata tensors/lists for speed, torque, temperature, direction, and source file.

## Input Features Used In The Current Dataset Class

Each point currently includes these input features:

1. output angular position in degrees
2. speed in rpm
3. torque in Nm
4. oil temperature in degrees
5. direction flag (`+1` forward, `-1` backward)

The regression target is:

- Transmission Error in degrees

## Flatten A Padded Batch Into Point-Wise Tensors

If the model is trained point by point rather than sequence by sequence, you can flatten the padded batch.

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config, flatten_curve_batch; bundle=create_transmission_error_dataloaders_from_config(); batch=next(iter(bundle['train_dataloader'])); flat=flatten_curve_batch(batch); print(flat['input_tensor'].shape); print(flat['target_tensor'].shape)"
```

This removes the padding using the batch validity mask.

## Dataset Visualization

## What The Visualization Script Does

The visualization entry point is:

- `scripts/datasets/visualize_transmission_error.py`

This script:

- reads the visualization config;
- resolves the dataset config;
- selects one CSV file;
- loads forward and backward TE curves;
- plots TE against output angular position;
- either opens the plot or saves it to an image file.

## Visualization Configuration

The visualization settings are stored in:

- `config/visualization.yaml`

Main configurable fields:

- `paths.dataset_config_path`
  Path to the dataset-processing YAML config, relative to the project root.

- `selection.file_index`
  Default file index when no explicit CSV path is provided.

- `plot.figure_width`
  Figure width in inches.

- `plot.figure_height`
  Figure height in inches.

- `plot.figure_dpi`
  Figure DPI used for saved plots.

- `output.save_path`
  Optional default output path for saved figures.

## Save A Plot To File

This is the most robust option in terminal or headless environments.

```powershell
python -m scripts.datasets.visualize_transmission_error --save-path output\te_curve.png
```

What happens:

- the script reads the default YAML files in `config/`;
- it selects the dataset file indicated by `selection.file_index`;
- it generates forward and backward TE curves;
- it saves the image to `output\te_curve.png`.

## Visualize A Specific Dataset File

If you want to inspect one exact CSV:

```powershell
python -m scripts.datasets.visualize_transmission_error --csv-path "data\datasets\Test_35degree\1000rpm\1000.0rpm0.0Nm35.0deg.csv" --save-path output\sample_te_curve.png
```

This bypasses the default file index and directly uses the selected CSV file.

## Override The Default File Index

If you prefer to keep the configured dataset root but change the selected file:

```powershell
python -m scripts.datasets.visualize_transmission_error --file-index 10 --save-path output\te_curve_10.png
```

## Feedforward Training Baseline

## What The Training Workflow Does

The first training entry point is:

- `training/train_feedforward_network.py`

This workflow trains a feedforward regression baseline implemented with PyTorch Lightning.

The script now prints a structured terminal summary with colorized section headers on Windows terminals, so the training configuration and run artifacts are easier to inspect than with the earlier raw dictionary dump.

The training stack is composed of:

- `models/feedforward_network.py`
  Feedforward backbone with hidden layers, activation, optional layer normalization, and dropout.

- `models/model_factory.py`
  Model selection layer used to instantiate the requested architecture.

- `training/transmission_error_datamodule.py`
  Lightning datamodule that reuses the TE curve dataset and converts curves into point-wise batches.

- `training/transmission_error_regression_module.py`
  Generic Lightning regression module with normalization, loss computation, optimizer setup, and validation metrics.

- `config/feedforward_network_training.yaml`
  Main training configuration file for the baseline.

## Current Baseline Assumptions

The current baseline:

- trains point-wise on TE curve samples rather than with recurrent sequence modeling;
- computes normalization statistics from the training split only;
- uses the normalized tensors during optimization and reports interpretable metrics on denormalized TE values;
- uses validation-based early stopping and checkpoint selection;
- reloads the best checkpoint for the final validation and held-out test evaluation;
- saves machine-readable and human-readable reports for each completed run.

This is the first baseline only. It does not replace the future need for LSTM, RNN, or PINN models.

## Training Configuration

The training settings are stored in:

- `config/feedforward_network_training.yaml`

An additional lighter proof-run configuration is also available in:

- `config/feedforward_network_training_trial.yaml`

Main configurable sections:

- `paths.dataset_config_path`
  Dataset-processing config used by the Lightning datamodule.

- `paths.output_root`
  Root output directory for logs and checkpoints.

- `experiment.run_name`
  Name of the training run output folder.

- `experiment.model_type`
  Requested architecture name resolved by the model factory.

- `dataset.curve_batch_size`
  Number of directional curves loaded per batch before point extraction.

- `dataset.point_stride`
  Downsampling stride used when extracting point-wise samples from each curve.

- `dataset.maximum_points_per_curve`
  Optional cap on the number of points taken from each curve.

- `dataset.num_workers`
  PyTorch dataloader worker count.
  The current default is `4`, which is a conservative multiprocessing setting for this Windows-based training environment.

- `dataset.pin_memory`
  Pin-memory flag for the dataloaders.
  The current default is `true` to improve host-to-device transfer when training on GPU.

- `model.input_size`
  Expected point-wise feature dimension.

- `model.hidden_size`
  Hidden-layer sizes for the feedforward backbone.

- `model.output_size`
  Output dimension of the regression model.

- `model.activation_name`
  Activation function used in the hidden layers.

- `model.dropout_probability`
  Dropout probability used after hidden activations.

- `model.use_layer_norm`
  Enables or disables `LayerNorm` in the hidden stages.

- `training.learning_rate`
  Optimizer learning rate.

- `training.weight_decay`
  `AdamW` weight decay.

- `training.min_epochs`
  Minimum number of epochs.

- `training.max_epochs`
  Maximum number of epochs.

- `training.patience`
  Early-stopping patience.

- `training.min_delta`
  Minimum monitored improvement threshold.

- `training.log_every_n_steps`
  Lightning logging frequency.

- `training.fast_dev_run`
  Lightning developer-mode shortcut.

- `training.deterministic`
  Deterministic training flag.

## Run The Default Training Command

From the project root:

```powershell
conda run -n standard_ml_codex_env python training/train_feedforward_network.py
```

The direct script execution shown above is supported from the repository root. The training entry point bootstraps the project root into `sys.path`, so the internal `models/`, `training/`, and `scripts/` imports resolve correctly even when the file is launched directly.

This command:

- loads `config/feedforward_network_training.yaml`;
- builds the datamodule from `config/dataset_processing.yaml`;
- uses `validation_split` plus `test_split` from the dataset config to create three file-level subsets;
- uses `num_workers: 4` and `pin_memory: true` in the point-wise dataloaders by default;
- enables `persistent_workers` internally when dataloader multiprocessing is active;
- computes training normalization statistics;
- creates the feedforward model;
- prints a compact colorized summary for configuration, dataset, normalization, runtime, and output artifacts;
- suppresses the current low-signal Lightning `litlogger` startup tip and the known `_pytree` sanity-check warning;
- starts Lightning training, validation, and held-out testing;
- reloads the best checkpoint before the final evaluation phase;
- writes artifacts under `output/feedforward_network/<run_name>/`.

Typical artifacts now include:

- `feedforward_network_training.yaml`
  Snapshot of the effective run configuration.

- `checkpoints/`
  Best and last Lightning checkpoints.

- `best_checkpoint_path.txt`
  Plain-text pointer to the selected best checkpoint.

- `training_test_metrics.yaml`
  Machine-readable validation and test metrics.

- `training_test_report.md`
  Human-readable training and testing summary.

## Run The Lightweight Proof Configuration

If you want a faster verification run before trying the default baseline, use the trial config:

```powershell
conda run -n standard_ml_codex_env python -c "from training.train_feedforward_network import train_feedforward_network; train_feedforward_network('config/feedforward_network_training_trial.yaml')"
```

This proof configuration:

- uses `run_name: te_feedforward_trial`;
- increases `dataset.point_stride` to reduce the sampled points per curve;
- caps the point count with `dataset.maximum_points_per_curve: 200`;
- reduces the epoch budget to a short verification range;
- still executes validation, held-out testing, and report generation.

## Current Dataloader Runtime Defaults

The current feedforward-training config now uses these dataloader defaults:

- `dataset.num_workers: 4`
- `dataset.pin_memory: true`

These values were selected as the first practical tuning step after the initial stable baseline:

- `num_workers: 4` reduces dataloader bottlenecks without jumping immediately to aggressive multiprocessing values on Windows;
- `pin_memory: true` is appropriate when the training run uses CUDA, which is the current expected setup for this repository.

If the project is later executed on CPU-only hardware or on a different workstation, these values can still be adjusted directly in `config/feedforward_network_training.yaml`.

## Run Training With A Custom Config Path

If you want to launch the same workflow with a different YAML file:

```powershell
conda run -n standard_ml_codex_env python -c "from training.train_feedforward_network import train_feedforward_network; train_feedforward_network(r'config\feedforward_network_training.yaml')"
```

This is the current way to override the training config path because the script does not yet expose CLI arguments for that option.

## Typical Training Outputs

The baseline writes outputs under the configured root directory, currently:

- `output/feedforward_network/`

For the default run name, the typical output location is:

- `output/feedforward_network/te_feedforward_baseline/`

Typical generated artifacts include:

- a copy of the effective training config;
- TensorBoard logs;
- Lightning checkpoints;
- a text file containing the best checkpoint path.

## Inspect Training Logs With TensorBoard

After a real training run, you can inspect logs with:

```powershell
tensorboard --logdir output\feedforward_network
```

Then open the local TensorBoard URL shown in the terminal.

## Current Training Metrics

The Lightning regression module currently logs:

- `train_loss`
- `train_mae`
- `train_rmse`
- `val_loss`
- `val_mae`
- `val_rmse`

The best checkpoint and early stopping are both driven by `val_mae`.

## Typical Workflow For The Current Project

If you want to inspect the dataset and train the current baseline, use this sequence:

1. Activate the environment.
2. Check `config/dataset_processing.yaml`.
3. Check `config/feedforward_network_training.yaml`.
4. Inspect one dataset batch if needed.
5. Visualize one or more TE curves.
6. Start the feedforward Lightning training run.
7. Inspect logs and checkpoints under `output/feedforward_network/`.

Example sequence:

```powershell
conda activate standard_ml_codex_env
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset']))"
python -m scripts.datasets.visualize_transmission_error --file-index 0 --save-path output\te_curve_0.png
conda run -n standard_ml_codex_env python training/train_feedforward_network.py
```

## Inference Status

Inference and export are not yet implemented as runnable project scripts.

This means there is currently no entry point such as:

- `inference/run_inference.py`
- `inference/export_onnx.py`
- `inference/runtime_validation.py`

So, at the moment, you cannot run a documented project inference or export command from this repository.

## What Is Already Ready For The Next Step

The repository now already has:

- a validated TE dataset;
- a YAML-driven dataset-processing configuration;
- PyTorch datasets and curve dataloaders;
- a TE visualization utility;
- a modular PyTorch Lightning feedforward training baseline;
- a reusable datamodule and regression module structure for future architectures;
- technical, script-level, and user-facing documentation aligned with the current structure.

This is enough to extend the project toward:

1. recurrent sequence models such as RNN or LSTM
2. evaluation entry points
3. inference/export utilities
4. PINN-specific losses and training flows

## Recommended Next Development Order

To extend the repository cleanly, the recommended order is:

1. add a sequence-aware recurrent baseline on top of the current `training/` and `models/` structure
2. add a dedicated evaluation entry point
3. add inference and export utilities
4. extend the regression module toward physics-informed loss composition
5. add PINN-specific training and validation workflows
