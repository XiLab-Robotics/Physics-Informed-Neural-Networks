# Training Campaign Execution Report

## Overview

- Campaign Name: `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15`
- Generated At: `2026-05-24T12:27:31`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Completed Runs: `9`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-05-24-11-20-37_001_01_temporal_convolution_global.yaml` | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | `completed` | `00:09:46` |
| `config/training/queue/completed/2026-05-24-11-20-37_002_02_temporal_convolution_fw.yaml` | `te_temporal_convolution_sequence_remote_Fw` | `temporal_convolution` | `completed` | `00:06:45` |
| `config/training/queue/completed/2026-05-24-11-20-37_003_03_temporal_convolution_bw.yaml` | `te_temporal_convolution_sequence_remote_Bw` | `temporal_convolution` | `completed` | `00:08:12` |
| `config/training/queue/completed/2026-05-24-11-20-37_004_04_gru_sequence_global.yaml` | `te_gru_sequence_remote_global` | `gru_sequence` | `completed` | `00:08:44` |
| `config/training/queue/completed/2026-05-24-11-20-37_005_05_gru_sequence_fw.yaml` | `te_gru_sequence_remote_Fw` | `gru_sequence` | `completed` | `00:06:01` |
| `config/training/queue/completed/2026-05-24-11-20-37_006_06_gru_sequence_bw.yaml` | `te_gru_sequence_remote_Bw` | `gru_sequence` | `completed` | `00:06:29` |
| `config/training/queue/completed/2026-05-24-11-20-37_007_07_lstm_sequence_global.yaml` | `te_lstm_sequence_remote_global` | `lstm_sequence` | `completed` | `00:09:56` |
| `config/training/queue/completed/2026-05-24-11-20-37_008_08_lstm_sequence_fw.yaml` | `te_lstm_sequence_remote_Fw` | `lstm_sequence` | `completed` | `00:04:31` |
| `config/training/queue/completed/2026-05-24-11-20-37_009_09_lstm_sequence_bw.yaml` | `te_lstm_sequence_remote_Bw` | `lstm_sequence` | `completed` | `00:06:29` |

## Run Details

### te_temporal_convolution_sequence_remote_global

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_001_01_temporal_convolution_global.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/01_temporal_convolution_global.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global`
- Queue Status: `completed`
- Start Time: `2026-05-24T11:20:37`
- End Time: `2026-05-24T11:30:23`
- Duration: `00:09:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global\checkpoints\temporal_convolution-epoch=055-val_mae=0.00393457.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/001_te_temporal_convolution_sequence_remote_global.log`
- Error Message: `N/A`

### te_temporal_convolution_sequence_remote_Fw

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_002_02_temporal_convolution_fw.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/02_temporal_convolution_fw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-05-24T11:30:23`
- End Time: `2026-05-24T11:37:07`
- Duration: `00:06:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution_fw/2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw`
- Config Snapshot: `output/training_runs/temporal_convolution_fw/2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution_fw/2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution_fw\2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw\checkpoints\temporal_convolution-epoch=059-val_mae=0.00349000.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution_fw/2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution_fw/2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/002_te_temporal_convolution_sequence_remote_fw.log`
- Error Message: `N/A`

### te_temporal_convolution_sequence_remote_Bw

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_003_03_temporal_convolution_bw.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/03_temporal_convolution_bw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-05-24T11:37:07`
- End Time: `2026-05-24T11:45:19`
- Duration: `00:08:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution_bw/2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw`
- Config Snapshot: `output/training_runs/temporal_convolution_bw/2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution_bw/2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution_bw\2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw\checkpoints\temporal_convolution-epoch=089-val_mae=0.00393295.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution_bw/2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution_bw/2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/003_te_temporal_convolution_sequence_remote_bw.log`
- Error Message: `N/A`

### te_gru_sequence_remote_global

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_004_04_gru_sequence_global.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/04_gru_sequence_global.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-05-24-11-45-19__te_gru_sequence_remote_global`
- Queue Status: `completed`
- Start Time: `2026-05-24T11:45:19`
- End Time: `2026-05-24T11:54:04`
- Duration: `00:08:44`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-05-24-11-45-19__te_gru_sequence_remote_global`
- Config Snapshot: `output/training_runs/gru_sequence/2026-05-24-11-45-19__te_gru_sequence_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-05-24-11-45-19__te_gru_sequence_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-05-24-11-45-19__te_gru_sequence_remote_global\checkpoints\gru_sequence-epoch=056-val_mae=0.00370743.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-05-24-11-45-19__te_gru_sequence_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-05-24-11-45-19__te_gru_sequence_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/004_te_gru_sequence_remote_global.log`
- Error Message: `N/A`

### te_gru_sequence_remote_Fw

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_005_05_gru_sequence_fw.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/05_gru_sequence_fw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-05-24-11-54-04__te_gru_sequence_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-05-24T11:54:04`
- End Time: `2026-05-24T12:00:05`
- Duration: `00:06:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence_fw/2026-05-24-11-54-04__te_gru_sequence_remote_fw`
- Config Snapshot: `output/training_runs/gru_sequence_fw/2026-05-24-11-54-04__te_gru_sequence_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence_fw/2026-05-24-11-54-04__te_gru_sequence_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence_fw\2026-05-24-11-54-04__te_gru_sequence_remote_fw\checkpoints\gru_sequence-epoch=045-val_mae=0.00340867.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence_fw/2026-05-24-11-54-04__te_gru_sequence_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence_fw/2026-05-24-11-54-04__te_gru_sequence_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/005_te_gru_sequence_remote_fw.log`
- Error Message: `N/A`

### te_gru_sequence_remote_Bw

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_006_06_gru_sequence_bw.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/06_gru_sequence_bw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-05-24-12-00-05__te_gru_sequence_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-05-24T12:00:05`
- End Time: `2026-05-24T12:06:34`
- Duration: `00:06:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence_bw/2026-05-24-12-00-05__te_gru_sequence_remote_bw`
- Config Snapshot: `output/training_runs/gru_sequence_bw/2026-05-24-12-00-05__te_gru_sequence_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence_bw/2026-05-24-12-00-05__te_gru_sequence_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence_bw\2026-05-24-12-00-05__te_gru_sequence_remote_bw\checkpoints\gru_sequence-epoch=058-val_mae=0.00386744.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence_bw/2026-05-24-12-00-05__te_gru_sequence_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence_bw/2026-05-24-12-00-05__te_gru_sequence_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/006_te_gru_sequence_remote_bw.log`
- Error Message: `N/A`

### te_lstm_sequence_remote_global

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_007_07_lstm_sequence_global.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/07_lstm_sequence_global.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-05-24-12-06-34__te_lstm_sequence_remote_global`
- Queue Status: `completed`
- Start Time: `2026-05-24T12:06:34`
- End Time: `2026-05-24T12:16:30`
- Duration: `00:09:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-05-24-12-06-34__te_lstm_sequence_remote_global`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-05-24-12-06-34__te_lstm_sequence_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-05-24-12-06-34__te_lstm_sequence_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence\2026-05-24-12-06-34__te_lstm_sequence_remote_global\checkpoints\lstm_sequence-epoch=045-val_mae=0.00368138.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-05-24-12-06-34__te_lstm_sequence_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-05-24-12-06-34__te_lstm_sequence_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/007_te_lstm_sequence_remote_global.log`
- Error Message: `N/A`

### te_lstm_sequence_remote_Fw

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_008_08_lstm_sequence_fw.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/08_lstm_sequence_fw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-05-24-12-16-30__te_lstm_sequence_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-05-24T12:16:30`
- End Time: `2026-05-24T12:21:01`
- Duration: `00:04:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence_fw/2026-05-24-12-16-30__te_lstm_sequence_remote_fw`
- Config Snapshot: `output/training_runs/lstm_sequence_fw/2026-05-24-12-16-30__te_lstm_sequence_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence_fw/2026-05-24-12-16-30__te_lstm_sequence_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence_fw\2026-05-24-12-16-30__te_lstm_sequence_remote_fw\checkpoints\lstm_sequence-epoch=012-val_mae=0.00344807.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence_fw/2026-05-24-12-16-30__te_lstm_sequence_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence_fw/2026-05-24-12-16-30__te_lstm_sequence_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/008_te_lstm_sequence_remote_fw.log`
- Error Message: `N/A`

### te_lstm_sequence_remote_Bw

- Queue Config: `config/training/queue/completed/2026-05-24-11-20-37_009_09_lstm_sequence_bw.yaml`
- Source Config: `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/09_lstm_sequence_bw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-05-24-12-21-01__te_lstm_sequence_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-05-24T12:21:01`
- End Time: `2026-05-24T12:27:31`
- Duration: `00:06:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence_bw/2026-05-24-12-21-01__te_lstm_sequence_remote_bw`
- Config Snapshot: `output/training_runs/lstm_sequence_bw/2026-05-24-12-21-01__te_lstm_sequence_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence_bw/2026-05-24-12-21-01__te_lstm_sequence_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence_bw\2026-05-24-12-21-01__te_lstm_sequence_remote_bw\checkpoints\lstm_sequence-epoch=055-val_mae=0.00381528.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence_bw/2026-05-24-12-21-01__te_lstm_sequence_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence_bw/2026-05-24-12-21-01__te_lstm_sequence_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/logs/009_te_lstm_sequence_remote_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
