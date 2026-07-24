# Wave 5.2 MMT Residual-Explanatory Diagnostic Rerun

## Overview

This non-training rerun tests whether repository-available MMT
signatures explain frozen-baseline residual metrics beyond causal
operating metadata. Coefficients are fitted on training rows only;
validation and test rows remain held out.

## Decision

Decision: `blocked_by_parameter_availability`.

The exact-manifest replay closes the earlier residual-provenance
blocker. The remaining blocker is physical parameter availability:
geometry-locked MMT values are constant across operating conditions,
while the five equivalent-error groups lack observed causal inputs or
a validated contact-state reconstruction. Target-derived substitutes
were not created.

## Provenance And Split Isolation

- run instance: `2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic`;
- config: `config/analysis/wave52_mmt_residual_explanatory_diagnostic.yaml`;
- residual source: `output/validation_checks/wave52_frozen_baseline_residual_replay/2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay/per_curve_residual_metrics.csv`;
- output directory: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic`;
- resolved baselines: `4`;
- unique dataset files: `1938`;
- train files: `1356`;
- validation files: `388`;
- test files: `194`.

Split membership comes directly from the replayed direction-specific
training snapshots. No global replacement split or held-out fitting was
performed.

| Residual split | Candidate rows | Policy |
| --- | ---: | --- |
| train | 2712 | fit allowed |
| validation | 776 | evaluation only |
| test | 388 | final held-out evaluation only |

## MMT Evidence Arms

The diagnostic materialized `22`
geometry-locked curve-summary and harmonic signature values. It fitted
four permitted arms: metadata only, geometry only, metadata plus
geometry, and metadata plus shuffled geometry. The fifth arm,
train-only calibrated equivalent errors, is recorded as blocked rather
than synthesized from TE targets.

Because every geometry signature is identical for every operating
condition, standardization maps those columns to zero. Geometry-only
therefore reduces to an intercept; combined and shuffled arms are
algebraically equivalent to metadata only.

## Held-Out Test Comparison

| Candidate | Residual target | Metadata MAE | Metadata + MMT MAE | MAE gain | Shuffled gain |
| --- | --- | ---: | ---: | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Bw` | `absolute_offset_error_deg` | 0.000473 | 0.000473 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `centered_mae_deg` | 0.001030 | 0.001030 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `mean_harmonic_amplitude_error_pct` | 9.958968 | 9.958968 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `mean_harmonic_phase_error_deg` | 5.393392 | 5.393392 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `normalized_derivative_rmse` | 0.009290 | 0.009290 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `peak_to_peak_error_pct` | 4.728758 | 4.728758 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `raw_mae_deg` | 0.001039 | 0.001039 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `absolute_offset_error_deg` | 0.000538 | 0.000538 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `centered_mae_deg` | 0.000729 | 0.000729 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `mean_harmonic_amplitude_error_pct` | 8.678853 | 8.678853 | -0.000000000 | -0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `mean_harmonic_phase_error_deg` | 5.845490 | 5.845490 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `normalized_derivative_rmse` | 0.008108 | 0.008108 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `peak_to_peak_error_pct` | 3.846493 | 3.846493 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `raw_mae_deg` | 0.000779 | 0.000779 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `absolute_offset_error_deg` | 0.000590 | 0.000590 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `centered_mae_deg` | 0.001136 | 0.001136 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `mean_harmonic_amplitude_error_pct` | 6.277973 | 6.277973 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `mean_harmonic_phase_error_deg` | 5.774543 | 5.774543 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `normalized_derivative_rmse` | 0.453286 | 0.453286 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `peak_to_peak_error_pct` | 5.833944 | 5.833944 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `raw_mae_deg` | 0.001115 | 0.001115 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `absolute_offset_error_deg` | 0.000633 | 0.000633 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `centered_mae_deg` | 0.000755 | 0.000755 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `mean_harmonic_amplitude_error_pct` | 4.245138 | 4.245138 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `mean_harmonic_phase_error_deg` | 5.261089 | 5.261089 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `normalized_derivative_rmse` | 0.367997 | 0.367997 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `peak_to_peak_error_pct` | 4.669915 | 4.669915 | 0.000000000 | 0.000000000 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `raw_mae_deg` | 0.000836 | 0.000836 | 0.000000000 | 0.000000000 |

All metadata-plus-MMT and shuffled gains are expected to be numerical
zero because the available MMT design columns are constant. This is
a structural result, not evidence that the underlying mechanical
equations are false.

## Descriptive Test Evidence

| Candidate | Raw MAE [deg] | Centered MAE [deg] |
| --- | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Fw` | 0.001340 | 0.001106 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001507 | 0.001149 |
| `polished_setpoints_periodic_gru_sequence_Bw` | 0.001702 | 0.001463 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | 0.001702 | 0.001431 |

## Blockers

- train-only equivalent-error groups are unavailable as causal condition-level inputs and cannot be physically calibrated.
- current geometry-locked MMT signatures are invariant across operating conditions and collapse to the fitted intercept.

## Next Action

Keep MMT diagnostic-only. Do not prepare an MMT feature, auxiliary
head, weak soft constraint, full PINN, or Wave 6 campaign from this
evidence. Reopen the gate only after independent component-error
measurements or a validated causal contact-state reconstruction
provides condition-varying MMT inputs without using held-out TE.

## Machine-Readable Artifacts

- baseline manifest: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/resolved_baseline_manifest.yaml`;
- split audit: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/split_boundary_audit.csv`;
- residual features: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/per_curve_residual_features.csv`;
- MMT signatures: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/mmt_signature_table.csv`;
- descriptive summary: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/descriptive_split_summary.csv`;
- comparison table: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/explanatory_comparison.csv`;
- decision summary: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/decision_summary.yaml`;
- validation summary: `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/2026-07-24-12-55-30__wave52_mmt_residual_explanatory_diagnostic/validation_summary.yaml`.
