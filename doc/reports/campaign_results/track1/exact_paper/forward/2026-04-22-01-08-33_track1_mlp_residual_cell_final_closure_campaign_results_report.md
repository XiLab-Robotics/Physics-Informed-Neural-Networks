# Track 1 MLP Residual Cell Final Closure Campaign Results Report

## Overview

This report closes the dedicated exact-paper residual-cell `MLP` wave
prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-21-23-32-36_track1_mlp_residual_cell_final_closure_campaign_plan_report.md`

The campaign targeted only the last four distinct accepted `MLP`
family-target pairs that were still non-green in the canonical `Track 1`
full-matrix benchmark.

- campaign name: `track1_mlp_residual_cell_final_closure_campaign_2026_04_21_23_32_36`
- report timestamp: `2026-04-22-01-08-33`
- completed validation runs: `216`
- failed validation runs: `0`
- promoted targeted pairs: `4/4`
- retained baseline pairs: `0/4`
- visibly promoted benchmark cells: `7/8`
- campaign artifact root: `output/training_campaigns/track1/exact_paper/forward/family_repair/mlp/track1_mlp_residual_cell_final_closure_campaign_2026_04_21_23_32_36`

## Campaign Winner

- Run: `track1_mlp_amplitude_156_final_closure_attempt_32`
- Scope: `amplitudes_only`
- Closure Score: `1.000`
- Met / Near / Open: `2` / `0` / `0`

## Targeted Pair Outcome

The table below compares the accepted pre-wave baseline against the best
campaign-local candidate and the final accepted post-wave value for each
targeted residual `MLP` pair. Each metric cell is shown as `MAE / RMSE`.

| Pair | Baseline | Campaign Best | Accepted | Source | Result |
| --- | --- | --- | --- | --- | --- |
| `A1` | `0.00755033 / 0.0137694` | `0.00476074 / 0.00898767` | `0.00476074 / 0.00898767` | `campaign` | `fully_green` |
| `A156` | `0.00682945 / 0.011491` | `0.00644413 / 0.0106664` | `0.00644413 / 0.0106664` | `campaign` | `fully_green` |
| `A240` | `0.00638307 / 0.0121452` | `0.00524356 / 0.00911022` | `0.00524356 / 0.00911022` | `campaign` | `fully_green` |
| `phi162` | `0.826864 / 1.33334` | `0.826864 / 1.29701` | `0.826864 / 1.29701` | `mixed` | `still_non_green` |

## Accepted MLP Row After Closeout

- `Table 2` remaining non-green harmonics: `none`
- `Table 3` remaining non-green harmonics: `none`
- `Table 4` remaining non-green harmonics: `162`
- `Table 5` remaining non-green harmonics: `162`
- total remaining non-green `MLP` cells on Tables `2-5`: `2`

## Canonical Track 1 Impact

- This residual `MLP` wave updates the accepted `MLP` family row without
  changing the canonical Track 1 scope definition.
- The benchmark row now keeps the better visible metric cell between the
  accepted baseline and this dedicated residual closure wave.
- The cross-family closure counts should now be read directly from the
  refreshed benchmark after this closeout.

## Resulting Canonical State

- benchmark path: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- master summary path: `doc/reports/analysis/Training Results Master Summary.md`
- final closeout report path: `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-22-01-08-33_track1_mlp_residual_cell_final_closure_campaign_results_report.md`
