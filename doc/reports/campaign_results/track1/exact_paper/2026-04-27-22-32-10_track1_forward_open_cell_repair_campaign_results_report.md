# Track 1 Forward Open-Cell Repair Campaign Results

## Overview

- campaign name: `track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10`
- planning report: `doc/reports/campaign_plans/track1/exact_paper/2026-04-27-13-00-21_track1_forward_open_cell_repair_campaign_plan_report.md`
- queue size: `300`
- execution window: `2026-04-27T16:09:50.0377746+02:00` to `2026-04-27T22:01:36+02:00`
- campaign output directory: `output/training_campaigns/track1/exact_paper/forward_open_cell_repair/track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10`
- validation root: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair`
- report timestamp: `2026-04-27-22-32-10`

## Executive Summary

- The forward-only repair wave completed the full `300/300` queue successfully.
- Targeted family-target pairs: `30`.
- Promoted pair winners: `25`.
- Retained baseline pair winners: `5`.
- Forward non-green cells moved from `53` to `11`.

## Family Best Retry Outcome

| Family | Best Run | Scope | Harmonic | Closure Score | Met | Near | Open |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `track1_forward_svm_ampl_h40_open_cell_repair_attempt_07` | `amplitude` | 40 | 1.000 | 2 | 0 | 0 |
| `ERT` | `track1_forward_ert_ampl_h156_open_cell_repair_attempt_02` | `amplitude` | 156 | 0.750 | 1 | 1 | 0 |
| `GBM` | `track1_forward_gbm_ampl_h3_open_cell_repair_attempt_07` | `amplitude` | 3 | 1.000 | 2 | 0 | 0 |
| `HGBM` | `track1_forward_hgbm_ampl_h0_open_cell_repair_attempt_06` | `amplitude` | 0 | 1.000 | 2 | 0 | 0 |
| `XGBM` | `track1_forward_xgbm_ampl_h240_open_cell_repair_attempt_06` | `amplitude` | 240 | 0.500 | 0 | 2 | 0 |
| `LGBM` | `track1_forward_lgbm_ampl_h81_open_cell_repair_attempt_08` | `amplitude` | 81 | 1.000 | 2 | 0 | 0 |

## Campaign Best Run

- run: `track1_forward_lgbm_ampl_h81_open_cell_repair_attempt_08`
- family: `LGBM`
- scope: `amplitude`
- harmonic: `81`
- closure score: `1.000`
- met / near / open: `2` / `0` / `0`

## Forward Benchmark Delta

| Surface | Before | After | Delta |
| --- | --- | --- | --- |
| Table `2` forward amplitude MAE | `82G / 2Y / 16R` | `94G / 3Y / 3R` | `1Y / -13R` |
| Table `3` forward amplitude RMSE | `82G / 6Y / 12R` | `96G / 3Y / 1R` | `-3Y / -11R` |
| Table `4` forward phase MAE | `82G / 0Y / 8R` | `89G / 1Y / 0R` | `1Y / -8R` |
| Table `5` forward phase RMSE | `81G / 6Y / 3R` | `90G / 0Y / 0R` | `-6Y / -3R` |

## Canonical Forward Status After Closeout

- Table `2`: `3` yellow, `3` red
- Table `3`: `3` yellow, `1` red
- Table `4`: `1` yellow, `0` red
- Table `5`: `0` yellow, `0` red

## Linked Artifacts

- benchmark report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- training results master summary: `doc/reports/analysis/Training Results Master Summary.md`
- campaign leaderboard: `output/training_campaigns/track1/exact_paper/forward_open_cell_repair/track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10/campaign_leaderboard.yaml`
- campaign best run YAML: `output/training_campaigns/track1/exact_paper/forward_open_cell_repair/track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10/campaign_best_run.yaml`
- campaign best run Markdown: `output/training_campaigns/track1/exact_paper/forward_open_cell_repair/track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10/campaign_best_run.md`
