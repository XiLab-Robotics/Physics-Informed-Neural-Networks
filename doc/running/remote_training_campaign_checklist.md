# Remote Training Campaign Checklist

- Run status: closed
- Stage: closeout reported
- Remote host alias: xilab-remote
- Remote repository path: C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks
- Remote Conda environment: pinns_env
- Campaign name: causal_offset_mean_calibration_pilot_2026_07_22
- Planning report path: doc/reports/campaign_plans/cross_wave/causal_offset_mean_calibration/2026-07-22-17-42-11_causal_offset_mean_calibration_pilot_plan_report.md
- Remote campaign output directory: output\training_campaigns\2026-07-22-18-09-27_causal_offset_mean_calibration_pilot_2026_07_22
- Remote manifest path: output\training_campaigns\2026-07-22-18-09-27_causal_offset_mean_calibration_pilot_2026_07_22\campaign_manifest.yaml
- Campaign results report path: doc/reports/campaign_results/cross_wave/causal_offset_mean_calibration/2026-07-22-18-33-02_causal_offset_mean_calibration_pilot_campaign_results_report.md
- Campaign results PDF path: doc/reports/campaign_results/cross_wave/causal_offset_mean_calibration/2026-07-22-18-33-02_causal_offset_mean_calibration_pilot_campaign_results_report.pdf
- Updated at: 2026-07-22 18:36:21

## Campaign Config Paths

- config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/queue/001_causal_offset_mean_gru_sequence_fw.yaml
- config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/queue/002_causal_offset_mean_periodic_mlp_harmonic_fw.yaml

## Synced Artifact Paths

- output\training_campaigns\2026-07-22-18-09-27_causal_offset_mean_calibration_pilot_2026_07_22
- output\training_runs\causal_offset_mean_calibration\2026-07-22-18-09-27__te_causal_offset_mean_gru_sequence_fw__polished_setpoints
- output\training_runs\causal_offset_mean_calibration\2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints
- config\training\queue\causal_offset_mean_calibration\causal_offset_mean_calibration_pilot_2026_07_22\completed\2026-07-22-18-09-27_001_001_causal_offset_mean_gru_sequence_fw.yaml
- config\training\queue\causal_offset_mean_calibration\causal_offset_mean_calibration_pilot_2026_07_22\completed\2026-07-22-18-09-27_002_002_causal_offset_mean_periodic_mlp_harmonic_fw.yaml
- output\registries\program\current_best_solution.yaml

## Recovery Note

The shared remote launcher exited during remote preflight and direct
`conda run` returned `-1073740791` after the campaign had already written a
complete `Completed 2 | Failed 0` output package. Artifacts were synchronized
manually from the remote sync manifest. The manifest referenced a missing
aggregate family registry under
`output/registries/families/causal_offset_mean_calibration/leaderboard.yaml`,
so the campaign leaderboard is the canonical ranking surface for this run.
