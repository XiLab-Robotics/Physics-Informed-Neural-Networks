# TE Curve Verification Pipeline Original ONNX Offset Diagnostic

## Executive Verdict

The recovered original RCIM paper ONNX models do show the same forward
`TE Curve Verification Pipeline` offset pattern seen in the repository `rcim_original/forward` Python
archive for the executable tree and boosting families.

This is the important result: for `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, and
`LGBM`, the ONNX release and repository Python archive have matching raw
`TE Curve Verification Pipeline` curve errors and matching mean-centered improvements. Therefore the
mean-offset behavior is not introduced by the repository pickle archive or by
the Python archive loader. It is already present when the recovered original
ONNX release is evaluated through the same `TE Curve Verification Pipeline` harmonic reconstruction
path.

`MLP` remains a known ONNX-release discrepancy: it runs, but it does not match
the repository archive. `SVR` and `XGBM` remain incomplete under ONNX Runtime
and cannot provide full-family `TE Curve Verification Pipeline` offset evidence.

## Diagnostic Artifacts

| Artifact | Path |
| --- | --- |
| Generated validation report | `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/2026-06-04-23-41-54_original_onnx_release_track2_offset_diagnostic_2026_06_04_report.md` |
| Validation summary YAML | `output/validation_checks/rcim_original_onnx_release_parity/2026-06-04-23-41-54__original_onnx_release_track2_offset_diagnostic_2026_06_04/validation_summary.yaml` |
| Tables 2-5 target parity CSV | `output/validation_checks/rcim_original_onnx_release_parity/2026-06-04-23-41-54__original_onnx_release_track2_offset_diagnostic_2026_06_04/tables_2_5_target_parity.csv` |
| TE Curve Verification Pipeline offset diagnostics CSV | `output/validation_checks/rcim_original_onnx_release_parity/2026-06-04-23-41-54__original_onnx_release_track2_offset_diagnostic_2026_06_04/track2_curve_offset_diagnostics.csv` |
| Runner | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_original_onnx_release_parity_validation.py` |

## What Changed In The Runner

The existing original ONNX parity runner already loaded the recovered paper
ONNX release and evaluated it through `TE Curve Verification Pipeline` forward reconstruction. The
new diagnostic preserves that behavior and adds offset-specific outputs:

- per-curve raw `TE Curve Verification Pipeline` metrics;
- measured curve mean;
- predicted curve mean;
- signed offset error;
- absolute offset error;
- mean-centered MAE and RMSE;
- raw-to-centered MAE improvement.

The new per-curve CSV is:

```text
output/validation_checks/rcim_original_onnx_release_parity/2026-06-04-23-41-54__original_onnx_release_track2_offset_diagnostic_2026_06_04/track2_curve_offset_diagnostics.csv
```

It contains `97` forward curves per executable family/source pair.

## TE Curve Verification Pipeline Forward Raw Parity

These values come from the generated validation report.

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

For the validated tree and boosting families, the ONNX release and repository
archive are effectively identical in `TE Curve Verification Pipeline` raw curve reconstruction.

## Mean-Centered Offset Result

These values also come from the generated validation report.

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

For `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, and `LGBM`, the ONNX and repository
rows are the same to practical precision. The offset pattern is therefore
upstream of the repository Python archive representation.

## Interpretation

The result supports this conclusion:

> The forward original-paper executable ONNX surface already carries the same
> `TE Curve Verification Pipeline` mean-offset behavior observed in the repository
> `rcim_original/forward` archive. The offset is not introduced by the
> repository pickle archive, registry loader, or Python-side reference-bank
> reconstruction wrapper.

This does not mean the original paper models are wrong. It means that when
their amplitude and phase predictions are reconstructed against the repository
held-out TE curves, a meaningful part of the raw error is a per-curve mean/DC
offset. The same behavior appears in the recovered original ONNX release and in
the repository archive derived from that release/workflow.

## Impact On The CVP 1.1 Through Wave 3.1 Investigation

The diagnostic narrows the likely source of the investigated error:

- It is not specific to the repository Python archive.
- It is not created by replacing ONNX inference with pickle inference.
- It is not created by the new mean-centered diagnostic report.
- It is already visible in the original ONNX release when passed through
  canonical `TE Curve Verification Pipeline` forward reconstruction.

The remaining likely explanations are therefore in the modeling and data
interface layer:

- original paper target convention for the `h0` or DC term;
- difference between paper-original training/evaluation zeroing and repository
  held-out curve zeroing;
- inherent offset bias in the original paper target models;
- mismatch between recovered paper feature/target semantics and the repository
  `TE Curve Verification Pipeline` curve truth surface.

The phase/sign convention is less likely to be the primary explanation for the
offset-only improvement because mean-centering improves the executable tree and
boosting families by roughly `38%` to `49%` while preserving the same curve
shape comparison path.

## ONNX Runtime Limitations

`SVR` and `XGBM` remain incomplete under ONNX Runtime:

| Stage | Family | Error Type | Count |
| --- | --- | --- | ---: |
| `tables_2_5` | `SVR` | `Fail` | 5 |
| `tables_2_5` | `XGBM` | `RuntimeException` | 16 |
| `track2` | `SVR` | `Fail` | 1 |
| `track2` | `XGBM` | `RuntimeException` | 1 |

These are recovered ONNX artifact/runtime limitations, not offset-diagnostic
evidence. `XGBM` remains available in the repository Python archive row, but it
cannot be judged as an ONNX release family in this diagnostic.

## Operational Follow-Up

The next useful check is not another ONNX-vs-pickle parity run. The ONNX
diagnostic already shows that the offset pattern is present before the
repository archive layer.

The next useful checks are:

1. audit the recovered original `h0` target semantics against the repository
   `coefficient_cos_h0` convention;
2. compare per-curve truth mean versus predicted `h0` contribution directly;
3. verify whether the source paper data applied a mean-removal or zeroing step
   before target generation that is not mirrored in repository `TE Curve Verification Pipeline` truth;
4. keep `SVR` and `XGBM` out of full-family ONNX offset conclusions until their
   recovered ONNX runtime failures are resolved.
