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
- candidate count: `24`;
- held-out curve count before candidate filtering: `194`;
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
| `accepted_periodic_gru_sequence_global` | `accepted_non_pinn_incumbent` | `periodic_gru_sequence` | `global` | `forward, backward` |
| `accepted_periodic_mlp_harmonic_global` | `accepted_non_pinn_incumbent` | `periodic_mlp_harmonic` | `global` | `forward, backward` |

## Forward Comparison

## Backward Comparison

## Global Model Direction Breakdown

| Candidate | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `accepted_periodic_gru_sequence_global` | `forward` | 0.001742 | 0.002053 | 3.562 | 7.416 |
| `accepted_periodic_gru_sequence_global` | `backward` | 0.001879 | 0.002228 | 3.572 | 9.292 |
| `accepted_periodic_gru_sequence_global` | `combined` | 0.001810 | 0.002141 | 3.567 | 9.193 |
| `accepted_periodic_mlp_harmonic_global` | `forward` | 0.001632 | 0.001925 | 3.298 | 8.144 |
| `accepted_periodic_mlp_harmonic_global` | `backward` | 0.001836 | 0.002182 | 3.472 | 9.150 |
| `accepted_periodic_mlp_harmonic_global` | `combined` | 0.001734 | 0.002054 | 3.385 | 8.907 |
| `wave52r_integrated_a02_seed_161803` | `forward` | 0.001402 | 0.001660 | 2.858 | 7.468 |
| `wave52r_integrated_a02_seed_161803` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_161803` | `combined` | 0.001462 | 0.001736 | 2.891 | 7.056 |
| `wave52r_integrated_a02_seed_271828` | `forward` | 0.001401 | 0.001660 | 2.858 | 7.466 |
| `wave52r_integrated_a02_seed_271828` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_271828` | `combined` | 0.001462 | 0.001736 | 2.891 | 7.056 |
| `wave52r_integrated_a02_seed_314159` | `forward` | 0.001400 | 0.001658 | 2.856 | 7.463 |
| `wave52r_integrated_a02_seed_314159` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a02_seed_314159` | `combined` | 0.001462 | 0.001735 | 2.890 | 7.056 |
| `wave52r_integrated_a03_seed_161803` | `forward` | 0.001403 | 0.001662 | 2.862 | 7.462 |
| `wave52r_integrated_a03_seed_161803` | `backward` | 0.001512 | 0.001801 | 2.909 | 6.764 |
| `wave52r_integrated_a03_seed_161803` | `combined` | 0.001457 | 0.001731 | 2.885 | 7.076 |
| `wave52r_integrated_a03_seed_271828` | `forward` | 0.001402 | 0.001661 | 2.859 | 7.477 |
| `wave52r_integrated_a03_seed_271828` | `backward` | 0.001515 | 0.001805 | 2.914 | 6.746 |
| `wave52r_integrated_a03_seed_271828` | `combined` | 0.001459 | 0.001733 | 2.887 | 7.078 |
| `wave52r_integrated_a03_seed_314159` | `forward` | 0.001403 | 0.001662 | 2.861 | 7.485 |
| `wave52r_integrated_a03_seed_314159` | `backward` | 0.001517 | 0.001806 | 2.916 | 6.740 |
| `wave52r_integrated_a03_seed_314159` | `combined` | 0.001460 | 0.001734 | 2.889 | 7.082 |
| `wave52r_integrated_a04_seed_161803` | `forward` | 0.001398 | 0.001655 | 2.848 | 7.309 |
| `wave52r_integrated_a04_seed_161803` | `backward` | 0.001517 | 0.001802 | 2.907 | 6.672 |
| `wave52r_integrated_a04_seed_161803` | `combined` | 0.001457 | 0.001729 | 2.877 | 6.916 |
| `wave52r_integrated_a04_seed_271828` | `forward` | 0.001401 | 0.001658 | 2.853 | 7.389 |
| `wave52r_integrated_a04_seed_271828` | `backward` | 0.001521 | 0.001807 | 2.913 | 6.748 |
| `wave52r_integrated_a04_seed_271828` | `combined` | 0.001461 | 0.001733 | 2.883 | 6.994 |
| `wave52r_integrated_a04_seed_314159` | `forward` | 0.001402 | 0.001661 | 2.858 | 7.424 |
| `wave52r_integrated_a04_seed_314159` | `backward` | 0.001519 | 0.001804 | 2.910 | 6.690 |
| `wave52r_integrated_a04_seed_314159` | `combined` | 0.001461 | 0.001733 | 2.884 | 6.987 |
| `wave52r_integrated_a05_seed_161803` | `forward` | 0.001400 | 0.001658 | 2.852 | 7.278 |
| `wave52r_integrated_a05_seed_161803` | `backward` | 0.001521 | 0.001808 | 2.916 | 6.724 |
| `wave52r_integrated_a05_seed_161803` | `combined` | 0.001461 | 0.001733 | 2.884 | 6.909 |
| `wave52r_integrated_a05_seed_271828` | `forward` | 0.001404 | 0.001663 | 2.860 | 7.346 |
| `wave52r_integrated_a05_seed_271828` | `backward` | 0.001524 | 0.001811 | 2.920 | 6.784 |
| `wave52r_integrated_a05_seed_271828` | `combined` | 0.001464 | 0.001737 | 2.890 | 6.977 |
| `wave52r_integrated_a05_seed_314159` | `forward` | 0.001403 | 0.001662 | 2.859 | 7.349 |
| `wave52r_integrated_a05_seed_314159` | `backward` | 0.001526 | 0.001814 | 2.925 | 6.748 |
| `wave52r_integrated_a05_seed_314159` | `combined` | 0.001464 | 0.001738 | 2.892 | 6.949 |
| `wave52r_integrated_a06_seed_161803` | `forward` | 0.001416 | 0.001678 | 2.884 | 7.548 |
| `wave52r_integrated_a06_seed_161803` | `backward` | 0.001525 | 0.001814 | 2.924 | 6.649 |
| `wave52r_integrated_a06_seed_161803` | `combined` | 0.001471 | 0.001746 | 2.904 | 7.061 |
| `wave52r_integrated_a06_seed_271828` | `forward` | 0.001404 | 0.001662 | 2.858 | 7.230 |
| `wave52r_integrated_a06_seed_271828` | `backward` | 0.001523 | 0.001809 | 2.919 | 6.663 |
| `wave52r_integrated_a06_seed_271828` | `combined` | 0.001463 | 0.001736 | 2.889 | 6.785 |
| `wave52r_integrated_a06_seed_314159` | `forward` | 0.001403 | 0.001661 | 2.857 | 7.301 |
| `wave52r_integrated_a06_seed_314159` | `backward` | 0.001521 | 0.001807 | 2.915 | 6.700 |
| `wave52r_integrated_a06_seed_314159` | `combined` | 0.001462 | 0.001734 | 2.886 | 6.905 |
| `wave52r_integrated_a07_seed_161803` | `forward` | 0.001405 | 0.001664 | 2.862 | 7.491 |
| `wave52r_integrated_a07_seed_161803` | `backward` | 0.001521 | 0.001809 | 2.918 | 6.645 |
| `wave52r_integrated_a07_seed_161803` | `combined` | 0.001463 | 0.001736 | 2.890 | 7.016 |
| `wave52r_integrated_a07_seed_271828` | `forward` | 0.001404 | 0.001662 | 2.860 | 7.369 |
| `wave52r_integrated_a07_seed_271828` | `backward` | 0.001524 | 0.001811 | 2.921 | 6.744 |
| `wave52r_integrated_a07_seed_271828` | `combined` | 0.001464 | 0.001737 | 2.891 | 6.978 |
| `wave52r_integrated_a07_seed_314159` | `forward` | 0.001403 | 0.001661 | 2.858 | 7.197 |
| `wave52r_integrated_a07_seed_314159` | `backward` | 0.001523 | 0.001810 | 2.919 | 6.722 |
| `wave52r_integrated_a07_seed_314159` | `combined` | 0.001463 | 0.001736 | 2.888 | 6.873 |
| `wave52r_integrated_a08_seed_161803` | `forward` | 0.001402 | 0.001660 | 2.858 | 7.468 |
| `wave52r_integrated_a08_seed_161803` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_161803` | `combined` | 0.001462 | 0.001736 | 2.891 | 7.056 |
| `wave52r_integrated_a08_seed_271828` | `forward` | 0.001401 | 0.001660 | 2.858 | 7.466 |
| `wave52r_integrated_a08_seed_271828` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_271828` | `combined` | 0.001462 | 0.001736 | 2.891 | 7.056 |
| `wave52r_integrated_a08_seed_314159` | `forward` | 0.001400 | 0.001658 | 2.856 | 7.463 |
| `wave52r_integrated_a08_seed_314159` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_integrated_a08_seed_314159` | `combined` | 0.001462 | 0.001735 | 2.890 | 7.056 |
| `wave52r_promotion_k01_global_seed_271828` | `forward` | 0.001405 | 0.001664 | 2.863 | 7.513 |
| `wave52r_promotion_k01_global_seed_271828` | `backward` | 0.001523 | 0.001811 | 2.923 | 6.727 |
| `wave52r_promotion_k01_global_seed_271828` | `combined` | 0.001464 | 0.001738 | 2.893 | 7.057 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-08-03-22-01-08__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_global/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-08-03-22-01-08__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_global\per_condition_metrics.csv`;
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
