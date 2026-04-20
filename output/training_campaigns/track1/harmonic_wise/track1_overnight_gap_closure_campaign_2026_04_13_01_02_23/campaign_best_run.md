# Campaign Best Run

## Overview

- Campaign Name: `track1_overnight_gap_closure_campaign_2026_04_13_01_02_23`
- Run Name: `track1_hgbm_h01_shallow_regularized`
- Run Instance Id:
  `2026-04-13-01-45-32__track1_hgbm_h01_shallow_regularized_campaign_run`
- Track Kind: `shared_offline_evaluator`
- Eligibility: `eligible_for_campaign_winner`
- Test Mean Percentage Error: `8.773671010022024`
- Test Curve MAE [deg]: `0.002578214884212948`
- Test Curve RMSE [deg]: `0.002775679702931834`
- Oracle Test Mean Percentage Error: `2.7490651472987206`
- Target A Threshold [%]: `4.7`
- Target A Status: `not_yet_met`
- Output Directory:
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-13-01-45-32__track1_hgbm_h01_shallow_regularized_campaign_run`
- Validation Summary Path:
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-13-01-45-32__track1_hgbm_h01_shallow_regularized_campaign_run/validation_summary.yaml`

## Selection Policy

- Eligibility Gate: `shared_offline_evaluator_only`
- Primary Metric: `test_mean_percentage_error_pct`
- First Tie Breaker: `test_curve_mae_deg`
- Second Tie Breaker: `test_curve_rmse_deg`
- Third Tie Breaker: `run_name`
