# Training Campaign Execution Report

## Overview

- Campaign Name: `polished_dataset_stage1_smoke_2026_06_21`
- Generated At: `2026-06-22T12:04:16`
- Queue Root: `config/training/queue/polished_dataset_stage1_smoke`
- Campaign Output Directory: `output/training_campaigns/2026-06-22-11-55-01_polished_dataset_stage1_smoke_2026_06_21`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md`
- Completed Runs: `0`
- Failed Runs: `1`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/polished_dataset_stage1_smoke/failed/2026-06-22-11-55-01_001_trial.yaml` | `te_feedforward_trial` | `feedforward` | `failed` | `00:09:15` |

## Run Details

### te_feedforward_trial

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/failed/2026-06-22-11-55-01_001_trial.yaml`
- Source Config: `config/training/feedforward/presets/trial.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-22-11-55-01__te_feedforward_trial`
- Queue Status: `failed`
- Start Time: `2026-06-22T11:55:01`
- End Time: `2026-06-22T12:04:16`
- Duration: `00:09:15`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-22-11-55-01__te_feedforward_trial`
- Config Snapshot: `output/training_runs/feedforward/2026-06-22-11-55-01__te_feedforward_trial/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-06-22-11-55-01_polished_dataset_stage1_smoke_2026_06_21/logs/001_te_feedforward_trial.log`
- Error Message: `invalid literal for int() with base 10: 'auto'`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
