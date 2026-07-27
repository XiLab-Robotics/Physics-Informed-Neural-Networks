# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `wave52r_stage0_forward_evidence_freeze`;
- candidate count: `2`;
- held-out curve count before candidate filtering: `97`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `accepted_periodic_mlp_harmonic_Fw` | `accepted_non_windowed_reference` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `accepted_periodic_gru_sequence_Fw` | `accepted_time_windowed_reference` | `periodic_gru_sequence` | `Fw` | `forward` |

## Forward Comparison

## Backward Comparison

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-27-12-40-51__wave52r_stage0_accepted_forward_neural_replay_stage0_freeze/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-27-12-40-51__wave52r_stage0_accepted_forward_neural_replay_stage0_freeze\per_condition_metrics.csv`;
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
