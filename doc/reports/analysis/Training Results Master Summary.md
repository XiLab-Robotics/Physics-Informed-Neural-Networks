# Training Results Master Summary

## Executive Snapshot

- Generated At: `2026-05-21T09:38:39`
- Program State: active.
- Current Completed Wave: `Wave 1` structured-baseline optimization pass,
- Current Focus: finish `Track 2` by closing the canonical direction-aware
- Active Campaign Status: `prepared`
- Active Campaign Name: `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49`
- Current Global Winner: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | Family `tree_fw` | Test MAE `0.002743`

## Main Takeaways

- Strongest current neural family: `residual_harmonic_mlp`
- Current plain MLP anchor: `te_feedforward_stride1_high_compute_long_remote_global`
- Active family-improvement branch count: `2`
- Implemented and benchmarked family count: `15`

## Current Project Status

### Implemented And Benchmarked Families

- Multi-scope waves must keep `global`, `Fw`, and `Bw` reporting surfaces separated in this canonical summary.

#### Global Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree` | Implemented Benchmark | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002782 | 5 | `2026-05-11 20:38:56` |
| `residual_harmonic_mlp` | Strongest Neural Family | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 26,266 | `2026-05-20 11:41:03` |
| `feedforward` | Current Plain MLP Anchor | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 109,953 | `2026-05-13 13:25:56` |
| `periodic_mlp` | Active Improvement | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 27,265 | `2026-05-21 08:12:57` |
| `feedforward_recovery_micro` | Implemented Benchmark | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004164 | 109,953 | `2026-05-12 11:12:51` |
| `feedforward_recovery_probe_dense` | Implemented Benchmark | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004602 | 109,953 | `2026-05-12 17:16:41` |
| `harmonic_regression` | Active Improvement | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | 0.020767 | 114 | `2026-05-20 10:32:21` |

#### Forward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree_fw` | Current Global Winner | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002743 | 5 | `2026-05-11 20:58:32` |
| `harmonic_regression_fw` | Implemented Benchmark | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002916 | 4,326 | `2026-05-20 10:50:22` |
| `periodic_mlp_fw` | Implemented Benchmark | `te_periodic_mlp_dense240_tracking_Fw` | `periodic_mlp` | 0.003055 | 87,681 | `2026-05-21 08:48:01` |
| `residual_harmonic_mlp_fw` | Implemented Benchmark | `te_residual_harmonic_rcim_sparse_tracking_Fw` | `residual_harmonic_mlp` | 0.003089 | 26,260 | `2026-05-20 11:57:15` |
| `feedforward_fw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.003203 | 109,953 | `2026-05-14 22:03:06` |

#### Backward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree_bw` | Implemented Benchmark | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002954 | 5 | `2026-05-11 21:18:29` |
| `residual_harmonic_mlp_bw` | Implemented Benchmark | `te_residual_harmonic_rcim_sparse_tracking_Bw` | `residual_harmonic_mlp` | 0.003042 | 26,260 | `2026-05-20 12:25:49` |
| `feedforward_bw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003099 | 167,937 | `2026-05-14 13:49:53` |
| `periodic_mlp_bw` | Implemented Benchmark | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.003233 | 27,777 | `2026-05-21 09:38:37` |
| `harmonic_regression_bw` | Implemented Benchmark | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003400 | 2,886 | `2026-05-20 11:08:01` |

### Active Training Or Improvement Branches

- Current campaign: `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49`
- Launch mode: `N/A`
- Families under active improvement: `harmonic_regression`, `periodic_mlp`
- Planning report: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`

### Roadmap And Planned Work

| Wave Or Track | Status |
| --- | --- |
| Wave 0. Shared Infrastructure | completed. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 1. Structured Static Baselines | planning report: completed;; implementation: completed;; smoke tests: completed;; validation checks: completed;; campaign execution: completed;; directional HPO closeout: completed;; exported `global`, `forward`, and `backward` surfaces: completed;; results report: completed;; status: closed. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Track 1. RCIM Paper-Faithful Model Bank | recovered original workflow: preserved;; original-dataset reimplementation: completed;; retuned reference archive: completed;; forward campaign: completed;; backward campaign: completed;; paper-reference archives: refreshed;; Tables `2`-`5`: repopulated;; status: closed as faithful full-bank reproduction, not all-green |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Track 2. Directional Offline Comparison | direction-aware loader and candidate matrix: completed;; recovered original forward candidates: included;; retuned forward and backward candidates: included;; `Track 1` forward and backward candidates: included;; `Wave 1` `global`, `forward`, and `backward` exports: included;; grouped source tables: completed;; composite best-reference visibility: completed;; direction/truth and preview audit: completed;; status: active closeout branch. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 2. Temporal Models | status: planned after Track 2 closeout;; mandatory rule: prepare or justify `global`, `forward`, and `backward`; baseline comparison: Track 2 plus closed Wave 1. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 3. Hybrid Structured Models | status: pending;; mandatory rule: prepare or justify `global`, `forward`, and `backward`; paper-reproduction scope:; compare hybrid structured predictors against the paper-style harmonic stack;; prepare the repository-owned deployable predictor package. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 4. PINN Formulation And First PINN | status: pending;; mandatory rule: prepare or justify `global`, `forward`, and `backward`; paper-reproduction scope:; prepare PINN-side model and loss formulations for later offline and; keep online compensation execution out of Wave 4 unless Track 3 is |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 5. Cross-Wave Comparison And Best Solution | status: pending;; mandatory rule: preserve direction-separated reporting;; paper-reproduction scope:; compare closed offline waves and Track 3 results when available;; finalize the real `paper vs repository` comparison only after Track 3 |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Track 3. Online Compensation And Deployment Evaluation | status: future implementation branch;; canonical objective: close `Target B`;; scope:; online compensation loop in the TestRig / TwinCAT path;; old future Pipelines `8-10`;; `Robot` and `Cycloidal` motion-profile validation;; uncompensated versus compensated `TE RMS` and `TE max`;; final paper-style `Table 9` report;; deployment-readiness interpretation for the selected repository model path. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`

## Recent Campaign Changes

| Campaign | Generated At | Completed | Failed | Winner | Impact |
| --- | --- | ---: | ---: | --- | --- |
| `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` | `2026-05-21 09:38:37` | 9 | 0 | `te_periodic_mlp_dense240_tracking_Fw` | Updated periodic_mlp_fw family best |
| `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` | `2026-05-20 12:25:49` | 18 | 0 | `te_harmonic_dense360_tracking_Fw` | Updated harmonic_regression_fw family best |

## Ranking Policy

- Primary metric: `test_mae`
- First tie-breaker: `test_rmse`
- Second tie-breaker: `val_mae`
- Third tie-breaker: `trainable_parameter_count`
- Direction: `minimize`

## Best Result Per Family

- Scope-separated family ranking is mandatory for every future wave that introduces more than one canonical training surface.

### Global Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree` | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002655 | 0.002782 | 0.003520 | 5 | 0.48 MB | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.002895 | 0.003034 | 0.003550 | 26,266 | 0.32 MB | Unknown | Strongest Neural Family |
| `feedforward` | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003056 | 0.003150 | 0.003603 | 109,953 | 1.28 MB | Unknown | Current Plain MLP Anchor |
| `periodic_mlp` | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.002994 | 0.003186 | 0.003690 | 27,265 | 0.33 MB | Unknown | Active Improvement |
| `feedforward_recovery_micro` | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004266 | 0.004164 | 0.005109 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `feedforward_recovery_probe_dense` | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004257 | 0.004602 | 0.005262 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `harmonic_regression` | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | 0.016995 | 0.020767 | 0.022376 | 114 | 0.01 MB | Low | Active Improvement |

### Forward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree_fw` | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002677 | 0.002743 | 0.003409 | 5 | 0.45 MB | Unknown | Current Global Winner |
| `harmonic_regression_fw` | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002610 | 0.002916 | 0.003237 | 4,326 | 0.06 MB | Low | Implemented Benchmark |
| `periodic_mlp_fw` | `te_periodic_mlp_dense240_tracking_Fw` | `periodic_mlp` | 0.002541 | 0.003055 | 0.003537 | 87,681 | 1.03 MB | Low | Implemented Benchmark |
| `residual_harmonic_mlp_fw` | `te_residual_harmonic_rcim_sparse_tracking_Fw` | `residual_harmonic_mlp` | 0.002704 | 0.003089 | 0.003498 | 26,260 | 0.32 MB | Low | Implemented Benchmark |
| `feedforward_fw` | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.002850 | 0.003203 | 0.003787 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |

### Backward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree_bw` | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002681 | 0.002954 | 0.003749 | 5 | 0.45 MB | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_bw` | `te_residual_harmonic_rcim_sparse_tracking_Bw` | `residual_harmonic_mlp` | 0.002953 | 0.003042 | 0.003548 | 26,260 | 0.32 MB | Low | Implemented Benchmark |
| `feedforward_bw` | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003018 | 0.003099 | 0.003630 | 167,937 | 1.95 MB | Unknown | Implemented Benchmark |
| `periodic_mlp_bw` | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.002907 | 0.003233 | 0.003792 | 27,777 | 0.34 MB | Unknown | Implemented Benchmark |
| `harmonic_regression_bw` | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003588 | 0.003400 | 0.003886 | 2,886 | 0.04 MB | Low | Implemented Benchmark |

## Cross-Family Interpretation

- Current global reference winner: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` from family `tree_fw`.
- Strongest current neural family: `residual_harmonic_mlp`.
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
| Offline model-selection direction | Boosting/tree-heavy deployed harmonic predictors | Current winner `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` from family `tree_fw` with model type `hist_gradient_boosting` | not_aligned |
| Strongest neural branch role | Neural models are evaluated, but not the primary deployed winners | Strongest repository neural family is `residual_harmonic_mlp` and still trails the tree winner | aligned |
| Track 1 canonical closure rule | Paper Tables `3-6` replicated per target and per harmonic | Exact-paper report currently shows `0/0` harmonics fully closed, `0/0` partially closed, `0/0` still open | not_yet_met |
| Supporting harmonic-wise TE metric | Mean percentage error over full TE curves | Latest harmonic-wise validation reports `11.212%` mean percentage error on held-out curves using harmonics `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | supporting_only_not_yet_met |
| Online robot-profile compensation | TE RMS reduction `83.6%` | No repository-owned online compensation result yet | not_yet_comparable |
| Online cycloidal-profile compensation | TE RMS reduction `94.0%`, TE max reduction `91.7%` | No repository-owned online compensation result yet | not_yet_comparable |
| Table 9-style end-to-end benchmark | PLC-integrated motion-profile compensation benchmark | Missing in the repository at the current state | not_yet_comparable |

### Track 1 Canonical Status

- Latest exact-paper validation summary: `N/A`
- Table `3` amplitude `RMSE`: `0/0` harmonics at or below the paper target
- Table `4` phase `MAE`: `0/0` harmonics at or below the paper target
- Table `5` phase `RMSE`: `0/0` harmonics at or below the paper target
- Target-level expected-family direction: `0/0`
- Harmonic-level Table `6` closure: `0/0` fully matched, `0/0` partially matched, `0/0` still open
- Highest-priority open harmonics: `N/A`

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
- Neural models remain secondary in the repository (`residual_harmonic_mlp`), which is also consistent with the paper not promoting a plain neural winner for deployment.
- End-to-end paper comparison remains `not yet comparable` until repository-owned online compensation tests exist.

## Family-By-Family Result Breakdowns

- For multi-scope waves, family breakdowns are grouped by canonical reporting scope before the per-family ranking tables.

### Global Models

#### feedforward

- Best run: `te_feedforward_stride1_high_compute_long_remote_global`
- Best test MAE: `0.003150`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 0.003603 | 0.003056 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0017` | `feedforward` | 0.003208 | 0.003810 | 0.002962 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0012` | `feedforward` | 0.003217 | 0.003847 | 0.003014 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |

#### feedforward_recovery_micro

- Best run: `te_feedforward_optuna_recovery_micro_global_optuna_t0000`
- Best test MAE: `0.004164`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004164 | 0.005109 | 0.004266 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |

#### feedforward_recovery_probe_dense

- Best run: `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000`
- Best test MAE: `0.004602`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004602 | 0.005262 | 0.004257 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |

#### harmonic_regression

- Best run: `te_harmonic_rcim_sparse_tracking_global`
- Best test MAE: `0.020767`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | 0.020767 | 0.022376 | 0.016995 | 114 | 6m 17s | 0.01 MB | Very Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.020774 | 0.022412 | 0.017025 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0001_stride1` | `harmonic_regression` | 0.020775 | 0.022417 | 0.017013 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.020779 | 0.022403 | 0.017017 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 5 | `te_harmonic_dense360_tracking_global` | `harmonic_regression` | 0.020780 | 0.022399 | 0.016991 | 4,326 | 8m 57s | 0.06 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 6 | `te_harmonic_dense240_tracking_global` | `harmonic_regression` | 0.020787 | 0.022388 | 0.016989 | 2,886 | 6m 02s | 0.04 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |

#### periodic_mlp

- Best run: `te_periodic_mlp_h04_standard_global_optuna_t0010`
- Best test MAE: `0.003186`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 0.003690 | 0.002994 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_periodic_mlp_h04_standard_global_optuna_t0008` | `periodic_mlp` | 0.003200 | 0.003798 | 0.003057 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_periodic_mlp_h04_standard_global_optuna_t0006` | `periodic_mlp` | 0.003233 | 0.003733 | 0.002964 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_periodic_mlp_rcim_sparse_tracking_global` | `periodic_mlp` | 0.003275 | 0.003726 | 0.002863 | 28,545 | 7h 47m 34s | 0.35 MB | Medium | Very High | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 5 | `te_periodic_mlp_dense240_tracking_global` | `periodic_mlp` | 0.003348 | 0.003862 | 0.002962 | 87,681 | 20m 22s | 1.03 MB | High | Medium | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 6 | `te_periodic_mlp_dense360_tracking_global` | `periodic_mlp` | 0.003401 | 0.003831 | 0.002859 | 118,401 | 50m 45s | 1.38 MB | High | High | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |

#### residual_harmonic_mlp

- Best run: `te_residual_h12_deep_joint_wave1_global_optuna_t0006`
- Best test MAE: `0.003034`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 0.003550 | 0.002895 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_residual_h12_deep_joint_wave1_global_optuna_t0010` | `residual_harmonic_mlp` | 0.003067 | 0.003568 | 0.002903 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 0.003640 | 0.003024 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_harmonic_dense240_tracking_global` | `residual_harmonic_mlp` | 0.003162 | 0.003598 | 0.002976 | 26,722 | 11m 07s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 5 | `te_residual_harmonic_rcim_sparse_tracking_global` | `residual_harmonic_mlp` | 0.003378 | 0.003902 | 0.002969 | 26,260 | 8m 03s | 0.32 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 6 | `te_residual_harmonic_dense360_tracking_global` | `residual_harmonic_mlp` | 0.003434 | 0.003957 | 0.002943 | 26,962 | 13m 52s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |

#### tree

- Best run: `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10`
- Best test MAE: `0.002782`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | N/A | 0.48 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf20` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | N/A | 0.48 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 3 | `te_hist_gbr_tabular_global_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.002830 | 0.003585 | 0.002677 | 5 | N/A | 0.50 MB | Light Artifact | Unknown | `standalone_or_unknown` |

### Forward Models

#### feedforward_fw

- Best run: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008`
- Best test MAE: `0.003203`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.003203 | 0.003787 | 0.002850 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0009` | `feedforward` | 0.003229 | 0.003774 | 0.002850 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0014` | `feedforward` | 0.003232 | 0.003812 | 0.002846 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |

#### harmonic_regression_fw

- Best run: `te_harmonic_dense360_tracking_Fw`
- Best test MAE: `0.002916`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002916 | 0.003237 | 0.002610 | 4,326 | 7m 00s | 0.06 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_harmonic_dense240_tracking_Fw` | `harmonic_regression` | 0.002935 | 0.003239 | 0.002593 | 2,886 | 5m 56s | 0.04 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 3 | `te_harmonic_rcim_sparse_tracking_Fw` | `harmonic_regression` | 0.002943 | 0.003254 | 0.002566 | 114 | 5m 05s | 0.01 MB | Very Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride5` | `harmonic_regression` | 0.003101 | 0.003527 | 0.002848 | 102 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 5 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.003102 | 0.003528 | 0.002843 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr00005_stride1` | `harmonic_regression` | 0.003105 | 0.003534 | 0.002839 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |

#### periodic_mlp_fw

- Best run: `te_periodic_mlp_dense240_tracking_Fw`
- Best test MAE: `0.003055`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_dense240_tracking_Fw` | `periodic_mlp` | 0.003055 | 0.003537 | 0.002541 | 87,681 | 13m 21s | 1.03 MB | High | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 2 | `te_periodic_mlp_rcim_sparse_tracking_Fw` | `periodic_mlp` | 0.003131 | 0.003578 | 0.002516 | 28,545 | 9m 28s | 0.35 MB | Medium | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 3 | `te_periodic_mlp_dense360_tracking_Fw` | `periodic_mlp` | 0.003155 | 0.003680 | 0.002524 | 118,401 | 12m 15s | 1.38 MB | High | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 4 | `te_periodic_mlp_h04_standard_Fw_optuna_t0008` | `periodic_mlp` | 0.003287 | 0.003833 | 0.002809 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_periodic_mlp_h04_standard_Fw_optuna_t0001` | `periodic_mlp` | 0.003294 | 0.003899 | 0.002751 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_periodic_mlp_h04_standard_Fw_optuna_t0015` | `periodic_mlp` | 0.003296 | 0.003924 | 0.002802 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |

#### residual_harmonic_mlp_fw

- Best run: `te_residual_harmonic_rcim_sparse_tracking_Fw`
- Best test MAE: `0.003089`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_rcim_sparse_tracking_Fw` | `residual_harmonic_mlp` | 0.003089 | 0.003498 | 0.002704 | 26,260 | 4m 56s | 0.32 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0005` | `residual_harmonic_mlp` | 0.003168 | 0.003871 | 0.002870 | 34,978 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0006` | `residual_harmonic_mlp` | 0.003194 | 0.003809 | 0.002827 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0009` | `residual_harmonic_mlp` | 0.003211 | 0.003828 | 0.002794 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_harmonic_dense240_tracking_Fw` | `residual_harmonic_mlp` | 0.003304 | 0.003773 | 0.002649 | 26,722 | 5m 04s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 6 | `te_residual_harmonic_dense360_tracking_Fw` | `residual_harmonic_mlp` | 0.003568 | 0.004118 | 0.002598 | 26,962 | 6m 12s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |

#### tree_fw

- Best run: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10`
- Best test MAE: `0.002743`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002845 | 0.003476 | 0.002666 | 5 | N/A | 0.50 MB | Very Low | Unknown | `standalone_or_unknown` |

### Backward Models

#### feedforward_bw

- Best run: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005`
- Best test MAE: `0.003099`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003099 | 0.003630 | 0.003018 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0013` | `feedforward` | 0.003106 | 0.003700 | 0.002989 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0016` | `feedforward` | 0.003173 | 0.003818 | 0.002901 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |

#### harmonic_regression_bw

- Best run: `te_harmonic_dense240_tracking_Bw`
- Best test MAE: `0.003400`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003400 | 0.003886 | 0.003588 | 2,886 | 5m 00s | 0.04 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_harmonic_dense360_tracking_Bw` | `harmonic_regression` | 0.003403 | 0.003866 | 0.003637 | 4,326 | 6m 43s | 0.06 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 3 | `te_harmonic_rcim_sparse_tracking_Bw` | `harmonic_regression` | 0.003406 | 0.003894 | 0.003570 | 114 | 5m 56s | 0.01 MB | Very Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5` | `harmonic_regression` | 0.003494 | 0.004081 | 0.003638 | 102 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 5 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr00005_stride1` | `harmonic_regression` | 0.003497 | 0.004053 | 0.003743 | 102 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.003506 | 0.004063 | 0.003729 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |

#### periodic_mlp_bw

- Best run: `te_periodic_mlp_h04_standard_Bw_optuna_t0006`
- Best test MAE: `0.003233`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.003233 | 0.003792 | 0.002907 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_periodic_mlp_h04_standard_Bw_optuna_t0007` | `periodic_mlp` | 0.003239 | 0.003820 | 0.002933 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_periodic_mlp_h04_standard_Bw_optuna_t0010` | `periodic_mlp` | 0.003248 | 0.003817 | 0.002963 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_periodic_mlp_rcim_sparse_tracking_Bw` | `periodic_mlp` | 0.003398 | 0.003922 | 0.003011 | 28,545 | 9m 57s | 0.35 MB | Medium | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 5 | `te_periodic_mlp_dense240_tracking_Bw` | `periodic_mlp` | 0.003417 | 0.004005 | 0.003041 | 87,681 | 20m 05s | 1.03 MB | High | Medium | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 6 | `te_periodic_mlp_dense360_tracking_Bw` | `periodic_mlp` | 0.003424 | 0.004006 | 0.003072 | 118,401 | 20m 33s | 1.38 MB | High | Medium | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |

#### residual_harmonic_mlp_bw

- Best run: `te_residual_harmonic_rcim_sparse_tracking_Bw`
- Best test MAE: `0.003042`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_rcim_sparse_tracking_Bw` | `residual_harmonic_mlp` | 0.003042 | 0.003548 | 0.002953 | 26,260 | 6m 07s | 0.32 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_residual_harmonic_dense360_tracking_Bw` | `residual_harmonic_mlp` | 0.003068 | 0.003545 | 0.002826 | 26,962 | 14m 01s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 3 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0007` | `residual_harmonic_mlp` | 0.003162 | 0.003862 | 0.002948 | 34,962 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0012` | `residual_harmonic_mlp` | 0.003180 | 0.003642 | 0.002979 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_harmonic_dense240_tracking_Bw` | `residual_harmonic_mlp` | 0.003188 | 0.003717 | 0.002861 | 26,722 | 8m 25s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 6 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0013` | `residual_harmonic_mlp` | 0.003195 | 0.003636 | 0.003051 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |

#### tree_bw

- Best run: `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10`
- Best test MAE: `0.002954`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_hist_gbr_tabular_Bw_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.003002 | 0.003809 | 0.002650 | 5 | N/A | 0.44 MB | Very Low | Unknown | `standalone_or_unknown` |

## Source Of Truth

- Live backlog: `doc/running/te_model_live_backlog.md`
- Active campaign state: `doc/running/active_training_campaign.yaml`
- Program registry: `output/registries/program/current_best_solution.yaml`
- Family registries root: `output/registries/families`
- Training campaign root: `output/training_campaigns`
- Training run root: `output/training_runs`
- Paper reference report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

This document is repository-generated. Regenerate it after new campaign results so the cross-family snapshot stays aligned with the canonical registries and campaign artifacts.
