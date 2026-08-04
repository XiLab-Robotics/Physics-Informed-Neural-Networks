# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `wave52r_integrated_specialist_curve_first`;
- candidate count: `26`;
- held-out curve count before candidate filtering: `97`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;
- `global` candidates are evaluated on both directions and reported with
  direction-separated metrics.

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `wave52r_integrated_a02_seed_314159` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a02` | `global` | `forward, backward` |
| `wave52r_integrated_a02_seed_271828` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a02` | `global` | `forward, backward` |
| `wave52r_integrated_a02_seed_161803` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a02` | `global` | `forward, backward` |
| `wave52r_integrated_a03_seed_314159` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a03` | `global` | `forward, backward` |
| `wave52r_integrated_a03_seed_271828` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a03` | `global` | `forward, backward` |
| `wave52r_integrated_a03_seed_161803` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a03` | `global` | `forward, backward` |
| `wave52r_integrated_a04_seed_314159` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a04` | `global` | `forward, backward` |
| `wave52r_integrated_a04_seed_271828` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a04` | `global` | `forward, backward` |
| `wave52r_integrated_a04_seed_161803` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a04` | `global` | `forward, backward` |
| `wave52r_integrated_a05_seed_314159` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a05` | `global` | `forward, backward` |
| `wave52r_integrated_a05_seed_271828` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a05` | `global` | `forward, backward` |
| `wave52r_integrated_a05_seed_161803` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a05` | `global` | `forward, backward` |
| `wave52r_integrated_a06_seed_314159` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a06` | `global` | `forward, backward` |
| `wave52r_integrated_a06_seed_271828` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a06` | `global` | `forward, backward` |
| `wave52r_integrated_a06_seed_161803` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a06` | `global` | `forward, backward` |
| `wave52r_integrated_a07_seed_314159` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a07` | `global` | `forward, backward` |
| `wave52r_integrated_a07_seed_271828` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a07` | `global` | `forward, backward` |
| `wave52r_integrated_a07_seed_161803` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a07` | `global` | `forward, backward` |
| `wave52r_integrated_a08_seed_314159` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a08` | `global` | `forward, backward` |
| `wave52r_integrated_a08_seed_271828` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a08` | `global` | `forward, backward` |
| `wave52r_integrated_a08_seed_161803` | `wave52r_integrated_specialist_trained` | `wave52r_integrated_specialist_a08` | `global` | `forward, backward` |
| `wave52r_promotion_k01_global_seed_271828` | `wave52r_offline_leader_cross_surface_promotion` | `wave52r_promotion_k01` | `global` | `forward, backward` |
| `accepted_periodic_gru_sequence_Bw` | `accepted_non_pinn_incumbent` | `periodic_gru_sequence` | `Bw` | `backward` |
| `accepted_periodic_mlp_harmonic_Bw` | `accepted_non_pinn_incumbent` | `periodic_mlp_harmonic` | `Bw` | `backward` |
| `accepted_periodic_gru_sequence_global` | `accepted_non_pinn_incumbent` | `periodic_gru_sequence` | `global` | `forward, backward` |
| `accepted_periodic_mlp_harmonic_global` | `accepted_non_pinn_incumbent` | `periodic_mlp_harmonic` | `global` | `forward, backward` |

## Forward Comparison

## Backward Comparison

## Global Model Direction Breakdown

| Candidate | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `accepted_periodic_gru_sequence_global` | `backward` | 0.001879 | 0.002228 | 3.572 | 9.292 |
| `accepted_periodic_gru_sequence_global` | `combined` | 0.001879 | 0.002228 | 3.572 | 9.292 |
| `accepted_periodic_mlp_harmonic_global` | `backward` | 0.001836 | 0.002182 | 3.472 | 9.150 |
| `accepted_periodic_mlp_harmonic_global` | `combined` | 0.001836 | 0.002182 | 3.472 | 9.150 |
| `wave52r_integrated_a02_seed_161803` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_161803` | `combined` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_271828` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_271828` | `combined` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_314159` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_314159` | `combined` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a03_seed_161803` | `backward` | 0.001512 | 0.001801 | 2.909 | 6.764 |
| `wave52r_integrated_a03_seed_161803` | `combined` | 0.001512 | 0.001801 | 2.909 | 6.764 |
| `wave52r_integrated_a03_seed_271828` | `backward` | 0.001515 | 0.001805 | 2.914 | 6.746 |
| `wave52r_integrated_a03_seed_271828` | `combined` | 0.001515 | 0.001805 | 2.914 | 6.746 |
| `wave52r_integrated_a03_seed_314159` | `backward` | 0.001517 | 0.001806 | 2.916 | 6.740 |
| `wave52r_integrated_a03_seed_314159` | `combined` | 0.001517 | 0.001806 | 2.916 | 6.740 |
| `wave52r_integrated_a04_seed_161803` | `backward` | 0.001517 | 0.001802 | 2.907 | 6.672 |
| `wave52r_integrated_a04_seed_161803` | `combined` | 0.001517 | 0.001802 | 2.907 | 6.672 |
| `wave52r_integrated_a04_seed_271828` | `backward` | 0.001521 | 0.001807 | 2.913 | 6.748 |
| `wave52r_integrated_a04_seed_271828` | `combined` | 0.001521 | 0.001807 | 2.913 | 6.748 |
| `wave52r_integrated_a04_seed_314159` | `backward` | 0.001519 | 0.001804 | 2.910 | 6.690 |
| `wave52r_integrated_a04_seed_314159` | `combined` | 0.001519 | 0.001804 | 2.910 | 6.690 |
| `wave52r_integrated_a05_seed_161803` | `backward` | 0.001521 | 0.001808 | 2.916 | 6.724 |
| `wave52r_integrated_a05_seed_161803` | `combined` | 0.001521 | 0.001808 | 2.916 | 6.724 |
| `wave52r_integrated_a05_seed_271828` | `backward` | 0.001524 | 0.001811 | 2.920 | 6.784 |
| `wave52r_integrated_a05_seed_271828` | `combined` | 0.001524 | 0.001811 | 2.920 | 6.784 |
| `wave52r_integrated_a05_seed_314159` | `backward` | 0.001526 | 0.001814 | 2.925 | 6.748 |
| `wave52r_integrated_a05_seed_314159` | `combined` | 0.001526 | 0.001814 | 2.925 | 6.748 |
| `wave52r_integrated_a06_seed_161803` | `backward` | 0.001525 | 0.001814 | 2.924 | 6.649 |
| `wave52r_integrated_a06_seed_161803` | `combined` | 0.001525 | 0.001814 | 2.924 | 6.649 |
| `wave52r_integrated_a06_seed_271828` | `backward` | 0.001523 | 0.001809 | 2.919 | 6.663 |
| `wave52r_integrated_a06_seed_271828` | `combined` | 0.001523 | 0.001809 | 2.919 | 6.663 |
| `wave52r_integrated_a06_seed_314159` | `backward` | 0.001521 | 0.001807 | 2.915 | 6.700 |
| `wave52r_integrated_a06_seed_314159` | `combined` | 0.001521 | 0.001807 | 2.915 | 6.700 |
| `wave52r_integrated_a07_seed_161803` | `backward` | 0.001521 | 0.001809 | 2.918 | 6.645 |
| `wave52r_integrated_a07_seed_161803` | `combined` | 0.001521 | 0.001809 | 2.918 | 6.645 |
| `wave52r_integrated_a07_seed_271828` | `backward` | 0.001524 | 0.001811 | 2.921 | 6.744 |
| `wave52r_integrated_a07_seed_271828` | `combined` | 0.001524 | 0.001811 | 2.921 | 6.744 |
| `wave52r_integrated_a07_seed_314159` | `backward` | 0.001523 | 0.001810 | 2.919 | 6.722 |
| `wave52r_integrated_a07_seed_314159` | `combined` | 0.001523 | 0.001810 | 2.919 | 6.722 |
| `wave52r_integrated_a08_seed_161803` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_161803` | `combined` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_271828` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_271828` | `combined` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_314159` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_314159` | `combined` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_promotion_k01_global_seed_271828` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_promotion_k01_global_seed_271828` | `combined` | 0.001523 | 0.001811 | 2.923 | 6.727 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-08-03-21-59-38__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_backward/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-08-03-21-59-38__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_backward\per_condition_metrics.csv`;
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
