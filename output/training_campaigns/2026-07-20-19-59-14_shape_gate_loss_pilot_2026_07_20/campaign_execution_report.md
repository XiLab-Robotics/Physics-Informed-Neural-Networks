# Training Campaign Execution Report

## Overview

- Campaign Name: `shape_gate_loss_pilot_2026_07_20`
- Generated At: `2026-07-20T20:07:19`
- Queue Root: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/config/training/queue/shape_gate_loss_pilot`
- Campaign Output Directory: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/output/training_campaigns/2026-07-20-19-59-14_shape_gate_loss_pilot_2026_07_20`
- Planning Report Path: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/doc/reports/campaign_plans/cross_wave/shape_gate_loss/2026-07-20-19-10-23_shape_gate_loss_pilot_campaign_plan_report.md`
- Completed Runs: `1`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/config/training/queue/shape_gate_loss_pilot/completed/2026-07-20-19-59-14_001_001_shape_gate_loss_periodic_gru_sequence_fw.yaml` | `te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | `completed` | `00:08:05` |

## Run Details

### te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints

- Queue Config: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/config/training/queue/shape_gate_loss_pilot/completed/2026-07-20-19-59-14_001_001_shape_gate_loss_periodic_gru_sequence_fw.yaml`
- Source Config: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/config/training/shape_gate_loss_pilot/campaigns/2026-07-20_shape_gate_loss_pilot/queue/001_shape_gate_loss_periodic_gru_sequence_fw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-20T19:59:14`
- End Time: `2026-07-20T20:07:19`
- Duration: `00:08:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/shape_gate_loss/2026-07-20-19-10-23_shape_gate_loss_pilot_campaign_plan_report.md`
- Output Directory: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints`
- Config Snapshot: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_gate_loss_pilot_periodic_gru_sequence\2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints\checkpoints\periodic_gru_sequence-epoch=007-val_mae=0.00229675.ckpt`
- Metrics Snapshot: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `C:/Users/Martina Salami/Documents/Davide/Physics-Informed-Neural-Networks/output/training_campaigns/2026-07-20-19-59-14_shape_gate_loss_pilot_2026_07_20/logs/001_te_shape_gate_loss_periodic_gru_sequence_fw__pol.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
