# Training Campaign Execution Report

## Overview

- Campaign Name: `track2h_quantile_probabilistic_campaign_2026_06_12`
- Generated At: `2026-06-12T13:53:26`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md`
- Completed Runs: `6`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-12-11-16-18_001_01_quantile_p10_p50_p90_global.yaml` | `te_track2h_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:18:38` |
| `config/training/queue/completed/2026-06-12-11-16-18_002_02_quantile_p10_p50_p90_fw.yaml` | `te_track2h_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:08:53` |
| `config/training/queue/completed/2026-06-12-11-16-18_003_03_quantile_p10_p50_p90_bw.yaml` | `te_track2h_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:26:33` |
| `config/training/queue/completed/2026-06-12-11-16-18_004_04_gaussian_nll_global.yaml` | `te_track2h_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `01:02:12` |
| `config/training/queue/completed/2026-06-12-11-16-18_005_05_gaussian_nll_fw.yaml` | `te_track2h_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:13:18` |
| `config/training/queue/completed/2026-06-12-11-16-18_006_06_gaussian_nll_bw.yaml` | `te_track2h_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:27:33` |

## Run Details

### te_track2h_quantile_p10_p50_p90_global

- Queue Config: `config/training/queue/completed/2026-06-12-11-16-18_001_01_quantile_p10_p50_p90_global.yaml`
- Source Config: `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/01_quantile_p10_p50_p90_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global`
- Queue Status: `completed`
- Start Time: `2026-06-12T11:16:18`
- End Time: `2026-06-12T11:34:56`
- Duration: `00:18:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_global/2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global`
- Config Snapshot: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_global/2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_global/2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_global\2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=030-val_mae=0.00360589.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_global/2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_global/2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/logs/001_te_track2h_quantile_p10_p50_p90_global.log`
- Error Message: `N/A`

### te_track2h_quantile_p10_p50_p90_fw

- Queue Config: `config/training/queue/completed/2026-06-12-11-16-18_002_02_quantile_p10_p50_p90_fw.yaml`
- Source Config: `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/02_quantile_p10_p50_p90_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw`
- Queue Status: `completed`
- Start Time: `2026-06-12T11:34:56`
- End Time: `2026-06-12T11:43:50`
- Duration: `00:08:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_fw/2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw`
- Config Snapshot: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_fw/2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_fw/2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_fw\2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=019-val_mae=0.00326876.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_fw/2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_fw/2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/logs/002_te_track2h_quantile_p10_p50_p90_fw.log`
- Error Message: `N/A`

### te_track2h_quantile_p10_p50_p90_bw

- Queue Config: `config/training/queue/completed/2026-06-12-11-16-18_003_03_quantile_p10_p50_p90_bw.yaml`
- Source Config: `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/03_quantile_p10_p50_p90_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw`
- Queue Status: `completed`
- Start Time: `2026-06-12T11:43:50`
- End Time: `2026-06-12T12:10:23`
- Duration: `00:26:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_bw/2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw`
- Config Snapshot: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_bw/2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_bw/2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_bw\2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=206-val_mae=0.00343553.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_bw/2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_quantile_probabilistic_quantile_p10_p50_p90_bw/2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/logs/003_te_track2h_quantile_p10_p50_p90_bw.log`
- Error Message: `N/A`

### te_track2h_gaussian_nll_global

- Queue Config: `config/training/queue/completed/2026-06-12-11-16-18_004_04_gaussian_nll_global.yaml`
- Source Config: `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/04_gaussian_nll_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-12-12-10-23__te_track2h_gaussian_nll_global`
- Queue Status: `completed`
- Start Time: `2026-06-12T12:10:23`
- End Time: `2026-06-12T13:12:35`
- Duration: `01:02:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_global/2026-06-12-12-10-23__te_track2h_gaussian_nll_global`
- Config Snapshot: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_global/2026-06-12-12-10-23__te_track2h_gaussian_nll_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_global/2026-06-12-12-10-23__te_track2h_gaussian_nll_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_gaussian_nll_global\2026-06-12-12-10-23__te_track2h_gaussian_nll_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=230-val_mae=0.00326664.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_global/2026-06-12-12-10-23__te_track2h_gaussian_nll_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_global/2026-06-12-12-10-23__te_track2h_gaussian_nll_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/logs/004_te_track2h_gaussian_nll_global.log`
- Error Message: `N/A`

### te_track2h_gaussian_nll_fw

- Queue Config: `config/training/queue/completed/2026-06-12-11-16-18_005_05_gaussian_nll_fw.yaml`
- Source Config: `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/05_gaussian_nll_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-12-13-12-35__te_track2h_gaussian_nll_fw`
- Queue Status: `completed`
- Start Time: `2026-06-12T13:12:35`
- End Time: `2026-06-12T13:25:53`
- Duration: `00:13:18`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_fw/2026-06-12-13-12-35__te_track2h_gaussian_nll_fw`
- Config Snapshot: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_fw/2026-06-12-13-12-35__te_track2h_gaussian_nll_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_fw/2026-06-12-13-12-35__te_track2h_gaussian_nll_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_gaussian_nll_fw\2026-06-12-13-12-35__te_track2h_gaussian_nll_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=056-val_mae=0.00329281.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_fw/2026-06-12-13-12-35__te_track2h_gaussian_nll_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_fw/2026-06-12-13-12-35__te_track2h_gaussian_nll_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/logs/005_te_track2h_gaussian_nll_fw.log`
- Error Message: `N/A`

### te_track2h_gaussian_nll_bw

- Queue Config: `config/training/queue/completed/2026-06-12-11-16-18_006_06_gaussian_nll_bw.yaml`
- Source Config: `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue/06_gaussian_nll_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-12-13-25-53__te_track2h_gaussian_nll_bw`
- Queue Status: `completed`
- Start Time: `2026-06-12T13:25:53`
- End Time: `2026-06-12T13:53:26`
- Duration: `00:27:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_bw/2026-06-12-13-25-53__te_track2h_gaussian_nll_bw`
- Config Snapshot: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_bw/2026-06-12-13-25-53__te_track2h_gaussian_nll_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_bw/2026-06-12-13-25-53__te_track2h_gaussian_nll_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_gaussian_nll_bw\2026-06-12-13-25-53__te_track2h_gaussian_nll_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=180-val_mae=0.00329833.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_bw/2026-06-12-13-25-53__te_track2h_gaussian_nll_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_quantile_probabilistic_gaussian_nll_bw/2026-06-12-13-25-53__te_track2h_gaussian_nll_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/logs/006_te_track2h_gaussian_nll_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
