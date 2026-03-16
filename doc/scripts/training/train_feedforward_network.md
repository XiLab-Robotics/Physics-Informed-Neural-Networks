# Feedforward Training Script

## Overview

This script is the first neural-network training entry point for the Transmission Error project.

It trains a modular feedforward regression baseline implemented with PyTorch Lightning and built on top of the existing TE dataset pipeline.

The script is stored in:

- `scripts/training/train_feedforward_network.py`

## Main Role

The script coordinates the full baseline-training flow:

1. load the YAML training configuration;
2. initialize the Lightning datamodule;
3. compute training-set normalization statistics;
4. instantiate the feedforward backbone through the model factory;
5. build the generic Lightning regression module;
6. create callbacks, logger, and trainer;
7. run training and validation;
8. reload the best checkpoint and run held-out testing;
9. save the effective training configuration, checkpoint path, metrics snapshot, and markdown report.

## Main Components Used

### `config/training/feedforward/presets/baseline.yaml`

Provides:

- dataset batching parameters;
- point subsampling stride;
- optional maximum point cap per curve;
- model architecture;
- optimizer settings;
- runtime accelerator, precision, and transfer settings;
- early-stopping configuration;
- output run naming for trial or baseline execution.

### `scripts/training/transmission_error_datamodule.py`

Wraps the existing curve dataset and converts it into point-wise batches for the feedforward baseline.

### `scripts/models/feedforward_network.py`

Implements the actual MLP backbone.

### `scripts/training/transmission_error_regression_module.py`

Implements the Lightning training logic, normalization, optimizer, and regression metrics.

## Outputs

The script writes its outputs under the configured root directory, currently:

- `output/feedforward_network/`

Typical generated artifacts include:

- a copy of the training config;
- TensorBoard logs;
- Lightning checkpoints;
- a text file containing the best checkpoint path;
- a YAML file containing final validation and test metrics;
- a markdown report summarizing the executed run.

During execution, the script also prints a structured terminal summary with colorized section headers, compact dataset and normalization statistics, and a final artifact summary. The dataset summary now includes train, validation, and held-out test curve counts.

The runtime summary now also reports the configured accelerator, device selection, precision mode, cuDNN benchmark flag, and whether explicit non-blocking tensor transfer is enabled.

## Practical Use

Typical usage from the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py
```

To run an explicit configuration path from the command line:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/high_epoch.yaml
```

To run the lighter proof configuration used for a quick end-to-end verification:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/trial.yaml
```

The training entry point prints a compact terminal report before training, keeps the Lightning progress bars active, avoids the previous raw configuration dump, suppresses the current low-signal Lightning startup tip plus the known `_pytree` sanity-check warning, and writes both validation and test results for the selected best checkpoint.

The current implementation also exposes a runtime configuration block in the YAML presets so GPU-oriented options such as mixed precision, cuDNN benchmarking, and non-blocking batch transfer can be enabled or disabled explicitly without editing the Python source.
