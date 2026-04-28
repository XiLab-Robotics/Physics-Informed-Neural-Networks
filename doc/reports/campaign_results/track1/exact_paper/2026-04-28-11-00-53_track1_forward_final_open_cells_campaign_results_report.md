# Track 1 Forward Final Open-Cells Campaign Results

## Overview

- campaign name: `track1_forward_final_open_cells_campaign_2026-04-28_00_30_09`
- planning report: `doc/reports/campaign_plans/track1/exact_paper/2026-04-28-00-16-01_track1_forward_final_open_cells_campaign_plan_report.md`
- queue size: `76`
- execution window: `2026-04-28T00:32:27.4229313+02:00` to `2026-04-28T02:20:01+02:00`
- campaign output directory: `output/training_campaigns/track1/exact_paper/forward_final_open_cells/track1_forward_final_open_cells_campaign_2026-04-28_00_30_09`
- validation root: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells`
- report timestamp: `2026-04-28-11-00-53`

## Executive Summary

- The final forward-only residual wave completed the full `76/76` queue successfully.
- Targeted family-target pairs: `8`.
- Promoted pair winners: `2`.
- Retained baseline pair winners: `6`.
- Forward non-green cells moved from `11` to `10`.

## Family Best Retry Outcome

| Family | Best Run | Scope | Harmonic | Closure Score | Met | Near | Open |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `ERT` | `track1_forward_ert_ampl_h162_final_open_cells_attempt_08` | `amplitude` | 162 | 0.500 | 1 | 0 | 1 |
| `GBM` | `track1_forward_gbm_ampl_h162_final_open_cells_attempt_08` | `amplitude` | 162 | 0.000 | 0 | 0 | 2 |
| `XGBM` | `track1_forward_xgbm_ampl_h240_final_open_cells_attempt_08` | `amplitude` | 240 | 0.750 | 1 | 1 | 0 |
| `LGBM` | `track1_forward_lgbm_phase_h81_final_open_cells_attempt_05` | `phase` | 81 | 1.000 | 2 | 0 | 0 |

## Campaign Best Run

- run: `track1_forward_lgbm_phase_h81_final_open_cells_attempt_05`
- family: `LGBM`
- scope: `phase`
- harmonic: `81`
- closure score: `1.000`
- met / near / open: `2` / `0` / `0`

## Forward Benchmark Delta

| Surface | Before | After | Delta |
| --- | --- | --- | --- |
| Table `2` forward amplitude MAE | `94G / 3Y / 3R` | `93G / 4Y / 3R` | `1Y / 0R` |
| Table `3` forward amplitude RMSE | `96G / 3Y / 1R` | `97G / 2Y / 1R` | `-1Y / 0R` |
| Table `4` forward phase MAE | `89G / 1Y / 0R` | `90G / 0Y / 0R` | `-1Y / 0R` |
| Table `5` forward phase RMSE | `90G / 0Y / 0R` | `90G / 0Y / 0R` | `0Y / 0R` |

## Canonical Forward Status After Closeout

- Table `2`: `4` yellow, `3` red
- Table `3`: `2` yellow, `1` red
- Table `4`: `0` yellow, `0` red
- Table `5`: `0` yellow, `0` red

## Reference Archive Refresh

| Direction | Family | Archived Targets | Unique Source Runs | Unique Source Configs | Archive Root |
| --- | --- | ---: | ---: | ---: | --- |
| `forward` | `SVM` | 19 | 11 | 11 | `models/paper_reference/rcim_track1/forward/svm_reference_models` |
| `forward` | `MLP` | 19 | 13 | 13 | `models/paper_reference/rcim_track1/forward/mlp_reference_models` |
| `forward` | `RF` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/rf_reference_models` |
| `forward` | `DT` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/dt_reference_models` |
| `forward` | `ET` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/et_reference_models` |
| `forward` | `ERT` | 19 | 10 | 10 | `models/paper_reference/rcim_track1/forward/ert_reference_models` |
| `forward` | `GBM` | 19 | 11 | 11 | `models/paper_reference/rcim_track1/forward/gbm_reference_models` |
| `forward` | `HGBM` | 19 | 11 | 11 | `models/paper_reference/rcim_track1/forward/hgbm_reference_models` |
| `forward` | `XGBM` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/xgbm_reference_models` |
| `forward` | `LGBM` | 19 | 17 | 17 | `models/paper_reference/rcim_track1/forward/lgbm_reference_models` |

## Linked Artifacts

- benchmark report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- training results master summary: `doc/reports/analysis/Training Results Master Summary.md`
- track1 reference root: `models/paper_reference/rcim_track1/forward/`
- campaign leaderboard: `output/training_campaigns/track1/exact_paper/forward_final_open_cells/track1_forward_final_open_cells_campaign_2026-04-28_00_30_09/campaign_leaderboard.yaml`
- campaign best run YAML: `output/training_campaigns/track1/exact_paper/forward_final_open_cells/track1_forward_final_open_cells_campaign_2026-04-28_00_30_09/campaign_best_run.yaml`
- campaign best run Markdown: `output/training_campaigns/track1/exact_paper/forward_final_open_cells/track1_forward_final_open_cells_campaign_2026-04-28_00_30_09/campaign_best_run.md`
