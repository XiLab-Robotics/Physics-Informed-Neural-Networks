# Shape-Gated TE Curve Reranker Report

## Overview

This report applies a reduced shape-first gate to the
selected-active `TE Curve Verification Pipeline` candidate set. It does
not run training and does not change the deployable runtime input
contract.

## Scope

- run instance: `2026-07-21-00-19-44__shape_gated_te_curve_reranker`;
- config path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix.yaml`;
- dataset: `polished_dataset`;
- evaluated surfaces: `forward`;
- non-evaluated surfaces remain unchanged by this reduced selection pass;

## Gate Thresholds

| Metric | Threshold |
| --- | ---: |
| FFT amplitude similarity | >= 0.820 |
| Raw derivative correlation | >= 0.700 |
| Smoothed derivative correlation | >= 0.250 |
| Derivative sign agreement rate | >= 0.540 |
| Normalized derivative RMSE | <= 1.000 |
| Mean harmonic amplitude error [%] | <= 55.000 |
| Mean harmonic phase error [deg] | <= 75.000 |
| Peak-to-peak error [%] | <= 35.000 |
| Per-curve shape pass rate | >= 0.600 |
| Near-pass FFT amplitude similarity | >= 0.950 |
| Near-pass mean harmonic amplitude error [%] | <= 38.000 |
| Near-pass mean harmonic phase error [deg] | <= 55.000 |
| Near-pass peak-to-peak error [%] | <= 32.000 |
| Near-pass derivative sign agreement rate | >= 0.500 |
| Near-pass normalized derivative RMSE | <= 1.350 |

## Surface Decisions

### Forward

| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Raw Deriv Corr | Smoothed Deriv Corr | Deriv Sign Rate | Norm Deriv RMSE | Shape Pass Rate | Composite |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | `recommended_candidate` | 0.002398 | 0.001603 | 0.985 | 30.115 | 20.382 | 0.121 | 0.246 | 0.538 | 0.352 | 0.920 | 0.000 |

## Interpretation Rules

- `recommended_candidate` is the first active candidate that passes the
  shape gate after block-score reranking.
- `baseline_anchor_only` entries remain useful references, but they do not
  replace the active development baseline in this reduced pass.
- `near_pass` entries miss the strict per-curve pass-rate gate but keep
  enough aggregate FFT, harmonic, peak-to-peak, and derivative evidence
  to remain visible for review.
- `shape_gate_failed` entries may still have good scalar error, but they
  are demoted until the curve-shape evidence improves.
- `insufficient_evidence` entries could not be evaluated from their
  referenced artifact and must not be promoted until provenance is
  repaired.
- All FFT, centered-shape, derivative, and harmonic diagnostics are
  validation-time evidence only, not deployable runtime corrections.
- The threshold sweep is calibration evidence only; it is not a second
  promotion policy.

## Output Artifacts

- per-curve metrics: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-21-00-19-44__shape_gated_te_curve_reranker\shape_gated_per_curve_metrics.csv`;
- candidate summary: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-21-00-19-44__shape_gated_te_curve_reranker\shape_gated_candidate_summary.csv`;
- threshold sweep: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-21-00-19-44__shape_gated_te_curve_reranker\shape_gate_threshold_sweep.csv`;
- surface decisions: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-21-00-19-44__shape_gated_te_curve_reranker\shape_gated_surface_decisions.yaml`;
