# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This update accepts the completed `Wave 3.2` harmonic-offset probe into the
official `TE Curve Verification Pipeline` offline verification matrix.

Decision:

- `Wave 3.2` is verified as an exploratory harmonic-offset baseline.
- No `Wave 3.2` candidate is promoted over the current accepted `TE Curve Verification Pipeline`
  leaders.
- The project continues to maintain three parallel best surfaces: `Fw`, `Bw`,
  and `global`.
- Within `Wave 3.2`, the strongest forward candidate is
  `track2f_bis_harmonic_residual_offset_Fw`.
- Within `Wave 3.2`, the strongest backward candidate is
  `track2f_bis_harmonic_residual_offset_Bw`.
- Within `Wave 3.2`, the strongest global candidate is
  `track2f_bis_clean_sequential_residual_offset_global`.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-06-08-13-25-37__track2_full_directional_family_matrix_track2f_bis_harmonic_offset_probe_track2_refresh_2026_06_08/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-06-08-13-25-37__track2_full_directional_family_matrix_track2f_bis_harmonic_offset_probe_track2_refresh_2026_06_08/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-06-08]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-06-08]/track2_multi_model_curve_comparison_report.md`.

## Candidate Refresh

The refresh added `6` registry-backed `Wave 3.2` candidates and rechecked
the `3` existing `Wave 3.1` candidates in the same incremental package.

| Surface | Branch | Candidate | Registry |
| --- | --- | --- | --- |
| `global` | clean sequential residual offset | `track2f_bis_clean_sequential_residual_offset_global` | `output/registries/families/track2f_bis_clean_sequential_residual_offset_global/latest_family_best.yaml` |
| `Fw` | clean sequential residual offset | `track2f_bis_clean_sequential_residual_offset_Fw` | `output/registries/families/track2f_bis_clean_sequential_residual_offset_fw/latest_family_best.yaml` |
| `Bw` | clean sequential residual offset | `track2f_bis_clean_sequential_residual_offset_Bw` | `output/registries/families/track2f_bis_clean_sequential_residual_offset_bw/latest_family_best.yaml` |
| `global` | harmonic residual offset | `track2f_bis_harmonic_residual_offset_global` | `output/registries/families/track2f_bis_harmonic_residual_offset_global/latest_family_best.yaml` |
| `Fw` | harmonic residual offset | `track2f_bis_harmonic_residual_offset_Fw` | `output/registries/families/track2f_bis_harmonic_residual_offset_fw/latest_family_best.yaml` |
| `Bw` | harmonic residual offset | `track2f_bis_harmonic_residual_offset_Bw` | `output/registries/families/track2f_bis_harmonic_residual_offset_bw/latest_family_best.yaml` |

The matrix now contains `120` candidates. The incremental operator run used the
completed `Wave 3.1` refresh as its `114`-candidate baseline and evaluated
`9` registry-backed offset-aware candidates.

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

## Wave 3.2 Result

| Surface | Candidate | Branch | MAE [deg] | RMSE [deg] | Mean [%] |
| --- | --- | --- | ---: | ---: | ---: |
| `Fw` | `track2f_bis_harmonic_residual_offset_Fw` | harmonic residual offset | 0.002850 | 0.003108 | 6.286 |
| `Fw` | `track2f_bis_clean_sequential_residual_offset_Fw` | clean sequential residual offset | 0.003439 | 0.003870 | 7.632 |
| `Bw` | `track2f_bis_harmonic_residual_offset_Bw` | harmonic residual offset | 0.003331 | 0.003671 | 7.261 |
| `Bw` | `track2f_bis_clean_sequential_residual_offset_Bw` | clean sequential residual offset | 0.003541 | 0.003971 | 7.732 |
| `global forward slice` | `track2f_bis_harmonic_residual_offset_global` | harmonic residual offset | 0.003255 | 0.003547 | 7.224 |
| `global backward slice` | `track2f_bis_harmonic_residual_offset_global` | harmonic residual offset | 0.003805 | 0.004120 | 8.354 |
| `global combined` | `track2f_bis_clean_sequential_residual_offset_global` | clean sequential residual offset | 0.003522 | 0.003950 | 7.754 |
| `global combined` | `track2f_bis_harmonic_residual_offset_global` | harmonic residual offset | 0.003530 | 0.003833 | 7.789 |

The harmonic branch materially improves the direction-specific `Fw` result and
also improves the direction-specific `Bw` result versus the clean sequential
residual offset control. The same conclusion does not hold for the `global`
surface: the harmonic global model improves its forward slice, but degrades the
backward slice enough that the clean global control remains the stronger
Wave 3.2 global candidate by combined MAE.

## Visual Evidence

The `2026-06-08` collage and overlay bundles were regenerated with dedicated
Wave 3.2 sections:

- `Forward Wave 3.2 Harmonic-Offset Probe Models`;
- `Backward Wave 3.2 Harmonic-Offset Probe Models`;
- `Global Wave 3.2 Harmonic-Offset Probe Models` in the collage report.

The visual package confirms the same decision pattern as the matrix: harmonic
forcing is useful for the direction-specific branches, while the global branch
still needs a better way to balance forward and backward offset/shape behavior.

## Campaign Update Ledger

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-06-08 | `Wave 3.2` harmonic-offset probe refresh | `6` clean and harmonic `global`, `Fw`, and `Bw` candidates plus `3` rechecked Wave 3.1 candidates | included in the `120`-candidate matrix | dated collage and overlay bundles regenerated with Wave 3.2 sections | verified exploratory baseline; not promoted |
| 2026-06-04 | `Wave 3.1` offset-aware probe refresh | `3` `global`, `Fw`, and `Bw` sequential residual offset candidates | included in the `114`-candidate matrix | dated collage and overlay bundles regenerated | verified exploratory baseline; not promoted |
| 2026-05-28 | `Wave 2.3` residual harmonic temporal hybrid refresh | `18` `global`, `Fw`, and `Bw` residual harmonic GRU/LSTM candidates | included in the `111`-candidate matrix | collage and overlay reports refreshed with `Wave 2.3` sections | verified exploratory baseline; not promoted over `Wave 2.2` or accepted TE Curve Verification Pipeline baselines |
| 2026-05-26 | `Wave 2.2` harmonic temporal hybrid refresh | periodic temporal convolution, GRU, and LSTM `global`, `Fw`, and `Bw` candidates | included | collage and overlay reports refreshed | strongest repository-owned neural branch |

## Closeout Decision

`Wave 3.2` does not change the accepted `TE Curve Verification Pipeline` baseline. The current
direction-parallel decision remains:

- `Fw`: `rcim_retuned_GBM19_Fw` remains the strongest overall forward
  candidate, while `track2f_bis_harmonic_residual_offset_Fw` is a useful
  harmonic-offset exploratory branch.
- `Bw`: `periodic_gru_sequence_Bw` remains the strongest practical
  repository-owned backward candidate; `track2f_bis_harmonic_residual_offset_Bw`
  is better than the clean offset control but is not promoted.
- `global`: `periodic_gru_sequence_global` remains the strongest
  repository-owned bidirectional neural candidate; within Wave 3.2, the
  clean global control is slightly stronger than the harmonic global branch.

The next modeling step should keep harmonic forcing available for
direction-specific probes, but should not treat it as sufficient for the
global surface. The next planned branch should move to a curve-aware loss or a
multi-task shape/offset structure that can balance raw error, offset, centered
shape, amplitude, and phase while preserving the causal runtime input contract.
