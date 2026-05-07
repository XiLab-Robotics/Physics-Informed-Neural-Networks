# Wave 1 Closeout Status And Consolidated Summary Report

## Executive Summary

`Wave 1` remains closed, but its canonical comparison surface is now directional.

The repository now treats each `Wave 1` family as a triad of winners:

- one `global` model trained on the full directional dataset;
- one `forward` model trained on the forward-only split;
- one `backward` model trained on the backward-only split.

The current Wave 1 directional leader is `te_hist_gbr_tabular_Fw` from `tree_fw` with `test_mae = 0.002845 deg`.

## Family Directional Summary

| Family | Global Test MAE [deg] | Forward Test MAE [deg] | Backward Test MAE [deg] | Best Scope |
| --- | ---: | ---: | ---: | --- |
| `tree` | 0.002885 | 0.002845 | 0.003087 | `forward` |
| `residual_harmonic_mlp` | 0.003152 | 0.003530 | 0.003493 | `global` |
| `feedforward` | 0.003150 | 0.003563 | 0.003262 | `global` |
| `periodic_mlp` | 0.003317 | 0.003432 | 0.003525 | `global` |
| `harmonic_regression` | 0.020779 | 0.003129 | 0.003524 | `forward` |

## Operational Consequences

- Cross-family comparisons should now use like-for-like directional scopes instead of comparing a directional paper branch against an older all-directions repository baseline.
- Future model-family waves should materialize the same `global` plus `forward` plus `backward` surface and refresh `models/exported/` during closeout.
- The full closeout evidence bundle for this transition is the final campaign report `doc/reports/campaign_results/wave1/2026-05-07-13-29-12_wave1_directional_retraining_campaign_results_report.md`.
