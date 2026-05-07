# tree Forward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `tree`
- Family Key: `tree_fw`
- Scope: `forward`
- Training Variant: `Fw`
- Run Name: `te_hist_gbr_tabular_Fw`
- Run Instance Id: `2026-05-06-17-00-56__te_hist_gbr_tabular_fw`
- Model Type: `hist_gradient_boosting`
- Validation MAE: `0.002666 deg`
- Test MAE: `0.002845 deg`
- Test RMSE: `0.003476 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/tree/forward/python/tree_model.pkl`
- `onnx/` winner artifact: `models/exported/tree/forward/onnx/model.onnx`
- scope inventory: `models/exported/tree/forward/reference_inventory.yaml`
- dataset provenance: `models/exported/tree/forward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/tree/forward/source_runs/2026-05-06-17-00-56__te_hist_gbr_tabular_fw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
