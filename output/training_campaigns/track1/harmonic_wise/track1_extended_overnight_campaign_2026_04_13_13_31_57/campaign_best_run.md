# Campaign Best Run

## Overview

- Campaign Name: `track1_extended_overnight_campaign_2026_04_13_13_31_57`
- Run Name: `track1_hgbm_h01_wide_depth_2`
- Run Instance Id: `2026-04-13-15-11-49__track1_hgbm_h01_wide_depth_2_campaign_run`
- Block: `A`
- Block Description: `Wide low-order HGBM search`
- Test Mean Percentage Error: `8.706808%`
- Test Curve MAE: `0.002611 deg`
- Test Curve RMSE: `0.002810 deg`
- Validation Mean Percentage Error: `9.830052%`
- Oracle Test Mean Percentage Error: `2.749065%`
- Target A Threshold: `4.7%`
- Target A Status: `not_yet_met`
- Output Directory: `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-13-15-11-49__track1_hgbm_h01_wide_depth_2_campaign_run`
- Validation Summary Path: `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-13-15-11-49__track1_hgbm_h01_wide_depth_2_campaign_run/validation_summary.yaml`

## Selection Policy

- Eligibility Gate: `shared_offline_evaluator_only`
- Primary Metric: `test_mean_percentage_error_pct`
- First Tie Breaker: `test_curve_mae_deg`
- Second Tie Breaker: `test_curve_rmse_deg`
- Third Tie Breaker: `run_name`
- Direction: `minimize`
