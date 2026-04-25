# Track 1 Forward Original-Dataset Remote Diagnostic Campaign Launcher

## Overview

This launcher executes the prepared `Track 1` forward-only remote diagnostic
campaign.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_forward_original_dataset_remote_diagnostic_campaign.ps1`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches exactly one
family-specific run for each of the `10` exact-paper families through the
canonical remote exact-paper wrapper when `-Remote` is used.

The campaign purpose is diagnostic, not benchmark-complete:

- one `forward` run per family;
- total queue size `10`;
- explicit remote warning and error inspection surface;
- ONNX export validation after the dependency-guard repair;
- `MLP` convergence behavior check after the maximum-iteration adjustment.

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_forward_original_dataset_remote_diagnostic_campaign.py
```

## Remote Bootstrap Contract

- queue parsing uses a temporary Python helper script instead of `python -c`;
- remote Conda preflight checks use temporary Python helper scripts instead of
  inline Python;
- Windows paths are serialized through Python-safe literals;
- remote preflight validates `skl2onnx`, `onnxmltools`,
  `onnxconverter-common`, `xgboost`, and `lightgbm` when required by the queue.

## Launch Command

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_forward_original_dataset_remote_diagnostic_campaign.ps1 -Remote
```
