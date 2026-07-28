# Training Campaign Execution Report

## Overview

- Campaign Name: `wave52r_stage4_data_only_residual_capacity_2026_07_28`
- Generated At: `2026-07-28T10:00:02`
- Queue Root: `config/training/queue/data_only_residual_capacity/wave52r_stage4_data_only_residual_capacity_2026_07_28`
- Campaign Output Directory: `output/training_campaigns/2026-07-28-10-00-02_wave52r_stage4_data_only_residual_capacity_2026_07_28`
- Planning Report Path: `doc/reports/campaign_plans/model_development_waves/wave_5_2/data_only_residual_capacity_ladder/2026-07-27-22-39-42_wave52r_stage4_data_only_residual_capacity_ladder_campaign_plan_report.md`
- Completed Runs: `0`
- Failed Runs: `1`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/data_only_residual_capacity/wave52r_stage4_data_only_residual_capacity_2026_07_28/failed/2026-07-28-10-00-02_001_001_c01_r1_compact.yaml` | `te_stage4_c01_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | `failed` | `00:00:00` |

## Run Details

### te_stage4_c01_r1_compact__polished_setpoints_fw

- Queue Config: `config/training/queue/data_only_residual_capacity/wave52r_stage4_data_only_residual_capacity_2026_07_28/failed/2026-07-28-10-00-02_001_001_c01_r1_compact.yaml`
- Source Config: `config/training/data_only_residual_capacity/campaigns/2026-07-28_wave52r_stage4_data_only_residual_capacity/queue/001_c01_r1_compact.yaml`
- Model Type: `data_only_residual_capacity`
- Run Instance Id: `2026-07-28-10-00-02__te_stage4_c01_r1_compact__polished_setpoints_fw`
- Queue Status: `failed`
- Start Time: `2026-07-28T10:00:02`
- End Time: `2026-07-28T10:00:02`
- Duration: `00:00:00`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/model_development_waves/wave_5_2/data_only_residual_capacity_ladder/2026-07-27-22-39-42_wave52r_stage4_data_only_residual_capacity_ladder_campaign_plan_report.md`
- Output Directory: `output/training_runs/data_only_residual_capacity/2026-07-28-10-00-02__te_stage4_c01_r1_compact__polished_setpoints_fw`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-07-28-10-00-02_wave52r_stage4_data_only_residual_capacity_2026_07_28/logs/001_te_stage4_c01_r1_compact__polished_setpoints_fw.log`
- Error Message: `Unsupported Model Type for Campaign Runner | data_only_residual_capacity | Supported: ['curve_aware_harmonic_residual_offset_probe', 'feedforward', 'gru_sequence', 'harmonic_kinematic_pinn', 'harmonic_regression', 'harmonic_residual_offset_probe', 'hist_gradient_boosting', 'latent_state_hysteresis_probe', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'quasi_static_compliance_pinn', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution', 'wave3_harmonic_prior_residual', 'wave52b_offset_harmonic_guided']`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
