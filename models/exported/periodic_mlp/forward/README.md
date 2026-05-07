# periodic_mlp Forward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `periodic_mlp`
- Family Key: `periodic_mlp_fw`
- Scope: `forward`
- Training Variant: `Fw`
- Run Name: `te_periodic_mlp_h04_standard_Fw`
- Run Instance Id: `2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw`
- Model Type: `periodic_mlp`
- Validation MAE: `0.002848 deg`
- Test MAE: `0.003432 deg`
- Test RMSE: `0.004023 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/periodic_mlp/forward/python/periodic_mlp-epoch=022-val_mae=0.00284801.ckpt`
- `onnx/` winner artifact: `models/exported/periodic_mlp/forward/onnx/model.onnx`
- scope inventory: `models/exported/periodic_mlp/forward/reference_inventory.yaml`
- dataset provenance: `models/exported/periodic_mlp/forward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/periodic_mlp/forward/source_runs/2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
