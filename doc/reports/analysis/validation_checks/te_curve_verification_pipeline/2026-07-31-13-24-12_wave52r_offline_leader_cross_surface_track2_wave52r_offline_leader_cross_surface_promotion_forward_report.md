# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `wave52r_offline_leader_cross_surface_curve_first`;
- candidate count: `16`;
- held-out curve count before candidate filtering: `97`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;
- `global` candidates are evaluated on both directions and reported with
  direction-separated metrics.

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `wave52r_promotion_h08_fw_seed_314159` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_h08` | `Fw` | `forward` |
| `wave52r_promotion_k01_fw_seed_314159` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_k01` | `Fw` | `forward` |
| `wave52r_promotion_h08_fw_seed_271828` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_h08` | `Fw` | `forward` |
| `wave52r_promotion_k01_fw_seed_271828` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_k01` | `Fw` | `forward` |
| `wave52r_promotion_h08_fw_seed_161803` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_h08` | `Fw` | `forward` |
| `wave52r_promotion_k01_fw_seed_161803` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_k01` | `Fw` | `forward` |
| `wave52r_promotion_h08_global_seed_314159` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_h08` | `global` | `forward, backward` |
| `wave52r_promotion_k01_global_seed_314159` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_k01` | `global` | `forward, backward` |
| `wave52r_promotion_h08_global_seed_271828` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_h08` | `global` | `forward, backward` |
| `wave52r_promotion_k01_global_seed_271828` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_k01` | `global` | `forward, backward` |
| `wave52r_promotion_h08_global_seed_161803` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_h08` | `global` | `forward, backward` |
| `wave52r_promotion_k01_global_seed_161803` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_k01` | `global` | `forward, backward` |
| `accepted_periodic_gru_sequence_Fw` | `accepted_non_pinn_incumbent` | `periodic_gru_sequence` | `Fw` | `forward` |
| `accepted_periodic_mlp_harmonic_Fw` | `accepted_non_pinn_incumbent` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `accepted_periodic_gru_sequence_global` | `accepted_non_pinn_incumbent` | `periodic_gru_sequence` | `global` | `forward, backward` |
| `accepted_periodic_mlp_harmonic_global` | `accepted_non_pinn_incumbent` | `periodic_mlp_harmonic` | `global` | `forward, backward` |

## Forward Comparison

## Backward Comparison

## Global Model Direction Breakdown

| Candidate | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `accepted_periodic_gru_sequence_global` | `forward` | 0.001742 | 0.002053 | 3.562 | 7.416 |
| `accepted_periodic_gru_sequence_global` | `combined` | 0.001742 | 0.002053 | 3.562 | 7.416 |
| `accepted_periodic_mlp_harmonic_global` | `forward` | 0.001632 | 0.001925 | 3.298 | 8.144 |
| `accepted_periodic_mlp_harmonic_global` | `combined` | 0.001632 | 0.001925 | 3.298 | 8.144 |
| `wave52r_promotion_h08_global_seed_161803` | `forward` | 0.001765 | 0.002072 | 3.652 | 8.011 |
| `wave52r_promotion_h08_global_seed_161803` | `combined` | 0.001765 | 0.002072 | 3.652 | 8.011 |
| `wave52r_promotion_h08_global_seed_271828` | `forward` | 0.001767 | 0.002072 | 3.642 | 8.405 |
| `wave52r_promotion_h08_global_seed_271828` | `combined` | 0.001767 | 0.002072 | 3.642 | 8.405 |
| `wave52r_promotion_h08_global_seed_314159` | `forward` | 0.001760 | 0.002063 | 3.634 | 7.746 |
| `wave52r_promotion_h08_global_seed_314159` | `combined` | 0.001760 | 0.002063 | 3.634 | 7.746 |
| `wave52r_promotion_k01_global_seed_161803` | `forward` | 0.001477 | 0.001742 | 2.967 | 8.915 |
| `wave52r_promotion_k01_global_seed_161803` | `combined` | 0.001477 | 0.001742 | 2.967 | 8.915 |
| `wave52r_promotion_k01_global_seed_271828` | `forward` | 0.001405 | 0.001664 | 2.863 | 7.513 |
| `wave52r_promotion_k01_global_seed_271828` | `combined` | 0.001405 | 0.001664 | 2.863 | 7.513 |
| `wave52r_promotion_k01_global_seed_314159` | `forward` | 0.001492 | 0.001762 | 2.982 | 9.336 |
| `wave52r_promotion_k01_global_seed_314159` | `combined` | 0.001492 | 0.001762 | 2.982 | 9.336 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-31-13-23-15__wave52r_offline_leader_cross_surface_track2_wave52r_offline_leader_cross_surface_promotion_forward/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-31-13-23-15__wave52r_offline_leader_cross_surface_track2_wave52r_offline_leader_cross_surface_promotion_forward\per_condition_metrics.csv`;
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
