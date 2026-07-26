# Campaign Best Run

## Overview

- Campaign Name: `phase3_quasi_static_compliance_pinn_2026_07_26`
- Run Name: `te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints`
- Run Instance Id: `2026-07-26-18-14-00__te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints`
- Model Family: `phase3_pinn_c1_linear_compliance_soft_fw`
- Model Type: `quasi_static_compliance_pinn`
- Test MAE: `0.0014947345480322838`
- Test RMSE: `0.0018873440567404032`
- Validation MAE: `0.00170182716101408`
- Output Directory: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-14-00__te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-14-00__te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-14-00__te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-14-00__te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=017-val_mae=0.00170183.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
