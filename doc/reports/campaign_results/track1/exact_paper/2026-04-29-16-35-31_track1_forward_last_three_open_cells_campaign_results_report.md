# Track 1 Forward Last Three Open Cells Campaign Results

## Overview

- campaign name: `track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21`
- planning report: `doc/reports/campaign_plans/track1/exact_paper/2026-04-29-14-28-06_track1_forward_last_three_open_cells_campaign_plan_report.md`
- queue size: `84`
- execution window: `2026-04-29T14:58:21.9115993+02:00` to `2026-04-29T16:15:38+02:00`
- campaign output directory: `output/training_campaigns/track1/exact_paper/forward_last_three_open_cells/track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21`
- validation root: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells`
- report timestamp: `2026-04-29-16-35-31`

## Executive Summary

- The final forward-only last-three-open-cells wave completed the full `84/84` queue successfully.
- Targeted family-target pairs: `3`.
- Promoted pair winners: `0`.
- Retained baseline pair winners: `3`.
- Forward non-green cells moved from `3` to `3`.

## Family Best Retry Outcome

| Family | Best Run | Scope | Harmonic | Closure Score | Met | Near | Open |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `ERT` | `track1_forward_ert_ampl_h240_last_three_open_cells_attempt_15` | `amplitude` | 240 | 0.750 | 1 | 1 | 0 |
| `GBM` | `track1_forward_gbm_ampl_h162_last_three_open_cells_attempt_21` | `amplitude` | 162 | 0.250 | 0 | 1 | 1 |

## Campaign Best Run

- run: `track1_forward_ert_ampl_h240_last_three_open_cells_attempt_15`
- family: `ERT`
- scope: `amplitude`
- harmonic: `240`
- closure score: `0.750`
- met / near / open: `1` / `1` / `0`

## Forward Benchmark Delta

| Surface | Before | After | Delta |
| --- | --- | --- | --- |
| Table `2` forward amplitude MAE | `97G / 3Y / 0R` | `97G / 3Y / 0R` | `0Y / 0R` |
| Table `3` forward amplitude RMSE | `100G / 0Y / 0R` | `100G / 0Y / 0R` | `0Y / 0R` |
| Table `4` forward phase MAE | `90G / 0Y / 0R` | `90G / 0Y / 0R` | `0Y / 0R` |
| Table `5` forward phase RMSE | `90G / 0Y / 0R` | `90G / 0Y / 0R` | `0Y / 0R` |

## Canonical Forward Status After Closeout

- Table `2`: `3` yellow, `0` red
- Table `3`: `0` yellow, `0` red
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
- campaign leaderboard: `output/training_campaigns/track1/exact_paper/forward_last_three_open_cells/track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21/campaign_leaderboard.yaml`
- campaign best run YAML: `output/training_campaigns/track1/exact_paper/forward_last_three_open_cells/track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21/campaign_best_run.yaml`
- campaign best run Markdown: `output/training_campaigns/track1/exact_paper/forward_last_three_open_cells/track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21/campaign_best_run.md`
