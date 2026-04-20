# Track 1 Remaining Family Residual Cellwise Closure Campaign Results Report

## Overview

This report closes the residual exact-paper `Track 1` retry wave prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-19-01-04-28_track1_remaining_family_residual_cellwise_closure_campaigns_plan_report.md`

The batch targeted every non-`SVM` family-harmonic pair that still remained
`ðŸŸ¡` or `ðŸ”´` after the earlier `171`-run cellwise reference wave.

- completed family campaigns: `9`
- completed validation runs: `1026`
- failed validation runs: `0`
- promoted residual pair winners: `90/171`
- aggregate campaign artifact root:
  `output/training_campaigns/track1/exact_paper/track1_remaining_family_residual_cellwise_closure_campaigns_2026_04_19_01_04_28/`

## Operational Outcome

- every residual family campaign now exposes:
  - `campaign_leaderboard.yaml`
  - `campaign_best_run.yaml`
  - `campaign_best_run.md`
- the aggregate residual campaign root now exposes the final `1026`-entry
  leaderboard and deterministic bookkeeping representative
- `doc/running/active_training_campaign.yaml` now records the canonical results
  report path for the completed residual retry wave
- the canonical benchmark now reads from the best accepted pair winner across:
  - the earlier `171`-run `cellwise_reference` wave
  - the newer `1026`-run residual retry wave

## Family Recovery Outcome

The table below uses compact display aliases for PDF fit. The exact canonical
run names remain serialized in the family campaign leaderboards and best-run
artifacts under `output/training_campaigns/`.

| Family | Amplitude Run | Phase Run | Best Run | Best Scope | Best Closure Score | Open Cells |
| --- | --- | --- | --- | --- | ---: | ---: |
| `MLP` | `A162 a01` | `P156 a01` | `A162 a01` | `amplitudes_only` | 1.000 | `0` |
| `RF` | `A0 a03` | `P156 a01` | `A0 a03` | `amplitudes_only` | 1.000 | `0` |
| `DT` | `A0 a02` | `P156 a01` | `A0 a02` | `amplitudes_only` | 1.000 | `0` |
| `ET` | `A0 a01` | `P156 a01` | `A0 a01` | `amplitudes_only` | 1.000 | `0` |
| `ERT` | `A0 a02` | `P156 a01` | `A0 a02` | `amplitudes_only` | 1.000 | `0` |
| `GBM` | `A0 a02` | `P156 a01` | `A0 a02` | `amplitudes_only` | 1.000 | `0` |
| `HGBM` | `A0 a03` | `P156 a01` | `A0 a03` | `amplitudes_only` | 1.000 | `0` |
| `XGBM` | `A0 a02` | `P156 a01` | `A0 a02` | `amplitudes_only` | 1.000 | `0` |
| `LGBM` | `A0 a02` | `P156 a01` | `A0 a02` | `amplitudes_only` | 1.000 | `0` |

## Aggregate Ranking

The aggregate ranking below also uses compact run aliases for PDF fit. The
exact run names remain preserved in the aggregate leaderboard and family-level
campaign artifacts.

| Rank | Run | Family | Scope | Paper Cell | Met | Near | Open | Closure Score |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `1` | `A0 a02` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `2` | `A0 a05` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `3` | `A156 a02` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `4` | `A162 a02` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `5` | `A1 a02` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `6` | `A1 a05` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `7` | `A240 a01` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `8` | `A240 a02` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `9` | `A240 a03` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `10` | `A240 a04` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `11` | `A240 a05` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `12` | `A240 a06` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `13` | `A39 a01` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `14` | `A39 a02` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `15` | `A39 a03` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |

## Final Batch Winner

The aggregate batch bookkeeping representative is
`track1_dt_amplitude_0_closure_attempt_02` from family `DT`.

This is a deterministic winner under the per-run closure-first policy across
the full `1026`-entry residual batch. It should be read as a bookkeeping
representative of the completed campaign, not as the whole scientific verdict
of the promoted pairwise residual upgrades.

- winning scope: `amplitudes_only`
- closure score: `1.000`
- met paper cells: `2`
- near paper cells: `0`
- open paper cells: `0`

## Scientific Outcome

- the residual retry wave materially improved the accepted benchmark surface
  without changing the exact-paper family definitions
- amplitude `RMSE` closure rises to `10/10`
- phase `MAE` closure rises to `9/9`
- phase `RMSE` closure rises to `8/9`
- amplitude `MAE` closure rises to `7/10`
- no harmonic remains fully red in Table `6`
- `Track 1` remains canonically open because the harmonic-level family
  alignment rule is still not fully satisfied

## Final Benchmark Refresh Effect

The canonical benchmark after the residual retry closeout is:

- Table `2` amplitude `MAE`: `7/10` harmonics meet or beat the paper target
- Table `3` amplitude `RMSE`: `10/10` harmonics meet or beat the paper target
- Table `4` phase `MAE`: `9/9` harmonics meet or beat the paper target
- Table `5` phase `RMSE`: `8/9` harmonics meet or beat the paper target
- harmonic-level Table `6` closure: `2/10` fully matched, `8/10` partially
  matched, `0/10` not yet matched

The highest-priority still-open harmonics are now:

- `0`
- `3`
- `39`
- `78`
- `81`
- `156`
- `162`
- `240`

## Final Interpretation

This batch is operationally complete and materially stronger than the earlier
non-`SVM` cellwise reference wave.

The key final conclusion is:

- the residual retry wave is fully closed out
- the repository now has the aggressive `1026`-run residual retry evidence on
  top of the earlier `171` exact-paper reference runs
- the canonical benchmark and Tables `2-5` now read from the best accepted pair
  winner across both waves
- `Track 1` is no longer numerically blocked by broad red surfaces; the
  remaining work is concentrated on harmonic-level family alignment in Table `6`
