# Training Campaign Execution Report

## Overview

- Campaign Name: `phase2_harmonic_kinematic_pinn_2026_07_26`
- Generated At: `2026-07-26T12:50:34`
- Queue Root: `config/training/queue/harmonic_kinematic_pinn/phase2_harmonic_kinematic_pinn_2026_07_26`
- Campaign Output Directory: `output/training_campaigns/2026-07-26-12-50-34_phase2_harmonic_kinematic_pinn_2026_07_26`
- Planning Report Path: `doc/reports/campaign_plans/model_development_waves/wave_5_2/harmonic_kinematic_pinn/2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md`
- Completed Runs: `0`
- Failed Runs: `1`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/harmonic_kinematic_pinn/phase2_harmonic_kinematic_pinn_2026_07_26/failed/2026-07-26-12-50-33_001_001_h0_fourier_control_fw.yaml` | `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | `harmonic_kinematic_pinn` | `failed` | `00:00:00` |

## Run Details

### te_phase2_pinn_h0_fourier_control_fw__polished_setpoints

- Queue Config: `config/training/queue/harmonic_kinematic_pinn/phase2_harmonic_kinematic_pinn_2026_07_26/failed/2026-07-26-12-50-33_001_001_h0_fourier_control_fw.yaml`
- Source Config: `config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/001_h0_fourier_control_fw.yaml`
- Model Type: `harmonic_kinematic_pinn`
- Run Instance Id: `2026-07-26-12-50-34__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Queue Status: `failed`
- Start Time: `2026-07-26T12:50:34`
- End Time: `2026-07-26T12:50:34`
- Duration: `00:00:00`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/model_development_waves/wave_5_2/harmonic_kinematic_pinn/2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_kinematic_pinn/2026-07-26-12-50-34__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-07-26-12-50-34_phase2_harmonic_kinematic_pinn_2026_07_26/logs/001_te_phase2_pinn_h0_fourier_control_fw__polished_s.log`
- Error Message: `Unsupported Model Type for Campaign Runner | harmonic_kinematic_pinn | Supported: ['curve_aware_harmonic_residual_offset_probe', 'feedforward', 'gru_sequence', 'harmonic_regression', 'harmonic_residual_offset_probe', 'hist_gradient_boosting', 'latent_state_hysteresis_probe', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution', 'wave3_harmonic_prior_residual', 'wave52b_offset_harmonic_guided']`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
