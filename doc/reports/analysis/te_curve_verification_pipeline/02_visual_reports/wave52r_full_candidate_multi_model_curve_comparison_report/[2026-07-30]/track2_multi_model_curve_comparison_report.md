# TE Curve Verification Pipeline Multi-Model Curve Comparison Report

## Overview

This report compares representative `TE Curve Verification Pipeline` TE curves by overlaying
multiple model predictions on the same original measured curve. The
plots are intended to show whether each model tracks the local harmonic
oscillations rather than only the broad mean trend.

## Scope

- each comparison image contains four deterministic held-out test curves;
- forward comparisons are shown on forward curves only;
- backward comparisons are shown on backward curves only;
- Wave 1 screening keeps the three strongest family-best models by
  `Curve MAE [deg]` within each direction;
- `Original Curve` uses the same visual weight as predictions and a
  dark-gray color for balanced comparison.

## Metrics Summary

### Forward Wave52r Stage5 Non Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52r_stage5_h08_seed_314159` | `wave52r_stage5_non_temporal` | Fw | 0.001694 | 0.002005 | 3.483 |

### Forward Wave52r Stage9 Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52r_stage9_k01` | `wave52r_stage9_temporal` | Fw | 0.001374 | 0.001645 | 2.716 |

### Forward Wave52r Stage12 Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52r_stage12_f01` | `wave52r_stage12_temporal` | Fw | 0.001444 | 0.001724 | 2.993 |

### Forward Accepted Non Windowed Reference Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `accepted_periodic_mlp_harmonic_Fw` | `accepted_non_windowed_reference` | Fw | 0.001694 | 0.002008 | 3.439 |

### Forward Accepted Time Windowed Incumbent Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `accepted_periodic_gru_sequence_Fw` | `accepted_time_windowed_incumbent` | Fw | 0.001618 | 0.001931 | 3.278 |

### Forward Wave 5.2R Cross-Lane Finalist Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52r_stage5_h08_seed_314159` | `wave52r_stage5_non_temporal` | Fw | 0.001694 | 0.002005 | 3.483 |
| `wave52r_stage9_k01` | `wave52r_stage9_temporal` | Fw | 0.001374 | 0.001645 | 2.716 |
| `wave52r_stage12_f01` | `wave52r_stage12_temporal` | Fw | 0.001444 | 0.001724 | 2.993 |
| `accepted_periodic_mlp_harmonic_Fw` | `accepted_non_windowed_reference` | Fw | 0.001694 | 0.002008 | 3.439 |
| `accepted_periodic_gru_sequence_Fw` | `accepted_time_windowed_incumbent` | Fw | 0.001618 | 0.001931 | 3.278 |

## Comparison Gallery - Forward Wave52r Stage5 Non Temporal Overlay

Included models: `wave52r_stage5_h08_seed_314159`.

![Forward Wave52r Stage5 Non Temporal Overlay TE Curve Verification Pipeline comparison](assets/comparisons/auto_forward_wave52r_stage5_non_temporal.png)

## Comparison Gallery - Forward Wave52r Stage9 Temporal Overlay

Included models: `wave52r_stage9_k01`.

![Forward Wave52r Stage9 Temporal Overlay TE Curve Verification Pipeline comparison](assets/comparisons/auto_forward_wave52r_stage9_temporal.png)

## Comparison Gallery - Forward Wave52r Stage12 Temporal Overlay

Included models: `wave52r_stage12_f01`.

![Forward Wave52r Stage12 Temporal Overlay TE Curve Verification Pipeline comparison](assets/comparisons/auto_forward_wave52r_stage12_temporal.png)

## Comparison Gallery - Forward Accepted Non Windowed Reference Overlay

Included models: `accepted_periodic_mlp_harmonic_Fw`.

![Forward Accepted Non Windowed Reference Overlay TE Curve Verification Pipeline comparison](assets/comparisons/auto_forward_accepted_non_windowed_reference.png)

## Comparison Gallery - Forward Accepted Time Windowed Incumbent Overlay

Included models: `accepted_periodic_gru_sequence_Fw`.

![Forward Accepted Time Windowed Incumbent Overlay TE Curve Verification Pipeline comparison](assets/comparisons/auto_forward_accepted_time_windowed_incumbent.png)

## Comparison Gallery - Forward Wave 5.2R Cross-Lane Finalist Overlay

Included models: `wave52r_stage5_h08_seed_314159`, `wave52r_stage9_k01`, `wave52r_stage12_f01`, `accepted_periodic_mlp_harmonic_Fw`, `accepted_periodic_gru_sequence_Fw`.

![Forward Wave 5.2R Cross-Lane Finalist Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave52r_cross_lane_shortlist.png)

## Output Artifacts

- output directory: `output\validation_checks\wave52r_full_candidate_track2_multi_model_curve_comparison_report\2026-07-30-11-05-54__track2_multi_model_curve_comparison_report`;
- summary YAML: `output\validation_checks\wave52r_full_candidate_track2_multi_model_curve_comparison_report\2026-07-30-11-05-54__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_summary.yaml`;
- metrics CSV: `output\validation_checks\wave52r_full_candidate_track2_multi_model_curve_comparison_report\2026-07-30-11-05-54__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\wave52r_full_candidate_multi_model_curve_comparison_report\[2026-07-30]\track2_multi_model_curve_comparison_report.md`.
