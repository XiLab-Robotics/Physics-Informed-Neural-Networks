# Recovered Original RCIM Workflow

This folder is the repository-owned direct execution surface for the recovered
original RCIM workflow rebuilt from the newly recovered full original root
under:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`

The goal here is not to redesign the original logic. The goal is to keep the
original code modules almost unchanged and only modernize:

- entrypoint names;
- folder layout;
- path handling;
- repository-owned output roots.

## Folder Structure

- `create_dataframe.py`
  direct entrypoint for the original dataframe-creation stage.
- `training_models.py`
  direct entrypoint that unifies the original `v17`, `v17+tuning`, and `v18`
  training flows behind CLI arguments.
- `evaluate_models.py`
  direct entrypoint for the original paper-table evaluation stage.
- `utilities/`
  copied original support modules kept as close as possible to the recovered
  source.

Utility modules:

- `utilities/statistics.py`
  copied from original `statistic.py`.
- `utilities/instance_v4.py`
  copied original signal-reconstruction dependency for evaluation.
- `utilities/instance_v5.py`
  copied original instance/FFT dependency for dataframe creation.
- `utilities/predictorML.py`
  copied original `predictorML_v7.py` with only one minimal compatibility
  adjustment so the shipped `v17` call signature remains runnable.

## Original-To-New Mapping

- `0-main_createDFforPrediction.py`
  -> `create_dataframe.py`
- `1.1-main_prediction_v17.py`
  -> `training_models.py --mode export`
- `1.1-main_prediction_v17.py` plus
  `predictorMLCrossValidationWithHyperparameter(...)`
  -> `training_models.py --mode retune`
- `1-main_prediction_v18.py`
  -> `training_models.py --mode paper_eval`
- `2-main_evaluatePrediction_v4.py`
  -> `evaluate_models.py`
- `statistic.py`
  -> `utilities/statistics.py`
- `predictorML_v7.py`
  -> `utilities/predictorML.py`
- `instance_v4.py`
  -> `utilities/instance_v4.py`
- `instance_v5.py`
  -> `utilities/instance_v5.py`

## Execution Order

The intended operator order is:

1. `create_dataframe.py`
2. `training_models.py`
3. `evaluate_models.py`

That matches the canonical author workflow:

- build dataframe;
- train/export/tune models;
- generate paper tables from prediction outputs.

## Path Policy

The original scripts wrote into mutable local folders such as:

- `instances_V3/`
- `output_prediction/`
- `model_output_dir/`
- `evaluation/`

The rebuilt repository surface still creates those original-style folders when
needed, but only inside one repository-owned runtime root under:

- `output/validation_checks/paper_reimplementation_rcim_recovered_original_workflow/`

Each direct script creates its own timestamped runtime folder there unless
`--output-root` is provided explicitly.

This keeps the original relative-path logic working while avoiding scattered
mutable outputs inside the script folder itself.

## 1. Dataframe Creation

Entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`

What it does in code terms:

- prepends `utilities/` to `sys.path`;
- loads `Statistics` from `utilities/statistics.py`;
- prepares a runtime-local `instances_V3/` cache folder;
- reuses `.pickle` files if the input directory already contains them;
- otherwise lets the original logic read CSVs and create the cache;
- calls `genDfWithAmplEPhase('Fw')` or `genDfWithAmplEPhase('Bw')`;
- writes the original-style dataframe CSV into the runtime root.

Default input:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/instances_V3/`

Example:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py `
  --direction backward `
  --output-suffix bw_dataframe
```

Example with raw CSV directory:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py `
  --instances-path "C:\path\to\raw_instance_csv_dir" `
  --direction forward `
  --output-suffix fw_from_raw
```

Primary outputs:

- `dataFrame_prediction_Fw_v14_newFreq.csv`
- or `dataFrame_prediction_Bw_v14_newFreq.csv`
- plus `run_summary.json`

## 2. Training And Export

Entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`

This script intentionally unifies three original behaviors.

### Mode `export`

This mirrors the role of `1.1-main_prediction_v17.py`:

- full-dataset training/export;
- default family surface from the shipped `v17` file;
- ONNX export through the copied original predictor helper.

Example:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py `
  --mode export `
  --direction forward `
  --output-suffix v17_export_fw
```

### Mode `retune`

This mirrors the author guidance:

- start from the `v17` structure;
- replace `predictorML_allForExport(...)` with
  `predictorMLCrossValidationWithHyperparameter(...)`;
- use this when the dataset changes or is intentionally restricted.

Example:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py `
  --mode retune `
  --direction forward `
  --test-size 0.20 `
  --families DT,RF,HGBM `
  --output-suffix retune_fw_subset
```

### Mode `paper_eval`

This mirrors `1-main_prediction_v18.py`:

- load the selected dataframe;
- apply the original `deg <= 35` filter unless disabled explicitly;
- use the tuned family list from the recovered `v18` file;
- run the original held-out `80/20` evaluation path.

Example:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py `
  --mode paper_eval `
  --direction forward `
  --test-size 0.20 `
  --output-suffix v18_fw
```

Example for future `Bw` replay:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py `
  --mode paper_eval `
  --direction backward `
  --dataframe-path "C:\path\to\dataFrame_prediction_Bw_v14_newFreq.csv" `
  --output-suffix v18_bw
```

Shared notes:

- default dataframe inputs come from the shipped recovered `Fw`/`Bw` CSVs;
- the script copies the selected dataframe into the runtime root under the
  original filename;
- original-style folders such as `output_prediction/` and `model_output_dir/`
  are created inside the runtime root;
- `run_summary.json` records the selected mode, dataframe, families, and
  artifact locations.

## 3. Evaluation

Entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py`

What it does in code terms:

- prepends `utilities/` to `sys.path`;
- loads `Statistics` from `utilities/statistics.py`;
- prepares a runtime-local `instances_V3/` cache folder;
- copies the selected prediction directory into:
  `output_prediction/instV3.8_Fw_allFreq_def/` inside the runtime root;
- runs the recovered `2-main_evaluatePrediction_v4.py` logic against that
  copied prediction set;
- writes the original-style evaluation CSVs into `evaluation/V3.9/`.

Important current limitation:

- the shipped original evaluation code is still forward-shaped in practice;
- this direct script therefore supports only `forward`/`Fw` for now.

Example:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py `
  --direction forward `
  --prediction-directory "C:\path\to\output_prediction\instV3.8_Fw_allFreq_def" `
  --output-suffix eval_fw
```

## Runtime Output Layout

Typical runtime root:

`output/validation_checks/paper_reimplementation_rcim_recovered_original_workflow/<timestamp>__<stage>_<mode_or_direction>_<suffix>/`

Typical contents:

- `run_summary.json`
- `instances_V3/`
- `dataFrame_prediction_*.csv`
- `output_prediction/`
- `model_output_dir/`
- `evaluation/`

## Practical Interpretation

This surface is not a clean-room rewrite of the original RCIM workflow.

It is a direct repository-owned execution layout built from the recovered
original scripts, with only these deliberate changes:

- the three main stages are direct top-level entrypoints;
- support code is grouped under `utilities/`;
- path handling is repository-owned and artifact-root aware;
- `v17`, `v17+tuning`, and `v18` are unified under one training entrypoint.
