# Track 1 Open-Cell Full-Matrix Closure Campaign Results Report

## Overview

This report closes the exact-paper `Track 1` open-cell full-matrix closure
wave prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-20-23-50-13_track1_open_cell_full_matrix_closure_campaigns_plan_report.md`

The batch targeted only the still-open family-target pairs in the canonical
`Track 1` progress surface:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

- campaign name: `track1_open_cell_full_matrix_closure_campaigns_2026_04_20_23_50_13`
- report timestamp: `2026-04-21-14-58-00`
- completed family campaigns: `9`
- completed validation runs now available in canonical local review paths: `756`
- failed validation runs: `0`
- locally reconstructed relaunch validation artifacts: `459`
- later recovered first-launch `MLP` validation artifacts: `297`
- promoted targeted pairs: `17/28`
- retained canonical baseline pairs: `11/28`
- aggregate campaign artifact root: `output/training_campaigns/track1/exact_paper/forward/open_cell_full_matrix_closure/shared/track1_open_cell_full_matrix_closure_campaigns_2026_04_20_23_50_13`

## Operational Outcome

- the eight relaunched family retry campaign folders now expose:
  - `campaign_leaderboard.yaml`
  - `campaign_best_run.yaml`
  - `campaign_best_run.md`
- the aggregate campaign root now exposes the final `459`-entry locally
  reconstructed leaderboard and deterministic bookkeeping representative for
  the relaunched non-`MLP` family batch
- `doc/running/active_training_campaign.yaml` now records the canonical
  results report path for the completed open-cell closure wave
- the first `MLP` launch artifact gap is now closed locally:
  - all `297` first-launch validation folders are present in the canonical
    validation-check output root;
  - all `297` first-launch validation reports are present in the canonical
    validation-report root
- the recovered `MLP` first-launch retry evidence does not beat the already
  accepted baseline representative or change the canonical `Table 2-5`
  envelope; `MLP` therefore remains pinned to the accepted baseline
  representative in the family summary
- the canonical benchmark now reads from the better value between:
  - the already accepted benchmark baseline;
  - the new open-cell retry wave.

## Family Representative Outcome

The table below uses one stable representative entry per family across the
accepted baseline plus the new retry wave. For `MLP`, the representative
remains the accepted baseline entry because the fully recovered first-launch
retry evidence still does not beat that baseline representative.

| Family | Best Run | Scope | Closure Score | Met | Near | Open |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `MLP` | `baseline_mlp_phase_3` | `phases_only` | 0.750 | 1 | 1 | 0 |
| `RF` | `track1_rf_amplitude_240_closure_attempt_07` | `amplitudes_only` | 1.000 | 2 | 0 | 0 |
| `DT` | `track1_dt_phase_162_closure_attempt_03` | `phases_only` | 1.000 | 2 | 0 | 0 |
| `ET` | `track1_et_phase_240_closure_attempt_03` | `phases_only` | 1.000 | 2 | 0 | 0 |
| `ERT` | `track1_ert_phase_162_closure_attempt_12` | `phases_only` | 1.000 | 2 | 0 | 0 |
| `GBM` | `track1_gbm_phase_162_closure_attempt_12` | `phases_only` | 1.000 | 2 | 0 | 0 |
| `HGBM` | `track1_hgbm_phase_162_closure_attempt_07` | `phases_only` | 1.000 | 2 | 0 | 0 |
| `XGBM` | `track1_xgbm_amplitude_81_closure_attempt_08` | `amplitudes_only` | 1.000 | 2 | 0 | 0 |
| `LGBM` | `track1_lgbm_phase_162_closure_attempt_07` | `phases_only` | 1.000 | 2 | 0 | 0 |

## Aggregate Winner

- Run: `track1_dt_phase_162_closure_attempt_03`
- Family: `DT`
- Scope: `phases_only`
- Closure Score: `1.000`
- Met / Near / Open: `2` / `0` / `0`

## Canonical Benchmark Outcome

| Surface | Harmonics Met | Total Harmonics | Open Harmonics |
| --- | ---: | ---: | --- |
| Table `2` Amplitude MAE | 7 | 10 | `39, 156, 162` |
| Table `3` Amplitude RMSE | 10 | 10 | `none` |
| Table `4` Phase MAE | 9 | 9 | `none` |
| Table `5` Phase RMSE | 9 | 9 | `none` |

## Track 1 Closure Reading

- `Track 1` is evaluated only from the canonical `Table 2-5` full-matrix
  surfaces plus the accepted `10 x 19` family-bank rule.
- Harmonic-wise Table `6` evidence is postponed into `Track 1.5` and is no
  longer part of the primary closure gate.
- current remaining non-green cells across the canonical surface: `3`
- `Track 1` remains open because at least one canonical full-matrix cell is still non-green.

## Resulting Canonical State

- supporting benchmark report path: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- supporting master summary path: `doc/reports/analysis/Training Results Master Summary.md`
- final closeout report path: `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-21-14-58-00_track1_open_cell_full_matrix_closure_campaign_results_report.md`

## Final Interpretation

- This batch is operationally complete and closes the intended overnight
  retry wave without regressing already accepted cells.
- The earlier `MLP` first-launch sync incident is now closed as a bookkeeping
  and artifact-recovery issue rather than as an unresolved training gap.
- The recovered `MLP` artifact set improves family-level auditability but does
  not change the canonical Tables `2-5` outcome or the accepted family
  representative outcome.
- The closure rule now stays fully aligned with the repository-wide decision
  to keep `Track 1` focused only on the four full-matrix replication tables.
- Any remaining work should therefore target only the still-open cells in
  Tables `2-5`, not the postponed harmonic-wise branch.
