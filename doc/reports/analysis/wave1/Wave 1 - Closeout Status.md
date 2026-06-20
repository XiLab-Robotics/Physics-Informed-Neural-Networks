# Wave 1 Closeout Status And Consolidated Summary Report

## Executive Summary

`Wave 1` remains closed with a directional `global` / `forward` /
`backward` comparison surface. The latest completed optimization pass is
the directional best-hyperparameter search campaign.

- Current HPO leader: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10`
- Leader family: `tree_fw`
- Leader scope: `forward`
- Leader test MAE: `0.002743 deg`
- Full HPO closeout report: `doc\reports\campaign_results\wave_1\2026-05-17-11-40-42_wave1_directional_best_hyperparameter_search_campaign_results_report.md`

Curve-first interpretation:

- this report remains the scalar HPO closeout for `Wave 1`;
- the final compensation target is continuous TE-curve prediction, so scalar
  `MAE` is not sufficient promotion evidence by itself;
- future `Wave 1B` work should rerank accepted `Wave 1` artifacts on the full
  `TE Curve Verification Pipeline` curve surface before retraining or changing model families;
- curve-first reranking must not reinterpret `Wave 1` as a non-causal
  full-curve-input model; inputs remain point-level operating states unless a
  later approved branch adds only past-history features;
- the governing strategy is
  `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`.

## HPO Surface Ranking

| Rank | Family | Scope | Engine | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `1` | `tree_fw` | `forward` | `bounded_grid` | 0.002677 | 0.002743 | 0.003409 |
| `2` | `tree` | `global` | `bounded_grid` | 0.002655 | 0.002782 | 0.003520 |
| `3` | `tree_bw` | `backward` | `bounded_grid` | 0.002681 | 0.002954 | 0.003749 |
| `4` | `harmonic_regression_fw` | `forward` | `bounded_grid` | 0.002848 | 0.003101 | 0.003527 |
| `5` | `periodic_mlp_bw` | `backward` | `optuna` | 0.002907 | 0.003233 | 0.003792 |
| `6` | `periodic_mlp` | `global` | `optuna` | 0.002964 | 0.003233 | 0.003733 |
| `7` | `feedforward_bw` | `backward` | `optuna` | 0.002875 | 0.003276 | 0.003767 |
| `8` | `feedforward_fw` | `forward` | `optuna` | 0.002746 | 0.003287 | 0.003911 |
| `9` | `periodic_mlp_fw` | `forward` | `optuna` | 0.002751 | 0.003294 | 0.003899 |
| `10` | `residual_harmonic_mlp_fw` | `forward` | `optuna` | 0.002759 | 0.003354 | 0.003995 |
| `11` | `residual_harmonic_mlp` | `global` | `optuna` | 0.002868 | 0.003428 | 0.003928 |
| `12` | `feedforward` | `global` | `optuna` | 0.002958 | 0.003446 | 0.004158 |
| `13` | `residual_harmonic_mlp_bw` | `backward` | `optuna` | 0.002930 | 0.003454 | 0.003918 |
| `14` | `harmonic_regression_bw` | `backward` | `bounded_grid` | 0.003638 | 0.003494 | 0.004081 |
| `15` | `harmonic_regression` | `global` | `bounded_grid` | 0.017025 | 0.020774 | 0.022412 |
