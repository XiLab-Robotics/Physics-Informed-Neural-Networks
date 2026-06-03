# Training Results Master Summary

## Executive Snapshot

- Generated At: `2026-05-28T11:42:23`
- Program State: active.
- Current Completed Wave: `Wave 2C` residual harmonic temporal hybrid campaign and official `Track 2` refresh complete.
- Current Focus: use completed `Track 2E` offset-predictability feasibility
  labels to prepare the next direction-parallel offset-aware training or
  calibration branch.
- Active Campaign Status: `none`
- Active Campaign Name: `None`
- Current Scalar Registry Winner: `te_periodic_gru_sequence_remote_Bw` |
  Family `periodic_gru_sequence_bw` | Test MAE `0.002344`
- Current Curve-First Promotion State: `Track 2B` reranking, screened
  `Track 2C` curve-payload diagnostics, `Track 2` mean-centered collage
  diagnostics, `Track 2D` full-matrix mean-offset audit, and `Track 2E`
  offset-predictability feasibility complete; no automatic single-winner
  registry promotion.
- Runtime Input Constraint: point-level operating state, optional short causal
  history, or derived causal features only.

## Main Takeaways

- Strongest current neural family: `periodic_gru_sequence_bw`
- Latest Track 2 decision: `Wave 2C` sparse `RCIM` residual harmonic temporal
  models are verified exploratory baselines, not promoted over `Wave 2B`.
- New selection direction: future best-model promotion must keep three
  parallel surfaces, not one single competition: `Fw`, `Bw`, and `global`.
  The first standardized reranking favors `rcim_retuned_GBM19_Fw` forward,
  `rcim_retuned_GBM19_Bw` backward, and `periodic_lstm_sequence_global` on
  the global surface.
- New diagnostic direction: `Track 2D` evaluated `111` candidates over
  `12,416` curves and confirms that many candidates are offset-limited. The
  global surface leader is `periodic_gru_sequence_global`, while the strongest
  forward diagnostic leader remains `rcim_retuned_GBM19_Fw`.
- New feasibility direction: `Track 2E` excludes exact full-condition
  memorization and finds `direction_torque` as the strongest conservative
  causal offset grouping. The next branch should compare post-hoc offset
  baselines, sequential residual-offset modeling, and multi-head shape/offset
  losses per `Fw`, `Bw`, and `global` surface.
- Current plain MLP anchor: `te_feedforward_stride1_high_compute_long_remote_global`
- Active family-improvement branch count: `0`
- Implemented and benchmarked family count: `53`

## Current Project Status

### Implemented And Benchmarked Families

- Multi-scope waves must keep `global`, `Fw`, and `Bw` reporting surfaces separated in this canonical summary.

#### Global Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence` | Implemented Benchmark | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.002681 | 157,953 | `2026-05-25 17:27:07` |
| `periodic_lstm_sequence` | Implemented Benchmark | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002682 | 210,561 | `2026-05-25 19:20:56` |
| `tree` | Implemented Benchmark | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002782 | 5 | `2026-05-11 20:38:56` |
| `residual_harmonic_mlp` | Implemented Benchmark | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 26,266 | `2026-05-20 11:41:03` |
| `feedforward` | Current Plain MLP Anchor | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 109,953 | `2026-05-13 13:25:56` |
| `periodic_mlp` | Implemented Benchmark | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 27,265 | `2026-05-21 08:12:57` |
| `residual_harmonic_lstm_sequence_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003368 | 201,364 | `2026-05-27 20:55:58` |
| `residual_harmonic_gru_sequence_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003440 | 151,060 | `2026-05-27 19:07:31` |
| `residual_harmonic_lstm_sequence_dense240` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence` | 0.003473 | 201,826 | `2026-05-27 21:22:30` |
| `residual_harmonic_lstm_sequence_dense360` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence` | 0.003477 | 202,066 | `2026-05-27 22:09:01` |
| `lstm_sequence` | Implemented Benchmark | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003482 | 201,345 | `2026-05-24 12:16:30` |
| `periodic_temporal_convolution` | Implemented Benchmark | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | 0.003508 | 158,529 | `2026-05-25 16:10:13` |
| `residual_harmonic_gru_sequence_dense240` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence` | 0.003511 | 151,522 | `2026-05-27 19:32:17` |
| `residual_harmonic_gru_sequence_dense360` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence` | 0.003535 | 151,762 | `2026-05-27 20:21:50` |
| `gru_sequence` | Implemented Benchmark | `te_gru_sequence_remote_global` | `gru_sequence` | 0.003591 | 151,041 | `2026-05-24 11:54:03` |
| `temporal_convolution` | Implemented Benchmark | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | 0.003754 | 147,009 | `2026-05-24 11:30:23` |
| `feedforward_recovery_micro` | Implemented Benchmark | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004164 | 109,953 | `2026-05-12 11:12:51` |
| `feedforward_recovery_probe_dense` | Implemented Benchmark | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004602 | 109,953 | `2026-05-12 17:16:41` |
| `harmonic_regression` | Implemented Benchmark | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | 0.020767 | 114 | `2026-05-20 10:32:21` |

#### Forward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `tree_fw` | Implemented Benchmark | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002743 | 5 | `2026-05-11 20:58:32` |
| `harmonic_regression_fw` | Implemented Benchmark | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002916 | 4,326 | `2026-05-20 10:50:22` |
| `periodic_mlp_fw` | Implemented Benchmark | `te_periodic_mlp_dense240_tracking_Fw` | `periodic_mlp` | 0.003055 | 87,681 | `2026-05-21 08:48:01` |
| `residual_harmonic_mlp_fw` | Implemented Benchmark | `te_residual_harmonic_rcim_sparse_tracking_Fw` | `residual_harmonic_mlp` | 0.003089 | 26,260 | `2026-05-20 11:57:15` |
| `periodic_gru_sequence_fw` | Implemented Benchmark | `te_periodic_gru_sequence_remote_Fw` | `periodic_gru_sequence` | 0.003193 | 157,953 | `2026-05-25 17:38:18` |
| `residual_harmonic_gru_sequence_fw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003200 | 151,060 | `2026-05-27 19:12:38` |
| `feedforward_fw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.003203 | 109,953 | `2026-05-14 22:03:06` |
| `residual_harmonic_gru_sequence_fw_dense240` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | `residual_harmonic_gru_sequence` | 0.003219 | 151,522 | `2026-05-27 19:40:30` |
| `residual_harmonic_lstm_sequence_fw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003234 | 201,364 | `2026-05-27 21:00:48` |
| `residual_harmonic_gru_sequence_fw_dense360` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | `residual_harmonic_gru_sequence` | 0.003241 | 151,762 | `2026-05-27 20:33:03` |
| `residual_harmonic_lstm_sequence_fw_dense240` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | `residual_harmonic_lstm_sequence` | 0.003262 | 201,826 | `2026-05-27 21:29:55` |
| `periodic_lstm_sequence_fw` | Implemented Benchmark | `te_periodic_lstm_sequence_remote_Fw` | `periodic_lstm_sequence` | 0.003274 | 210,561 | `2026-05-25 19:30:17` |
| `gru_sequence_fw` | Implemented Benchmark | `te_gru_sequence_remote_Fw` | `gru_sequence` | 0.003333 | 151,041 | `2026-05-24 12:00:05` |
| `periodic_temporal_convolution_fw` | Implemented Benchmark | `te_periodic_temporal_convolution_sequence_remote_Fw` | `periodic_temporal_convolution` | 0.003337 | 158,529 | `2026-05-25 16:18:28` |
| `residual_harmonic_lstm_sequence_fw_dense360` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | `residual_harmonic_lstm_sequence` | 0.003351 | 202,066 | `2026-05-27 22:19:22` |
| `lstm_sequence_fw` | Implemented Benchmark | `te_lstm_sequence_remote_Fw` | `lstm_sequence` | 0.003370 | 201,345 | `2026-05-24 12:21:01` |
| `temporal_convolution_fw` | Implemented Benchmark | `te_temporal_convolution_sequence_remote_Fw` | `temporal_convolution` | 0.003611 | 147,009 | `2026-05-24 11:37:07` |

#### Backward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence_bw` | Current Program Winner | `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence` | 0.002344 | 157,953 | `2026-05-25 18:09:44` |
| `periodic_lstm_sequence_bw` | Implemented Benchmark | `te_periodic_lstm_sequence_remote_Bw` | `periodic_lstm_sequence` | 0.002556 | 210,561 | `2026-05-25 20:05:38` |
| `tree_bw` | Implemented Benchmark | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002954 | 5 | `2026-05-11 21:18:29` |
| `residual_harmonic_mlp_bw` | Implemented Benchmark | `te_residual_harmonic_rcim_sparse_tracking_Bw` | `residual_harmonic_mlp` | 0.003042 | 26,260 | `2026-05-20 12:25:49` |
| `feedforward_bw` | Implemented Benchmark | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003099 | 167,937 | `2026-05-14 13:49:53` |
| `periodic_mlp_bw` | Implemented Benchmark | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.003233 | 27,777 | `2026-05-21 09:38:37` |
| `harmonic_regression_bw` | Implemented Benchmark | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003400 | 2,886 | `2026-05-20 11:08:01` |
| `residual_harmonic_lstm_sequence_bw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003440 | 201,364 | `2026-05-27 21:08:36` |
| `residual_harmonic_gru_sequence_bw_dense360` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | `residual_harmonic_gru_sequence` | 0.003468 | 151,762 | `2026-05-27 20:46:25` |
| `residual_harmonic_gru_sequence_bw_dense240` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | `residual_harmonic_gru_sequence` | 0.003492 | 151,522 | `2026-05-27 20:00:10` |
| `residual_harmonic_gru_sequence_bw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003502 | 151,060 | `2026-05-27 19:18:56` |
| `residual_harmonic_lstm_sequence_bw_dense360` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | `residual_harmonic_lstm_sequence` | 0.003556 | 202,066 | `2026-05-27 22:35:20` |
| `lstm_sequence_bw` | Implemented Benchmark | `te_lstm_sequence_remote_Bw` | `lstm_sequence` | 0.003557 | 201,345 | `2026-05-24 12:27:31` |
| `residual_harmonic_lstm_sequence_bw_dense240` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | `residual_harmonic_lstm_sequence` | 0.003605 | 201,826 | `2026-05-27 21:40:13` |
| `periodic_temporal_convolution_bw` | Implemented Benchmark | `te_periodic_temporal_convolution_sequence_remote_Bw` | `periodic_temporal_convolution` | 0.003614 | 158,529 | `2026-05-25 16:26:53` |
| `gru_sequence_bw` | Implemented Benchmark | `te_gru_sequence_remote_Bw` | `gru_sequence` | 0.003631 | 151,041 | `2026-05-24 12:06:34` |
| `temporal_convolution_bw` | Implemented Benchmark | `te_temporal_convolution_sequence_remote_Bw` | `temporal_convolution` | 0.003739 | 147,009 | `2026-05-24 11:45:19` |

### Active Training Or Improvement Branches

- No campaign is currently in `prepared` or `running` state.
- The next active implementation branch should therefore be read from the live backlog focus and the next approved campaign plan.

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
| Track 2. Directional Offline Comparison | direction-aware loader and candidate matrix: completed;; recovered original forward candidates: included;; retuned forward and backward candidates: included;; `Track 1` forward and backward candidates: included;; `Wave 1`, `Wave 2`, `Wave 2B`, and `Wave 2C` registry candidates: included;; grouped source tables: completed;; composite best-reference visibility: completed;; visual reports refreshed through `Wave 2C`;; official model-verification report: completed;; `Track 2B` curve-first reranking: completed;; `Track 2C` curve-payload diagnostics: completed;; mean-centered collage diagnostic: completed;; `Track 2D` mean-offset full-matrix audit: completed;; `Track 2E` offset-predictability feasibility: completed;; next decision: plan a direction-parallel offset-aware probe comparing post-hoc, sequential, and multi-head interventions;; status: closed as official baseline, with diagnostic extensions active. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 2. Temporal Models | status: entry campaign completed; closeout report prepared; official; initial families: `temporal_convolution`, `gru_sequence`, `lstm_sequence`;; configuration root: `config/training/hydra/wave2/`;; preliminary campaign plan:; closeout report:; campaign winner: `te_gru_sequence_remote_Fw` from family; refresh plan:; official verification report:; Track 2 decision: verified exploratory baselines, not promoted over `tree`;; mandatory rule: prepare or justify `global`, `forward`, and `backward`; baseline comparison: Track 2 plus closed Wave 1. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 2B. Harmonic Temporal Hybrid Models | status: harmonic-temporal hybrid campaign completed; normal closeout report; families: `periodic_temporal_convolution`, `periodic_gru_sequence`, `periodic_lstm_sequence`;; campaign winner: `te_periodic_gru_sequence_remote_Bw` from family `periodic_gru_sequence_bw`;; strongest bidirectional candidate: `te_periodic_gru_sequence_remote_global`;; Track 2 decision: strongest current repository-owned neural branch;; mandatory rule: prepare or justify `global`, `forward`, and `backward`; baseline comparison: official Track 2 matrix plus visual reports. |
| Wave 2C. Residual Harmonic Temporal Hybrid Models | status: residual harmonic temporal hybrid campaign and official Track 2 refresh completed;; families: `residual_harmonic_gru_sequence`, `residual_harmonic_lstm_sequence` with sparse `RCIM`, dense `240`, and dense `360` harmonic banks;; campaign winner: `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim`;; strongest Track 2 Wave 2C candidates: `residual_harmonic_gru_sequence_sparse_rcim_Fw`, `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, and `residual_harmonic_lstm_sequence_sparse_rcim_global`;; Track 2 decision: verified exploratory baseline, not promoted over `Wave 2B` periodic sequence leaders. |

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
| `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` | `2026-05-27 22:35:20` | 18 | 0 | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | Updated residual_harmonic_gru_sequence_fw_sparse_rcim family best |
| `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` | `2026-05-25 20:05:38` | 9 | 0 | `te_periodic_gru_sequence_remote_Bw` | Updated global best |
| `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` | `2026-05-24 12:27:31` | 9 | 0 | `te_gru_sequence_remote_Fw` | Updated gru_sequence_fw family best |
| `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` | `2026-05-21 09:38:37` | 9 | 0 | `te_periodic_mlp_dense240_tracking_Fw` | Updated periodic_mlp_fw family best |
| `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` | `2026-05-20 12:25:49` | 18 | 0 | `te_harmonic_dense360_tracking_Fw` | Updated harmonic_regression_fw family best |

## Ranking Policy

- Scalar registry primary metric: `test_mae`
- Scalar registry first tie-breaker: `test_rmse`
- Scalar registry second tie-breaker: `val_mae`
- Scalar registry third tie-breaker: `trainable_parameter_count`
- Direction: `minimize`

Curve-first promotion policy:

- scalar registry ranking remains a required sanity surface;
- deployment-relevant promotion must also pass Track 2 direction-valid
  full-curve evaluation;
- full curves are evaluation and aggregation units, not future inputs supplied
  to the model at inference time;
- future deployed models must keep causal inputs: current point, optional past
  history, and causal derived features;
- completed curve-first analysis now separates `Fw`, `Bw`, and `global`
  leaders instead of one single winner;
- completed mean-centered diagnostics now separate curve-bias error from
  centered waveform-shape error;
- future Track 2 diagnostics should report raw error, explicit `DC` / curve
  offset error, centered-shape error, amplitude error, and harmonic phase
  error as separate quantities;
- spectral or non-`DC` harmonic metrics are useful shape diagnostics, but they
  must not replace the explicit offset term;
- candidate promotion should keep scalar, curve-first, and deployment-ready
  evidence separated for each surface until Track 3 online compensation
  evidence exists.

## Best Result Per Family

- Scope-separated family ranking is mandatory for every future wave that introduces more than one canonical training surface.

### Global Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `periodic_gru_sequence` | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.002507 | 0.002681 | 0.002971 | 157,953 | 1.82 MB | High | Implemented Benchmark |
| `periodic_lstm_sequence` | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002526 | 0.002682 | 0.002969 | 210,561 | 2.43 MB | High | Implemented Benchmark |
| `tree` | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002655 | 0.002782 | 0.003520 | 5 | 0.48 MB | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.002895 | 0.003034 | 0.003550 | 26,266 | 0.32 MB | Unknown | Implemented Benchmark |
| `feedforward` | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003056 | 0.003150 | 0.003603 | 109,953 | 1.28 MB | Unknown | Current Plain MLP Anchor |
| `periodic_mlp` | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.002994 | 0.003186 | 0.003690 | 27,265 | 0.33 MB | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003632 | 0.003368 | 0.003808 | 201,364 | 2.32 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003607 | 0.003440 | 0.003848 | 151,060 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense240` | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence` | 0.003624 | 0.003473 | 0.003925 | 201,826 | 2.33 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense360` | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence` | 0.003648 | 0.003477 | 0.003940 | 202,066 | 2.33 MB | Medium | Implemented Benchmark |
| `lstm_sequence` | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003681 | 0.003482 | 0.003948 | 201,345 | 2.32 MB | Low | Implemented Benchmark |
| `periodic_temporal_convolution` | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | 0.003634 | 0.003508 | 0.003929 | 158,529 | 1.83 MB | Medium | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense240` | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence` | 0.003600 | 0.003511 | 0.003983 | 151,522 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense360` | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence` | 0.003628 | 0.003535 | 0.003999 | 151,762 | 1.75 MB | Medium | Implemented Benchmark |
| `gru_sequence` | `te_gru_sequence_remote_global` | `gru_sequence` | 0.003707 | 0.003591 | 0.004110 | 151,041 | 1.74 MB | Low | Implemented Benchmark |
| `temporal_convolution` | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | 0.003935 | 0.003754 | 0.004266 | 147,009 | 1.70 MB | Low | Implemented Benchmark |
| `feedforward_recovery_micro` | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004266 | 0.004164 | 0.005109 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `feedforward_recovery_probe_dense` | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004257 | 0.004602 | 0.005262 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `harmonic_regression` | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | 0.016995 | 0.020767 | 0.022376 | 114 | 0.01 MB | Low | Implemented Benchmark |

### Forward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `tree_fw` | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002677 | 0.002743 | 0.003409 | 5 | 0.45 MB | Unknown | Implemented Benchmark |
| `harmonic_regression_fw` | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002610 | 0.002916 | 0.003237 | 4,326 | 0.06 MB | Low | Implemented Benchmark |
| `periodic_mlp_fw` | `te_periodic_mlp_dense240_tracking_Fw` | `periodic_mlp` | 0.002541 | 0.003055 | 0.003537 | 87,681 | 1.03 MB | Low | Implemented Benchmark |
| `residual_harmonic_mlp_fw` | `te_residual_harmonic_rcim_sparse_tracking_Fw` | `residual_harmonic_mlp` | 0.002704 | 0.003089 | 0.003498 | 26,260 | 0.32 MB | Low | Implemented Benchmark |
| `periodic_gru_sequence_fw` | `te_periodic_gru_sequence_remote_Fw` | `periodic_gru_sequence` | 0.003227 | 0.003193 | 0.003583 | 157,953 | 1.82 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_fw_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003309 | 0.003200 | 0.003635 | 151,060 | 1.75 MB | Low | Implemented Benchmark |
| `feedforward_fw` | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.002850 | 0.003203 | 0.003787 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_fw_dense240` | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | `residual_harmonic_gru_sequence` | 0.003270 | 0.003219 | 0.003653 | 151,522 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_fw_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003344 | 0.003234 | 0.003679 | 201,364 | 2.32 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_fw_dense360` | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | `residual_harmonic_gru_sequence` | 0.003265 | 0.003241 | 0.003677 | 151,762 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_fw_dense240` | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | `residual_harmonic_lstm_sequence` | 0.003307 | 0.003262 | 0.003706 | 201,826 | 2.33 MB | Low | Implemented Benchmark |
| `periodic_lstm_sequence_fw` | `te_periodic_lstm_sequence_remote_Fw` | `periodic_lstm_sequence` | 0.003254 | 0.003274 | 0.003651 | 210,561 | 2.43 MB | Low | Implemented Benchmark |
| `gru_sequence_fw` | `te_gru_sequence_remote_Fw` | `gru_sequence` | 0.003409 | 0.003333 | 0.003881 | 151,041 | 1.74 MB | Low | Implemented Benchmark |
| `periodic_temporal_convolution_fw` | `te_periodic_temporal_convolution_sequence_remote_Fw` | `periodic_temporal_convolution` | 0.003321 | 0.003337 | 0.003830 | 158,529 | 1.83 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_fw_dense360` | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | `residual_harmonic_lstm_sequence` | 0.003302 | 0.003351 | 0.003774 | 202,066 | 2.33 MB | Low | Implemented Benchmark |
| `lstm_sequence_fw` | `te_lstm_sequence_remote_Fw` | `lstm_sequence` | 0.003448 | 0.003370 | 0.003921 | 201,345 | 2.32 MB | Low | Implemented Benchmark |
| `temporal_convolution_fw` | `te_temporal_convolution_sequence_remote_Fw` | `temporal_convolution` | 0.003490 | 0.003611 | 0.004183 | 147,009 | 1.70 MB | Low | Implemented Benchmark |

### Backward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `periodic_gru_sequence_bw` | `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence` | 0.002523 | 0.002344 | 0.002747 | 157,953 | 1.82 MB | Medium | Current Program Winner |
| `periodic_lstm_sequence_bw` | `te_periodic_lstm_sequence_remote_Bw` | `periodic_lstm_sequence` | 0.002432 | 0.002556 | 0.002953 | 210,561 | 2.43 MB | Medium | Implemented Benchmark |
| `tree_bw` | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002681 | 0.002954 | 0.003749 | 5 | 0.45 MB | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_bw` | `te_residual_harmonic_rcim_sparse_tracking_Bw` | `residual_harmonic_mlp` | 0.002953 | 0.003042 | 0.003548 | 26,260 | 0.32 MB | Low | Implemented Benchmark |
| `feedforward_bw` | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003018 | 0.003099 | 0.003630 | 167,937 | 1.95 MB | Unknown | Implemented Benchmark |
| `periodic_mlp_bw` | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.002907 | 0.003233 | 0.003792 | 27,777 | 0.34 MB | Unknown | Implemented Benchmark |
| `harmonic_regression_bw` | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003588 | 0.003400 | 0.003886 | 2,886 | 0.04 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_bw_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003764 | 0.003440 | 0.004030 | 201,364 | 2.32 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_bw_dense360` | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | `residual_harmonic_gru_sequence` | 0.003773 | 0.003468 | 0.004050 | 151,762 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_bw_dense240` | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | `residual_harmonic_gru_sequence` | 0.003585 | 0.003492 | 0.004074 | 151,522 | 1.75 MB | Medium | Implemented Benchmark |
| `residual_harmonic_gru_sequence_bw_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003833 | 0.003502 | 0.004061 | 151,060 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_bw_dense360` | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | `residual_harmonic_lstm_sequence` | 0.003729 | 0.003556 | 0.004125 | 202,066 | 2.33 MB | Medium | Implemented Benchmark |
| `lstm_sequence_bw` | `te_lstm_sequence_remote_Bw` | `lstm_sequence` | 0.003815 | 0.003557 | 0.004201 | 201,345 | 2.32 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_bw_dense240` | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | `residual_harmonic_lstm_sequence` | 0.003742 | 0.003605 | 0.004129 | 201,826 | 2.33 MB | Low | Implemented Benchmark |
| `periodic_temporal_convolution_bw` | `te_periodic_temporal_convolution_sequence_remote_Bw` | `periodic_temporal_convolution` | 0.003890 | 0.003614 | 0.004163 | 158,529 | 1.83 MB | Low | Implemented Benchmark |
| `gru_sequence_bw` | `te_gru_sequence_remote_Bw` | `gru_sequence` | 0.003867 | 0.003631 | 0.004297 | 151,041 | 1.74 MB | Low | Implemented Benchmark |
| `temporal_convolution_bw` | `te_temporal_convolution_sequence_remote_Bw` | `temporal_convolution` | 0.003933 | 0.003739 | 0.004369 | 147,009 | 1.70 MB | Low | Implemented Benchmark |

## Cross-Family Interpretation

- Current scalar program-registry winner: `te_periodic_gru_sequence_remote_Bw` from family `periodic_gru_sequence_bw`.
- Current curve-first interpretation: maintain `Fw`, `Bw`, and `global`
  branches in parallel; do not collapse them into the scalar registry winner.
- Strongest practical screened neural `Bw` candidate: `periodic_gru_sequence_Bw`.
- Strongest practical screened neural `global` candidate: `periodic_lstm_sequence_global`.
- Forward branch status: current screened leader is paper-reference
  `rcim_retuned_GBM19_Fw`, so the repository-owned `Fw` branch remains open.
- Mean-offset interpretation: pointwise `MSE` and `RMSE` can favor a
  conditional-average prediction when the input features do not identify the
  curve-level offset. `Track 2D` now provides candidate-level labels for
  offset, centered shape, amplitude, phase, and condition dependence before
  retraining.
- Offset-predictability interpretation: `Track 2E` shows that conservative
  causal condition groupings, especially `direction_torque`, explain part of
  the offset but do not justify exact-condition memorization or automatic
  model promotion.
- `Wave 2C` is now Track 2 verified as exploratory evidence: sparse `RCIM`
  residual harmonic temporal models are the only competitive branch, but they
  do not displace `Wave 2B`.
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
| Offline model-selection direction | Boosting/tree-heavy deployed harmonic predictors | Repository now tracks `Fw`, `Bw`, and `global` best surfaces separately; strongest screened neural candidates are `periodic_gru_sequence_Bw` and `periodic_lstm_sequence_global` | partly_aligned |
| Strongest neural branch role | Neural models are evaluated, but not the primary deployed winners | Neural branches remain active per surface, while the current screened `Fw` leader is still paper-reference | aligned |
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
- Neural models remain secondary in the repository (`periodic_gru_sequence_bw`), which is also consistent with the paper not promoting a plain neural winner for deployment.
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

#### gru_sequence

- Best run: `te_gru_sequence_remote_global`
- Best test MAE: `0.003591`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_remote_global` | `gru_sequence` | 0.003591 | 0.004110 | 0.003707 | 151,041 | 8m 44s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

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

#### lstm_sequence

- Best run: `te_lstm_sequence_remote_global`
- Best test MAE: `0.003482`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003482 | 0.003948 | 0.003681 | 201,345 | 9m 56s | 2.32 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### periodic_gru_sequence

- Best run: `te_periodic_gru_sequence_remote_global`
- Best test MAE: `0.002681`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.002681 | 0.002971 | 0.002507 | 157,953 | 1h 00m 14s | 1.82 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_lstm_sequence

- Best run: `te_periodic_lstm_sequence_remote_global`
- Best test MAE: `0.002682`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002682 | 0.002969 | 0.002526 | 210,561 | 1h 11m 12s | 2.43 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

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

#### periodic_temporal_convolution

- Best run: `te_periodic_temporal_convolution_sequence_remote_global`
- Best test MAE: `0.003508`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | 0.003508 | 0.003929 | 0.003634 | 158,529 | 25m 37s | 1.83 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### residual_harmonic_gru_sequence_dense240

- Best run: `te_residual_harmonic_gru_sequence_remote_global_dense240`
- Best test MAE: `0.003511`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence` | 0.003511 | 0.003983 | 0.003600 | 151,522 | 13m 21s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_dense360

- Best run: `te_residual_harmonic_gru_sequence_remote_global_dense360`
- Best test MAE: `0.003535`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence` | 0.003535 | 0.003999 | 0.003628 | 151,762 | 21m 39s | 1.75 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_sparse_rcim

- Best run: `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim`
- Best test MAE: `0.003440`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003440 | 0.003848 | 0.003607 | 151,060 | 11m 44s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_dense240

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_dense240`
- Best test MAE: `0.003473`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence` | 0.003473 | 0.003925 | 0.003624 | 201,826 | 13m 54s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_dense360

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_dense360`
- Best test MAE: `0.003477`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence` | 0.003477 | 0.003940 | 0.003648 | 202,066 | 28m 49s | 2.33 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_sparse_rcim

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim`
- Best test MAE: `0.003368`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003368 | 0.003808 | 0.003632 | 201,364 | 9m 32s | 2.32 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

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

#### temporal_convolution

- Best run: `te_temporal_convolution_sequence_remote_global`
- Best test MAE: `0.003754`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | 0.003754 | 0.004266 | 0.003935 | 147,009 | 9m 46s | 1.70 MB | High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

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

#### gru_sequence_fw

- Best run: `te_gru_sequence_remote_Fw`
- Best test MAE: `0.003333`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_remote_Fw` | `gru_sequence` | 0.003333 | 0.003881 | 0.003409 | 151,041 | 6m 01s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

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

#### lstm_sequence_fw

- Best run: `te_lstm_sequence_remote_Fw`
- Best test MAE: `0.003370`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_lstm_sequence_remote_Fw` | `lstm_sequence` | 0.003370 | 0.003921 | 0.003448 | 201,345 | 4m 31s | 2.32 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### periodic_gru_sequence_fw

- Best run: `te_periodic_gru_sequence_remote_Fw`
- Best test MAE: `0.003193`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_remote_Fw` | `periodic_gru_sequence` | 0.003193 | 0.003583 | 0.003227 | 157,953 | 11m 11s | 1.82 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_lstm_sequence_fw

- Best run: `te_periodic_lstm_sequence_remote_Fw`
- Best test MAE: `0.003274`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_remote_Fw` | `periodic_lstm_sequence` | 0.003274 | 0.003651 | 0.003254 | 210,561 | 9m 20s | 2.43 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

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

#### periodic_temporal_convolution_fw

- Best run: `te_periodic_temporal_convolution_sequence_remote_Fw`
- Best test MAE: `0.003337`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_sequence_remote_Fw` | `periodic_temporal_convolution` | 0.003337 | 0.003830 | 0.003321 | 158,529 | 8m 15s | 1.83 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### residual_harmonic_gru_sequence_fw_dense240

- Best run: `te_residual_harmonic_gru_sequence_remote_Fw_dense240`
- Best test MAE: `0.003219`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | `residual_harmonic_gru_sequence` | 0.003219 | 0.003653 | 0.003270 | 151,522 | 8m 13s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_fw_dense360

- Best run: `te_residual_harmonic_gru_sequence_remote_Fw_dense360`
- Best test MAE: `0.003241`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | `residual_harmonic_gru_sequence` | 0.003241 | 0.003677 | 0.003265 | 151,762 | 11m 14s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_fw_sparse_rcim

- Best run: `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim`
- Best test MAE: `0.003200`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003200 | 0.003635 | 0.003309 | 151,060 | 5m 07s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_fw_dense240

- Best run: `te_residual_harmonic_lstm_sequence_remote_Fw_dense240`
- Best test MAE: `0.003262`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | `residual_harmonic_lstm_sequence` | 0.003262 | 0.003706 | 0.003307 | 201,826 | 7m 24s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_fw_dense360

- Best run: `te_residual_harmonic_lstm_sequence_remote_Fw_dense360`
- Best test MAE: `0.003351`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | `residual_harmonic_lstm_sequence` | 0.003351 | 0.003774 | 0.003302 | 202,066 | 10m 20s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_fw_sparse_rcim

- Best run: `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim`
- Best test MAE: `0.003234`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003234 | 0.003679 | 0.003344 | 201,364 | 4m 50s | 2.32 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

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

#### temporal_convolution_fw

- Best run: `te_temporal_convolution_sequence_remote_Fw`
- Best test MAE: `0.003611`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_temporal_convolution_sequence_remote_Fw` | `temporal_convolution` | 0.003611 | 0.004183 | 0.003490 | 147,009 | 6m 45s | 1.70 MB | High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

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

#### gru_sequence_bw

- Best run: `te_gru_sequence_remote_Bw`
- Best test MAE: `0.003631`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_remote_Bw` | `gru_sequence` | 0.003631 | 0.004297 | 0.003867 | 151,041 | 6m 29s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

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

#### lstm_sequence_bw

- Best run: `te_lstm_sequence_remote_Bw`
- Best test MAE: `0.003557`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_lstm_sequence_remote_Bw` | `lstm_sequence` | 0.003557 | 0.004201 | 0.003815 | 201,345 | 6m 29s | 2.32 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### periodic_gru_sequence_bw

- Best run: `te_periodic_gru_sequence_remote_Bw`
- Best test MAE: `0.002344`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence` | 0.002344 | 0.002747 | 0.002523 | 157,953 | 31m 26s | 1.82 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_lstm_sequence_bw

- Best run: `te_periodic_lstm_sequence_remote_Bw`
- Best test MAE: `0.002556`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_remote_Bw` | `periodic_lstm_sequence` | 0.002556 | 0.002953 | 0.002432 | 210,561 | 35m 21s | 2.43 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

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

#### periodic_temporal_convolution_bw

- Best run: `te_periodic_temporal_convolution_sequence_remote_Bw`
- Best test MAE: `0.003614`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_sequence_remote_Bw` | `periodic_temporal_convolution` | 0.003614 | 0.004163 | 0.003890 | 158,529 | 8m 25s | 1.83 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### residual_harmonic_gru_sequence_bw_dense240

- Best run: `te_residual_harmonic_gru_sequence_remote_Bw_dense240`
- Best test MAE: `0.003492`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | `residual_harmonic_gru_sequence` | 0.003492 | 0.004074 | 0.003585 | 151,522 | 19m 40s | 1.75 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_bw_dense360

- Best run: `te_residual_harmonic_gru_sequence_remote_Bw_dense360`
- Best test MAE: `0.003468`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | `residual_harmonic_gru_sequence` | 0.003468 | 0.004050 | 0.003773 | 151,762 | 13m 22s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_bw_sparse_rcim

- Best run: `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim`
- Best test MAE: `0.003502`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003502 | 0.004061 | 0.003833 | 151,060 | 6m 18s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_bw_dense240

- Best run: `te_residual_harmonic_lstm_sequence_remote_Bw_dense240`
- Best test MAE: `0.003605`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | `residual_harmonic_lstm_sequence` | 0.003605 | 0.004129 | 0.003742 | 201,826 | 10m 18s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_bw_dense360

- Best run: `te_residual_harmonic_lstm_sequence_remote_Bw_dense360`
- Best test MAE: `0.003556`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | `residual_harmonic_lstm_sequence` | 0.003556 | 0.004125 | 0.003729 | 202,066 | 15m 59s | 2.33 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_bw_sparse_rcim

- Best run: `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim`
- Best test MAE: `0.003440`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003440 | 0.004030 | 0.003764 | 201,364 | 7m 48s | 2.32 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

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

#### temporal_convolution_bw

- Best run: `te_temporal_convolution_sequence_remote_Bw`
- Best test MAE: `0.003739`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_temporal_convolution_sequence_remote_Bw` | `temporal_convolution` | 0.003739 | 0.004369 | 0.003933 | 147,009 | 8m 12s | 1.70 MB | High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

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
