# Campaign Best Run

## Overview

- Campaign Name: `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26`
- Run Name: `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Run Instance Id: `2026-07-26-14-03-44__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Model Family: `phase2_pinn_h0_fourier_control_fw`
- Model Type: `harmonic_kinematic_pinn`
- Test MAE: `0.0016458159079775214`
- Test RMSE: `0.002040258841589093`
- Validation MAE: `0.001852305606007576`
- Output Directory: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-03-44__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-03-44__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-03-44__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-03-44__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=018-val_mae=0.00185231.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
