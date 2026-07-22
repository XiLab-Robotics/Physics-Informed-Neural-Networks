# Remote Training Campaign Checklist

- Run status: completed
- Stage: completed_with_manual_recovery
- Remote host alias: xilab-remote
- Remote repository path: C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks
- Remote Conda environment: pinns_env
- Campaign name: shape_first_training_rule_distillation_pilot_2026_07_22
- Planning report path: doc/reports/campaign_plans/cross_wave/shape_first_training_rule_distillation/2026-07-22-13-14-28_shape_first_training_rule_distillation_pilot_campaign_plan_report.md
- Local log path: C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\.temp\remote_training_campaigns\2026-07-22-14-35-47_shape_first_training_rule_distillation_pilot_2026_07_22\remote_training_campaign.log
- Remote campaign output directory: output/training_campaigns/2026-07-22-14-38-51_shape_first_training_rule_distillation_pilot_2026_07_22
- Remote manifest path: output/training_campaigns/2026-07-22-14-38-51_shape_first_training_rule_distillation_pilot_2026_07_22/campaign_manifest.yaml
- Updated at: 2026-07-22 15:20:49

## Campaign Config Paths

- config/training/shape_first_training_rule_distillation/campaigns/2026-07-22_shape_first_training_rule_distillation_pilot/queue/001_shape_first_distilled_periodic_gru_sequence_fw.yaml
- config/training/shape_first_training_rule_distillation/campaigns/2026-07-22_shape_first_training_rule_distillation_pilot/queue/002_shape_first_distilled_periodic_mlp_harmonic_fw.yaml

## Source Sync Paths

- scripts
- config
- doc
- site
- requirements.txt
- AGENTS.md

## Synced Output Paths

- output/training_campaigns/2026-07-22-14-38-51_shape_first_training_rule_distillation_pilot_2026_07_22
- output/training_runs/shape_first_training_rule_distillation/2026-07-22-14-38-51__te_shape_first_distilled_periodic_gru_sequence_fw__polished_setpoints
- output/training_runs/shape_first_training_rule_distillation/2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints
- config/training/queue/shape_first_training_rule_distillation/shape_first_training_rule_distillation_pilot_2026_07_22/completed
- output/registries/families/shape_first_distilled_periodic_gru_sequence_fw
- output/registries/families/shape_first_distilled_periodic_mlp_harmonic_fw
- output/registries/program/current_best_solution.yaml

## Recovery Note

Remote training completed successfully, but the local SSH wrapper stayed active
because the previous stream reader used blocking `Peek()` polling. The hung
local `ssh.exe` and wrapper `cmd.exe` processes were stopped after remote
completion was verified and artifacts were recovered. The shared remote runner
now uses asynchronous stdout/stderr handlers.
