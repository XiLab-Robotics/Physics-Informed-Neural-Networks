# Track 1 Forward Final Open-Cells Campaign Launcher

## Overview

This launcher executes the prepared final forward-only `Track 1`
original-dataset residual repair campaign.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_forward_final_open_cells_campaign.ps1`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches only the last grouped
forward repair items that are still non-green in the canonical benchmark.

For the actual model execution step, the launcher invokes the original-dataset
runner:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`

The campaign purpose is final residual closure, not another family-bank sweep:

- `forward` only;
- `8` grouped repair items;
- `76` total YAML runs;
- escalation depth only for the currently red amplitude pairs.

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_forward_final_open_cells_campaign.py
```

## Queue Design

Each queue item restricts the exact target scope through:

- `target_scope.mode: amplitudes_only` or `phases_only`
- `target_scope.harmonic_order_filter: [k]`
- `training.enabled_families: [family]`

The retry policy is two-tier:

- `8` base retries for every residual target pair;
- `4` extra retries only for the `3` currently red amplitude pairs.

This keeps the campaign aligned with the exact residual benchmark surface
instead of reopening already-green forward targets.

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
.\scripts\campaigns\track1\exact_paper\run_track1_forward_final_open_cells_campaign.ps1 -Remote
```
