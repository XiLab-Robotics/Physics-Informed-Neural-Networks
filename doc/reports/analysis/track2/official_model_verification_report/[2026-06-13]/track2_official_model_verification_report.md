# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This update accepts the completed `Wave 4.3` mixture-density heads campaign
into the official `TE Curve Verification Pipeline` offline verification matrix.

Decision:

- `Wave 4.3` mixture-density heads are verified as an exploratory
  dispersion-aware baseline.
- No MDN candidate is promoted over the current accepted `TE Curve Verification Pipeline` leaders.
- The strongest MDN forward candidate is `track2h_mdn_k3_Fw`.
- The strongest MDN backward candidate is `track2h_mdn_k2_Bw`.
- The strongest MDN global candidate is `track2h_mdn_k2_global`.
- The best MDN backward candidate improves over the previous
  quantile/probabilistic and robust-loss `Wave 4 series` backward branches, but it
  remains behind the accepted periodic temporal backward leader.
- The project continues to maintain direction-parallel `Fw`, `Bw`, and
  `global` surfaces instead of collapsing them into one scalar ranking.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-06-13-17-24-53__track2_full_directional_family_matrix_track2h_mixture_density_heads_track2_refresh_2026_06_13/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-06-13-17-24-53__track2_full_directional_family_matrix_track2h_mixture_density_heads_track2_refresh_2026_06_13/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-06-13]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-13]/track2_multi_model_curve_comparison_report.md`;
- operator launch logs:
  `output/validation_checks/track2_operator_launch_logs/2026-06-13-17-24-48_track2h_mixture_density_heads_track2_refresh_2026_06_13/`.

## Candidate Refresh

The refresh added `6` registry-backed `Wave 4.3` MDN candidates covering
two- and three-component mixture heads across the `global`, `Fw`, and `Bw`
surfaces.

| Surface | Profile | Deterministic Curve | Candidate |
| --- | --- | --- | --- |
| `global` | `mdn_k2` | mixture expectation | `track2h_mdn_k2_global` |
| `Fw` | `mdn_k2` | mixture expectation | `track2h_mdn_k2_Fw` |
| `Bw` | `mdn_k2` | mixture expectation | `track2h_mdn_k2_Bw` |
| `global` | `mdn_k3` | mixture expectation | `track2h_mdn_k3_global` |
| `Fw` | `mdn_k3` | mixture expectation | `track2h_mdn_k3_Fw` |
| `Bw` | `mdn_k3` | mixture expectation | `track2h_mdn_k3_Bw` |

The matrix source group is `track2h_mixture_density_heads_registry`. The
matrix now contains `153` candidates.

## Verification Rules

| Surface | Training or Archive Scope | Evaluation Scope |
| --- | --- | --- |
| `Fw` | forward-only training or archive | forward TE Curve Verification Pipeline curves only |
| `Bw` | backward-only training or archive | backward TE Curve Verification Pipeline curves only |
| `global` | forward and backward training together | both directions, reported by direction and combined |

The MDN heads are not compared as raw mixture tensors. The official matrix
evaluates only the deterministic TE curve exposed by each checkpoint: the
mixture expectation computed from component logits and component means.

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

## Wave 4.3 Mixture Density Result

| Surface | Candidate | Profile | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `Bw` | `track2h_mdn_k2_Bw` | `mdn_k2` | 0.002668 | 0.002947 | 5.880 | 15.593 |
| `Bw` | `track2h_mdn_k3_Bw` | `mdn_k3` | 0.002730 | 0.003009 | 6.049 | 15.512 |
| `global forward` | `track2h_mdn_k2_global` | `mdn_k2` | 0.003263 | 0.003582 | 7.261 | 14.354 |
| `Fw` | `track2h_mdn_k3_Fw` | `mdn_k3` | 0.003226 | 0.003487 | 7.164 | 11.702 |
| `Fw` | `track2h_mdn_k2_Fw` | `mdn_k2` | 0.003329 | 0.003593 | 7.388 | 12.771 |
| `global forward` | `track2h_mdn_k3_global` | `mdn_k3` | 0.003415 | 0.003713 | 7.594 | 15.012 |
| `global backward` | `track2h_mdn_k3_global` | `mdn_k3` | 0.003701 | 0.004023 | 8.129 | 16.261 |
| `global backward` | `track2h_mdn_k2_global` | `mdn_k2` | 0.003735 | 0.004073 | 8.194 | 15.436 |

The strongest MDN `Bw` candidate improves over the best
quantile/probabilistic `Bw` candidate from `0.002935` to `0.002668` TE Curve Verification Pipeline
MAE. It also improves over the best robust-loss `Bw` candidate from
`0.003078` to `0.002668` curve-verification MAE. This makes `track2h_mdn_k2_Bw` the
strongest `Wave 4 series` backward surface so far.

The same improvement does not carry over to `Fw` or `global`. The strongest
MDN `Fw` candidate remains behind the best probabilistic `Fw` candidate, and
both MDN global candidates remain weaker than the best probabilistic global
surface. The campaign-level mixture diagnostics also showed effective
component counts near `1.0`, so this official refresh does not prove a stable
learned multimodal TE distribution.

## Visual Evidence

The `2026-06-13` collage and overlay bundles were regenerated after the MDN
refresh. They include explicit `Wave 4.3` mixture-density sections for `Fw`,
`Bw`, and `global` collage evidence, plus explicit `Fw` and `Bw` MDN overlay
sections.

The visual source-coverage validator passed with
`track2h_mixture_density_heads_registry` exposed in both visual reports:
`collage=6`, `overlay_forward=2`, and `overlay_backward=2`.

The visual package supports the matrix decision: MDN is a useful
dispersion-aware backward branch, but it does not replace the strongest
periodic temporal branch or the forward paper-reference leader.

## Campaign Update Ledger

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-06-13 | `Wave 4.3` mixture-density heads refresh | `6` MDN `global`, `Fw`, and `Bw` candidates | included in the `153`-candidate matrix | dated collage and overlay bundles regenerated with MDN sections | verified exploratory baseline; not promoted |
| 2026-06-12 | `Wave 4.2` quantile/probabilistic refresh | `6` quantile and Gaussian `global`, `Fw`, and `Bw` candidates | included in the `147`-candidate matrix | dated collage and overlay bundles regenerated | verified exploratory baseline; not promoted |
| 2026-06-11 | `Wave 4.1` robust-loss dispersion-aware refresh | `9` robust `global`, `Fw`, and `Bw` candidates | included in the `141`-candidate matrix | dated collage and overlay bundles regenerated with Wave 4 series sections | verified exploratory baseline; not promoted |
| 2026-06-10 | `Wave 3.3` curve-aware training refresh | `12` pointwise-control, centered-shape, offset, and full-composite `global`, `Fw`, and `Bw` candidates | included in the `132`-candidate matrix | dated collage and overlay bundles regenerated with Wave 3.3 sections | verified exploratory baseline; not promoted |
| 2026-06-08 | `Wave 3.2` harmonic-offset probe refresh | `6` clean and harmonic `global`, `Fw`, and `Bw` candidates plus `3` rechecked Wave 3.1 candidates | included in the `120`-candidate matrix | dated collage and overlay bundles regenerated with Wave 3.2 sections | verified exploratory baseline; not promoted |
| 2026-06-04 | `Wave 3.1` offset-aware probe refresh | `3` `global`, `Fw`, and `Bw` sequential residual offset candidates | included in the `114`-candidate matrix | dated collage and overlay bundles regenerated | verified exploratory baseline; not promoted |
| 2026-05-28 | `Wave 2.3` residual harmonic temporal hybrid refresh | `18` `global`, `Fw`, and `Bw` residual harmonic GRU/LSTM candidates | included in the `111`-candidate matrix | collage and overlay reports refreshed with `Wave 2.3` sections | verified exploratory baseline; not promoted over `Wave 2.2` or accepted TE Curve Verification Pipeline baselines |

## Closeout Decision

`Wave 4.3` mixture-density heads do not change the accepted `TE Curve Verification Pipeline`
baseline. The current direction-parallel decision remains:

- `Fw`: `rcim_retuned_GBM19_Fw` remains the strongest overall forward
  candidate. Within the MDN package, `track2h_mdn_k3_Fw` is the strongest
  forward-only candidate, but it trails the best probabilistic forward branch.
- `Bw`: `periodic_gru_sequence_Bw` remains the strongest accepted
  repository-owned backward candidate. Within the MDN package,
  `track2h_mdn_k2_Bw` is the strongest backward candidate and the strongest
  `Wave 4 series` backward result so far.
- `global`: `periodic_gru_sequence_global` remains the strongest accepted
  bidirectional neural candidate. Within the MDN package,
  `track2h_mdn_k2_global` is the strongest global surface, but it trails the
  best probabilistic global candidate.

The next modeling step should not be another MDN-only variant. The evidence
supports moving to the first real `Wave 5.1` hybrid structured campaign, while
keeping robust and probabilistic losses as candidate ingredients for later
multi-task / multi-head integration. A latent-state / hysteresis-aware Track
2H branch remains justified if the next decision is to pursue experimental
state compensation before structured harmonic priors.
