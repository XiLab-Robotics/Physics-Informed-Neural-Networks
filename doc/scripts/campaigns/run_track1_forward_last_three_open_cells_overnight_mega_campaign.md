# Track 1 Forward Last Three Open Cells Overnight Mega Campaign Launcher

## Overview

This launcher executes the prepared overnight mega forward-only `Track 1`
original-dataset residual repair campaign.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_forward_last_three_open_cells_overnight_mega_campaign.ps1`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches only the last grouped
forward amplitude repair items that are still non-green in the canonical
benchmark.

For the actual model execution step, the launcher invokes the original-dataset
runner:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`

The campaign purpose is final overnight closure pressure, not another
family-bank sweep:

- `forward` only
- amplitude only
- `3` grouped repair items
- `240` total YAML runs
- maximum depth concentrated on the last stubborn residual pair

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_forward_last_three_open_cells_overnight_mega_campaign.py
```

## Queue Design

Each queue item restricts the exact target scope through:

- `target_scope.mode: amplitudes_only`
- `target_scope.harmonic_order_filter: [k]`
- `training.enabled_families: [family]`

The retry policy is intentionally narrow but much deeper than the failed
`84`-run wave:

- `72` retries for each `yellow_single_surface_deep` pair
- `96` retries for the only `yellow_single_surface_stubborn_maxi` pair

This keeps the campaign aligned with the exact residual benchmark surface
instead of reopening already-green forward targets.

## Remote Bootstrap Contract

- queue parsing uses a temporary Python helper script instead of `python -c`
- remote Conda preflight checks use temporary Python helper scripts instead of
  inline Python
- Windows paths are serialized through Python-safe literals
- remote preflight validates `skl2onnx`, `onnxmltools`,
  `onnxconverter-common`, `xgboost`, and `lightgbm` when required by the queue
- remote artifact sync uses short deterministic temporary archive names instead
  of full slugged relative paths, preventing Windows staging-path overflow
  during post-run synchronization
- the operator console uses structured queue progress markers and suppresses
  raw `[CV] END ...` grid-search noise while preserving the per-run log files

## Launch Command

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_forward_last_three_open_cells_overnight_mega_campaign.ps1 -Remote
```
