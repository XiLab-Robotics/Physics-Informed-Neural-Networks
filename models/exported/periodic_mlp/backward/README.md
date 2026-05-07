# periodic_mlp Backward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `periodic_mlp`
- Family Key: `periodic_mlp_bw`
- Scope: `backward`
- Training Variant: `Bw`
- Run Name: `te_periodic_mlp_h04_standard_Bw`
- Run Instance Id: `2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw`
- Model Type: `periodic_mlp`
- Validation MAE: `0.003154 deg`
- Test MAE: `0.003525 deg`
- Test RMSE: `0.004132 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/periodic_mlp/backward/python/periodic_mlp-epoch=049-val_mae=0.00315372.ckpt`
- `onnx/` winner artifact: `models/exported/periodic_mlp/backward/onnx/model.onnx`
- scope inventory: `models/exported/periodic_mlp/backward/reference_inventory.yaml`
- dataset provenance: `models/exported/periodic_mlp/backward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/periodic_mlp/backward/source_runs/2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
