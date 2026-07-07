# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp__simplified_setpoints`
- Generated At: `2026-07-07T20:29:45`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-20-03-02_dataset_input_mode_retraining__periodic_mlp__simplified_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/completed/2026-07-07-20-03-02_001_001_periodic_mlp_global.yaml` | `te_periodic_mlp_global__simplified_setpoints` | `periodic_mlp` | `completed` | `00:11:13` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/completed/2026-07-07-20-03-02_002_002_periodic_mlp_fw.yaml` | `te_periodic_mlp_fw__simplified_setpoints` | `periodic_mlp` | `completed` | `00:06:39` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/completed/2026-07-07-20-03-02_003_003_periodic_mlp_bw.yaml` | `te_periodic_mlp_bw__simplified_setpoints` | `periodic_mlp` | `completed` | `00:08:51` |

## Run Details

### te_periodic_mlp_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/completed/2026-07-07-20-03-02_001_001_periodic_mlp_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/queue/001_periodic_mlp_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T20:03:02`
- End Time: `2026-07-07T20:14:15`
- Duration: `00:11:13`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/checkpoints/periodic_mlp-epoch=090-val_mae=0.00301298.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-20-03-02_dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/logs/001_te_periodic_mlp_global__simplified_setpoints.log`
- Error Message: `N/A`

### te_periodic_mlp_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/completed/2026-07-07-20-03-02_002_002_periodic_mlp_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/queue/002_periodic_mlp_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-20-14-15__te_periodic_mlp_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T20:14:15`
- End Time: `2026-07-07T20:20:54`
- Duration: `00:06:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-20-14-15__te_periodic_mlp_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-14-15__te_periodic_mlp_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-20-14-15__te_periodic_mlp_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-14-15__te_periodic_mlp_fw__simplified_setpoints/checkpoints/periodic_mlp-epoch=037-val_mae=0.00302141.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-14-15__te_periodic_mlp_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-20-14-15__te_periodic_mlp_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-20-03-02_dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/logs/002_te_periodic_mlp_fw__simplified_setpoints.log`
- Error Message: `N/A`

### te_periodic_mlp_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/completed/2026-07-07-20-03-02_003_003_periodic_mlp_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/queue/003_periodic_mlp_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T20:20:54`
- End Time: `2026-07-07T20:29:45`
- Duration: `00:08:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints/checkpoints/periodic_mlp-epoch=062-val_mae=0.00301630.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-20-03-02_dataset_input_mode_retraining__periodic_mlp__simplified_setpoints/logs/003_te_periodic_mlp_bw__simplified_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
