# Wave 1 Residual Harmonic Family Campaign Results Report

## Overview

This report summarizes the completed residual-harmonic family campaign prepared
in:

- `doc/reports/campaign_plans/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`

The campaign goal was narrower than the earlier cross-family Wave 1 screening.
This pass focused only on the `residual_harmonic_mlp` family and expanded the
search around the recovered residual reference point to test:

- structured-branch regime choices;
- residual-head capacity;
- dropout and layer-normalization variants;
- longer and lower-learning-rate schedules;
- denser sampling and larger curve-batch settings.

The campaign executed cleanly end to end:

- completed runs: `15`
- failed runs: `0`
- execution report generated at: `2026-03-26T20:19:32`
- campaign execution window: `2026-03-26T15:01:20` to `2026-03-26T20:19:32`

The campaign artifact root is:

- `output/training_campaigns/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/`

## Objective And Outcome

This campaign was designed to answer one practical question:

- can the residual-harmonic family close the gap to the current tree-based
  program leader when given a broader family-specific optimization budget?

On execution quality, the answer is clearly yes:

- all `15` approved runs completed;
- the campaign produced a stable ranked leaderboard;
- family-level and program-level registries were updated consistently.

On model-selection quality, the answer is mixed but encouraging:

- the campaign found a new best residual-harmonic configuration with
  `test_mae = 0.003152 deg`;
- this is materially better than the earlier recovered residual reference
  `te_residual_h12_small_joint_recovery` at `0.003466 deg`;
- the residual family still does not overtake the program-level
  `hist_gradient_boosting` leader at `test_mae = 0.002885 deg`.

## Ranking Policy

The campaign ranking follows the serialized policy stored in
`campaign_leaderboard.yaml`:

- primary metric: `test_mae`
- first tie breaker: `test_rmse`
- second tie breaker: `val_mae`
- third tie breaker: `trainable_parameter_count`

## Campaign Ranking

### Test-Side Ranking

| Rank | Config | Parameters | Runtime | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `1` | `te_residual_h12_deep_joint_wave1` | 26266 | 28.8 min | 0.003152 | 0.003640 | 0.003024 |
| `2` | `te_residual_h12_small_joint_high_dropout_wave1` | 4890 | 21.5 min | 0.003230 | 0.003704 | 0.003001 |
| `3` | `te_residual_h16_small_joint_wave1` | 4898 | 20.1 min | 0.003274 | 0.003747 | 0.003020 |
| `4` | `te_residual_h12_wide_joint_low_lr_long_wave1` | 17946 | 22.8 min | 0.003278 | 0.003814 | 0.002924 |
| `5` | `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | 4890 | 18.1 min | 0.003302 | 0.003909 | 0.002935 |
| `6` | `te_residual_h12_small_joint_low_dropout_wave1` | 4890 | 21.1 min | 0.003359 | 0.003852 | 0.003027 |
| `7` | `te_residual_h12_small_joint_no_layer_norm_wave1` | 4634 | 12.8 min | 0.003360 | 0.003835 | 0.003089 |
| `8` | `te_residual_h12_small_frozen_wave1` | 4865 trainable / 4890 total | 23.4 min | 0.003368 | 0.003898 | 0.003036 |
| `9` | `te_residual_h12_wide_joint_wave1` | 17946 | 31.4 min | 0.003376 | 0.003906 | 0.002884 |
| `10` | `te_residual_h08_small_frozen_wave1` | 4865 trainable / 4882 total | 18.6 min | 0.003384 | 0.003912 | 0.003007 |
| `11` | `te_residual_h08_small_joint_wave1` | 4882 | 11.4 min | 0.003385 | 0.003862 | 0.003030 |
| `12` | `te_residual_h12_medium_joint_wave1` | 9498 | 22.2 min | 0.003406 | 0.003863 | 0.002968 |
| `13` | `te_residual_h12_small_joint_dense_wave1` | 4890 | 27.0 min | 0.003410 | 0.003790 | 0.002962 |
| `14` | `te_residual_h12_small_joint_low_lr_long_wave1` | 4890 | 27.7 min | 0.003465 | 0.003944 | 0.002987 |
| `15` | `te_residual_h12_small_joint_anchor_wave1` | 4890 | 11.3 min | 0.003557 | 0.004064 | 0.003090 |

### Validation-Side Snapshot

| Config | Val MAE [deg] | Test MAE [deg] | Generalization Gap [deg] |
| --- | ---: | ---: | ---: |
| `te_residual_h12_wide_joint_wave1` | 0.002884 | 0.003376 | 0.000492 |
| `te_residual_h12_wide_joint_low_lr_long_wave1` | 0.002924 | 0.003278 | 0.000354 |
| `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | 0.002935 | 0.003302 | 0.000367 |
| `te_residual_h12_small_joint_dense_wave1` | 0.002962 | 0.003410 | 0.000448 |
| `te_residual_h12_medium_joint_wave1` | 0.002968 | 0.003406 | 0.000437 |
| `te_residual_h12_small_joint_high_dropout_wave1` | 0.003001 | 0.003230 | 0.000229 |
| `te_residual_h12_deep_joint_wave1` | 0.003024 | 0.003152 | 0.000129 |

This validation view matters because the campaign winner is not the
lowest-validation run. The best held-out test result came from the deep joint
variant, which also has the smallest validation-to-test gap among the leading
configurations.

## Campaign Winner

The explicit campaign winner is:

- `te_residual_h12_deep_joint_wave1`

Its result was:

- validation MAE: `0.003024 deg`
- validation RMSE: `0.003580 deg`
- test MAE: `0.003152 deg`
- test RMSE: `0.003640 deg`
- validation structured MAE: `0.040554 deg`
- test structured MAE: `0.039416 deg`

The deep joint run wins because it generalizes better than the more
aggressively tuned alternatives. Several configurations pushed validation MAE a
bit lower, but none beat this run on the primary campaign metric `test_mae`.

## Interpretation By Search Axis

### 1. Deeper Residual Capacity Was The Highest-Value Change

The strongest signal in the campaign is that deeper residual capacity matters
more than simply widening the branch or extending the schedule.

Key comparison:

| Config | Capacity Pattern | Val MAE [deg] | Test MAE [deg] |
| --- | --- | ---: | ---: |
| `te_residual_h12_deep_joint_wave1` | deeper `128-128-64` residual head | 0.003024 | 0.003152 |
| `te_residual_h12_wide_joint_wave1` | wider `128-128` residual head | 0.002884 | 0.003376 |
| `te_residual_h12_medium_joint_wave1` | moderate `128-64` residual head | 0.002968 | 0.003406 |

Interpretation:

- the deep model clearly has the best test-side ranking;
- the wide and medium variants look attractive on validation MAE but degrade on
  held-out test error;
- the deep variant appears to provide the best bias-capacity tradeoff within
  this family.

### 2. Mild Additional Regularization Helped, But Not Enough To Win

The high-dropout variant is the second-best campaign run:

- `te_residual_h12_small_joint_high_dropout_wave1`
- validation MAE: `0.003001 deg`
- test MAE: `0.003230 deg`

This is a useful result because it suggests the small residual branch can be
made slightly more robust with stronger regularization. However, the gain is
still smaller than what was achieved by the deeper joint configuration.

The no-layer-norm variant confirms the opposite side of the same point:

- `te_residual_h12_small_joint_no_layer_norm_wave1`
- validation MAE: `0.003089 deg`
- test MAE: `0.003360 deg`

Removing layer normalization is therefore not a good direction for the current
family baseline.

### 3. Lower-Learning-Rate Long Schedules Improved Validation More Than Test

Two long-schedule runs looked good on validation:

- `te_residual_h12_wide_joint_low_lr_long_wave1`
- `te_residual_h12_small_joint_low_lr_long_wave1`

But their final held-out test ranking stayed below the winner. This suggests
that longer convergence windows are useful, but not sufficient by themselves to
replace the capacity benefit of the deep residual branch.

### 4. Dense Training Regimes Did Not Produce The Best Generalization

The denser sampling experiments are competitive but not dominant:

| Config | Data Regime | Val MAE [deg] | Test MAE [deg] |
| --- | --- | ---: | ---: |
| `te_residual_h12_small_joint_dense_wave1` | full-point density | 0.002962 | 0.003410 |
| `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | stride 5 + larger curve batch | 0.002935 | 0.003302 |

Interpretation:

- denser regimes improve validation relative to the original small joint anchor;
- they do not beat the deep joint configuration on the held-out test metric;
- future dense-regime passes should probably be combined with the deep capacity
  setting rather than treated as the main axis on their own.

### 5. Joint Optimization Still Beats The Frozen Structured Base

The frozen vs joint decision remains directionally clear:

| Config | Training Mode | Val MAE [deg] | Test MAE [deg] |
| --- | --- | ---: | ---: |
| `te_residual_h12_small_frozen_wave1` | frozen harmonic base + learned residual | 0.003036 | 0.003368 |
| `te_residual_h12_deep_joint_wave1` | joint harmonic + residual optimization | 0.003024 | 0.003152 |

The campaign therefore reinforces the earlier recovery signal: the residual
family should continue to use joint optimization as the mainline direction.

## Comparison Against The Previous Residual Reference

The recovery-stage residual reference was:

- `te_residual_h12_small_joint_recovery`
- test MAE: `0.003466 deg`

The new campaign winner improves that to:

- `te_residual_h12_deep_joint_wave1`
- test MAE: `0.003152 deg`

That is an absolute improvement of about `0.000314 deg`, which is a meaningful
gain for a family-internal follow-up campaign.

## Program-Level Context

The campaign winner is now the family-level best residual-harmonic result, but
it is still not the global program leader.

According to `output/registries/program/current_best_solution.yaml`, the
current program-level best solution remains:

- `te_hist_gbr_tabular`
- model type: `hist_gradient_boosting`
- test MAE: `0.002885 deg`
- test RMSE: `0.003607 deg`

Relative to that global leader, the new residual winner is still behind by
roughly `0.000267 deg` test MAE.

The practical program ranking is therefore:

1. global program best still belongs to the tree family through
   `hist_gradient_boosting`;
2. best residual-harmonic family result is now
   `te_residual_h12_deep_joint_wave1`;
3. the residual family has improved enough to remain the strongest practical
   neural challenger.

## Main Conclusions

The campaign supports five concrete conclusions.

### 1. The Familywise Search Was Operationally Successful

All `15` runs completed and produced a coherent campaign-local ranking with no
missing artifacts.

### 2. The Residual Family Has A Better Champion Than The Recovery Baseline

`te_residual_h12_deep_joint_wave1` is a clear improvement over the earlier
recovery reference and is now the correct residual-family anchor.

### 3. Best Validation Does Not Equal Best Test For This Search Space

Several wide, dense, and long-schedule runs beat the winner on validation MAE,
but the deep joint model has the best held-out test score and the cleanest
generalization gap among the top group.

### 4. Capacity Was More Valuable Than Extra Density Alone

The strongest progress came from the deeper residual head rather than from
batch-size or point-density changes in isolation.

### 5. The Tree Leader Still Stands

The campaign closes part of the gap but does not yet displace the global
`hist_gradient_boosting` winner.

## Recommended Next Actions

The next technically useful steps are:

1. treat `te_residual_h12_deep_joint_wave1` as the canonical residual-family
   baseline for any future residual follow-up work;
2. if the residual family remains a priority, combine the winning deep branch
   with the most promising secondary levers:
   higher dropout, lower-learning-rate long schedule, or denser sampling, but
   not all at once without a narrower hypothesis;
3. avoid using validation MAE alone as the decision signal for this family,
   because the current campaign shows a real validation-to-test ranking shift;
4. compare the new residual winner against the tree leader only in tightly
   scoped follow-up experiments rather than launching another broad family
   sweep immediately;
5. preserve the current registries and campaign outputs as the official
   reference point for the residual-harmonic family.

## Artifact References

Campaign-level references:

- `output/training_campaigns/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/campaign_manifest.yaml`
- `output/training_campaigns/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/campaign_execution_report.md`
- `output/training_campaigns/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/campaign_leaderboard.yaml`
- `output/training_campaigns/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/campaign_best_run.yaml`
- `output/training_campaigns/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/campaign_best_run.md`

Winning run:

- `output/training_runs/residual_harmonic_mlp/2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1/`

Current global program leader:

- `output/training_runs/tree/2026-03-20-15-17-30__te_hist_gbr_tabular/`

Each run folder includes:

- `metrics_summary.yaml`
- `training_test_report.md`
- model checkpoint directory plus `best_checkpoint_path.txt`
