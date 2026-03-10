# Project Usage Guide

## Overview

This guide explains how to use the currently available scripts in the repository.

At the moment, the implemented workflows are:

- dataset processing through the validated TE dataset utilities;
- dataset visualization through the TE plotting script.

Training, inference, and export workflows are planned but are not implemented yet as runnable project scripts. This guide marks those parts explicitly to avoid ambiguity.

## Prerequisites

Before using the scripts, make sure the project environment is installed and activated.

### 1. Activate The Conda Environment

```powershell
conda activate standard_ml_codex_env
```

### 2. Verify The Main Dependencies

```powershell
python -c "import torch, lightning, pandas, matplotlib; print(torch.__version__); print(lightning.__version__)"
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
  Dataset processing and visualization scripts.

- `config/`
  YAML files for path selection and runtime options.

- `data/datasets/`
  Validated Transmission Error CSV dataset.

- `doc/`
  Technical, script-level, and user-facing documentation.

## Dataset Processing

## What The Processing Script Does

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

Important note:

- the CSV files currently present in the repository are already validated TE files;
- they do not contain raw encoder columns or `DataValid Forward` / `DataValid Backward` flags;
- the raw TE reconstruction helpers are present for future raw datasets, but they are not exercised by the current repository files.

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

- `split.random_seed`
  Seed used for split reproducibility.

- `dataloader.batch_size`
  Batch size used by the generated dataloaders.

- `dataloader.num_workers`
  Number of PyTorch dataloader workers.

## Use The Processing Module From Python

The most direct way to use the processing utilities is from Python.

### Example: Build Train And Validation Dataloaders From Config

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset']))"
```

What this does:

- reads `config/dataset_processing.yaml`;
- collects CSV files from the configured dataset root;
- creates forward and backward directional samples;
- splits the files into train and validation sets;
- returns a dictionary containing:
  - `train_dataset`
  - `validation_dataset`
  - `train_dataloader`
  - `validation_dataloader`

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

If the future model is trained point by point rather than sequence by sequence, you can flatten the padded batch.

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

## Use A Different Visualization Config

If you create another visualization YAML file:

```powershell
python -m scripts.datasets.visualize_transmission_error --config-path config\visualization.yaml --save-path output\custom_plot.png
```

This is useful when multiple plot presets are needed later.

## Typical Workflow For The Current Project

If you want to inspect and prepare the current dataset, use this sequence:

1. Activate the environment.
2. Check `config/dataset_processing.yaml`.
3. Build dataloaders from Python and inspect one batch.
4. Use the visualization script to inspect one or more TE curves.
5. Adjust YAML configuration if you want different split settings or plotting defaults.

Example sequence:

```powershell
conda activate standard_ml_codex_env
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset']))"
python -m scripts.datasets.visualize_transmission_error --file-index 0 --save-path output\te_curve_0.png
```

## Training Status

Training is not yet implemented as a runnable project script.

This means there is currently no entry point such as:

- `scripts/training/train_model.py`
- `scripts/training/lightning_datamodule.py`
- `scripts/training/evaluate_model.py`

So, at the moment, you cannot run a documented project training command from this repository.

## Inference Status

Inference is also not yet implemented as a runnable project script.

This means there is currently no entry point such as:

- `scripts/inference/run_inference.py`
- `scripts/inference/export_onnx.py`
- `scripts/inference/runtime_validation.py`

So, at the moment, you cannot run a documented project inference command from this repository.

## What Is Already Ready For The Next Step

Even though training and inference scripts are not available yet, the repository already has:

- a validated TE dataset;
- a YAML-driven dataset-processing configuration;
- PyTorch datasets and dataloaders;
- a TE visualization utility;
- technical and script-level documentation aligned with the current structure.

This is enough to start implementing:

1. a LightningDataModule
2. a LightningModule
3. a training entry point
4. an evaluation entry point
5. an inference/export entry point

## Recommended Next Development Order

To extend the repository cleanly, the recommended order is:

1. add `scripts/datasets/` data-module integration for Lightning
2. add `config/training.yaml`
3. add `scripts/training/train_model.py`
4. add `scripts/training/evaluate_model.py`
5. add `scripts/inference/` utilities

This keeps the project consistent with the current `scripts/`, `config/`, and `doc/` structure.
