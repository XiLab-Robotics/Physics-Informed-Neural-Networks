# Track 1 Forward Original-Dataset Remote Micro Campaign Launcher

## Overview

This launcher executes the prepared `Track 1` forward-only remote micro
campaign.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_forward_original_dataset_remote_micro_campaign.ps1`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches exactly one
family-specific run for each of the `10` exact-paper families through the
canonical remote exact-paper wrapper when `-Remote` is used.

For the actual family execution step, the launcher invokes the original-dataset
runner:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`

The campaign purpose is a relaunch gate, not a scientific benchmark wave:

- one `forward` run per family;
- total queue size `10`;
- validation of the current remote launcher stack after the interrupted
  bidirectional mega-campaign discard;
- validation of the current `MLP` stabilization;
- validation of the current operator-facing progress and log surface.

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_forward_original_dataset_remote_micro_campaign.py
```

## Remote Bootstrap Contract

- queue parsing uses a temporary Python helper script instead of `python -c`;
- remote Conda preflight checks use temporary Python helper scripts instead of
  inline Python;
- Windows paths are serialized through Python-safe literals;
- remote preflight validates `skl2onnx`, `onnxmltools`,
  `onnxconverter-common`, `xgboost`, and `lightgbm` when required by the queue;
- the operator console uses structured queue progress markers and suppresses
  raw `[CV] END ...` grid-search noise;
- the operator console suppresses repeated Torch `triton not found` noise while
  preserving the full per-run log files.

## Launch Command

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_forward_original_dataset_remote_micro_campaign.ps1 -Remote
```
