# Remote Training Campaign Checklist

- Run status: completed
- Stage: completed_with_manual_sync_recovery
- Remote host alias: xilab-remote
- Remote repository path: C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks
- Remote Conda environment: pinns_env
- Campaign name: parallel_shape_objective_followup_2026_07_21
- Planning report path: doc/reports/campaign_plans/cross_wave/shape_objective/2026-07-21-18-36-30_parallel_shape_objective_followup_campaign_plan_report.md
- Local log path: C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\.temp\remote_training_campaigns\2026-07-21-18-51-06_parallel_shape_objective_followup_2026_07_21\remote_training_campaign.log
- Remote campaign output directory: output/training_campaigns/2026-07-21-18-52-44_parallel_shape_objective_followup_2026_07_21
- Remote manifest path: output/training_campaigns/2026-07-21-18-52-44_parallel_shape_objective_followup_2026_07_21/campaign_manifest.yaml
- Updated at: 2026-07-21 19:29:30

## Campaign Config Paths

- config/training/shape_objective_followup/campaigns/2026-07-21_parallel_shape_objective_followup/queue/001_shape_objective_v3_periodic_gru_sequence_fw.yaml
- config/training/shape_objective_followup/campaigns/2026-07-21_parallel_shape_objective_followup/queue/002_shape_objective_periodic_mlp_harmonic_fw.yaml
- config/training/shape_objective_followup/campaigns/2026-07-21_parallel_shape_objective_followup/queue/003_shape_objective_curve_aware_residual_fw.yaml

## Source Sync Paths

- scripts
- config
- doc
- site
- requirements.txt
- AGENTS.md

## Synced Artifact Paths

- output/training_campaigns/2026-07-21-18-52-44_parallel_shape_objective_followup_2026_07_21
- output/training_runs/shape_objective_followup/2026-07-21-18-52-44__te_shape_objective_v3_periodic_gru_sequence_fw__polished_setpoints
- output/training_runs/shape_objective_followup/2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints
- output/training_runs/shape_objective_followup/2026-07-21-19-12-09__te_shape_objective_curve_aware_residual_fw__polished_setpoints
- config/training/queue/shape_objective_followup/parallel_shape_objective_followup_2026_07_21
- output/registries/families/shape_objective_v3_periodic_gru_sequence_fw
- output/registries/families/shape_objective_periodic_mlp_harmonic_fw
- output/registries/families/shape_objective_curve_aware_residual_fw
- output/registries/program/current_best_solution.yaml

## Manual Sync Recovery

Remote training completed successfully, but the local SSH wrapper became stale
after remote completion. The stale SSH process was stopped after confirming the
remote Python campaign process had exited and the completed remote artifacts
existed. The artifact set above was synchronized manually from the remote
campaign output, run directories, queue end state, family registries, and
program best registry.
