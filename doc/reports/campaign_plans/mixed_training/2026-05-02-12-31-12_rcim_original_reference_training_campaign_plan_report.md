# RCIM Original Reference Training Campaign Plan Report

## Overview

This planning report prepares the operator-run commands for retraining the
recovered original RCIM workflow and staging the resulting model artifacts
under `models/paper_reference/rcim_original/`.

This is not a RCIM Model-Bank Reproduction benchmark refresh. It is a separate paper-reference
surface that keeps the recovered original workflow outputs distinct from the
existing `models/paper_reference/rcim_track1/` archives.

## Objective

Prepare the exact commands needed to:

- replay the shipped `forward` tuned-parameter training path with `v18`
  semantics;
- retune the `backward` family hyperparameters with the recovered `v17`
  cross-validation path;
- document the manual checkpoint currently required before a later
  `backward` tuned replay can be launched.

## Safety Constraints

| Setting | Value |
| --- | --- |
| Active Campaign State | `running`, untouched |
| Protected Files | `doc/running/active_training_campaign.yaml` and its listed protected files remain untouched |
| Training Execution In This Turn | not performed |
| Output Root Policy | isolated under `models/paper_reference/rcim_original/` |
| Dataframe Source Policy | use shipped recovered `Fw` / `Bw` CSVs unless dataframe regeneration is explicitly requested |

## Planned Runtime Roots

| Direction | Runtime Root Pattern |
| --- | --- |
| `forward` | `models/paper_reference/rcim_original/forward/source_runs/<run_instance_id>/` |
| `backward` | `models/paper_reference/rcim_original/backward/source_runs/<run_instance_id>/` |

## Current Functional Limitation

The repository-owned `retune` mode writes the best hyperparameters to CSV, but
the repository-owned `paper_eval` mode still consumes hardcoded tuned
estimators from `training_models.py`.

Because of that, the `backward` flow cannot yet be reduced to one continuous
CLI-only pipeline. A manual checkpoint is still required between:

- `backward retune`
- `backward paper_eval`

## Operator Commands

### 1. Optional Root Preparation

```powershell
New-Item -ItemType Directory -Force "models\paper_reference\rcim_original\forward\source_runs" | Out-Null
New-Item -ItemType Directory -Force "models\paper_reference\rcim_original\backward\source_runs" | Out-Null
```

### 2. Optional Dataframe Regeneration

Regenerate `Fw` from the original instances only if you do not want to reuse
the shipped recovered CSV:

```powershell
$fwDfRunId = "$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')__fw_dataframe_refresh"
python -B "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\create_dataframe.py" `
  --direction forward `
  --output-root "models\paper_reference\rcim_original\forward\source_runs\$fwDfRunId"
```

Regenerate `Bw` from the original instances only if you do not want to reuse
the shipped recovered CSV:

```powershell
$bwDfRunId = "$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')__bw_dataframe_refresh"
python -B "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\create_dataframe.py" `
  --direction backward `
  --output-root "models\paper_reference\rcim_original\backward\source_runs\$bwDfRunId"
```

### 3. Forward Tuned Replay With Recovered `v18`

This is the direct `paper_eval` replay using the recovered tuned family map:

```powershell
$fwRunId = "$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')__fw_v18_paper_reference"
python -B "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py" `
  --mode paper_eval `
  --direction forward `
  --output-root "models\paper_reference\rcim_original\forward\source_runs\$fwRunId"
```

If you want to restrict the replay to a subset of families:

```powershell
$fwRunId = "$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')__fw_v18_subset"
python -B "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py" `
  --mode paper_eval `
  --direction forward `
  --families "SVR,MLP,RF,DT,ET,ERT,GBM,HGBM,LGBM,XGBM,ELM" `
  --output-root "models\paper_reference\rcim_original\forward\source_runs\$fwRunId"
```

### 4. Backward Retuning With Recovered `v17` Cross-Validation

This is the parameter-search stage that must run before any valid `backward`
`paper_eval` replay:

```powershell
$bwRetuneRunId = "$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')__bw_v17_retune"
python -B "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py" `
  --mode retune `
  --direction backward `
  --output-root "models\paper_reference\rcim_original\backward\source_runs\$bwRetuneRunId"
```

If you want to retune only one family at a time:

```powershell
$bwRetuneRunId = "$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')__bw_v17_retune_svr"
python -B "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py" `
  --mode retune `
  --direction backward `
  --families "SVR" `
  --output-root "models\paper_reference\rcim_original\backward\source_runs\$bwRetuneRunId"
```

### 5. Manual Backward Parameter Handoff Checkpoint

After the `backward retune` run, inspect:

- `models/paper_reference/rcim_original/backward/source_runs/<run_instance_id>/output_prediction/summaryBestParameter+*.csv`

That CSV is the current repository-owned handoff artifact containing the
`best_params_` values exported by
`predictorMLCrossValidationWithHyperparameter(...)`.

At the moment, those tuned parameters are not yet consumable automatically by
`--mode paper_eval`.

### 6. Deferred Backward Tuned Replay

Only after the tuned `backward` parameters have been transferred into the
`paper_eval` tuned-family map should you run:

```powershell
$bwRunId = "$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')__bw_v18_paper_reference"
python -B "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py" `
  --mode paper_eval `
  --direction backward `
  --output-root "models\paper_reference\rcim_original\backward\source_runs\$bwRunId"
```

## Expected Output Surface

Each runtime root produced by the commands above will contain the original
workflow staging surface, including:

- copied dataframe CSV;
- `output_prediction/`;
- `model_output_dir/`;
- `run_summary.json`.

The current commands do not yet build the full curated
`rcim_track1`-style family archive structure under
`models/paper_reference/rcim_original/`. They only stage the raw source runs
there in an orderly way.

## Next Follow-Up

If the user wants the full `rcim_track1`-style curated archive surface for
`rcim_original/`, the next repository task should add a dedicated packaging
step that:

- splits the staged source runs by family;
- copies ONNX and Python artifacts into family archive roots;
- writes `reference_inventory.yaml`;
- writes dataset and split provenance manifests;
- writes per-family README documentation.
