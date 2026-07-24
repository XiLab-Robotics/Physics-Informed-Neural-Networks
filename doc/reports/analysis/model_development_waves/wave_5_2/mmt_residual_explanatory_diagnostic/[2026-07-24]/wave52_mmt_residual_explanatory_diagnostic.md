# Wave 5.2 MMT Residual-Explanatory Diagnostic

## Overview

This report audits whether the current repository artifacts can support
a leakage-safe fitted test of MMT signatures against baseline residuals.
It does not train a TE model, update a registry, or modify campaign state.

## Decision

Decision: `blocked_by_missing_training_residuals`.

Do not fit an MMT residual-explanation model from the configured
curve-first artifact. It contains held-out test residuals only.
Fitting coefficients on those rows would convert the test surface
into a calibration surface and violate the approved leakage gate.

The MMT path therefore remains diagnostic-only. The next required
artifact is a provenance-matched residual replay for the existing
training and validation curve manifests, generated without changing
the archived baseline models.

## Provenance Audit

- run instance: `2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic`;
- config: `config/analysis/wave52_mmt_residual_explanatory_diagnostic.yaml`;
- residual source: `output/validation_checks/shape_gated_te_curve_reranker/2026-07-21-00-50-05__shape_gated_te_curve_reranker/shape_gated_per_curve_metrics.csv`;
- output directory: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic`;
- resolved baselines: `4`;
- dataset files: `1938`;
- train files: `1356`;
- validation files: `388`;
- test files: `194`;

All four archived baseline inventories, ONNX models, Python
checkpoints, and training-config snapshots resolved successfully.

## Residual Split Coverage

| Residual split | Candidate rows | Fit allowed |
| --- | ---: | --- |
| train | 0 | no rows available |
| validation | 0 | evaluation only |
| test | 388 | evaluation only |

The `194` unique test curves produce `200` forward candidate rows and
`188` backward candidate rows across the four configured baselines
(`388` rows in total). No replacement random split was made.

## Geometry-Locked MMT Signatures

The builder materialized `22` analytical
curve-summary and harmonic signature rows from the repository MMT
equation-chain demonstration.

These signatures are currently fixed across operating conditions.
The paper supports their mechanical interpretation, but the repository
does not yet have a validated speed, torque, or temperature calibration
for the equivalent-error amplitudes. Constant signatures cannot prove
incremental between-condition explanatory value over an intercept.

## Descriptive Test Evidence

The report preserves descriptive summaries of the existing held-out
residual metrics without fitting coefficients. Representative raw and
centered MAE means are:

| Candidate | Raw MAE [deg] | Centered MAE [deg] |
| --- | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Fw` | 0.001837 | 0.001483 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001938 | 0.001490 |
| `polished_setpoints_periodic_gru_sequence_Bw` | 0.002489 | 0.002036 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | 0.002470 | 0.002001 |

## Blockers

- configured residual artifact contains no training residual rows.
- configured residual artifact contains no validation residual rows.
- train-only calibrated equivalent-error signatures are not materialized.
- current geometry-locked MMT signatures are constant across operating conditions.

## Next Action

Prepare a narrow non-training residual replay that runs the four frozen
baseline artifacts over their exact training and validation file
manifests and emits the same per-curve residual schema used here.

After that artifact exists, configure it as the residual source and
rerun the same comparison workflow. Only a held-out improvement over
metadata-only and shuffled controls can justify a later MMT feature
or auxiliary-prediction pilot.

## Machine-Readable Artifacts

- baseline manifest: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/resolved_baseline_manifest.yaml`;
- split audit: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/split_boundary_audit.csv`;
- residual features: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/per_curve_residual_features.csv`;
- MMT signatures: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/mmt_signature_table.csv`;
- descriptive summary: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/descriptive_test_summary.csv`;
- comparison table: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/explanatory_comparison.csv`;
- decision summary: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/decision_summary.yaml`;
- validation summary: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-08-29-32__wave52_mmt_residual_explanatory_diagnostic/validation_summary.yaml`.
