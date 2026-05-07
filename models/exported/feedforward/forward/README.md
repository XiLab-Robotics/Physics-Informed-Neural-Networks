# feedforward Forward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `feedforward`
- Family Key: `feedforward_fw`
- Scope: `forward`
- Training Variant: `Fw`
- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw`
- Run Instance Id: `2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw`
- Model Type: `feedforward`
- Validation MAE: `0.002915 deg`
- Test MAE: `0.003563 deg`
- Test RMSE: `0.004009 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/feedforward/forward/python/feedforward-epoch=033-val_mae=0.00291539.ckpt`
- `onnx/` winner artifact: `models/exported/feedforward/forward/onnx/model.onnx`
- scope inventory: `models/exported/feedforward/forward/reference_inventory.yaml`
- dataset provenance: `models/exported/feedforward/forward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/feedforward/forward/source_runs/2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
