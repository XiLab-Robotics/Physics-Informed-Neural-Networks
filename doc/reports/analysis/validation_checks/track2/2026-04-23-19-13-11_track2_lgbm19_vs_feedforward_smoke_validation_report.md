# Track 2 LGBM19 Vs Feedforward Comparison Report

## Overview

This report compares the curated paper-faithful `LGBM-19` harmonic bank
against the canonical best direct-TE `feedforward` baseline on the
repository held-out TE-curve test split.

## Scope

- reference family: `LGBM`;
- reference bank size: `19` archived target models;
- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- held-out curve count: `194`;
- percentage-error denominator: `peak_to_peak_truth`;
- canonical feedforward run: `2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote`;

## Aggregate Comparison

| Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `LGBM-19 reference bank` | 0.041793 | 0.041957 | 93.133 | 303.204 |
| `feedforward best` | 0.003502 | 0.003932 | 7.718 | 14.460 |
| `oracle harmonic truncation` | 0.000846 | 0.001034 | 1.785 | 4.548 |

## Reference Bank Diagnostics

- amplitude MAE on repository harmonic decomposition: `0.010267`.
- amplitude RMSE on repository harmonic decomposition: `0.034659`.
- phase MAE on repository harmonic decomposition: `0.581902 rad`.
- phase RMSE on repository harmonic decomposition: `1.032405 rad`.

## Direction Breakdown

| Direction | Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: |
| `forward` | `lgbm19_reference_bank` | 0.001950 | 0.002160 | 4.329 |
| `forward` | `feedforward_best` | 0.003475 | 0.003905 | 7.722 |
| `forward` | `oracle_harmonic_truncation` | 0.000828 | 0.001013 | 1.766 |
| `backward` | `lgbm19_reference_bank` | 0.081635 | 0.081753 | 181.936 |
| `backward` | `feedforward_best` | 0.003529 | 0.003958 | 7.714 |
| `backward` | `oracle_harmonic_truncation` | 0.000863 | 0.001054 | 1.804 |

## Temperature Breakdown

| Temperature [C] | Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] |
| ---: | --- | ---: | ---: | ---: |
| `25.0` | `lgbm19_reference_bank` | 0.040540 | 0.040625 | 94.325 |
| `25.0` | `feedforward_best` | 0.003249 | 0.003583 | 7.688 |
| `25.0` | `oracle_harmonic_truncation` | 0.000588 | 0.000730 | 1.364 |
| `30.0` | `lgbm19_reference_bank` | 0.041731 | 0.041939 | 91.443 |
| `30.0` | `feedforward_best` | 0.003545 | 0.004031 | 7.554 |
| `30.0` | `oracle_harmonic_truncation` | 0.001026 | 0.001245 | 2.117 |
| `35.0` | `lgbm19_reference_bank` | 0.043924 | 0.044163 | 93.273 |
| `35.0` | `feedforward_best` | 0.003865 | 0.004380 | 7.972 |
| `35.0` | `oracle_harmonic_truncation` | 0.001044 | 0.001270 | 2.065 |

## Sample Preview

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | `forward` | `1000 rpm` | `1200 Nm` | `25 C` | `LGBM=6.985%` | `feedforward=9.652%` | `oracle=1.465%`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | `backward` | `1000 rpm` | `1200 Nm` | `25 C` | `LGBM=224.123%` | `feedforward=13.454%` | `oracle=1.292%`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | `forward` | `1000 rpm` | `1300 Nm` | `25 C` | `LGBM=2.404%` | `feedforward=6.079%` | `oracle=1.460%`

## Output Artifacts

- summary YAML: `output/validation_checks/track2_reference_comparison/2026-04-23-19-11-37__track2_lgbm19_vs_feedforward_smoke_validation/validation_summary.yaml`;
- per-condition CSV: `output/validation_checks/track2_reference_comparison/2026-04-23-19-11-37__track2_lgbm19_vs_feedforward_smoke_validation/per_condition_metrics.csv`;
- preview plot: `output/validation_checks/track2_reference_comparison/2026-04-23-19-11-37__track2_lgbm19_vs_feedforward_smoke_validation/preview_curves/preview_01.png`;
- preview plot: `output/validation_checks/track2_reference_comparison/2026-04-23-19-11-37__track2_lgbm19_vs_feedforward_smoke_validation/preview_curves/preview_02.png`;
- preview plot: `output/validation_checks/track2_reference_comparison/2026-04-23-19-11-37__track2_lgbm19_vs_feedforward_smoke_validation/preview_curves/preview_03.png`;
