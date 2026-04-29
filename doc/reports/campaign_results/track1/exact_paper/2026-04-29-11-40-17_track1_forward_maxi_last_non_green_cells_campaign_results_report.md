# Track 1 Forward Maxi Last Non-Green Cells Campaign Results

## Overview

- campaign name: `track1_forward_maxi_last_non_green_cells_campaign_2026-04-29_01_44_22`
- planning report: `doc/reports/campaign_plans/track1/exact_paper/2026-04-29-01-37-16_track1_forward_maxi_last_non_green_cells_campaign_plan_report.md`
- queue size: `270`
- execution window: `2026-04-29T01:45:38.9774858+02:00` to `2026-04-29T07:49:53+02:00`
- campaign output directory: `output/training_campaigns/track1/exact_paper/forward_maxi_last_non_green_cells/track1_forward_maxi_last_non_green_cells_campaign_2026-04-29_01_44_22`
- validation root: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells`
- report timestamp: `2026-04-29-11-40-17`

## Executive Summary

- The forward-only maxi residual wave completed the full `270/270` queue successfully.
- Targeted family-target pairs: `7`.
- Promoted pair winners: `6`.
- Retained baseline pair winners: `1`.
- Forward non-green cells moved from `9` to `4`.

## Family Best Retry Outcome

| Family | Best Run | Scope | Harmonic | Closure Score | Met | Near | Open |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `ERT` | `track1_forward_ert_ampl_h162_maxi_last_non_green_cells_attempt_21` | `amplitude` | 162 | 1.000 | 2 | 0 | 0 |
| `GBM` | `track1_forward_gbm_ampl_h162_maxi_last_non_green_cells_attempt_16` | `amplitude` | 162 | 0.750 | 1 | 1 | 0 |
| `XGBM` | `track1_forward_xgbm_ampl_h240_maxi_last_non_green_cells_attempt_16` | `amplitude` | 240 | 1.000 | 2 | 0 | 0 |
| `LGBM` | `track1_forward_lgbm_ampl_h162_maxi_last_non_green_cells_attempt_18` | `amplitude` | 162 | 1.000 | 2 | 0 | 0 |

## Campaign Best Run

- run: `track1_forward_ert_ampl_h162_maxi_last_non_green_cells_attempt_21`
- family: `ERT`
- scope: `amplitude`
- harmonic: `162`
- closure score: `1.000`
- met / near / open: `2` / `0` / `0`

## Forward Benchmark Delta

| Surface | Before | After | Delta |
| --- | --- | --- | --- |
| Table `2` forward amplitude MAE | `93G / 5Y / 2R` | `97G / 3Y / 0R` | `-2Y / -2R` |
| Table `3` forward amplitude RMSE | `98G / 1Y / 1R` | `99G / 1Y / 0R` | `0Y / -1R` |
| Table `4` forward phase MAE | `90G / 0Y / 0R` | `90G / 0Y / 0R` | `0Y / 0R` |
| Table `5` forward phase RMSE | `90G / 0Y / 0R` | `90G / 0Y / 0R` | `0Y / 0R` |

## Canonical Forward Status After Closeout

- Table `2`: `3` yellow, `0` red
- Table `3`: `1` yellow, `0` red
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
| `forward` | `ERT` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/ert_reference_models` |
| `forward` | `GBM` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/gbm_reference_models` |
| `forward` | `HGBM` | 19 | 11 | 11 | `models/paper_reference/rcim_track1/forward/hgbm_reference_models` |
| `forward` | `XGBM` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/xgbm_reference_models` |
| `forward` | `LGBM` | 19 | 17 | 17 | `models/paper_reference/rcim_track1/forward/lgbm_reference_models` |

## Linked Artifacts

- benchmark report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- training results master summary: `doc/reports/analysis/Training Results Master Summary.md`
- track1 reference root: `models/paper_reference/rcim_track1/forward/`
- campaign leaderboard: `output/training_campaigns/track1/exact_paper/forward_maxi_last_non_green_cells/track1_forward_maxi_last_non_green_cells_campaign_2026-04-29_01_44_22/campaign_leaderboard.yaml`
- campaign best run YAML: `output/training_campaigns/track1/exact_paper/forward_maxi_last_non_green_cells/track1_forward_maxi_last_non_green_cells_campaign_2026-04-29_01_44_22/campaign_best_run.yaml`
- campaign best run Markdown: `output/training_campaigns/track1/exact_paper/forward_maxi_last_non_green_cells/track1_forward_maxi_last_non_green_cells_campaign_2026-04-29_01_44_22/campaign_best_run.md`
