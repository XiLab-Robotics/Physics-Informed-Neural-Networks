# RCIM Model-Bank Reproduction Forward DT Paper-Faithful Search Campaign Results

## Overview

- campaign name: `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__forward_dt_search`
- parent planning report: `doc/reports/campaign_plans/track_1/exact_paper/2026-05-04-12-13-07_track1_paper_faithful_search_protocol_and_campaign_replacement_plan_report.md`
- campaign output directory: `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__forward_dt_search`
- queue size: `1`
- direction scope: `forward`
- family scope: `DT`
- workflow stage: `search`
- launch mode: `remote_operator_launcher`
- remote host alias: `xilab-remote`

## Completion Summary

- the subset exact-paper campaign completed the full `1/1` queue successfully;
- remote artifact sync-back completed successfully and materialized the local log, validation bundle, and validation report;
- the run executed the paper-faithful search path with repository-aligned historical `cross_validate(...)` replay at both wrapper and target levels;
- the subset closeout materialized campaign-level `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and `campaign_best_run.md` bookkeeping artifacts;
- the parent `20`-run paper-faithful RCIM Model-Bank Reproduction campaign remains canonically `cancelled` and is not reopened by this subset closeout.

## Campaign Best Run

- run instance id: `2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation`
- run name: `track1_paper_faithful_grid_search_forward_dt`
- direction label: `forward`
- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAE: `0.095493`
- winning mean component RMSE: `0.186076`
- winning mean component MAPE: `40.5591%`
- best parameter source: `grid_search`
- best parameters: `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': 23, 'estimator__min_samples_split': 5}`

Selection rule:

- Primary metric: `winning_mean_component_mae_asc`
- First tie-breaker: `winning_mean_component_rmse_asc`
- Second tie-breaker: `winning_mean_component_mape_percent_asc`
- Third tie-breaker: `run_name`

## Search Protocol Summary

| Item | Value |
| --- | --- |
| Grid search candidates | `300` |
| Grid search CV folds | `5` |
| Estimated grid-search CV fits | `1500` |
| Historical wrapper `cross_validate(...)` folds | `10` |
| Historical target-level `cross_validate(...)` folds | `10` per target |
| Target count | `19` |
| Random seed | `0` |

## Validation Outcome

| Metric | Value |
| --- | ---: |
| Mean component MAPE % | 40.559 |
| Mean component MAE | 0.095493 |
| Mean component RMSE | 0.186076 |
| Train rows | 678 |
| Validation rows | 194 |
| Test rows | 97 |
| ONNX exports | 19 |
| ONNX export failures | 0 |

## Historical Replay Outcome

| Scope | Mean MAE | Mean RMSE | Mean MAPE % |
| --- | ---: | ---: | ---: |
| Wrapper `cross_validate(...)` replay | 0.082761 | 0.196496 | 47.602 |
| Held-out test evaluation | 0.095493 | 0.186076 | 40.559 |

## Linked Artifacts

- campaign log: `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__forward_dt_search/logs/001_track1_paper_faithful_grid_search_forward_dt.log`
- remote wrapper log: `.temp/remote_training_campaigns/2026-05-08-17-07-22_track1_bidirectional_paper_faithful_grid_search_campaign_2026_05_04_12_26_30__forward_dt_search/remote_training_campaign.log`
- validation report: `doc/reports/analysis/validation_checks/rcim_model_bank_reproduction/rcim_paper_reimplementation/track1/original_dataset/[2026-04-25_to_2026-05-16]/2026-05-08-17-10-02_paper_rei_57e160d8_track1_paper_faithful_grid_s_bd96d56f_original_dataset_exact_model_bank_report.md`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation/validation_summary.yaml`
- best-parameter summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation/best_parameter_summary.yaml`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation/paper_family_model_bank.pkl`
- campaign leaderboard: `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__forward_dt_search/campaign_leaderboard.yaml`
- campaign best run YAML: `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__forward_dt_search/campaign_best_run.yaml`
- campaign best run Markdown: `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__forward_dt_search/campaign_best_run.md`
- parent active campaign state: `doc/running/active_training_campaign.yaml`

## Closeout Notes

- this is a subset closeout for the successful `forward + DT + search` bundle launched through the family-stage exact-paper wrapper;
- it is not a canonical full closeout of the parent paper-faithful `20`-run RCIM Model-Bank Reproduction campaign;
- no RCIM Model-Bank Reproduction benchmark refresh, master-summary refresh, or paper-reference archive refresh is performed here because the parent campaign remains interrupted and incomplete;
- the subset closeout is intended to preserve auditable evidence for the new launcher, logging, and paper-faithful search protocol on one completed family-direction run.
