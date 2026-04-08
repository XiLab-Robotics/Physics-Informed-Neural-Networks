# Training Results Master Summary

## Executive Snapshot

- Generated At: `2026-04-08T16:40:36`
- Program State: active
- Current Completed Wave: `Wave 1` structured-baseline familywise optimization pass
- Current Focus: `Wave 1` is now fully closed in campaign execution, reporting, and ranking; the next main focus is `Wave 2` planning and implementation, while the TwinCAT deployment-evaluation branch is deferred until after that wave is complete and reviewed
- Active Campaign Status: `completed`
- Active Campaign Name: `targeted_remote_followup_campaign_2026_04_04_11_21_09`
- Current Global Winner: `te_hist_gbr_tabular` | Family `tree` | Test MAE `0.002885`

## Main Takeaways

- Strongest current neural family: `residual_harmonic_mlp`
- Current plain MLP anchor: `te_feedforward_stride1_high_compute_long_remote`
- Active family-improvement branch count: `0`
- Implemented and benchmarked family count: `5`

## Current Project Status

### Implemented And Benchmarked Families

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree` | Current Global Winner | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002885 | 5 | `2026-04-04 13:03:55` |
| `residual_harmonic_mlp` | Strongest Neural Family | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 26,266 | `2026-04-04 12:18:37` |
| `feedforward` | Current Plain MLP Anchor | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` | 0.003264 | 109,953 | `2026-04-04 13:02:09` |
| `periodic_mlp` | Implemented Benchmark | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003317 | 27,265 | `2026-03-20 15:10:02` |
| `harmonic_regression` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 0.020782 | 150 | `2026-03-20 16:41:05` |

### Active Training Or Improvement Branches

- No campaign is currently in `prepared` or `running` state.
- The next active implementation branch should therefore be read from the live backlog focus and the next approved campaign plan.

### Roadmap And Planned Work

| Wave Or Track | Status |
| --- | --- |
| Wave 0. Shared Infrastructure | completed |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 1. Structured Static Baselines | planning report: completed; implementation: completed; smoke-tests: completed; validation checks: completed; campaign execution: completed; results report: completed |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 2. Temporal Models | next primary implementation wave |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 3. Hybrid Structured Models | pending |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 4. PINN Formulation And First PINN | pending |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 5. Cross-Wave Comparison And Best Solution | pending |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`

## Recent Campaign Changes

| Campaign | Generated At | Completed | Failed | Winner | Impact |
| --- | --- | ---: | ---: | --- | --- |
| `targeted_remote_followup_campaign_2026_04_04_11_21_09` | `2026-04-04 13:03:55` | 5 | 0 | `te_hist_gbr_remote_refined` | No family-best change |
| `remote_training_validation_campaign_2026_04_03_17_54_21` | `2026-04-03 22:30:26` | 4 | 1 | `te_hist_gbr_remote_deep` | No family-best change |
| `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` | `2026-03-26 20:19:32` | 15 | 0 | `te_residual_h12_deep_joint_wave1` | Updated residual_harmonic_mlp family best |
| `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42` | `2026-03-20 18:32:18` | 6 | 0 | `te_residual_h12_small_joint_recovery` | No family-best change |
| `wave1_structured_baseline_campaign_2026_03_17_21_01_47` | `2026-03-20 15:20:03` | 4 | 6 | `te_periodic_mlp_h04_standard` | Updated periodic_mlp family best |

## Ranking Policy

- Primary metric: `test_mae`
- First tie-breaker: `test_rmse`
- Second tie-breaker: `val_mae`
- Third tie-breaker: `trainable_parameter_count`
- Direction: `minimize`

## Best Result Per Family

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree` | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002719 | 0.002885 | 0.003607 | 5 | 0.62 MB | Unknown | Current Global Winner |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003024 | 0.003152 | 0.003640 | 26,266 | 0.32 MB | Medium | Strongest Neural Family |
| `feedforward` | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` | 0.003044 | 0.003264 | 0.003679 | 109,953 | 1.28 MB | Medium | Current Plain MLP Anchor |
| `periodic_mlp` | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003097 | 0.003317 | 0.003793 | 27,265 | 0.33 MB | Medium | Implemented Benchmark |
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 0.017004 | 0.020782 | 0.022405 | 150 | 0.01 MB | Low | Implemented Benchmark |

## Cross-Family Interpretation

- Current global reference winner: `te_hist_gbr_tabular` from family `tree`.
- Strongest current neural family: `residual_harmonic_mlp`.
- Current plain-MLP comparison anchor: `te_feedforward_stride1_high_compute_long_remote`.
- Predictive quality and deployment suitability must stay separate: the best leaderboard entry is not automatically the best TwinCAT/PLC candidate.
- Large tree artifacts should be treated cautiously even when tree-based accuracy remains strong, because model weight and memory footprint can dominate deployment feasibility.

## Family-By-Family Result Breakdowns

### feedforward

- Best run: `te_feedforward_stride1_high_compute_long_remote`
- Best test MAE: `0.003264`
- Completed tracked runs: `20`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` | 0.003264 | 0.003679 | 0.003044 | 109,953 | 30m 09s | 1.28 MB | High | Medium | `targeted_remote_followup_campaign_2026_04_04_11_21_09` |
| 2 | `te_feedforward_high_compute_remote` | `feedforward` | 0.003274 | 0.003873 | 0.003059 | 109,953 | 10m 24s | 1.28 MB | High | Low | `remote_training_validation_campaign_2026_04_03_17_54_21` |
| 3 | `te_feedforward_stride1_big_remote` | `feedforward` | 0.003278 | 0.003671 | 0.003019 | 109,953 | 29m 55s | 1.28 MB | High | Medium | `remote_training_validation_campaign_2026_04_03_17_54_21` |
| 4 | `te_feedforward_stride5_long_large_batch` | `feedforward` | 0.003301 | 0.003791 | 0.003109 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_feedforward_stride1_long_large_batch_big_model` | `feedforward` | 0.003308 | 0.003779 | 0.003090 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 6 | `te_feedforward_high_compute` | `feedforward` | 0.003319 | 0.003915 | 0.003198 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 7 | `te_feedforward_high_epoch` | `feedforward` | 0.003335 | 0.003767 | 0.003007 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_feedforward_stride1_long_large_batch` | `feedforward` | 0.003358 | 0.003769 | 0.003104 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_feedforward_best_training` | `feedforward` | 0.003409 | 0.003948 | 0.003039 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_feedforward_stride10_long_large_batch_big_model` | `feedforward` | 0.003413 | 0.004063 | 0.003040 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 11 | `te_feedforward_stride10_long_large_batch` | `feedforward` | 0.003433 | 0.004123 | 0.003066 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_feedforward_stride5_long_large_batch_big_model` | `feedforward` | 0.003472 | 0.004004 | 0.003104 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 13 | `te_feedforward_stride10_long` | `feedforward` | 0.003483 | 0.004050 | 0.003053 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_feedforward_baseline` | `feedforward` | 0.003504 | 0.003969 | 0.003148 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_feedforward_high_density` | `feedforward` | 0.003519 | 0.004046 | 0.003077 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_feedforward_trial` | `feedforward` | 0.003535 | 0.004211 | 0.003618 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_feedforward_high_compute_long_remote` | `feedforward` | 0.003542 | 0.004228 | 0.003058 | 109,953 | 13m 24s | 1.28 MB | High | Low | `targeted_remote_followup_campaign_2026_04_04_11_21_09` |
| 18 | `te_feedforward_stride5_long` | `feedforward` | 0.003580 | 0.004008 | 0.003178 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_feedforward_stride1_long` | `feedforward` | 0.003646 | 0.003990 | 0.003126 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 20 | `te_feedforward_trial` | `feedforward` | 0.003671 | 0.004418 | 0.003706 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |

### harmonic_regression

- Best run: `te_harmonic_order12_linear_conditioned_recovery`
- Best test MAE: `0.020782`
- Completed tracked runs: `3`
- Known failed campaign attempts: `3`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 0.020782 | 0.022405 | 0.017004 | 150 | 9m 45s | 0.01 MB | Very Low | Low | `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42` |
| 2 | `te_harmonic_order12_static_recovery` | `harmonic_regression` | 0.039404 | 0.042797 | 0.040524 | 25 | 10m 53s | 0.01 MB | Very Low | Low | `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42` |
| 3 | `te_harmonic_order06_static_recovery` | `harmonic_regression` | 0.039406 | 0.042796 | 0.040529 | 13 | 9m 05s | 0.01 MB | Very Low | Low | `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42` |

Known failed campaign attempts for this family:

- `te_harmonic_order06_static` | campaign `wave1_structured_baseline_campaign_2026_03_17_21_01_47` | model type `harmonic_regression` | error `'hidden_size'`
- `te_harmonic_order12_static` | campaign `wave1_structured_baseline_campaign_2026_03_17_21_01_47` | model type `harmonic_regression` | error `'hidden_size'`
- `te_harmonic_order12_linear_conditioned` | campaign `wave1_structured_baseline_campaign_2026_03_17_21_01_47` | model type `harmonic_regression` | error `'hidden_size'`

### periodic_mlp

- Best run: `te_periodic_mlp_h04_standard`
- Best test MAE: `0.003317`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003317 | 0.003793 | 0.003097 | 27,265 | 16m 22s | 0.33 MB | Medium | Medium | `wave1_structured_baseline_campaign_2026_03_17_21_01_47` |
| 2 | `te_periodic_mlp_h08_standard` | `periodic_mlp` | 0.003395 | 0.003951 | 0.003086 | 28,289 | 16m 46s | 0.35 MB | Medium | Medium | `wave1_structured_baseline_campaign_2026_03_17_21_01_47` |
| 3 | `te_periodic_mlp_h08_wide` | `periodic_mlp` | 0.003590 | 0.004143 | 0.003089 | 47,745 | 17m 22s | 0.57 MB | Medium | Medium | `wave1_structured_baseline_campaign_2026_03_17_21_01_47` |

### residual_harmonic_mlp

- Best run: `te_residual_h12_deep_joint_wave1`
- Best test MAE: `0.003152`
- Completed tracked runs: `19`
- Known failed campaign attempts: `2`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 0.003640 | 0.003024 | 26,266 | 28m 48s | 0.32 MB | Medium | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 2 | `te_residual_h12_small_joint_high_dropout_wave1` | `residual_harmonic_mlp` | 0.003230 | 0.003704 | 0.003001 | 4,890 | 21m 29s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 3 | `te_residual_h16_small_joint_wave1` | `residual_harmonic_mlp` | 0.003274 | 0.003747 | 0.003020 | 4,898 | 20m 09s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 4 | `te_residual_h12_wide_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | 0.003278 | 0.003814 | 0.002924 | 17,946 | 22m 45s | 0.22 MB | Medium | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 5 | `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | `residual_harmonic_mlp` | 0.003302 | 0.003909 | 0.002935 | 4,890 | 18m 07s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 6 | `te_residual_h12_small_joint_low_dropout_wave1` | `residual_harmonic_mlp` | 0.003359 | 0.003852 | 0.003027 | 4,890 | 21m 04s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 7 | `te_residual_h12_small_joint_no_layer_norm_wave1` | `residual_harmonic_mlp` | 0.003360 | 0.003835 | 0.003089 | 4,634 | 12m 49s | 0.07 MB | Low | Low | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 8 | `te_residual_h12_deep_dense_remote` | `residual_harmonic_mlp` | 0.003365 | 0.003868 | 0.003018 | 26,266 | 13m 28s | 0.32 MB | Medium | Low | `targeted_remote_followup_campaign_2026_04_04_11_21_09` |
| 9 | `te_residual_h12_small_frozen_wave1` | `residual_harmonic_mlp` | 0.003368 | 0.003898 | 0.003036 | 4,865 | 23m 21s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 10 | `te_residual_h12_wide_joint_wave1` | `residual_harmonic_mlp` | 0.003376 | 0.003906 | 0.002884 | 17,946 | 31m 23s | 0.22 MB | Medium | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 11 | `te_residual_h12_deep_long_remote` | `residual_harmonic_mlp` | 0.003384 | 0.003908 | 0.002973 | 26,266 | 15m 58s | 0.32 MB | Medium | Medium | `targeted_remote_followup_campaign_2026_04_04_11_21_09` |
| 12 | `te_residual_h08_small_frozen_wave1` | `residual_harmonic_mlp` | 0.003384 | 0.003912 | 0.003007 | 4,865 | 18m 38s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 13 | `te_residual_h08_small_joint_wave1` | `residual_harmonic_mlp` | 0.003385 | 0.003862 | 0.003030 | 4,882 | 11m 22s | 0.07 MB | Low | Low | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 14 | `te_residual_h12_medium_joint_wave1` | `residual_harmonic_mlp` | 0.003406 | 0.003863 | 0.002968 | 9,498 | 22m 14s | 0.13 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 15 | `te_residual_h12_small_joint_dense_wave1` | `residual_harmonic_mlp` | 0.003410 | 0.003790 | 0.002962 | 4,890 | 26m 57s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 16 | `te_residual_h12_small_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | 0.003465 | 0.003944 | 0.002987 | 4,890 | 27m 44s | 0.07 MB | Low | Medium | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |
| 17 | `te_residual_h12_small_joint_recovery` | `residual_harmonic_mlp` | 0.003466 | 0.003967 | 0.003016 | 4,890 | 16m 51s | 0.07 MB | Low | Medium | `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42` |
| 18 | `te_residual_h12_small_frozen_recovery` | `residual_harmonic_mlp` | 0.003554 | 0.004061 | 0.003030 | 4,865 | 17m 29s | 0.07 MB | Low | Medium | `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42` |
| 19 | `te_residual_h12_small_joint_anchor_wave1` | `residual_harmonic_mlp` | 0.003557 | 0.004064 | 0.003090 | 4,890 | 11m 20s | 0.07 MB | Low | Low | `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00` |

Known failed campaign attempts for this family:

- `te_residual_h12_small_frozen` | campaign `wave1_structured_baseline_campaign_2026_03_17_21_01_47` | model type `residual_harmonic_mlp` | error `'hidden_size'`
- `te_residual_h12_small_joint` | campaign `wave1_structured_baseline_campaign_2026_03_17_21_01_47` | model type `residual_harmonic_mlp` | error `'hidden_size'`

### tree

- Best run: `te_hist_gbr_tabular`
- Best test MAE: `0.002885`
- Completed tracked runs: `5`
- Known failed campaign attempts: `2`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | N/A | 0.62 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_remote_deep` | `hist_gradient_boosting` | 0.002920 | 0.003644 | 0.002749 | 5 | 1m 55s | 0.91 MB | Light Artifact | Very Low | `remote_training_validation_campaign_2026_04_03_17_54_21` |
| 3 | `te_hist_gbr_remote_refined` | `hist_gradient_boosting` | 0.003101 | 0.003781 | 0.002809 | 5 | 1m 46s | 0.84 MB | Light Artifact | Very Low | `targeted_remote_followup_campaign_2026_04_04_11_21_09` |
| 4 | `te_random_forest_tabular_recovery` | `random_forest` | 0.003833 | 0.004809 | 0.003792 | 5 | 1h 16m 53s | 7.09 GB | Extreme Artifact | High | `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42` |
| 5 | `te_random_forest_remote_medium` | `random_forest` | 0.003865 | 0.004861 | 0.003808 | 5 | N/A | 85.40 GB | Extreme Artifact | Unknown | `standalone_or_unknown` |

Known failed campaign attempts for this family:

- `te_random_forest_remote_aggressive` | campaign `remote_training_validation_campaign_2026_04_03_17_54_21` | model type `random_forest` | error `could not allocate 536870912 bytes`
- `te_random_forest_tabular` | campaign `wave1_structured_baseline_campaign_2026_03_17_21_01_47` | model type `random_forest` | error `could not allocate 134217728 bytes`

## Source Of Truth

- Live backlog: `doc/running/te_model_live_backlog.md`
- Active campaign state: `doc/running/active_training_campaign.yaml`
- Program registry: `output/registries/program/current_best_solution.yaml`
- Family registries root: `output/registries/families`
- Training campaign root: `output/training_campaigns`
- Training run root: `output/training_runs`

This document is repository-generated. Regenerate it after new campaign results so the cross-family snapshot stays aligned with the canonical registries and campaign artifacts.
