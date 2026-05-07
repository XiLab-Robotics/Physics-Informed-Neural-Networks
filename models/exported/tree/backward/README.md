# tree Backward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `tree`
- Family Key: `tree_bw`
- Scope: `backward`
- Training Variant: `Bw`
- Run Name: `te_hist_gbr_tabular_Bw`
- Run Instance Id: `2026-05-06-17-02-06__te_hist_gbr_tabular_bw`
- Model Type: `hist_gradient_boosting`
- Validation MAE: `0.002698 deg`
- Test MAE: `0.003087 deg`
- Test RMSE: `0.003850 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/tree/backward/python/tree_model.pkl`
- `onnx/` winner artifact: `models/exported/tree/backward/onnx/model.onnx`
- scope inventory: `models/exported/tree/backward/reference_inventory.yaml`
- dataset provenance: `models/exported/tree/backward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/tree/backward/source_runs/2026-05-06-17-02-06__te_hist_gbr_tabular_bw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
