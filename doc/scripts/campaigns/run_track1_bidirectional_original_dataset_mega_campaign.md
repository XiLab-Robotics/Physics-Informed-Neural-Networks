# Track 1 Bidirectional Original-Dataset Mega Campaign Launcher

## Overview

This launcher executes the prepared large-scale `Track 1` bidirectional
original-dataset campaign package.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches the prepared
family-direction queue through the canonical remote exact-paper wrapper when
`-Remote` is used.

The remote bootstrap contract for this campaign is:

- queue parsing uses a temporary Python helper script instead of `python -c`;
- remote Conda preflight checks use temporary Python helper scripts instead of
  inline Python;
- Windows paths are serialized through Python-safe literals, so mapped roots
  such as `R:\` remain valid.
- remote preflight validates the full ONNX toolchain required by the queue:
  `skl2onnx`, `onnxmltools`, `onnxconverter-common`, `xgboost`, and
  `lightgbm`.

The prepared package covers:

- `forward` and `backward`;
- all `10` exact-paper families;
- `20` split-seed attempts per family-direction surface;
- total queue size `400`.

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py
```

## Launch Command

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_original_dataset_mega_campaign.ps1 -Remote
```
