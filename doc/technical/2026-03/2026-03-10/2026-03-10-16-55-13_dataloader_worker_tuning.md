# Dataloader Worker Tuning

## Overview

This document defines the tuning of the feedforward-training dataloader settings currently left at the conservative baseline:

- `num_workers: 0`
- `pin_memory: false`

The current configuration is stable and simple to debug, but it is likely underusing the available CPU and GPU pipeline during training.

The goal of this change is to improve practical training throughput for the current PyTorch Lightning baseline while keeping the configuration safe for the user's Windows + Conda environment.

## Technical Approach

The tuning will be applied to the existing feedforward training stack:

- `config/feedforward_network_training.yaml`
- `training/transmission_error_datamodule.py`
- `training/train_feedforward_network.py`

The decision will follow official PyTorch and Lightning guidance:

- PyTorch documents that `num_workers > 0` enables multi-process data loading and that `pin_memory=True` can speed up CPU-to-GPU transfers;
- Lightning explicitly recommends `num_workers > 0` and `pin_memory=True` for GPU-backed training, while also noting that the best worker count must be tuned empirically.

Because this repository runs on Windows and uses custom collation plus a dataset with large curve files, the tuning should stay incremental rather than jumping directly to a very large worker count.

### Planned Tuning Strategy

The initial tuned baseline will:

- set `pin_memory: true`
- raise `num_workers` from `0` to a moderate value suitable for the current workstation

The proposed starting point is:

- `num_workers: 4`
- `pin_memory: true`

Reasoning:

- `num_workers=0` removes multiprocessing overhead but can bottleneck GPU training because all loading and collation happen in the main process;
- a moderate worker count is safer on Windows than starting with a very high value;
- the current point-extraction and collation logic is simple enough that parallel loading should help;
- pinned memory is a low-risk optimization when training on CUDA devices and the current environment already uses an NVIDIA GPU.

### Scope Of The Change

The implementation should:

1. update the default training config;
2. keep the datamodule interface unchanged so future models reuse the same tuning path;
3. verify that the tuned config still works with the current feedforward Lightning workflow;
4. update `doc/guide/project_usage_guide.md` because this changes a user-facing training configuration and expected runtime behavior.

The tuning should not:

- change the dataset format;
- change the feedforward architecture;
- change loss, optimizer, or checkpoint logic;
- introduce complicated auto-detection logic before a simple stable baseline is confirmed.

## Involved Components

- `doc/technical/2026-03/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md`
- `README.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `config/feedforward_network_training.yaml`
- `training/transmission_error_datamodule.py`
- `training/train_feedforward_network.py`

## Implementation Steps

1. Add this technical document and reference it from the documentation indexes.
2. After user approval, update the default feedforward training config to the tuned dataloader settings.
3. Verify that the current datamodule and training workflow still run correctly in `standard_ml_codex_env`.
4. Update `doc/guide/project_usage_guide.md` so the training section documents the new default dataloader settings and their meaning.
5. Verify repository status and create a Git commit summarizing the tuning change.
