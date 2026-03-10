# Feedforward Training Script

## Overview

This script is the first neural-network training entry point for the Transmission Error project.

It trains a modular feedforward regression baseline implemented with PyTorch Lightning and built on top of the existing TE dataset pipeline.

The script is stored in:

- `training/train_feedforward_network.py`

## Main Role

The script coordinates the full baseline-training flow:

1. load the YAML training configuration;
2. initialize the Lightning datamodule;
3. compute training-set normalization statistics;
4. instantiate the feedforward backbone through the model factory;
5. build the generic Lightning regression module;
6. create callbacks, logger, and trainer;
7. run training and validation;
8. save the effective training configuration and checkpoint path.

## Main Components Used

### `config/feedforward_network_training.yaml`

Provides:

- dataset batching parameters;
- point subsampling stride;
- model architecture;
- optimizer settings;
- early-stopping configuration.

### `training/transmission_error_datamodule.py`

Wraps the existing curve dataset and converts it into point-wise batches for the feedforward baseline.

### `models/feedforward_network.py`

Implements the actual MLP backbone.

### `training/transmission_error_regression_module.py`

Implements the Lightning training logic, normalization, optimizer, and regression metrics.

## Outputs

The script writes its outputs under the configured root directory, currently:

- `output/feedforward_network/`

Typical generated artifacts include:

- a copy of the training config;
- TensorBoard logs;
- Lightning checkpoints;
- a text file containing the best checkpoint path.

During execution, the script also prints a structured terminal summary with colorized section headers, compact dataset and normalization statistics, and a final artifact summary.

## Practical Use

Typical usage from the project root:

```powershell
conda run -n standard_ml_codex_env python training/train_feedforward_network.py
```

The direct script command prints a compact terminal report before training, keeps the Lightning progress bars active, and avoids the previous raw configuration dump.
