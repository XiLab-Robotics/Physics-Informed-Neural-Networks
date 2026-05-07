# residual_harmonic_mlp Forward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `residual_harmonic_mlp`
- Family Key: `residual_harmonic_mlp_fw`
- Scope: `forward`
- Training Variant: `Fw`
- Run Name: `te_residual_h12_deep_joint_wave1_Fw`
- Run Instance Id: `2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw`
- Model Type: `residual_harmonic_mlp`
- Validation MAE: `0.002852 deg`
- Test MAE: `0.003530 deg`
- Test RMSE: `0.004145 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/residual_harmonic_mlp/forward/python/residual_harmonic_mlp-epoch=018-val_mae=0.00285191.ckpt`
- `onnx/` winner artifact: `models/exported/residual_harmonic_mlp/forward/onnx/model.onnx`
- scope inventory: `models/exported/residual_harmonic_mlp/forward/reference_inventory.yaml`
- dataset provenance: `models/exported/residual_harmonic_mlp/forward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/residual_harmonic_mlp/forward/source_runs/2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
