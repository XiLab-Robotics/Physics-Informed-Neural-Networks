# tree Global Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `tree`
- Family Key: `tree`
- Scope: `global`
- Training Variant: `global`
- Run Name: `te_hist_gbr_tabular`
- Run Instance Id: `2026-03-20-15-17-30__te_hist_gbr_tabular`
- Model Type: `hist_gradient_boosting`
- Validation MAE: `0.002719 deg`
- Test MAE: `0.002885 deg`
- Test RMSE: `0.003607 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/tree/global/python/tree_model.pkl`
- `onnx/` winner artifact: `models/exported/tree/global/onnx/model.onnx`
- scope inventory: `models/exported/tree/global/reference_inventory.yaml`
- dataset provenance: `models/exported/tree/global/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/tree/global/source_runs/2026-03-20-15-17-30__te_hist_gbr_tabular`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
