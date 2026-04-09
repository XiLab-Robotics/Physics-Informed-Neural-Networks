# Campaign Best Run

## Overview

- Campaign Name: `track1_second_iteration_harmonic_wise_campaign_2026_04_09_18_56_03`
- Run Name: `te_harmonic_wise_full_rcim_no_engineering_reference`
- Run Instance Id:
  `2026-04-09-20-45-48__te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run`
- Model Family: `paper_reimplementation_rcim_harmonic_wise`
- Model Type: `harmonic_wise_hist_gradient_boosting`
- Selected Harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- Feature Set: `base_only`
- Validation Mean Percentage Error: `9.229%`
- Test Mean Percentage Error: `8.877%`
- Oracle Test Mean Percentage Error: `2.749%`
- Test MAE: `0.002613 deg`
- Test RMSE: `0.002812 deg`
- Output Directory:
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-09-20-45-48__te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run`
- Metrics Snapshot:
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-09-20-45-48__te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run/validation_summary.yaml`
- Report Path:
  `doc/reports/analysis/validation_checks/2026-04-09-20-46-45_paper_reimplementation_rcim_harmonic_wise_te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run_harmonic_wise_comparison_report.md`
- Best Checkpoint Path:
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-09-20-45-48__te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run/harmonic_model_bundle.pkl`

## Selection Policy

- Primary Metric: `test_curve_mean_percentage_error_pct`
- First Tie Breaker: `test_curve_rmse_deg`
- Second Tie Breaker: `validation_curve_mean_percentage_error_pct`
- Third Tie Breaker: `harmonic_target_mae`
