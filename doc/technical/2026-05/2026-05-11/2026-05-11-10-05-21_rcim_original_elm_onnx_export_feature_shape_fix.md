# RCIM Original ELM ONNX Export Feature Shape Fix

## Overview

The recovered-original RCIM export workflow currently fails the per-target ONNX
export for `ELMRegressor` models during the `paper_export` stage. The runtime
warning surface shows repeated `AttributeError: 'ELMRegressor' object has no
attribute 'n_features_in_'` failures across amplitude and phase targets.

The current workflow already preserves the Python `.pkl` artifacts and the
`*.onnx.export_error.txt` sidecars, so the failure is isolated to the ONNX
input-shape preparation path. The goal of this fix is to restore successful
ELM ONNX export without changing the training protocol, family selection
surface, or the existing error-sidecar contract for other exporters.

## Technical Approach

The ONNX exporter in
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
currently builds the generic `initial_type` from `est.n_features_in_`. That
assumption is valid for many scikit-learn estimators but not for the fitted
`skelm.ELMRegressor` objects used in this workflow.

The narrow fix is to introduce a fitted-estimator feature-dimension resolver
and a repo-owned `ELMRegressor` ONNX converter registration used by the export
path:

1. Prefer `n_features_in_` when the fitted estimator exposes it.
2. Otherwise recover the feature count from a stable fitted ELM attribute
   surface discovered in the local object state.
3. Register a dedicated `skl2onnx` converter for the supported fitted
   `ELMRegressor` surface because native `skl2onnx` conversion does not ship a
   shape calculator or converter for that estimator class.
4. Raise a clear exporter-local error only if no valid fitted feature shape can
   be resolved or if the fitted ELM configuration falls outside the supported
   converter surface.

This keeps the current `XGBRegressor`, `LGBMRegressor`, and generic
scikit-learn export paths intact while extending the recovered-original export
surface to a fitted estimator class that does not implement the common
`n_features_in_` convention.

Context7 did not provide a usable `skelm` documentation surface in this
session, so this fix will rely on local code inspection plus runtime-safe
introspection of the fitted `ELMRegressor` state already present in the
workflow.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/technical/2026-05/2026-05-11/2026-05-11-10-05-21_rcim_original_elm_onnx_export_feature_shape_fix.md`

## Implementation Steps

1. Inspect the fitted `ELMRegressor` state used by the recovered-original
   export path to identify the stable input-feature-dimension surface.
2. Add a narrow feature-dimension resolver in `predictorML.py` for ONNX export.
3. Update the generic ONNX export branch to use the resolver instead of
   assuming `n_features_in_`.
4. Run a narrow export-oriented validation path that confirms `ELMRegressor`
   can now produce ONNX artifacts instead of only error sidecars.
5. Update the recovered-original workflow documentation if the exporter support
   contract changes in a user-visible way.
6. Run Markdown QA on the touched technical-document scope before closing the
   task.
