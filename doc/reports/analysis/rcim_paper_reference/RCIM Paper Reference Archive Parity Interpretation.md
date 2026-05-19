# RCIM Paper Reference Archive Parity Interpretation

## Executive Verdict

The repository paper-reference archives are internally consistent but they
are not three equivalent implementations of the same fitted model surface.

The direct same-family comparison shows that `rcim_original/forward` and
`rcim_retuned/forward` are mostly similar, with `DT` and `LGBM` effectively
near-equivalent on Track 2 curve metrics and substantial differences only
for `MLP` and `ELM`. By contrast, `rcim_track1` is not a near-copy of either
`rcim_original` or `rcim_retuned`: many forward families and all backward
families show substantial Track 2 metric differences.

`rcim_original/forward` remains the recovered original-pipeline baseline.
`rcim_retuned` is the closest repository-local continuation of that
pipeline and the strongest Track 2 curve performer in this comparison.
`rcim_track1` is the closed faithful full-dataset Track 1 archive: it is
structurally complete and direction-valid, but it is a materially different
trained archive rather than an interchangeable implementation of the
original or retuned bank.

The practical conclusion is that the three archives are usable as distinct
baselines: original-paper behavior, retuned recovered-pipeline behavior,
and final Track 1 faithful full-dataset behavior.

## Source Validation Artifacts

| Artifact | Path |
| --- | --- |
| Source Track 2 summary | `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\validation_summary.yaml` |
| Validation summary YAML | `output\validation_checks\rcim_paper_reference_archive_parity\2026_05_18_22_18_12__paper_reference_archive_parity_paper_reference_archive_pairwise_v2\validation_summary.yaml` |
| Curve metric CSV | `output\validation_checks\rcim_paper_reference_archive_parity\2026_05_18_22_18_12__paper_reference_archive_parity_paper_reference_archive_pairwise_v2\curve_metric_comparison.csv` |
| Target metric CSV | `output\validation_checks\rcim_paper_reference_archive_parity\2026_05_18_22_18_12__paper_reference_archive_parity_paper_reference_archive_pairwise_v2\target_metric_comparison.csv` |
| Pairwise comparison CSV | `output\validation_checks\rcim_paper_reference_archive_parity\2026_05_18_22_18_12__paper_reference_archive_parity_paper_reference_archive_pairwise_v2\pairwise_archive_comparison.csv` |
| Original archive | `models/paper_reference/rcim_original` |
| Retuned archive | `models/paper_reference/rcim_retuned` |
| Track 1 archive | `models/paper_reference/rcim_track1` |

## Test Context

| Item | Value |
| --- | --- |
| Dataset config | `config/datasets/transmission_error_dataset.yaml` |
| Dataset root | `data\datasets` |
| Source contract | `data/datasets` |
| Source comparison mode | `full_directional_candidate_matrix` |
| Held-out curve count | `194` |
| Percentage-error denominator | `peak_to_peak_truth` |
| Forward policy | `Fw` archives evaluated only on forward curves |
| Backward policy | `Bw` archives evaluated only on backward curves |
| Original backward coverage | not available in `rcim_original` |

## Same-Family Archive Parity Verdict

This is the direct implementation-to-implementation comparison. It compares
the same family across archive groups on the same direction-valid Track 2
curve surface. A positive delta means the right-side archive has higher
mean percentage error than the left-side archive.

Classification thresholds are intentionally pragmatic:

- `near-equivalent`: absolute delta MPE at or below `0.25` percentage points;
- `similar`: absolute delta MPE above `0.25` and at or below `2.0` points;
- `substantial difference`: absolute delta MPE above `2.0` points.

| Comparison | Near-Equivalent | Similar | Substantial Difference |
| --- | ---: | ---: | ---: |
| `forward_original_vs_retuned` | 2 | 7 | 2 |
| `forward_original_vs_track1` | 0 | 4 | 7 |
| `forward_retuned_vs_track1` | 2 | 2 | 7 |
| `backward_retuned_vs_track1` | 0 | 0 | 11 |

### Forward Original Vs Retuned

| Family | Left Candidate | Right Candidate | Left MPE [%] | Right MPE [%] | Delta MPE [pp] | Delta Curve MAE [deg] | Verdict |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `SVM` | `rcim_original_SVM19_Fw` | `rcim_retuned_SVM19_Fw` | 6.767 | 7.035 | 0.269 | 0.000114 | `similar` |
| `MLP` | `rcim_original_MLP19_Fw` | `rcim_retuned_MLP19_Fw` | 42.943 | 38.510 | -4.434 | -0.002107 | `substantial difference` |
| `RF` | `rcim_original_RF19_Fw` | `rcim_retuned_RF19_Fw` | 3.940 | 3.292 | -0.648 | -0.000280 | `similar` |
| `DT` | `rcim_original_DT19_Fw` | `rcim_retuned_DT19_Fw` | 4.306 | 4.306 | -0.000 | -0.000000 | `near-equivalent` |
| `ET` | `rcim_original_ET19_Fw` | `rcim_retuned_ET19_Fw` | 4.985 | 4.426 | -0.559 | -0.000232 | `similar` |
| `ERT` | `rcim_original_ERT19_Fw` | `rcim_retuned_ERT19_Fw` | 3.253 | 4.039 | 0.786 | 0.000336 | `similar` |
| `GBM` | `rcim_original_GBM19_Fw` | `rcim_retuned_GBM19_Fw` | 4.312 | 2.372 | -1.940 | -0.000832 | `similar` |
| `HGBM` | `rcim_original_HGBM19_Fw` | `rcim_retuned_HGBM19_Fw` | 4.493 | 4.126 | -0.367 | -0.000160 | `similar` |
| `XGBM` | `rcim_original_XGBM19_Fw` | `rcim_retuned_XGBM19_Fw` | 5.805 | 4.588 | -1.218 | -0.000540 | `similar` |
| `LGBM` | `rcim_original_LGBM19_Fw` | `rcim_retuned_LGBM19_Fw` | 4.017 | 4.135 | 0.118 | 0.000051 | `near-equivalent` |
| `ELM` | `rcim_original_ELM19_Fw` | `rcim_retuned_ELM19_Fw` | 12.130 | 16.181 | 4.052 | 0.001759 | `substantial difference` |

### Forward Original Vs Track 1

| Family | Left Candidate | Right Candidate | Left MPE [%] | Right MPE [%] | Delta MPE [pp] | Delta Curve MAE [deg] | Verdict |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `SVM` | `rcim_original_SVM19_Fw` | `SVM19_Fw` | 6.767 | 7.185 | 0.418 | 0.000184 | `similar` |
| `MLP` | `rcim_original_MLP19_Fw` | `MLP19_Fw` | 42.943 | 89.567 | 46.624 | 0.019936 | `substantial difference` |
| `RF` | `rcim_original_RF19_Fw` | `RF19_Fw` | 3.940 | 4.841 | 0.901 | 0.000397 | `similar` |
| `DT` | `rcim_original_DT19_Fw` | `DT19_Fw` | 4.306 | 7.011 | 2.705 | 0.001203 | `substantial difference` |
| `ET` | `rcim_original_ET19_Fw` | `ET19_Fw` | 4.985 | 7.339 | 2.354 | 0.001034 | `substantial difference` |
| `ERT` | `rcim_original_ERT19_Fw` | `ERT19_Fw` | 3.253 | 5.163 | 1.910 | 0.000824 | `similar` |
| `GBM` | `rcim_original_GBM19_Fw` | `GBM19_Fw` | 4.312 | 6.238 | 1.926 | 0.000858 | `similar` |
| `HGBM` | `rcim_original_HGBM19_Fw` | `HGBM19_Fw` | 4.493 | 7.315 | 2.822 | 0.001240 | `substantial difference` |
| `XGBM` | `rcim_original_XGBM19_Fw` | `XGBM19_Fw` | 5.805 | 9.407 | 3.601 | 0.001596 | `substantial difference` |
| `LGBM` | `rcim_original_LGBM19_Fw` | `LGBM19_Fw` | 4.017 | 15.415 | 11.398 | 0.005012 | `substantial difference` |
| `ELM` | `rcim_original_ELM19_Fw` | `ELM19_Fw` | 12.130 | 16.352 | 4.222 | 0.001858 | `substantial difference` |

### Forward Retuned Vs Track 1

| Family | Left Candidate | Right Candidate | Left MPE [%] | Right MPE [%] | Delta MPE [pp] | Delta Curve MAE [deg] | Verdict |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `SVM` | `rcim_retuned_SVM19_Fw` | `SVM19_Fw` | 7.035 | 7.185 | 0.149 | 0.000069 | `near-equivalent` |
| `MLP` | `rcim_retuned_MLP19_Fw` | `MLP19_Fw` | 38.510 | 89.567 | 51.057 | 0.022044 | `substantial difference` |
| `RF` | `rcim_retuned_RF19_Fw` | `RF19_Fw` | 3.292 | 4.841 | 1.550 | 0.000677 | `similar` |
| `DT` | `rcim_retuned_DT19_Fw` | `DT19_Fw` | 4.306 | 7.011 | 2.705 | 0.001203 | `substantial difference` |
| `ET` | `rcim_retuned_ET19_Fw` | `ET19_Fw` | 4.426 | 7.339 | 2.914 | 0.001266 | `substantial difference` |
| `ERT` | `rcim_retuned_ERT19_Fw` | `ERT19_Fw` | 4.039 | 5.163 | 1.125 | 0.000488 | `similar` |
| `GBM` | `rcim_retuned_GBM19_Fw` | `GBM19_Fw` | 2.372 | 6.238 | 3.867 | 0.001690 | `substantial difference` |
| `HGBM` | `rcim_retuned_HGBM19_Fw` | `HGBM19_Fw` | 4.126 | 7.315 | 3.189 | 0.001400 | `substantial difference` |
| `XGBM` | `rcim_retuned_XGBM19_Fw` | `XGBM19_Fw` | 4.588 | 9.407 | 4.819 | 0.002136 | `substantial difference` |
| `LGBM` | `rcim_retuned_LGBM19_Fw` | `LGBM19_Fw` | 4.135 | 15.415 | 11.280 | 0.004961 | `substantial difference` |
| `ELM` | `rcim_retuned_ELM19_Fw` | `ELM19_Fw` | 16.181 | 16.352 | 0.171 | 0.000098 | `near-equivalent` |

### Backward Retuned Vs Track 1

| Family | Left Candidate | Right Candidate | Left MPE [%] | Right MPE [%] | Delta MPE [pp] | Delta Curve MAE [deg] | Verdict |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `SVM` | `rcim_retuned_SVM19_Bw` | `SVM19_Bw` | 8.813 | 10.864 | 2.051 | 0.000806 | `substantial difference` |
| `MLP` | `rcim_retuned_MLP19_Bw` | `MLP19_Bw` | 44.141 | 86.544 | 42.402 | 0.017565 | `substantial difference` |
| `RF` | `rcim_retuned_RF19_Bw` | `RF19_Bw` | 7.543 | 12.731 | 5.188 | 0.001743 | `substantial difference` |
| `DT` | `rcim_retuned_DT19_Bw` | `DT19_Bw` | 9.728 | 12.359 | 2.631 | 0.000648 | `substantial difference` |
| `ET` | `rcim_retuned_ET19_Bw` | `ET19_Bw` | 7.021 | 14.314 | 7.293 | 0.002832 | `substantial difference` |
| `ERT` | `rcim_retuned_ERT19_Bw` | `ERT19_Bw` | 7.269 | 12.434 | 5.165 | 0.001707 | `substantial difference` |
| `GBM` | `rcim_retuned_GBM19_Bw` | `GBM19_Bw` | 5.398 | 12.252 | 6.853 | 0.002414 | `substantial difference` |
| `HGBM` | `rcim_retuned_HGBM19_Bw` | `HGBM19_Bw` | 9.978 | 15.494 | 5.516 | 0.001936 | `substantial difference` |
| `XGBM` | `rcim_retuned_XGBM19_Bw` | `XGBM19_Bw` | 24.184 | 18.722 | -5.461 | -0.002688 | `substantial difference` |
| `LGBM` | `rcim_retuned_LGBM19_Bw` | `LGBM19_Bw` | 18.057 | 11.880 | -6.177 | -0.003069 | `substantial difference` |
| `ELM` | `rcim_retuned_ELM19_Bw` | `ELM19_Bw` | 20.169 | 23.034 | 2.865 | 0.001154 | `substantial difference` |

## Forward Archive Comparison

Forward compares all three archives on the same forward Track 2 curve
surface. The best family rows are:

| Archive | Best Family Candidate | Mean Percentage Error [%] | Curve MAE [deg] |
| --- | --- | ---: | ---: |
| `rcim_original` | `rcim_original_ERT19_Fw` | 3.253 | 0.001471 |
| `rcim_retuned` | `rcim_retuned_GBM19_Fw` | 2.372 | 0.001089 |
| `rcim_track1` | `RF19_Fw` | 4.841 | 0.002164 |

### Original Forward Models

| Candidate | Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `rcim_original_ERT19_Fw` | `ERT` | 0.001471 | 0.001677 | 3.253 | 6.145 |
| `rcim_original_RF19_Fw` | `RF` | 0.001767 | 0.001971 | 3.940 | 6.872 |
| `rcim_original_LGBM19_Fw` | `LGBM` | 0.001801 | 0.002004 | 4.017 | 10.054 |
| `rcim_original_DT19_Fw` | `DT` | 0.001919 | 0.002114 | 4.306 | 9.063 |
| `rcim_original_GBM19_Fw` | `GBM` | 0.001921 | 0.002122 | 4.312 | 8.193 |
| `rcim_original_HGBM19_Fw` | `HGBM` | 0.002011 | 0.002217 | 4.493 | 10.617 |
| `rcim_original_ET19_Fw` | `ET` | 0.002232 | 0.002432 | 4.985 | 11.357 |
| `rcim_original_XGBM19_Fw` | `XGBM` | 0.002594 | 0.002814 | 5.805 | 10.574 |
| `paper_original_best_Fw` | `best_composite` | 0.002769 | 0.002951 | 6.250 | 13.827 |
| `rcim_original_SVM19_Fw` | `SVM` | 0.003052 | 0.003324 | 6.767 | 13.827 |
| `rcim_original_ELM19_Fw` | `ELM` | 0.005423 | 0.005731 | 12.130 | 28.721 |
| `rcim_original_MLP19_Fw` | `MLP` | 0.018754 | 0.022589 | 42.943 | 107.515 |

### Retuned Forward Models

| Candidate | Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_GBM19_Fw` | `GBM` | 0.001089 | 0.001299 | 2.372 | 4.912 |
| `rcim_retuned_RF19_Fw` | `RF` | 0.001487 | 0.001699 | 3.292 | 5.998 |
| `rcim_retuned_ERT19_Fw` | `ERT` | 0.001807 | 0.002010 | 4.039 | 7.599 |
| `paper_retuned_best_Fw` | `best_composite` | 0.001839 | 0.002041 | 4.109 | 9.866 |
| `rcim_retuned_HGBM19_Fw` | `HGBM` | 0.001851 | 0.002056 | 4.126 | 9.401 |
| `rcim_retuned_LGBM19_Fw` | `LGBM` | 0.001851 | 0.002055 | 4.135 | 9.866 |
| `rcim_retuned_DT19_Fw` | `DT` | 0.001919 | 0.002114 | 4.306 | 9.063 |
| `rcim_retuned_ET19_Fw` | `ET` | 0.002001 | 0.002196 | 4.426 | 9.533 |
| `rcim_retuned_XGBM19_Fw` | `XGBM` | 0.002054 | 0.002264 | 4.588 | 10.488 |
| `rcim_retuned_SVM19_Fw` | `SVM` | 0.003167 | 0.003428 | 7.035 | 12.971 |
| `rcim_retuned_ELM19_Fw` | `ELM` | 0.007182 | 0.007463 | 16.181 | 40.024 |
| `rcim_retuned_MLP19_Fw` | `MLP` | 0.016647 | 0.020154 | 38.510 | 86.197 |

### Track 1 Forward Models

| Candidate | Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `RF19_Fw` | `RF` | 0.002164 | 0.002371 | 4.841 | 11.061 |
| `ERT19_Fw` | `ERT` | 0.002295 | 0.002491 | 5.163 | 13.141 |
| `GBM19_Fw` | `GBM` | 0.002779 | 0.002981 | 6.238 | 12.995 |
| `track1_best_Fw` | `best_composite` | 0.003014 | 0.003204 | 6.819 | 11.638 |
| `DT19_Fw` | `DT` | 0.003122 | 0.003313 | 7.011 | 13.928 |
| `SVM19_Fw` | `SVM` | 0.003236 | 0.003487 | 7.185 | 11.841 |
| `HGBM19_Fw` | `HGBM` | 0.003251 | 0.003464 | 7.315 | 13.802 |
| `ET19_Fw` | `ET` | 0.003267 | 0.003467 | 7.339 | 14.670 |
| `XGBM19_Fw` | `XGBM` | 0.004190 | 0.004396 | 9.407 | 22.660 |
| `LGBM19_Fw` | `LGBM` | 0.006812 | 0.007009 | 15.415 | 30.398 |
| `ELM19_Fw` | `ELM` | 0.007281 | 0.007573 | 16.352 | 36.326 |
| `MLP19_Fw` | `MLP` | 0.038690 | 0.047157 | 89.567 | 201.437 |

## Backward Archive Comparison

Backward comparison is available for `rcim_retuned` and `rcim_track1`.
`rcim_original` has no original backward archive and is therefore absent
from this section.

| Archive | Best Family Candidate | Mean Percentage Error [%] | Curve MAE [deg] |
| --- | --- | ---: | ---: |
| `rcim_retuned` | `rcim_retuned_GBM19_Bw` | 5.398 | 0.002766 |
| `rcim_track1` | `SVM19_Bw` | 10.864 | 0.004822 |

### Retuned Backward Models

| Candidate | Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_GBM19_Bw` | `GBM` | 0.002766 | 0.003300 | 5.398 | 12.280 |
| `rcim_retuned_ET19_Bw` | `ET` | 0.003441 | 0.004028 | 7.021 | 15.287 |
| `rcim_retuned_ERT19_Bw` | `ERT` | 0.003551 | 0.004161 | 7.269 | 13.187 |
| `rcim_retuned_RF19_Bw` | `RF` | 0.003649 | 0.004256 | 7.543 | 15.083 |
| `paper_retuned_best_Bw` | `best_composite` | 0.003675 | 0.004284 | 7.572 | 15.645 |
| `rcim_retuned_SVM19_Bw` | `SVM` | 0.004016 | 0.004599 | 8.813 | 17.215 |
| `rcim_retuned_DT19_Bw` | `DT` | 0.004578 | 0.005169 | 9.728 | 19.601 |
| `rcim_retuned_HGBM19_Bw` | `HGBM` | 0.004683 | 0.005301 | 9.978 | 17.712 |
| `rcim_retuned_LGBM19_Bw` | `LGBM` | 0.008105 | 0.008655 | 18.057 | 35.748 |
| `rcim_retuned_ELM19_Bw` | `ELM` | 0.008917 | 0.009518 | 20.169 | 51.896 |
| `rcim_retuned_XGBM19_Bw` | `XGBM` | 0.010679 | 0.011209 | 24.184 | 48.082 |
| `rcim_retuned_MLP19_Bw` | `MLP` | 0.019115 | 0.023025 | 44.141 | 88.991 |

### Track 1 Backward Models

| Candidate | Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `SVM19_Bw` | `SVM` | 0.004822 | 0.005116 | 10.864 | 25.533 |
| `track1_best_Bw` | `best_composite` | 0.005027 | 0.005212 | 11.860 | 48.106 |
| `LGBM19_Bw` | `LGBM` | 0.005037 | 0.005231 | 11.880 | 48.106 |
| `GBM19_Bw` | `GBM` | 0.005180 | 0.005363 | 12.252 | 49.984 |
| `DT19_Bw` | `DT` | 0.005226 | 0.005409 | 12.359 | 48.860 |
| `ERT19_Bw` | `ERT` | 0.005258 | 0.005442 | 12.434 | 51.665 |
| `RF19_Bw` | `RF` | 0.005392 | 0.005584 | 12.731 | 55.740 |
| `ET19_Bw` | `ET` | 0.006273 | 0.006520 | 14.314 | 48.624 |
| `HGBM19_Bw` | `HGBM` | 0.006619 | 0.006834 | 15.494 | 53.982 |
| `XGBM19_Bw` | `XGBM` | 0.007991 | 0.008195 | 18.722 | 59.067 |
| `ELM19_Bw` | `ELM` | 0.010071 | 0.010486 | 23.034 | 52.159 |
| `MLP19_Bw` | `MLP` | 0.036681 | 0.044921 | 86.544 | 225.831 |

## Target-Level Metric Snapshot

These target-level rows come from the saved harmonic target model archives.
They are not a replacement for Track 2 curve evaluation, but they explain
how amplitude and phase prediction quality changes before TE reconstruction.

### Forward Target Metrics

#### Original Forward

| Candidate | Family | Amplitude MAE | Amplitude RMSE | Phase MAE [rad] | Phase RMSE [rad] |
| --- | --- | ---: | ---: | ---: | ---: |
| `rcim_original_SVM19_Fw` | `SVM` | 0.011868 | 0.039077 | 0.234102 | 0.550534 |
| `rcim_original_MLP19_Fw` | `MLP` | 0.018172 | 0.040790 | 0.411358 | 0.814420 |
| `rcim_original_RF19_Fw` | `RF` | 0.011731 | 0.039249 | 0.053689 | 0.177040 |
| `rcim_original_DT19_Fw` | `DT` | 0.011725 | 0.039202 | 0.053960 | 0.226815 |
| `rcim_original_ET19_Fw` | `ET` | 0.011735 | 0.039237 | 0.081596 | 0.301460 |
| `rcim_original_ERT19_Fw` | `ERT` | 0.011727 | 0.039243 | 0.039523 | 0.120053 |
| `rcim_original_GBM19_Fw` | `GBM` | 0.011727 | 0.039167 | 0.060889 | 0.159701 |
| `rcim_original_HGBM19_Fw` | `HGBM` | 0.011737 | 0.039239 | 0.102279 | 0.267713 |
| `rcim_original_XGBM19_Fw` | `XGBM` | 0.011786 | 0.039172 | 0.160366 | 0.393788 |
| `rcim_original_LGBM19_Fw` | `LGBM` | 0.011732 | 0.039234 | 0.085129 | 0.222125 |
| `rcim_original_ELM19_Fw` | `ELM` | 0.011984 | 0.039242 | 0.354739 | 0.724576 |

#### Retuned Forward

| Candidate | Family | Amplitude MAE | Amplitude RMSE | Phase MAE [rad] | Phase RMSE [rad] |
| --- | --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_SVM19_Fw` | `SVM` | 0.011834 | 0.039061 | 0.320794 | 0.696698 |
| `rcim_retuned_MLP19_Fw` | `MLP` | 0.017272 | 0.040386 | 0.402765 | 0.809420 |
| `rcim_retuned_RF19_Fw` | `RF` | 0.011727 | 0.039234 | 0.045901 | 0.139376 |
| `rcim_retuned_DT19_Fw` | `DT` | 0.011725 | 0.039202 | 0.053934 | 0.226837 |
| `rcim_retuned_ET19_Fw` | `ET` | 0.011735 | 0.039261 | 0.059229 | 0.262517 |
| `rcim_retuned_ERT19_Fw` | `ERT` | 0.011728 | 0.039236 | 0.048855 | 0.155670 |
| `rcim_retuned_GBM19_Fw` | `GBM` | 0.011708 | 0.039122 | 0.035092 | 0.071053 |
| `rcim_retuned_HGBM19_Fw` | `HGBM` | 0.011728 | 0.039226 | 0.088921 | 0.226194 |
| `rcim_retuned_XGBM19_Fw` | `XGBM` | 0.011786 | 0.039264 | 0.063405 | 0.155224 |
| `rcim_retuned_LGBM19_Fw` | `LGBM` | 0.011729 | 0.039231 | 0.086322 | 0.219852 |
| `rcim_retuned_ELM19_Fw` | `ELM` | 0.011959 | 0.039023 | 0.407448 | 0.792569 |

#### Track 1 Forward

| Candidate | Family | Amplitude MAE | Amplitude RMSE | Phase MAE [rad] | Phase RMSE [rad] |
| --- | --- | ---: | ---: | ---: | ---: |
| `SVM19_Fw` | `SVM` | 0.000441 | 0.001219 | 0.331625 | 0.726009 |
| `MLP19_Fw` | `MLP` | 0.015552 | 0.027645 | 0.430603 | 0.825869 |
| `RF19_Fw` | `RF` | 0.000214 | 0.000792 | 0.109391 | 0.345850 |
| `DT19_Fw` | `DT` | 0.000337 | 0.001103 | 0.141690 | 0.323615 |
| `ET19_Fw` | `ET` | 0.000359 | 0.001176 | 0.145092 | 0.340324 |
| `ERT19_Fw` | `ERT` | 0.000221 | 0.000815 | 0.066694 | 0.226815 |
| `GBM19_Fw` | `GBM` | 0.000303 | 0.001004 | 0.098410 | 0.240849 |
| `HGBM19_Fw` | `HGBM` | 0.000368 | 0.001172 | 0.200468 | 0.511179 |
| `XGBM19_Fw` | `XGBM` | 0.000507 | 0.001612 | 0.245260 | 0.560530 |
| `LGBM19_Fw` | `LGBM` | 0.000799 | 0.002521 | 0.302995 | 0.630958 |
| `ELM19_Fw` | `ELM` | 0.000940 | 0.002781 | 0.409441 | 0.798600 |

### Backward Target Metrics

#### Retuned Backward

| Candidate | Family | Amplitude MAE | Amplitude RMSE | Phase MAE [rad] | Phase RMSE [rad] |
| --- | --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_SVM19_Bw` | `SVM` | 0.000768 | 0.002965 | 1.488595 | 1.781093 |
| `rcim_retuned_MLP19_Bw` | `MLP` | 0.007155 | 0.011597 | 1.529308 | 1.817972 |
| `rcim_retuned_RF19_Bw` | `RF` | 0.000514 | 0.002857 | 1.475540 | 1.785935 |
| `rcim_retuned_DT19_Bw` | `DT` | 0.000633 | 0.002965 | 1.452520 | 1.767879 |
| `rcim_retuned_ET19_Bw` | `ET` | 0.000496 | 0.002945 | 1.440638 | 1.759632 |
| `rcim_retuned_ERT19_Bw` | `ERT` | 0.000492 | 0.002845 | 1.460274 | 1.770953 |
| `rcim_retuned_GBM19_Bw` | `GBM` | 0.000341 | 0.002871 | 1.445237 | 1.765765 |
| `rcim_retuned_HGBM19_Bw` | `HGBM` | 0.000618 | 0.002618 | 1.521388 | 1.811502 |
| `rcim_retuned_XGBM19_Bw` | `XGBM` | 0.001046 | 0.003258 | 1.611533 | 1.905869 |
| `rcim_retuned_LGBM19_Bw` | `LGBM` | 0.000836 | 0.002735 | 1.581513 | 1.864699 |
| `rcim_retuned_ELM19_Bw` | `ELM` | 0.001359 | 0.004468 | 1.539331 | 1.814290 |

#### Track 1 Backward

| Candidate | Family | Amplitude MAE | Amplitude RMSE | Phase MAE [rad] | Phase RMSE [rad] |
| --- | --- | ---: | ---: | ---: | ---: |
| `SVM19_Bw` | `SVM` | 0.000702 | 0.002429 | 0.382816 | 0.770788 |
| `MLP19_Bw` | `MLP` | 0.015144 | 0.025982 | 0.443511 | 0.802302 |
| `RF19_Bw` | `RF` | 0.000262 | 0.000854 | 0.083762 | 0.263375 |
| `DT19_Bw` | `DT` | 0.000238 | 0.000981 | 0.044574 | 0.156414 |
| `ET19_Bw` | `ET` | 0.000415 | 0.001527 | 0.148151 | 0.371412 |
| `ERT19_Bw` | `ERT` | 0.000237 | 0.000838 | 0.062821 | 0.212855 |
| `GBM19_Bw` | `GBM` | 0.000234 | 0.000827 | 0.073542 | 0.230040 |
| `HGBM19_Bw` | `HGBM` | 0.000419 | 0.001261 | 0.167781 | 0.420890 |
| `XGBM19_Bw` | `XGBM` | 0.000587 | 0.001789 | 0.215728 | 0.471334 |
| `LGBM19_Bw` | `LGBM` | 0.000231 | 0.000804 | 0.096080 | 0.248383 |
| `ELM19_Bw` | `ELM` | 0.001080 | 0.003271 | 0.452833 | 0.845089 |

## Interpretation By Archive

| Archive | Coverage | Interpretation |
| --- | --- | --- |
| `rcim_original` | forward only | Recovered original-pipeline reference. It remains the correct baseline for paper-original forward behavior and ONNX parity context. |
| `rcim_retuned` | forward and backward | Best current paper-reference curve performer in this comparison; it reflects repository retuning rather than exact original-paper hyperparameter behavior. |
| `rcim_track1` | forward and backward | Closed faithful full-dataset Track 1 archive. It is the most complete paper-reference family bank but is not the lowest-error Track 2 archive in this validation. |

## Final Conclusion

The repository `models/paper_reference` surface is coherent and usable as a
three-baseline system rather than a single interchangeable model bank.
`rcim_original` and `rcim_retuned` forward are broadly analogous but not
identical. `rcim_track1` is substantially different from both on the Track 2
curve surface, especially in backward where every family differs
substantially from the retuned counterpart under the selected thresholds.

The defensible wording is:

> `rcim_original` preserves the recovered forward original-pipeline baseline;
> `rcim_retuned` provides the strongest current paper-reference Track 2 curve
> metrics; and `rcim_track1` provides the final faithful full-dataset
> Track 1 family archive for both directions.

This report should be used together with the canonical Track 2 matrix when
choosing which paper-reference archive to cite in downstream comparisons.
