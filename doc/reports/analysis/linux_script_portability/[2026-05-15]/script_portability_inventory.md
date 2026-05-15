# Repository Script Linux Portability Inventory

## Summary

- script count: `212`
- Python CLI-like scripts: `63`
- Python CLI-like scripts with platform flags: `13`
- PowerShell scripts: `98`
- PowerShell scripts missing Linux equivalents: `94`
- Bash scripts: `4`
- report-domain scripts: `28`
- report-domain scripts with platform flags: `3`
- inventory YAML: `doc/reports/analysis/linux_script_portability/[2026-05-15]/script_portability_inventory.yaml`

## Status Counts

| Status | Count |
| --- | ---: |
| `helper_no_cli` | 47 |
| `linux_equivalent_present` | 4 |
| `linux_launcher_present` | 4 |
| `missing_linux_equivalent` | 94 |
| `missing_platform_flags` | 50 |
| `needs_review` | 3 |
| `platform_flagged` | 10 |

## Script Inventory

| Script | Domain | Kind | Status | Platform Flags | Linux Equivalent | Note |
| --- | --- | --- | --- | --- | --- | --- |
| `scripts/__init__.py` | `__init__.py` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/campaigns/infrastructure/directional_training_variant_support.py` | `campaigns` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/infrastructure/run_remote_training_validation_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/infrastructure/run_targeted_remote_followup_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1` | `campaigns` | `launcher` | `linux_equivalent_present` | no | yes | PowerShell launcher has a sibling Bash launcher. |
| `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh` | `campaigns` | `launcher` | `linux_launcher_present` | no | yes | Bash launcher is available. |
| `scripts/campaigns/paper_reference/rcim_original/rcim_original_best_parameter_registry.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.ps1` | `campaigns` | `launcher` | `linux_equivalent_present` | no | yes | PowerShell launcher has a sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.sh` | `campaigns` | `launcher` | `linux_launcher_present` | no | yes | Bash launcher is available. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_literal_workflow_refresh_mega_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py` | `campaigns` | `python_entrypoint` | `needs_review` | yes | yes | Script contains Windows-specific markers. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_final_open_cells_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_last_four_open_cells_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_last_non_green_cells_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_last_three_open_cells_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_last_three_open_cells_overnight_mega_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_maxi_last_non_green_cells_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_open_cell_repair_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_original_dataset_remote_diagnostic_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/prepare_track1_forward_original_dataset_remote_micro_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1` | `campaigns` | `launcher` | `linux_equivalent_present` | no | yes | PowerShell launcher has a sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.sh` | `campaigns` | `launcher` | `linux_launcher_present` | no | yes | Bash launcher is available. |
| `scripts/campaigns/track1/exact_paper/run_exact_paper_faithful_reproduction_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_exact_paper_model_bank_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_literal_workflow_refresh_mega_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_smoke_validation.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1` | `campaigns` | `launcher` | `linux_equivalent_present` | no | yes | PowerShell launcher has a sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh` | `campaigns` | `launcher` | `linux_launcher_present` | yes | yes | Bash launcher is available. |
| `scripts/campaigns/track1/exact_paper/run_track1_dt_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_dt_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_dt_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_dt_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_ert_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_ert_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_ert_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_ert_remaining_yellow_cell_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_ert_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_et_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_et_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_et_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_et_remaining_yellow_cell_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_et_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_exact_paper_open_cell_repair_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_final_open_cells_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_last_four_open_cells_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_last_non_green_cells_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_last_three_open_cells_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_last_three_open_cells_overnight_mega_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_maxi_last_non_green_cells_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_open_cell_repair_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_original_dataset_remote_diagnostic_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_forward_original_dataset_remote_micro_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_full_matrix_family_reproduction_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_gbm_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_gbm_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_gbm_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_gbm_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_hgbm_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_hgbm_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_hgbm_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_hgbm_remaining_yellow_cell_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_hgbm_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_lgbm_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_lgbm_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_lgbm_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_lgbm_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_mlp_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_mlp_family_full_matrix_repair_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_mlp_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_mlp_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_mlp_remaining_yellow_cell_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_mlp_residual_cell_final_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_mlp_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_open_cell_full_matrix_closure_campaigns.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_open_cell_full_matrix_closure_campaigns_resume_after_mlp.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_remaining_family_cellwise_reference_campaigns.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_remaining_family_full_matrix_campaigns.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_remaining_family_residual_cellwise_closure_campaigns.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_remaining_yellow_cell_campaigns.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_rf_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_rf_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_rf_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_rf_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_svm_remaining_yellow_cell_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_xgbm_cellwise_reference_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_xgbm_full_matrix_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_xgbm_open_cell_full_matrix_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_xgbm_remaining_yellow_cell_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/run_track1_xgbm_residual_cellwise_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/sync_track1_interrupted_remaining_yellow_cell_campaign_artifacts.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/exact_paper/watch_track1_remaining_yellow_cell_campaign_progress.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/harmonic_wise/run_track1_extended_overnight_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/harmonic_wise/run_track1_overnight_gap_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/harmonic_wise/run_track1_second_iteration_harmonic_wise_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svm_exact_faithful_final_attempt_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svm_exact_faithful_final_attempt_campaign_remote.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svm_final_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svm_micro_closure_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svm_open_cell_repair_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_smoke_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_smoke_campaign_remote.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/wave1/prepare_wave1_directional_best_hyperparameter_search_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/wave1/prepare_wave1_directional_optuna_recovery_micro_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/wave1/prepare_wave1_directional_retraining_campaign.py` | `campaigns` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/campaigns/wave1/run_wave1_directional_best_hyperparameter_search_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/wave1/run_wave1_directional_optuna_recovery_micro_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/wave1/run_wave1_directional_retraining_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/wave1/run_wave1_residual_harmonic_family_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/campaigns/wave1/run_wave1_structured_baseline_recovery_campaign.ps1` | `campaigns` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/datasets/__init__.py` | `datasets` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/datasets/export_dataset_split.py` | `datasets` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/datasets/transmission_error_dataset.py` | `datasets` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/datasets/visualize_transmission_error.py` | `datasets` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/models/__init__.py` | `models` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/models/feedforward_network.py` | `models` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/models/harmonic_regression.py` | `models` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/models/model_factory.py` | `models` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/models/periodic_feature_network.py` | `models` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/models/residual_harmonic_network.py` | `models` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py` | `paper_reimplementation` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/harmonic_wise_support.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/run_harmonic_wise_comparison_pipeline.py` | `paper_reimplementation` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/generate_original_dataset_exact_smoke_configs.py` | `paper_reimplementation` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py` | `paper_reimplementation` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py` | `paper_reimplementation` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py` | `paper_reimplementation` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py` | `paper_reimplementation` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/statistics.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/workflow_runtime.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/__init__.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `paper_reimplementation` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py` | `paper_reimplementation` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/analysis/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/analysis/generate_model_report_diagrams.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/analysis/generate_training_results_master_summary.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/analysis/plot_wave1_best_model_te_curves.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/closeout/closeout_rcim_retuned_reference_archive.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/closeout/track1/closeout_track1_bidirectional_original_dataset_mega_campaign.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/closeout_track1_forward_paper_faithful_grid_search_campaign.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/closeout_track1_mlp_family_full_matrix_repair.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/closeout_track1_mlp_residual_cell_final_closure.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/closeout_track1_open_cell_full_matrix_closure.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/closeout_track1_residual_cellwise_closure.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/closeout/track1/track1_reference_archive_closeout_support.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/closeout/wave1/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/closeout/wave1/closeout_wave1_directional_retraining_campaign.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/pdf/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/pdf/generate_styled_report_pdf.py` | `reports` | `python_entrypoint` | `needs_review` | yes | yes | Script contains Windows-specific markers. |
| `scripts/reports/pdf/run_report_pipeline.py` | `reports` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/reports/pdf/validate_report_pdf.py` | `reports` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/reports/presentation/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/presentation/generate_markdown_presentation.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/presentation/run_presentation_pipeline.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/track1/__init__.py` | `reports` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/reports/track1/refresh_track1_benchmark_colored_markers.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/reports/track1/refresh_track1_family_reference_archives.py` | `reports` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/__init__.py` | `tooling` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/tooling/lan_ai/__init__.py` | `tooling` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/tooling/lan_ai/lan_ai_node_client.py` | `tooling` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/tooling/lan_ai/lan_ai_node_server.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/lan_ai/setup_lan_ai_node_cuda_path.ps1` | `tooling` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/tooling/linux_portability/build_script_portability_inventory.py` | `tooling` | `python_entrypoint` | `needs_review` | yes | yes | Script contains Windows-specific markers. |
| `scripts/tooling/markdown/__init__.py` | `tooling` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/tooling/markdown/markdown_style_check.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/markdown/run_markdownlint.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/repository_path_support.py` | `tooling` | `python_cli_like` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/tooling/session/__init__.py` | `tooling` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/tooling/session/isolated_mode.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/technical_documents/create_technical_document.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/video_guides/__init__.py` | `tooling` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/tooling/video_guides/analyze_video_guides.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/video_guides/extract_video_guide_knowledge.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/video_guides/generate_video_guide_reports.py` | `tooling` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/tooling/video_guides/run_remote_high_quality_video_rerun.ps1` | `tooling` | `launcher` | `missing_linux_equivalent` | no | no | PowerShell launcher has no sibling Bash launcher. |
| `scripts/training/__init__.py` | `training` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/training/build_remote_training_sync_manifest.py` | `training` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/training/build_track1_interrupted_remaining_yellow_cell_manual_sync_plan.py` | `training` | `python_entrypoint` | `missing_platform_flags` | no | yes | Python CLI entry point lacks --linux/--windows. |
| `scripts/training/optuna_hpo_support.py` | `training` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/training/run_optuna_neural_hpo_study.py` | `training` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/training/run_training_campaign.py` | `training` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/training/run_training_smoke_test.py` | `training` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/training/shared_training_infrastructure.py` | `training` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/training/train_feedforward_network.py` | `training` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/training/train_tree_regressor.py` | `training` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
| `scripts/training/transmission_error_datamodule.py` | `training` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/training/transmission_error_regression_module.py` | `training` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/training/tree_regression_support.py` | `training` | `python_helper` | `helper_no_cli` | no | yes | Python helper has no direct CLI surface. |
| `scripts/training/validate_training_setup.py` | `training` | `python_entrypoint` | `platform_flagged` | yes | yes | Python CLI entry point exposes platform flags. |
