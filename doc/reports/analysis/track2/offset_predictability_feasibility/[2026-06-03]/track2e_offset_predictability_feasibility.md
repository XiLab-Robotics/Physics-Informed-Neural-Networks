# Track 2E Offset Predictability Feasibility

## Overview

This report consumes the completed `Track 2D` mean-offset artifacts and asks whether the vertical curve offset is predictable enough from causal condition information to justify an offset-aware next branch.

This is an analysis-only feasibility diagnostic. It does not train
models, alter the dataset, update registries, or use future TE samples
as model inputs.

- Run Instance: `2026-06-03-13-28-54__track2e_offset_predictability_feasibility`
- Track 2D Source: `output\validation_checks\track2d_mean_offset_full_matrix_audit\2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit`
- Output Directory: `output\validation_checks\track2e_offset_predictability_feasibility\2026-06-03-13-28-54__track2e_offset_predictability_feasibility`
- Candidate Count: `111`

## Method

- candidate raw, centered-shape, and offset metrics are imported from
  `Track 2D`;
- candidate offsets are summarized by causal groups: direction, speed,
  torque, oil temperature, and their direction-aware combinations;
- exact full-condition groups such as speed plus torque plus oil
  temperature are intentionally excluded from the recommendation
  ranking because they can collapse to one evaluated curve and
  overstate deployable offset predictability;
- the corrected `MAE` is an upper-bound diagnostic approximation:
  centered `MAE` plus the remaining absolute offset after subtracting a
  group mean offset;
- the correction baseline is not a production model and is not a valid
  registry promotion rule;
- `Fw`, `Bw`, and `global` are interpreted as parallel branches.

## Intervention Counts

| Surface | Intervention | Candidate Count |
| --- | --- | --- |
| Bw | `multi_head_shape_offset` | 19 |
| Bw | `not_offset_first` | 11 |
| Bw | `posthoc_offset_baseline` | 10 |
| Bw | `sequential_offset_model` | 1 |
| Fw | `multi_head_shape_offset` | 44 |
| Fw | `not_offset_first` | 8 |
| Fw | `sequential_offset_model` | 1 |
| global | `multi_head_shape_offset` | 12 |
| global | `not_offset_first` | 4 |
| global | `sequential_offset_model` | 1 |

## Surface Recommendations

| Rank | Candidate | Surface | Interv. | Raw MAE | Corr. MAE | Gain [%] | Explain [%] | Best Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | `rcim_retuned_XGBM19_Bw` | Bw | seq | 0.010679 | 0.005572 | 47.8 | 72.6 | dir_torque |
| 3 | `LGBM19_Fw` | Fw | seq | 0.006812 | 0.003684 | 45.9 | 61.3 | dir_torque |
| 1 | `harmonic_regression_global` | global | seq | 0.018160 | 0.004604 | 74.6 | 84.2 | dir_torque |

## Track 2E Feasibility Ranking

| Rank | Candidate | Surface | Interv. | Raw MAE | Corr. MAE | Gain [%] | Explain [%] | Best Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `harmonic_regression_global` | global | seq | 0.018160 | 0.004604 | 74.6 | 84.2 | dir_torque |
| 2 | `rcim_retuned_XGBM19_Bw` | Bw | seq | 0.010679 | 0.005572 | 47.8 | 72.6 | dir_torque |
| 3 | `LGBM19_Fw` | Fw | seq | 0.006812 | 0.003684 | 45.9 | 61.3 | dir_torque |
| 4 | `XGBM19_Bw` | Bw | post | 0.007991 | 0.003925 | 50.9 | 64.7 | dir_torque |
| 5 | `GBM19_Bw` | Bw | post | 0.005180 | 0.002811 | 45.7 | 61.3 | dir_torque |
| 6 | `RF19_Bw` | Bw | post | 0.005392 | 0.003075 | 43.0 | 58.7 | dir_torque |
| 7 | `HGBM19_Bw` | Bw | post | 0.006619 | 0.003785 | 42.8 | 58.2 | dir_torque |
| 8 | `track1_best_Bw` | Bw | post | 0.005027 | 0.002917 | 42.0 | 57.9 | dir_torque |
| 9 | `LGBM19_Bw` | Bw | post | 0.005037 | 0.002947 | 41.5 | 57.9 | dir_torque |
| 10 | `ERT19_Bw` | Bw | post | 0.005258 | 0.003248 | 38.2 | 53.7 | dir_torque |
| 11 | `DT19_Bw` | Bw | post | 0.005226 | 0.003355 | 35.8 | 50.5 | dir_torque |
| 12 | `ET19_Bw` | Bw | post | 0.006273 | 0.004289 | 31.6 | 49.7 | dir_torque |
| 13 | `rcim_retuned_LGBM19_Bw` | Bw | post | 0.008105 | 0.005684 | 29.9 | 60.3 | dir_torque |
| 14 | `ELM19_Bw` | Bw | head | 0.010071 | 0.008031 | 20.3 | 37.9 | dir_torque |
| 15 | `XGBM19_Fw` | Fw | head | 0.004190 | 0.003489 | 16.7 | 37.5 | dir_torque |
| 16 | `GBM19_Fw` | Fw | head | 0.002779 | 0.002323 | 16.4 | 44.0 | dir_torque |
| 17 | `ELM19_Fw` | Fw | head | 0.007281 | 0.006370 | 12.5 | 30.3 | dir_torque |
| 18 | `rcim_retuned_ELM19_Fw` | Fw | head | 0.007182 | 0.006367 | 11.4 | 29.0 | dir_torque |
| 19 | `SVM19_Bw` | Bw | head | 0.004822 | 0.004372 | 9.3 | 33.6 | dir_torque |
| 20 | `rcim_retuned_ELM19_Bw` | Bw | head | 0.008917 | 0.008354 | 6.3 | 32.2 | dir_torque |

## Largest Conservative Offset-Correction Gains

| Rank | Candidate | Surface | Interv. | Raw MAE | Corr. MAE | Gain [%] | Explain [%] | Best Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `harmonic_regression_global` | global | seq | 0.018160 | 0.004604 | 74.6 | 84.2 | dir_torque |
| 4 | `XGBM19_Bw` | Bw | post | 0.007991 | 0.003925 | 50.9 | 64.7 | dir_torque |
| 2 | `rcim_retuned_XGBM19_Bw` | Bw | seq | 0.010679 | 0.005572 | 47.8 | 72.6 | dir_torque |
| 3 | `LGBM19_Fw` | Fw | seq | 0.006812 | 0.003684 | 45.9 | 61.3 | dir_torque |
| 5 | `GBM19_Bw` | Bw | post | 0.005180 | 0.002811 | 45.7 | 61.3 | dir_torque |
| 6 | `RF19_Bw` | Bw | post | 0.005392 | 0.003075 | 43.0 | 58.7 | dir_torque |
| 7 | `HGBM19_Bw` | Bw | post | 0.006619 | 0.003785 | 42.8 | 58.2 | dir_torque |
| 8 | `track1_best_Bw` | Bw | post | 0.005027 | 0.002917 | 42.0 | 57.9 | dir_torque |
| 9 | `LGBM19_Bw` | Bw | post | 0.005037 | 0.002947 | 41.5 | 57.9 | dir_torque |
| 10 | `ERT19_Bw` | Bw | post | 0.005258 | 0.003248 | 38.2 | 53.7 | dir_torque |
| 11 | `DT19_Bw` | Bw | post | 0.005226 | 0.003355 | 35.8 | 50.5 | dir_torque |
| 12 | `ET19_Bw` | Bw | post | 0.006273 | 0.004289 | 31.6 | 49.7 | dir_torque |
| 13 | `rcim_retuned_LGBM19_Bw` | Bw | post | 0.008105 | 0.005684 | 29.9 | 60.3 | dir_torque |
| 14 | `ELM19_Bw` | Bw | head | 0.010071 | 0.008031 | 20.3 | 37.9 | dir_torque |
| 15 | `XGBM19_Fw` | Fw | head | 0.004190 | 0.003489 | 16.7 | 37.5 | dir_torque |

## Decision Interpretation

`sequential_offset_model` means the offset component appears large and condition-predictable enough to justify a future causal residual-offset probe. `posthoc_offset_baseline` means a simple causal aggregate calibration is worth keeping as a benchmark before training a second model.

`multi_head_shape_offset` means the next model should split centered waveform shape from offset / low-frequency behavior. `loss_reweighting` means the next safer step is a raw plus centered-shape plus offset loss. `not_offset_first` means amplitude, phase, or centered shape should stay ahead of offset correction.

## Runtime Input Boundary

The causal grouping baselines use only direction and operating condition metadata already present in the Track 2 payload. The analysis never gives a model the future TE curve. Any learned offset model still requires a later technical document and campaign plan before it can become a training branch.

## Machine-Readable Artifacts

- `output\validation_checks\track2e_offset_predictability_feasibility\2026-06-03-13-28-54__track2e_offset_predictability_feasibility\track2e_candidate_feasibility_summary.csv`
- `output\validation_checks\track2e_offset_predictability_feasibility\2026-06-03-13-28-54__track2e_offset_predictability_feasibility\track2e_surface_intervention_recommendation.csv`
- `output\validation_checks\track2e_offset_predictability_feasibility\2026-06-03-13-28-54__track2e_offset_predictability_feasibility\track2e_condition_offset_stability.csv`
- `output\validation_checks\track2e_offset_predictability_feasibility\2026-06-03-13-28-54__track2e_offset_predictability_feasibility\track2e_offset_predictability_feasibility_summary.yaml`

