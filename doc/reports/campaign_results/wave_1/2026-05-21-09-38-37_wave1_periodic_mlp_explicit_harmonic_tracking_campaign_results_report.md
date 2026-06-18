# Wave 1 Periodic MLP Explicit Harmonic Tracking Campaign Results

## Overview

This report closes the approved `Wave 1` periodic MLP explicit harmonic
tracking campaign. The campaign tested whether fixed sparse and dense harmonic
feature dictionaries improve the existing `periodic_mlp` family without
changing the pure `feedforward` baseline or redefining the future
`Fourier-Feature MLP` family.

The campaign completed all 9 planned runs with zero launcher failures. The
campaign winner by the configured selection policy, minimum `test_mae` with
`test_rmse`, `val_mae`, and parameter count as tie breakers, is
`te_periodic_mlp_dense240_tracking_Fw`.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42` |
| Campaign leaderboard | `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/wave_1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md` |
| Technical document | `doc/technical/2026-05/2026-05-20/2026-05-20-22-34-11_periodic_mlp_explicit_harmonic_basis.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| Started at | `2026-05-20T23:14:17` |
| Finished at | `2026-05-21T09:38:37` |
| Completed runs | 9 |
| Failed runs | 0 |
| Tested model type | `periodic_mlp` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Tested harmonic banks | `RCIM sparse`, `0..240`, `0..360` |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `te_periodic_mlp_dense240_tracking_Fw` |
| Run instance | `2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw` |
| Model family | `periodic_mlp_fw` |
| Model type | `periodic_mlp` |
| Direction scope | forward only |
| Harmonic bank | `0..240` |
| Trainable parameters | 87,681 |
| Validation MAE | 0.002541 |
| Validation RMSE | 0.003049 |
| Test MAE | 0.003055 |
| Test RMSE | 0.003537 |

The winning checkpoint is stored at
`output/training_runs/periodic_mlp_fw/2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw/checkpoints/periodic_mlp-epoch=039-val_mae=0.00254077.ckpt`.

## Leaderboard

| Rank | Run | Scope | Harmonics | Test MAE | Test RMSE | Params |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_dense240_tracking_Fw` | Fw | `0..240` | 0.003055 | 0.003537 | 87,681 |
| 2 | `te_periodic_mlp_rcim_sparse_tracking_Fw` | Fw | RCIM sparse | 0.003131 | 0.003578 | 28,545 |
| 3 | `te_periodic_mlp_dense360_tracking_Fw` | Fw | `0..360` | 0.003155 | 0.003680 | 118,401 |
| 4 | `te_periodic_mlp_rcim_sparse_tracking_global` | global | RCIM sparse | 0.003275 | 0.003726 | 28,545 |
| 5 | `te_periodic_mlp_dense240_tracking_global` | global | `0..240` | 0.003348 | 0.003862 | 87,681 |
| 6 | `te_periodic_mlp_rcim_sparse_tracking_Bw` | Bw | RCIM sparse | 0.003398 | 0.003922 | 28,545 |
| 7 | `te_periodic_mlp_dense360_tracking_global` | global | `0..360` | 0.003401 | 0.003831 | 118,401 |
| 8 | `te_periodic_mlp_dense240_tracking_Bw` | Bw | `0..240` | 0.003417 | 0.004005 | 87,681 |
| 9 | `te_periodic_mlp_dense360_tracking_Bw` | Bw | `0..360` | 0.003424 | 0.004006 | 118,401 |

## Technical Interpretation

The strongest new result is forward-only `periodic_mlp` with the dense `0..240`
fixed periodic-feature bank. It reaches test MAE 0.003055,
ahead of the forward RCIM sparse candidate at 0.003131 and the forward dense
`0..360` candidate at 0.003155.

The result does not create a universal improvement for every direction scope.
The global campaign candidates remain behind the previous global Optuna
`periodic_mlp` winner, and the backward campaign candidates remain behind the
previous backward Optuna winner. This suggests that simply increasing the
fixed harmonic dictionary is useful in the forward-only surface but is not a
drop-in replacement for the earlier tuned compact periodic MLP surfaces.

The dense `0..240` forward model is also much larger than the compact Optuna
periodic MLP baseline. It should therefore be treated as a stronger
curve-fidelity candidate, not as an automatic deployment promotion. The Track
2 curve-overlay workflow is still required to decide whether the extra
harmonic inputs recover visible TE oscillations or only improve scalar error
locally.

## Registry Effects

| Registry Scope | Current Family Best | Test MAE | Interpretation |
| --- | --- | --- | --- |
| `periodic_mlp` | `te_periodic_mlp_h04_standard_global_optuna_t0010` | 0.003186 | Previous Optuna best remains ahead |
| `periodic_mlp_fw` | `te_periodic_mlp_dense240_tracking_Fw` | 0.003055 | Updated by this campaign |
| `periodic_mlp_bw` | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | 0.003233 | Previous Optuna best remains ahead |

The current program-level winner remains the previously registered `tree_fw`
run with test MAE 0.002743. This closeout therefore does not promote a new
program-level best model for deployment.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all 9
runs completed, the leaderboard and best-run artifacts exist, and the relevant
family registries were refreshed.

From a modeling standpoint, the explicit harmonic periodic-feature extension
is worth keeping. The forward dense `0..240` result is the main candidate to
carry into visual validation. The global and backward high-order periodic MLP
candidates should not replace the existing compact Optuna-selected family
bests unless later curve-level evidence justifies the larger feature bank.

## Recommended Follow-Up

1. Generate Track 2 curve overlays for the forward dense `0..240`, forward
   RCIM sparse, and forward dense `0..360` periodic MLP candidates.
2. Compare the same curves against the existing `tree_fw` program winner and
   earlier compact `periodic_mlp_fw` Optuna baseline.
3. Promote no periodic MLP checkpoint until the overlay review confirms real
   oscillation tracking rather than scalar-only improvement.
4. Keep the future `Fourier-Feature MLP` family separate from this fixed
   engineered-feature `periodic_mlp` extension.
