# residual_harmonic_mlp Backward Export Archive

This folder stores the curated winner selected for one `Wave 1` family
and one directional training scope.

## Winner Summary

- Base Family: `residual_harmonic_mlp`
- Family Key: `residual_harmonic_mlp_bw`
- Scope: `backward`
- Training Variant: `Bw`
- Run Name: `te_residual_h12_deep_joint_wave1_Bw`
- Run Instance Id: `2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw`
- Model Type: `residual_harmonic_mlp`
- Validation MAE: `0.003110 deg`
- Test MAE: `0.003493 deg`
- Test RMSE: `0.004108 deg`

## Archive Contents

- `python/` winner artifact: `models/exported/residual_harmonic_mlp/backward/python/residual_harmonic_mlp-epoch=037-val_mae=0.00310962.ckpt`
- `onnx/` winner artifact: `models/exported/residual_harmonic_mlp/backward/onnx/model.onnx`
- scope inventory: `models/exported/residual_harmonic_mlp/backward/reference_inventory.yaml`
- dataset provenance: `models/exported/residual_harmonic_mlp/backward/dataset_snapshot_manifest.yaml`
- source-run snapshots: `models/exported/residual_harmonic_mlp/backward/source_runs/2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw`

The Python artifact keeps the model family's canonical reusable format:

- tree families remain `.pkl` estimators;
- PyTorch families remain `.ckpt` checkpoints;
- all families also expose an ONNX export for deployment-facing use.
