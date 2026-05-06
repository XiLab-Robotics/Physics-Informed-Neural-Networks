# wave1_directional_retraining_campaign_2026_05_06_16_07_16

## Overview

This campaign package retrains the current Wave 1 family-best baselines
under three explicit data scopes: `global`, `Fw`, and `Bw`.

## Candidate Count

- base families: `5`
- variants per family: `3`
- total configs: `15`

## Generated Queue Configs

- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/01_tree_global.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/02_tree_fw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/03_tree_bw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/04_residual_harmonic_mlp_global.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/05_residual_harmonic_mlp_fw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/06_residual_harmonic_mlp_bw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/07_feedforward_global.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/08_feedforward_fw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/09_feedforward_bw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/10_periodic_mlp_global.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/11_periodic_mlp_fw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/12_periodic_mlp_bw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/13_harmonic_regression_global.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/14_harmonic_regression_fw.yaml`
- `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/15_harmonic_regression_bw.yaml`

## Notes

- the active Track 1 campaign state was intentionally left untouched;
- launcher execution still requires explicit user approval of the campaign plan;
- directional identity is written into both config metadata and registry-facing family keys.
