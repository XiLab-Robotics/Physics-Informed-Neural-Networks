# Wave 1 Best Model TE Curve Prediction Report

## Overview

This report compares the current best model from each completed Wave 1
family on a deterministic subset of the canonical held-out TE test
curves. It is an offline inference and visualization pass only; no
model is trained or promoted by this report.

## Scope

- test-curve count: `97`;
- selected curve count: `97`;
- requested sample fraction: `1.000`;
- random seed: `42`;
- output directory: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction`;

## Loaded Family Best Models

| Family | Model Type | Best Run | Registry Test MAE [deg] | Registry Test RMSE [deg] |
| --- | --- | --- | ---: | ---: |
| `tree_fw` | `hist_gradient_boosting` | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | 0.002743 | 0.003409 |
| `harmonic_regression_fw` | `harmonic_regression` | `te_harmonic_dense360_tracking_Fw` | 0.002916 | 0.003237 |
| `residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | `te_residual_harmonic_rcim_sparse_tracking_Fw` | 0.003089 | 0.003498 |

## Aggregate Curve Metrics

| Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `tree_fw` | 0.003053 | 0.003395 | 6.731 | 11.995 |
| `harmonic_regression_fw` | 0.003230 | 0.003494 | 7.185 | 11.606 |
| `residual_harmonic_mlp_fw` | 0.003273 | 0.003563 | 7.266 | 12.752 |

## Selected Curves

| Index | Direction | Speed [rpm] | Torque [Nm] | Oil Temp [C] | Source |
| ---: | --- | ---: | ---: | ---: | --- |
| `0` | `forward` | 1000 | 1200 | 25 | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm1200.0Nm25.0deg.csv` |
| `1` | `forward` | 1000 | 1300 | 25 | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm1300.0Nm25.0deg.csv` |
| `2` | `forward` | 1000 | 1800 | 25 | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm1800.0Nm25.0deg.csv` |
| `3` | `forward` | 1000 | 400 | 25 | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm400.0Nm25.0deg.csv` |
| `4` | `forward` | 1000 | 800 | 25 | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm800.0Nm25.0deg.csv` |
| `5` | `forward` | 100 | 100 | 25 | `data\simplified_dataset\Test_25degree\100rpm\100.0rpm100.0Nm25.0deg.csv` |
| `6` | `forward` | 100 | 1800 | 25 | `data\simplified_dataset\Test_25degree\100rpm\100.0rpm1800.0Nm25.0deg.csv` |
| `7` | `forward` | 100 | 300 | 25 | `data\simplified_dataset\Test_25degree\100rpm\100.0rpm300.0Nm25.0deg.csv` |
| `8` | `forward` | 100 | 600 | 25 | `data\simplified_dataset\Test_25degree\100rpm\100.0rpm600.0Nm25.0deg.csv` |
| `9` | `forward` | 1300 | 1200 | 25 | `data\simplified_dataset\Test_25degree\1300rpm\1300.0rpm1200.0Nm25.0deg.csv` |
| `10` | `forward` | 1300 | 1500 | 25 | `data\simplified_dataset\Test_25degree\1300rpm\1300.0rpm1500.0Nm25.0deg.csv` |
| `11` | `forward` | 1300 | 1700 | 25 | `data\simplified_dataset\Test_25degree\1300rpm\1300.0rpm1700.0Nm25.0deg.csv` |
| `12` | `forward` | 1400 | 1600 | 25 | `data\simplified_dataset\Test_25degree\1400rpm\1400.0rpm1600.0Nm25.0deg.csv` |
| `13` | `forward` | 1600 | 1300 | 25 | `data\simplified_dataset\Test_25degree\1600rpm\1600.0rpm1300.0Nm25.0deg.csv` |
| `14` | `forward` | 1600 | 1500 | 25 | `data\simplified_dataset\Test_25degree\1600rpm\1600.0rpm1500.0Nm25.0deg.csv` |
| `15` | `forward` | 1700 | 1300 | 25 | `data\simplified_dataset\Test_25degree\1700rpm\1700.0rpm1300.0Nm25.0deg.csv` |
| `16` | `forward` | 1700 | 200 | 25 | `data\simplified_dataset\Test_25degree\1700rpm\1700.0rpm200.0Nm25.0deg.csv` |
| `17` | `forward` | 200 | 100 | 25 | `data\simplified_dataset\Test_25degree\200rpm\200.0rpm100.0Nm25.0deg.csv` |
| `18` | `forward` | 200 | 1700 | 25 | `data\simplified_dataset\Test_25degree\200rpm\200.0rpm1700.0Nm25.0deg.csv` |
| `19` | `forward` | 200 | 300 | 25 | `data\simplified_dataset\Test_25degree\200rpm\200.0rpm300.0Nm25.0deg.csv` |
| `20` | `forward` | 300 | 100 | 25 | `data\simplified_dataset\Test_25degree\300rpm\300.0rpm100.0Nm25.0deg.csv` |
| `21` | `forward` | 300 | 1000 | 25 | `data\simplified_dataset\Test_25degree\300rpm\300.0rpm1000.0Nm25.0deg.csv` |
| `22` | `forward` | 300 | 1100 | 25 | `data\simplified_dataset\Test_25degree\300rpm\300.0rpm1100.0Nm25.0deg.csv` |
| `23` | `forward` | 300 | 1700 | 25 | `data\simplified_dataset\Test_25degree\300rpm\300.0rpm1700.0Nm25.0deg.csv` |
| `24` | `forward` | 300 | 200 | 25 | `data\simplified_dataset\Test_25degree\300rpm\300.0rpm200.0Nm25.0deg.csv` |
| `25` | `forward` | 400 | 1200 | 25 | `data\simplified_dataset\Test_25degree\400rpm\400.0rpm1200.0Nm25.0deg.csv` |
| `26` | `forward` | 400 | 300 | 25 | `data\simplified_dataset\Test_25degree\400rpm\400.0rpm300.0Nm25.0deg.csv` |
| `27` | `forward` | 500 | 200 | 25 | `data\simplified_dataset\Test_25degree\500rpm\500.0rpm200.0Nm25.0deg.csv` |
| `28` | `forward` | 600 | 1000 | 25 | `data\simplified_dataset\Test_25degree\600rpm\600.0rpm1000.0Nm25.0deg.csv` |
| `29` | `forward` | 600 | 1700 | 25 | `data\simplified_dataset\Test_25degree\600rpm\600.0rpm1700.0Nm25.0deg.csv` |
| `30` | `forward` | 600 | 800 | 25 | `data\simplified_dataset\Test_25degree\600rpm\600.0rpm800.0Nm25.0deg.csv` |
| `31` | `forward` | 700 | 1400 | 25 | `data\simplified_dataset\Test_25degree\700rpm\700.0rpm1400.0Nm25.0deg.csv` |
| `32` | `forward` | 700 | 200 | 25 | `data\simplified_dataset\Test_25degree\700rpm\700.0rpm200.0Nm25.0deg.csv` |
| `33` | `forward` | 700 | 400 | 25 | `data\simplified_dataset\Test_25degree\700rpm\700.0rpm400.0Nm25.0deg.csv` |
| `34` | `forward` | 800 | 1200 | 25 | `data\simplified_dataset\Test_25degree\800rpm\800.0rpm1200.0Nm25.0deg.csv` |
| `35` | `forward` | 800 | 1300 | 25 | `data\simplified_dataset\Test_25degree\800rpm\800.0rpm1300.0Nm25.0deg.csv` |
| `36` | `forward` | 800 | 1600 | 25 | `data\simplified_dataset\Test_25degree\800rpm\800.0rpm1600.0Nm25.0deg.csv` |
| `37` | `forward` | 800 | 700 | 25 | `data\simplified_dataset\Test_25degree\800rpm\800.0rpm700.0Nm25.0deg.csv` |
| `38` | `forward` | 800 | 800 | 25 | `data\simplified_dataset\Test_25degree\800rpm\800.0rpm800.0Nm25.0deg.csv` |
| `39` | `forward` | 900 | 1200 | 25 | `data\simplified_dataset\Test_25degree\900rpm\900.0rpm1200.0Nm25.0deg.csv` |
| `40` | `forward` | 900 | 300 | 25 | `data\simplified_dataset\Test_25degree\900rpm\900.0rpm300.0Nm25.0deg.csv` |
| `41` | `forward` | 1000 | 1000 | 30 | `data\simplified_dataset\Test_30degree\1000rpm\1000.0rpm1000.0Nm30.0deg.csv` |
| `42` | `forward` | 1000 | 400 | 30 | `data\simplified_dataset\Test_30degree\1000rpm\1000.0rpm400.0Nm30.0deg.csv` |
| `43` | `forward` | 100 | 1500 | 30 | `data\simplified_dataset\Test_30degree\100rpm\100.0rpm1500.0Nm30.0deg.csv` |
| `44` | `forward` | 1100 | 1200 | 30 | `data\simplified_dataset\Test_30degree\1100rpm\1100.0rpm1200.0Nm30.0deg.csv` |
| `45` | `forward` | 1100 | 200 | 30 | `data\simplified_dataset\Test_30degree\1100rpm\1100.0rpm200.0Nm30.0deg.csv` |
| `46` | `forward` | 1300 | 0 | 30 | `data\simplified_dataset\Test_30degree\1300rpm\1300.0rpm0.0Nm30.0deg.csv` |
| `47` | `forward` | 1300 | 1300 | 30 | `data\simplified_dataset\Test_30degree\1300rpm\1300.0rpm1300.0Nm30.0deg.csv` |
| `48` | `forward` | 1300 | 300 | 30 | `data\simplified_dataset\Test_30degree\1300rpm\1300.0rpm300.0Nm30.0deg.csv` |
| `49` | `forward` | 1300 | 800 | 30 | `data\simplified_dataset\Test_30degree\1300rpm\1300.0rpm800.0Nm30.0deg.csv` |
| `50` | `forward` | 1400 | 1000 | 30 | `data\simplified_dataset\Test_30degree\1400rpm\1400.0rpm1000.0Nm30.0deg.csv` |
| `51` | `forward` | 1400 | 1300 | 30 | `data\simplified_dataset\Test_30degree\1400rpm\1400.0rpm1300.0Nm30.0deg.csv` |
| `52` | `forward` | 1400 | 900 | 30 | `data\simplified_dataset\Test_30degree\1400rpm\1400.0rpm900.0Nm30.0deg.csv` |
| `53` | `forward` | 1500 | 1500 | 30 | `data\simplified_dataset\Test_30degree\1500rpm\1500.0rpm1500.0Nm30.0deg.csv` |
| `54` | `forward` | 1500 | 900 | 30 | `data\simplified_dataset\Test_30degree\1500rpm\1500.0rpm900.0Nm30.0deg.csv` |
| `55` | `forward` | 1600 | 900 | 30 | `data\simplified_dataset\Test_30degree\1600rpm\1600.0rpm900.0Nm30.0deg.csv` |
| `56` | `forward` | 1700 | 100 | 30 | `data\simplified_dataset\Test_30degree\1700rpm\1700.0rpm100.0Nm30.0deg.csv` |
| `57` | `forward` | 1700 | 1300 | 30 | `data\simplified_dataset\Test_30degree\1700rpm\1700.0rpm1300.0Nm30.0deg.csv` |
| `58` | `forward` | 1800 | 1000 | 30 | `data\simplified_dataset\Test_30degree\1800rpm\1800.0rpm1000.0Nm30.0deg.csv` |
| `59` | `forward` | 200 | 1700 | 30 | `data\simplified_dataset\Test_30degree\200rpm\200.0rpm1700.0Nm30.0deg.csv` |
| `60` | `forward` | 400 | 0 | 30 | `data\simplified_dataset\Test_30degree\400rpm\400.0rpm0.0Nm30.0deg.csv` |
| `61` | `forward` | 400 | 1800 | 30 | `data\simplified_dataset\Test_30degree\400rpm\400.0rpm1800.0Nm30.0deg.csv` |
| `62` | `forward` | 500 | 1400 | 30 | `data\simplified_dataset\Test_30degree\500rpm\500.0rpm1400.0Nm30.0deg.csv` |
| `63` | `forward` | 500 | 800 | 30 | `data\simplified_dataset\Test_30degree\500rpm\500.0rpm800.0Nm30.0deg.csv` |
| `64` | `forward` | 600 | 1700 | 30 | `data\simplified_dataset\Test_30degree\600rpm\600.0rpm1700.0Nm30.0deg.csv` |
| `65` | `forward` | 600 | 700 | 30 | `data\simplified_dataset\Test_30degree\600rpm\600.0rpm700.0Nm30.0deg.csv` |
| `66` | `forward` | 700 | 1400 | 30 | `data\simplified_dataset\Test_30degree\700rpm\700.0rpm1400.0Nm30.0deg.csv` |
| `67` | `forward` | 700 | 300 | 30 | `data\simplified_dataset\Test_30degree\700rpm\700.0rpm300.0Nm30.0deg.csv` |
| `68` | `forward` | 700 | 900 | 30 | `data\simplified_dataset\Test_30degree\700rpm\700.0rpm900.0Nm30.0deg.csv` |
| `69` | `forward` | 800 | 1400 | 30 | `data\simplified_dataset\Test_30degree\800rpm\800.0rpm1400.0Nm30.0deg.csv` |
| `70` | `forward` | 900 | 1700 | 30 | `data\simplified_dataset\Test_30degree\900rpm\900.0rpm1700.0Nm30.0deg.csv` |
| `71` | `forward` | 900 | 200 | 30 | `data\simplified_dataset\Test_30degree\900rpm\900.0rpm200.0Nm30.0deg.csv` |
| `72` | `forward` | 1000 | 700 | 35 | `data\simplified_dataset\Test_35degree\1000rpm\1000.0rpm700.0Nm35.0deg.csv` |
| `73` | `forward` | 1100 | 1700 | 35 | `data\simplified_dataset\Test_35degree\1100rpm\1100.0rpm1700.0Nm35.0deg.csv` |
| `74` | `forward` | 1100 | 900 | 35 | `data\simplified_dataset\Test_35degree\1100rpm\1100.0rpm900.0Nm35.0deg.csv` |
| `75` | `forward` | 1300 | 1300 | 35 | `data\simplified_dataset\Test_35degree\1300rpm\1300.0rpm1300.0Nm35.0deg.csv` |
| `76` | `forward` | 1300 | 1700 | 35 | `data\simplified_dataset\Test_35degree\1300rpm\1300.0rpm1700.0Nm35.0deg.csv` |
| `77` | `forward` | 1500 | 1500 | 35 | `data\simplified_dataset\Test_35degree\1500rpm\1500.0rpm1500.0Nm35.0deg.csv` |
| `78` | `forward` | 1500 | 1700 | 35 | `data\simplified_dataset\Test_35degree\1500rpm\1500.0rpm1700.0Nm35.0deg.csv` |
| `79` | `forward` | 1600 | 1400 | 35 | `data\simplified_dataset\Test_35degree\1600rpm\1600.0rpm1400.0Nm35.0deg.csv` |
| `80` | `forward` | 1700 | 1400 | 35 | `data\simplified_dataset\Test_35degree\1700rpm\1700.0rpm1400.0Nm35.0deg.csv` |
| `81` | `forward` | 1800 | 0 | 35 | `data\simplified_dataset\Test_35degree\1800rpm\1800.0rpm0.0Nm35.0deg.csv` |
| `82` | `forward` | 1800 | 100 | 35 | `data\simplified_dataset\Test_35degree\1800rpm\1800.0rpm100.0Nm35.0deg.csv` |
| `83` | `forward` | 200 | 100 | 35 | `data\simplified_dataset\Test_35degree\200rpm\200.0rpm100.0Nm35.0deg.csv` |
| `84` | `forward` | 300 | 200 | 35 | `data\simplified_dataset\Test_35degree\300rpm\300.0rpm200.0Nm35.0deg.csv` |
| `85` | `forward` | 300 | 600 | 35 | `data\simplified_dataset\Test_35degree\300rpm\300.0rpm600.0Nm35.0deg.csv` |
| `86` | `forward` | 400 | 1500 | 35 | `data\simplified_dataset\Test_35degree\400rpm\400.0rpm1500.0Nm35.0deg.csv` |
| `87` | `forward` | 400 | 400 | 35 | `data\simplified_dataset\Test_35degree\400rpm\400.0rpm400.0Nm35.0deg.csv` |
| `88` | `forward` | 400 | 800 | 35 | `data\simplified_dataset\Test_35degree\400rpm\400.0rpm800.0Nm35.0deg.csv` |
| `89` | `forward` | 500 | 1400 | 35 | `data\simplified_dataset\Test_35degree\500rpm\500.0rpm1400.0Nm35.0deg.csv` |
| `90` | `forward` | 500 | 800 | 35 | `data\simplified_dataset\Test_35degree\500rpm\500.0rpm800.0Nm35.0deg.csv` |
| `91` | `forward` | 600 | 1800 | 35 | `data\simplified_dataset\Test_35degree\600rpm\600.0rpm1800.0Nm35.0deg.csv` |
| `92` | `forward` | 600 | 900 | 35 | `data\simplified_dataset\Test_35degree\600rpm\600.0rpm900.0Nm35.0deg.csv` |
| `93` | `forward` | 700 | 1600 | 35 | `data\simplified_dataset\Test_35degree\700rpm\700.0rpm1600.0Nm35.0deg.csv` |
| `94` | `forward` | 800 | 0 | 35 | `data\simplified_dataset\Test_35degree\800rpm\800.0rpm0.0Nm35.0deg.csv` |
| `95` | `forward` | 800 | 1100 | 35 | `data\simplified_dataset\Test_35degree\800rpm\800.0rpm1100.0Nm35.0deg.csv` |
| `96` | `forward` | 800 | 1800 | 35 | `data\simplified_dataset\Test_35degree\800rpm\800.0rpm1800.0Nm35.0deg.csv` |

## Output Artifacts

- validation summary: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction/validation_summary.yaml`;
- per-curve metrics CSV: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\per_curve_metrics.csv`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_001_dataset_0000_forward_1000_0rpm1200_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_002_dataset_0001_forward_1000_0rpm1300_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_003_dataset_0002_forward_1000_0rpm1800_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_004_dataset_0003_forward_1000_0rpm400_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_005_dataset_0004_forward_1000_0rpm800_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_006_dataset_0005_forward_100_0rpm100_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_007_dataset_0006_forward_100_0rpm1800_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_008_dataset_0007_forward_100_0rpm300_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_009_dataset_0008_forward_100_0rpm600_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_forward\2026-05-20-17-06-14__wave1_best_model_te_curve_prediction\plots\curve_010_dataset_0009_forward_1300_0rpm1200_0nm25_0deg.png`;
- additional plots omitted from this list: `87`.
