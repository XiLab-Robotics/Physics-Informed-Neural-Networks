# periodic_mlp Global Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `periodic_mlp`
- Family Key: `periodic_mlp`
- Scope: `global`
- Training Variant: `global`
- Run Name: `te_periodic_mlp_h04_standard`
- Run Instance Id: `2026-03-20-14-19-32__te_periodic_mlp_h04_standard`
- Model Type: `periodic_mlp`
- Validation MAE: `0.003097 deg`
- Test MAE: `0.003317 deg`
- Test RMSE: `0.003793 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/periodic_mlp/global/python/periodic_mlp-epoch=031-val_mae=0.00309735.ckpt`
- `onnx/` winner artifact: `models/exported/periodic_mlp/global/onnx/model.onnx`
- scope inventory: `models/exported/periodic_mlp/global/reference_inventory.yaml`
- dataset provenance: `models/exported/periodic_mlp/global/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/periodic_mlp/global/source_runs/2026-03-20-14-19-32__te_periodic_mlp_h04_standard`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
