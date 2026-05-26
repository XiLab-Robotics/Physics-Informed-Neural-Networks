# Training Campaign Execution Report

## Overview

- Campaign Name: `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25`
- Generated At: `2026-05-25T20:05:38`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Completed Runs: `9`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-05-25-15-44-37_001_01_periodic_temporal_convolution_global.yaml` | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | `completed` | `00:25:37` |
| `config/training/queue/completed/2026-05-25-15-44-37_002_02_periodic_temporal_convolution_fw.yaml` | `te_periodic_temporal_convolution_sequence_remote_Fw` | `periodic_temporal_convolution` | `completed` | `00:08:15` |
| `config/training/queue/completed/2026-05-25-15-44-37_003_03_periodic_temporal_convolution_bw.yaml` | `te_periodic_temporal_convolution_sequence_remote_Bw` | `periodic_temporal_convolution` | `completed` | `00:08:25` |
| `config/training/queue/completed/2026-05-25-15-44-37_004_04_periodic_gru_sequence_global.yaml` | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | `completed` | `01:00:14` |
| `config/training/queue/completed/2026-05-25-15-44-37_005_05_periodic_gru_sequence_fw.yaml` | `te_periodic_gru_sequence_remote_Fw` | `periodic_gru_sequence` | `completed` | `00:11:11` |
| `config/training/queue/completed/2026-05-25-15-44-37_006_06_periodic_gru_sequence_bw.yaml` | `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence` | `completed` | `00:31:26` |
| `config/training/queue/completed/2026-05-25-15-44-37_007_07_periodic_lstm_sequence_global.yaml` | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | `completed` | `01:11:12` |
| `config/training/queue/completed/2026-05-25-15-44-37_008_08_periodic_lstm_sequence_fw.yaml` | `te_periodic_lstm_sequence_remote_Fw` | `periodic_lstm_sequence` | `completed` | `00:09:20` |
| `config/training/queue/completed/2026-05-25-15-44-37_009_09_periodic_lstm_sequence_bw.yaml` | `te_periodic_lstm_sequence_remote_Bw` | `periodic_lstm_sequence` | `completed` | `00:35:21` |

## Run Details

### te_periodic_temporal_convolution_sequence_remote_global

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_001_01_periodic_temporal_convolution_global.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/01_periodic_temporal_convolution_global.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-05-25-15-44-37__te_periodic_temporal_convolution_sequence_remote_global`
- Queue Status: `completed`
- Start Time: `2026-05-25T15:44:37`
- End Time: `2026-05-25T16:10:13`
- Duration: `00:25:37`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-05-25-15-44-37__te_periodic_temporal_convolution_sequence_remote_global`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-05-25-15-44-37__te_periodic_temporal_convolution_sequence_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-05-25-15-44-37__te_periodic_temporal_convolution_sequence_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution\2026-05-25-15-44-37__te_periodic_temporal_convolution_sequence_remote_global\checkpoints\periodic_temporal_convolution-epoch=088-val_mae=0.00363409.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-05-25-15-44-37__te_periodic_temporal_convolution_sequence_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-05-25-15-44-37__te_periodic_temporal_convolution_sequence_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/001_te_periodic_temporal_convolution_sequence_remote.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_sequence_remote_Fw

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_002_02_periodic_temporal_convolution_fw.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/02_periodic_temporal_convolution_fw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-05-25T16:10:13`
- End Time: `2026-05-25T16:18:28`
- Duration: `00:08:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution_fw/2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution_fw/2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution_fw/2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution_fw\2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw\checkpoints\periodic_temporal_convolution-epoch=017-val_mae=0.00332097.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution_fw/2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution_fw/2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/002_te_periodic_temporal_convolution_sequence_remote.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_sequence_remote_Bw

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_003_03_periodic_temporal_convolution_bw.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/03_periodic_temporal_convolution_bw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-05-25T16:18:28`
- End Time: `2026-05-25T16:26:53`
- Duration: `00:08:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution_bw/2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution_bw/2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution_bw/2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution_bw\2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw\checkpoints\periodic_temporal_convolution-epoch=018-val_mae=0.00388991.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution_bw/2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution_bw/2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/003_te_periodic_temporal_convolution_sequence_remote.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_remote_global

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_004_04_periodic_gru_sequence_global.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/04_periodic_gru_sequence_global.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global`
- Queue Status: `completed`
- Start Time: `2026-05-25T16:26:53`
- End Time: `2026-05-25T17:27:07`
- Duration: `01:00:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global\checkpoints\periodic_gru_sequence-epoch=251-val_mae=0.00250715.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/004_te_periodic_gru_sequence_remote_global.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_remote_Fw

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_005_05_periodic_gru_sequence_fw.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/05_periodic_gru_sequence_fw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-05-25-17-27-08__te_periodic_gru_sequence_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-05-25T17:27:08`
- End Time: `2026-05-25T17:38:18`
- Duration: `00:11:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence_fw/2026-05-25-17-27-08__te_periodic_gru_sequence_remote_fw`
- Config Snapshot: `output/training_runs/periodic_gru_sequence_fw/2026-05-25-17-27-08__te_periodic_gru_sequence_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence_fw/2026-05-25-17-27-08__te_periodic_gru_sequence_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence_fw\2026-05-25-17-27-08__te_periodic_gru_sequence_remote_fw\checkpoints\periodic_gru_sequence-epoch=029-val_mae=0.00322710.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence_fw/2026-05-25-17-27-08__te_periodic_gru_sequence_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence_fw/2026-05-25-17-27-08__te_periodic_gru_sequence_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/005_te_periodic_gru_sequence_remote_fw.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_remote_Bw

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_006_06_periodic_gru_sequence_bw.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/06_periodic_gru_sequence_bw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-05-25T17:38:18`
- End Time: `2026-05-25T18:09:44`
- Duration: `00:31:26`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence_bw/2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw`
- Config Snapshot: `output/training_runs/periodic_gru_sequence_bw/2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence_bw/2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence_bw\2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw\checkpoints\periodic_gru_sequence-epoch=252-val_mae=0.00252321.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence_bw/2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence_bw/2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/006_te_periodic_gru_sequence_remote_bw.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_remote_global

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_007_07_periodic_lstm_sequence_global.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/07_periodic_lstm_sequence_global.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-05-25-18-09-44__te_periodic_lstm_sequence_remote_global`
- Queue Status: `completed`
- Start Time: `2026-05-25T18:09:44`
- End Time: `2026-05-25T19:20:56`
- Duration: `01:11:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-05-25-18-09-44__te_periodic_lstm_sequence_remote_global`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-05-25-18-09-44__te_periodic_lstm_sequence_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-05-25-18-09-44__te_periodic_lstm_sequence_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence\2026-05-25-18-09-44__te_periodic_lstm_sequence_remote_global\checkpoints\periodic_lstm_sequence-epoch=257-val_mae=0.00252630.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-05-25-18-09-44__te_periodic_lstm_sequence_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-05-25-18-09-44__te_periodic_lstm_sequence_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/007_te_periodic_lstm_sequence_remote_global.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_remote_Fw

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_008_08_periodic_lstm_sequence_fw.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/08_periodic_lstm_sequence_fw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-05-25-19-20-56__te_periodic_lstm_sequence_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-05-25T19:20:56`
- End Time: `2026-05-25T19:30:17`
- Duration: `00:09:20`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence_fw/2026-05-25-19-20-56__te_periodic_lstm_sequence_remote_fw`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence_fw/2026-05-25-19-20-56__te_periodic_lstm_sequence_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence_fw/2026-05-25-19-20-56__te_periodic_lstm_sequence_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence_fw\2026-05-25-19-20-56__te_periodic_lstm_sequence_remote_fw\checkpoints\periodic_lstm_sequence-epoch=007-val_mae=0.00325365.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence_fw/2026-05-25-19-20-56__te_periodic_lstm_sequence_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence_fw/2026-05-25-19-20-56__te_periodic_lstm_sequence_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/008_te_periodic_lstm_sequence_remote_fw.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_remote_Bw

- Queue Config: `config/training/queue/completed/2026-05-25-15-44-37_009_09_periodic_lstm_sequence_bw.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/09_periodic_lstm_sequence_bw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-05-25-19-30-17__te_periodic_lstm_sequence_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-05-25T19:30:17`
- End Time: `2026-05-25T20:05:38`
- Duration: `00:35:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence_bw/2026-05-25-19-30-17__te_periodic_lstm_sequence_remote_bw`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence_bw/2026-05-25-19-30-17__te_periodic_lstm_sequence_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence_bw/2026-05-25-19-30-17__te_periodic_lstm_sequence_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence_bw\2026-05-25-19-30-17__te_periodic_lstm_sequence_remote_bw\checkpoints\periodic_lstm_sequence-epoch=243-val_mae=0.00243159.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence_bw/2026-05-25-19-30-17__te_periodic_lstm_sequence_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence_bw/2026-05-25-19-30-17__te_periodic_lstm_sequence_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/logs/009_te_periodic_lstm_sequence_remote_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
