# RCIM Original HGBM ONNX Export Scalar Sanitization

## Overview

The recovered-original RCIM export stage currently persists Python `.pkl`
artifacts for `HGBM` targets but writes `*.onnx.export_error.txt` files instead
of valid ONNX models. The observed failure comes from `skl2onnx` creating a
`TreeEnsembleRegressor` node with integer attribute lists that still contain
NumPy scalar or boolean values from scikit-learn histogram-tree nodes.

Example failing artifact:

`output/training_campaigns/rcim_original/forward/2026-05-11-08-50-55__fw_export_bundle/export/model_output_dir/HistGradientBoostingRegressor_paperReferenceExport_3.8_allFreq_MultiOutput_tot_fft_y_Fw_filtered_ampl_0.onnx.export_error.txt`

The failure signature is:

`TypeError: Field onnx.AttributeProto.ints: Expected an int, got a boolean.`

## Technical Approach

Apply a narrow recovered-original exporter fix in
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`.

The implementation should mirror the already validated exact-paper model-bank
patch in
`scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`:

- import the required `skl2onnx.common.tree_ensemble` and
  `skl2onnx.operator_converters.random_forest` modules;
- add a temporary context manager for `HistGradientBoostingRegressor` export;
- replace `add_tree_to_attribute_pairs_hist_gradient_boosting` only inside the
  HGBM conversion window;
- emit all ONNX node identifiers and missing-value branch flags as plain Python
  `int` values;
- restore the original converter functions immediately after conversion;
- keep `.pkl` persistence and existing `*.onnx.export_error.txt` failure capture
  unchanged for non-HGBM export failures.

This is a compatibility shim for the local `scikit-learn` plus `skl2onnx`
surface, not a training-behavior change. It does not alter HGBM hyperparameters,
dataset selection, evaluation metrics, or the recovered-original output folder
contract.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `output/training_campaigns/rcim_original/forward/*/export/model_output_dir/`
- Reference implementation:
  `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`

## Implementation Steps

1. Add the missing `contextlib` and `Any` imports plus the two `skl2onnx`
   converter-module imports to the recovered-original `predictorML.py`.
2. Add a local `_patched_hist_gradient_boosting_onnx_converter()` context
   manager that copies the exact-paper scalar-sanitizing logic.
3. In `MLModelMultipleOutput.exportModel`, detect
   `HistGradientBoostingRegressor` before the generic `convert_sklearn` branch
   and wrap only that conversion call in the temporary patch.
4. Preserve `target_opset=12` behavior where family-specific converters already
   require it, but do not broaden the scope of this fix to unrelated families.
5. Verify with a focused forward `HGBM` export rerun using the same
   `summaryBestParameter+_3.8_allFreq.csv` that produced the failing artifact.
6. Confirm the rerun writes `.onnx` files for HGBM and no new
   `HistGradientBoostingRegressor*.onnx.export_error.txt` files.
7. Run Markdown warning checks on the touched Markdown scope before closing the
   implementation task.

No subagent is planned for this fix. If subagent use becomes necessary later,
the task boundary and approval requirement must be recorded before requesting
approval.
