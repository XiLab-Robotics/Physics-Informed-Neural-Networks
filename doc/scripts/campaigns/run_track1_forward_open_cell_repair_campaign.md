# Track 1 Forward Open-Cell Repair Campaign Launcher

## Overview

This launcher executes the prepared forward-only `Track 1` original-dataset
open-cell repair campaign.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_forward_open_cell_repair_campaign.ps1`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches only the grouped
forward repair items that are still non-green in the canonical benchmark.

For the actual model execution step, the launcher invokes the original-dataset
runner:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`

The campaign purpose is residual closure, not a fresh full-bank sweep:

- `forward` only;
- grouped by `family + target_kind + harmonic_order`;
- `30` grouped repair items;
- `10` retries per repair item;
- `300` total YAML runs.

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_forward_open_cell_repair_campaign.py
```

## Queue Design

Each queue item restricts the exact target scope through:

- `target_scope.mode: amplitudes_only` or `phases_only`
- `target_scope.harmonic_order_filter: [k]`
- `training.enabled_families: [family]`

This keeps each run aligned with one residual forward benchmark target rather
than retraining unrelated harmonic outputs.

## Remote Bootstrap Contract

- queue parsing uses a temporary Python helper script instead of `python -c`;
- remote Conda preflight checks use temporary Python helper scripts instead of
  inline Python;
- Windows paths are serialized through Python-safe literals;
- remote preflight validates `skl2onnx`, `onnxmltools`,
  `onnxconverter-common`, `xgboost`, and `lightgbm` when required by the queue;
- remote artifact sync uses short deterministic temporary archive names instead
  of full slugged relative paths, preventing Windows staging-path overflow
  during post-run synchronization;
- the operator console uses structured queue progress markers and suppresses
  raw `[CV] END ...` grid-search noise while preserving the per-run log files.

## Launch Command

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_forward_open_cell_repair_campaign.ps1 -Remote
```
