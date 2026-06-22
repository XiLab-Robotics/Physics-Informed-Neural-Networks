# DataLoader Worker Auto-Sizing

## Overview

The local `polished_dataset_stage1_smoke_2026_06_21` run showed PyTorch
Lightning warnings that the train and validation dataloaders have too few
workers:

```text
The 'train_dataloader' does not have many workers which may be a bottleneck.
Consider increasing the value of the `num_workers` argument to `num_workers=31`.
```

The currently running first Stage 1 item,
`config/training/queue/polished_dataset_stage1_smoke/running/2026-06-22-12-46-43_001_trial.yaml`,
uses:

```yaml
dataset:
  num_workers: 0
  pin_memory: false
```

The remaining Stage 1 pending items already use `num_workers: 8` and mostly
`pin_memory: true`. The observed slowdown is therefore expected for the first
feedforward trial, because `num_workers: 0` makes the main process load
batches synchronously while the GPU waits.

PyTorch Lightning guidance is to use `num_workers > 0`, `pin_memory=True` for
GPU training, and persistent workers when worker startup overhead matters. The
repository datamodule already enables `persistent_workers` whenever
`num_workers > 0`, so the missing part is a safe way to resolve worker counts
automatically instead of preserving stale `0` values in older configs.

## Technical Approach

Add a repository-owned `auto` mode for dataloader worker selection. The intent
is not to blindly use the maximum value suggested by Lightning. On Windows,
too many worker processes can increase process-spawn overhead and RAM use,
especially with large CSV-backed datasets. The safer default is:

```text
resolved_num_workers = min(max_cpu_based_worker_count, repository_cap)
```

The initial cap should be conservative and overridable. A practical default is
`8`, because many existing successful GPU campaigns already use
`num_workers: 8` with `pin_memory: true`. The code should still support an
explicit integer for reproducibility-sensitive configs and should support
`auto` for new polished-dataset campaign configs and launcher overrides.

The implementation should:

1. Accept `dataset.num_workers: auto` in training YAML files.
2. Resolve `auto` inside shared training infrastructure before constructing
   `TransmissionErrorDataModule`.
3. Use an environment override such as `PINNS_DATALOADER_WORKERS` when the
   operator wants a specific value on a given machine.
4. Keep a repository cap such as `PINNS_DATALOADER_WORKER_CAP`, defaulting to
   `8`, so a machine with 32 logical CPUs does not automatically spawn 31
   workers unless explicitly requested.
5. Enable `pin_memory` automatically for CUDA-capable neural training when the
   config uses an auto worker profile, while preserving explicit `false` for
   tree or CPU-only configs.
6. Update the Stage 1 feedforward trial configuration path or launcher
   override so the first run no longer starts with `num_workers: 0`.
7. Keep smoke tests and one-batch validators forced to `num_workers: 0`,
   because those are diagnostic checks where process startup overhead and
   deterministic failure isolation matter more than throughput.

This change cannot speed up dataloaders already constructed in the currently
running Python process. It applies to newly launched runs only. If the current
first feedforward run is too slow, the operator should stop the campaign,
apply the approved patch, archive or clear the partially generated queue state,
and relaunch.

## Involved Components

- `scripts/training/shared_training_infrastructure.py`
  - resolves training YAML into runtime datamodule arguments.
- `scripts/training/transmission_error_datamodule.py`
  - constructs the actual PyTorch `DataLoader` objects and already enables
    `persistent_workers` for positive worker counts.
- `scripts/training/train_feedforward_network.py`
  - displays dataloader settings in the training summary.
- `scripts/campaigns/cross_wave/run_polished_dataset_stage1_smoke_campaign.ps1`
  - may need an explicit worker-profile or environment override for the Stage
    1 launcher.
- `scripts/campaigns/cross_wave/validate_polished_dataset_stage1_smoke_package.py`
  - should validate the worker auto-resolution contract without enabling
    multiprocessing during one-batch validation.
- `config/training/feedforward/presets/trial.yaml`
  - the current first Stage 1 source config that still contains
    `num_workers: 0`.
- `doc/running/active_training_campaign.yaml`
  - protected state that must record any stop/restart decision for the current
    Stage 1 attempt.

## Implementation Steps

1. If the current Stage 1 run is still executing and the user chooses to stop
   it, preserve its output as a failed or interrupted attempt instead of
   deleting artifacts.
2. Implement worker auto-resolution in shared training infrastructure:
   - explicit integer values remain unchanged;
   - `auto` reads `PINNS_DATALOADER_WORKERS` first;
   - otherwise it uses a capped CPU-based value;
   - invalid negative or non-integer values raise a clear error.
3. Add optional `auto_pin_memory` handling only where it is safe and visible;
   avoid silently changing tree-model configs that do not benefit from pinned
   CUDA transfers.
4. Update Stage 1 feedforward source or launcher behavior so the first queued
   feedforward run uses the auto worker profile.
5. Keep preflight and smoke-test paths forcing `num_workers: 0` where they
   intentionally avoid multiprocessing.
6. Run focused verification:
   - Python compile checks for touched Python files;
   - YAML parse checks for touched configs;
   - Stage 1 `-PreflightOnly`;
   - Stage 1 `-PreflightOnly -RunOneBatchValidation`;
   - a dry run or enqueue-only check proving the first queued config no longer
     contains `num_workers: 0` for real training.
7. Update `doc/running/active_training_campaign.yaml` to record whether the
   current slow attempt was allowed to finish, stopped, or replaced by a new
   worker-auto attempt.
