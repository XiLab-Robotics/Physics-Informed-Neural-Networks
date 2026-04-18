# Track 1 Remaining Family Final Closeout Campaign Results Report

## Overview

This report closes the full remaining-family exact-paper `Track 1` batch
prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-18-00-48-05_track1_remaining_exact_paper_family_campaigns_plan_report.md`

The earlier partial closeout already covered the first seven completed
families. This final report promotes the recovered `XGBM` and `LGBM` reruns
into the canonical campaign bookkeeping and removes the temporary
`pending rerun` state from the batch.

- completed family campaigns: `9`
- completed validation runs: `18`
- failed validation runs: `0`
- aggregate campaign artifact root:
  `output/training_campaigns/track1_remaining_family_full_matrix_campaigns_2026_04_18_00_48_05/`

## Operational Outcome

- the recovered `XGBM` rerun completed both amplitude and phase exact-paper runs
- the recovered `LGBM` rerun completed both amplitude and phase exact-paper runs
- the `XGBM` and `LGBM` family campaign folders now expose:
  - `campaign_leaderboard.yaml`
  - `campaign_best_run.yaml`
  - `campaign_best_run.md`
- the aggregate remaining-family campaign root now exposes the final `18`-entry
  leaderboard and the final winning run
- `doc/running/active_training_campaign.yaml` can now move from
  `interrupted` to `finished`

## Family Recovery Outcome

| Family | Amplitude Run | Phase Run | Best Run | Best Scope | Best Closure Score | Open Cells |
| --- | --- | --- | --- | --- | ---: | ---: |
| `XGBM` | `track1_xgbm_amplitude_full_matrix` | `track1_xgbm_phase_full_matrix` | `track1_xgbm_phase_full_matrix` | `phases_only` | 0.111 | `14` |
| `LGBM` | `track1_lgbm_amplitude_full_matrix` | `track1_lgbm_phase_full_matrix` | `track1_lgbm_amplitude_full_matrix` | `amplitudes_only` | 0.550 | `4` |

## Aggregate Ranking

| Rank | Run | Family | Scope | Paper Cell | Met | Near | Open | Closure Score |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `1` | `track1_rf_phase_full_matrix` | `RF` | `phases_only` | `18` | `7` | `8` | `3` | 0.611 |
| `2` | `track1_gbm_phase_full_matrix` | `GBM` | `phases_only` | `18` | `7` | `6` | `5` | 0.556 |
| `3` | `track1_hgbm_phase_full_matrix` | `HGBM` | `phases_only` | `18` | `6` | `8` | `4` | 0.556 |
| `4` | `track1_lgbm_amplitude_full_matrix` | `LGBM` | `amplitudes_only` | `10` | `5` | `1` | `4` | 0.550 |
| `5` | `track1_lgbm_phase_full_matrix` | `LGBM` | `phases_only` | `18` | `6` | `7` | `5` | 0.528 |
| `6` | `track1_ert_phase_full_matrix` | `ERT` | `phases_only` | `18` | `7` | `3` | `8` | 0.472 |
| `7` | `track1_hgbm_amplitude_full_matrix` | `HGBM` | `amplitudes_only` | `10` | `3` | `3` | `4` | 0.450 |
| `8` | `track1_ert_amplitude_full_matrix` | `ERT` | `amplitudes_only` | `10` | `2` | `3` | `5` | 0.350 |
| `9` | `track1_rf_amplitude_full_matrix` | `RF` | `amplitudes_only` | `10` | `1` | `5` | `4` | 0.350 |
| `10` | `track1_dt_phase_full_matrix` | `DT` | `phases_only` | `18` | `2` | `8` | `8` | 0.333 |
| `11` | `track1_gbm_amplitude_full_matrix` | `GBM` | `amplitudes_only` | `10` | `1` | `4` | `5` | 0.300 |
| `12` | `track1_et_phase_full_matrix` | `ET` | `phases_only` | `18` | `2` | `1` | `15` | 0.139 |
| `13` | `track1_xgbm_phase_full_matrix` | `XGBM` | `phases_only` | `18` | `0` | `4` | `14` | 0.111 |
| `14` | `track1_dt_amplitude_full_matrix` | `DT` | `amplitudes_only` | `10` | `0` | `2` | `8` | 0.100 |
| `15` | `track1_et_amplitude_full_matrix` | `ET` | `amplitudes_only` | `10` | `0` | `2` | `8` | 0.100 |
| `16` | `track1_xgbm_amplitude_full_matrix` | `XGBM` | `amplitudes_only` | `10` | `0` | `1` | `9` | 0.050 |
| `17` | `track1_mlp_amplitude_full_matrix` | `MLP` | `amplitudes_only` | `10` | `0` | `0` | `10` | 0.000 |
| `18` | `track1_mlp_phase_full_matrix` | `MLP` | `phases_only` | `18` | `0` | `0` | `18` | 0.000 |

## Final Batch Winner

The aggregate batch winner remains `track1_rf_phase_full_matrix` from family
`RF`.

The recovered `XGBM` and `LGBM` reruns materially complete the batch but do not
displace the existing aggregate winner under the explicit closure-first ranking
policy.

- winning scope: `phases_only`
- closure score: `0.611`
- met paper cells: `7`
- near paper cells: `8`
- open paper cells: `3`

## Scientific Outcome

- `XGBM` is now fully validated as a completed row, but it does not improve the
  canonical benchmark envelope materially
- `LGBM` closes the batch with a strong amplitude row and a competitive phase
  row
- the main final benchmark gains versus the earlier partial closeout come from
  `LGBM`:
  - harmonic `1` amplitude `MAE` moves from near-target to met-target
  - harmonic `3` amplitude `RMSE` moves from near-target to met-target
- the aggregate winner and the highest-priority open harmonics remain unchanged

## Final Benchmark Refresh Effect

The canonical benchmark after the full remaining-family closeout is:

- Table `2` amplitude `MAE`: `3/10` harmonics meet or beat the paper target
- Table `3` amplitude `RMSE`: `6/10` harmonics meet or beat the paper target
- Table `4` phase `MAE`: `5/9` harmonics meet or beat the paper target
- Table `5` phase `RMSE`: `5/9` harmonics meet or beat the paper target
- harmonic-level Table `6` closure: `2/10` fully matched, `5/10` partially matched, `3/10` not yet matched

The highest-priority still-open harmonics remain:

- `3`
- `81`
- `156`
- `162`
- `240`

## Final Interpretation

This batch is now operationally complete and scientifically much better
anchored than the interrupted partial-closeout state.

The key final conclusion is:

- the remaining-family batch is fully closed out;
- `RF phase` remains the strongest bookkeeping winner;
- `LGBM` improves the amplitude-side paper envelope;
- `Track 1` still remains canonically open because the exact-paper tables are
  not yet fully matched at harmonics `3`, `81`, `156`, `162`, and `240`.
