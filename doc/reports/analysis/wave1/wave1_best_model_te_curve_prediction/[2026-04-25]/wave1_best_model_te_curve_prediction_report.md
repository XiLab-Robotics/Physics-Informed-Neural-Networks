# Wave 1 Best Model TE Curve Prediction Report

## Overview

This report compares the current best model from each completed Wave 1
family on a deterministic subset of the canonical held-out TE test
curves. It is an offline inference and visualization pass only; no
model is trained or promoted by this report.

## Scope

- test-curve count: `194`;
- selected curve count: `39`;
- requested sample fraction: `0.200`;
- random seed: `42`;
- output directory: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction`;

## Loaded Family Best Models

| Family | Model Type | Best Run | Registry Test MAE [deg] | Registry Test RMSE [deg] |
| --- | --- | --- | ---: | ---: |
| `tree` | `hist_gradient_boosting` | `te_hist_gbr_tabular` | 0.002885 | 0.003607 |
| `residual_harmonic_mlp` | `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | 0.003152 | 0.003640 |
| `feedforward` | `feedforward` | `te_feedforward_stride1_high_compute_long_remote` | 0.003264 | 0.003679 |
| `periodic_mlp` | `periodic_mlp` | `te_periodic_mlp_h04_standard` | 0.003317 | 0.003793 |
| `harmonic_regression` | `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | 0.020782 | 0.022405 |

## Aggregate Curve Metrics

| Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `tree` | 0.003023 | 0.003373 | 6.947 | 14.079 |
| `residual_harmonic_mlp` | 0.003353 | 0.003727 | 7.734 | 13.474 |
| `feedforward` | 0.003432 | 0.003814 | 7.917 | 15.060 |
| `periodic_mlp` | 0.003422 | 0.003804 | 7.898 | 13.684 |
| `harmonic_regression` | 0.018997 | 0.019160 | 44.412 | 86.736 |

## Selected Curves

| Index | Direction | Speed [rpm] | Torque [Nm] | Oil Temp [C] | Source |
| ---: | --- | ---: | ---: | ---: | --- |
| `1` | `backward` | 1000 | 1200 | 25 | `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` |
| `6` | `forward` | 1000 | 400 | 25 | `data/datasets/Test_25degree/1000rpm/1000.0rpm400.0Nm25.0deg.csv` |
| `7` | `backward` | 1000 | 400 | 25 | `data/datasets/Test_25degree/1000rpm/1000.0rpm400.0Nm25.0deg.csv` |
| `8` | `forward` | 1000 | 800 | 25 | `data/datasets/Test_25degree/1000rpm/1000.0rpm800.0Nm25.0deg.csv` |
| `22` | `forward` | 1300 | 1700 | 25 | `data/datasets/Test_25degree/1300rpm/1300.0rpm1700.0Nm25.0deg.csv` |
| `23` | `backward` | 1300 | 1700 | 25 | `data/datasets/Test_25degree/1300rpm/1300.0rpm1700.0Nm25.0deg.csv` |
| `26` | `forward` | 1600 | 1300 | 25 | `data/datasets/Test_25degree/1600rpm/1600.0rpm1300.0Nm25.0deg.csv` |
| `28` | `forward` | 1600 | 1500 | 25 | `data/datasets/Test_25degree/1600rpm/1600.0rpm1500.0Nm25.0deg.csv` |
| `35` | `backward` | 200 | 100 | 25 | `data/datasets/Test_25degree/200rpm/200.0rpm100.0Nm25.0deg.csv` |
| `39` | `backward` | 200 | 300 | 25 | `data/datasets/Test_25degree/200rpm/200.0rpm300.0Nm25.0deg.csv` |
| `40` | `forward` | 300 | 100 | 25 | `data/datasets/Test_25degree/300rpm/300.0rpm100.0Nm25.0deg.csv` |
| `50` | `forward` | 400 | 1200 | 25 | `data/datasets/Test_25degree/400rpm/400.0rpm1200.0Nm25.0deg.csv` |
| `55` | `backward` | 500 | 200 | 25 | `data/datasets/Test_25degree/500rpm/500.0rpm200.0Nm25.0deg.csv` |
| `56` | `forward` | 600 | 1000 | 25 | `data/datasets/Test_25degree/600rpm/600.0rpm1000.0Nm25.0deg.csv` |
| `57` | `backward` | 600 | 1000 | 25 | `data/datasets/Test_25degree/600rpm/600.0rpm1000.0Nm25.0deg.csv` |
| `59` | `backward` | 600 | 1700 | 25 | `data/datasets/Test_25degree/600rpm/600.0rpm1700.0Nm25.0deg.csv` |
| `62` | `forward` | 700 | 1400 | 25 | `data/datasets/Test_25degree/700rpm/700.0rpm1400.0Nm25.0deg.csv` |
| `70` | `forward` | 800 | 1300 | 25 | `data/datasets/Test_25degree/800rpm/800.0rpm1300.0Nm25.0deg.csv` |
| `71` | `backward` | 800 | 1300 | 25 | `data/datasets/Test_25degree/800rpm/800.0rpm1300.0Nm25.0deg.csv` |
| `86` | `forward` | 100 | 1500 | 30 | `data/datasets/Test_30degree/100rpm/100.0rpm1500.0Nm30.0deg.csv` |
| `87` | `backward` | 100 | 1500 | 30 | `data/datasets/Test_30degree/100rpm/100.0rpm1500.0Nm30.0deg.csv` |
| `107` | `backward` | 1500 | 1500 | 30 | `data/datasets/Test_30degree/1500rpm/1500.0rpm1500.0Nm30.0deg.csv` |
| `108` | `forward` | 1500 | 900 | 30 | `data/datasets/Test_30degree/1500rpm/1500.0rpm900.0Nm30.0deg.csv` |
| `114` | `forward` | 1700 | 1300 | 30 | `data/datasets/Test_30degree/1700rpm/1700.0rpm1300.0Nm30.0deg.csv` |
| `129` | `backward` | 600 | 1700 | 30 | `data/datasets/Test_30degree/600rpm/600.0rpm1700.0Nm30.0deg.csv` |
| `139` | `backward` | 800 | 1400 | 30 | `data/datasets/Test_30degree/800rpm/800.0rpm1400.0Nm30.0deg.csv` |
| `143` | `backward` | 900 | 200 | 30 | `data/datasets/Test_30degree/900rpm/900.0rpm200.0Nm30.0deg.csv` |
| `150` | `forward` | 1300 | 1300 | 35 | `data/datasets/Test_35degree/1300rpm/1300.0rpm1300.0Nm35.0deg.csv` |
| `151` | `backward` | 1300 | 1300 | 35 | `data/datasets/Test_35degree/1300rpm/1300.0rpm1300.0Nm35.0deg.csv` |
| `154` | `forward` | 1500 | 1500 | 35 | `data/datasets/Test_35degree/1500rpm/1500.0rpm1500.0Nm35.0deg.csv` |
| `163` | `backward` | 1800 | 0 | 35 | `data/datasets/Test_35degree/1800rpm/1800.0rpm0.0Nm35.0deg.csv` |
| `166` | `forward` | 200 | 100 | 35 | `data/datasets/Test_35degree/200rpm/200.0rpm100.0Nm35.0deg.csv` |
| `173` | `backward` | 400 | 1500 | 35 | `data/datasets/Test_35degree/400rpm/400.0rpm1500.0Nm35.0deg.csv` |
| `176` | `forward` | 400 | 800 | 35 | `data/datasets/Test_35degree/400rpm/400.0rpm800.0Nm35.0deg.csv` |
| `180` | `forward` | 500 | 800 | 35 | `data/datasets/Test_35degree/500rpm/500.0rpm800.0Nm35.0deg.csv` |
| `183` | `backward` | 600 | 1800 | 35 | `data/datasets/Test_35degree/600rpm/600.0rpm1800.0Nm35.0deg.csv` |
| `189` | `backward` | 800 | 0 | 35 | `data/datasets/Test_35degree/800rpm/800.0rpm0.0Nm35.0deg.csv` |
| `191` | `backward` | 800 | 1100 | 35 | `data/datasets/Test_35degree/800rpm/800.0rpm1100.0Nm35.0deg.csv` |
| `193` | `backward` | 800 | 1800 | 35 | `data/datasets/Test_35degree/800rpm/800.0rpm1800.0Nm35.0deg.csv` |

## Output Artifacts

- validation summary: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/validation_summary.yaml`;
- per-curve metrics CSV: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/per_curve_metrics.csv`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_001_dataset_0001_backward_1000_0rpm1200_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_002_dataset_0006_forward_1000_0rpm400_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_003_dataset_0007_backward_1000_0rpm400_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_004_dataset_0008_forward_1000_0rpm800_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_005_dataset_0022_forward_1300_0rpm1700_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_006_dataset_0023_backward_1300_0rpm1700_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_007_dataset_0026_forward_1600_0rpm1300_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_008_dataset_0028_forward_1600_0rpm1500_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_009_dataset_0035_backward_200_0rpm100_0nm25_0deg.png`;
- plot: `output/validation_checks/wave1_best_model_te_curve_prediction/2026-04-25-11-22-44__wave1_best_model_te_curve_prediction/plots/curve_010_dataset_0039_backward_200_0rpm300_0nm25_0deg.png`;
- additional plots omitted from this list: `29`.
