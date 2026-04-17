# Track 1 Extended Overnight Campaign Results Report

## Overview

This report closes the extended `Track 1` campaign prepared in:

- `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-13-13-27-37_track1_extended_overnight_campaign_plan_report.md`

The package executed `48` repository-owned harmonic-wise validation runs
through one coordinated launcher:

- completed runs: `48`
- failed runs: `0`
- execution window: `2026-04-13T15:10:50+02:00` to `2026-04-13T16:00:30+02:00`
- campaign artifact root:
  `output/training_campaigns/track1_extended_overnight_campaign_2026_04_13_13_31_57/`

The extended batch was organized into six logical experiment blocks:

- `Campaign A`: wide low-order `HGBM` search
- `Campaign B`: heavy low-order `HGBM` escalation
- `Campaign C`: late-harmonic repair `HGBM`
- `Campaign D`: bridge joint `HGBM`
- `Campaign E`: engineered-feature `HGBM` controls
- `Campaign F`: `RandomForest` controls

## Objective And Outcome

The campaign had four practical questions:

1. can a much wider low-order search finally beat the current `Track 1` shared-evaluator reference;
2. can a heavier low-order budget outperform the lighter winners when the budget is increased aggressively;
3. can bridge runs that couple `h0/h1` with the late-harmonic cluster close the remaining gap better than isolated ladders;
4. do engineered terms or `RandomForest` recover enough value to re-enter the promotion discussion under a much broader budget.

Outcome:

- the batch completed successfully with `48/48` runs and no observed launcher failures;
- the best test mean percentage error improved from the previous repository best `8.774%` to `8.707%`;
- the improvement is real but still small, so the support branch for `Target A` remains `not_yet_met` against the paper threshold `4.7%`;
- the strongest alternatives are still `HGBM`, especially the bridge joint and late-repair blocks;
- the heavy low-order escalation did not beat the lighter wide winner, which means extra budget alone is not enough;
- engineered-term and `RandomForest` controls remained clearly non-promotable in this branch.

Primary `Track 1` interpretation:

- this campaign does not close `Track 1` by campaign-local winner selection;
- its value is to prioritize the next exact-paper table-repair actions;
- the canonical `Track 1` closure state must still be read from the exact-paper
  Tables `3-6` comparison report.

## Ranking Policy

The campaign winner uses the explicit ranking rule approved in the campaign
plan:

- eligible winner set: all completed runs that emit the shared offline evaluator;
- primary metric: `test_mean_percentage_error_pct`;
- first tie breaker: `test_curve_mae_deg`;
- second tie breaker: `test_curve_rmse_deg`;
- third tie breaker: lexical `run_name`;
- direction: minimize.

This policy is serialized under:

- `output/training_campaigns/track1_extended_overnight_campaign_2026_04_13_13_31_57/campaign_leaderboard.yaml`

## Ranked Completed Runs

<!-- markdownlint-disable MD013 -->
| Rank | Config | Block | Test MPE [%] | Curve MAE [deg] | Curve RMSE [deg] |
| ---: | --- | --- | ---: | ---: | ---: |
| `1` | `track1_hgbm_h01_wide_depth_2` | `A` | 8.707 | 0.002611 | 0.002810 |
| `2` | `track1_hgbm_h01_h162240_joint_balanced` | `D` | 8.720 | 0.002605 | 0.002802 |
| `3` | `track1_hgbm_h01_wide_depth_1` | `A` | 8.759 | 0.002614 | 0.002809 |
| `4` | `track1_hgbm_h01_h156162240_joint` | `D` | 8.768 | 0.002648 | 0.002844 |
| `5` | `track1_hgbm_h0181_h162240_joint` | `D` | 8.770 | 0.002647 | 0.002843 |
| `6` | `track1_hgbm_h014078_h162240_joint` | `D` | 8.772 | 0.002648 | 0.002844 |
| `7` | `track1_hgbm_h81156162240_cluster` | `C` | 8.778 | 0.002594 | 0.002790 |
| `8` | `track1_hgbm_h014078_wide_anchor_1` | `A` | 8.797 | 0.002648 | 0.002843 |
| `9` | `track1_hgbm_h0139_wide_anchor_1` | `A` | 8.797 | 0.002648 | 0.002843 |
| `10` | `track1_hgbm_h01_long_budget_regularized` | `A` | 8.807 | 0.002620 | 0.002817 |
| `11` | `track1_hgbm_h162_h240_wide_repair_1` | `C` | 8.914 | 0.002619 | 0.002815 |
| `12` | `track1_hgbm_h156162240_bridge_1` | `C` | 8.971 | 0.002632 | 0.002830 |
| `13` | `track1_hgbm_h01_ultraheavy_guarded` | `B` | 8.977 | 0.002685 | 0.002881 |
| `14` | `track1_hgbm_h081162240_bridge_1` | `C` | 8.986 | 0.002633 | 0.002831 |
| `15` | `track1_hgbm_h162_h240_wide_repair_2` | `C` | 9.000 | 0.002633 | 0.002835 |
| `16` | `track1_hgbm_h0181_wide_anchor_1` | `A` | 9.009 | 0.002677 | 0.002874 |
| `17` | `track1_hgbm_h01_high_bin_count` | `A` | 9.011 | 0.002678 | 0.002874 |
| `18` | `track1_hgbm_h013981_wide_anchor` | `A` | 9.030 | 0.002662 | 0.002860 |
| `19` | `track1_hgbm_h01_wide_depth_3` | `A` | 9.032 | 0.002686 | 0.002882 |
| `20` | `track1_hgbm_h39162240_bridge_1` | `C` | 9.036 | 0.002664 | 0.002860 |
| `21` | `track1_hgbm_h01_small_leaf_extreme` | `A` | 9.125 | 0.002700 | 0.002894 |
| `22` | `track1_hgbm_h013_h162240_joint_heavy` | `D` | 9.127 | 0.002734 | 0.002927 |
| `23` | `track1_hgbm_h013_h081162240_joint` | `D` | 9.129 | 0.002734 | 0.002927 |
| `24` | `track1_hgbm_h013_wide_support_2` | `A` | 9.131 | 0.002688 | 0.002884 |
| `25` | `track1_hgbm_h0181_heavy_reference` | `B` | 9.131 | 0.002735 | 0.002929 |
| `26` | `track1_hgbm_h014078_heavy_reference` | `B` | 9.135 | 0.002736 | 0.002930 |
| `27` | `track1_hgbm_h01_heavy_reference` | `B` | 9.136 | 0.002736 | 0.002930 |
| `28` | `track1_hgbm_h013_h162240_engineered_joint` | `E` | 9.155 | 0.002627 | 0.002830 |
| `29` | `track1_hgbm_h013_wide_support_1` | `A` | 9.177 | 0.002727 | 0.002923 |
| `30` | `track1_hgbm_h013_heavy_reference` | `B` | 9.199 | 0.002728 | 0.002924 |
| `31` | `track1_hgbm_h0139_heavy_reference` | `B` | 9.201 | 0.002728 | 0.002924 |
| `32` | `track1_hgbm_h013981_h162240_joint` | `D` | 9.213 | 0.002730 | 0.002926 |
| `33` | `track1_hgbm_h0139_h162240_joint_heavy` | `D` | 9.217 | 0.002732 | 0.002927 |
| `34` | `track1_hgbm_h162_isolation_heavy` | `C` | 9.301 | 0.002708 | 0.002904 |
| `35` | `track1_hgbm_h240_isolation_heavy` | `C` | 9.302 | 0.002708 | 0.002905 |
| `36` | `track1_hgbm_h01_engineered_heavy` | `E` | 9.360 | 0.002677 | 0.002879 |
| `37` | `track1_hgbm_h013_engineered_heavy` | `E` | 9.361 | 0.002677 | 0.002878 |
| `38` | `track1_hgbm_h0139_h162240_engineered_joint` | `E` | 9.382 | 0.002650 | 0.002853 |
| `39` | `track1_hgbm_h162240_engineered_heavy` | `E` | 9.644 | 0.002696 | 0.002900 |
| `40` | `track1_rf_h01_h81_engineered_control` | `F` | 10.982 | 0.003239 | 0.003431 |
| `41` | `track1_rf_h81_heavy_control` | `F` | 11.200 | 0.003315 | 0.003500 |
| `42` | `track1_rf_h039_h162240_bridge_control` | `F` | 11.212 | 0.003317 | 0.003502 |
| `43` | `track1_rf_h162240_heavy_control` | `F` | 11.212 | 0.003317 | 0.003502 |
| `44` | `track1_rf_h013_h162240_joint_control` | `F` | 11.233 | 0.003319 | 0.003504 |
| `45` | `track1_rf_h013981_bridge_control` | `F` | 11.233 | 0.003319 | 0.003504 |
| `46` | `track1_rf_h01_h81_bridge_control` | `F` | 11.236 | 0.003319 | 0.003504 |
| `47` | `track1_rf_full_rcim_heavy_control` | `F` | 11.244 | 0.003320 | 0.003505 |
| `48` | `track1_rf_h01_heavy_control` | `F` | 11.244 | 0.003320 | 0.003505 |

| Config | Validation MPE [%] | Oracle Test MPE [%] | Delta Vs `8.774%` Baseline |
| --- | ---: | ---: | ---: |
| `track1_hgbm_h01_wide_depth_2` | 9.830 | 2.749 | -0.067 |
| `track1_hgbm_h01_h162240_joint_balanced` | 10.067 | 2.749 | -0.054 |
| `track1_hgbm_h01_wide_depth_1` | 9.711 | 2.749 | -0.015 |
| `track1_hgbm_h01_h156162240_joint` | 9.621 | 2.749 | -0.006 |
| `track1_hgbm_h0181_h162240_joint` | 9.619 | 2.749 | -0.004 |
<!-- markdownlint-enable MD013 -->

## Best Run Per Block

<!-- markdownlint-disable MD013 -->
| Block | Best Config | Test MPE [%] | Interpretation |
| --- | --- | ---: | --- |
| `A` | `track1_hgbm_h01_wide_depth_2` | 8.707 | The best result came from the wide low-order search, confirming that controlled h0/h1 tuning is still the strongest direction. |
| `B` | `track1_hgbm_h01_ultraheavy_guarded` | 8.977 | Heavier low-order budgets did not beat the simpler wide winner, so extra depth and budget alone are not the fix. |
| `C` | `track1_hgbm_h81156162240_cluster` | 8.778 | Late-harmonic repair remains useful, but it still trails the best low-order and joint variants on the shared evaluator. |
| `D` | `track1_hgbm_h01_h162240_joint_balanced` | 8.720 | Joint low-order plus late-harmonic coupling nearly matched the winner and remains the strongest secondary promotion path. |
| `E` | `track1_hgbm_h013_h162240_engineered_joint` | 9.155 | Engineered terms stayed clearly behind the best no-engineering HGBM candidates and do not justify default promotion. |
| `F` | `track1_rf_h01_h81_engineered_control` | 10.982 | RandomForest remained non-competitive even under the broader and heavier campaign budget. |
<!-- markdownlint-enable MD013 -->

## Support-Branch Winner

The explicit campaign winner is:

- `track1_hgbm_h01_wide_depth_2`

Its result was:

- test mean percentage error: `8.707%`
- test curve MAE: `0.002611 deg`
- test curve RMSE: `0.002810 deg`
- validation mean percentage error: `9.830%`
- oracle test mean percentage error: `2.749%`
- previous shared-evaluator best: `8.774%`
- absolute improvement versus previous best: `0.067 percentage points`
- Target A threshold: `4.7%`
- Target A status: `not_yet_met`

This run is useful as support evidence because it is the lowest-error completed
candidate under the shared offline evaluator, but it is not the canonical
`Track 1` closure signal.

## Primary Track 1 Readout

For `Track 1`, the relevant readout from this campaign is which repair
directions should now be prioritized against the still-open paper-table cells.

The main conclusions are:

- low-order `h0 / h1` support remains the strongest direction for the open
  low-order cells;
- joint low-order plus `162/240` coupling is the strongest secondary repair
  direction and should remain in scope for the next exact-paper repair pass;
- isolated late-harmonic repair remains useful but is weaker than the best
  coupled branch;
- engineered terms and `RandomForest` still do not deserve primary runtime
  budget in the next `Track 1` repair cycle.

## Interpretation By Experiment Block

### 1. Wide Low-Order Search Won Again

The winner still came from the low-order `HGBM` search, not from the heavy
escalation block.

Important evidence:

- `track1_hgbm_h01_wide_depth_2`: `8.707%`
- `track1_hgbm_h01_h162240_joint_balanced`: `8.720%`
- `track1_hgbm_h01_wide_depth_1`: `8.759%`
- `track1_hgbm_h01_ultraheavy_guarded`: `8.977%`

Interpretation:

- `h0 / h1` remain the main leverage point for TE-level improvement;
- broader exploration still works better than simply making the same
  low-order family heavier;
- the campaign therefore does not justify promoting the heavy block as the
  new default search path.

### 2. Joint Low-Order Plus Late-Harmonic Coupling Is The Best Secondary Path

The strongest non-winning direction came from the bridge-joint block:

- `track1_hgbm_h01_h162240_joint_balanced`: `8.720%`

Interpretation:

- coupling low-order treatment with `162/240` still looks structurally useful;
- the joint path nearly tied the winner and should remain the main companion
  direction in the next iteration;
- this is stronger evidence than the previous smaller overnight batch because
  the bridge family survived a much wider search.

### 3. Late-Harmonic Repair Helps, But It Still Trails The Best Low-Order Path

The best late-repair run was:

- `track1_hgbm_h81156162240_cluster`: `8.778%`

Interpretation:

- the late-harmonic cluster remains relevant;
- however, isolated late repair still does not beat the best low-order or
  bridge-joint candidate;
- this suggests the remaining gain probably needs better coupling, not just
  stronger isolated repair.

### 4. Engineered Terms And RandomForest Still Do Not Earn Promotion

The best engineered and `RandomForest` controls were:

- engineered `HGBM`: `track1_hgbm_h013_h162240_engineered_joint` at `9.155%`
- best `RF`: `track1_rf_h01_h81_engineered_control` at `10.982%`

Interpretation:

- engineered operating-condition terms remain weaker than the strongest
  no-engineering `HGBM` path;
- `RandomForest` remained far from competitive even after the campaign budget
  was widened and deepened;
- the next `Track 1` push should not spend primary budget on either of these directions.

## Recommended Next Step

The batch improved the supporting harmonic-wise evaluator, but the gain is
still incremental and does not change the canonical `Track 1` closure status
by itself.

The most defensible next step is:

1. keep `track1_hgbm_h01_wide_depth_2` only as the current best support-branch reference;
2. keep `track1_hgbm_h01_h162240_joint_balanced` as the strongest bridge-joint companion;
3. keep `track1_hgbm_h81156162240_cluster` as the strongest late-repair companion;
4. design the next exact-paper repair cycle around a combined low-order plus
   late-harmonic coupling path instead of another broad engineered or `RF`
   retry;
5. if this stronger coupling path still stalls after the next exact-paper
   rerun, move the next research step to a new target-parameterization
   implementation rather than only adding more budget to the current
   coefficient path.

## Artifact References

- `output/training_campaigns/track1_extended_overnight_campaign_2026_04_13_13_31_57/campaign_leaderboard.yaml`
- `output/training_campaigns/track1_extended_overnight_campaign_2026_04_13_13_31_57/campaign_best_run.yaml`
- `output/training_campaigns/track1_extended_overnight_campaign_2026_04_13_13_31_57/campaign_best_run.md`
- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-13-15-11-49__track1_hgbm_h01_wide_depth_2_campaign_run/validation_summary.yaml`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
