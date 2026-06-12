# Track 2 Official Model Verification Report

## Executive Verdict

This update accepts the completed `Track 2H` quantile/probabilistic campaign
into the official `Track 2` offline verification matrix.

Decision:

- `Track 2H` quantile/probabilistic regression is verified as an exploratory
  dispersion-aware baseline.
- No quantile/probabilistic candidate is promoted over the current accepted
  `Track 2` leaders.
- The project continues to maintain three parallel best surfaces: `Fw`, `Bw`,
  and `global`.
- Within the quantile/probabilistic package, the strongest forward candidate is
  `track2h_gaussian_nll_global`.
- Within the quantile/probabilistic package, the strongest backward candidate
  is `track2h_quantile_p10_p50_p90_Bw`.
- Within the quantile/probabilistic package, the strongest global candidate is
  `track2h_gaussian_nll_global`.
- The probabilistic package improves the previous `Track 2H` robust-loss
  package on the best `global` and `Bw` surfaces, but not on the best `Fw`
  surface.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-06-12-14-44-45__track2_full_directional_family_matrix_track2h_quantile_probabilistic_track2_refresh_2026_06_12/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-06-12-14-44-45__track2_full_directional_family_matrix_track2h_quantile_probabilistic_track2_refresh_2026_06_12/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-06-12]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-12]/track2_multi_model_curve_comparison_report.md`;
- operator launch logs:
  `output/validation_checks/track2_operator_launch_logs/2026-06-12-14-44-41_track2h_quantile_probabilistic_track2_refresh_2026_06_12/`.

## Candidate Refresh

The refresh added `6` registry-backed `Track 2H`
quantile/probabilistic candidates covering quantile and Gaussian uncertainty
profiles across the `global`, `Fw`, and `Bw` surfaces.

| Surface | Profile | Deterministic Curve | Candidate |
| --- | --- | --- | --- |
| `global` | `quantile_p10_p50_p90` | `p50` | `track2h_quantile_p10_p50_p90_global` |
| `Fw` | `quantile_p10_p50_p90` | `p50` | `track2h_quantile_p10_p50_p90_Fw` |
| `Bw` | `quantile_p10_p50_p90` | `p50` | `track2h_quantile_p10_p50_p90_Bw` |
| `global` | `gaussian_nll` | `mu` | `track2h_gaussian_nll_global` |
| `Fw` | `gaussian_nll` | `mu` | `track2h_gaussian_nll_Fw` |
| `Bw` | `gaussian_nll` | `mu` | `track2h_gaussian_nll_Bw` |

The matrix source group is `track2h_quantile_probabilistic_registry`. The
matrix now contains `147` candidates.

## Verification Rules

| Surface | Training or Archive Scope | Evaluation Scope |
| --- | --- | --- |
| `Fw` | forward-only training or archive | forward Track 2 curves only |
| `Bw` | backward-only training or archive | backward Track 2 curves only |
| `global` | forward and backward training together | both directions, reported by direction and combined |

The probabilistic heads are not compared as raw multi-channel tensors. The
official matrix evaluates only the deterministic TE curve exposed by each
checkpoint: `p50` for quantile heads and `mu` for Gaussian NLL heads.

## Current Leaders

### Overall Direction Leaders

| Direction | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |
| `backward` | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 | 14.820 |
| `global forward` | `periodic_gru_sequence_global` | 0.002777 | 0.003025 | 6.267 | 13.580 |
| `global backward` | `periodic_gru_sequence_global` | 0.002630 | 0.002872 | 6.010 | 12.693 |

### Repository-Owned Static Baselines

| Direction | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `backward` | `tree_Bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| `global forward` | `tree_global` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| `global backward` | `tree_global` | 0.003290 | 0.003702 | 7.118 | 13.703 |

## Track 2H Quantile Probabilistic Result

| Surface | Candidate | Profile | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `global forward` | `track2h_gaussian_nll_global` | `gaussian_nll` | 0.002951 | 0.003246 | 6.524 | 15.237 |
| `Bw` | `track2h_quantile_p10_p50_p90_Bw` | `quantile_p10_p50_p90` | 0.002935 | 0.003250 | 6.307 | 16.529 |
| `Bw` | `track2h_gaussian_nll_Bw` | `gaussian_nll` | 0.003001 | 0.003303 | 6.488 | 14.856 |
| `global backward` | `track2h_gaussian_nll_global` | `gaussian_nll` | 0.003068 | 0.003372 | 6.627 | 15.928 |
| `Fw` | `track2h_gaussian_nll_Fw` | `gaussian_nll` | 0.003156 | 0.003415 | 7.008 | 10.991 |
| `global forward` | `track2h_quantile_p10_p50_p90_global` | `quantile_p10_p50_p90` | 0.003188 | 0.003469 | 7.059 | 12.765 |
| `Fw` | `track2h_quantile_p10_p50_p90_Fw` | `quantile_p10_p50_p90` | 0.003276 | 0.003545 | 7.279 | 12.393 |
| `global backward` | `track2h_quantile_p10_p50_p90_global` | `quantile_p10_p50_p90` | 0.003563 | 0.003909 | 7.816 | 15.378 |

The best probabilistic `global` candidate improves over the best robust-loss
global candidate from `0.003401` to `0.003009` combined Track 2 MAE. The best
probabilistic `Bw` candidate improves over the best robust-loss `Bw` candidate
from `0.003078` to `0.002935` Track 2 MAE. The best robust-loss `Fw`
candidate remains slightly better than the best probabilistic `Fw` candidate:
`0.003134` versus `0.003156` Track 2 MAE.

The strongest probabilistic `Bw` candidate also beats the static `tree_Bw`
baseline on Track 2 MAE, `0.002935` versus `0.003258`, but it remains behind
the accepted `periodic_gru_sequence_Bw` branch.

## Visual Evidence

The `2026-06-12` collage and overlay bundles were regenerated after the
probabilistic refresh. They now include explicit `Track 2H` quantile
probabilistic sections for `Fw`, `Bw`, and `global` collage evidence, plus
explicit `Fw` and `Bw` probabilistic overlay sections.

The visual package supports the matrix decision: the probabilistic heads are a
useful dispersion-aware ingredient, especially for `Bw` and the global
surface, but they do not replace the strongest periodic temporal branch or the
forward paper-reference leader.

## Campaign Update Ledger

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-06-12 | `Track 2H` quantile/probabilistic refresh | `6` quantile and Gaussian `global`, `Fw`, and `Bw` candidates | included in the `147`-candidate matrix | dated collage and overlay bundles regenerated | verified exploratory baseline; not promoted |
| 2026-06-11 | `Track 2H` robust-loss dispersion-aware refresh | `9` robust `global`, `Fw`, and `Bw` candidates | included in the `141`-candidate matrix | dated collage and overlay bundles regenerated with Track 2H sections | verified exploratory baseline; not promoted |
| 2026-06-10 | `Track 2G` curve-aware training refresh | `12` pointwise-control, centered-shape, offset, and full-composite `global`, `Fw`, and `Bw` candidates | included in the `132`-candidate matrix | dated collage and overlay bundles regenerated with Track 2G sections | verified exploratory baseline; not promoted |
| 2026-06-08 | `Track 2F-bis` harmonic-offset probe refresh | `6` clean and harmonic `global`, `Fw`, and `Bw` candidates plus `3` rechecked Track 2F candidates | included in the `120`-candidate matrix | dated collage and overlay bundles regenerated with Track 2F-bis sections | verified exploratory baseline; not promoted |
| 2026-06-04 | `Track 2F` offset-aware probe refresh | `3` `global`, `Fw`, and `Bw` sequential residual offset candidates | included in the `114`-candidate matrix | dated collage and overlay bundles regenerated | verified exploratory baseline; not promoted |
| 2026-05-28 | `Wave 2C` residual harmonic temporal hybrid refresh | `18` `global`, `Fw`, and `Bw` residual harmonic GRU/LSTM candidates | included in the `111`-candidate matrix | collage and overlay reports refreshed with `Wave 2C` sections | verified exploratory baseline; not promoted over `Wave 2B` or accepted Track 2 baselines |
| 2026-05-26 | `Wave 2B` harmonic temporal hybrid refresh | periodic temporal convolution, GRU, and LSTM `global`, `Fw`, and `Bw` candidates | included | collage and overlay reports refreshed | strongest repository-owned neural branch |

## Closeout Decision

`Track 2H` quantile/probabilistic regression does not change the accepted
`Track 2` baseline. The current direction-parallel decision remains:

- `Fw`: `rcim_retuned_GBM19_Fw` remains the strongest overall forward
  candidate; within this package, `track2h_gaussian_nll_Fw` is the strongest
  forward-only probabilistic candidate, but `track2h_gaussian_nll_global`
  performs better on forward curves.
- `Bw`: `periodic_gru_sequence_Bw` remains the strongest practical
  repository-owned backward candidate; `track2h_quantile_p10_p50_p90_Bw` is
  the strongest probabilistic backward candidate and improves over both the
  robust-loss Track 2H backward candidate and `tree_Bw` on Track 2 MAE.
- `global`: `periodic_gru_sequence_global` remains the strongest
  repository-owned bidirectional neural candidate; within the probabilistic
  package, `track2h_gaussian_nll_global` is clearly the best global surface
  and improves over the best robust-loss global Track 2H result.

The next modeling step should keep probabilistic losses as a validated
ingredient for dispersion-aware training. The evidence supports moving to
mixture-density heads and latent-state or hysteresis-aware variants before
deciding which mechanisms belong inside the integrated multi-task /
multi-head branch.
