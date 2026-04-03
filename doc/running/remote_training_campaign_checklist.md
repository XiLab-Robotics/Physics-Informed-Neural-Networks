# Remote Training Campaign Checklist

- Run status: completed with manual sync recovery
- Stage: completed
- Remote host alias: xilab-remote
- Remote repository path: C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks
- Remote Conda environment: standard_ml_lan_node
- Campaign name: remote_training_validation_campaign_2026_04_03_17_54_21
- Planning report path: doc\reports\campaign_plans\2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md
- Local log path: C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\.temp\remote_training_campaigns\2026-04-03-20-37-59_remote_training_validation_campaign_2026_04_03_17_54_21\remote_training_campaign.log
- Remote campaign output directory: output\training_campaigns\2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21
- Remote manifest path: output\training_campaigns\2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21\campaign_manifest.yaml
- Updated at: 2026-04-03 22:35:07

## Campaign Config Paths

- config\training\remote_validation\campaigns\2026-04-03_remote_training_validation_campaign\01_random_forest_remote_medium.yaml
- config\training\remote_validation\campaigns\2026-04-03_remote_training_validation_campaign\02_random_forest_remote_aggressive.yaml
- config\training\remote_validation\campaigns\2026-04-03_remote_training_validation_campaign\03_hist_gbr_remote_deep.yaml
- config\training\remote_validation\campaigns\2026-04-03_remote_training_validation_campaign\04_feedforward_high_compute_remote.yaml
- config\training\remote_validation\campaigns\2026-04-03_remote_training_validation_campaign\05_feedforward_stride1_big_remote.yaml

## Source Sync Paths

- scripts
- config
- requirements.txt

## Synced Artifact Paths

- output\training_campaigns\2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21
- config\training\queue\completed\2026-04-03-20-38-07_001_01_random_forest_remote_medium.yaml
- output\training_runs\tree\2026-04-03-20-38-08__te_random_forest_remote_medium
- output\training_runs\tree\2026-04-03-21-17-21__te_random_forest_remote_aggressive
- config\training\queue\failed\2026-04-03-20-38-07_002_02_random_forest_remote_aggressive.yaml
- output\training_runs\tree\2026-04-03-21-48-11__te_hist_gbr_remote_deep
- config\training\queue\completed\2026-04-03-20-38-07_003_03_hist_gbr_remote_deep.yaml
- output\training_runs\feedforward\2026-04-03-21-50-07__te_feedforward_high_compute_remote
- config\training\queue\completed\2026-04-03-20-38-07_004_04_feedforward_high_compute_remote.yaml
- output\training_runs\feedforward\2026-04-03-22-00-31__te_feedforward_stride1_big_remote
- config\training\queue\completed\2026-04-03-20-38-07_005_05_feedforward_stride1_big_remote.yaml
- output\registries\families\feedforward\leaderboard.yaml
- output\registries\families\feedforward\latest_family_best.yaml
- output\registries\families\tree\leaderboard.yaml
- output\registries\families\tree\latest_family_best.yaml
- output\registries\program\current_best_solution.yaml

## Recovery Notes

The remote run completed successfully, but the local launcher needed manual
sync recovery because the first real validation exposed PowerShell 5
binary-stream and `CLIXML` progress issues.

The campaign manifest also serialized the medium random-forest
`run_instance_id` one second early. The real completed artifact directory was:

- `output\training_runs\tree\2026-04-03-20-38-08__te_random_forest_remote_medium`
