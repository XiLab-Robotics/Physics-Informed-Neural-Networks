# harmonic_regression Forward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `harmonic_regression`
- Family Key: `harmonic_regression_fw`
- Scope: `forward`
- Training Variant: `Fw`
- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw`
- Run Instance Id: `2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw`
- Model Type: `harmonic_regression`
- Validation MAE: `0.002811 deg`
- Test MAE: `0.003129 deg`
- Test RMSE: `0.003567 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/harmonic_regression/forward/python/harmonic_regression-epoch=068-val_mae=0.00281060.ckpt`
- `onnx/` winner artifact: `models/exported/harmonic_regression/forward/onnx/model.onnx`
- scope inventory: `models/exported/harmonic_regression/forward/reference_inventory.yaml`
- dataset provenance: `models/exported/harmonic_regression/forward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/harmonic_regression/forward/source_runs/2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
