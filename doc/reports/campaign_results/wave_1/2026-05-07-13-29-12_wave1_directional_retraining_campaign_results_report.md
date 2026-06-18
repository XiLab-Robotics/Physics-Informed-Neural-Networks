# Wave 1 Directional Retraining Campaign Results

## Overview

- Campaign Name: `wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- Closeout Timestamp: `2026-05-07-13-48-50`
- Campaign Output Directory: `output/training_campaigns/wave1/directional_retraining/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- Completed Runs: `15`
- Failed Runs: `0`
- All `15` planned Wave 1 runs are now closed across `global`, `forward`, and `backward` variants.
- The protected `doc/running/active_training_campaign.yaml` file was intentionally left untouched because it still tracks a separate `Track 1` campaign.

## Closeout Actions

- Repaired directional metadata in `0` tree metrics snapshots so registry-facing artifacts now preserve `base_model_family`, `training_variant`, and direction flags consistently.
- Rebuilt the affected family registries, the campaign leaderboard, the campaign best-run snapshots, and the program best registry from the repaired metrics.
- Archived one ONNX export plus one Python artifact for every `Wave 1` family/scope winner under `models/exported/`, together with scope-local inventories, dataset provenance, and source-run snapshots.
- Refreshed the canonical `Wave 1` closeout report and regenerated the training-results master summary from the updated registries.

## Campaign Ranking

| Rank | Family | Scope | Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| `1` | `tree` | `forward` | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002666 | 0.002845 | 0.003476 |
| `2` | `tree` | `global` | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.002719 | 0.002885 | 0.003607 |
| `3` | `tree` | `backward` | `te_hist_gbr_tabular_Bw` | `hist_gradient_boosting` | 0.002698 | 0.003087 | 0.003850 |
| `4` | `harmonic_regression` | `forward` | `te_harmonic_order12_linear_conditioned_recovery_Fw` | `harmonic_regression` | 0.002811 | 0.003129 | 0.003567 |
| `5` | `feedforward` | `global` | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003056 | 0.003150 | 0.003603 |
| `6` | `feedforward` | `backward` | `te_feedforward_stride1_high_compute_long_remote_Bw` | `feedforward` | 0.003049 | 0.003262 | 0.003749 |
| `7` | `periodic_mlp` | `global` | `te_periodic_mlp_h04_standard_global` | `periodic_mlp` | 0.002985 | 0.003349 | 0.003916 |
| `8` | `residual_harmonic_mlp` | `global` | `te_residual_h12_deep_joint_wave1_global` | `residual_harmonic_mlp` | 0.003115 | 0.003420 | 0.003931 |
| `9` | `periodic_mlp` | `forward` | `te_periodic_mlp_h04_standard_Fw` | `periodic_mlp` | 0.002848 | 0.003432 | 0.004023 |
| `10` | `residual_harmonic_mlp` | `backward` | `te_residual_h12_deep_joint_wave1_Bw` | `residual_harmonic_mlp` | 0.003110 | 0.003493 | 0.004108 |
| `11` | `harmonic_regression` | `backward` | `te_harmonic_order12_linear_conditioned_recovery_Bw` | `harmonic_regression` | 0.003701 | 0.003524 | 0.004080 |
| `12` | `periodic_mlp` | `backward` | `te_periodic_mlp_h04_standard_Bw` | `periodic_mlp` | 0.003154 | 0.003525 | 0.004132 |
| `13` | `residual_harmonic_mlp` | `forward` | `te_residual_h12_deep_joint_wave1_Fw` | `residual_harmonic_mlp` | 0.002852 | 0.003530 | 0.004145 |
| `14` | `feedforward` | `forward` | `te_feedforward_stride1_high_compute_long_remote_Fw` | `feedforward` | 0.002915 | 0.003563 | 0.004009 |
| `15` | `harmonic_regression` | `global` | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.017017 | 0.020779 | 0.022403 |

## Family Directional Surface

- Current campaign-best entry: `te_hist_gbr_tabular_Fw` from family `tree_fw` with `test_mae = 0.002845 deg`.

| Family | Global Test MAE [deg] | Forward Test MAE [deg] | Backward Test MAE [deg] | Best Scope |
| --- | ---: | ---: | ---: | --- |
| `tree` | 0.002885 | 0.002845 | 0.003087 | `forward` |
| `residual_harmonic_mlp` | 0.003152 | 0.003530 | 0.003493 | `global` |
| `feedforward` | 0.003150 | 0.003563 | 0.003262 | `global` |
| `periodic_mlp` | 0.003317 | 0.003432 | 0.003525 | `global` |
| `harmonic_regression` | 0.020779 | 0.003129 | 0.003524 | `forward` |

## Exported Model Archive

- Export root: `models/exported`
- Root inventory: `models/exported/wave1_directional_retraining_export_inventory.yaml`
- Each family now exposes `global/`, `forward/`, and `backward/` subfolders, each containing `python/`, `onnx/`, `reference_inventory.yaml`, `dataset_snapshot_manifest.yaml`, and `source_runs/<run_instance_id>/` provenance snapshots.

| Family | Scope | Python Artifact | ONNX Artifact | Provenance Bundle |
| --- | --- | --- | --- | --- |
| `tree` | `global` | `models/exported/tree/global/python/tree_model.pkl` | `models/exported/tree/global/onnx/model.onnx` | `models/exported/tree/global/reference_inventory.yaml` |
| `tree` | `forward` | `models/exported/tree/forward/python/tree_model.pkl` | `models/exported/tree/forward/onnx/model.onnx` | `models/exported/tree/forward/reference_inventory.yaml` |
| `tree` | `backward` | `models/exported/tree/backward/python/tree_model.pkl` | `models/exported/tree/backward/onnx/model.onnx` | `models/exported/tree/backward/reference_inventory.yaml` |
| `residual_harmonic_mlp` | `global` | `models/exported/residual_harmonic_mlp/global/python/residual_harmonic_mlp-epoch=077-val_mae=0.00302384.ckpt` | `models/exported/residual_harmonic_mlp/global/onnx/model.onnx` | `models/exported/residual_harmonic_mlp/global/reference_inventory.yaml` |
| `residual_harmonic_mlp` | `forward` | `models/exported/residual_harmonic_mlp/forward/python/residual_harmonic_mlp-epoch=018-val_mae=0.00285191.ckpt` | `models/exported/residual_harmonic_mlp/forward/onnx/model.onnx` | `models/exported/residual_harmonic_mlp/forward/reference_inventory.yaml` |
| `residual_harmonic_mlp` | `backward` | `models/exported/residual_harmonic_mlp/backward/python/residual_harmonic_mlp-epoch=037-val_mae=0.00310962.ckpt` | `models/exported/residual_harmonic_mlp/backward/onnx/model.onnx` | `models/exported/residual_harmonic_mlp/backward/reference_inventory.yaml` |
| `feedforward` | `global` | `models/exported/feedforward/global/python/feedforward-epoch=180-val_mae=0.00305586.ckpt` | `models/exported/feedforward/global/onnx/model.onnx` | `models/exported/feedforward/global/reference_inventory.yaml` |
| `feedforward` | `forward` | `models/exported/feedforward/forward/python/feedforward-epoch=033-val_mae=0.00291539.ckpt` | `models/exported/feedforward/forward/onnx/model.onnx` | `models/exported/feedforward/forward/reference_inventory.yaml` |
| `feedforward` | `backward` | `models/exported/feedforward/backward/python/feedforward-epoch=093-val_mae=0.00304864.ckpt` | `models/exported/feedforward/backward/onnx/model.onnx` | `models/exported/feedforward/backward/reference_inventory.yaml` |
| `periodic_mlp` | `global` | `models/exported/periodic_mlp/global/python/periodic_mlp-epoch=031-val_mae=0.00309735.ckpt` | `models/exported/periodic_mlp/global/onnx/model.onnx` | `models/exported/periodic_mlp/global/reference_inventory.yaml` |
| `periodic_mlp` | `forward` | `models/exported/periodic_mlp/forward/python/periodic_mlp-epoch=022-val_mae=0.00284801.ckpt` | `models/exported/periodic_mlp/forward/onnx/model.onnx` | `models/exported/periodic_mlp/forward/reference_inventory.yaml` |
| `periodic_mlp` | `backward` | `models/exported/periodic_mlp/backward/python/periodic_mlp-epoch=049-val_mae=0.00315372.ckpt` | `models/exported/periodic_mlp/backward/onnx/model.onnx` | `models/exported/periodic_mlp/backward/reference_inventory.yaml` |
| `harmonic_regression` | `global` | `models/exported/harmonic_regression/global/python/harmonic_regression-epoch=018-val_mae=0.01701703.ckpt` | `models/exported/harmonic_regression/global/onnx/model.onnx` | `models/exported/harmonic_regression/global/reference_inventory.yaml` |
| `harmonic_regression` | `forward` | `models/exported/harmonic_regression/forward/python/harmonic_regression-epoch=068-val_mae=0.00281060.ckpt` | `models/exported/harmonic_regression/forward/onnx/model.onnx` | `models/exported/harmonic_regression/forward/reference_inventory.yaml` |
| `harmonic_regression` | `backward` | `models/exported/harmonic_regression/backward/python/harmonic_regression-epoch=019-val_mae=0.00370070.ckpt` | `models/exported/harmonic_regression/backward/onnx/model.onnx` | `models/exported/harmonic_regression/backward/reference_inventory.yaml` |

## Canonical Follow-Through

- `Wave 1` summary refreshed: `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- master summary refreshed: `doc/reports/analysis/Training Results Master Summary.md`
- campaign leaderboard refreshed: `output/training_campaigns/wave1/directional_retraining/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/campaign_leaderboard.yaml`
- campaign best run refreshed: `output/training_campaigns/wave1/directional_retraining/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/campaign_best_run.yaml`
- program best registry: `output/registries/program/current_best_solution.yaml`
