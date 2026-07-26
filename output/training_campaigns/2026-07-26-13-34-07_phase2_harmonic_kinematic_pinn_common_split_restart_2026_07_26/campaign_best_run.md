# Campaign Best Run

## Overview

- Campaign Name: `phase2_harmonic_kinematic_pinn_common_split_restart_2026_07_26`
- Run Name: `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Run Instance Id: `2026-07-26-13-34-07__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Model Family: `phase2_pinn_h0_fourier_control_fw`
- Model Type: `harmonic_kinematic_pinn`
- Test MAE: `0.0013538131024688482`
- Test RMSE: `0.0016197613440454006`
- Validation MAE: `0.001417710678651929`
- Output Directory: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-13-34-07__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-13-34-07__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-13-34-07__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\harmonic_kinematic_pinn\2026-07-26-13-34-07__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=034-val_mae=0.00141771.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
