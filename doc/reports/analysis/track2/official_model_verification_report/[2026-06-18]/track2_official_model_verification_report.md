# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This official closure report accepts the completed `Wave 4.4`
latent-state hysteresis refresh into the canonical `TE Curve Verification Pipeline` evidence package.

Decision:

- `track2h_latent_state_hysteresis_registry` is closed as a verified
  exploratory baseline.
- No `Wave 4.4` candidate is promoted over the accepted direction-parallel
  leaders.
- The strongest refreshed `Wave 4.4` aggregate candidate is
  `track2h_l_causal_tcn_offset_residual_global`.
- The accepted direction-parallel leaders remain `rcim_retuned_GBM19_Fw`,
  `periodic_gru_sequence_Bw`, and the accepted global neural
  `periodic_gru_sequence_global`.
- The closure keeps latent-state / hysteresis-aware modeling as integration
  evidence for later multi-head work, not as the next standalone promoted
  family.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-06-18-15-20-21__track2_full_directional_family_matrix_track2h_latent_state_hysteresis_track2_refresh_2026_06_18/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-06-18-15-20-21__track2_full_directional_family_matrix_track2h_latent_state_hysteresis_track2_refresh_2026_06_18/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-06-18]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-18]/track2_multi_model_curve_comparison_report.md`;
- operator launch logs:
  `output/validation_checks/track2_operator_launch_logs/2026-06-18-15-20-09_track2h_latent_state_hysteresis_track2_refresh_2026_06_18`.

## Candidate Refresh

The refresh added `6` candidates from `track2h_latent_state_hysteresis_registry` into the official `165`-candidate matrix.

| Surface | Candidate | Family |
| --- | --- | --- |
| global | `track2h_l_gru_offset_residual_global` | `track2h_l_gru_offset_residual` |
| Fw | `track2h_l_gru_offset_residual_Fw` | `track2h_l_gru_offset_residual` |
| Bw | `track2h_l_gru_offset_residual_Bw` | `track2h_l_gru_offset_residual` |
| global | `track2h_l_causal_tcn_offset_residual_global` | `track2h_l_causal_tcn_offset_residual` |
| Fw | `track2h_l_causal_tcn_offset_residual_Fw` | `track2h_l_causal_tcn_offset_residual` |
| Bw | `track2h_l_causal_tcn_offset_residual_Bw` | `track2h_l_causal_tcn_offset_residual` |

## Refreshed Source Leaders

The table ranks the refreshed source by aggregate offline TE Curve Verification Pipeline metrics.

| Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| Fw | `track2h_l_causal_tcn_offset_residual_Fw` | 0.003476 | 0.003939 | 7.717 | 13.330 |
| Bw | `track2h_l_gru_offset_residual_Bw` | 0.003542 | 0.003984 | 7.736 | 12.831 |
| global | `track2h_l_causal_tcn_offset_residual_global` | 0.003372 | 0.003827 | 7.398 | 13.454 |

Interpretation:

- `global`: causal TCN is the best `Wave 4.4` aggregate candidate, but it
  remains behind the accepted global neural baseline and behind the strongest
  probabilistic `Wave 4 series` global scalar evidence.
- `Fw`: causal TCN is the best `Wave 4.4` forward candidate, but its
  `0.003476 deg` curve MAE is far behind `rcim_retuned_GBM19_Fw`
  at `0.001089 deg`.
- `Bw`: GRU is the best `Wave 4.4` backward candidate, but its
  `0.003542 deg` curve MAE is behind `periodic_gru_sequence_Bw`
  at `0.002392 deg`.

## Refreshed Source Leaderboard

| Rank | Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | global | `track2h_l_causal_tcn_offset_residual_global` | 0.003372 | 0.003827 | 7.398 | 13.454 |
| 2 | Fw | `track2h_l_causal_tcn_offset_residual_Fw` | 0.003476 | 0.003939 | 7.717 | 13.330 |
| 3 | Bw | `track2h_l_gru_offset_residual_Bw` | 0.003542 | 0.003984 | 7.736 | 12.831 |
| 4 | Fw | `track2h_l_gru_offset_residual_Fw` | 0.003549 | 0.003996 | 7.873 | 12.664 |
| 5 | global | `track2h_l_gru_offset_residual_global` | 0.003591 | 0.004024 | 7.896 | 12.986 |
| 6 | Bw | `track2h_l_causal_tcn_offset_residual_Bw` | 0.003624 | 0.004098 | 7.903 | 13.135 |

## Current Direction Leaders

These leaders are read from the matrix direction breakdown after the refresh.

| Direction | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| backward | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 | 14.820 |
| forward | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |

The current accepted direction-parallel baselines do not change.

## Multi-Index Closure

This refresh provides raw-error and visual-evidence coverage for the
`Wave 4.4` source. The companion collage and overlay reports show that the
latent-state candidates follow the broad TE curve trend, but they still show
visible offset and high-frequency mismatch on representative conditions. The
available evidence does not justify promotion on raw error, offset /
continuity behavior, harmonic / phase fidelity, robustness, or deployment
readiness.

The official closure therefore treats `Wave 4.4` as useful evidence that
causal history can help the `global` scalar surface, while rejecting it as a
standalone replacement for the accepted forward, backward, or global TE Curve Verification Pipeline
leaders.

## Visual Evidence

The same launcher run regenerated the visual companion reports and verified
that the refreshed source appears in the visual package.

| Source | Collage | Overlay Forward | Overlay Backward |
| --- | ---: | ---: | ---: |
| `track2h_latent_state_hysteresis_registry` | 6 | 2 | 2 |

## Closeout Decision

`Wave 4.4 latent-state hysteresis refresh` is closed as a verified
exploratory baseline and is not promoted.

Use the latent-state hysteresis evidence as a later integration ingredient
when comparing multi-head designs that combine causal state, offset handling,
uncertainty, mixture pressure, and structured harmonic residuals.
