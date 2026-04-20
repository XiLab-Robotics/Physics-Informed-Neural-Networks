# Track 1 Remaining Family Partial Closeout Campaign Results Report

## Overview

This report closes the completed subset of the interrupted remaining-family
exact-paper batch prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-18-00-48-05_track1_remaining_exact_paper_family_campaigns_plan_report.md`

The remote terminal crashed during the `XGBM` portion of the sequence. The
repository now has a clean partial-closeout state for the seven completed
families and leaves `XGBM` plus `LGBM` explicitly pending for the follow-up
crash diagnosis and rerun.

- completed family campaigns: `7`
- completed validation runs: `14`
- pending family campaigns: `2`
- completed families: `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`
- pending families: `XGBM`, `LGBM`
- aggregate campaign artifact root:
  `output/training_campaigns/track1/exact_paper/track1_remaining_family_full_matrix_campaigns_2026_04_18_00_48_05/`

## Operational Outcome

- all `14` finished runs produced validation summaries and Markdown validation reports
- the seven completed family campaign folders now expose `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and `campaign_best_run.md`
- the aggregate interrupted batch now also exposes the same three winner-bookkeeping artifacts under its canonical campaign root
- `XGBM` and `LGBM` are intentionally left open until the crash log is reviewed and the missing reruns are executed

## Completed Family Closeout

| Family | Amplitude Run | Phase Run | Best Run | Best Scope | Best Closure Score | Open Cells |
| --- | --- | --- | --- | --- | ---: | ---: |
| `DT` | `track1_dt_amplitude_full_matrix` | `track1_dt_phase_full_matrix` | `track1_dt_phase_full_matrix` | `phases_only` | 0.333 | `8` |
| `ERT` | `track1_ert_amplitude_full_matrix` | `track1_ert_phase_full_matrix` | `track1_ert_phase_full_matrix` | `phases_only` | 0.472 | `8` |
| `ET` | `track1_et_amplitude_full_matrix` | `track1_et_phase_full_matrix` | `track1_et_phase_full_matrix` | `phases_only` | 0.139 | `15` |
| `GBM` | `track1_gbm_amplitude_full_matrix` | `track1_gbm_phase_full_matrix` | `track1_gbm_phase_full_matrix` | `phases_only` | 0.556 | `5` |
| `HGBM` | `track1_hgbm_amplitude_full_matrix` | `track1_hgbm_phase_full_matrix` | `track1_hgbm_phase_full_matrix` | `phases_only` | 0.556 | `4` |
| `MLP` | `track1_mlp_amplitude_full_matrix` | `track1_mlp_phase_full_matrix` | `track1_mlp_amplitude_full_matrix` | `amplitudes_only` | 0.000 | `10` |
| `RF` | `track1_rf_amplitude_full_matrix` | `track1_rf_phase_full_matrix` | `track1_rf_phase_full_matrix` | `phases_only` | 0.611 | `3` |

## Aggregate Ranking

| Rank | Run | Family | Scope | Paper Cell | Met | Near | Open | Closure Score |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `1` | `track1_rf_phase_full_matrix` | `RF` | `phases_only` | `18` | `7` | `8` | `3` | 0.611 |
| `2` | `track1_gbm_phase_full_matrix` | `GBM` | `phases_only` | `18` | `7` | `6` | `5` | 0.556 |
| `3` | `track1_hgbm_phase_full_matrix` | `HGBM` | `phases_only` | `18` | `6` | `8` | `4` | 0.556 |
| `4` | `track1_ert_phase_full_matrix` | `ERT` | `phases_only` | `18` | `7` | `3` | `8` | 0.472 |
| `5` | `track1_hgbm_amplitude_full_matrix` | `HGBM` | `amplitudes_only` | `10` | `3` | `3` | `4` | 0.450 |
| `6` | `track1_ert_amplitude_full_matrix` | `ERT` | `amplitudes_only` | `10` | `2` | `3` | `5` | 0.350 |
| `7` | `track1_rf_amplitude_full_matrix` | `RF` | `amplitudes_only` | `10` | `1` | `5` | `4` | 0.350 |
| `8` | `track1_dt_phase_full_matrix` | `DT` | `phases_only` | `18` | `2` | `8` | `8` | 0.333 |
| `9` | `track1_gbm_amplitude_full_matrix` | `GBM` | `amplitudes_only` | `10` | `1` | `4` | `5` | 0.300 |
| `10` | `track1_et_phase_full_matrix` | `ET` | `phases_only` | `18` | `2` | `1` | `15` | 0.139 |
| `11` | `track1_dt_amplitude_full_matrix` | `DT` | `amplitudes_only` | `10` | `0` | `2` | `8` | 0.100 |
| `12` | `track1_et_amplitude_full_matrix` | `ET` | `amplitudes_only` | `10` | `0` | `2` | `8` | 0.100 |
| `13` | `track1_mlp_amplitude_full_matrix` | `MLP` | `amplitudes_only` | `10` | `0` | `0` | `10` | 0.000 |
| `14` | `track1_mlp_phase_full_matrix` | `MLP` | `phases_only` | `18` | `0` | `0` | `18` | 0.000 |

## Partial Batch Winner

The aggregate bookkeeping winner is `track1_rf_phase_full_matrix` from family `RF`.

It wins the interrupted batch because it has the strongest closure score among
the `14` completed runs while also keeping the fewest materially open cells
under the explicit row-closure ranking policy.

- winning scope: `phases_only`
- closure score: `0.611`
- met paper cells: `7`
- near paper cells: `8`
- open paper cells: `3`

## Scientific Outcome

- the seven rerun families materially refresh the row-reproduction evidence for `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, and `HGBM`
- several rows move numerically relative to the older `2026-04-14` full-matrix pass, so the canonical benchmark tables must now read from the refreshed family rows
- the partial refresh improves the envelope on a few exact-paper cells, but `Track 1` still remains open pending the unresolved harmonics and the missing `XGBM` / `LGBM` reruns
- `SVM` remains separately accepted as closed at the repository level with archived canonical reference models

## Benchmark Refresh Effect

The canonical benchmark refresh after this partial closeout is:

- Table `2` amplitude `MAE`: `2/10` harmonics meet or beat the paper target
- Table `3` amplitude `RMSE`: `5/10` harmonics meet or beat the paper target
- Table `4` phase `MAE`: `5/9` harmonics meet or beat the paper target
- Table `5` phase `RMSE`: `5/9` harmonics meet or beat the paper target
- harmonic-level Table `6` closure: `2/10` fully matched, `5/10` partially matched, `3/10` not yet matched

The highest-priority still-open harmonics after the refresh are now concentrated around:

- `3`
- `81`
- `156`
- `162`
- `240`

## Pending Follow-Up

This partial closeout intentionally stops before any crash diagnosis. The next
step is to inspect the terminal log, repair the interrupted remote sequence, and
rerun the missing `XGBM` and `LGBM` family campaigns.
