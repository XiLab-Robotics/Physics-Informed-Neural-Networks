# Dataset Input-Mode Retraining Campaign Plan

## Campaign Status

Planning only. No implementation, Slurm execution, smoke run, or training has
started.

## Objective

Retrain every active model family for three input-mode versions and three
surfaces, then export matching ONNX and Python artifacts to deterministic
`models/` locations.

The three input-mode versions are:

- `simplified_setpoints`;
- `polished_setpoints`;
- `polished_actual_values`.

The three surfaces are:

- `forward`;
- `backward`;
- `global`.

## Current Dataset Finding

The existing polished training configs and loader use actual values. The
current `polished_point_v1` model input list is `theta`, `theta_dot`,
`tau_load`, `T`, `direction_flag`; filename setpoints are not model inputs for
those polished actual-values runs. The previous `simplified_dataset` contract
uses path/filename setpoints for speed, torque, and temperature.

## Planned Campaign Matrix

The matrix contains `37` family groups, including `rcim_track1` and the `36`
model-development families from the completed full-wave polished campaign.
Each family group has `3` input-mode versions and `3` surfaces.

Total planned family-version campaigns: `111`.
Total planned surface runs: `333`.

### RCIM Model-Bank Reproduction

- `rcim_track1` x `simplified_setpoints` x `forward/backward/global`
- `rcim_track1` x `polished_setpoints` x `forward/backward/global`
- `rcim_track1` x `polished_actual_values` x `forward/backward/global`

The RCIM package must also preserve its internal model bank naming for SVR,
MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, and LGBM where supported.

### Wave 1 And Early Model-Development Families

- `tree` x all three input modes x `forward/backward/global`
- `residual_harmonic_mlp` x all three input modes x `forward/backward/global`
- `feedforward` x all three input modes x `forward/backward/global`
- `periodic_mlp` x all three input modes x `forward/backward/global`
- `harmonic_regression` x all three input modes x `forward/backward/global`
- `periodic_mlp_harmonic` x all three input modes x `forward/backward/global`

### Wave 2 Temporal Families

- `temporal_convolution` x all three input modes x `forward/backward/global`
- `gru_sequence` x all three input modes x `forward/backward/global`
- `lstm_sequence` x all three input modes x `forward/backward/global`
- `periodic_temporal_convolution` x all three input modes x
  `forward/backward/global`
- `periodic_gru_sequence` x all three input modes x `forward/backward/global`
- `periodic_lstm_sequence` x all three input modes x `forward/backward/global`
- `residual_harmonic_gru_sequence_sparse_rcim` x all three input modes x
  `forward/backward/global`
- `residual_harmonic_gru_sequence_dense240` x all three input modes x
  `forward/backward/global`
- `residual_harmonic_gru_sequence_dense360` x all three input modes x
  `forward/backward/global`
- `residual_harmonic_lstm_sequence_sparse_rcim` x all three input modes x
  `forward/backward/global`
- `residual_harmonic_lstm_sequence_dense240` x all three input modes x
  `forward/backward/global`
- `residual_harmonic_lstm_sequence_dense360` x all three input modes x
  `forward/backward/global`

### Wave 3 Offset And Curve-Aware Families

- `wave3_1_sequential_residual_offset_probe` x all three input modes x
  `forward/backward/global`
- `wave3_2_clean_sequential_residual_offset` x all three input modes x
  `forward/backward/global`
- `wave3_2_harmonic_residual_offset` x all three input modes x
  `forward/backward/global`
- `wave3_3_curve_aware_pointwise_control` x all three input modes x
  `forward/backward/global`
- `wave3_3_raw_centered_shape_curve_aware` x all three input modes x
  `forward/backward/global`
- `wave3_3_raw_offset_curve_aware` x all three input modes x
  `forward/backward/global`
- `wave3_3_full_curve_composite` x all three input modes x
  `forward/backward/global`

### Wave 4 Robust, Probabilistic, Mixture, And Stateful Families

- `wave4_1_mae_robust_loss` x all three input modes x
  `forward/backward/global`
- `wave4_1_smooth_l1_robust_loss` x all three input modes x
  `forward/backward/global`
- `wave4_1_log_cosh_robust_loss` x all three input modes x
  `forward/backward/global`
- `wave4_2_quantile_p10_p50_p90` x all three input modes x
  `forward/backward/global`
- `wave4_2_gaussian_nll` x all three input modes x
  `forward/backward/global`
- `wave4_3_mixture_density_k2` x all three input modes x
  `forward/backward/global`
- `wave4_3_mixture_density_k3` x all three input modes x
  `forward/backward/global`
- `wave4_4_gru_latent_offset_residual` x all three input modes x
  `forward/backward/global`
- `wave4_4_causal_tcn_latent_offset_residual` x all three input modes x
  `forward/backward/global`

### Wave 5.1 Harmonic-Prior Families

- `wave5_1_harmonic_prior_pointwise_control` x all three input modes x
  `forward/backward/global`
- `wave5_1_harmonic_prior_smooth_l1_structured` x all three input modes x
  `forward/backward/global`

## Artifact Placement Contract

Each accepted training run must export to exactly one dataset/input-mode root:

- `models/simplified_dataset/setpoints/exported/<family>/<surface>/<run_instance_id>/`
- `models/polished_dataset/setpoints/exported/<family>/<surface>/<run_instance_id>/`
- `models/polished_dataset/actual_values/exported/<family>/<surface>/<run_instance_id>/`

Every export directory must include:

- `onnx/model.onnx` when the model family supports ONNX export;
- the Python artifact under `python/`;
- `reference_inventory.yaml`;
- source-run metadata snapshots;
- dataset and input-mode audit fields.

## Aries Execution Plan

The first execution must be a fast GPU smoke run through `srun`, using a small
single-family package and reduced training settings. The intended GPU request
follows the local Aries guide:

```bash
srun \
  --nodes=1 \
  --ntasks=1 \
  --cpus-per-task=4 \
  --time=00:20:00 \
  --mem=20g \
  --partition=ice4hpc \
  --account=xilab \
  --qos=gpus \
  --gpus=1g.20gb:1 \
  --mpi=pmix \
  ./scripts/campaigns/aries/run_dataset_input_mode_retraining_smoke.sh
```

Only after the `srun` smoke succeeds should the first real one-family campaign
be submitted with `sbatch`.

## Safety Checks

- Fail if `dataset_name`, `input_mode`, `dataset_schema`, and destination
  model root do not agree.
- Fail if `polished_setpoints` reads `theta_dot`, `tau_load`, or `T` as input
  features.
- Fail if `polished_actual_values` replaces row-level values with filename
  setpoints.
- Fail if `simplified_dataset` is paired with `actual_values`.
- Fail if `forward`, `backward`, or `global` outputs are written to the wrong
  surface folder.
- Record the resolved CSV root and a sample source path in every run metadata
  file and export inventory.
- Keep `TE Curve Verification Pipeline` refresh out of normal training
  closeout until all retraining artifacts are accepted.
