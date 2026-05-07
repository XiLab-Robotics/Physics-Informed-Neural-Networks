# feedforward Backward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `feedforward`
- Family Key: `feedforward_bw`
- Scope: `backward`
- Training Variant: `Bw`
- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw`
- Run Instance Id: `2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw`
- Model Type: `feedforward`
- Validation MAE: `0.003049 deg`
- Test MAE: `0.003262 deg`
- Test RMSE: `0.003749 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/feedforward/backward/python/feedforward-epoch=093-val_mae=0.00304864.ckpt`
- `onnx/` winner artifact: `models/exported/feedforward/backward/onnx/model.onnx`
- scope inventory: `models/exported/feedforward/backward/reference_inventory.yaml`
- dataset provenance: `models/exported/feedforward/backward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/feedforward/backward/source_runs/2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
