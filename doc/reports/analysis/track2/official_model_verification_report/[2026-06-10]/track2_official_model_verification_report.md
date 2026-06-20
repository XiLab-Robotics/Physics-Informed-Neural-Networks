# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This update accepts the completed `Wave 3.3` curve-aware training campaign into
the official `TE Curve Verification Pipeline` offline verification matrix.

Decision:

- `Wave 3.3` is verified as an exploratory curve-aware training baseline.
- No `Wave 3.3` candidate is promoted over the current accepted `TE Curve Verification Pipeline`
  leaders.
- The project continues to maintain three parallel best surfaces: `Fw`, `Bw`,
  and `global`.
- Within `Wave 3.3`, the strongest forward candidate is
  `track2g_curve_aware_raw_centered_shape_Fw`.
- Within `Wave 3.3`, the strongest backward candidate is
  `track2g_curve_aware_pointwise_control_Bw`.
- Within `Wave 3.3`, the strongest global candidate is
  `track2g_curve_aware_full_curve_composite_global`.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-06-09-13-25-56__track2_full_directional_family_matrix_track2g_curve_aware_track2_refresh_2026_06_09/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-06-09-13-25-56__track2_full_directional_family_matrix_track2g_curve_aware_track2_refresh_2026_06_09/per_condition_metrics.csv`;
- validation report:
  `doc/reports/analysis/validation_checks/track2/2026-06-09-13-33-45_track2_full_directional_family_matrix_track2g_curve_aware_track2_refresh_2026_06_09_report.md`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-06-09]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-09]/track2_multi_model_curve_comparison_report.md`.

## Candidate Refresh

The refresh added `12` registry-backed `Wave 3.3` candidates. Because the
baseline summary used by the operator launcher predated the `Wave 3.1` and
`Wave 3.2` refreshes, the incremental package also rechecked the existing
`3` `Wave 3.1` and `6` `Wave 3.2` candidates. The official decision scope
of this report is the `Wave 3.3` candidate family.

| Surface | Loss Profile | Candidate | Registry Family |
| --- | --- | --- | --- |
| `global` | pointwise control | `track2g_curve_aware_pointwise_control_global` | `track2g_curve_aware_harmonic_residual_offset_pointwise_control_global` |
| `Fw` | pointwise control | `track2g_curve_aware_pointwise_control_Fw` | `track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw` |
| `Bw` | pointwise control | `track2g_curve_aware_pointwise_control_Bw` | `track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw` |
| `global` | raw plus centered shape | `track2g_curve_aware_raw_centered_shape_global` | `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global` |
| `Fw` | raw plus centered shape | `track2g_curve_aware_raw_centered_shape_Fw` | `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw` |
| `Bw` | raw plus centered shape | `track2g_curve_aware_raw_centered_shape_Bw` | `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw` |
| `global` | raw plus offset | `track2g_curve_aware_raw_offset_global` | `track2g_curve_aware_harmonic_residual_offset_raw_offset_global` |
| `Fw` | raw plus offset | `track2g_curve_aware_raw_offset_Fw` | `track2g_curve_aware_harmonic_residual_offset_raw_offset_fw` |
| `Bw` | raw plus offset | `track2g_curve_aware_raw_offset_Bw` | `track2g_curve_aware_harmonic_residual_offset_raw_offset_bw` |
| `global` | full curve composite | `track2g_curve_aware_full_curve_composite_global` | `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global` |
| `Fw` | full curve composite | `track2g_curve_aware_full_curve_composite_Fw` | `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw` |
| `Bw` | full curve composite | `track2g_curve_aware_full_curve_composite_Bw` | `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw` |

The matrix now contains `132` candidates.

## Verification Rules

| Surface | Training or Archive Scope | Evaluation Scope |
| --- | --- | --- |
| `Fw` | forward-only training or archive | forward TE Curve Verification Pipeline curves only |
| `Bw` | backward-only training or archive | backward TE Curve Verification Pipeline curves only |
| `global` | forward and backward training together | both directions, reported by direction and combined |

The `global`, `Fw`, and `Bw` branches are carried forward in parallel. They are
not collapsed into one scalar winner.

## Current Leaders

### Best Composite References

| Candidate | Source | Direction | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | `forward` | 0.001839 | 0.002041 | 4.109 | 9.866 |
| `paper_retuned_best_Bw` | `rcim_retuned` | `backward` | 0.003675 | 0.004284 | 7.572 | 15.645 |

### Repository-Owned Static Baselines

| Direction | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `tree_global` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| `backward` | `tree_Bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| `global combined` | `tree_global` | 0.003144 | 0.003533 | 6.854 | 13.314 |

### Repository-Owned Neural Leaders

| Surface | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `Fw` | `periodic_gru_sequence_Fw` | 0.003186 | 0.003438 | 7.077 | 13.323 |
| `Bw` | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 | 14.820 |
| `global combined` | `periodic_gru_sequence_global` | 0.002704 | 0.002949 | 6.139 | 13.396 |

## Wave 3.3 Result

| Surface | Candidate | Loss Profile | MAE [deg] | RMSE [deg] | Mean [%] |
| --- | --- | --- | ---: | ---: | ---: |
| `Fw` | `track2g_curve_aware_raw_centered_shape_Fw` | raw plus centered shape | 0.003174 | 0.003429 | 7.047 |
| `Fw` | `track2g_curve_aware_full_curve_composite_Fw` | full curve composite | 0.003251 | 0.003515 | 7.209 |
| `Fw` | `track2g_curve_aware_raw_offset_Fw` | raw plus offset | 0.003269 | 0.003588 | 7.268 |
| `Fw` | `track2g_curve_aware_pointwise_control_Fw` | pointwise control | 0.003362 | 0.003612 | 7.474 |
| `Bw` | `track2g_curve_aware_pointwise_control_Bw` | pointwise control | 0.003436 | 0.003761 | 7.538 |
| `Bw` | `track2g_curve_aware_raw_centered_shape_Bw` | raw plus centered shape | 0.003465 | 0.003790 | 7.582 |
| `Bw` | `track2g_curve_aware_raw_offset_Bw` | raw plus offset | 0.003469 | 0.003799 | 7.608 |
| `Bw` | `track2g_curve_aware_full_curve_composite_Bw` | full curve composite | 0.003510 | 0.003897 | 7.683 |
| `global combined` | `track2g_curve_aware_full_curve_composite_global` | full curve composite | 0.003338 | 0.003649 | 7.364 |
| `global combined` | `track2g_curve_aware_raw_centered_shape_global` | raw plus centered shape | 0.003348 | 0.003682 | 7.395 |
| `global combined` | `track2g_curve_aware_raw_offset_global` | raw plus offset | 0.003459 | 0.003755 | 7.630 |
| `global combined` | `track2g_curve_aware_pointwise_control_global` | pointwise control | 0.003578 | 0.003900 | 7.911 |

The curve-aware loss profiles improve over their own pointwise control in the
`Fw` and `global` surfaces, but not in the `Bw` surface. They do not overtake
the accepted direction-parallel leaders.

## Visual Evidence

The `2026-06-09` collage and overlay bundles were regenerated with dedicated
Wave 3.3 sections:

- `Forward Wave 3.3 Curve-Aware Training Models`;
- `Backward Wave 3.3 Curve-Aware Training Models`;
- `Global Wave 3.3 Curve-Aware Training Models` in the collage report;
- `Forward Reference Tree And Wave 3.3 Overlay`;
- `Backward Reference Tree And Wave 3.3 Overlay`.

The visual package supports the matrix decision: the curve-aware losses are
valid experimental controls, but they do not yet produce the clean curve-shape
and offset behavior needed to replace the strongest existing periodic temporal
branches.

## Campaign Update Ledger

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-06-10 | `Wave 3.3` curve-aware training refresh | `12` pointwise-control, centered-shape, offset, and full-composite `global`, `Fw`, and `Bw` candidates | included in the `132`-candidate matrix | dated collage and overlay bundles regenerated with Wave 3.3 sections | verified exploratory baseline; not promoted |
| 2026-06-08 | `Wave 3.2` harmonic-offset probe refresh | `6` clean and harmonic `global`, `Fw`, and `Bw` candidates plus `3` rechecked Wave 3.1 candidates | included in the `120`-candidate matrix | dated collage and overlay bundles regenerated with Wave 3.2 sections | verified exploratory baseline; not promoted |
| 2026-06-04 | `Wave 3.1` offset-aware probe refresh | `3` `global`, `Fw`, and `Bw` sequential residual offset candidates | included in the `114`-candidate matrix | dated collage and overlay bundles regenerated | verified exploratory baseline; not promoted |
| 2026-05-28 | `Wave 2.3` residual harmonic temporal hybrid refresh | `18` `global`, `Fw`, and `Bw` residual harmonic GRU/LSTM candidates | included in the `111`-candidate matrix | collage and overlay reports refreshed with `Wave 2.3` sections | verified exploratory baseline; not promoted over `Wave 2.2` or accepted TE Curve Verification Pipeline baselines |
| 2026-05-26 | `Wave 2.2` harmonic temporal hybrid refresh | periodic temporal convolution, GRU, and LSTM `global`, `Fw`, and `Bw` candidates | included | collage and overlay reports refreshed | strongest repository-owned neural branch |

## Closeout Decision

`Wave 3.3` does not change the accepted `TE Curve Verification Pipeline` baseline. The current
direction-parallel decision remains:

- `Fw`: `rcim_retuned_GBM19_Fw` remains the strongest overall forward
  candidate, while `track2g_curve_aware_raw_centered_shape_Fw` is the strongest
  Wave 3.3 forward candidate and nearly matches the current repository-owned
  neural forward leader.
- `Bw`: `periodic_gru_sequence_Bw` remains the strongest practical
  repository-owned backward candidate; the Wave 3.3 backward candidates are
  weaker than both the current periodic temporal branch and the `tree_Bw`
  static baseline.
- `global`: `periodic_gru_sequence_global` remains the strongest
  repository-owned bidirectional neural candidate; within Wave 3.3, the full
  curve composite loss is the strongest global profile but remains behind the
  existing periodic temporal global branch.

The next modeling step should not continue loss-only tuning as the primary
branch. The evidence supports moving to an explicit multi-head shape/offset
architecture or a closely related decomposition that keeps harmonic structure,
causal runtime inputs, and separate `global`, `Fw`, and `Bw` best-model
surfaces.
