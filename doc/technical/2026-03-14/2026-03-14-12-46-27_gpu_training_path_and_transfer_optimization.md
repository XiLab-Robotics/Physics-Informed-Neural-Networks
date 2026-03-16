# GPU Training Path And Transfer Optimization

## Overview

This document defines a focused optimization pass for the current feedforward training workflow so GPU execution is used more efficiently where it provides a practical benefit.

The goal is not to force maximum GPU saturation at any cost. The goal is to remove avoidable bottlenecks in the CPU-to-GPU path and expose safe performance options that can reduce training time without hurting numerical stability or engineering clarity.

The current training stack already has a good baseline:

- Lightning is responsible for moving the model and training batches to the selected device;
- the dataloaders already use `pin_memory` and `persistent_workers`;
- `torch.set_float32_matmul_precision("high")` is already enabled;
- the current configuration keeps `deterministic: false`, which avoids an unnecessary reproducibility penalty.

However, the current implementation still leaves several GPU-performance opportunities unexposed:

- no explicit mixed-precision configuration is available in the training YAML or `Trainer`;
- no explicit asynchronous host-to-device transfer path is implemented for the custom batch dictionary;
- no Trainer-level `benchmark` control is exposed for the fixed-shape feedforward workload;
- no runtime summary prints the actual selected precision or transfer-related optimization mode.

Context7 documentation was consulted for:

- PyTorch `/pytorch/pytorch`
- PyTorch Lightning `/lightning-ai/pytorch-lightning`

The consulted documentation confirms:

- pinned host memory plus `non_blocking=True` can improve host-to-GPU transfer overlap;
- mixed precision through Lightning `precision=` is the preferred high-level integration path for GPU acceleration;
- `benchmark=True` can speed up fixed-shape CUDA workloads when tensor sizes remain stable;
- `set_float32_matmul_precision("high")` is a documented speed-oriented tradeoff and is already aligned with the current repository.

## Technical Approach

### Current Behavior Assessment

The current workflow does not appear to be fundamentally broken from a GPU-placement perspective.

Lightning will move the module and batch tensors to the selected accelerator during training. That means the current concern is not "are tensors ever on GPU?" but rather:

1. whether the batch transfer path is as efficient as it could be;
2. whether arithmetic precision and backend settings are leaving practical speed on the table;
3. whether the current dataloader/collate shape creates a visible CPU-side bottleneck before each GPU step.

### Recommended Optimization Scope

The recommended implementation scope is intentionally conservative:

1. expose GPU optimization settings in the training YAML;
2. add explicit non-blocking batch transfer support for the training batch dictionary;
3. enable optional mixed precision through Lightning;
4. expose optional cuDNN benchmarking for stable-shape workloads;
5. improve runtime reporting so the selected GPU optimization mode is visible.

This keeps the workflow understandable and TwinCAT-oriented engineering clarity intact.

### Proposed Configuration Additions

Add a dedicated `runtime` or `acceleration` section to the training configuration with entries such as:

- `accelerator`
- `devices`
- `precision`
- `benchmark`
- `use_non_blocking_transfer`

Recommended initial defaults:

- `accelerator: auto`
- `devices: auto`
- `precision: 32`
- `benchmark: true`
- `use_non_blocking_transfer: true`

Reasoning:

- `precision: 32` preserves the current numerical baseline by default;
- `benchmark: true` is appropriate for this feedforward workflow because input dimensionality is fixed and the point-wise batches are shape-stable enough to benefit;
- `use_non_blocking_transfer: true` is low risk when batches come from pinned memory;
- mixed precision should be available, but not forced by default without a quick validation pass.

### Mixed Precision Recommendation

The first recommended optional speed mode is Lightning mixed precision through `Trainer(precision=...)`.

Practical rollout:

- keep `32` as the default baseline;
- add support for `16-mixed` and `bf16-mixed`;
- prefer `bf16-mixed` only if the local GPU stack supports it cleanly;
- otherwise use `16-mixed` as the first optional acceleration mode.

This is preferable to a manual AMP rewrite because Lightning already integrates precision control at the Trainer level.

### Batch Transfer Recommendation

The dataloader currently returns a dictionary containing tensors and lists.

Because the training code uses a custom collate structure, the safest explicit optimization is to handle device transfer in the datamodule or LightningModule using a dedicated transfer hook and pass `non_blocking=True` for tensors when enabled.

The implementation should:

- recursively walk the batch dictionary;
- move only tensors;
- preserve lists and strings unchanged;
- use `non_blocking=True` only when the optimization flag is enabled.

This makes the transfer path explicit and easy to inspect instead of relying only on implicit framework behavior.

### Dataloader Bottleneck Review

The current dataloader path is already reasonably structured:

- dataset samples are CPU tensors;
- point extraction happens in the collate function;
- pinned memory is enabled in the YAML baseline;
- persistent workers are enabled when `num_workers > 0`.

This suggests the next likely bottleneck is not "GPU tensors are missing" but rather:

- CPU-side collation and point concatenation;
- synchronous host-to-device copies of the resulting tensors.

The proposed optimization pass therefore targets transfer efficiency first, not a premature rewrite of dataset preprocessing.

### What Should Not Be Added Yet

The following ideas are intentionally out of scope for the first pass:

- `torch.compile` by default;
- aggressive model-graph rewrites;
- returning CUDA tensors directly from worker processes;
- major dataset caching redesign;
- multi-GPU strategy changes.

These may help in some contexts, but they add complexity and are not justified before measuring the simpler transfer and precision improvements.

## Involved Components

- `README.md`
  Must reference this technical document.
- `doc/README.md`
  Should reference this technical document for the internal documentation index.
- `doc/guide/project_usage_guide.md`
  Must be updated after approval because the training workflow will expose new runtime/GPU options.
- `config/training/feedforward/presets/baseline.yaml`
  Will need new GPU/runtime optimization keys.
- `config/training/feedforward/presets/best_training.yaml`
  Should be checked for alignment if the new runtime keys become part of the standard training schema.
- `scripts/training/train_feedforward_network.py`
  Trainer construction point where precision, benchmark, accelerator, and devices should be made configurable.
- `scripts/training/transmission_error_datamodule.py`
  Main candidate for explicit non-blocking transfer handling for custom batch dictionaries.
- `scripts/training/transmission_error_regression_module.py`
  May need minor runtime reporting or transfer-related support depending on the final implementation split.
- `doc/reference_summaries/06_Programming_Style_Guide.md`
  Style reference that must continue to guide any modifications.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. Wait for explicit user approval before modifying training code or YAML files.
3. After approval, add explicit GPU/runtime optimization settings to the feedforward training configuration schema.
4. Update the Trainer construction so precision, benchmark, accelerator, and device selection are controlled by configuration.
5. Add an explicit batch-transfer path for tensors with optional `non_blocking=True` behavior.
6. Extend runtime reporting so the selected GPU optimization mode is visible during training.
7. Update `doc/guide/project_usage_guide.md` with the new configuration keys and recommended GPU usage modes.
8. Verify with at least command-level smoke tests and one short training-path validation run if the user later approves execution.
