# Exact RCIM Paper Model-Bank Validation Report

## Overview

This report summarizes one repository-owned validation run of the
exact paper-faithful RCIM family bank reconstructed from the recovered
paper assets.

- model family: `paper_reimplementation_rcim_exact_model_bank`;
- model type: `exact_paper_family_bank`;
- run name: `exact_open_cell_phase_gap_bridge`;
- output run name: `exact_open_cell_phase_gap_bridge_campaign_run`;
- run instance id: `2026-04-13-22-09-07__exact_open_cell_phase_gap_bridge_campaign_run`;
- source dataframe: `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`;
- enabled families: `RF, ERT, GBM, HGBM, LGBM`;

## Dataset Scope

- filtered row count: `969`;
- feature schema: `rpm, deg, tor`;
- target count: `20`;
- train rows: `775`;
- test rows: `194`;
- maximum `deg` filter: `35.0`;

## Winner Summary

- winning family: `RF`;
- winning estimator: `RandomForestRegressor`;
- winning mean component MAPE: `18.369%`;
- winning mean component MAE: `0.056284`;
- winning mean component RMSE: `0.144839`;

## Family Ranking

| Rank | Family | Estimator | Mean Component MAPE [%] | Mean Component MAE | Mean Component RMSE |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `RF` | `RandomForestRegressor` | 18.369 | 0.056284 | 0.144839 |
| 2 | `HGBM` | `HistGradientBoostingRegressor` | 20.586 | 0.079797 | 0.155340 |
| 3 | `ERT` | `ExtraTreesRegressor` | 21.017 | 0.054424 | 0.139747 |
| 4 | `GBM` | `GradientBoostingRegressor` | 24.343 | 0.062593 | 0.152818 |
| 5 | `LGBM` | `LGBMRegressor` | 32.598 | 0.077943 | 0.155869 |

## Target-Winner Registry

| Target | Winning Family | Estimator | MAPE [%] | MAE | RMSE |
| --- | --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | `HistGradientBoostingRegressor` | 10.804 | 0.002505 | 0.003699 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | `HistGradientBoostingRegressor` | 0.148 | 0.000025 | 0.000035 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | `HistGradientBoostingRegressor` | 2.321 | 0.000018 | 0.000026 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | `HistGradientBoostingRegressor` | 2.124 | 0.000023 | 0.000032 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | `RandomForestRegressor` | 2.778 | 0.000022 | 0.000033 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | `HistGradientBoostingRegressor` | 8.314 | 0.000025 | 0.000038 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | `ExtraTreesRegressor` | 3.430 | 0.000011 | 0.000019 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | `ExtraTreesRegressor` | 12.812 | 0.000035 | 0.000105 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | `ExtraTreesRegressor` | 7.838 | 0.000045 | 0.000144 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | `ExtraTreesRegressor` | 10.537 | 0.000038 | 0.000072 |
| `fft_y_Fw_filtered_phase_0` | `ERT` | `ExtraTreesRegressor` | 0.000 | 0.000000 | 0.000000 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | `HistGradientBoostingRegressor` | 21.061 | 0.001846 | 0.002563 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | `GradientBoostingRegressor` | 1.323 | 0.023757 | 0.034316 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | `HistGradientBoostingRegressor` | 1.628 | 0.020390 | 0.032648 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | `ExtraTreesRegressor` | 48.272 | 0.034522 | 0.054119 |
| `fft_y_Fw_filtered_phase_78` | `RF` | `RandomForestRegressor` | 74.433 | 0.051585 | 0.125012 |
| `fft_y_Fw_filtered_phase_81` | `RF` | `RandomForestRegressor` | 4.324 | 0.047979 | 0.068145 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | `LGBMRegressor` | 56.378 | 0.609151 | 1.054014 |
| `fft_y_Fw_filtered_phase_162` | `RF` | `RandomForestRegressor` | 10.098 | 0.230457 | 0.747172 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | `ExtraTreesRegressor` | 19.890 | 0.269941 | 0.757287 |

## Paper-Target Comparison

This section serializes the current `paper vs repository` comparison
for each exact-paper target at the family-direction level. The stricter
numeric table replication is reported in the canonical table sections
below.

| Target | Paper Expected Family | Repository Winner | Repo MAPE [%] | Family Direction Status |
| --- | --- | --- | ---: | --- |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | `HGBM` | 10.804 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_0` | `SVR` | `ERT` | 0.000 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_1` | `RF / LGBM` | `HGBM` | 0.148 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_1` | `RF / LGBM` | `HGBM` | 21.061 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | `HGBM` | 2.321 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | `GBM` | 1.323 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | `HGBM` | 2.124 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | `HGBM` | 1.628 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_40` | `ERT / GBM` | `RF` | 2.778 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_40` | `ERT / GBM` | `ERT` | 48.272 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_78` | `HGBM / RF` | `HGBM` | 8.314 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_78` | `HGBM / RF` | `RF` | 74.433 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_81` | `RF` | `ERT` | 3.430 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_81` | `RF` | `RF` | 4.324 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_156` | `ERT / RF` | `ERT` | 12.812 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_156` | `ERT / RF` | `LGBM` | 56.378 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | `ERT` | 7.838 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_162` | `ERT` | `RF` | 10.098 | `not_matched_expected_family_direction` |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | `ERT` | 10.537 | `matched_expected_family_direction` |
| `fft_y_Fw_filtered_phase_240` | `ERT` | `ERT` | 19.890 | `matched_expected_family_direction` |

## Paper-Harmonic Comparison

This section collapses the amplitude and phase target evidence into one
harmonic-facing status so `Track 1` closure can later be tied to a
single inspectable harmonic table.

| Harmonic | Paper Expected Family | Ampl Winner | Phase Winner | Matching Targets | Harmonic Status |
| ---: | --- | --- | --- | ---: | --- |
| `0` | `SVR` | `HGBM` | `ERT` | 0/2 | `no_family_direction_match` |
| `1` | `RF / LGBM` | `HGBM` | `HGBM` | 0/2 | `no_family_direction_match` |
| `3` | `HGBM` | `HGBM` | `GBM` | 1/2 | `partial_family_direction_match` |
| `39` | `HGBM` | `HGBM` | `HGBM` | 2/2 | `full_family_direction_match` |
| `40` | `ERT / GBM` | `RF` | `ERT` | 1/2 | `partial_family_direction_match` |
| `78` | `HGBM / RF` | `HGBM` | `RF` | 2/2 | `full_family_direction_match` |
| `81` | `RF` | `ERT` | `RF` | 1/2 | `partial_family_direction_match` |
| `156` | `ERT / RF` | `ERT` | `LGBM` | 1/2 | `partial_family_direction_match` |
| `162` | `ERT` | `ERT` | `RF` | 1/2 | `partial_family_direction_match` |
| `240` | `ERT` | `ERT` | `ERT` | 2/2 | `full_family_direction_match` |

## Canonical Table 3 Comparison

This table mirrors paper Table 3 for amplitude RMSE and adds the
repository best-achieved RMSE per harmonic together with the remaining
numeric gap against the paper target.

| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003300 | 7.40e-05 | 1.80e-04 | 1.80e-04 | 9.50e-05 | 3.30e-04 | 1.00e-04 | 8.80e-04 | 0.002200 | 4.70e-04 |
| `MLP` | 0.0140 | 0.0120 | 0.0120 | 0.0100 | 0.0140 | 0.0130 | 0.0150 | 0.0130 | 0.0160 | 0.0100 |
| `RF` | 0.004100 | 3.50e-05 | 3.00e-05 | 3.80e-05 | 3.70e-05 | 5.60e-05 | 1.50e-05 | 1.70e-04 | 2.20e-04 | 5.40e-05 |
| `DT` | 0.004900 | 4.00e-05 | 3.30e-05 | 5.30e-05 | 4.50e-05 | 8.20e-05 | 1.80e-05 | 2.00e-04 | 1.70e-04 | 1.10e-04 |
| `ET` | 0.004500 | 4.20e-05 | 3.50e-05 | 5.10e-05 | 4.30e-05 | 8.50e-05 | 2.70e-05 | 1.90e-04 | 3.80e-04 | 1.80e-04 |
| `ERT` | 0.004000 | 3.70e-05 | 3.40e-05 | 4.00e-05 | 3.60e-05 | 5.70e-05 | 1.60e-05 | 1.30e-04 | 1.60e-04 | 4.20e-05 |
| `GBM` | 0.004000 | 3.60e-05 | 3.10e-05 | 3.90e-05 | 3.90e-05 | 5.50e-05 | 1.60e-05 | 1.70e-04 | 2.20e-04 | 4.70e-05 |
| `HGBM` | 0.003400 | 3.60e-05 | 2.50e-05 | 3.20e-05 | 3.80e-05 | 4.50e-05 | 1.60e-05 | 2.50e-04 | 5.00e-04 | 7.40e-05 |
| `XGBM` | 0.003500 | 7.10e-05 | 1.00e-04 | 1.30e-04 | 8.70e-05 | 1.50e-04 | 6.00e-05 | 5.40e-04 | 7.50e-04 | 2.10e-04 |
| `LGBM` | 0.003500 | 3.70e-05 | 2.60e-05 | 3.30e-05 | 3.80e-05 | 4.60e-05 | 1.60e-05 | 2.20e-04 | 4.70e-04 | 6.20e-05 |
| `Repo Best Family` | `HGBM` | `HGBM` | `HGBM` | `HGBM` | `RF` | `LGBM` | `RF` | `ERT` | `ERT` | `RF` |
| `Repo Best RMSE` | 0.003699 | 3.52e-05 | 2.57e-05 | 3.17e-05 | 3.28e-05 | 3.57e-05 | 1.82e-05 | 1.05e-04 | 1.44e-04 | 5.47e-05 |
| `Paper Best Family` | `SVM` | `RF` | `HGBM` | `HGBM` | `ERT` | `HGBM` | `RF` | `ERT` | `ERT` | `ERT` |
| `Paper Target RMSE` | 0.003300 | 3.50e-05 | 2.50e-05 | 3.20e-05 | 3.60e-05 | 4.50e-05 | 1.50e-05 | 1.30e-04 | 1.60e-04 | 4.20e-05 |
| `Gap Vs Paper` | 3.99e-04 | 1.76e-07 | 7.42e-07 | -3.47e-07 | -3.24e-06 | -9.30e-06 | 3.22e-06 | -2.46e-05 | -1.64e-05 | 1.27e-05 |
| `Status` | `above_paper_target` | `above_paper_target` | `above_paper_target` | `met_paper_target` | `met_paper_target` | `met_paper_target` | `above_paper_target` | `met_paper_target` | `met_paper_target` | `above_paper_target` |

## Canonical Table 4 Comparison

This table mirrors paper Table 4 for phase MAE and adds the repository
best-achieved MAE per harmonic together with the remaining numeric gap
against the paper target.

| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002200 | 0.0330 | 0.0270 | 0.0610 | 0.1900 | 0.1300 | 1.200 | 0.4900 | 0.4900 |
| `MLP` | 0.007200 | 0.0650 | 0.0620 | 0.0800 | 0.1600 | 0.1500 | 1.900 | 0.7800 | 0.7000 |
| `RF` | 0.002000 | 0.0240 | 0.0280 | 0.0370 | 0.0740 | 0.0530 | 0.5100 | 0.2300 | 0.2500 |
| `DT` | 0.002100 | 0.0300 | 0.0360 | 0.0430 | 0.0900 | 0.0660 | 0.5200 | 0.2000 | 0.2300 |
| `ET` | 0.002400 | 0.0310 | 0.0350 | 0.0510 | 0.0940 | 0.0870 | 0.7100 | 0.2800 | 0.2600 |
| `ERT` | 0.002200 | 0.0270 | 0.0280 | 0.0400 | 0.0760 | 0.0560 | 0.5300 | 0.2000 | 0.2300 |
| `GBM` | 0.002000 | 0.0240 | 0.0300 | 0.0360 | 0.0740 | 0.0530 | 0.5400 | 0.2500 | 0.2900 |
| `HGBM` | 0.001900 | 0.0200 | 0.0210 | 0.0400 | 0.0910 | 0.0570 | 0.7400 | 0.3500 | 0.3600 |
| `XGBM` | 0.001900 | 0.0240 | 0.0320 | 0.0610 | 0.1400 | 0.0910 | 0.9600 | 0.5400 | 0.3900 |
| `LGBM` | 0.001800 | 0.0210 | 0.0210 | 0.0400 | 0.0950 | 0.0550 | 0.7400 | 0.3500 | 0.3400 |
| `Repo Best Family` | `HGBM` | `GBM` | `LGBM` | `ERT` | `RF` | `LGBM` | `ERT` | `ERT` | `ERT` |
| `Repo Best MAE` | 0.001846 | 0.0238 | 0.0204 | 0.0345 | 0.0516 | 0.0475 | 0.3967 | 0.2125 | 0.2699 |
| `Paper Best Family` | `LGBM` | `HGBM` | `HGBM` | `GBM` | `GBM` | `GBM` | `RF` | `DT` | `DT` |
| `Paper Target MAE` | 0.001800 | 0.0200 | 0.0210 | 0.0360 | 0.0740 | 0.0530 | 0.5100 | 0.2000 | 0.2300 |
| `Gap Vs Paper` | 4.64e-05 | 0.003757 | -6.25e-04 | -0.001478 | -0.0224 | -0.005526 | -0.1133 | 0.0125 | 0.0399 |
| `Status` | `above_paper_target` | `above_paper_target` | `met_paper_target` | `met_paper_target` | `met_paper_target` | `met_paper_target` | `met_paper_target` | `above_paper_target` | `above_paper_target` |

## Canonical Table 5 Comparison

This table mirrors paper Table 5 for phase RMSE and adds the repository
best-achieved RMSE per harmonic together with the remaining numeric gap
against the paper target.

| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003100 | 0.0420 | 0.0440 | 0.0970 | 0.3200 | 0.2000 | 1.800 | 1.100 | 1.100 |
| `MLP` | 0.0130 | 0.0840 | 0.0770 | 0.1100 | 0.2400 | 0.2200 | 2.200 | 1.200 | 1.100 |
| `RF` | 0.002800 | 0.0330 | 0.0430 | 0.0550 | 0.1600 | 0.0820 | 1.200 | 0.6800 | 0.6300 |
| `DT` | 0.002800 | 0.0420 | 0.0610 | 0.0610 | 0.2000 | 0.1000 | 1.300 | 0.7300 | 0.6700 |
| `ET` | 0.003300 | 0.0460 | 0.0620 | 0.0740 | 0.2300 | 0.1500 | 1.500 | 0.9300 | 0.6800 |
| `ERT` | 0.003600 | 0.0400 | 0.0440 | 0.0600 | 0.1800 | 0.1100 | 1.200 | 0.6400 | 0.5800 |
| `GBM` | 0.002600 | 0.0340 | 0.0450 | 0.0550 | 0.1800 | 0.0840 | 1.300 | 0.7100 | 0.7100 |
| `HGBM` | 0.002500 | 0.0290 | 0.0270 | 0.0600 | 0.1900 | 0.0850 | 1.300 | 0.7000 | 0.7400 |
| `XGBM` | 0.002800 | 0.0330 | 0.0430 | 0.0890 | 0.2300 | 0.1300 | 1.400 | 0.8100 | 0.7600 |
| `LGBM` | 0.002500 | 0.0300 | 0.0280 | 0.0600 | 0.1900 | 0.0820 | 1.300 | 0.7000 | 0.7100 |
| `Repo Best Family` | `GBM` | `HGBM` | `HGBM` | `ERT` | `RF` | `RF` | `ERT` | `ERT` | `ERT` |
| `Repo Best RMSE` | 0.002510 | 0.0343 | 0.0326 | 0.0541 | 0.1250 | 0.0681 | 0.9129 | 0.7186 | 0.7573 |
| `Paper Best Family` | `HGBM` | `HGBM` | `HGBM` | `GBM` | `RF` | `LGBM` | `ERT` | `ERT` | `ERT` |
| `Paper Target RMSE` | 0.002500 | 0.0290 | 0.0270 | 0.0550 | 0.1600 | 0.0820 | 1.200 | 0.6400 | 0.5800 |
| `Gap Vs Paper` | 1.01e-05 | 0.005302 | 0.005648 | -8.81e-04 | -0.0350 | -0.0139 | -0.2871 | 0.0786 | 0.1773 |
| `Status` | `above_paper_target` | `above_paper_target` | `above_paper_target` | `met_paper_target` | `met_paper_target` | `met_paper_target` | `met_paper_target` | `above_paper_target` | `above_paper_target` |

## Canonical Table 6 Comparison

This table compares the paper-selected top-performing models from Table 6
against the repository best families measured on the current exact-paper
validation split.

| `k` | Paper `A*_k` | Repo Best Ampl RMSE Family | Ampl RMSE Status | Paper `phi*_k` | Repo Best Phase MAE Family | Repo Best Phase RMSE Family | Phase MAE Status | Phase RMSE Status | Harmonic Status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `SVM` | `HGBM` | `above_paper_target` | `-` | `ERT` | `ERT` | `not_applicable` | `not_applicable` | `not_yet_matched_tables_3_6` |
| `1` | `RF` | `HGBM` | `above_paper_target` | `LGBM` | `HGBM` | `GBM` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` |
| `3` | `HGBM` | `HGBM` | `above_paper_target` | `HGBM` | `GBM` | `HGBM` | `above_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` |
| `39` | `HGBM` | `HGBM` | `met_paper_target` | `HGBM` | `LGBM` | `HGBM` | `met_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` |
| `40` | `ERT` | `RF` | `met_paper_target` | `GBM` | `ERT` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `78` | `HGBM` | `LGBM` | `met_paper_target` | `RF` | `RF` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `81` | `RF` | `RF` | `above_paper_target` | `RF` | `LGBM` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `156` | `ERT` | `ERT` | `met_paper_target` | `RF` | `ERT` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `162` | `ERT` | `ERT` | `met_paper_target` | `ERT` | `ERT` | `ERT` | `above_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` |
| `240` | `ERT` | `RF` | `above_paper_target` | `ERT` | `ERT` | `ERT` | `above_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` |

## ONNX Export Surface

- export enabled: `True`;
- export root: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-13-22-09-07__exact_open_cell_phase_gap_bridge_campaign_run/onnx_export`;
- exported file count: `100`;
- export failure mode: `strict`;
- recovered reference file count: `201`;
- matched relative paths: `0`;
- missing against recovered reference: `201`;
- extra exported relative paths: `100`;
- failed exports: `0`;
- surrogate exports: `0`;

## Runtime Dependencies

| Dependency | Version |
| --- | --- |
| `numpy` | `2.3.5` |
| `pandas` | `2.3.3` |
| `scikit-learn` | `1.8.0` |
| `skl2onnx` | `1.20.0` |
| `onnxmltools` | `1.16.0` |
| `xgboost` | `3.2.0` |
| `lightgbm` | `4.6.0` |

## Interpretation

This validation run is the strict paper-faithful branch of `Track 1`.
Its role is to reproduce the original RCIM family bank with the exact
recovered input schema, target schema, and export surface before any
repository-specific simplification or target-wise winner assembly.

At the current repository state, the workflow now serializes the numeric
targets from paper Tables 3, 4, 5, and the selected-model targets from
Table 6. The repository can therefore show both the paper thresholds and
the current exact-paper results side by side. `Track 1` still remains
open until those gaps are actually closed on the repository side.
