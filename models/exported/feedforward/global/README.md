# feedforward Global Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `feedforward`
- Family Key: `feedforward`
- Scope: `global`
- Training Variant: `global`
- Run Name: `te_feedforward_stride1_high_compute_long_remote_global`
- Run Instance Id: `2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global`
- Model Type: `feedforward`
- Validation MAE: `0.003056 deg`
- Test MAE: `0.003150 deg`
- Test RMSE: `0.003603 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/feedforward/global/python/feedforward-epoch=180-val_mae=0.00305586.ckpt`
- `onnx/` winner artifact: `models/exported/feedforward/global/onnx/model.onnx`
- scope inventory: `models/exported/feedforward/global/reference_inventory.yaml`
- dataset provenance: `models/exported/feedforward/global/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/feedforward/global/source_runs/2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
