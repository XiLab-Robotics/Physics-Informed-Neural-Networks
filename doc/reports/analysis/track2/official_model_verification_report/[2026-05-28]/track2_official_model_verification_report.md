# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This update accepts the completed `Wave 2.3` residual harmonic temporal hybrid
campaign into the official `TE Curve Verification Pipeline` offline verification package.

Decision:

- `Wave 2.3` is verified as an exploratory residual harmonic temporal baseline.
- No `Wave 2.3` candidate is promoted over the current `Wave 2.2` periodic
  sequence leaders.
- The accepted paper-derived forward baseline remains `paper_retuned_best_Fw`.
- The accepted paper-derived backward baseline remains `paper_retuned_best_Bw`.
- The strongest repository-owned static `TE Curve Verification Pipeline` baseline remains `tree`.
- The strongest repository-owned neural branch remains `Wave 2.2`
  `periodic_gru_sequence_Bw` for backward-only evaluation and
  `periodic_gru_sequence_global` for bidirectional neural evaluation.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-05-28-12-22-56__track2_full_directional_family_matrix_wave2c_residual_harmonic_temporal_hybrid_track2_refresh_2026_05_28/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-05-28-12-22-56__track2_full_directional_family_matrix_wave2c_residual_harmonic_temporal_hybrid_track2_refresh_2026_05_28/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-05-28]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-28]/track2_multi_model_curve_comparison_report.md`.

## Candidate Refresh

The refresh added `18` registry-backed `Wave 2.3` candidates:

| Family | Surfaces |
| --- | --- |
| `residual_harmonic_gru_sequence_sparse_rcim` | `global`, `Fw`, `Bw` |
| `residual_harmonic_gru_sequence_dense240` | `global`, `Fw`, `Bw` |
| `residual_harmonic_gru_sequence_dense360` | `global`, `Fw`, `Bw` |
| `residual_harmonic_lstm_sequence_sparse_rcim` | `global`, `Fw`, `Bw` |
| `residual_harmonic_lstm_sequence_dense240` | `global`, `Fw`, `Bw` |
| `residual_harmonic_lstm_sequence_dense360` | `global`, `Fw`, `Bw` |

The matrix now contains `111` candidates. The incremental operator run used the
completed `Wave 2.2` refresh as its `93`-candidate baseline and evaluated only
the `18` new `Wave 2.3` candidates.

## Current Leaders

| Scope | Current strongest candidate | MAE [deg] | RMSE [deg] | Mean [%] |
| --- | --- | ---: | ---: | ---: |
| forward overall | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 |
| backward overall | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 |
| paper-derived forward | `paper_retuned_best_Fw` | 0.001839 | 0.002041 | 4.109 |
| paper-derived backward | `paper_retuned_best_Bw` | 0.003675 | 0.004284 | 7.572 |
| repository static backward | `tree_Bw` | 0.003258 | 0.003651 | 7.051 |
| repository global static | `tree_global` | 0.003144 | 0.003533 | 6.854 |
| repository global neural | `periodic_gru_sequence_global` | 0.002704 | 0.002949 | 6.139 |

## Wave 2.3 Result

The strongest `Wave 2.3` candidates are:

| Scope | Strongest Wave 2.3 candidate | MAE [deg] | RMSE [deg] | Mean [%] |
| --- | --- | ---: | ---: | ---: |
| forward | `residual_harmonic_gru_sequence_sparse_rcim_Fw` | 0.003194 | 0.003499 | 7.083 |
| backward | `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | 0.003440 | 0.003793 | 7.510 |
| global | `residual_harmonic_lstm_sequence_sparse_rcim_global` | 0.003368 | 0.003719 | 7.409 |

The sparse `RCIM` harmonic set is clearly the best `Wave 2.3` setting. The
dense `240` and dense `360` residual harmonic variants are not competitive in
the official matrix and appear to over-expand the harmonic base for this
residual sequence branch.

## Visual Evidence

The refreshed best-model collage report includes dedicated `Wave 2.3` sections
for forward, backward, and global candidates. The refreshed multi-model overlay
report includes dedicated `Wave 2.3` overlays and direct reference/tree versus
`Wave 2.3` overlays.

Visual bundle paths:

- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-28]/track2_best_model_collage_report.pdf`;
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-28]/track2_multi_model_curve_comparison_report.pdf`.

## Campaign Update Ledger

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-05-28 | `Wave 2.3` residual harmonic temporal hybrid refresh | `18` `global`, `Fw`, and `Bw` residual harmonic GRU/LSTM candidates | included in the `111`-candidate matrix | collage and overlay reports refreshed with `Wave 2.3` sections | verified exploratory baseline; not promoted over `Wave 2.2` or accepted TE Curve Verification Pipeline baselines |
| 2026-05-26 | `Wave 2.2` harmonic temporal hybrid refresh | periodic temporal convolution, GRU, and LSTM `global`, `Fw`, and `Bw` candidates | included | collage and overlay reports refreshed | strongest repository-owned neural branch |
| 2026-05-24 | `Wave 2.1` temporal entry refresh | temporal convolution, GRU, and LSTM `global`, `Fw`, and `Bw` candidates | included | visual reports refreshed | verified exploratory baseline |
| 2026-05-21 | `periodic_mlp` explicit harmonic registry refresh | `global`, `Fw`, `Bw` visual verification | source matrix unchanged; visual registry refresh included | collage and overlay PDFs refreshed | included as visual evidence, not promoted over `tree` |

## Closeout Decision

`Wave 2.3` does not change the accepted `TE Curve Verification Pipeline` baseline. Its practical value
is diagnostic: it confirms that adding a residual recurrent branch over the
structured harmonic base is viable only with the sparse `RCIM` harmonic set,
while the dense harmonic banks are dimensionally expensive and less accurate.

The next modeling decision should keep `Wave 2.2` periodic sequence models as
the strongest neural branch and treat `Wave 2.3` as a verified exploratory
baseline rather than the next promotion target.

## Curve-First Follow-Up

The next approved analysis direction is curve-first reranking before any new
training campaign. The reason is practical compensation: future deployed
models must follow complete TE curves for many consecutive motor revolutions,
not only reduce pointwise scalar error on the dataset.

Follow-up rules:

- keep this official report as the accepted `Wave 2.3` TE Curve Verification closeout;
- do not reopen `Wave 1`, `Wave 2.1`, `Wave 2.2`, or `Wave 2.3`;
- create a separate `CVP 1.1 Curve-First Reranking` branch that evaluates
  accepted candidates on expanded full-curve metrics;
- preserve causal runtime inputs: current point-level operating state, optional
  short past-history windows, and derived causal features only;
- separate scalar registry winner, curve-first offline winner, and future
  deployment-ready candidate in later summaries.
