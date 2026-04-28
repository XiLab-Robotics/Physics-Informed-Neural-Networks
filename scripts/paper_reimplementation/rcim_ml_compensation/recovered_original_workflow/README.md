# Recovered Original RCIM Workflow

This folder contains the repository-owned copy of the recovered original RCIM
workflow reorganized into one single three-stage surface.

It no longer keeps two competing copied roots such as `latest_snapshot/` and
`original_pipeline/`. Instead it is split by stage:

- `dataframe_creation/`
- `training/`
- `evaluation/`

The canonical recovered-original training branch used here comes from the
recovered `latest_snapshot/main_prediction_v17.py` source, but the copied file
inside this repository is now named `training/train_and_export_models.py`.

The recovered `1-main_prediction_v18.py` branch is intentionally not used as
the canonical paper training stage because the repository interpretation is
that the `ELMRegressor`-bearing `v18` script belongs to a later experimental
attempt rather than to the paper-faithful workflow surface.

## Folder Structure

### `dataframe_creation/`

Copied original dataframe-building stage:

- `create_dataframe.py`
- `statistics.py`
- `instance_v5.py`

Code role:

- `create_dataframe.py`
  original stage runner that reads original-style instance CSVs and generates a
  harmonic dataframe.
- `statistics.py`
  main helper used by the original stage to load `Instance` objects and expand
  harmonic amplitude/phase columns into a dataframe.
- `instance_v5.py`
  restored reference dependency required by the copied statistic helper.

Primary output:

- `dataFrame_prediction_Fw_v14_newFreq.csv`
- or `dataFrame_prediction_Bw_v14_newFreq.csv`

depending on the direction selected by the repository-owned wrapper.

### `training/`

Copied original training/export stage:

- `train_and_export_models.py`
- `predictor_multioutput.py`
- `requirements.txt`
- shipped recovered dataframe fixtures:
  - `dataFrame_prediction_Fw_v14_newFreq.csv`
  - `dataFrame_prediction_Bw_v14_newFreq.csv`

Code role:

- `train_and_export_models.py`
  narrow family-bank runner that loads one dataframe, filters `deg <= 35`,
  trains the recovered family list, exports ONNX, and writes prediction CSVs.
- `predictor_multioutput.py`
  original monolithic helper that contains the real multioutput training,
  export, and alternative-evaluation logic.
- the shipped CSVs
  are recovered snapshot inputs kept here for direct side-by-side inspection.

Canonical family set in this stage:

- `DT`
- `ET`
- `ERT`
- `RF`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`
- `MLP`

Important detail:

- the wrapper preserves the recovered `deg <= 35` thermal filter, where `deg`
  is the oil-temperature column in the recovered CSVs.

### `evaluation/`

Copied original offline-evaluation stage:

- `statistics.py`
- `evaluate_predictions.py`
- `evaluate_signals.py`
- `instance_v4.py`
- `instance_v5.py`

Code role:

- `evaluate_predictions.py`
  computes per-file evaluation tables and per-component paper-style exports.
- `evaluate_signals.py`
  computes signal-level aggregate errors from prediction CSVs.
- `statistics.py`
  original helper reused by the evaluation stage.
- `instance_v4.py` and `instance_v5.py`
  restored reference dependencies required by the copied evaluation logic.

Important limitation:

- the copied evaluation scripts are forward-specific in practice because they
  call forward-oriented prediction helpers and original naming conventions.
- the repository wrapper therefore allows evaluation only for the `forward`
  direction unless the code is manually widened later.

## Canonical Runner

Use the repository-owned wrapper:

`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py`

This wrapper exists so the copied original code can be run in the new stage
layout without editing the recovered source files themselves into a completely
different architecture.

The wrapper does three things:

1. runs the copied original logic stage by stage;
2. supplies the minimum compatibility glue needed by the copied files;
3. writes immutable validation artifacts under
   `output/validation_checks/paper_reimplementation_rcim_recovered_original_workflow/`.

## Stage Order

The intended execution order is:

1. dataframe creation
2. training
3. evaluation

That sequence corresponds directly to the original recovered pipeline shape.

## Commands

### 1. Print Stage Status

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --print-stage-status
```

### 2. Dataframe Creation Only

Forward:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage dataframe_creation `
  --direction forward `
  --instances-path "C:\path\to\original_instance_csv_dir" `
  --output-suffix forward_dataframe_rebuild
```

Backward:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage dataframe_creation `
  --direction backward `
  --instances-path "C:\path\to\original_instance_csv_dir" `
  --output-suffix backward_dataframe_rebuild
```

What the wrapper does in code terms:

- loads `dataframe_creation/statistics.py`;
- instantiates `Statistics`;
- calls `read_all_fft(instances_path)`;
- calls `genDfWithAmplEPhase('Fw')` or `genDfWithAmplEPhase('Bw')`;
- saves the resulting dataframe into the immutable artifact folder.

### 3. Training Only Using The Shipped Recovered CSV

Forward default:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage training `
  --direction forward `
  --output-suffix training_forward_default
```

Backward shipped CSV:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage training `
  --direction backward `
  --output-suffix training_backward_default
```

Specific family subset:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage training `
  --direction forward `
  --families DT,RF,HGBM `
  --output-suffix training_forward_subset
```

Training on a dataframe rebuilt by stage 1:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage training `
  --direction forward `
  --dataframe-path "C:\path\to\dataFrame_prediction_Fw_v14_newFreq.csv" `
  --output-suffix training_from_rebuilt_dataframe
```

What the wrapper does in code terms:

- loads `training/predictor_multioutput.py`;
- loads the selected CSV with `sep=';'` and `decimal=','`;
- applies the original `deg <= 35` filter;
- resolves all `ampl` and `phase` targets from the dataframe header;
- instantiates the recovered `v17` family bank;
- runs `MLModelMultipleOutput(...).predictorML_allForExport(...)`;
- writes original-style prediction CSVs;
- exports per-target ONNX files unless `--skip-onnx-export` is used.

### 4. Evaluation Only

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage evaluation `
  --direction forward `
  --instances-path "C:\path\to\original_instance_csv_dir" `
  --prediction-directory "C:\path\to\output_prediction\instV3.2_Fw" `
  --output-suffix evaluation_forward_manual
```

Skip one of the copied evaluation passes if needed:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage evaluation `
  --direction forward `
  --instances-path "C:\path\to\original_instance_csv_dir" `
  --prediction-directory "C:\path\to\output_prediction\instV3.2_Fw" `
  --skip-evaluate-signals `
  --output-suffix evaluation_prediction_only
```

What the wrapper does in code terms:

- loads `evaluation/statistics.py` as the original copied statistics helper;
- builds a `Statistics` object from the supplied instance directory;
- calls the copied `evaluatePredictionFile(...)` functions from:
  - `evaluate_predictions.py`
  - `evaluate_signals.py`
- materializes their original-style output files under one immutable runtime
  artifact root.

### 5. End-To-End Forward Run

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage all `
  --direction forward `
  --instances-path "C:\path\to\original_instance_csv_dir" `
  --output-suffix full_forward_rebuild
```

What happens:

1. dataframe creation writes a fresh recovered-style `Fw` dataframe;
2. training consumes that dataframe through the `v17` family bank;
3. evaluation consumes the generated prediction CSVs with the copied
   forward-specific evaluation stage.

## Artifact Layout

Each run writes into:

`output/validation_checks/paper_reimplementation_rcim_recovered_original_workflow/<timestamp>_<stage>_<direction>_<suffix>/`

Typical contents:

- `run_summary.json`
- `dataframe_creation/...`
- `training/output_prediction/...`
- `training/model_output_dir/...`
- `evaluation/original_style_runtime/...`

## Practical Interpretation

This folder is not a clean-room rewrite of the paper pipeline.

It is a repository-owned execution surface built around copied recovered code,
with just enough wrapper logic to make the three original stages inspectable
and runnable in sequence:

- the copied original stage files remain visible as copied code;
- the wrapper avoids mixing the recovered-original surface with the newer
  repository-designed workflows;
- the training stage is anchored to the recovered `v17` branch, not to the
  later `v18` ELM-bearing branch.
