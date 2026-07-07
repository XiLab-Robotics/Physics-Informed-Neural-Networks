# Dataset Input-Mode Retraining Campaigns

## Overview

The retraining program must produce three unambiguous model artifact branches:

- `simplified_dataset` with filename/path setpoints;
- `polished_dataset` with filename/path setpoints;
- `polished_dataset` with row-level actual values.

The existing polished training contract has already used row-level actual
values. The current loader resolves `polished_point_v1` inputs as
`theta`, `theta_dot`, `tau_load`, and `T`, while `simplified_curve_v1` uses
filename/path setpoints for speed, torque, and temperature plus
`direction_flag`.

No implementation or training may start until this technical document and the
matching campaign planning report are explicitly approved.

No subagent is planned. If a subagent becomes useful later, its name, task
boundary, and approval requirement must be recorded before requesting
approval.

## Technical Approach

Create explicit input-mode contracts instead of relying on dataset names alone.

- `simplified_setpoints`: read `data/simplified_dataset`; parse nominal speed,
  torque, and temperature from path and filename; keep `direction_flag`.
- `polished_setpoints`: read `data/polished_dataset`; parse nominal speed,
  torque, and temperature from path and filename; keep `direction_flag`; use
  polished row-level `theta` and `theta_TE`.
- `polished_actual_values`: read `data/polished_dataset`; use row-level
  `theta`, `theta_dot`, `tau_load`, and `T`; preserve the existing
  actual-value behavior.

Every generated queue item, run name, output folder, exported archive, and
validation manifest must carry all of these fields:

- `dataset_name`;
- `input_mode`;
- `dataset_schema`;
- `source_dataset_root`;
- `expected_model_archive_root`;
- `surface`, with values `forward`, `backward`, or `global`.

Aries execution will use a first GPU `srun` smoke run before any `sbatch`
campaign. The local Aries guide and public wiki agree that GPU jobs use the
`ice4hpc` partition with `--account=xilab`, `--qos=gpus`, and a GPU request.
The local guide recommends starting with `--gpus=1g.20gb:1`; the public wiki
shows the generic GPU pattern with `--gpus=1`.

## Detailed Campaign Inventory

Each campaign below is a family-version campaign. Every campaign must prepare
and execute exactly three surface runs: `forward`, `backward`, and `global`.

The campaign ID pattern is:

```text
dataset_input_mode_retraining__<family>__<input_mode>
```

The three input modes are:

- `simplified_setpoints`;
- `polished_setpoints`;
- `polished_actual_values`.

The complete campaign inventory is:

1. `rcim_track1`
   - `dataset_input_mode_retraining__rcim_track1__simplified_setpoints`
   - `dataset_input_mode_retraining__rcim_track1__polished_setpoints`
   - `dataset_input_mode_retraining__rcim_track1__polished_actual_values`
2. `tree`
   - `dataset_input_mode_retraining__tree__simplified_setpoints`
   - `dataset_input_mode_retraining__tree__polished_setpoints`
   - `dataset_input_mode_retraining__tree__polished_actual_values`
3. `residual_harmonic_mlp`
   - `dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints`
   - `dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints`
   - `dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values`
4. `feedforward`
   - `dataset_input_mode_retraining__feedforward__simplified_setpoints`
   - `dataset_input_mode_retraining__feedforward__polished_setpoints`
   - `dataset_input_mode_retraining__feedforward__polished_actual_values`
5. `periodic_mlp`
   - `dataset_input_mode_retraining__periodic_mlp__simplified_setpoints`
   - `dataset_input_mode_retraining__periodic_mlp__polished_setpoints`
   - `dataset_input_mode_retraining__periodic_mlp__polished_actual_values`
6. `harmonic_regression`
   - `dataset_input_mode_retraining__harmonic_regression__simplified_setpoints`
   - `dataset_input_mode_retraining__harmonic_regression__polished_setpoints`
   - `dataset_input_mode_retraining__harmonic_regression__polished_actual_values`
7. `periodic_mlp_harmonic`
   - `dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints`
   - `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints`
   - `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values`
8. `temporal_convolution`
   - `dataset_input_mode_retraining__temporal_convolution__simplified_setpoints`
   - `dataset_input_mode_retraining__temporal_convolution__polished_setpoints`
   - `dataset_input_mode_retraining__temporal_convolution__polished_actual_values`
9. `gru_sequence`
   - `dataset_input_mode_retraining__gru_sequence__simplified_setpoints`
   - `dataset_input_mode_retraining__gru_sequence__polished_setpoints`
   - `dataset_input_mode_retraining__gru_sequence__polished_actual_values`
10. `lstm_sequence`
    - `dataset_input_mode_retraining__lstm_sequence__simplified_setpoints`
    - `dataset_input_mode_retraining__lstm_sequence__polished_setpoints`
    - `dataset_input_mode_retraining__lstm_sequence__polished_actual_values`
11. `periodic_temporal_convolution`
    - `dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints`
    - `dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints`
    - `dataset_input_mode_retraining__periodic_temporal_convolution__polished_actual_values`
12. `periodic_gru_sequence`
    - `dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints`
    - `dataset_input_mode_retraining__periodic_gru_sequence__polished_setpoints`
    - `dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values`
13. `periodic_lstm_sequence`
    - `dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints`
    - `dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints`
    - `dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values`
14. `residual_harmonic_gru_sequence_sparse_rcim`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values`
15. `residual_harmonic_gru_sequence_dense240`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__simplified_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_actual_values`
16. `residual_harmonic_gru_sequence_dense360`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values`
17. `residual_harmonic_lstm_sequence_sparse_rcim`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values`
18. `residual_harmonic_lstm_sequence_dense240`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_actual_values`
19. `residual_harmonic_lstm_sequence_dense360`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints`
    - `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values`
20. `wave3_1_sequential_residual_offset_probe`
    - `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints`
    - `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_setpoints`
    - `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values`
21. `wave3_2_clean_sequential_residual_offset`
    - `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__simplified_setpoints`
    - `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints`
    - `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values`
22. `wave3_2_harmonic_residual_offset`
    - `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints`
    - `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints`
    - `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values`
23. `wave3_3_curve_aware_pointwise_control`
    - `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints`
    - `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_setpoints`
    - `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values`
24. `wave3_3_raw_centered_shape_curve_aware`
    - `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints`
    - `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints`
    - `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values`
25. `wave3_3_raw_offset_curve_aware`
    - `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints`
    - `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_setpoints`
    - `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_actual_values`
26. `wave3_3_full_curve_composite`
    - `dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints`
    - `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints`
    - `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values`
27. `wave4_1_mae_robust_loss`
    - `dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_actual_values`
28. `wave4_1_smooth_l1_robust_loss`
    - `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values`
29. `wave4_1_log_cosh_robust_loss`
    - `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values`
30. `wave4_2_quantile_p10_p50_p90`
    - `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values`
31. `wave4_2_gaussian_nll`
    - `dataset_input_mode_retraining__wave4_2_gaussian_nll__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values`
32. `wave4_3_mixture_density_k2`
    - `dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_actual_values`
33. `wave4_3_mixture_density_k3`
    - `dataset_input_mode_retraining__wave4_3_mixture_density_k3__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values`
34. `wave4_4_gru_latent_offset_residual`
    - `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values`
35. `wave4_4_causal_tcn_latent_offset_residual`
    - `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints`
    - `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_setpoints`
    - `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values`
36. `wave5_1_harmonic_prior_pointwise_control`
    - `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__simplified_setpoints`
    - `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints`
    - `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values`
37. `wave5_1_harmonic_prior_smooth_l1_structured`
    - `dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints`
    - `dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_setpoints`
    - `dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values`

This inventory defines `111` family-version campaigns. Since every campaign
contains three surface runs, the full retraining program contains `333`
surface runs before any optional `TE Curve Verification Pipeline` refresh.

## Involved Components

- `scripts/datasets/transmission_error_dataset.py`
- `config/datasets/transmission_error_dataset.yaml`
- `config/training/polished_dataset_retraining/`
- `config/training/queue/`
- `scripts/campaigns/cross_wave/`
- new Aries Linux Slurm launchers under `scripts/campaigns/aries/`
- campaign notes under `doc/scripts/campaigns/aries/`
- campaign plans under `doc/reports/campaign_plans/cross_wave/input_modes/`
- training outputs under `output/training_campaigns/`
- run outputs under `output/training_runs/`
- model archives under:
  - `models/simplified_dataset/setpoints/exported/`
  - `models/polished_dataset/setpoints/exported/`
  - `models/polished_dataset/actual_values/exported/`

The existing `models/polished_dataset/exported/` and
`models/simplified_dataset/exported/` roots must be treated as compatibility
surfaces until a deliberate migration or alias policy is approved.

## Implementation Steps

1. Add an input-mode selector and schema metadata so polished setpoint rows can
   be built from polished CSV paths without using row-varying
   `theta_dot`, `tau_load`, or `T`.
2. Add hard assertions that reject impossible combinations, including
   `simplified_dataset` with `actual_values`.
3. Generate one preliminary fast Aries smoke campaign for a single small
   model-family/surface pair and delete or quarantine the smoke artifacts after
   verification.
4. Generate full campaign packages one family-version at a time. Each package
   contains the three surfaces `forward`, `backward`, and `global`.
5. Add a Linux Slurm batch script for Aries and keep `srun` smoke execution
   separate from later `sbatch` execution.
6. Add artifact export checks that fail unless the source run metadata and the
   destination `models/` subfolder agree on dataset, input mode, and surface.
7. Run package validators, Python syntax checks, and Markdown QA on touched
   scopes before requesting execution approval.
8. After approved campaign completion, close out each campaign with
   leaderboard artifacts, exported ONNX and Python artifacts, registries, and
   campaign-results reports.
9. Only after normal closeout, prepare the separate `TE Curve Verification
   Pipeline` refresh requested for the final reports.
