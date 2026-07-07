# Campaign Best Run

## Best Entry

- Run: `te_tree_global__polished_actual_values`
- Run Instance ID: `2026-07-07-09-52-50__te_tree_global__polished_actual_values`
- Model Family: `tree_global`
- Dataset: `polished_dataset`
- Dataset Schema: `polished_point_v1`
- Input Mode: `actual_values`
- Input Feature Dim: `5`
- Test MAE: `0.001749789662`
- Test RMSE: `0.002892060915`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
