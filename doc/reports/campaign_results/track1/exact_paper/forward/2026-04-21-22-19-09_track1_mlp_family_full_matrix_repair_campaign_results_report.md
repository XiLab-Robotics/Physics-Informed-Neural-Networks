# Track 1 MLP Family Full-Matrix Repair Campaign Results Report

## Overview

This report closes the dedicated exact-paper `MLP` family repair wave
prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-21-17-20-12_track1_mlp_family_full_matrix_repair_campaign_plan_report.md`

The campaign targeted only the `MLP` family-target pairs selected for the
post-relaunch repair pass across the canonical `Track 1` full-matrix
surfaces.

- campaign name: `track1_mlp_family_full_matrix_repair_campaign_2026_04_21_17_20_12`
- report timestamp: `2026-04-21-22-19-09`
- completed validation runs: `324`
- failed validation runs: `0`
- promoted targeted pairs: `1/12`
- retained baseline pairs: `11/12`
- visibly promoted benchmark cells: `1/24`
- campaign artifact root: `output/training_campaigns/track1/exact_paper/forward/family_repair/mlp/track1_mlp_family_full_matrix_repair_campaign_2026_04_21_17_20_12`

## Campaign Winner

- Run: `track1_mlp_amplitude_0_closure_attempt_17`
- Scope: `amplitudes_only`
- Closure Score: `1.000`
- Met / Near / Open: `2` / `0` / `0`

## Targeted Pair Outcome

The table below compares the accepted pre-wave baseline against the best
campaign-local candidate and the final accepted post-wave value for each
targeted `MLP` pair. Each metric cell is shown as `MAE / RMSE`.

| Pair | Baseline | Campaign Best | Accepted | Source | Result |
| --- | --- | --- | --- | --- | --- |
| `A0` | `0.0093971 / 0.013702` | `0.0093971 / 0.013702` | `0.0093971 / 0.013702` | `baseline` | `fully_green` |
| `A1` | `0.00755033 / 0.0137694` | `0.00755033 / 0.0137694` | `0.00755033 / 0.0137694` | `baseline` | `still_non_green` |
| `A3` | `0.00552258 / 0.00892685` | `0.00552258 / 0.00892685` | `0.00552258 / 0.00892685` | `baseline` | `fully_green` |
| `A39` | `0.00520776 / 0.00919113` | `0.00520776 / 0.00919113` | `0.00520776 / 0.00919113` | `baseline` | `fully_green` |
| `A40` | `0.00699309 / 0.0120674` | `0.00672959 / 0.0128006` | `0.00672959 / 0.0120674` | `mixed` | `fully_green` |
| `A81` | `0.00536461 / 0.00939595` | `0.00536461 / 0.00939595` | `0.00536461 / 0.00939595` | `baseline` | `fully_green` |
| `A156` | `0.00682945 / 0.011491` | `0.00682945 / 0.011491` | `0.00682945 / 0.011491` | `baseline` | `still_non_green` |
| `A240` | `0.00638307 / 0.0121452` | `0.00638307 / 0.0121452` | `0.00638307 / 0.0121452` | `baseline` | `still_non_green` |
| `phi1` | `0.00582546 / 0.00916257` | `0.00582546 / 0.00916257` | `0.00582546 / 0.00916257` | `baseline` | `fully_green` |
| `phi3` | `0.0590324 / 0.0742506` | `0.0590324 / 0.0742506` | `0.0590324 / 0.0742506` | `baseline` | `fully_green` |
| `phi39` | `0.0531587 / 0.0696308` | `0.0531587 / 0.0696308` | `0.0531587 / 0.0696308` | `baseline` | `fully_green` |
| `phi162` | `0.826864 / 1.33334` | `0.826864 / 1.33334` | `0.826864 / 1.33334` | `baseline` | `still_non_green` |

## Accepted MLP Row After Closeout

- `Table 2` remaining non-green harmonics: `1, 156, 240`
- `Table 3` remaining non-green harmonics: `1, 240`
- `Table 4` remaining non-green harmonics: `162`
- `Table 5` remaining non-green harmonics: `162`
- total remaining non-green `MLP` cells on Tables `2-5`: `7`

## Canonical Track 1 Impact

- This `MLP`-only wave updates the accepted `MLP` family row without
  reopening the already closed cross-family open-cell closeout.
- The benchmark row now keeps the better visible metric cell between the
  accepted baseline and this dedicated repair wave.
- Global `Track 1` cross-family closure counts remain unchanged at
  `7/10`, `10/10`, `9/9`, and `9/9` across Tables `2-5`.

## Resulting Canonical State

- benchmark path: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- master summary path: `doc/reports/analysis/Training Results Master Summary.md`
- final closeout report path: `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report.md`
