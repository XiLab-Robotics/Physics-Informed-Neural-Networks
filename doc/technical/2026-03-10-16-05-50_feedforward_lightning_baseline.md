# Feedforward Lightning Baseline

## Overview

This document defines the first neural-network implementation for the RV-reducer Transmission Error project.

The requested scope is:

- implement the first trainable neural-network baseline with PyTorch Lightning;
- keep the implementation style aligned with `blind_handover_controller`;
- start from a simple feedforward network;
- keep the code modular so that future RNN, LSTM, and PINN models can be added without rewriting the training stack.

Current dataset observations recorded on March 10, 2026:

- the active processed dataset is exposed by `scripts/datasets/transmission_error_dataset.py`;
- each valid sample is currently represented point-wise by 5 input features:
  - `angular_position_deg`
  - `speed_rpm`
  - `torque_nm`
  - `oil_temperature_deg`
  - `direction_flag`
- the regression target is one scalar:
  - `transmission_error_deg`
- the repository contains `969` CSV files, which become `1938` directional curves when forward and backward directions are both enabled;
- inspected curve lengths are variable and include at least:
  - `19440` points
  - `194400` / `194401` points

This means the first baseline should be treated as a point-wise regression model operating on the existing per-angle features, while preserving the current curve-oriented batching so future sequential models can reuse the same data interface.

## Technical Approach

### Modeling Strategy

The first model will be a feedforward regressor trained on flattened valid points extracted from the padded curve batches already produced by the dataset pipeline.

This is the right first baseline because:

1. the current active features are point-wise and already explicit;
2. the model should first establish a clean regression baseline before introducing sequential recurrence;
3. the training loop can stay compatible with future sequence-aware models if the datamodule keeps returning full curves plus masks.

The feedforward baseline will therefore:

- receive normalized point-wise feature tensors with shape `[N, 5]`;
- predict normalized or denormalized TE values with shape `[N, 1]`;
- use a modular backbone class that can later be replaced by `RNN`, `LSTM`, or `PINN` variants.

### Proposed Architecture

The initial architecture will be a moderate-width MLP designed for small tabular inputs and scalar regression:

- input size: `5`
- hidden layers: `128 -> 128 -> 64`
- activation: `GELU`
- normalization: `LayerNorm` after each hidden linear stage
- dropout: `0.10`
- output size: `1`

Reasoning behind this choice:

- the input dimensionality is very small, so very wide layers are unnecessary for the first baseline;
- the dataset contains a large number of trainable point samples once curves are flattened, so a small-to-medium MLP is sufficient to learn nonlinear condition-dependent TE trends;
- `GELU` and light regularization are reasonable modern defaults for tabular-style regression while keeping the implementation simple and readable;
- the architecture remains small enough to inspect, export, and later compare against recurrent or physics-informed models.

### Normalization And Target Handling

To keep the regression stable and reusable across future architectures, the implementation will introduce explicit training-set statistics:

- input-feature mean and standard deviation computed only on the training split;
- target mean and standard deviation computed only on the training split;
- stored normalization values reused during validation, testing, checkpoint loading, and future inference.

This is especially important because the input variables live on very different scales:

- angular position in degrees;
- speed in rpm;
- torque in Nm;
- temperature in degrees;
- direction as a signed flag.

### Training Stack

The implementation will use a modular PyTorch Lightning design based on official Lightning patterns for:

- `LightningModule`
- `LightningDataModule`
- `Trainer`
- `EarlyStopping`
- `ModelCheckpoint`

Planned optimization and monitoring choices:

- optimizer: `AdamW`
- learning rate: `1e-3`
- weight decay: `1e-4`
- training loss: `MSELoss`
- logged metrics:
  - `train_loss`
  - `val_loss`
  - `val_mae`
  - `val_rmse`
- early stopping:
  - monitor: `val_mae`
  - mode: `min`
  - patience: `20`
- checkpointing:
  - save top-1 checkpoint on `val_mae`
- trainer defaults:
  - `accelerator='auto'`
  - `devices='auto'`
  - `max_epochs=150`
  - `log_every_n_steps=1`

`val_mae` is preferred as the stopping and checkpoint metric because it remains directly interpretable in TE units and is easier to compare across later model families.

### Modular Code Structure

The implementation should not hard-wire the feedforward baseline into a one-off training script.

The proposed structure is:

- `models/feedforward_network.py`
  Feedforward backbone only.
- `models/model_factory.py`
  Simple model-selection layer that returns the requested backbone by name.
- `training/transmission_error_datamodule.py`
  Lightning datamodule wrapping the existing dataset and curve batching utilities.
- `training/transmission_error_regression_module.py`
  Generic Lightning regression module that owns loss, metrics, optimizer, and normalization logic.
- `training/train_feedforward_network.py`
  Entry-point script for the first baseline.
- `config/feedforward_network_training.yaml`
  Explicit training and architecture configuration.

This structure is designed so that future implementations can be added with minimal churn:

- `models/recurrent_network.py` or `models/lstm_network.py`
- `models/pinn_network.py`
- extended regression modules for physics-informed losses
- additional training configs without replacing the datamodule or the experiment entry flow

### Reuse Of Existing Dataset Pipeline

The existing `scripts/datasets/transmission_error_dataset.py` pipeline should remain the single source of truth for:

- CSV discovery;
- metadata parsing;
- directional curve generation;
- padding and masking.

The new Lightning datamodule should wrap that pipeline instead of duplicating it.

For the feedforward baseline:

- padded curve batches will be flattened through the existing valid-mask logic before the backbone forward pass.

For future recurrent models:

- the same datamodule can keep returning `[batch, time, feature]` tensors with masks intact.

This is the main compatibility point that avoids rewriting the data layer later.

## Involved Components

- `doc/technical/2026-03-10-16-05-50_feedforward_lightning_baseline.md`
- `README.md`
- `doc/README.md`
- `config/feedforward_network_training.yaml`
- `models/feedforward_network.py`
- `models/model_factory.py`
- `training/transmission_error_datamodule.py`
- `training/transmission_error_regression_module.py`
- `training/train_feedforward_network.py`
- `scripts/datasets/transmission_error_dataset.py`

## Implementation Steps

1. Create this technical document and register it in the project documentation indexes.
2. After user approval, add the training configuration file for the feedforward baseline.
3. Implement the reusable Lightning datamodule on top of the existing TE dataset pipeline.
4. Implement the modular feedforward backbone and a small model factory for future architecture extension.
5. Implement the generic Lightning regression module with normalization, loss, metrics, optimizer, early stopping, and checkpoint support.
6. Implement the first training entry script for the feedforward network in the project coding style.
7. Run a lightweight training verification and confirm:
   - batch shape consistency;
   - normalization statistics creation;
   - trainer startup;
   - validation metric logging;
   - checkpoint generation.
8. Create a Git commit with a repository-aligned title and body summarizing the full baseline implementation.
