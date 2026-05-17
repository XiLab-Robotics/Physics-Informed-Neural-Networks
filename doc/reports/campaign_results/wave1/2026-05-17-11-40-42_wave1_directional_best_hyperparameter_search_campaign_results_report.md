# Wave 1 Directional Best Hyperparameter Search Campaign Results

## Overview

- Campaign Name: `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11`
- Artifact Commit: `5cf40ebe2f3625f6e202237d4ed06265f5b9659c`
- Closeout Timestamp: `2026-05-17T11:55:57`
- Bounded Grid Surfaces: `6`
- Optuna Surfaces: `9`
- Total Surfaces: `15`
- Best Hyperparameters Available: `True`
- Native Python Artifacts Verified: `True`
- ONNX Exports Verified: `True`

The closeout combines the `6` bounded-grid `tree` and
`harmonic_regression` surfaces with the `9` persisted `Optuna` neural
surfaces.

## Search Completion

| Phase | Surface Count | Completion Evidence |
| --- | ---: | --- |
| `bounded_grid` | `6` | `campaign_leaderboard.yaml` and family registries |
| `optuna` | `9` | `best_trial.yaml`, `study_summary.yaml`, and trial result snapshots |

## Best Hyperparameters

| Family | Scope | Engine | Best Run | Best Hyperparameters | Canonical Family Best? |
| --- | --- | --- | --- | --- | --- |
| `tree` | `global` | `bounded_grid` | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `model.max_depth=10; model.learning_rate=0.08; model.min_samples_leaf=10; dataset.point_stride=5` | `True` |
| `tree_fw` | `forward` | `bounded_grid` | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `model.max_depth=6; model.learning_rate=0.08; model.min_samples_leaf=10; dataset.point_stride=5` | `True` |
| `tree_bw` | `backward` | `bounded_grid` | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `model.max_depth=6; model.learning_rate=0.08; model.min_samples_leaf=10; dataset.point_stride=5` | `True` |
| `harmonic_regression` | `global` | `bounded_grid` | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5` | `model.harmonic_order=12; training.learning_rate=0.0005; dataset.point_stride=5` | `True` |
| `harmonic_regression_fw` | `forward` | `bounded_grid` | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride5` | `model.harmonic_order=8; training.learning_rate=0.0005; dataset.point_stride=5` | `True` |
| `harmonic_regression_bw` | `backward` | `bounded_grid` | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5` | `model.harmonic_order=8; training.learning_rate=0.002; dataset.point_stride=5` | `True` |
| `feedforward` | `global` | `optuna` | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0001` | `training.learning_rate=0.0004891706203866443; training.weight_decay=3.0955664602423687e-06; dataset.curve_batch_size=8; model.dropout_probability=0.1; model.hidden_size=[256, 128, 64]` | `False` |
| `feedforward_fw` | `forward` | `optuna` | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0005` | `training.learning_rate=0.00031782605138591587; training.weight_decay=1.0379733829293252e-06; dataset.curve_batch_size=8; model.dropout_probability=0.0; model.hidden_size=[256, 128, 64]` | `False` |
| `feedforward_bw` | `backward` | `optuna` | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0000` | `training.learning_rate=0.0007106591851092234; training.weight_decay=0.00036808608148776104; dataset.curve_batch_size=2; model.dropout_probability=0.1; model.hidden_size=[256, 256, 256, 128]` | `False` |
| `periodic_mlp` | `global` | `optuna` | `te_periodic_mlp_h04_standard_global_optuna_t0006` | `training.learning_rate=0.0003109682534027558; training.weight_decay=3.5208625912830525e-06; dataset.curve_batch_size=4; model.dropout_probability=0.0; model.hidden_size=[128, 128, 64]; model.harmonic_order=6` | `False` |
| `periodic_mlp_fw` | `forward` | `optuna` | `te_periodic_mlp_h04_standard_Fw_optuna_t0001` | `training.learning_rate=0.0006044543365247595; training.weight_decay=2.607965659809584e-05; dataset.curve_batch_size=8; model.dropout_probability=0.15; model.hidden_size=[128, 128, 64]; model.harmonic_order=6` | `False` |
| `periodic_mlp_bw` | `backward` | `optuna` | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `training.learning_rate=0.0003109682534027558; training.weight_decay=3.5208625912830525e-06; dataset.curve_batch_size=4; model.dropout_probability=0.0; model.hidden_size=[128, 128, 64]; model.harmonic_order=6` | `True` |
| `residual_harmonic_mlp` | `global` | `optuna` | `te_residual_h12_deep_joint_wave1_global_optuna_t0011` | `training.learning_rate=0.00043116294467215643; training.weight_decay=0.00011347122039083106; dataset.curve_batch_size=4; model.residual_dropout_probability=0.0; model.residual_hidden_size=[128, 128, 64]; model.harmonic_order=8` | `False` |
| `residual_harmonic_mlp_fw` | `forward` | `optuna` | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0011` | `training.learning_rate=0.0006427381768091817; training.weight_decay=1.0093958069558592e-05; dataset.curve_batch_size=8; model.residual_dropout_probability=0.0; model.residual_hidden_size=[192, 128, 64]; model.harmonic_order=12` | `False` |
| `residual_harmonic_mlp_bw` | `backward` | `optuna` | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0005` | `training.learning_rate=0.002643977767420395; training.weight_decay=0.0003294325864613329; dataset.curve_batch_size=2; model.residual_dropout_probability=0.1; model.residual_hidden_size=[192, 128, 64]; model.harmonic_order=8` | `False` |

## HPO Winner Ranking

| Rank | Family | Scope | Engine | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `1` | `tree_fw` | `forward` | `bounded_grid` | 0.002677 | 0.002743 | 0.003409 |
| `2` | `tree` | `global` | `bounded_grid` | 0.002655 | 0.002782 | 0.003520 |
| `3` | `tree_bw` | `backward` | `bounded_grid` | 0.002681 | 0.002954 | 0.003749 |
| `4` | `harmonic_regression_fw` | `forward` | `bounded_grid` | 0.002848 | 0.003101 | 0.003527 |
| `5` | `periodic_mlp_bw` | `backward` | `optuna` | 0.002907 | 0.003233 | 0.003792 |
| `6` | `periodic_mlp` | `global` | `optuna` | 0.002964 | 0.003233 | 0.003733 |
| `7` | `feedforward_bw` | `backward` | `optuna` | 0.002875 | 0.003276 | 0.003767 |
| `8` | `feedforward_fw` | `forward` | `optuna` | 0.002746 | 0.003287 | 0.003911 |
| `9` | `periodic_mlp_fw` | `forward` | `optuna` | 0.002751 | 0.003294 | 0.003899 |
| `10` | `residual_harmonic_mlp_fw` | `forward` | `optuna` | 0.002759 | 0.003354 | 0.003995 |
| `11` | `residual_harmonic_mlp` | `global` | `optuna` | 0.002868 | 0.003428 | 0.003928 |
| `12` | `feedforward` | `global` | `optuna` | 0.002958 | 0.003446 | 0.004158 |
| `13` | `residual_harmonic_mlp_bw` | `backward` | `optuna` | 0.002930 | 0.003454 | 0.003918 |
| `14` | `harmonic_regression_bw` | `backward` | `bounded_grid` | 0.003638 | 0.003494 | 0.004081 |
| `15` | `harmonic_regression` | `global` | `bounded_grid` | 0.017025 | 0.020774 | 0.022412 |

## Artifact Verification

| Family | Scope | Native Format | Native Status | ONNX Status | ONNX Size [B] |
| --- | --- | --- | --- | --- | ---: |
| `tree` | `global` | `.pkl` | `ok` | `ok` | 313782 |
| `tree_fw` | `forward` | `.pkl` | `ok` | `ok` | 290566 |
| `tree_bw` | `backward` | `.pkl` | `ok` | `ok` | 290566 |
| `harmonic_regression` | `global` | `.ckpt` | `ok` | `ok` | 6647 |
| `harmonic_regression_fw` | `forward` | `.ckpt` | `ok` | `ok` | 5334 |
| `harmonic_regression_bw` | `backward` | `.ckpt` | `ok` | `ok` | 5334 |
| `feedforward` | `global` | `.ckpt` | `ok` | `ok` | 184441 |
| `feedforward_fw` | `forward` | `.ckpt` | `ok` | `ok` | 184410 |
| `feedforward_bw` | `backward` | `.ckpt` | `ok` | `ok` | 684512 |
| `periodic_mlp` | `global` | `.ckpt` | `ok` | `ok` | 122741 |
| `periodic_mlp_fw` | `forward` | `.ckpt` | `ok` | `ok` | 122772 |
| `periodic_mlp_bw` | `backward` | `.ckpt` | `ok` | `ok` | 122741 |
| `residual_harmonic_mlp` | `global` | `.ckpt` | `ok` | `ok` | 118553 |
| `residual_harmonic_mlp_fw` | `forward` | `.ckpt` | `ok` | `ok` | 154521 |
| `residual_harmonic_mlp_bw` | `backward` | `.ckpt` | `ok` | `ok` | 153400 |

## Export Archive

- Export Root: `models\exported`
- Export Inventory: `models\exported\wave1_directional_hpo_export_inventory.yaml`
- `tree` surfaces use `.pkl` Python artifacts.
- `harmonic_regression` and neural surfaces use `.ckpt` Python artifacts.
- Every surface has a refreshed `onnx/model.onnx` export in `models/exported/`.

## Registry Note

HPO winners and canonical family-best winners are related but not always
identical. The canonical registries use the repository selection policy
based on held-out test metrics, while `Optuna` selects the best trial by
`val_mae`. This closeout records the HPO winners and explicitly flags
whether each one is also the current canonical family-best entry.
