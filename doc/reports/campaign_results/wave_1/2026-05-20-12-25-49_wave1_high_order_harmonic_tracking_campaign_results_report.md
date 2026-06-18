# Wave 1 High-Order Harmonic Tracking Campaign Results

## Overview

This report closes the approved `Wave 1` high-order harmonic tracking campaign.
The campaign tested whether explicit higher-order harmonic bases reduce the
over-smoothing observed in the earlier Wave 1 models.

The campaign completed all 18 planned runs with zero launcher failures. The
campaign winner by the configured selection policy, minimum `test_mae` with
`test_rmse`, `val_mae`, and parameter count as tie breakers, is
`te_harmonic_dense360_tracking_Fw`.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| Campaign leaderboard | `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/wave_1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md` |
| Technical document | `doc/technical/2026-05/2026-05-19/2026-05-19-17-32-08_wave1_high_order_harmonic_tracking.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| Started at | `2026-05-20T10:11:06+02:00` |
| Finished at | `2026-05-20T12:25:49+02:00` |
| Completed runs | 18 |
| Failed runs | 0 |
| Tested model types | `harmonic_regression`, `residual_harmonic_mlp` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Tested harmonic banks | `RCIM sparse`, `0..240`, `0..360` |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `te_harmonic_dense360_tracking_Fw` |
| Run instance | `2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw` |
| Model family | `harmonic_regression_fw` |
| Model type | `harmonic_regression` |
| Direction scope | forward only |
| Harmonic bank | dense `0..360` |
| Trainable parameters | 4,326 |
| Validation MAE | 0.002610 |
| Validation RMSE | 0.003057 |
| Test MAE | 0.002916 |
| Test RMSE | 0.003237 |

The winning checkpoint is stored at
`output/training_runs/harmonic_regression_fw/2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw/checkpoints/harmonic_regression-epoch=053-val_mae=0.00261006.ckpt`.

## Leaderboard

| Rank | Run | Scope | Harmonics | Test MAE | Test RMSE |
| --- | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_dense360_tracking_Fw` | Fw | `0..360` | 0.002916 | 0.003237 |
| 2 | `te_harmonic_dense240_tracking_Fw` | Fw | `0..240` | 0.002935 | 0.003239 |
| 3 | `te_harmonic_rcim_sparse_tracking_Fw` | Fw | RCIM sparse | 0.002943 | 0.003254 |
| 4 | `te_residual_harmonic_rcim_sparse_tracking_Bw` | Bw | RCIM sparse | 0.003042 | 0.003548 |
| 5 | `te_residual_harmonic_dense360_tracking_Bw` | Bw | `0..360` | 0.003068 | 0.003545 |
| 6 | `te_residual_harmonic_rcim_sparse_tracking_Fw` | Fw | RCIM sparse | 0.003089 | 0.003498 |
| 7 | `te_residual_harmonic_dense240_tracking_global` | global | `0..240` | 0.003162 | 0.003598 |
| 8 | `te_residual_harmonic_dense240_tracking_Bw` | Bw | `0..240` | 0.003188 | 0.003717 |
| 9 | `te_residual_harmonic_dense240_tracking_Fw` | Fw | `0..240` | 0.003304 | 0.003773 |
| 10 | `te_residual_harmonic_rcim_sparse_tracking_global` | global | RCIM sparse | 0.003378 | 0.003902 |
| 11 | `te_harmonic_dense240_tracking_Bw` | Bw | `0..240` | 0.003400 | 0.003886 |
| 12 | `te_harmonic_dense360_tracking_Bw` | Bw | `0..360` | 0.003403 | 0.003866 |
| 13 | `te_harmonic_rcim_sparse_tracking_Bw` | Bw | RCIM sparse | 0.003406 | 0.003894 |
| 14 | `te_residual_harmonic_dense360_tracking_global` | global | `0..360` | 0.003434 | 0.003957 |
| 15 | `te_residual_harmonic_dense360_tracking_Fw` | Fw | `0..360` | 0.003568 | 0.004118 |
| 16 | `te_harmonic_rcim_sparse_tracking_global` | global | RCIM sparse | 0.020767 | 0.022376 |
| 17 | `te_harmonic_dense360_tracking_global` | global | `0..360` | 0.020780 | 0.022399 |
| 18 | `te_harmonic_dense240_tracking_global` | global | `0..240` | 0.020787 | 0.022388 |

## Technical Interpretation

The strongest result is concentrated in the forward-only
`harmonic_regression` family. Dense `0..360` wins the campaign with test MAE
0.002916, followed very closely by dense `0..240` at 0.002935 and the RCIM
sparse bank at 0.002943. The absolute margin between dense `0..360` and RCIM
sparse is small, about 0.000027 test MAE, so the larger basis is useful in this
campaign but not a dramatic scalar-metric breakthrough.

The result is still direction dependent. The same direct harmonic-regression
form is weak in the global bidirectional setting, where all three global
harmonic-regression runs remain around 0.02077 test MAE. This confirms that the
direct harmonic basis should not be treated as a single global solution without
additional conditioning or direction separation.

The residual-harmonic family behaves differently. In backward-only scope, the
RCIM sparse residual model has the best test MAE at 0.003042, while dense
`0..360` has a slightly lower test RMSE and better validation metrics but a
higher test MAE. In global scope, dense `0..240` is the best high-order
residual candidate from this campaign at 0.003162 test MAE, but it does not
improve the already registered global residual-harmonic best run.

The campaign supports the original hypothesis only partially. Explicit
high-order harmonic bases improve the best new forward-only harmonic result and
provide a better mechanism for representing fast oscillatory components than a
smooth MLP-only predictor. However, scalar MAE and RMSE are not enough to prove
that the predicted transmission-error curves visually recover all harmonic
detail. The next validation step must be curve-overlay inspection on the Track
2 plotting workflow.

## Registry Effects

The campaign runner updated the family registries and campaign-level winner
artifacts. The most relevant effects are:

| Registry Scope | New Relevant Entry | Test MAE | Interpretation |
| --- | --- | --- | --- |
| `harmonic_regression_fw` | `te_harmonic_dense360_tracking_Fw` | 0.002916 | New forward harmonic family best |
| `harmonic_regression_bw` | `te_harmonic_dense240_tracking_Bw` | 0.003400 | New backward harmonic family best |
| `residual_harmonic_mlp_fw` | `te_residual_harmonic_rcim_sparse_tracking_Fw` | 0.003089 | New forward residual-harmonic candidate |
| `residual_harmonic_mlp_bw` | `te_residual_harmonic_rcim_sparse_tracking_Bw` | 0.003042 | New backward residual-harmonic family best |
| `harmonic_regression` | `te_harmonic_rcim_sparse_tracking_global` | 0.020767 | Best among weak global harmonic runs |

The current program-level winner remains the previously registered `tree_fw`
run with test MAE 0.002743. This closeout therefore does not promote a new
program-level best model for deployment.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all 18
runs completed, the leaderboard and best-run artifacts exist, and the family
registries were refreshed.

From a modeling standpoint, the high-order harmonic feature is worth keeping.
The strongest practical candidate from this campaign is
`te_harmonic_dense360_tracking_Fw`, with dense `0..240` and RCIM sparse close
enough to remain useful lower-complexity comparison points. No model from this
campaign should be exported or promoted as the program-level solution until the
Track 2 curve-overlay plots confirm that the high-frequency TE components are
actually tracked rather than merely improving aggregate error.

## Recommended Follow-Up

1. Generate Track 2 curve overlays for the top three forward harmonic runs:
   dense `0..360`, dense `0..240`, and RCIM sparse.
2. Compare local oscillation fidelity, not only MAE, against the existing
   `tree_fw` winner and the earlier Wave 1 smooth predictors.
3. If dense `0..360` visibly tracks the harmonics better, prepare a bounded
   promotion campaign focused on forward-only harmonic and hybrid candidates.
4. Keep the global harmonic-regression configuration out of promotion paths
   unless a better conditioned global formulation is introduced.
