# RCIM Original ONNX Release Parity Validation

## Overview

This report compares the recovered original ONNX release against the
current repository `rcim_original` forward archives using the same
forward evaluation surfaces.

## Manifest Status

- ONNX release root: `reference\rcim_ml_compensation_recovered_assets\models\exact_onnx_paper_release`;
- repo original archive root: `models\paper_reference\rcim_original\forward`;
- exact-paper source dataframe: `reference\rcim_ml_compensation_recovered_assets\code\original_pipeline\dataFrame_prediction_Fw_v14_newFreq.csv`;
- ONNX file count: `201`;
- resolved target model count: `200`;
- expected target model count: `200`;
- duplicate target keys: `1`;
- missing target keys: `0`.

## Tables 2-5 Split Parity

| Family | Targets | ONNX Mean MAE | Repo Mean MAE | ONNX Mean RMSE | Repo Mean RMSE | Max Prediction Delta | Mean Prediction Delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVR` | 15 | 0.178738 | 0.178739 | 0.326755 | 0.326760 | 0.001069 | 0.000188 |
| `MLP` | 20 | 0.208097 | 0.221410 | 0.288685 | 0.294545 | 1.950384 | 0.078916 |
| `RF` | 20 | 0.024802 | 0.024382 | 0.066736 | 0.066732 | 0.892174 | 0.006881 |
| `DT` | 20 | 0.024938 | 0.024938 | 0.076923 | 0.076923 | 0.000000 | 0.000000 |
| `ET` | 20 | 0.040166 | 0.040166 | 0.110175 | 0.110175 | 0.000000 | 0.000000 |
| `ERT` | 20 | 0.015060 | 0.015060 | 0.044176 | 0.044176 | 0.000002 | 0.000000 |
| `GBM` | 20 | 0.029730 | 0.029730 | 0.074675 | 0.074675 | 0.000001 | 0.000000 |
| `HGBM` | 20 | 0.050058 | 0.050058 | 0.099923 | 0.099923 | 0.000002 | 0.000000 |
| `XGBM` | 4 | 0.000043 | 0.000041 | 0.000056 | 0.000053 | 0.000010 | 0.000010 |
| `LGBM` | 20 | 0.040953 | 0.040953 | 0.084579 | 0.084579 | 0.000001 | 0.000000 |

## TE Curve Verification Pipeline Forward Curve Parity

| Family | ONNX MAE [deg] | Repo MAE [deg] | Delta MAE [deg] | ONNX MPE [%] | Repo MPE [%] | Delta MPE [%] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `MLP` | 0.024962 | 0.018754 | 0.006208 | 56.844 | 42.943 | 13.901 |
| `RF` | 0.001764 | 0.001767 | -0.000003 | 3.936 | 3.940 | -0.004 |
| `DT` | 0.001919 | 0.001919 | 0.000000 | 4.306 | 4.306 | 0.000 |
| `ET` | 0.002232 | 0.002232 | 0.000000 | 4.985 | 4.985 | 0.000 |
| `ERT` | 0.001471 | 0.001471 | 0.000000 | 3.253 | 3.253 | 0.000 |
| `GBM` | 0.001921 | 0.001921 | -0.000000 | 4.312 | 4.312 | -0.000 |
| `HGBM` | 0.002011 | 0.002011 | 0.000000 | 4.493 | 4.493 | 0.000 |
| `LGBM` | 0.001801 | 0.001801 | 0.000000 | 4.017 | 4.017 | 0.000 |

## TE Curve Verification Pipeline Mean-Centered Offset Diagnostics

| Source | Family | Raw MAE [deg] | Centered MAE [deg] | Mean Abs Offset [deg] | MAE Improvement [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| ONNX | `MLP` | 0.024962 | 0.018080 | 0.016988 | 25.840 |
| ONNX | `RF` | 0.001764 | 0.000836 | 0.001491 | 45.763 |
| ONNX | `DT` | 0.001919 | 0.000834 | 0.001590 | 43.248 |
| ONNX | `ET` | 0.002232 | 0.000896 | 0.001880 | 46.431 |
| ONNX | `ERT` | 0.001471 | 0.000831 | 0.001138 | 38.590 |
| ONNX | `GBM` | 0.001921 | 0.000834 | 0.001672 | 49.071 |
| ONNX | `HGBM` | 0.002011 | 0.000859 | 0.001737 | 45.865 |
| ONNX | `LGBM` | 0.001801 | 0.000846 | 0.001487 | 40.791 |
| Repo | `MLP` | 0.018754 | 0.015515 | 0.009760 | 16.461 |
| Repo | `RF` | 0.001767 | 0.000837 | 0.001502 | 45.874 |
| Repo | `DT` | 0.001919 | 0.000834 | 0.001590 | 43.248 |
| Repo | `ET` | 0.002232 | 0.000896 | 0.001880 | 46.431 |
| Repo | `ERT` | 0.001471 | 0.000831 | 0.001138 | 38.590 |
| Repo | `GBM` | 0.001921 | 0.000834 | 0.001672 | 49.071 |
| Repo | `HGBM` | 0.002011 | 0.000859 | 0.001737 | 45.865 |
| Repo | `XGBM` | 0.002594 | 0.000937 | 0.002368 | 55.993 |
| Repo | `LGBM` | 0.001801 | 0.000846 | 0.001487 | 40.791 |

## Artifacts

- validation summary: `output\validation_checks\rcim_original_onnx_release_parity\2026-06-04-23-41-54__original_onnx_release_track2_offset_diagnostic_2026_06_04\validation_summary.yaml`;
- target parity CSV: `output\validation_checks\rcim_original_onnx_release_parity\2026-06-04-23-41-54__original_onnx_release_track2_offset_diagnostic_2026_06_04\tables_2_5_target_parity.csv`;
- TE Curve Verification Pipeline offset diagnostics CSV: `output\validation_checks\rcim_original_onnx_release_parity\2026-06-04-23-41-54__original_onnx_release_track2_offset_diagnostic_2026_06_04\track2_curve_offset_diagnostics.csv`.

## Failures

Raw ONNX Runtime messages are preserved in the validation YAML.

| Stage | Family | Error Type | Count |
| --- | --- | --- | ---: |
| `tables_2_5` | `SVR` | `Fail` | 5 |
| `tables_2_5` | `XGBM` | `RuntimeException` | 16 |
| `track2` | `SVR` | `Fail` | 1 |
| `track2` | `XGBM` | `RuntimeException` | 1 |
