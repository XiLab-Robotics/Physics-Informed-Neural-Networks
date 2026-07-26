# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `phase3_c1_fw_initialization_stability_curve_first`;
- candidate count: `6`;
- held-out curve count before candidate filtering: `97`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `phase3_c0_learned_mean_control_Fw` | `phase3_canonical_campaign_control` | `phase3_pinn_c0_learned_mean_control_fw` | `Fw` | `forward` |
| `phase3_c1_linear_compliance_soft_Fw` | `phase3_canonical_campaign_initial_run` | `phase3_pinn_c1_linear_compliance_soft_fw` | `Fw` | `forward` |
| `phase3_c1_fw_seed_271828` | `phase3_initialization_stability_repeat` | `phase3_pinn_c1_linear_compliance_soft_fw_seed_271828` | `Fw` | `forward` |
| `phase3_c1_fw_seed_314159` | `phase3_initialization_stability_repeat` | `phase3_pinn_c1_linear_compliance_soft_fw_seed_314159` | `Fw` | `forward` |
| `accepted_periodic_mlp_harmonic_Fw` | `accepted_non_windowed_reference` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `accepted_periodic_gru_sequence_Fw` | `accepted_time_windowed_reference` | `periodic_gru_sequence` | `Fw` | `forward` |

## Forward Comparison

## Backward Comparison

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-26-20-09-09__phase3_c1_fw_stability_common_test_matrix_phase3_c1_fw_stability_closeout/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-26-20-09-09__phase3_c1_fw_stability_common_test_matrix_phase3_c1_fw_stability_closeout\per_condition_metrics.csv`;
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
