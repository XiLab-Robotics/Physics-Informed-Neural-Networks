# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `phase3_common_split_bounded_curve_payload_diagnostics`;
- candidate count: `16`;
- held-out curve count before candidate filtering: `194`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;
- `global` candidates are evaluated on both directions and reported with
  direction-separated metrics.

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `phase3_c0_learned_mean_control_Bw` | `phase3_canonical_campaign` | `phase3_pinn_c0_learned_mean_control_bw` | `Bw` | `backward` |
| `phase3_c1_linear_compliance_soft_Bw` | `phase3_canonical_campaign` | `phase3_pinn_c1_linear_compliance_soft_bw` | `Bw` | `backward` |
| `phase3_c2_temperature_compliance_soft_Bw` | `phase3_canonical_campaign` | `phase3_pinn_c2_temperature_compliance_soft_bw` | `Bw` | `backward` |
| `phase3_c3_nonlinear_compliance_soft_Bw` | `phase3_canonical_campaign` | `phase3_pinn_c3_nonlinear_compliance_soft_bw` | `Bw` | `backward` |
| `phase3_c4_hard_elastic_offset_Bw` | `phase3_canonical_campaign` | `phase3_pinn_c4_hard_elastic_offset_bw` | `Bw` | `backward` |
| `phase3_c0_learned_mean_control_Fw` | `phase3_canonical_campaign` | `phase3_pinn_c0_learned_mean_control_fw` | `Fw` | `forward` |
| `phase3_c1_linear_compliance_soft_Fw` | `phase3_canonical_campaign` | `phase3_pinn_c1_linear_compliance_soft_fw` | `Fw` | `forward` |
| `phase3_c2_temperature_compliance_soft_Fw` | `phase3_canonical_campaign` | `phase3_pinn_c2_temperature_compliance_soft_fw` | `Fw` | `forward` |
| `phase3_c3_nonlinear_compliance_soft_Fw` | `phase3_canonical_campaign` | `phase3_pinn_c3_nonlinear_compliance_soft_fw` | `Fw` | `forward` |
| `phase3_c4_hard_elastic_offset_Fw` | `phase3_canonical_campaign` | `phase3_pinn_c4_hard_elastic_offset_fw` | `Fw` | `forward` |
| `phase3_c0_learned_mean_control_global` | `phase3_canonical_campaign` | `phase3_pinn_c0_learned_mean_control_global` | `global` | `forward, backward` |
| `phase3_c5_shared_stiffness_global` | `phase3_canonical_campaign` | `phase3_pinn_c5_shared_stiffness_global` | `global` | `forward, backward` |
| `accepted_periodic_mlp_harmonic_Fw` | `accepted_non_windowed_reference` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `accepted_periodic_gru_sequence_Fw` | `accepted_time_windowed_reference` | `periodic_gru_sequence` | `Fw` | `forward` |
| `accepted_periodic_mlp_harmonic_Bw` | `accepted_non_windowed_reference` | `periodic_mlp_harmonic` | `Bw` | `backward` |
| `accepted_periodic_gru_sequence_Bw` | `accepted_time_windowed_reference` | `periodic_gru_sequence` | `Bw` | `backward` |

## Forward Comparison

## Backward Comparison

## Global Model Direction Breakdown

| Candidate | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `phase3_c0_learned_mean_control_global` | `forward` | 0.002128 | 0.002508 | 4.491 | 8.211 |
| `phase3_c0_learned_mean_control_global` | `backward` | 0.002645 | 0.003092 | 5.436 | 12.686 |
| `phase3_c0_learned_mean_control_global` | `combined` | 0.002386 | 0.002800 | 4.963 | 10.838 |
| `phase3_c5_shared_stiffness_global` | `forward` | 0.002346 | 0.002688 | 4.983 | 10.929 |
| `phase3_c5_shared_stiffness_global` | `backward` | 0.002668 | 0.003068 | 5.407 | 12.509 |
| `phase3_c5_shared_stiffness_global` | `combined` | 0.002507 | 0.002878 | 5.195 | 12.510 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-26-19-30-10__phase3_quasi_static_compliance_pinn_common_test_matrix_phase3_closeout_retry/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-26-19-30-10__phase3_quasi_static_compliance_pinn_common_test_matrix_phase3_closeout_retry\per_condition_metrics.csv`;
- grouped report plot root: `None`;
- grouped report plot count: `0`;

## Interpretation

Rows are ranked by mean percentage error within each source group
and direction. Directional paper-reference, Wave 1, and Wave 2.1
models are never evaluated on the opposite direction. Global Wave
models remain valid on both directions and are therefore shown in
the directional sections and again in the global breakdown.
The `rcim_track1` forward reference banks use the opposite stored
`h0` sign convention relative to the TE Curve Verification Pipeline reconstruction
contract, so the TE Curve Verification Pipeline comparison applies the documented
source-specific `h0` compatibility multiplier before curve
reconstruction.

## Open Gaps

- This remains an offline TE-curve comparison and does not replace the
  future online `Table 9` compensation benchmark.
- The report uses the saved Python model artifacts from `models/`; ONNX
  parity checks remain a separate deployment-readiness task.
