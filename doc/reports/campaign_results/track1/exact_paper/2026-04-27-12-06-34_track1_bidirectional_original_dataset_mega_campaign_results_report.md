# Track 1 Bidirectional Original-Dataset Mega Campaign Results

## Overview

- campaign name: `track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17`
- planning report: `doc/reports/campaign_plans/track1/exact_paper/2026-04-26-00-43-19_track1_bidirectional_original_dataset_mega_relaunch_after_micro_gate_plan_report.md`
- campaign output directory: `output/training_campaigns/track1/exact_paper/bidirectional_original_dataset/track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17`
- queue size: `400`
- launch mode: `remote_operator_launcher`
- remote host alias: `xilab-remote`

## Completion Summary

- the bidirectional original-dataset exact-paper mega campaign completed the full `400/400` queue;
- the closeout refreshed both directional repository-owned restart matrices in `RCIM Paper Reference Benchmark.md`;
- the closeout rebuilt the canonical paper-reference archives under `models/paper_reference/rcim_track1/forward/` and `models/paper_reference/rcim_track1/backward/`;
- the closeout materialized campaign-level `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and `campaign_best_run.md` bookkeeping artifacts.

## Campaign Best Run

- run instance id: `2026-04-26-17-34-18__track1_original_dataset_backward_ert_attempt_20_campaign_validation`
- run name: `track1_original_dataset_backward_ert_attempt_20`
- direction label: `backward`
- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- mean component MAE: `0.033975`
- mean component RMSE: `0.087169`
- mean component MAPE: `14.8114%`

Selection rule:

- Primary metric: `winning_mean_component_mae_asc`
- First tie-breaker: `winning_mean_component_rmse_asc`
- Second tie-breaker: `winning_mean_component_mape_percent_asc`
- Third tie-breaker: `run_name`

## Benchmark Restart Surface

| Table | Direction | Green | Yellow | Red | Total |
| --- | --- | ---: | ---: | ---: | ---: |
| `Table 2 - Amplitude MAE` | `forward` | 82 | 2 | 16 | 100 |
| `Table 2 - Amplitude MAE` | `backward` | 76 | 7 | 17 | 100 |
| `Table 3 - Amplitude RMSE` | `forward` | 82 | 6 | 12 | 100 |
| `Table 3 - Amplitude RMSE` | `backward` | 81 | 6 | 13 | 100 |
| `Table 4 - Phase MAE` | `forward` | 82 | 0 | 8 | 90 |
| `Table 4 - Phase MAE` | `backward` | 61 | 5 | 24 | 90 |
| `Table 5 - Phase RMSE` | `forward` | 81 | 6 | 3 | 90 |
| `Table 5 - Phase RMSE` | `backward` | 63 | 5 | 22 | 90 |

## Reference Archive Refresh

| Direction | Family | Archived Targets | Unique Source Runs | Unique Source Configs | Archive Root |
| --- | --- | ---: | ---: | ---: | --- |
| `forward` | `SVM` | 19 | 11 | 11 | `models/paper_reference/rcim_track1/forward/svm_reference_models` |
| `forward` | `MLP` | 19 | 13 | 13 | `models/paper_reference/rcim_track1/forward/mlp_reference_models` |
| `forward` | `RF` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/rf_reference_models` |
| `forward` | `DT` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/dt_reference_models` |
| `forward` | `ET` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/forward/et_reference_models` |
| `forward` | `ERT` | 19 | 10 | 10 | `models/paper_reference/rcim_track1/forward/ert_reference_models` |
| `forward` | `GBM` | 19 | 8 | 8 | `models/paper_reference/rcim_track1/forward/gbm_reference_models` |
| `forward` | `HGBM` | 19 | 11 | 11 | `models/paper_reference/rcim_track1/forward/hgbm_reference_models` |
| `forward` | `XGBM` | 19 | 11 | 11 | `models/paper_reference/rcim_track1/forward/xgbm_reference_models` |
| `forward` | `LGBM` | 19 | 13 | 13 | `models/paper_reference/rcim_track1/forward/lgbm_reference_models` |
| `backward` | `SVM` | 19 | 14 | 14 | `models/paper_reference/rcim_track1/backward/svm_reference_models` |
| `backward` | `MLP` | 19 | 10 | 10 | `models/paper_reference/rcim_track1/backward/mlp_reference_models` |
| `backward` | `RF` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/backward/rf_reference_models` |
| `backward` | `DT` | 19 | 9 | 9 | `models/paper_reference/rcim_track1/backward/dt_reference_models` |
| `backward` | `ET` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/backward/et_reference_models` |
| `backward` | `ERT` | 19 | 9 | 9 | `models/paper_reference/rcim_track1/backward/ert_reference_models` |
| `backward` | `GBM` | 19 | 9 | 9 | `models/paper_reference/rcim_track1/backward/gbm_reference_models` |
| `backward` | `HGBM` | 19 | 10 | 10 | `models/paper_reference/rcim_track1/backward/hgbm_reference_models` |
| `backward` | `XGBM` | 19 | 12 | 12 | `models/paper_reference/rcim_track1/backward/xgbm_reference_models` |
| `backward` | `LGBM` | 19 | 9 | 9 | `models/paper_reference/rcim_track1/backward/lgbm_reference_models` |

## Linked Artifacts

- benchmark report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- training results master summary: `doc/reports/analysis/Training Results Master Summary.md`
- track1 reference root: `models/paper_reference/rcim_track1`
- campaign leaderboard: `output/training_campaigns/track1/exact_paper/bidirectional_original_dataset/track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17/campaign_leaderboard.yaml`
- campaign best run YAML: `output/training_campaigns/track1/exact_paper/bidirectional_original_dataset/track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17/campaign_best_run.yaml`
- campaign best run Markdown: `output/training_campaigns/track1/exact_paper/bidirectional_original_dataset/track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17/campaign_best_run.md`
- active campaign state: `doc/running/active_training_campaign.yaml`

## Closeout Notes

- the archive refresh rule remains mandatory for every future Track 1 closeout;
- when a newly accepted target winner improves the stored archive entry under `models/paper_reference/rcim_track1/`, the archive must be updated together with its reference documents;
- when the accepted target winner does not improve, the stored archive entry must remain unchanged.

This report is the canonical closeout record for `track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17` and is linked from `doc/reports/campaign_results/track1/exact_paper/2026-04-27-12-06-34_track1_bidirectional_original_dataset_mega_campaign_results_report.md`.
