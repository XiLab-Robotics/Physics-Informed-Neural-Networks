# TE Curve Verification Pipeline Original ONNX Forward Collage Report

## Overview

This report evaluates only the recovered paper-original forward `ONNX`
model bank for `paper_original_best_Fw`. The curve prediction is rebuilt
directly from the `19` original target models under
`reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`.

## Loaded ONNX Targets

The table lists the original release filenames loaded for the `19`
paper-best forward targets. Full original `ONNX` paths are kept in
the validation summary YAML.

| Target | Harmonic | Family | Original ONNX Files |
| --- | ---: | --- | --- |
| `amplitude` | `A0` | `SVR` | `SVR_ampl0.onnx` |
| `amplitude` | `A1` | `RF` | `RandomForestRegressor_ampl1.onnx` |
| `amplitude` | `A3` | `HGBM` | `HistGradientBoostingRegressor_ampl3.onnx` |
| `amplitude` | `A39` | `HGBM` | `HistGradientBoostingRegressor_ampl39.onnx` |
| `amplitude` | `A40` | `ERT` | `ExtraTreesRegressor_ampl40.onnx` |
| `amplitude` | `A78` | `HGBM` | `HistGradientBoostingRegressor_ampl78.onnx` |
| `amplitude` | `A81` | `RF` | `RandomForestRegressor_ampl81.onnx` |
| `amplitude` | `A156` | `ERT` | `ExtraTreesRegressor_ampl156.onnx` |
| `amplitude` | `A162` | `ERT` | `ExtraTreesRegressor_ampl162.onnx` |
| `amplitude` | `A240` | `ERT` | `ExtraTreesRegressor_ampl240.onnx` |
| `phase` | `P1` | `LGBM` | `LGBMRegressor_phase1.onnx` |
| `phase` | `P3` | `HGBM` | `HistGradientBoostingRegressor_phase3.onnx` |
| `phase` | `P39` | `HGBM` | `HistGradientBoostingRegressor_phase39.onnx` |
| `phase` | `P40` | `GBM` | `GradientBoostingRegressor_phase40.onnx` |
| `phase` | `P78` | `RF` | `RandomForestRegressor_phase78.onnx` |
| `phase` | `P81` | `RF` | `RandomForestRegressor_phase81.onnx` |
| `phase` | `P156` | `RF` | `RandomForestRegressor_phase156.onnx` |
| `phase` | `P162` | `ERT` | `ExtraTreesRegressor_phase162.onnx` |
| `phase` | `P240` | `ERT` | `ExtraTreesRegressor_phase240.onnx` |

## TE Curve Verification Pipeline Forward Metrics

| Candidate | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| `paper_original_best_Fw ONNX` | 97 | 0.002804 | 0.002987 | 6.329 | 13.847 |

## Collage

The collage shows four deterministic held-out forward `TE Curve Verification Pipeline` curves
spread across the sorted forward evaluation set.

![paper_original_best_Fw_original_onnx_release curve-verification collage](assets/paper_original_best_fw_original_onnx_release.png)

## Collaged Curves

| Curve | Speed [rpm] | Torque [Nm] | Oil [C] | MAE [deg] | Mean Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| `Curve 1` | 100 | 100 | 25 | 0.004471 | 11.607 |
| `Curve 2` | 1600 | 1500 | 25 | 0.001935 | 3.809 |
| `Curve 3` | 700 | 1400 | 30 | 0.001359 | 3.104 |
| `Curve 4` | 800 | 1800 | 35 | 0.001279 | 2.786 |

## Output Artifacts

- output directory: `output\validation_checks\track2_original_onnx_fw_collage_report\2026-06-08-12-57-36__track2_original_onnx_fw_collage_report`;
- summary YAML: `output\validation_checks\track2_original_onnx_fw_collage_report\2026-06-08-12-57-36__track2_original_onnx_fw_collage_report\track2_original_onnx_fw_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_original_onnx_fw_collage_report\2026-06-08-12-57-36__track2_original_onnx_fw_collage_report\track2_original_onnx_fw_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\track2\original_onnx_fw_collage_report\[2026-06-05]\track2_original_onnx_fw_collage_report.md`.
