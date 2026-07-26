# Campaign Best Run

## Overview

- Campaign Name: `phase3_c1_fw_stability_repeat_2026_07_26`
- Run Name: `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints`
- Run Instance Id: `2026-07-26-19-52-45__te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints`
- Model Family: `phase3_pinn_c1_linear_compliance_soft_fw_seed_314159`
- Model Type: `quasi_static_compliance_pinn`
- Test MAE: `0.0014724736101925373`
- Test RMSE: `0.0018639324698597193`
- Validation MAE: `0.0016763968160375953`
- Output Directory: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-19-52-45__te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints`
- Metrics Snapshot: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-19-52-45__te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-19-52-45__te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-19-52-45__te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=019-val_mae=0.00167640.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
