# residual_harmonic_mlp Global Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `residual_harmonic_mlp`
- Family Key: `residual_harmonic_mlp`
- Scope: `global`
- Training Variant: `global`
- Run Name: `te_residual_h12_deep_joint_wave1`
- Run Instance Id: `2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1`
- Model Type: `residual_harmonic_mlp`
- Validation MAE: `0.003024 deg`
- Test MAE: `0.003152 deg`
- Test RMSE: `0.003640 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/residual_harmonic_mlp/global/python/residual_harmonic_mlp-epoch=077-val_mae=0.00302384.ckpt`
- `onnx/` winner artifact: `models/exported/residual_harmonic_mlp/global/onnx/model.onnx`
- scope inventory: `models/exported/residual_harmonic_mlp/global/reference_inventory.yaml`
- dataset provenance: `models/exported/residual_harmonic_mlp/global/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/residual_harmonic_mlp/global/source_runs/2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
