# harmonic_regression Backward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `harmonic_regression`
- Family Key: `harmonic_regression_bw`
- Scope: `backward`
- Training Variant: `Bw`
- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw`
- Run Instance Id: `2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw`
- Model Type: `harmonic_regression`
- Validation MAE: `0.003701 deg`
- Test MAE: `0.003524 deg`
- Test RMSE: `0.004080 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/harmonic_regression/backward/python/harmonic_regression-epoch=019-val_mae=0.00370070.ckpt`
- `onnx/` winner artifact: `models/exported/harmonic_regression/backward/onnx/model.onnx`
- scope inventory: `models/exported/harmonic_regression/backward/reference_inventory.yaml`
- dataset provenance: `models/exported/harmonic_regression/backward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/harmonic_regression/backward/source_runs/2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
