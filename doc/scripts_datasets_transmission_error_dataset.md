# Transmission Error Dataset Script

## Overview

This script provides the dataset-processing utilities for the validated Transmission Error CSV files stored in `data/datasets`.

Its purpose is to:

- read the validated TE CSV files;
- parse operating-condition metadata from file and folder names;
- keep an explicit helper path for future raw TE reconstruction from encoder data and `DataValid` flags;
- build PyTorch-ready `Dataset` and `DataLoader` objects for network training.

The script is stored in:

- `scripts/datasets/transmission_error_dataset.py`

## Main Role

The current repository data already contains forward and backward TE curves.

The script therefore supports two different logic paths:

1. active path for the validated TE dataset that is already available in the repository;
2. helper path for future raw datasets where TE must be reconstructed through:
   - `TE = theta_out - tau * theta_in`
   - `tau = 81`
   - `DataValid Forward` / `DataValid Backward` filtering.

## Main Functions And Classes

### `load_dataset_processing_config`

Loads the YAML configuration used for dataset paths and dataloader settings.

### `resolve_dataset_root_from_config`

Reads the dataset root directly from `config/dataset_processing.yaml`.

### `collect_dataset_csv_paths`

Recursively collects every CSV file inside the configured dataset root.

### `parse_operating_condition_metadata`

Extracts:

- speed;
- torque;
- oil temperature;

from file names and test folder names.

### `load_validated_te_dataframe`

Loads one validated TE CSV and normalizes the column names, including the original typo in the forward position column.

### `compute_transmission_error`

Computes TE from raw encoder signals using:

- `theta_out - reduction_ratio * theta_in`

This is the explicit raw-data TE formula helper.

### `extract_valid_rotation_window`

Builds the valid sample mask using:

- `DataValid` flags;
- the `0-360 deg` output-position interval.

This function is intended for future raw datasets.

### `build_raw_directional_sample`

Creates one directional TE sample from raw signals after applying the valid-window mask and TE reconstruction.

### `build_validated_directional_sample`

Creates one directional sample from the validated TE CSV format currently present in the repository.

### `build_validated_directional_samples`

Returns both:

- forward sample;
- backward sample;

for a given CSV file.

### `TransmissionErrorCurveDataset`

PyTorch dataset class that converts each directional curve into:

- an input tensor with angular position, speed, torque, temperature, and direction;
- a target tensor with TE values.

### `collate_transmission_error_curves`

Pads variable-length curves into batched tensors and builds a validity mask.

### `flatten_curve_batch`

Converts a padded batch into point-wise tensors by removing masked padding positions.

### `create_transmission_error_dataloaders`

Builds train and validation dataloaders from runtime parameters.

### `create_transmission_error_dataloaders_from_config`

Builds train and validation dataloaders directly from the YAML configuration file.

## Inputs And Outputs

### Inputs

- validated TE CSV files in `data/datasets`
- YAML config in `config/dataset_processing.yaml`

### Outputs

- PyTorch `Dataset`
- PyTorch `DataLoader`
- directional TE samples with explicit metadata

## Practical Use

Typical usage from Python:

```python
from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config

dataset_bundle = create_transmission_error_dataloaders_from_config()
train_dataloader = dataset_bundle["train_dataloader"]
```
