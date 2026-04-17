# Training Campaign Execution Report

## Overview

- Campaign Name: `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42`
- Generated At: `2026-03-20T18:32:18`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
- Completed Runs: `6`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-03-20-16-11-22_001_01_harmonic_order06_static_recovery.yaml` | `te_harmonic_order06_static_recovery` | `harmonic_regression` | `completed` | `00:09:05` |
| `config/training/queue/completed/2026-03-20-16-11-22_002_02_harmonic_order12_static_recovery.yaml` | `te_harmonic_order12_static_recovery` | `harmonic_regression` | `completed` | `00:10:53` |
| `config/training/queue/completed/2026-03-20-16-11-22_003_03_harmonic_order12_linear_conditioned_recovery.yaml` | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | `completed` | `00:09:45` |
| `config/training/queue/completed/2026-03-20-16-11-22_004_04_residual_h12_small_frozen_recovery.yaml` | `te_residual_h12_small_frozen_recovery` | `residual_harmonic_mlp` | `completed` | `00:17:29` |
| `config/training/queue/completed/2026-03-20-16-11-22_005_05_residual_h12_small_joint_recovery.yaml` | `te_residual_h12_small_joint_recovery` | `residual_harmonic_mlp` | `completed` | `00:16:51` |
| `config/training/queue/completed/2026-03-20-16-11-22_006_06_random_forest_tabular_conservative.yaml` | `te_random_forest_tabular_recovery` | `random_forest` | `completed` | `01:16:53` |

## Run Details

### te_harmonic_order06_static_recovery

- Queue Config: `config/training/queue/completed/2026-03-20-16-11-22_001_01_harmonic_order06_static_recovery.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-20_wave1_structured_baseline_recovery_campaign/01_harmonic_order06_static_recovery.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-03-20-16-11-22__te_harmonic_order06_static_recovery`
- Queue Status: `completed`
- Start Time: `2026-03-20T16:11:22`
- End Time: `2026-03-20T16:20:27`
- Duration: `00:09:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-03-20-16-11-22__te_harmonic_order06_static_recovery`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-03-20-16-11-22__te_harmonic_order06_static_recovery/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-03-20-16-11-22__te_harmonic_order06_static_recovery/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-03-20-16-11-22__te_harmonic_order06_static_recovery\checkpoints\harmonic_regression-epoch=005-val_mae=0.04052873.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-03-20-16-11-22__te_harmonic_order06_static_recovery/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-03-20-16-11-22__te_harmonic_order06_static_recovery/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/logs/001_te_harmonic_order06_static_recovery.log`
- Error Message: `N/A`

### te_harmonic_order12_static_recovery

- Queue Config: `config/training/queue/completed/2026-03-20-16-11-22_002_02_harmonic_order12_static_recovery.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-20_wave1_structured_baseline_recovery_campaign/02_harmonic_order12_static_recovery.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-03-20-16-20-27__te_harmonic_order12_static_recovery`
- Queue Status: `completed`
- Start Time: `2026-03-20T16:20:27`
- End Time: `2026-03-20T16:31:19`
- Duration: `00:10:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-03-20-16-20-27__te_harmonic_order12_static_recovery`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-03-20-16-20-27__te_harmonic_order12_static_recovery/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-03-20-16-20-27__te_harmonic_order12_static_recovery/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-03-20-16-20-27__te_harmonic_order12_static_recovery\checkpoints\harmonic_regression-epoch=017-val_mae=0.04052421.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-03-20-16-20-27__te_harmonic_order12_static_recovery/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-03-20-16-20-27__te_harmonic_order12_static_recovery/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/logs/002_te_harmonic_order12_static_recovery.log`
- Error Message: `N/A`

### te_harmonic_order12_linear_conditioned_recovery

- Queue Config: `config/training/queue/completed/2026-03-20-16-11-22_003_03_harmonic_order12_linear_conditioned_recovery.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-20_wave1_structured_baseline_recovery_campaign/03_harmonic_order12_linear_conditioned_recovery.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery`
- Queue Status: `completed`
- Start Time: `2026-03-20T16:31:19`
- End Time: `2026-03-20T16:41:05`
- Duration: `00:09:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery\checkpoints\harmonic_regression-epoch=026-val_mae=0.01700371.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/logs/003_te_harmonic_order12_linear_conditioned_recovery.log`
- Error Message: `N/A`

### te_residual_h12_small_frozen_recovery

- Queue Config: `config/training/queue/completed/2026-03-20-16-11-22_004_04_residual_h12_small_frozen_recovery.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-20_wave1_structured_baseline_recovery_campaign/04_residual_h12_small_frozen_recovery.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery`
- Queue Status: `completed`
- Start Time: `2026-03-20T16:41:05`
- End Time: `2026-03-20T16:58:34`
- Duration: `00:17:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery\checkpoints\residual_harmonic_mlp-epoch=092-val_mae=0.00303009.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/logs/004_te_residual_h12_small_frozen_recovery.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_recovery

- Queue Config: `config/training/queue/completed/2026-03-20-16-11-22_005_05_residual_h12_small_joint_recovery.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-20_wave1_structured_baseline_recovery_campaign/05_residual_h12_small_joint_recovery.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-20-16-58-34__te_residual_h12_small_joint_recovery`
- Queue Status: `completed`
- Start Time: `2026-03-20T16:58:34`
- End Time: `2026-03-20T17:15:25`
- Duration: `00:16:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-58-34__te_residual_h12_small_joint_recovery`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-58-34__te_residual_h12_small_joint_recovery/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-58-34__te_residual_h12_small_joint_recovery/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-20-16-58-34__te_residual_h12_small_joint_recovery\checkpoints\residual_harmonic_mlp-epoch=056-val_mae=0.00301633.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-58-34__te_residual_h12_small_joint_recovery/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-20-16-58-34__te_residual_h12_small_joint_recovery/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/logs/005_te_residual_h12_small_joint_recovery.log`
- Error Message: `N/A`

### te_random_forest_tabular_recovery

- Queue Config: `config/training/queue/completed/2026-03-20-16-11-22_006_06_random_forest_tabular_conservative.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-20_wave1_structured_baseline_recovery_campaign/06_random_forest_tabular_conservative.yaml`
- Model Type: `random_forest`
- Run Instance Id: `2026-03-20-17-15-25__te_random_forest_tabular_recovery`
- Queue Status: `completed`
- Start Time: `2026-03-20T17:15:25`
- End Time: `2026-03-20T18:32:18`
- Duration: `01:16:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-03-20-17-15-25__te_random_forest_tabular_recovery`
- Config Snapshot: `output/training_runs/tree/2026-03-20-17-15-25__te_random_forest_tabular_recovery/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-03-20-17-15-25__te_random_forest_tabular_recovery/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-03-20-17-15-25__te_random_forest_tabular_recovery/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/logs/006_te_random_forest_tabular_recovery.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
