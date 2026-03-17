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

The current implementation now also uses the shared Wave 0 training infrastructure, so the feedforward path acts as the first validated consumer of:

- explicit `model_family` identity;
- a common metrics schema;
- shared validation and smoke-test utilities.

## Main Components Used

### `config/training/feedforward/presets/baseline.yaml`

Provides:

- dataset batching parameters;
- point subsampling stride;
- optional maximum point cap per curve;
- explicit `experiment.model_family` identity for the shared training infrastructure;
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

The script writes its outputs under the configured training-run root, currently:

- `output/training_runs/feedforward/`

Typical generated artifacts include:

- a copy of the training config under `training_config.yaml`;
- a run metadata snapshot under `run_metadata.yaml`;
- TensorBoard logs;
- Lightning checkpoints;
- a text file containing the best checkpoint path;
- a family-agnostic YAML metrics artifact under `metrics_summary.yaml`;
- a markdown report summarizing the executed run.
- automatic family/program best-result registries under:
  - `output/registries/families/feedforward/`
  - `output/registries/program/`

Each physical run now writes into an immutable timestamped directory such as:

- `output/training_runs/feedforward/2026-03-17-20-05-11__te_feedforward_baseline/`

This directory is the `run_instance_id` location. The logical experiment name remains `experiment.run_name`.

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

Before a longer run, you can now validate the shared training wiring with:

```powershell
conda run -n standard_ml_codex_env python scripts/training/validate_training_setup.py --config-path config/training/feedforward/presets/trial.yaml --output-suffix validation_check
```

You can also run the minimal Lightning smoke test with:

```powershell
conda run -n standard_ml_codex_env python scripts/training/run_training_smoke_test.py --config-path config/training/feedforward/presets/trial.yaml --output-suffix smoke_test --fast-dev-run-batches 1
```

The training entry point prints a compact terminal report before training, keeps the Lightning progress bars active, avoids the previous raw configuration dump, suppresses the current low-signal Lightning startup tip plus the known `_pytree` sanity-check warning, and writes both validation and test results for the selected best checkpoint.

The current implementation also exposes a runtime configuration block in the YAML presets so GPU-oriented options such as mixed precision, cuDNN benchmarking, and non-blocking batch transfer can be enabled or disabled explicitly without editing the Python source.
