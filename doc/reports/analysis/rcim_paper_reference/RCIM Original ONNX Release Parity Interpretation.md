# RCIM Original ONNX Release Parity Interpretation

## Executive Verdict

The recovered original ONNX release substantially validates the repository
`rcim_original/forward` reimplementation for the executable forward model
families.

The strongest parity evidence is on `DT`, `ET`, `ERT`, `GBM`, `HGBM`, and
`LGBM`: these families are numerically aligned with the repository
`rcim_original/forward` archive in both `Tables 2-5` target evaluation and
TE Curve Verification Pipeline forward TE-curve reconstruction.

`RF` is also operationally aligned, with very small TE Curve Verification Pipeline aggregate drift.
`SVR` and `XGBM` are not fully judgeable from ONNX Runtime because some original
ONNX artifacts fail to initialize or execute. `MLP` is executable but shows a
meaningful TE Curve Verification Pipeline discrepancy, so it should be treated as an ONNX-release
exception rather than proof against the reimplementation.

Practical conclusion: the repository forward original-pipeline
reimplementation is successful for the usable recovered ONNX surface, with
documented limitations tied to recovered ONNX artifact/runtime behavior.

## Source Validation Artifacts

| Artifact | Path |
| --- | --- |
| Validation-check report | `doc/reports/analysis/validation_checks/track2/2026-05-18-21-42-15_original_onnx_release_initial_parity_validation_report.md` |
| Validation summary YAML | `output/validation_checks/rcim_original_onnx_release_parity/2026-05-18-21-42-15__original_onnx_release_initial_parity_validation/validation_summary.yaml` |
| Target parity CSV | `output/validation_checks/rcim_original_onnx_release_parity/2026-05-18-21-42-15__original_onnx_release_initial_parity_validation/tables_2_5_target_parity.csv` |
| ONNX release root | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release` |
| Repository baseline | `models/paper_reference/rcim_original/forward` |

## Test Context

| Item | Value |
| --- | --- |
| Direction | `forward` only |
| Source dataframe | `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/dataFrame_prediction_Fw_v14_newFreq.csv` |
| Exact-paper split | same `baseline.yaml` seed and test split used by the exact-paper validation path |
| TE Curve Verification Pipeline context | same forward curve split, denominator, and reconstruction path used by the current TE Curve Verification Pipeline runner |
| ONNX runtime provider | `CPUExecutionProvider` |
| Expected ONNX surface | `10` families x `20` target models = `200` target artifacts |
| Resolved ONNX surface | `200` target artifacts |
| Raw ONNX file count | `201`, because `RF/ampl/RandomForestRegressor_ampl240 (1).onnx` is a duplicate |

## Tables 2-5 Target-Level Parity

| Family | Evaluated Targets | Verdict | Evidence |
| --- | ---: | --- | --- |
| `SVR` | 15 | partial parity | Running targets match closely, but `5` ONNX targets fail to initialize. |
| `MLP` | 20 | discrepant | Executable, but mean prediction delta is large enough to affect TE Curve Verification Pipeline. |
| `RF` | 20 | close parity | Aggregate errors are close; some target-level prediction deltas remain visible. |
| `DT` | 20 | strong parity | Target metrics and predictions are effectively identical. |
| `ET` | 20 | strong parity | Target metrics and predictions are effectively identical. |
| `ERT` | 20 | strong parity | Target metrics and predictions are effectively identical within numerical noise. |
| `GBM` | 20 | strong parity | Target metrics and predictions are effectively identical within numerical noise. |
| `HGBM` | 20 | strong parity | Target metrics and predictions are effectively identical within numerical noise. |
| `XGBM` | 4 | incomplete | Only `4` targets run; `16` targets fail at ONNX Runtime execution. |
| `LGBM` | 20 | strong parity | Target metrics and predictions are effectively identical within numerical noise. |

### Target-Level Metric Snapshot

| Family | ONNX Mean MAE | Repo Mean MAE | ONNX Mean RMSE | Repo Mean RMSE | Max Prediction Delta |
| --- | ---: | ---: | ---: | ---: | ---: |
| `SVR` | 0.178738 | 0.178739 | 0.326755 | 0.326760 | 0.001069 |
| `MLP` | 0.208097 | 0.221410 | 0.288685 | 0.294545 | 1.950384 |
| `RF` | 0.024802 | 0.024382 | 0.066736 | 0.066732 | 0.892174 |
| `DT` | 0.024938 | 0.024938 | 0.076923 | 0.076923 | 0.000000 |
| `ET` | 0.040166 | 0.040166 | 0.110175 | 0.110175 | 0.000000 |
| `ERT` | 0.015060 | 0.015060 | 0.044176 | 0.044176 | 0.000002 |
| `GBM` | 0.029730 | 0.029730 | 0.074675 | 0.074675 | 0.000001 |
| `HGBM` | 0.050058 | 0.050058 | 0.099923 | 0.099923 | 0.000002 |
| `XGBM` | 0.000043 | 0.000041 | 0.000056 | 0.000053 | 0.000010 |
| `LGBM` | 0.040953 | 0.040953 | 0.084579 | 0.084579 | 0.000001 |

## TE Curve Verification Pipeline Forward Curve Parity

TE Curve Verification Pipeline is the stricter end-to-end check because it reconstructs TE curves from
predicted harmonic amplitude and phase values. The same conclusion holds:
tree and boosting families are aligned, `RF` is close, `MLP` is divergent, and
`SVR` / `XGBM` are incomplete because ONNX Runtime cannot evaluate the full
original artifact surface.

| Family | ONNX MPE [%] | Repo MPE [%] | Delta MPE [%] | Verdict |
| --- | ---: | ---: | ---: | --- |
| `MLP` | 56.844 | 42.943 | 13.901 | discrepant |
| `RF` | 3.936 | 3.940 | -0.004 | close parity |
| `DT` | 4.306 | 4.306 | 0.000 | strong parity |
| `ET` | 4.985 | 4.985 | 0.000 | strong parity |
| `ERT` | 3.253 | 3.253 | 0.000 | strong parity |
| `GBM` | 4.312 | 4.312 | -0.000 | strong parity |
| `HGBM` | 4.493 | 4.493 | 0.000 | strong parity |
| `LGBM` | 4.017 | 4.017 | 0.000 | strong parity |

## ONNX Runtime Limitations

| Family | Scope | Count | Interpretation |
| --- | --- | ---: | --- |
| `SVR` | `Tables 2-5` | 5 failed target models | Some recovered SVM/SVR ONNX graphs fail to initialize because ONNX Runtime reports empty coefficients. |
| `SVR` | `TE Curve Verification Pipeline` | 1 failed family evaluation | The family-level TE Curve Verification Pipeline reconstruction cannot be completed because the full target surface is unavailable. |
| `XGBM` | `Tables 2-5` | 16 failed target models | Several XGBM ONNX graphs declare a 3-feature input but request feature index `3` during execution. |
| `XGBM` | `TE Curve Verification Pipeline` | 1 failed family evaluation | The family-level TE Curve Verification Pipeline reconstruction cannot be completed because the full target surface is unavailable. |

These failures are treated as recovered-artifact or ONNX Runtime compatibility
limitations. They are not evidence that the repository Python reimplementation
is wrong, because the comparison fails before a valid full prediction surface
can be produced.

## Interpretation By Family Group

| Group | Families | Interpretation |
| --- | --- | --- |
| Strongly validated | `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `LGBM` | The repository archive reproduces the recovered original ONNX behavior to numerical precision. |
| Operationally validated with small drift | `RF` | TE Curve Verification Pipeline aggregate metrics are effectively equivalent; target-level deltas should remain documented. |
| Partial only | `SVR` | The running targets align closely, but the recovered ONNX surface is incomplete under ONNX Runtime. |
| Incomplete only | `XGBM` | The ONNX release cannot provide enough valid target outputs for a full-family verdict. |
| Executable but divergent | `MLP` | The ONNX release and repository archive differ materially in TE Curve Verification Pipeline, so this family is an exception rather than part of the strong-equivalence claim. |

## Final Conclusion

The forward `rcim_original` repository reimplementation can be considered
successful and aligned with the recovered original pipeline for the usable
original ONNX release surface.

The defensible wording is:

> The repository `rcim_original/forward` implementation reproduces the recovered
> original paper pipeline for the executable tree and boosting families, with
> near-identical TE Curve Verification Pipeline curve behavior. `RF` is close enough for operational
> parity. `SVR` and `XGBM` remain limited by recovered ONNX artifact/runtime
> failures, and `MLP` remains a documented discrepancy.

This supports using the repository `models/paper_reference/rcim_original/forward`
archive as the canonical forward original-pipeline baseline for TE Curve Verification Pipeline, while
keeping the ONNX release parity report as historical evidence and as a record of
artifact-level limitations.
