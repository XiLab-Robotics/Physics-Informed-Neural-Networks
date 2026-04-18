# Track 1 Remaining Family Cellwise Final Closeout Campaign Results Report

## Overview

This report closes the full remaining-family exact-paper `Track 1` cellwise batch
prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-18-22-28-04_track1_remaining_family_cellwise_reference_campaigns_plan_report.md`

The batch replicated the accepted `SVM` workflow family-by-family by training a
separate exact-paper model for every paper-facing cell of the remaining `Track 1`
families.

- completed family campaigns: `9`
- completed validation runs: `171`
- failed validation runs: `0`
- aggregate campaign artifact root:
  `output/training_campaigns/track1_remaining_family_cellwise_reference_campaigns_2026_04_18_22_28_04/`

## Operational Outcome

- every non-`SVM` exact-paper family now has its full `19`-run cellwise bank
- all `9` family campaign folders now expose:
  - `campaign_leaderboard.yaml`
  - `campaign_best_run.yaml`
  - `campaign_best_run.md`
- the aggregate remaining-family campaign root now exposes the final `171`-entry
  leaderboard and deterministic bookkeeping representative
- `doc/running/active_training_campaign.yaml` now records the canonical results
  report path for the completed batch

## Family Recovery Outcome

| Family | Amplitude Run | Phase Run | Best Run | Best Scope | Best Closure Score | Open Cells |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `MLP` | `track1_mlp_amplitude_162_cellwise_reference` | `track1_mlp_phase_156_cellwise_reference` | `track1_mlp_amplitude_162_cellwise_reference` | `amplitudes_only` | 1.000 | `11` |
| `RF` | `track1_rf_amplitude_162_cellwise_reference` | `track1_rf_phase_156_cellwise_reference` | `track1_rf_amplitude_162_cellwise_reference` | `amplitudes_only` | 1.000 | `1` |
| `DT` | `track1_dt_amplitude_240_cellwise_reference` | `track1_dt_phase_156_cellwise_reference` | `track1_dt_amplitude_240_cellwise_reference` | `amplitudes_only` | 1.000 | `4` |
| `ET` | `track1_et_amplitude_0_cellwise_reference` | `track1_et_phase_156_cellwise_reference` | `track1_et_amplitude_0_cellwise_reference` | `amplitudes_only` | 1.000 | `5` |
| `ERT` | `track1_ert_amplitude_1_cellwise_reference` | `track1_ert_phase_156_cellwise_reference` | `track1_ert_amplitude_1_cellwise_reference` | `amplitudes_only` | 1.000 | `6` |
| `GBM` | `track1_gbm_amplitude_162_cellwise_reference` | `track1_gbm_phase_156_cellwise_reference` | `track1_gbm_amplitude_162_cellwise_reference` | `amplitudes_only` | 1.000 | `1` |
| `HGBM` | `track1_hgbm_amplitude_162_cellwise_reference` | `track1_hgbm_phase_156_cellwise_reference` | `track1_hgbm_amplitude_162_cellwise_reference` | `amplitudes_only` | 1.000 | `1` |
| `XGBM` | `track1_xgbm_amplitude_162_cellwise_reference` | `track1_xgbm_phase_156_cellwise_reference` | `track1_xgbm_amplitude_162_cellwise_reference` | `amplitudes_only` | 1.000 | `3` |
| `LGBM` | `track1_lgbm_amplitude_162_cellwise_reference` | `track1_lgbm_phase_156_cellwise_reference` | `track1_lgbm_amplitude_162_cellwise_reference` | `amplitudes_only` | 1.000 | `1` |

## Aggregate Ranking

| Rank | Run | Family | Scope | Paper Cell | Met | Near | Open | Closure Score |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `1` | `track1_dt_amplitude_240_cellwise_reference` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `2` | `track1_dt_amplitude_39_cellwise_reference` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `3` | `track1_dt_amplitude_40_cellwise_reference` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `4` | `track1_dt_amplitude_78_cellwise_reference` | `DT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `5` | `track1_dt_phase_156_cellwise_reference` | `DT` | `phases_only` | `2` | `2` | `0` | `0` | 1.000 |
| `6` | `track1_dt_phase_39_cellwise_reference` | `DT` | `phases_only` | `2` | `2` | `0` | `0` | 1.000 |
| `7` | `track1_dt_phase_3_cellwise_reference` | `DT` | `phases_only` | `2` | `2` | `0` | `0` | 1.000 |
| `8` | `track1_dt_phase_78_cellwise_reference` | `DT` | `phases_only` | `2` | `2` | `0` | `0` | 1.000 |
| `9` | `track1_ert_amplitude_1_cellwise_reference` | `ERT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `10` | `track1_ert_amplitude_39_cellwise_reference` | `ERT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `11` | `track1_ert_amplitude_3_cellwise_reference` | `ERT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `12` | `track1_ert_amplitude_40_cellwise_reference` | `ERT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `13` | `track1_ert_amplitude_78_cellwise_reference` | `ERT` | `amplitudes_only` | `2` | `2` | `0` | `0` | 1.000 |
| `14` | `track1_ert_phase_156_cellwise_reference` | `ERT` | `phases_only` | `2` | `2` | `0` | `0` | 1.000 |
| `15` | `track1_ert_phase_40_cellwise_reference` | `ERT` | `phases_only` | `2` | `2` | `0` | `0` | 1.000 |

## Final Batch Winner

The aggregate batch bookkeeping representative is `track1_dt_amplitude_240_cellwise_reference` from family
`DT`.

This is a deterministic winner under the per-run closure-first policy across the
full `171`-entry batch. It should be read as a bookkeeping representative of the
completed campaign, not as the whole scientific verdict of the promoted cellwise
family rows.

- winning scope: `amplitudes_only`
- closure score: `1.000`
- met paper cells: `2`
- near paper cells: `0`
- open paper cells: `0`

## Scientific Outcome

- the `171`-run batch successfully materializes the intended `19`-model cellwise banks for `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, and `LGBM`
- the refreshed family rows improve the canonical amplitude `RMSE` envelope from `6/10` to `7/10`
- the refreshed family rows leave amplitude `MAE` at `3/10` and phase `MAE` at `5/9`
- the refreshed family rows reduce phase `RMSE` closure to `4/9` because the promoted cellwise references prioritize per-family row fidelity rather than preserving the older full-matrix winner envelope
- under the canonical Table `6` family-alignment rule, no harmonic is yet fully closed after this refresh

## Final Benchmark Refresh Effect

The canonical benchmark after the cellwise remaining-family closeout is:

- Table `2` amplitude `MAE`: `3/10` harmonics meet or beat the paper target
- Table `3` amplitude `RMSE`: `7/10` harmonics meet or beat the paper target
- Table `4` phase `MAE`: `5/9` harmonics meet or beat the paper target
- Table `5` phase `RMSE`: `4/9` harmonics meet or beat the paper target
- harmonic-level Table `6` closure: `0/10` fully matched, `8/10` partially matched, `2/10` not yet matched

The highest-priority still-open harmonics are now:

- `3`
- `240`
- `0`
- `1`
- `156`
- `162`

## Final Interpretation

This batch is operationally complete and materially stronger as a reference-bank
package than the earlier full-matrix remaining-family pass.

The key final conclusion is:

- the remaining-family cellwise batch is fully closed out;
- the repository now has the intended `171` exact-paper reference runs for the
  nine non-`SVM` families;
- the canonical family rows and the benchmark tables now read from those promoted
  cellwise references;
- `Track 1` still remains canonically open because the best numeric families do
  not yet align cleanly with the paper family selections in Table `6`.
