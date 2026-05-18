# Training Results Master Summary

## Executive Snapshot

- Generated At: `2026-05-18T01:08:06`
- Program State: active
- Current Completed Wave: `Wave 1` structured-baseline familywise optimization pass
- Current Focus: offline Track 2 directional model comparison is populated;
- Active Campaign Status: `completed`
- Active Campaign Name: `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30`
- Current Global Winner: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | Family `tree_fw` | Test MAE `0.002743`

## Main Takeaways

- Strongest current neural family: `residual_harmonic_mlp`
- Current plain MLP anchor: `te_feedforward_stride1_high_compute_long_remote_global`
- Active family-improvement branch count: `0`
- Implemented and benchmarked family count: `17`

## Current Project Status

### Implemented And Benchmarked Families

- Multi-scope waves must keep `global`, `Fw`, and `Bw` reporting surfaces separated in this canonical summary.

#### Global Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree` | Implemented Benchmark | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002782 | 5 | `2026-05-11 20:38:56` |
| `residual_harmonic_mlp` | Strongest Neural Family | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 26,266 | `2026-05-15 21:29:05` |
| `feedforward` | Current Plain MLP Anchor | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 109,953 | `2026-05-13 13:25:56` |
| `periodic_mlp` | Implemented Benchmark | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 27,265 | `2026-05-15 04:43:30` |
| `feedforward_recovery_micro` | Implemented Benchmark | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004164 | 109,953 | `2026-05-12 11:12:51` |
| `feedforward_recovery_probe_dense` | Implemented Benchmark | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004602 | 109,953 | `2026-05-12 17:16:41` |
| `harmonic_regression` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.020774 | 150 | `2026-05-12 00:51:52` |

#### Forward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree_fw` | Current Global Winner | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002743 | 5 | `2026-05-11 20:58:32` |
| `harmonic_regression_fw` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride5` | `harmonic_regression` | 0.003101 | 102 | `2026-05-12 03:06:40` |
| `residual_harmonic_mlp_fw` | Implemented Benchmark | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0005` | `residual_harmonic_mlp` | 0.003168 | 34,978 | `2026-05-16 06:03:09` |
| `feedforward_fw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.003203 | 109,953 | `2026-05-14 22:03:06` |
| `periodic_mlp_fw` | Implemented Benchmark | `te_periodic_mlp_h04_standard_Fw_optuna_t0008` | `periodic_mlp` | 0.003287 | 46,721 | `2026-05-15 12:47:24` |

#### Backward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree_bw` | Implemented Benchmark | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002954 | 5 | `2026-05-11 21:18:29` |
| `feedforward_bw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003099 | 167,937 | `2026-05-14 13:49:53` |
| `residual_harmonic_mlp_bw` | Implemented Benchmark | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0007` | `residual_harmonic_mlp` | 0.003162 | 34,962 | `2026-05-16 02:55:16` |
| `periodic_mlp_bw` | Implemented Benchmark | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.003233 | 27,777 | `2026-05-15 09:47:21` |
| `harmonic_regression_bw` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5` | `harmonic_regression` | 0.003494 | 102 | `2026-05-12 05:44:32` |

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
| Track 1. RCIM Paper-Faithful Model Bank | closed as faithful full-bank reproduction; forward and backward grid-search campaigns completed; Tables `2`-`5` repopulated; not all cells are green |

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
| `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__backward_svr_mlp_rf_dt_et_ert_gbm_hgbm_lgbm_xgbm_elm_search` | `2026-05-16-19-04-25` | 11 | 0 | `backward` | Closed the backward Track 1 full-bank surface, refreshed paper-reference archives, and repopulated RCIM Tables `2`-`5` |
| `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__forward_svr_mlp_rf_dt_et_ert_gbm_hgbm_lgbm_xgbm_elm_search` | `2026-05-15-07-07-30` | 11 | 0 | `forward` | Closed the forward Track 1 full-bank surface, refreshed paper-reference archives, and repopulated RCIM Tables `2`-`5` |
| `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` | `2026-05-12 05:44:32` | 90 | 0 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | Updated global best |
| `wave1_directional_retraining_campaign_2026_05_06_16_07_16` | `2026-05-06 23:14:10` | 15 | 0 | `te_hist_gbr_tabular_Fw` | No family-best change |

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
| `tree` | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002655 | 0.002782 | 0.003520 | 5 | 0.48 MB | Very Low | Implemented Benchmark |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.002895 | 0.003034 | 0.003550 | 26,266 | 0.32 MB | Unknown | Strongest Neural Family |
| `feedforward` | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003056 | 0.003150 | 0.003603 | 109,953 | 1.28 MB | Very High | Current Plain MLP Anchor |
| `periodic_mlp` | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.002994 | 0.003186 | 0.003690 | 27,265 | 0.33 MB | Unknown | Implemented Benchmark |
| `feedforward_recovery_micro` | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004266 | 0.004164 | 0.005109 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `feedforward_recovery_probe_dense` | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004257 | 0.004602 | 0.005262 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.017025 | 0.020774 | 0.022412 | 150 | 0.01 MB | Low | Implemented Benchmark |

### Forward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree_fw` | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002677 | 0.002743 | 0.003409 | 5 | 0.45 MB | Very Low | Current Global Winner |
| `harmonic_regression_fw` | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride5` | `harmonic_regression` | 0.002848 | 0.003101 | 0.003527 | 102 | 0.01 MB | Low | Implemented Benchmark |
| `residual_harmonic_mlp_fw` | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0005` | `residual_harmonic_mlp` | 0.002870 | 0.003168 | 0.003871 | 34,978 | 0.42 MB | Unknown | Implemented Benchmark |
| `feedforward_fw` | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.002850 | 0.003203 | 0.003787 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `periodic_mlp_fw` | `te_periodic_mlp_h04_standard_Fw_optuna_t0008` | `periodic_mlp` | 0.002809 | 0.003287 | 0.003833 | 46,721 | 0.56 MB | Unknown | Implemented Benchmark |

### Backward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree_bw` | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002681 | 0.002954 | 0.003749 | 5 | 0.45 MB | Very Low | Implemented Benchmark |
| `feedforward_bw` | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003018 | 0.003099 | 0.003630 | 167,937 | 1.95 MB | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_bw` | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0007` | `residual_harmonic_mlp` | 0.002948 | 0.003162 | 0.003862 | 34,962 | 0.42 MB | Unknown | Implemented Benchmark |
| `periodic_mlp_bw` | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.002907 | 0.003233 | 0.003792 | 27,777 | 0.34 MB | Unknown | Implemented Benchmark |
| `harmonic_regression_bw` | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5` | `harmonic_regression` | 0.003638 | 0.003494 | 0.004081 | 102 | 0.01 MB | Low | Implemented Benchmark |

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
| Track 1 canonical closure rule | Paper Tables `2`-`5` reproduced as a faithful model-bank comparison surface | Forward and backward Track 1 paper-faithful campaigns are completed, archived under `models/paper_reference/rcim_track1/`, and tabulated in `RCIM Paper Reference Benchmark.md` | closed_populated_not_cell_exact |
| Track 2 offline model comparison | Direction-valid direct TE-curve comparison between accepted reference banks and repository models | Full matrix generated across `22` Track 1 family banks and `15` Wave 1 exported surfaces, tabulated in `Track 2 Directional Model Comparison.md` | populated_directional_offline |
| Supporting harmonic-wise TE metric | Mean percentage error over full TE curves | Latest harmonic-wise validation reports `11.212%` mean percentage error on held-out curves using harmonics `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | supporting_only_not_yet_met |
| Online robot-profile compensation | TE RMS reduction `83.6%` | No repository-owned online compensation result yet | not_yet_comparable |
| Online cycloidal-profile compensation | TE RMS reduction `94.0%`, TE max reduction `91.7%` | No repository-owned online compensation result yet | not_yet_comparable |
| Table 9-style end-to-end benchmark | PLC-integrated motion-profile compensation benchmark | Missing in the repository at the current state | not_yet_comparable |

### Directional Family Surface Rule

Every model family in `Wave 1` and future waves must be prepared as three
explicit surfaces when the model family is promoted into the comparable
program-level workflow:

- `global`: trained and evaluated on forward plus backward curves together;
- `Fw`: trained and evaluated only on forward curves;
- `Bw`: trained and evaluated only on backward curves.

The same direction contract is now used by `Track 2`: directional candidates
are scored only on their matching held-out curve direction, while global
candidates are scored on both directions with direction-separated metrics.
All new `Track 1`, `Track 2`, `Wave 1`, and future-wave training or comparison
workflows must load TE curves directly from `data/datasets` through
`config/datasets/transmission_error_dataset.yaml`.

Current Track 2 output:
`doc/reports/analysis/Track 2 Directional Model Comparison.md`, backed by
`output/validation_checks/track2_reference_comparison/2026-05-18-01-01-02__track2_full_directional_family_matrix_full_directional_matrix_validation/`.

### Track 1 Canonical Status

- Status: `closed` as the faithful full-bank RCIM paper-pipeline
  reproduction surface.
- Recovered original workflow root: `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
- Faithful original-dataset exact-model-bank root:
  `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`
- Accepted paper-reference archive root: `models/paper_reference/rcim_track1/`
- Canonical Tables `2`-`5` benchmark report:
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- Latest exact-paper closeout report:
  `doc/reports/campaign_results/track1/exact_paper/backward/2026-05-16-20-07-07_track1_backward_paper_faithful_grid_search_closeout_report.md`
- Prior forward exact-paper closeout report:
  `doc/reports/campaign_results/track1/exact_paper/forward/2026-05-15-11-11-35_track1_forward_paper_faithful_grid_search_closeout_report.md`
- Latest completed surface: `backward` paper-faithful grid search across
  `SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, LGBM, XGBM, ELM`.
- Table `2` `forward` status: `19` green, `25` yellow, `66` red.
- Table `3` `forward` status: `21` green, `28` yellow, `61` red.
- Table `4` `forward` status: `23` green, `21` yellow, `55` red.
- Table `5` `forward` status: `23` green, `32` yellow, `44` red.
- Table `2` `backward` status: `61` green, `22` yellow, `27` red.
- Table `3` `backward` status: `63` green, `20` yellow, `27` red.
- Table `4` `backward` status: `65` green, `21` yellow, `13` red.
- Table `5` `backward` status: `65` green, `21` yellow, `13` red.
- Harmonic-wise Table `6` evidence remains postponed into the harmonic-wise
  comparison branch and does not gate Track 1 closure.

### Latest Harmonic-Wise Validation Support

- Latest harmonic-wise validation summary: `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/family_exploration/rf/2026-04-13-16-00-30__track1_rf_h039_h162240_bridge_control_campaign_run/validation_summary.yaml`
- Harmonic-wise test mean percentage error: `11.212%`
- `Target A` status from the latest harmonic-wise run: `not_yet_met`

### Online Compensation Tracking Placeholder

- Repository online compensation status: `not yet available`.
- When online compensation tests are implemented, update this master summary with TE RMS, TE max, and reduction percentages for both robot and cycloidal motion profiles.
- Until those tests exist, present the paper comparison as `offline-only` rather than end-to-end equivalent.

### Gap Summary

- `Track 1` Tables `2`-`5` are closed as populated forward/backward
  faithful full-bank surfaces, but not every cell matches the paper or
  retuned reference within the green threshold.
- Offline benchmark scope remains `partially comparable` rather than like-for-like.
- A future restricted-dataset Track 1 rerun is deferred until after all planned
  waves are implemented; it must create a new Markdown comparison report that
  places full-dataset and reduced-dataset Tables `2`-`5` side by side for each
  dataset-reduction level.
- Not yet aligned: the current repository winner is not tree-based, while the paper deployment path is dominated by boosting/tree models.
- Neural models remain secondary in the repository (`residual_harmonic_mlp`), which is also consistent with the paper not promoting a plain neural winner for deployment.
- End-to-end paper comparison remains `not yet comparable` until repository-owned online compensation tests exist.

## Family-By-Family Result Breakdowns

- For multi-scope waves, family breakdowns are grouped by canonical reporting scope before the per-family ranking tables.

### Global Models

#### feedforward

- Best run: `te_feedforward_stride1_high_compute_long_remote_global`
- Best test MAE: `0.003150`
- Completed tracked runs: `33`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 0.003603 | 0.003056 | 109,953 | 2h 27m 05s | 1.28 MB | High | Very High | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0017` | `feedforward` | 0.003208 | 0.003810 | 0.002962 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0012` | `feedforward` | 0.003217 | 0.003847 | 0.003014 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0011` | `feedforward` | 0.003238 | 0.003725 | 0.003028 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 5 | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` | 0.003264 | 0.003679 | 0.003044 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 6 | `te_feedforward_high_compute_remote` | `feedforward` | 0.003274 | 0.003873 | 0.003059 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 7 | `te_feedforward_stride1_big_remote` | `feedforward` | 0.003278 | 0.003671 | 0.003019 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 8 | `te_feedforward_stride5_long_large_batch` | `feedforward` | 0.003301 | 0.003791 | 0.003109 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_feedforward_stride1_long_large_batch_big_model` | `feedforward` | 0.003308 | 0.003779 | 0.003090 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 10 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0015` | `feedforward` | 0.003310 | 0.004062 | 0.002985 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 11 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0007` | `feedforward` | 0.003317 | 0.003936 | 0.002962 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_feedforward_high_compute` | `feedforward` | 0.003319 | 0.003915 | 0.003198 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 13 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0010` | `feedforward` | 0.003333 | 0.003989 | 0.003038 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 14 | `te_feedforward_high_epoch` | `feedforward` | 0.003335 | 0.003767 | 0.003007 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_feedforward_stride1_long_large_batch` | `feedforward` | 0.003358 | 0.003769 | 0.003104 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_feedforward_best_training` | `feedforward` | 0.003409 | 0.003948 | 0.003039 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0013` | `feedforward` | 0.003409 | 0.003947 | 0.003009 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 18 | `te_feedforward_stride10_long_large_batch_big_model` | `feedforward` | 0.003413 | 0.004063 | 0.003040 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 19 | `te_feedforward_stride10_long_large_batch` | `feedforward` | 0.003433 | 0.004123 | 0.003066 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 20 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0006` | `feedforward` | 0.003436 | 0.003857 | 0.003044 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 21 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0003` | `feedforward` | 0.003441 | 0.003868 | 0.003073 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 22 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0000` | `feedforward` | 0.003446 | 0.003871 | 0.003010 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 23 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0001` | `feedforward` | 0.003446 | 0.004158 | 0.002958 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 24 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0016` | `feedforward` | 0.003465 | 0.004147 | 0.002998 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 25 | `te_feedforward_stride5_long_large_batch_big_model` | `feedforward` | 0.003472 | 0.004004 | 0.003104 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 26 | `te_feedforward_stride10_long` | `feedforward` | 0.003483 | 0.004050 | 0.003053 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 27 | `te_feedforward_baseline` | `feedforward` | 0.003504 | 0.003969 | 0.003148 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 28 | `te_feedforward_high_density` | `feedforward` | 0.003519 | 0.004046 | 0.003077 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 29 | `te_feedforward_trial` | `feedforward` | 0.003535 | 0.004211 | 0.003618 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 30 | `te_feedforward_high_compute_long_remote` | `feedforward` | 0.003542 | 0.004228 | 0.003058 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 31 | `te_feedforward_stride5_long` | `feedforward` | 0.003580 | 0.004008 | 0.003178 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 32 | `te_feedforward_stride1_long` | `feedforward` | 0.003646 | 0.003990 | 0.003126 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 33 | `te_feedforward_trial` | `feedforward` | 0.003671 | 0.004418 | 0.003706 | 26,241 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |

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

- Best run: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5`
- Best test MAE: `0.020774`
- Completed tracked runs: `16`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.020774 | 0.022412 | 0.017025 | 150 | 12m 41s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 2 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0001_stride1` | `harmonic_regression` | 0.020775 | 0.022417 | 0.017013 | 150 | 22m 40s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 3 | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.020779 | 0.022403 | 0.017017 | 150 | 14m 04s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr00005_stride1` | `harmonic_regression` | 0.020781 | 0.022419 | 0.017021 | 102 | 27m 40s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 5 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0002_stride1` | `harmonic_regression` | 0.020781 | 0.022433 | 0.017009 | 150 | 15m 59s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride1` | `harmonic_regression` | 0.020782 | 0.022414 | 0.017019 | 150 | 27m 18s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 7 | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 0.020782 | 0.022405 | 0.017004 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 8 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0002_stride5` | `harmonic_regression` | 0.020783 | 0.022411 | 0.017003 | 150 | 11m 30s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 9 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr00005_stride5` | `harmonic_regression` | 0.020785 | 0.022420 | 0.017019 | 102 | 12m 51s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 10 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0001_stride5` | `harmonic_regression` | 0.020791 | 0.022414 | 0.017003 | 102 | 18m 56s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 11 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0001_stride1` | `harmonic_regression` | 0.020791 | 0.022416 | 0.017001 | 102 | 21m 28s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 12 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0001_stride5` | `harmonic_regression` | 0.020793 | 0.022416 | 0.017007 | 150 | 16m 41s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 13 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0002_stride5` | `harmonic_regression` | 0.020794 | 0.022423 | 0.016993 | 102 | 10m 36s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 14 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0002_stride1` | `harmonic_regression` | 0.020800 | 0.022409 | 0.016980 | 102 | 14m 53s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 15 | `te_harmonic_order12_static_recovery` | `harmonic_regression` | 0.039404 | 0.042797 | 0.040524 | 25 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 16 | `te_harmonic_order06_static_recovery` | `harmonic_regression` | 0.039406 | 0.042796 | 0.040529 | 13 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |

#### periodic_mlp

- Best run: `te_periodic_mlp_h04_standard_global_optuna_t0010`
- Best test MAE: `0.003186`
- Completed tracked runs: `22`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 0.003690 | 0.002994 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_periodic_mlp_h04_standard_global_optuna_t0008` | `periodic_mlp` | 0.003200 | 0.003798 | 0.003057 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_periodic_mlp_h04_standard_global_optuna_t0006` | `periodic_mlp` | 0.003233 | 0.003733 | 0.002964 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_periodic_mlp_h04_standard_global_optuna_t0015` | `periodic_mlp` | 0.003280 | 0.003873 | 0.003064 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_periodic_mlp_h04_standard_global_optuna_t0012` | `periodic_mlp` | 0.003290 | 0.003786 | 0.003011 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_periodic_mlp_h04_standard_global_optuna_t0009` | `periodic_mlp` | 0.003301 | 0.003818 | 0.003120 | 37,249 | N/A | 0.45 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003317 | 0.003793 | 0.003097 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_periodic_mlp_h04_standard_global_optuna_t0000` | `periodic_mlp` | 0.003321 | 0.003732 | 0.003131 | 44,033 | N/A | 0.53 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_periodic_mlp_h04_standard_global_optuna_t0007` | `periodic_mlp` | 0.003339 | 0.003858 | 0.003049 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_periodic_mlp_h04_standard_global_optuna_t0017` | `periodic_mlp` | 0.003344 | 0.003830 | 0.002996 | 44,545 | N/A | 0.54 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_periodic_mlp_h04_standard_global_optuna_t0003` | `periodic_mlp` | 0.003344 | 0.003713 | 0.003162 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_periodic_mlp_h04_standard_global_optuna_t0002` | `periodic_mlp` | 0.003348 | 0.003779 | 0.003088 | 44,033 | N/A | 0.53 MB | Medium | Unknown | `standalone_or_unknown` |
| 13 | `te_periodic_mlp_h04_standard_global` | `periodic_mlp` | 0.003349 | 0.003916 | 0.002985 | 27,265 | 24m 13s | 0.33 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 14 | `te_periodic_mlp_h08_standard` | `periodic_mlp` | 0.003395 | 0.003951 | 0.003086 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_periodic_mlp_h04_standard_global_optuna_t0014` | `periodic_mlp` | 0.003402 | 0.003880 | 0.002992 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_periodic_mlp_h04_standard_global_optuna_t0013` | `periodic_mlp` | 0.003441 | 0.003949 | 0.002988 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_periodic_mlp_h04_standard_global_optuna_t0004` | `periodic_mlp` | 0.003478 | 0.003973 | 0.003047 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 18 | `te_periodic_mlp_h04_standard_global_optuna_t0016` | `periodic_mlp` | 0.003517 | 0.004068 | 0.003111 | 45,697 | N/A | 0.54 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_periodic_mlp_h04_standard_global_optuna_t0001` | `periodic_mlp` | 0.003531 | 0.004168 | 0.003062 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 20 | `te_periodic_mlp_h08_wide` | `periodic_mlp` | 0.003590 | 0.004143 | 0.003089 | 47,745 | N/A | 0.57 MB | Medium | Unknown | `standalone_or_unknown` |
| 21 | `te_periodic_mlp_h04_standard_global_optuna_t0005` | `periodic_mlp` | 0.003685 | 0.004266 | 0.003098 | 38,017 | N/A | 0.46 MB | Medium | Unknown | `standalone_or_unknown` |
| 22 | `te_periodic_mlp_h04_standard_global_optuna_t0011` | `periodic_mlp` | 0.003696 | 0.004227 | 0.003056 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |

#### residual_harmonic_mlp

- Best run: `te_residual_h12_deep_joint_wave1_global_optuna_t0006`
- Best test MAE: `0.003034`
- Completed tracked runs: `38`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 0.003550 | 0.002895 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_residual_h12_deep_joint_wave1_global_optuna_t0010` | `residual_harmonic_mlp` | 0.003067 | 0.003568 | 0.002903 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 0.003640 | 0.003024 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_deep_joint_wave1_global_optuna_t0004` | `residual_harmonic_mlp` | 0.003226 | 0.003744 | 0.003010 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_h12_small_joint_high_dropout_wave1` | `residual_harmonic_mlp` | 0.003230 | 0.003704 | 0.003001 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 6 | `te_residual_h12_deep_joint_wave1_global_optuna_t0002` | `residual_harmonic_mlp` | 0.003236 | 0.003625 | 0.003021 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_residual_h12_deep_joint_wave1_global_optuna_t0009` | `residual_harmonic_mlp` | 0.003252 | 0.003769 | 0.003019 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_residual_h12_deep_joint_wave1_global_optuna_t0005` | `residual_harmonic_mlp` | 0.003257 | 0.003790 | 0.003075 | 34,978 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_residual_h12_deep_joint_wave1_global_optuna_t0007` | `residual_harmonic_mlp` | 0.003273 | 0.003849 | 0.002937 | 26,274 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_residual_h16_small_joint_wave1` | `residual_harmonic_mlp` | 0.003274 | 0.003747 | 0.003020 | 4,898 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 11 | `te_residual_h12_wide_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | 0.003278 | 0.003814 | 0.002924 | 17,946 | N/A | 0.22 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | `residual_harmonic_mlp` | 0.003302 | 0.003909 | 0.002935 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 13 | `te_residual_h12_deep_joint_wave1_global_optuna_t0001` | `residual_harmonic_mlp` | 0.003305 | 0.003914 | 0.003052 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_residual_h12_small_joint_low_dropout_wave1` | `residual_harmonic_mlp` | 0.003359 | 0.003852 | 0.003027 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 15 | `te_residual_h12_small_joint_no_layer_norm_wave1` | `residual_harmonic_mlp` | 0.003360 | 0.003835 | 0.003089 | 4,634 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 16 | `te_residual_h12_deep_dense_remote` | `residual_harmonic_mlp` | 0.003365 | 0.003868 | 0.003018 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_residual_h12_small_frozen_wave1` | `residual_harmonic_mlp` | 0.003368 | 0.003898 | 0.003036 | 4,865 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 18 | `te_residual_h12_deep_joint_wave1_global_optuna_t0003` | `residual_harmonic_mlp` | 0.003371 | 0.003740 | 0.003040 | 43,674 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_residual_h12_wide_joint_wave1` | `residual_harmonic_mlp` | 0.003376 | 0.003906 | 0.002884 | 17,946 | N/A | 0.22 MB | Medium | Unknown | `standalone_or_unknown` |
| 20 | `te_residual_h12_deep_joint_wave1_global_optuna_t0013` | `residual_harmonic_mlp` | 0.003377 | 0.003933 | 0.002978 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 21 | `te_residual_h12_deep_joint_wave1_global_optuna_t0015` | `residual_harmonic_mlp` | 0.003382 | 0.003983 | 0.002958 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 22 | `te_residual_h12_deep_long_remote` | `residual_harmonic_mlp` | 0.003384 | 0.003908 | 0.002973 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 23 | `te_residual_h08_small_frozen_wave1` | `residual_harmonic_mlp` | 0.003384 | 0.003912 | 0.003007 | 4,865 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 24 | `te_residual_h08_small_joint_wave1` | `residual_harmonic_mlp` | 0.003385 | 0.003862 | 0.003030 | 4,882 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 25 | `te_residual_h12_deep_joint_wave1_global_optuna_t0012` | `residual_harmonic_mlp` | 0.003389 | 0.003870 | 0.003002 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 26 | `te_residual_h12_deep_joint_wave1_global_optuna_t0014` | `residual_harmonic_mlp` | 0.003403 | 0.003961 | 0.002963 | 26,274 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 27 | `te_residual_h12_medium_joint_wave1` | `residual_harmonic_mlp` | 0.003406 | 0.003863 | 0.002968 | 9,498 | N/A | 0.13 MB | Low | Unknown | `standalone_or_unknown` |
| 28 | `te_residual_h12_small_joint_dense_wave1` | `residual_harmonic_mlp` | 0.003410 | 0.003790 | 0.002962 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 29 | `te_residual_h12_deep_joint_wave1_global` | `residual_harmonic_mlp` | 0.003420 | 0.003931 | 0.003115 | 26,266 | 20m 35s | 0.32 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 30 | `te_residual_h12_deep_joint_wave1_global_optuna_t0011` | `residual_harmonic_mlp` | 0.003428 | 0.003928 | 0.002868 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 31 | `te_residual_h12_deep_joint_wave1_global_optuna_t0008` | `residual_harmonic_mlp` | 0.003443 | 0.004085 | 0.002963 | 43,674 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 32 | `te_residual_h12_small_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | 0.003465 | 0.003944 | 0.002987 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 33 | `te_residual_h12_small_joint_recovery` | `residual_harmonic_mlp` | 0.003466 | 0.003967 | 0.003016 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 34 | `te_residual_h12_deep_joint_wave1_global_optuna_t0017` | `residual_harmonic_mlp` | 0.003506 | 0.004031 | 0.003096 | 43,034 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 35 | `te_residual_h12_small_frozen_recovery` | `residual_harmonic_mlp` | 0.003554 | 0.004061 | 0.003030 | 4,865 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 36 | `te_residual_h12_small_joint_anchor_wave1` | `residual_harmonic_mlp` | 0.003557 | 0.004064 | 0.003090 | 4,890 | N/A | 0.07 MB | Low | Unknown | `standalone_or_unknown` |
| 37 | `te_residual_h12_deep_joint_wave1_global_optuna_t0016` | `residual_harmonic_mlp` | 0.003559 | 0.004077 | 0.003075 | 43,666 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 38 | `te_residual_h12_deep_joint_wave1_global_optuna_t0000` | `residual_harmonic_mlp` | 0.003569 | 0.004019 | 0.003179 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |

#### tree

- Best run: `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10`
- Best test MAE: `0.002782`
- Completed tracked runs: `24`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | 1m 26s | 0.48 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 2 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf20` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | 1m 26s | 0.48 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 3 | `te_hist_gbr_tabular_global_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.002830 | 0.003585 | 0.002677 | 5 | 1m 27s | 0.50 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 4 | `te_hist_gbr_tabular_global_grid_depth8_lr008_leaf20` | `hist_gradient_boosting` | 0.002830 | 0.003585 | 0.002677 | 5 | 1m 27s | 0.50 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 5 | `te_hist_gbr_tabular_global_grid_depth10_lr005_leaf10` | `hist_gradient_boosting` | 0.002844 | 0.003584 | 0.002712 | 5 | 1m 38s | 0.61 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 6 | `te_hist_gbr_tabular_global_grid_depth10_lr005_leaf20` | `hist_gradient_boosting` | 0.002844 | 0.003584 | 0.002712 | 5 | 1m 39s | 0.61 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 7 | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | N/A | 0.62 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 8 | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | 2m 01s | 0.62 MB | Light Artifact | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 9 | `te_hist_gbr_tabular_global_grid_depth8_lr005_leaf10` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | 1m 39s | 0.62 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 10 | `te_hist_gbr_tabular_global_grid_depth8_lr005_leaf20` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | 1m 41s | 0.62 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 11 | `te_hist_gbr_tabular_global_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002911 | 0.003617 | 0.002607 | 5 | 1m 25s | 0.49 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 12 | `te_hist_gbr_tabular_global_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002911 | 0.003617 | 0.002607 | 5 | 1m 27s | 0.49 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 13 | `te_hist_gbr_remote_deep` | `hist_gradient_boosting` | 0.002920 | 0.003644 | 0.002749 | 5 | N/A | 0.91 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 14 | `te_hist_gbr_tabular_global_grid_depth6_lr005_leaf10` | `hist_gradient_boosting` | 0.002926 | 0.003638 | 0.002681 | 5 | 1m 43s | 0.68 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 15 | `te_hist_gbr_tabular_global_grid_depth6_lr005_leaf20` | `hist_gradient_boosting` | 0.002926 | 0.003638 | 0.002681 | 5 | 1m 43s | 0.68 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 16 | `te_hist_gbr_tabular_global_grid_depth10_lr003_leaf10` | `hist_gradient_boosting` | 0.002938 | 0.003652 | 0.002754 | 5 | 2m 09s | 0.91 MB | Light Artifact | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 17 | `te_hist_gbr_tabular_global_grid_depth10_lr003_leaf20` | `hist_gradient_boosting` | 0.002938 | 0.003652 | 0.002754 | 5 | 2m 04s | 0.91 MB | Light Artifact | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 18 | `te_hist_gbr_tabular_global_grid_depth8_lr003_leaf10` | `hist_gradient_boosting` | 0.002956 | 0.003664 | 0.002758 | 5 | 2m 01s | 0.88 MB | Light Artifact | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 19 | `te_hist_gbr_tabular_global_grid_depth8_lr003_leaf20` | `hist_gradient_boosting` | 0.002956 | 0.003664 | 0.002758 | 5 | 2m 01s | 0.88 MB | Light Artifact | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 20 | `te_hist_gbr_tabular_global_grid_depth6_lr003_leaf10` | `hist_gradient_boosting` | 0.003086 | 0.003753 | 0.002746 | 5 | 2m 18s | 0.82 MB | Light Artifact | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 21 | `te_hist_gbr_tabular_global_grid_depth6_lr003_leaf20` | `hist_gradient_boosting` | 0.003086 | 0.003753 | 0.002746 | 5 | 1m 56s | 0.82 MB | Light Artifact | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 22 | `te_hist_gbr_remote_refined` | `hist_gradient_boosting` | 0.003101 | 0.003781 | 0.002809 | 5 | N/A | 0.84 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 23 | `te_random_forest_tabular_recovery` | `random_forest` | 0.003833 | 0.004809 | 0.003792 | 5 | N/A | 7.09 GB | Extreme Artifact | Unknown | `standalone_or_unknown` |
| 24 | `te_random_forest_remote_medium` | `random_forest` | 0.003865 | 0.004861 | 0.003808 | 5 | N/A | 85.40 GB | Extreme Artifact | Unknown | `standalone_or_unknown` |

### Forward Models

#### feedforward_fw

- Best run: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008`
- Best test MAE: `0.003203`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.003203 | 0.003787 | 0.002850 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0009` | `feedforward` | 0.003229 | 0.003774 | 0.002850 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0014` | `feedforward` | 0.003232 | 0.003812 | 0.002846 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0010` | `feedforward` | 0.003232 | 0.003798 | 0.002817 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0011` | `feedforward` | 0.003268 | 0.003909 | 0.002855 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0003` | `feedforward` | 0.003280 | 0.003903 | 0.002821 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 7 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0005` | `feedforward` | 0.003287 | 0.003911 | 0.002746 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0002` | `feedforward` | 0.003301 | 0.003958 | 0.002904 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 9 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0013` | `feedforward` | 0.003357 | 0.004017 | 0.002824 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0007` | `feedforward` | 0.003364 | 0.003893 | 0.002856 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0012` | `feedforward` | 0.003366 | 0.004020 | 0.002778 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0017` | `feedforward` | 0.003372 | 0.004017 | 0.002815 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 13 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0015` | `feedforward` | 0.003420 | 0.003873 | 0.002871 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0016` | `feedforward` | 0.003449 | 0.004134 | 0.002877 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 15 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0001` | `feedforward` | 0.003467 | 0.004121 | 0.002801 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0004` | `feedforward` | 0.003482 | 0.004095 | 0.002894 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 17 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0000` | `feedforward` | 0.003487 | 0.003928 | 0.002838 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 18 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0006` | `feedforward` | 0.003531 | 0.003990 | 0.002807 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_feedforward_stride1_high_compute_long_remote_Fw` | `feedforward` | 0.003563 | 0.004009 | 0.002915 | 109,953 | 25m 08s | 1.28 MB | High | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |

#### harmonic_regression_fw

- Best run: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride5`
- Best test MAE: `0.003101`
- Completed tracked runs: `13`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride5` | `harmonic_regression` | 0.003101 | 0.003527 | 0.002848 | 102 | 9m 52s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 2 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.003102 | 0.003528 | 0.002843 | 150 | 10m 25s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 3 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr00005_stride1` | `harmonic_regression` | 0.003105 | 0.003534 | 0.002839 | 150 | 18m 46s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr0001_stride5` | `harmonic_regression` | 0.003111 | 0.003538 | 0.002842 | 150 | 8m 00s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 5 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr0001_stride1` | `harmonic_regression` | 0.003114 | 0.003549 | 0.002825 | 150 | 14m 06s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr0002_stride5` | `harmonic_regression` | 0.003118 | 0.003549 | 0.002800 | 102 | 9m 06s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 7 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr0002_stride1` | `harmonic_regression` | 0.003121 | 0.003553 | 0.002799 | 102 | 9m 43s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 8 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr0001_stride1` | `harmonic_regression` | 0.003127 | 0.003558 | 0.002827 | 102 | 11m 09s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 9 | `te_harmonic_order12_linear_conditioned_recovery_Fw` | `harmonic_regression` | 0.003129 | 0.003567 | 0.002811 | 150 | 10m 50s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 10 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr0001_stride5` | `harmonic_regression` | 0.003136 | 0.003577 | 0.002808 | 102 | 11m 30s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 11 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr0002_stride5` | `harmonic_regression` | 0.003144 | 0.003582 | 0.002779 | 150 | 9m 53s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 12 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride1` | `harmonic_regression` | 0.003155 | 0.003626 | 0.002831 | 102 | 10m 19s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 13 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr0002_stride1` | `harmonic_regression` | 0.003187 | 0.003656 | 0.002792 | 150 | 11m 50s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |

#### periodic_mlp_fw

- Best run: `te_periodic_mlp_h04_standard_Fw_optuna_t0008`
- Best test MAE: `0.003287`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_Fw_optuna_t0008` | `periodic_mlp` | 0.003287 | 0.003833 | 0.002809 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_periodic_mlp_h04_standard_Fw_optuna_t0001` | `periodic_mlp` | 0.003294 | 0.003899 | 0.002751 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_periodic_mlp_h04_standard_Fw_optuna_t0015` | `periodic_mlp` | 0.003296 | 0.003924 | 0.002802 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_periodic_mlp_h04_standard_Fw_optuna_t0012` | `periodic_mlp` | 0.003299 | 0.003876 | 0.002832 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_periodic_mlp_h04_standard_Fw_optuna_t0017` | `periodic_mlp` | 0.003308 | 0.003834 | 0.002807 | 44,545 | N/A | 0.54 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_periodic_mlp_h04_standard_Fw_optuna_t0009` | `periodic_mlp` | 0.003320 | 0.003934 | 0.002834 | 37,249 | N/A | 0.45 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_periodic_mlp_h04_standard_Fw_optuna_t0002` | `periodic_mlp` | 0.003323 | 0.003753 | 0.002845 | 44,033 | N/A | 0.53 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_periodic_mlp_h04_standard_Fw_optuna_t0006` | `periodic_mlp` | 0.003338 | 0.003969 | 0.002792 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_periodic_mlp_h04_standard_Fw_optuna_t0016` | `periodic_mlp` | 0.003365 | 0.003905 | 0.002897 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_periodic_mlp_h04_standard_Fw_optuna_t0007` | `periodic_mlp` | 0.003367 | 0.003987 | 0.002803 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_periodic_mlp_h04_standard_Fw_optuna_t0010` | `periodic_mlp` | 0.003368 | 0.004043 | 0.002803 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_periodic_mlp_h04_standard_Fw_optuna_t0013` | `periodic_mlp` | 0.003372 | 0.003950 | 0.002791 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 13 | `te_periodic_mlp_h04_standard_Fw_optuna_t0011` | `periodic_mlp` | 0.003414 | 0.004019 | 0.002807 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_periodic_mlp_h04_standard_Fw_optuna_t0004` | `periodic_mlp` | 0.003420 | 0.004025 | 0.002760 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_periodic_mlp_h04_standard_Fw_optuna_t0003` | `periodic_mlp` | 0.003421 | 0.003888 | 0.002786 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_periodic_mlp_h04_standard_Fw_optuna_t0005` | `periodic_mlp` | 0.003428 | 0.004078 | 0.002851 | 38,017 | N/A | 0.46 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_periodic_mlp_h04_standard_Fw` | `periodic_mlp` | 0.003432 | 0.004023 | 0.002848 | 27,265 | 11m 04s | 0.33 MB | Medium | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 18 | `te_periodic_mlp_h04_standard_Fw_optuna_t0014` | `periodic_mlp` | 0.003448 | 0.004036 | 0.002768 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_periodic_mlp_h04_standard_Fw_optuna_t0000` | `periodic_mlp` | 0.003574 | 0.004022 | 0.002864 | 44,033 | N/A | 0.53 MB | Medium | Unknown | `standalone_or_unknown` |

#### residual_harmonic_mlp_fw

- Best run: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0005`
- Best test MAE: `0.003168`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0005` | `residual_harmonic_mlp` | 0.003168 | 0.003871 | 0.002870 | 34,978 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0006` | `residual_harmonic_mlp` | 0.003194 | 0.003809 | 0.002827 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0009` | `residual_harmonic_mlp` | 0.003211 | 0.003828 | 0.002794 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0007` | `residual_harmonic_mlp` | 0.003215 | 0.003831 | 0.002829 | 26,274 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0012` | `residual_harmonic_mlp` | 0.003241 | 0.003814 | 0.002827 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0015` | `residual_harmonic_mlp` | 0.003252 | 0.003737 | 0.002890 | 34,978 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0010` | `residual_harmonic_mlp` | 0.003294 | 0.003867 | 0.002814 | 34,962 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0001` | `residual_harmonic_mlp` | 0.003328 | 0.003963 | 0.002806 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0011` | `residual_harmonic_mlp` | 0.003354 | 0.003995 | 0.002759 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0013` | `residual_harmonic_mlp` | 0.003373 | 0.003941 | 0.002792 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0008` | `residual_harmonic_mlp` | 0.003376 | 0.003960 | 0.002883 | 43,674 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0017` | `residual_harmonic_mlp` | 0.003389 | 0.004062 | 0.002829 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 13 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0003` | `residual_harmonic_mlp` | 0.003402 | 0.003838 | 0.002998 | 43,674 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0002` | `residual_harmonic_mlp` | 0.003473 | 0.003940 | 0.002839 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0014` | `residual_harmonic_mlp` | 0.003505 | 0.004202 | 0.002835 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0004` | `residual_harmonic_mlp` | 0.003527 | 0.004142 | 0.002810 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0000` | `residual_harmonic_mlp` | 0.003529 | 0.003975 | 0.002901 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 18 | `te_residual_h12_deep_joint_wave1_Fw` | `residual_harmonic_mlp` | 0.003530 | 0.004145 | 0.002852 | 26,266 | 10m 41s | 0.32 MB | Medium | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 19 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0016` | `residual_harmonic_mlp` | 0.003620 | 0.004317 | 0.002856 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |

#### tree_fw

- Best run: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10`
- Best test MAE: `0.002743`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | 1m 03s | 0.45 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 2 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | 1m 00s | 0.45 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 3 | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002845 | 0.003476 | 0.002666 | 5 | 1m 10s | 0.50 MB | Very Low | Very Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 4 | `te_hist_gbr_tabular_Fw_grid_depth8_lr005_leaf10` | `hist_gradient_boosting` | 0.002845 | 0.003476 | 0.002666 | 5 | 1m 03s | 0.50 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 5 | `te_hist_gbr_tabular_Fw_grid_depth8_lr005_leaf20` | `hist_gradient_boosting` | 0.002845 | 0.003476 | 0.002666 | 5 | 1m 03s | 0.50 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 6 | `te_hist_gbr_tabular_Fw_grid_depth6_lr005_leaf10` | `hist_gradient_boosting` | 0.002857 | 0.003465 | 0.002674 | 5 | 1m 02s | 0.46 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 7 | `te_hist_gbr_tabular_Fw_grid_depth6_lr005_leaf20` | `hist_gradient_boosting` | 0.002857 | 0.003465 | 0.002674 | 5 | 1m 04s | 0.46 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 8 | `te_hist_gbr_tabular_Fw_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.002861 | 0.003514 | 0.002605 | 5 | 59s | 0.41 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 9 | `te_hist_gbr_tabular_Fw_grid_depth8_lr008_leaf20` | `hist_gradient_boosting` | 0.002861 | 0.003514 | 0.002605 | 5 | 59s | 0.41 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 10 | `te_hist_gbr_tabular_Fw_grid_depth10_lr005_leaf10` | `hist_gradient_boosting` | 0.002866 | 0.003488 | 0.002601 | 5 | 1m 05s | 0.53 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 11 | `te_hist_gbr_tabular_Fw_grid_depth10_lr005_leaf20` | `hist_gradient_boosting` | 0.002866 | 0.003488 | 0.002601 | 5 | 1m 04s | 0.53 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 12 | `te_hist_gbr_tabular_Fw_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002889 | 0.003551 | 0.002653 | 5 | 58s | 0.38 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 13 | `te_hist_gbr_tabular_Fw_grid_depth10_lr008_leaf20` | `hist_gradient_boosting` | 0.002889 | 0.003551 | 0.002653 | 5 | 58s | 0.38 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 14 | `te_hist_gbr_tabular_Fw_grid_depth6_lr003_leaf10` | `hist_gradient_boosting` | 0.002918 | 0.003520 | 0.002722 | 5 | 1m 12s | 0.68 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 15 | `te_hist_gbr_tabular_Fw_grid_depth6_lr003_leaf20` | `hist_gradient_boosting` | 0.002918 | 0.003520 | 0.002722 | 5 | 1m 11s | 0.68 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 16 | `te_hist_gbr_tabular_Fw_grid_depth10_lr003_leaf10` | `hist_gradient_boosting` | 0.002931 | 0.003547 | 0.002655 | 5 | 1m 13s | 0.73 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 17 | `te_hist_gbr_tabular_Fw_grid_depth10_lr003_leaf20` | `hist_gradient_boosting` | 0.002931 | 0.003547 | 0.002655 | 5 | 1m 13s | 0.73 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 18 | `te_hist_gbr_tabular_Fw_grid_depth8_lr003_leaf10` | `hist_gradient_boosting` | 0.002960 | 0.003549 | 0.002697 | 5 | 1m 12s | 0.71 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 19 | `te_hist_gbr_tabular_Fw_grid_depth8_lr003_leaf20` | `hist_gradient_boosting` | 0.002960 | 0.003549 | 0.002697 | 5 | 1m 13s | 0.71 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |

### Backward Models

#### feedforward_bw

- Best run: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005`
- Best test MAE: `0.003099`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003099 | 0.003630 | 0.003018 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0013` | `feedforward` | 0.003106 | 0.003700 | 0.002989 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0016` | `feedforward` | 0.003173 | 0.003818 | 0.002901 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 4 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0015` | `feedforward` | 0.003224 | 0.003684 | 0.003056 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 5 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0011` | `feedforward` | 0.003234 | 0.003775 | 0.002941 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 6 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0002` | `feedforward` | 0.003243 | 0.003964 | 0.003035 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 7 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0014` | `feedforward` | 0.003243 | 0.003830 | 0.002905 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 8 | `te_feedforward_stride1_high_compute_long_remote_Bw` | `feedforward` | 0.003262 | 0.003749 | 0.003049 | 109,953 | 1h 08m 06s | 1.28 MB | High | High | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 9 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0012` | `feedforward` | 0.003263 | 0.003822 | 0.002962 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 10 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0000` | `feedforward` | 0.003276 | 0.003767 | 0.002875 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 11 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0001` | `feedforward` | 0.003286 | 0.004043 | 0.002997 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0010` | `feedforward` | 0.003320 | 0.003818 | 0.002994 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 13 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0007` | `feedforward` | 0.003358 | 0.003837 | 0.003095 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 14 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0004` | `feedforward` | 0.003383 | 0.004006 | 0.003009 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 15 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0003` | `feedforward` | 0.003388 | 0.004143 | 0.002976 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 16 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0008` | `feedforward` | 0.003401 | 0.004012 | 0.002936 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 17 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0006` | `feedforward` | 0.003434 | 0.003947 | 0.002959 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 18 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0009` | `feedforward` | 0.003486 | 0.003963 | 0.003061 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0017` | `feedforward` | 0.003499 | 0.004114 | 0.003136 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |

#### harmonic_regression_bw

- Best run: `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5`
- Best test MAE: `0.003494`
- Completed tracked runs: `13`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5` | `harmonic_regression` | 0.003494 | 0.004081 | 0.003638 | 102 | 10m 58s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 2 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr00005_stride1` | `harmonic_regression` | 0.003497 | 0.004053 | 0.003743 | 102 | 13m 24s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 3 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.003506 | 0.004063 | 0.003729 | 150 | 10m 53s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr0001_stride1` | `harmonic_regression` | 0.003513 | 0.004076 | 0.003691 | 150 | 22m 26s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 5 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr00005_stride1` | `harmonic_regression` | 0.003514 | 0.004067 | 0.003732 | 150 | 20m 08s | 0.01 MB | Very Low | Medium | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr0001_stride5` | `harmonic_regression` | 0.003516 | 0.004081 | 0.003691 | 150 | 9m 21s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 7 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0001_stride5` | `harmonic_regression` | 0.003516 | 0.004076 | 0.003697 | 102 | 10m 55s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 8 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr00005_stride5` | `harmonic_regression` | 0.003517 | 0.004063 | 0.003747 | 102 | 10m 20s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 9 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr0002_stride5` | `harmonic_regression` | 0.003519 | 0.004100 | 0.003603 | 150 | 10m 59s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 10 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0001_stride1` | `harmonic_regression` | 0.003524 | 0.004077 | 0.003710 | 102 | 12m 45s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 11 | `te_harmonic_order12_linear_conditioned_recovery_Bw` | `harmonic_regression` | 0.003524 | 0.004080 | 0.003701 | 150 | 8m 57s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 12 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr0002_stride1` | `harmonic_regression` | 0.003525 | 0.004111 | 0.003603 | 150 | 13m 10s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 13 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride1` | `harmonic_regression` | 0.003565 | 0.004148 | 0.003609 | 102 | 12m 23s | 0.01 MB | Very Low | Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |

#### periodic_mlp_bw

- Best run: `te_periodic_mlp_h04_standard_Bw_optuna_t0006`
- Best test MAE: `0.003233`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.003233 | 0.003792 | 0.002907 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_periodic_mlp_h04_standard_Bw_optuna_t0007` | `periodic_mlp` | 0.003239 | 0.003820 | 0.002933 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_periodic_mlp_h04_standard_Bw_optuna_t0010` | `periodic_mlp` | 0.003248 | 0.003817 | 0.002963 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_periodic_mlp_h04_standard_Bw_optuna_t0011` | `periodic_mlp` | 0.003271 | 0.003889 | 0.003058 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_periodic_mlp_h04_standard_Bw_optuna_t0009` | `periodic_mlp` | 0.003318 | 0.003889 | 0.003140 | 37,249 | N/A | 0.45 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_periodic_mlp_h04_standard_Bw_optuna_t0013` | `periodic_mlp` | 0.003329 | 0.003896 | 0.002925 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_periodic_mlp_h04_standard_Bw_optuna_t0015` | `periodic_mlp` | 0.003363 | 0.004052 | 0.003104 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_periodic_mlp_h04_standard_Bw_optuna_t0001` | `periodic_mlp` | 0.003386 | 0.004135 | 0.003082 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_periodic_mlp_h04_standard_Bw_optuna_t0008` | `periodic_mlp` | 0.003402 | 0.004096 | 0.003135 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_periodic_mlp_h04_standard_Bw_optuna_t0002` | `periodic_mlp` | 0.003412 | 0.003891 | 0.003183 | 44,033 | N/A | 0.53 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_periodic_mlp_h04_standard_Bw_optuna_t0014` | `periodic_mlp` | 0.003466 | 0.004092 | 0.003038 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_periodic_mlp_h04_standard_Bw_optuna_t0000` | `periodic_mlp` | 0.003479 | 0.003912 | 0.003313 | 44,033 | N/A | 0.53 MB | Medium | Unknown | `standalone_or_unknown` |
| 13 | `te_periodic_mlp_h04_standard_Bw_optuna_t0004` | `periodic_mlp` | 0.003498 | 0.004066 | 0.002995 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_periodic_mlp_h04_standard_Bw` | `periodic_mlp` | 0.003525 | 0.004132 | 0.003154 | 27,265 | 15m 06s | 0.33 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 15 | `te_periodic_mlp_h04_standard_Bw_optuna_t0017` | `periodic_mlp` | 0.003532 | 0.004158 | 0.003211 | 44,545 | N/A | 0.54 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_periodic_mlp_h04_standard_Bw_optuna_t0012` | `periodic_mlp` | 0.003589 | 0.004257 | 0.003061 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_periodic_mlp_h04_standard_Bw_optuna_t0005` | `periodic_mlp` | 0.003599 | 0.004241 | 0.003159 | 38,017 | N/A | 0.46 MB | Medium | Unknown | `standalone_or_unknown` |
| 18 | `te_periodic_mlp_h04_standard_Bw_optuna_t0016` | `periodic_mlp` | 0.003656 | 0.004282 | 0.003221 | 47,745 | N/A | 0.57 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_periodic_mlp_h04_standard_Bw_optuna_t0003` | `periodic_mlp` | 0.003669 | 0.004130 | 0.003194 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |

#### residual_harmonic_mlp_bw

- Best run: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0007`
- Best test MAE: `0.003162`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0007` | `residual_harmonic_mlp` | 0.003162 | 0.003862 | 0.002948 | 34,962 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0012` | `residual_harmonic_mlp` | 0.003180 | 0.003642 | 0.002979 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0013` | `residual_harmonic_mlp` | 0.003195 | 0.003636 | 0.003051 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0002` | `residual_harmonic_mlp` | 0.003206 | 0.003720 | 0.003087 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0011` | `residual_harmonic_mlp` | 0.003223 | 0.003657 | 0.003000 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0000` | `residual_harmonic_mlp` | 0.003266 | 0.003727 | 0.002935 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0009` | `residual_harmonic_mlp` | 0.003267 | 0.003810 | 0.002997 | 43,666 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 8 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0017` | `residual_harmonic_mlp` | 0.003271 | 0.003738 | 0.003075 | 43,666 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 9 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0004` | `residual_harmonic_mlp` | 0.003296 | 0.003884 | 0.003060 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 10 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0006` | `residual_harmonic_mlp` | 0.003358 | 0.004051 | 0.002993 | 34,978 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 11 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0001` | `residual_harmonic_mlp` | 0.003360 | 0.004083 | 0.002993 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 12 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0010` | `residual_harmonic_mlp` | 0.003366 | 0.003996 | 0.002950 | 34,962 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 13 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0015` | `residual_harmonic_mlp` | 0.003426 | 0.004125 | 0.003008 | 43,042 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0016` | `residual_harmonic_mlp` | 0.003442 | 0.003857 | 0.003091 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0005` | `residual_harmonic_mlp` | 0.003454 | 0.003918 | 0.002930 | 34,962 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0014` | `residual_harmonic_mlp` | 0.003467 | 0.003952 | 0.002954 | 34,962 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_residual_h12_deep_joint_wave1_Bw` | `residual_harmonic_mlp` | 0.003493 | 0.004108 | 0.003110 | 26,266 | 15m 03s | 0.32 MB | Medium | Medium | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 18 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0003` | `residual_harmonic_mlp` | 0.003532 | 0.004006 | 0.003043 | 43,674 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 19 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0008` | `residual_harmonic_mlp` | 0.003641 | 0.004137 | 0.002970 | 34,978 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |

#### tree_bw

- Best run: `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10`
- Best test MAE: `0.002954`
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | 1m 00s | 0.45 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 2 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | 1m 01s | 0.45 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 3 | `te_hist_gbr_tabular_Bw_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.003002 | 0.003809 | 0.002650 | 5 | 1m 01s | 0.44 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 4 | `te_hist_gbr_tabular_Bw_grid_depth8_lr008_leaf20` | `hist_gradient_boosting` | 0.003002 | 0.003809 | 0.002650 | 5 | 1m 01s | 0.44 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 5 | `te_hist_gbr_tabular_Bw_grid_depth10_lr005_leaf10` | `hist_gradient_boosting` | 0.003015 | 0.003814 | 0.002748 | 5 | 1m 07s | 0.56 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 6 | `te_hist_gbr_tabular_Bw_grid_depth10_lr005_leaf20` | `hist_gradient_boosting` | 0.003015 | 0.003814 | 0.002748 | 5 | 1m 06s | 0.56 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 7 | `te_hist_gbr_tabular_Bw_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.003023 | 0.003834 | 0.002738 | 5 | 1m 00s | 0.41 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 8 | `te_hist_gbr_tabular_Bw_grid_depth10_lr008_leaf20` | `hist_gradient_boosting` | 0.003023 | 0.003834 | 0.002738 | 5 | 1m 00s | 0.41 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 9 | `te_hist_gbr_tabular_Bw_grid_depth6_lr005_leaf10` | `hist_gradient_boosting` | 0.003038 | 0.003810 | 0.002704 | 5 | 1m 06s | 0.58 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 10 | `te_hist_gbr_tabular_Bw_grid_depth6_lr005_leaf20` | `hist_gradient_boosting` | 0.003038 | 0.003810 | 0.002704 | 5 | 1m 07s | 0.58 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 11 | `te_hist_gbr_tabular_Bw` | `hist_gradient_boosting` | 0.003087 | 0.003850 | 0.002698 | 5 | 1m 12s | 0.50 MB | Very Low | Very Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 12 | `te_hist_gbr_tabular_Bw_grid_depth8_lr005_leaf10` | `hist_gradient_boosting` | 0.003087 | 0.003850 | 0.002698 | 5 | 1m 05s | 0.50 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 13 | `te_hist_gbr_tabular_Bw_grid_depth8_lr005_leaf20` | `hist_gradient_boosting` | 0.003087 | 0.003850 | 0.002698 | 5 | 1m 04s | 0.50 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 14 | `te_hist_gbr_tabular_Bw_grid_depth10_lr003_leaf10` | `hist_gradient_boosting` | 0.003146 | 0.003920 | 0.002737 | 5 | 1m 14s | 0.73 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 15 | `te_hist_gbr_tabular_Bw_grid_depth10_lr003_leaf20` | `hist_gradient_boosting` | 0.003146 | 0.003920 | 0.002737 | 5 | 1m 14s | 0.73 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 16 | `te_hist_gbr_tabular_Bw_grid_depth8_lr003_leaf10` | `hist_gradient_boosting` | 0.003216 | 0.003995 | 0.002782 | 5 | 1m 11s | 0.65 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 17 | `te_hist_gbr_tabular_Bw_grid_depth8_lr003_leaf20` | `hist_gradient_boosting` | 0.003216 | 0.003995 | 0.002782 | 5 | 1m 11s | 0.65 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 18 | `te_hist_gbr_tabular_Bw_grid_depth6_lr003_leaf10` | `hist_gradient_boosting` | 0.003250 | 0.004024 | 0.002843 | 5 | 1m 11s | 0.64 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |
| 19 | `te_hist_gbr_tabular_Bw_grid_depth6_lr003_leaf20` | `hist_gradient_boosting` | 0.003250 | 0.004024 | 0.002843 | 5 | 1m 10s | 0.64 MB | Very Low | Very Low | `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11` |

## Source Of Truth

- Live backlog: `doc/running/te_model_live_backlog.md`
- Active campaign state: `doc/running/active_training_campaign.yaml`
- Program registry: `output/registries/program/current_best_solution.yaml`
- Family registries root: `output/registries/families`
- Training campaign root: `output/training_campaigns`
- Training run root: `output/training_runs`
- Paper reference report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

This document is repository-generated. Regenerate it after new campaign results so the cross-family snapshot stays aligned with the canonical registries and campaign artifacts.
