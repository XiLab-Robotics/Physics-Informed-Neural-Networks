# Training Campaign Execution Report

## Overview

- Campaign Name: `wave1_structured_baseline_campaign_2026_03_17_21_01_47`
- Generated At: `2026-03-20T15:20:04`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Completed Runs: `4`
- Failed Runs: `6`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/failed/2026-03-20-14-18-30_001_01_harmonic_order06_static.yaml` | `te_harmonic_order06_static` | `harmonic_regression` | `failed` | `00:00:27` |
| `config/training/queue/failed/2026-03-20-14-18-30_002_02_harmonic_order12_static.yaml` | `te_harmonic_order12_static` | `harmonic_regression` | `failed` | `00:00:18` |
| `config/training/queue/failed/2026-03-20-14-18-30_003_03_harmonic_order12_linear_conditioned.yaml` | `te_harmonic_order12_linear_conditioned` | `harmonic_regression` | `failed` | `00:00:18` |
| `config/training/queue/completed/2026-03-20-14-18-30_004_04_periodic_mlp_h04_standard.yaml` | `te_periodic_mlp_h04_standard` | `periodic_mlp` | `completed` | `00:16:22` |
| `config/training/queue/completed/2026-03-20-14-18-30_005_05_periodic_mlp_h08_standard.yaml` | `te_periodic_mlp_h08_standard` | `periodic_mlp` | `completed` | `00:16:46` |
| `config/training/queue/completed/2026-03-20-14-18-30_006_06_periodic_mlp_h08_wide.yaml` | `te_periodic_mlp_h08_wide` | `periodic_mlp` | `completed` | `00:17:22` |
| `config/training/queue/failed/2026-03-20-14-18-30_007_07_residual_h12_small_frozen.yaml` | `te_residual_h12_small_frozen` | `residual_harmonic_mlp` | `failed` | `00:00:20` |
| `config/training/queue/failed/2026-03-20-14-18-30_008_08_residual_h12_small_joint.yaml` | `te_residual_h12_small_joint` | `residual_harmonic_mlp` | `failed` | `00:00:20` |
| `config/training/queue/failed/2026-03-20-14-18-30_009_09_random_forest_tabular.yaml` | `te_random_forest_tabular` | `random_forest` | `failed` | `00:06:46` |
| `config/training/queue/completed/2026-03-20-14-18-30_010_10_hist_gbr_tabular.yaml` | `te_hist_gbr_tabular` | `hist_gradient_boosting` | `completed` | `00:02:34` |

## Run Details

### te_harmonic_order06_static

- Queue Config: `config/training/queue/failed/2026-03-20-14-18-30_001_01_harmonic_order06_static.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/01_harmonic_order06_static.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-03-20-14-18-30__te_harmonic_order06_static`
- Queue Status: `failed`
- Start Time: `2026-03-20T14:18:30`
- End Time: `2026-03-20T14:18:57`
- Duration: `00:00:27`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-03-20-14-18-30__te_harmonic_order06_static`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-03-20-14-18-30__te_harmonic_order06_static/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_001_01_harmonic_order06_static.log`
- Error Message: `'hidden_size'`

### te_harmonic_order12_static

- Queue Config: `config/training/queue/failed/2026-03-20-14-18-30_002_02_harmonic_order12_static.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/02_harmonic_order12_static.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-03-20-14-18-57__te_harmonic_order12_static`
- Queue Status: `failed`
- Start Time: `2026-03-20T14:18:57`
- End Time: `2026-03-20T14:19:15`
- Duration: `00:00:18`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-03-20-14-18-57__te_harmonic_order12_static`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-03-20-14-18-57__te_harmonic_order12_static/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_002_02_harmonic_order12_static.log`
- Error Message: `'hidden_size'`

### te_harmonic_order12_linear_conditioned

- Queue Config: `config/training/queue/failed/2026-03-20-14-18-30_003_03_harmonic_order12_linear_conditioned.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/03_harmonic_order12_linear_conditioned.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-03-20-14-19-15__te_harmonic_order12_linear_conditioned`
- Queue Status: `failed`
- Start Time: `2026-03-20T14:19:15`
- End Time: `2026-03-20T14:19:32`
- Duration: `00:00:18`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-03-20-14-19-15__te_harmonic_order12_linear_conditioned`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-03-20-14-19-15__te_harmonic_order12_linear_conditioned/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_003_03_harmonic_order12_linear_conditioned.log`
- Error Message: `'hidden_size'`

### te_periodic_mlp_h04_standard

- Queue Config: `config/training/queue/completed/2026-03-20-14-18-30_004_04_periodic_mlp_h04_standard.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/04_periodic_mlp_h04_standard.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-03-20-14-19-32__te_periodic_mlp_h04_standard`
- Queue Status: `completed`
- Start Time: `2026-03-20T14:19:32`
- End Time: `2026-03-20T14:35:54`
- Duration: `00:16:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-03-20-14-19-32__te_periodic_mlp_h04_standard`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-03-20-14-19-32__te_periodic_mlp_h04_standard/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-03-20-14-19-32__te_periodic_mlp_h04_standard/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-03-20-14-19-32__te_periodic_mlp_h04_standard\checkpoints\periodic_mlp-epoch=031-val_mae=0.00309735.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-03-20-14-19-32__te_periodic_mlp_h04_standard/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-03-20-14-19-32__te_periodic_mlp_h04_standard/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_004_04_periodic_mlp_h04_standard.log`
- Error Message: `N/A`

### te_periodic_mlp_h08_standard

- Queue Config: `config/training/queue/completed/2026-03-20-14-18-30_005_05_periodic_mlp_h08_standard.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/05_periodic_mlp_h08_standard.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-03-20-14-35-54__te_periodic_mlp_h08_standard`
- Queue Status: `completed`
- Start Time: `2026-03-20T14:35:54`
- End Time: `2026-03-20T14:52:40`
- Duration: `00:16:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-03-20-14-35-54__te_periodic_mlp_h08_standard`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-03-20-14-35-54__te_periodic_mlp_h08_standard/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-03-20-14-35-54__te_periodic_mlp_h08_standard/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-03-20-14-35-54__te_periodic_mlp_h08_standard\checkpoints\periodic_mlp-epoch=027-val_mae=0.00308566.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-03-20-14-35-54__te_periodic_mlp_h08_standard/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-03-20-14-35-54__te_periodic_mlp_h08_standard/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_005_05_periodic_mlp_h08_standard.log`
- Error Message: `N/A`

### te_periodic_mlp_h08_wide

- Queue Config: `config/training/queue/completed/2026-03-20-14-18-30_006_06_periodic_mlp_h08_wide.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/06_periodic_mlp_h08_wide.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-03-20-14-52-40__te_periodic_mlp_h08_wide`
- Queue Status: `completed`
- Start Time: `2026-03-20T14:52:40`
- End Time: `2026-03-20T15:10:02`
- Duration: `00:17:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-03-20-14-52-40__te_periodic_mlp_h08_wide`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-03-20-14-52-40__te_periodic_mlp_h08_wide/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-03-20-14-52-40__te_periodic_mlp_h08_wide/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-03-20-14-52-40__te_periodic_mlp_h08_wide\checkpoints\periodic_mlp-epoch=046-val_mae=0.00308864.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-03-20-14-52-40__te_periodic_mlp_h08_wide/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-03-20-14-52-40__te_periodic_mlp_h08_wide/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_006_06_periodic_mlp_h08_wide.log`
- Error Message: `N/A`

### te_residual_h12_small_frozen

- Queue Config: `config/training/queue/failed/2026-03-20-14-18-30_007_07_residual_h12_small_frozen.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/07_residual_h12_small_frozen.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-20-15-10-02__te_residual_h12_small_frozen`
- Queue Status: `failed`
- Start Time: `2026-03-20T15:10:02`
- End Time: `2026-03-20T15:10:22`
- Duration: `00:00:20`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-20-15-10-02__te_residual_h12_small_frozen`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-20-15-10-02__te_residual_h12_small_frozen/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_007_07_residual_h12_small_frozen.log`
- Error Message: `'hidden_size'`

### te_residual_h12_small_joint

- Queue Config: `config/training/queue/failed/2026-03-20-14-18-30_008_08_residual_h12_small_joint.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/08_residual_h12_small_joint.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-20-15-10-22__te_residual_h12_small_joint`
- Queue Status: `failed`
- Start Time: `2026-03-20T15:10:22`
- End Time: `2026-03-20T15:10:42`
- Duration: `00:00:20`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-20-15-10-22__te_residual_h12_small_joint`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-20-15-10-22__te_residual_h12_small_joint/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_008_08_residual_h12_small_joint.log`
- Error Message: `'hidden_size'`

### te_random_forest_tabular

- Queue Config: `config/training/queue/failed/2026-03-20-14-18-30_009_09_random_forest_tabular.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/09_random_forest_tabular.yaml`
- Model Type: `random_forest`
- Run Instance Id: `2026-03-20-15-10-42__te_random_forest_tabular`
- Queue Status: `failed`
- Start Time: `2026-03-20T15:10:42`
- End Time: `2026-03-20T15:17:29`
- Duration: `00:06:46`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-03-20-15-10-42__te_random_forest_tabular`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_009_09_random_forest_tabular.log`
- Error Message: `could not allocate 134217728 bytes`

### te_hist_gbr_tabular

- Queue Config: `config/training/queue/completed/2026-03-20-14-18-30_010_10_hist_gbr_tabular.yaml`
- Source Config: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/10_hist_gbr_tabular.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-03-20-15-17-29__te_hist_gbr_tabular`
- Queue Status: `completed`
- Start Time: `2026-03-20T15:17:29`
- End Time: `2026-03-20T15:20:03`
- Duration: `00:02:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-03-20-15-17-29__te_hist_gbr_tabular`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/logs/2026-03-20-14-18-30_010_10_hist_gbr_tabular.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
