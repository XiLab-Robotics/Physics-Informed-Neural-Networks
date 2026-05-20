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
- output directory: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction`;

## Loaded Family Best Models

| Family | Model Type | Best Run | Registry Test MAE [deg] | Registry Test RMSE [deg] |
| --- | --- | --- | ---: | ---: |
| `tree_bw` | `hist_gradient_boosting` | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | 0.002954 | 0.003749 |
| `harmonic_regression_bw` | `harmonic_regression` | `te_harmonic_dense240_tracking_Bw` | 0.003400 | 0.003886 |
| `residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | `te_residual_harmonic_rcim_sparse_tracking_Bw` | 0.003042 | 0.003548 |

## Aggregate Curve Metrics

| Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `tree_bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| `harmonic_regression_bw` | 0.003678 | 0.004012 | 8.058 | 15.071 |
| `residual_harmonic_mlp_bw` | 0.003536 | 0.003874 | 7.728 | 14.618 |

## Selected Curves

| Index | Direction | Speed [rpm] | Torque [Nm] | Oil Temp [C] | Source |
| ---: | --- | ---: | ---: | ---: | --- |
| `0` | `backward` | 1000 | 1200 | 25 | `data\datasets\Test_25degree\1000rpm\1000.0rpm1200.0Nm25.0deg.csv` |
| `1` | `backward` | 1000 | 1300 | 25 | `data\datasets\Test_25degree\1000rpm\1000.0rpm1300.0Nm25.0deg.csv` |
| `2` | `backward` | 1000 | 1800 | 25 | `data\datasets\Test_25degree\1000rpm\1000.0rpm1800.0Nm25.0deg.csv` |
| `3` | `backward` | 1000 | 400 | 25 | `data\datasets\Test_25degree\1000rpm\1000.0rpm400.0Nm25.0deg.csv` |
| `4` | `backward` | 1000 | 800 | 25 | `data\datasets\Test_25degree\1000rpm\1000.0rpm800.0Nm25.0deg.csv` |
| `5` | `backward` | 100 | 100 | 25 | `data\datasets\Test_25degree\100rpm\100.0rpm100.0Nm25.0deg.csv` |
| `6` | `backward` | 100 | 1800 | 25 | `data\datasets\Test_25degree\100rpm\100.0rpm1800.0Nm25.0deg.csv` |
| `7` | `backward` | 100 | 300 | 25 | `data\datasets\Test_25degree\100rpm\100.0rpm300.0Nm25.0deg.csv` |
| `8` | `backward` | 100 | 600 | 25 | `data\datasets\Test_25degree\100rpm\100.0rpm600.0Nm25.0deg.csv` |
| `9` | `backward` | 1300 | 1200 | 25 | `data\datasets\Test_25degree\1300rpm\1300.0rpm1200.0Nm25.0deg.csv` |
| `10` | `backward` | 1300 | 1500 | 25 | `data\datasets\Test_25degree\1300rpm\1300.0rpm1500.0Nm25.0deg.csv` |
| `11` | `backward` | 1300 | 1700 | 25 | `data\datasets\Test_25degree\1300rpm\1300.0rpm1700.0Nm25.0deg.csv` |
| `12` | `backward` | 1400 | 1600 | 25 | `data\datasets\Test_25degree\1400rpm\1400.0rpm1600.0Nm25.0deg.csv` |
| `13` | `backward` | 1600 | 1300 | 25 | `data\datasets\Test_25degree\1600rpm\1600.0rpm1300.0Nm25.0deg.csv` |
| `14` | `backward` | 1600 | 1500 | 25 | `data\datasets\Test_25degree\1600rpm\1600.0rpm1500.0Nm25.0deg.csv` |
| `15` | `backward` | 1700 | 1300 | 25 | `data\datasets\Test_25degree\1700rpm\1700.0rpm1300.0Nm25.0deg.csv` |
| `16` | `backward` | 1700 | 200 | 25 | `data\datasets\Test_25degree\1700rpm\1700.0rpm200.0Nm25.0deg.csv` |
| `17` | `backward` | 200 | 100 | 25 | `data\datasets\Test_25degree\200rpm\200.0rpm100.0Nm25.0deg.csv` |
| `18` | `backward` | 200 | 1700 | 25 | `data\datasets\Test_25degree\200rpm\200.0rpm1700.0Nm25.0deg.csv` |
| `19` | `backward` | 200 | 300 | 25 | `data\datasets\Test_25degree\200rpm\200.0rpm300.0Nm25.0deg.csv` |
| `20` | `backward` | 300 | 100 | 25 | `data\datasets\Test_25degree\300rpm\300.0rpm100.0Nm25.0deg.csv` |
| `21` | `backward` | 300 | 1000 | 25 | `data\datasets\Test_25degree\300rpm\300.0rpm1000.0Nm25.0deg.csv` |
| `22` | `backward` | 300 | 1100 | 25 | `data\datasets\Test_25degree\300rpm\300.0rpm1100.0Nm25.0deg.csv` |
| `23` | `backward` | 300 | 1700 | 25 | `data\datasets\Test_25degree\300rpm\300.0rpm1700.0Nm25.0deg.csv` |
| `24` | `backward` | 300 | 200 | 25 | `data\datasets\Test_25degree\300rpm\300.0rpm200.0Nm25.0deg.csv` |
| `25` | `backward` | 400 | 1200 | 25 | `data\datasets\Test_25degree\400rpm\400.0rpm1200.0Nm25.0deg.csv` |
| `26` | `backward` | 400 | 300 | 25 | `data\datasets\Test_25degree\400rpm\400.0rpm300.0Nm25.0deg.csv` |
| `27` | `backward` | 500 | 200 | 25 | `data\datasets\Test_25degree\500rpm\500.0rpm200.0Nm25.0deg.csv` |
| `28` | `backward` | 600 | 1000 | 25 | `data\datasets\Test_25degree\600rpm\600.0rpm1000.0Nm25.0deg.csv` |
| `29` | `backward` | 600 | 1700 | 25 | `data\datasets\Test_25degree\600rpm\600.0rpm1700.0Nm25.0deg.csv` |
| `30` | `backward` | 600 | 800 | 25 | `data\datasets\Test_25degree\600rpm\600.0rpm800.0Nm25.0deg.csv` |
| `31` | `backward` | 700 | 1400 | 25 | `data\datasets\Test_25degree\700rpm\700.0rpm1400.0Nm25.0deg.csv` |
| `32` | `backward` | 700 | 200 | 25 | `data\datasets\Test_25degree\700rpm\700.0rpm200.0Nm25.0deg.csv` |
| `33` | `backward` | 700 | 400 | 25 | `data\datasets\Test_25degree\700rpm\700.0rpm400.0Nm25.0deg.csv` |
| `34` | `backward` | 800 | 1200 | 25 | `data\datasets\Test_25degree\800rpm\800.0rpm1200.0Nm25.0deg.csv` |
| `35` | `backward` | 800 | 1300 | 25 | `data\datasets\Test_25degree\800rpm\800.0rpm1300.0Nm25.0deg.csv` |
| `36` | `backward` | 800 | 1600 | 25 | `data\datasets\Test_25degree\800rpm\800.0rpm1600.0Nm25.0deg.csv` |
| `37` | `backward` | 800 | 700 | 25 | `data\datasets\Test_25degree\800rpm\800.0rpm700.0Nm25.0deg.csv` |
| `38` | `backward` | 800 | 800 | 25 | `data\datasets\Test_25degree\800rpm\800.0rpm800.0Nm25.0deg.csv` |
| `39` | `backward` | 900 | 1200 | 25 | `data\datasets\Test_25degree\900rpm\900.0rpm1200.0Nm25.0deg.csv` |
| `40` | `backward` | 900 | 300 | 25 | `data\datasets\Test_25degree\900rpm\900.0rpm300.0Nm25.0deg.csv` |
| `41` | `backward` | 1000 | 1000 | 30 | `data\datasets\Test_30degree\1000rpm\1000.0rpm1000.0Nm30.0deg.csv` |
| `42` | `backward` | 1000 | 400 | 30 | `data\datasets\Test_30degree\1000rpm\1000.0rpm400.0Nm30.0deg.csv` |
| `43` | `backward` | 100 | 1500 | 30 | `data\datasets\Test_30degree\100rpm\100.0rpm1500.0Nm30.0deg.csv` |
| `44` | `backward` | 1100 | 1200 | 30 | `data\datasets\Test_30degree\1100rpm\1100.0rpm1200.0Nm30.0deg.csv` |
| `45` | `backward` | 1100 | 200 | 30 | `data\datasets\Test_30degree\1100rpm\1100.0rpm200.0Nm30.0deg.csv` |
| `46` | `backward` | 1300 | 0 | 30 | `data\datasets\Test_30degree\1300rpm\1300.0rpm0.0Nm30.0deg.csv` |
| `47` | `backward` | 1300 | 1300 | 30 | `data\datasets\Test_30degree\1300rpm\1300.0rpm1300.0Nm30.0deg.csv` |
| `48` | `backward` | 1300 | 300 | 30 | `data\datasets\Test_30degree\1300rpm\1300.0rpm300.0Nm30.0deg.csv` |
| `49` | `backward` | 1300 | 800 | 30 | `data\datasets\Test_30degree\1300rpm\1300.0rpm800.0Nm30.0deg.csv` |
| `50` | `backward` | 1400 | 1000 | 30 | `data\datasets\Test_30degree\1400rpm\1400.0rpm1000.0Nm30.0deg.csv` |
| `51` | `backward` | 1400 | 1300 | 30 | `data\datasets\Test_30degree\1400rpm\1400.0rpm1300.0Nm30.0deg.csv` |
| `52` | `backward` | 1400 | 900 | 30 | `data\datasets\Test_30degree\1400rpm\1400.0rpm900.0Nm30.0deg.csv` |
| `53` | `backward` | 1500 | 1500 | 30 | `data\datasets\Test_30degree\1500rpm\1500.0rpm1500.0Nm30.0deg.csv` |
| `54` | `backward` | 1500 | 900 | 30 | `data\datasets\Test_30degree\1500rpm\1500.0rpm900.0Nm30.0deg.csv` |
| `55` | `backward` | 1600 | 900 | 30 | `data\datasets\Test_30degree\1600rpm\1600.0rpm900.0Nm30.0deg.csv` |
| `56` | `backward` | 1700 | 100 | 30 | `data\datasets\Test_30degree\1700rpm\1700.0rpm100.0Nm30.0deg.csv` |
| `57` | `backward` | 1700 | 1300 | 30 | `data\datasets\Test_30degree\1700rpm\1700.0rpm1300.0Nm30.0deg.csv` |
| `58` | `backward` | 1800 | 1000 | 30 | `data\datasets\Test_30degree\1800rpm\1800.0rpm1000.0Nm30.0deg.csv` |
| `59` | `backward` | 200 | 1700 | 30 | `data\datasets\Test_30degree\200rpm\200.0rpm1700.0Nm30.0deg.csv` |
| `60` | `backward` | 400 | 0 | 30 | `data\datasets\Test_30degree\400rpm\400.0rpm0.0Nm30.0deg.csv` |
| `61` | `backward` | 400 | 1800 | 30 | `data\datasets\Test_30degree\400rpm\400.0rpm1800.0Nm30.0deg.csv` |
| `62` | `backward` | 500 | 1400 | 30 | `data\datasets\Test_30degree\500rpm\500.0rpm1400.0Nm30.0deg.csv` |
| `63` | `backward` | 500 | 800 | 30 | `data\datasets\Test_30degree\500rpm\500.0rpm800.0Nm30.0deg.csv` |
| `64` | `backward` | 600 | 1700 | 30 | `data\datasets\Test_30degree\600rpm\600.0rpm1700.0Nm30.0deg.csv` |
| `65` | `backward` | 600 | 700 | 30 | `data\datasets\Test_30degree\600rpm\600.0rpm700.0Nm30.0deg.csv` |
| `66` | `backward` | 700 | 1400 | 30 | `data\datasets\Test_30degree\700rpm\700.0rpm1400.0Nm30.0deg.csv` |
| `67` | `backward` | 700 | 300 | 30 | `data\datasets\Test_30degree\700rpm\700.0rpm300.0Nm30.0deg.csv` |
| `68` | `backward` | 700 | 900 | 30 | `data\datasets\Test_30degree\700rpm\700.0rpm900.0Nm30.0deg.csv` |
| `69` | `backward` | 800 | 1400 | 30 | `data\datasets\Test_30degree\800rpm\800.0rpm1400.0Nm30.0deg.csv` |
| `70` | `backward` | 900 | 1700 | 30 | `data\datasets\Test_30degree\900rpm\900.0rpm1700.0Nm30.0deg.csv` |
| `71` | `backward` | 900 | 200 | 30 | `data\datasets\Test_30degree\900rpm\900.0rpm200.0Nm30.0deg.csv` |
| `72` | `backward` | 1000 | 700 | 35 | `data\datasets\Test_35degree\1000rpm\1000.0rpm700.0Nm35.0deg.csv` |
| `73` | `backward` | 1100 | 1700 | 35 | `data\datasets\Test_35degree\1100rpm\1100.0rpm1700.0Nm35.0deg.csv` |
| `74` | `backward` | 1100 | 900 | 35 | `data\datasets\Test_35degree\1100rpm\1100.0rpm900.0Nm35.0deg.csv` |
| `75` | `backward` | 1300 | 1300 | 35 | `data\datasets\Test_35degree\1300rpm\1300.0rpm1300.0Nm35.0deg.csv` |
| `76` | `backward` | 1300 | 1700 | 35 | `data\datasets\Test_35degree\1300rpm\1300.0rpm1700.0Nm35.0deg.csv` |
| `77` | `backward` | 1500 | 1500 | 35 | `data\datasets\Test_35degree\1500rpm\1500.0rpm1500.0Nm35.0deg.csv` |
| `78` | `backward` | 1500 | 1700 | 35 | `data\datasets\Test_35degree\1500rpm\1500.0rpm1700.0Nm35.0deg.csv` |
| `79` | `backward` | 1600 | 1400 | 35 | `data\datasets\Test_35degree\1600rpm\1600.0rpm1400.0Nm35.0deg.csv` |
| `80` | `backward` | 1700 | 1400 | 35 | `data\datasets\Test_35degree\1700rpm\1700.0rpm1400.0Nm35.0deg.csv` |
| `81` | `backward` | 1800 | 0 | 35 | `data\datasets\Test_35degree\1800rpm\1800.0rpm0.0Nm35.0deg.csv` |
| `82` | `backward` | 1800 | 100 | 35 | `data\datasets\Test_35degree\1800rpm\1800.0rpm100.0Nm35.0deg.csv` |
| `83` | `backward` | 200 | 100 | 35 | `data\datasets\Test_35degree\200rpm\200.0rpm100.0Nm35.0deg.csv` |
| `84` | `backward` | 300 | 200 | 35 | `data\datasets\Test_35degree\300rpm\300.0rpm200.0Nm35.0deg.csv` |
| `85` | `backward` | 300 | 600 | 35 | `data\datasets\Test_35degree\300rpm\300.0rpm600.0Nm35.0deg.csv` |
| `86` | `backward` | 400 | 1500 | 35 | `data\datasets\Test_35degree\400rpm\400.0rpm1500.0Nm35.0deg.csv` |
| `87` | `backward` | 400 | 400 | 35 | `data\datasets\Test_35degree\400rpm\400.0rpm400.0Nm35.0deg.csv` |
| `88` | `backward` | 400 | 800 | 35 | `data\datasets\Test_35degree\400rpm\400.0rpm800.0Nm35.0deg.csv` |
| `89` | `backward` | 500 | 1400 | 35 | `data\datasets\Test_35degree\500rpm\500.0rpm1400.0Nm35.0deg.csv` |
| `90` | `backward` | 500 | 800 | 35 | `data\datasets\Test_35degree\500rpm\500.0rpm800.0Nm35.0deg.csv` |
| `91` | `backward` | 600 | 1800 | 35 | `data\datasets\Test_35degree\600rpm\600.0rpm1800.0Nm35.0deg.csv` |
| `92` | `backward` | 600 | 900 | 35 | `data\datasets\Test_35degree\600rpm\600.0rpm900.0Nm35.0deg.csv` |
| `93` | `backward` | 700 | 1600 | 35 | `data\datasets\Test_35degree\700rpm\700.0rpm1600.0Nm35.0deg.csv` |
| `94` | `backward` | 800 | 0 | 35 | `data\datasets\Test_35degree\800rpm\800.0rpm0.0Nm35.0deg.csv` |
| `95` | `backward` | 800 | 1100 | 35 | `data\datasets\Test_35degree\800rpm\800.0rpm1100.0Nm35.0deg.csv` |
| `96` | `backward` | 800 | 1800 | 35 | `data\datasets\Test_35degree\800rpm\800.0rpm1800.0Nm35.0deg.csv` |

## Output Artifacts

- validation summary: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction/validation_summary.yaml`;
- per-curve metrics CSV: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\per_curve_metrics.csv`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_001_dataset_0000_backward_1000_0rpm1200_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_002_dataset_0001_backward_1000_0rpm1300_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_003_dataset_0002_backward_1000_0rpm1800_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_004_dataset_0003_backward_1000_0rpm400_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_005_dataset_0004_backward_1000_0rpm800_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_006_dataset_0005_backward_100_0rpm100_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_007_dataset_0006_backward_100_0rpm1800_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_008_dataset_0007_backward_100_0rpm300_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_009_dataset_0008_backward_100_0rpm600_0nm25_0deg.png`;
- plot: `output\validation_checks\wave1_high_order_track2_curve_prediction_backward\2026-05-20-17-08-08__wave1_best_model_te_curve_prediction\plots\curve_010_dataset_0009_backward_1300_0rpm1200_0nm25_0deg.png`;
- additional plots omitted from this list: `87`.
