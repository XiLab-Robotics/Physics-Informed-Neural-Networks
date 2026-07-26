# Training Campaign Execution Report

## Overview

- Campaign Name: `phase2_harmonic_kinematic_pinn_2026_07_26`
- Generated At: `2026-07-26T13:01:51`
- Queue Root: `config/training/queue/harmonic_kinematic_pinn/phase2_harmonic_kinematic_pinn_2026_07_26`
- Campaign Output Directory: `output/training_campaigns/2026-07-26-12-51-55_phase2_harmonic_kinematic_pinn_2026_07_26`
- Planning Report Path: `doc/reports/campaign_plans/model_development_waves/wave_5_2/harmonic_kinematic_pinn/2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md`
- Completed Runs: `0`
- Failed Runs: `1`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/harmonic_kinematic_pinn/phase2_harmonic_kinematic_pinn_2026_07_26/failed/2026-07-26-12-50-33_001_001_h0_fourier_control_fw.yaml` | `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | `harmonic_kinematic_pinn` | `failed` | `00:09:56` |

## Run Details

### te_phase2_pinn_h0_fourier_control_fw__polished_setpoints

- Queue Config: `config/training/queue/harmonic_kinematic_pinn/phase2_harmonic_kinematic_pinn_2026_07_26/failed/2026-07-26-12-50-33_001_001_h0_fourier_control_fw.yaml`
- Source Config: `N/A`
- Model Type: `harmonic_kinematic_pinn`
- Run Instance Id: `2026-07-26-12-50-34__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Queue Status: `failed`
- Start Time: `2026-07-26T12:51:55`
- End Time: `2026-07-26T13:01:51`
- Duration: `00:09:56`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/model_development_waves/wave_5_2/harmonic_kinematic_pinn/2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_kinematic_pinn/2026-07-26-12-50-34__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/harmonic_kinematic_pinn/2026-07-26-12-50-34__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-07-26-12-51-55_phase2_harmonic_kinematic_pinn_2026_07_26/logs/001_te_phase2_pinn_h0_fourier_control_fw__polished_s.log`
- Error Message: `[Errno 22] Invalid argument`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
