# Training Results Master Summary

## Executive Snapshot

- Generated At: `2026-05-07T13:29:13`
- Program State: active
- Current Completed Wave: `Wave 1` structured-baseline familywise optimization pass
- Current Focus: the immediate implementation branch is now the offline
- Active Campaign Status: `running`
- Active Campaign Name: `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30`
- Current Global Winner: `te_hist_gbr_tabular_Fw` | Family `tree_fw` | Test MAE `0.002845`

## Main Takeaways

- Strongest current neural family: `feedforward`
- Current plain MLP anchor: `te_feedforward_stride1_high_compute_long_remote_global`
- Active family-improvement branch count: `0`
- Implemented and benchmarked family count: `15`

## Current Project Status

### Implemented And Benchmarked Families

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree_fw` | Current Global Winner | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002845 | 5 | `2026-05-07 13:24:57` |
| `tree` | Implemented Benchmark | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002885 | 5 | `2026-05-07 13:24:57` |
| `tree_bw` | Implemented Benchmark | `te_hist_gbr_tabular_Bw` | `hist_gradient_boosting` | 0.003087 | 5 | `2026-05-07 13:24:57` |
| `harmonic_regression_fw` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery_Fw` | `harmonic_regression` | 0.003129 | 150 | `2026-05-07 13:24:58` |
| `feedforward` | Strongest Neural Family | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 109,953 | `2026-05-07 13:24:58` |
| `residual_harmonic_mlp` | Implemented Benchmark | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 26,266 | `2026-05-07 13:24:58` |
| `feedforward_bw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Bw` | `feedforward` | 0.003262 | 109,953 | `2026-05-07 13:24:58` |
| `periodic_mlp` | Implemented Benchmark | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003317 | 27,265 | `2026-05-07 13:24:58` |
| `periodic_mlp_fw` | Implemented Benchmark | `te_periodic_mlp_h04_standard_Fw` | `periodic_mlp` | 0.003432 | 27,265 | `2026-05-07 13:24:58` |
| `residual_harmonic_mlp_bw` | Implemented Benchmark | `te_residual_h12_deep_joint_wave1_Bw` | `residual_harmonic_mlp` | 0.003493 | 26,266 | `2026-05-07 13:24:58` |
| `harmonic_regression_bw` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery_Bw` | `harmonic_regression` | 0.003524 | 150 | `2026-05-07 13:24:58` |
| `periodic_mlp_bw` | Implemented Benchmark | `te_periodic_mlp_h04_standard_Bw` | `periodic_mlp` | 0.003525 | 27,265 | `2026-05-07 13:24:58` |
| `residual_harmonic_mlp_fw` | Implemented Benchmark | `te_residual_h12_deep_joint_wave1_Fw` | `residual_harmonic_mlp` | 0.003530 | 26,266 | `2026-05-07 13:24:58` |
| `feedforward_fw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Fw` | `feedforward` | 0.003563 | 109,953 | `2026-05-07 13:24:58` |
| `harmonic_regression` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.020779 | 150 | `2026-05-07 13:24:58` |

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
| Wave 2. Temporal Models | planned after the harmonic-wise intermediate branch; temporal-model scope will start only after the harmonic-wise comparison |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Intermediate Branch. Harmonic-Wise Comparison Pipeline | current primary implementation branch; focused scope:; implement harmonic-wise prediction of `A_k` and `phi_k`; implement TE reconstruction from the predicted harmonic terms; add offline `Robot` and `Cycloidal` motion-profile playback; define comparable offline validation scenarios and TE-curve error metrics; close `Target A`; initial repository-owned offline pipeline script should live under; validation artifacts for this branch should live under |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 3. Hybrid Structured Models | pending; paper-reproduction scope:; compare hybrid structured predictors against the paper-style harmonic stack; prepare the repository-owned deployable predictor package |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 4. PINN Formulation And First PINN | pending; paper-reproduction scope:; implement the repository-side compensation-loop evaluation path in the; implement uncompensated vs compensated `TE RMS` / `TE max` measurements; prepare the final online benchmark harness |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 5. Cross-Wave Comparison And Best Solution | pending; paper-reproduction scope:; execute Table 9 style online compensation tests; evaluate `Target B`; finalize the real `paper vs repository` comparison with online results |

Low-priority exploratory families currently listed in the backlog:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`

## Recent Campaign Changes

| Campaign | Generated At | Completed | Failed | Winner | Impact |
| --- | --- | ---: | ---: | --- | --- |
| `wave1_directional_retraining_campaign_2026_05_06_16_07_16` | `2026-05-06 23:14:10` | 15 | 0 | `te_hist_gbr_tabular_Fw` | Updated global best |

## Ranking Policy

- Primary metric: `test_mae`
- First tie-breaker: `test_rmse`
- Second tie-breaker: `val_mae`
- Third tie-breaker: `trainable_parameter_count`
- Direction: `minimize`

## Best Result Per Family

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree_fw` | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002666 | 0.002845 | 0.003476 | 5 | 0.50 MB | Very Low | Current Global Winner |
| `tree` | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002719 | 0.002885 | 0.003607 | 5 | 0.62 MB | Unknown | Implemented Benchmark |
| `tree_bw` | `te_hist_gbr_tabular_Bw` | `hist_gradient_boosting` | 0.002698 | 0.003087 | 0.003850 | 5 | 0.50 MB | Very Low | Implemented Benchmark |
| `harmonic_regression_fw` | `te_harmonic_order12_linear_conditioned_recovery_Fw` | `harmonic_regression` | 0.002811 | 0.003129 | 0.003567 | 150 | 0.01 MB | Low | Implemented Benchmark |
| `feedforward` | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003056 | 0.003150 | 0.003603 | 109,953 | 1.28 MB | Very High | Strongest Neural Family |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003024 | 0.003152 | 0.003640 | 26,266 | 0.32 MB | Unknown | Implemented Benchmark |
| `feedforward_bw` | `te_feedforward_stride1_high_compute_long_remote_Bw` | `feedforward` | 0.003049 | 0.003262 | 0.003749 | 109,953 | 1.28 MB | High | Implemented Benchmark |
| `periodic_mlp` | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003097 | 0.003317 | 0.003793 | 27,265 | 0.33 MB | Unknown | Implemented Benchmark |
| `periodic_mlp_fw` | `te_periodic_mlp_h04_standard_Fw` | `periodic_mlp` | 0.002848 | 0.003432 | 0.004023 | 27,265 | 0.33 MB | Low | Implemented Benchmark |
| `residual_harmonic_mlp_bw` | `te_residual_h12_deep_joint_wave1_Bw` | `residual_harmonic_mlp` | 0.003110 | 0.003493 | 0.004108 | 26,266 | 0.32 MB | Medium | Implemented Benchmark |
| `harmonic_regression_bw` | `te_harmonic_order12_linear_conditioned_recovery_Bw` | `harmonic_regression` | 0.003701 | 0.003524 | 0.004080 | 150 | 0.01 MB | Low | Implemented Benchmark |
| `periodic_mlp_bw` | `te_periodic_mlp_h04_standard_Bw` | `periodic_mlp` | 0.003154 | 0.003525 | 0.004132 | 27,265 | 0.33 MB | Medium | Implemented Benchmark |
| `residual_harmonic_mlp_fw` | `te_residual_h12_deep_joint_wave1_Fw` | `residual_harmonic_mlp` | 0.002852 | 0.003530 | 0.004145 | 26,266 | 0.32 MB | Low | Implemented Benchmark |
| `feedforward_fw` | `te_feedforward_stride1_high_compute_long_remote_Fw` | `feedforward` | 0.002915 | 0.003563 | 0.004009 | 109,953 | 1.28 MB | Medium | Implemented Benchmark |
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.017017 | 0.020779 | 0.022403 | 150 | 0.01 MB | Low | Implemented Benchmark |

## Cross-Family Interpretation

- Current global reference winner: `te_hist_gbr_tabular_Fw` from family `tree_fw`.
- Strongest current neural family: `feedforward`.
- Current plain-MLP comparison anchor: `te_feedforward_stride1_high_compute_long_remote_global`.
- Predictive quality and deployment suitability must stay separate: the best leaderboard entry is not automatically the best TwinCAT/PLC candidate.
- Large tree artifacts should be treated cautiously even when tree-based accuracy remains strong, because model weight and memory footprint can dominate deployment feasibility.

## Paper Reference Benchmark

The repository benchmark paper is `reference/RCIM_ML-compensation.pdf`.
At the current repository state, the comparison is explicitly `offline-only`. A real paper-equivalent comparison still requires repository-owned online compensation tests.

### Extracted Paper Targets

- Paper dataset size: `1026` operating-condition samples.
- Paper input axes: `input speed`, `applied torque`, `oil temperature`.
- Offline prediction target: TE-curve mean percentage error at or below `4.7%` on unseen validation scenarios.
- Online `robot` compensation target: at least `83.6%` TE RMS reduction.
- Online `cycloidal` compensation target: at least `94.0%` TE RMS reduction and `91.7%` TE max reduction.
- Paper compensation harmonics baseline: `0, 1, 39` with additional checks on `40, 78`.

### Paper Vs Repository

| Comparison Item | Paper Reference | Repository Status | Current Verdict |
| --- | --- | --- | --- |
| Offline model-selection direction | Boosting/tree-heavy deployed harmonic predictors | Current winner `te_hist_gbr_tabular_Fw` from family `tree_fw` with model type `hist_gradient_boosting` | not_aligned |
| Strongest neural branch role | Neural models are evaluated, but not the primary deployed winners | Strongest repository neural family is `feedforward` and still trails the tree winner | aligned |
| Track 1 canonical closure rule | Paper Tables `3-6` replicated per target and per harmonic | Exact-paper report currently shows `0/1` harmonics fully closed, `0/1` partially closed, `1/1` still open | not_yet_met |
| Supporting harmonic-wise TE metric | Mean percentage error over full TE curves | Latest harmonic-wise validation reports `11.212%` mean percentage error on held-out curves using harmonics `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | supporting_only_not_yet_met |
| Online robot-profile compensation | TE RMS reduction `83.6%` | No repository-owned online compensation result yet | not_yet_comparable |
| Online cycloidal-profile compensation | TE RMS reduction `94.0%`, TE max reduction `91.7%` | No repository-owned online compensation result yet | not_yet_comparable |
| Table 9-style end-to-end benchmark | PLC-integrated motion-profile compensation benchmark | Missing in the repository at the current state | not_yet_comparable |

### Track 1 Canonical Status

- Latest exact-paper validation summary: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/svm_targeted_closure/svm/2026-04-24-05-06-01__track1_svm_amplitude_240_yellow_cell_attempt_19_campaign_run/validation_summary.yaml`
- Table `3` amplitude `RMSE`: `0/1` harmonics at or below the paper target
- Table `4` phase `MAE`: `0/0` harmonics at or below the paper target
- Table `5` phase `RMSE`: `0/0` harmonics at or below the paper target
- Target-level expected-family direction: `0/1`
- Harmonic-level Table `6` closure: `0/1` fully matched, `0/1` partially matched, `1/1` still open
- Highest-priority open harmonics: `240`

### Latest Harmonic-Wise Validation Support

- Latest harmonic-wise validation summary: `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/family_exploration/rf/2026-04-13-16-00-30__track1_rf_h039_h162240_bridge_control_campaign_run/validation_summary.yaml`
- Harmonic-wise test mean percentage error: `11.212%`
- `Target A` status from the latest harmonic-wise run: `not_yet_met`

### Online Compensation Tracking Placeholder

- Repository online compensation status: `not yet available`.
- When online compensation tests are implemented, update this master summary with TE RMS, TE max, and reduction percentages for both robot and cycloidal motion profiles.
- Until those tests exist, present the paper comparison as `offline-only` rather than end-to-end equivalent.

### Gap Summary

- `Track 1` remains open primarily because the canonical Tables `3-6` are not yet fully matched.
- Offline benchmark scope remains `partially comparable` rather than like-for-like.
- Not yet aligned: the current repository winner is not tree-based, while the paper deployment path is dominated by boosting/tree models.
- Neural models remain secondary in the repository (`feedforward`), which is also consistent with the paper not promoting a plain neural winner for deployment.
- End-to-end paper comparison remains `not yet comparable` until repository-owned online compensation tests exist.

## Family-By-Family Result Breakdowns

### feedforward

- Best run: `te_feedforward_stride1_high_compute_long_remote_global`
- Best test MAE: `0.003150`
- Completed tracked runs: `21`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 0.003603 | 0.003056 | 109,953 | 2h 27m 05s | 1.28 MB | High | Very High | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 2 | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` | 0.003264 | 0.003679 | 0.003044 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_high_compute_remote` | `feedforward` | 0.003274 | 0.003873 | 0.003059 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 4 | `te_feedforward_stride1_big_remote` | `feedforward` | 0.003278 | 0.003671 | 0.003019 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 5 | `te_feedforward_stride5_long_large_batch` | `feedforward` | 0.003301 | 0.003791 | 0.003109 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_feedforward_stride1_long_large_batch_big_model` | `feedforward` | 0.003308 | 0.003779 | 0.003090 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 7 | `te_feedforward_high_compute` | `feedforward` | 0.003319 | 0.003915 | 0.003198 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 8 | `te_feedforward_high_epoch` | `feedforward` | 0.003335 | 0.003767 | 0.003007 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_feedforward_stride1_long_large_batch` | `feedforward` | 0.003358 | 0.003769 | 0.003104 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_feedforward_best_training` | `feedforward` | 0.003409 | 0.003948 | 0.003039 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_feedforward_stride10_long_large_batch_big_model` | `feedforward` | 0.003413 | 0.004063 | 0.003040 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 12 | `te_feedforward_stride10_long_large_batch` | `feedforward` | 0.003433 | 0.004123 | 0.003066 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 13 | `te_feedforward_stride5_long_large_batch_big_model` | `feedforward` | 0.003472 | 0.004004 | 0.003104 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 14 | `te_feedforward_stride10_long` | `feedforward` | 0.003483 | 0.004050 | 0.003053 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_feedforward_baseline` | `feedforward` | 0.003504 | 0.003969 | 0.003148 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_feedforward_high_density` | `feedforward` | 0.003519 | 0.004046 | 0.003077 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_feedforward_trial` | `feedforward` | 0.003535 | 0.004211 | 0.003618 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 18 | `te_feedforward_high_compute_long_remote` | `feedforward` | 0.003542 | 0.004228 | 0.003058 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 19 | `te_feedforward_stride5_long` | `feedforward` | 0.003580 | 0.004008 | 0.003178 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 20 | `te_feedforward_stride1_long` | `feedforward` | 0.003646 | 0.003990 | 0.003126 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 21 | `te_feedforward_trial` | `feedforward` | 0.003671 | 0.004418 | 0.003706 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |

### feedforward_bw

- Best run: `te_feedforward_stride1_high_compute_long_remote_Bw`
- Best test MAE: `0.003262`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Bw` | `feedforward` | 0.003262 | 0.003749 | 0.003049 | 109,953 | 1h 08m 06s | 1.28 MB | High | High | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### feedforward_fw

- Best run: `te_feedforward_stride1_high_compute_long_remote_Fw`
- Best test MAE: `0.003563`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Fw` | `feedforward` | 0.003563 | 0.004009 | 0.002915 | 109,953 | 25m 08s | 1.28 MB | High | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### harmonic_regression

- Best run: `te_harmonic_order12_linear_conditioned_recovery_global`
- Best test MAE: `0.020779`
- Completed tracked runs: `4`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.020779 | 0.022403 | 0.017017 | 150 | 14m 04s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 2 | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 0.020782 | 0.022405 | 0.017004 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_harmonic_order12_static_recovery` | `harmonic_regression` | 0.039404 | 0.042797 | 0.040524 | 25 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 4 | `te_harmonic_order06_static_recovery` | `harmonic_regression` | 0.039406 | 0.042796 | 0.040529 | 13 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |

### harmonic_regression_bw

- Best run: `te_harmonic_order12_linear_conditioned_recovery_Bw`
- Best test MAE: `0.003524`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_order12_linear_conditioned_recovery_Bw` | `harmonic_regression` | 0.003524 | 0.004080 | 0.003701 | 150 | 8m 57s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### harmonic_regression_fw

- Best run: `te_harmonic_order12_linear_conditioned_recovery_Fw`
- Best test MAE: `0.003129`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_order12_linear_conditioned_recovery_Fw` | `harmonic_regression` | 0.003129 | 0.003567 | 0.002811 | 150 | 10m 50s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### periodic_mlp

- Best run: `te_periodic_mlp_h04_standard`
- Best test MAE: `0.003317`
- Completed tracked runs: `4`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003317 | 0.003793 | 0.003097 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_periodic_mlp_h04_standard_global` | `periodic_mlp` | 0.003349 | 0.003916 | 0.002985 | 27,265 | 24m 13s | 0.33 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 3 | `te_periodic_mlp_h08_standard` | `periodic_mlp` | 0.003395 | 0.003951 | 0.003086 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_periodic_mlp_h08_wide` | `periodic_mlp` | 0.003590 | 0.004143 | 0.003089 | 47,745 | N/A | 0.57 MB | Medium | Unknown | `standalone_or_unknown` |

### periodic_mlp_bw

- Best run: `te_periodic_mlp_h04_standard_Bw`
- Best test MAE: `0.003525`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_Bw` | `periodic_mlp` | 0.003525 | 0.004132 | 0.003154 | 27,265 | 15m 06s | 0.33 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### periodic_mlp_fw

- Best run: `te_periodic_mlp_h04_standard_Fw`
- Best test MAE: `0.003432`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_Fw` | `periodic_mlp` | 0.003432 | 0.004023 | 0.002848 | 27,265 | 11m 04s | 0.33 MB | Medium | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### residual_harmonic_mlp

- Best run: `te_residual_h12_deep_joint_wave1`
- Best test MAE: `0.003152`
- Completed tracked runs: `20`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 0.003640 | 0.003024 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_residual_h12_small_joint_high_dropout_wave1` | `residual_harmonic_mlp` | 0.003230 | 0.003704 | 0.003001 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 3 | `te_residual_h16_small_joint_wave1` | `residual_harmonic_mlp` | 0.003274 | 0.003747 | 0.003020 | 4,898 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_wide_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | 0.003278 | 0.003814 | 0.002924 | 17,946 | N/A | 0.22 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | `residual_harmonic_mlp` | 0.003302 | 0.003909 | 0.002935 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 6 | `te_residual_h12_small_joint_low_dropout_wave1` | `residual_harmonic_mlp` | 0.003359 | 0.003852 | 0.003027 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 7 | `te_residual_h12_small_joint_no_layer_norm_wave1` | `residual_harmonic_mlp` | 0.003360 | 0.003835 | 0.003089 | 4,634 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 8 | `te_residual_h12_deep_dense_remote` | `residual_harmonic_mlp` | 0.003365 | 0.003868 | 0.003018 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_residual_h12_small_frozen_wave1` | `residual_harmonic_mlp` | 0.003368 | 0.003898 | 0.003036 | 4,865 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 10 | `te_residual_h12_wide_joint_wave1` | `residual_harmonic_mlp` | 0.003376 | 0.003906 | 0.002884 | 17,946 | N/A | 0.22 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_residual_h12_deep_long_remote` | `residual_harmonic_mlp` | 0.003384 | 0.003908 | 0.002973 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_residual_h08_small_frozen_wave1` | `residual_harmonic_mlp` | 0.003384 | 0.003912 | 0.003007 | 4,865 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 13 | `te_residual_h08_small_joint_wave1` | `residual_harmonic_mlp` | 0.003385 | 0.003862 | 0.003030 | 4,882 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 14 | `te_residual_h12_medium_joint_wave1` | `residual_harmonic_mlp` | 0.003406 | 0.003863 | 0.002968 | 9,498 | N/A | 0.13 MB | Low | Unknown | `standalone_or_unknown` |
| 15 | `te_residual_h12_small_joint_dense_wave1` | `residual_harmonic_mlp` | 0.003410 | 0.003790 | 0.002962 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 16 | `te_residual_h12_deep_joint_wave1_global` | `residual_harmonic_mlp` | 0.003420 | 0.003931 | 0.003115 | 26,266 | 20m 35s | 0.32 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 17 | `te_residual_h12_small_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | 0.003465 | 0.003944 | 0.002987 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 18 | `te_residual_h12_small_joint_recovery` | `residual_harmonic_mlp` | 0.003466 | 0.003967 | 0.003016 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 19 | `te_residual_h12_small_frozen_recovery` | `residual_harmonic_mlp` | 0.003554 | 0.004061 | 0.003030 | 4,865 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 20 | `te_residual_h12_small_joint_anchor_wave1` | `residual_harmonic_mlp` | 0.003557 | 0.004064 | 0.003090 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |

### residual_harmonic_mlp_bw

- Best run: `te_residual_h12_deep_joint_wave1_Bw`
- Best test MAE: `0.003493`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1_Bw` | `residual_harmonic_mlp` | 0.003493 | 0.004108 | 0.003110 | 26,266 | 15m 03s | 0.32 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### residual_harmonic_mlp_fw

- Best run: `te_residual_h12_deep_joint_wave1_Fw`
- Best test MAE: `0.003530`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1_Fw` | `residual_harmonic_mlp` | 0.003530 | 0.004145 | 0.002852 | 26,266 | 10m 41s | 0.32 MB | Medium | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### tree

- Best run: `te_hist_gbr_tabular`
- Best test MAE: `0.002885`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | N/A | 0.62 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | 2m 01s | 0.62 MB | Light Artifact | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 3 | `te_hist_gbr_remote_deep` | `hist_gradient_boosting` | 0.002920 | 0.003644 | 0.002749 | 5 | N/A | 0.91 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 4 | `te_hist_gbr_remote_refined` | `hist_gradient_boosting` | 0.003101 | 0.003781 | 0.002809 | 5 | N/A | 0.84 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 5 | `te_random_forest_tabular_recovery` | `random_forest` | 0.003833 | 0.004809 | 0.003792 | 5 | N/A | 7.09 GB | Extreme Artifact | Unknown | `standalone_or_unknown` |
| 6 | `te_random_forest_remote_medium` | `random_forest` | 0.003865 | 0.004861 | 0.003808 | 5 | N/A | 85.40 GB | Extreme Artifact | Unknown | `standalone_or_unknown` |

### tree_bw

- Best run: `te_hist_gbr_tabular_Bw`
- Best test MAE: `0.003087`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Bw` | `hist_gradient_boosting` | 0.003087 | 0.003850 | 0.002698 | 5 | 1m 12s | 0.50 MB | Very Low | Very Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

### tree_fw

- Best run: `te_hist_gbr_tabular_Fw`
- Best test MAE: `0.002845`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002845 | 0.003476 | 0.002666 | 5 | 1m 10s | 0.50 MB | Very Low | Very Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

## Source Of Truth

- Live backlog: `doc/running/te_model_live_backlog.md`
- Active campaign state: `doc/running/active_training_campaign.yaml`
- Program registry: `output/registries/program/current_best_solution.yaml`
- Family registries root: `output/registries/families`
- Training campaign root: `output/training_campaigns`
- Training run root: `output/training_runs`
- Paper reference report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

This document is repository-generated. Regenerate it after new campaign results so the cross-family snapshot stays aligned with the canonical registries and campaign artifacts.
