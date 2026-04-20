# Training Campaign Execution Report

## Overview

- Campaign Name: `best_training_logging_validation_campaign_2026_03_14_00_56_06`
- Generated At: `2026-03-14T01:24:57`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/mixed_training/2026-03-14-01-09-30_best_training_logging_validation_campaign_2026_03_14_00_56_06`
- Planning Report Path: `doc/reports/campaign_plans/mixed_training/2026-03-14-00-56-06_best_training_logging_validation_campaign_plan_report.md`
- Completed Runs: `1`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-03-14-01-09-30_001_01_best_training_logging_validation.yaml` | `te_feedforward_best_training` | `feedforward` | `completed` | `00:15:27` |

## Run Details

### te_feedforward_best_training

- Queue Config: `config/training/queue/completed/2026-03-14-01-09-30_001_01_best_training_logging_validation.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-14_best_training_logging_validation_campaign/01_best_training_logging_validation.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-14T01:09:30`
- End Time: `2026-03-14T01:24:57`
- Duration: `00:15:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/mixed_training/2026-03-14-00-56-06_best_training_logging_validation_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/legacy__te_feedforward_best_training`
- Config Snapshot: `output/training_runs/feedforward/legacy__te_feedforward_best_training/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/legacy__te_feedforward_best_training/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_best_training\checkpoints\feedforward-epoch=063-val_mae=0.00317104.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/legacy__te_feedforward_best_training/training_test_metrics.yaml`
- Training Report: `output/training_runs/feedforward/legacy__te_feedforward_best_training/training_test_report.md`
- Terminal Log: `output/training_campaigns/mixed_training/2026-03-14-01-09-30_best_training_logging_validation_campaign_2026_03_14_00_56_06/logs/2026-03-14-01-09-30_001_01_best_training_logging_validation.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `training_test_metrics.yaml` for numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
