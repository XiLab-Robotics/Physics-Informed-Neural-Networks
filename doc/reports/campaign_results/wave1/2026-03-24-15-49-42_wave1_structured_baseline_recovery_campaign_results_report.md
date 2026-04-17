# Wave1 Structured Baseline Recovery Campaign Results Report

## Overview

This report summarizes the completed recovery campaign prepared in:

- `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`

The recovery campaign was created to rerun the Wave 1 configurations that had failed for operational reasons in the earlier execution:

- harmonic regression runs previously blocked by the shared summary path assuming `hidden_size`;
- residual harmonic MLP runs blocked by the same shared summary assumption;
- the random-forest tabular baseline previously failing under a higher-memory configuration.

The campaign executed successfully end to end:

- completed runs: `6`
- failed runs: `0`
- execution report generated at: `2026-03-20T18:32:18`
- campaign execution window: `2026-03-20T16:11:22` to `2026-03-20T18:32:18`

The campaign artifact root is:

- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/`

## Recovery Objective And Outcome

This campaign was not a new broad model screening pass. It had a narrower operational goal:

- prove that the corrected training path can execute the previously failing Wave 1 branches to completion;
- recover comparable metrics for the missing harmonic, residual, and random-forest entries;
- restore campaign-level ranking integrity before planning the next exploratory stage.

On that operational objective, the recovery campaign succeeded completely.

- all six queued runs completed;
- the harmonic and residual branches now produce the expected artifact set;
- the conservative random-forest configuration finished on the current workstation, although with the longest runtime in the campaign.

## Recovery Campaign Ranking

The campaign ranking follows the serialized policy stored in `campaign_leaderboard.yaml`:

- primary metric: `test_mae`
- first tie breaker: `test_rmse`
- second tie breaker: `val_mae`
- third tie breaker: `trainable_parameter_count`

### Test-Side Ranking

| Rank | Config | Family | Runtime | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | ---: | ---: | ---: |
| `1` | `te_residual_h12_small_joint_recovery` | `residual_harmonic_mlp` | 16.9 min | 0.003466 | 0.003967 |
| `2` | `te_residual_h12_small_frozen_recovery` | `residual_harmonic_mlp` | 17.5 min | 0.003554 | 0.004061 |
| `3` | `te_random_forest_tabular_recovery` | `tree` | 76.9 min | 0.003833 | 0.004809 |
| `4` | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 9.8 min | 0.020782 | 0.022405 |
| `5` | `te_harmonic_order12_static_recovery` | `harmonic_regression` | 10.9 min | 0.039404 | 0.042797 |
| `6` | `te_harmonic_order06_static_recovery` | `harmonic_regression` | 9.1 min | 0.039406 | 0.042796 |

### Validation-Side Snapshot

| Config | Parameters | Val MAE [deg] | Val RMSE [deg] |
| --- | --- | ---: | ---: |
| `te_residual_h12_small_joint_recovery` | 4890 | 0.003016 | 0.003534 |
| `te_residual_h12_small_frozen_recovery` | 4890 total / 4865 trainable | 0.003030 | 0.003554 |
| `te_random_forest_tabular_recovery` | 5 | 0.003792 | 0.004971 |
| `te_harmonic_order12_linear_conditioned_recovery` | 150 | 0.017004 | 0.018547 |
| `te_harmonic_order12_static_recovery` | 25 | 0.040524 | 0.042584 |
| `te_harmonic_order06_static_recovery` | 13 | 0.040529 | 0.042572 |

## Campaign Winner

The explicit campaign winner is:

- `te_residual_h12_small_joint_recovery`

Its result was:

- validation MAE: `0.003016 deg`
- validation RMSE: `0.003534 deg`
- test MAE: `0.003466 deg`
- test RMSE: `0.003967 deg`

This run beat the frozen residual variant by a small but consistent margin on both validation and test error. Within the recovery set, the joint residual variant is therefore the strongest practical candidate.

## Family-Level Interpretation

### Residual Harmonic MLP

The recovery campaign confirms that the residual family is the strongest of the recovered branches.

| Config | Training Mode | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | ---: | ---: | ---: |
| `te_residual_h12_small_joint_recovery` | joint residual + harmonic optimization | 0.003016 | 0.003466 | 0.003967 |
| `te_residual_h12_small_frozen_recovery` | frozen harmonic base + learned residual head | 0.003030 | 0.003554 | 0.004061 |

Interpretation:

- both residual runs are numerically stable and tightly grouped;
- joint optimization is slightly better than freezing the harmonic base;
- the gain is modest, but it is directionally consistent on both validation and test metrics;
- the residual family clearly dominates the recovered harmonic baselines by an order-of-magnitude margin on absolute error.

An additional residual-specific signal is available in the structured metrics:

- `te_residual_h12_small_joint_recovery` reports `test_structured_mae = 0.039405 deg`;
- `te_residual_h12_small_frozen_recovery` reports `test_structured_mae = 0.040148 deg`.

This suggests that even when the residual branch is decomposed back toward its structured component, the joint variant remains slightly cleaner.

### Random Forest

The conservative random-forest recovery run completed successfully:

- validation MAE: `0.003792 deg`
- test MAE: `0.003833 deg`
- runtime: `76.9 min`

Interpretation:

- the workstation-memory issue was mitigated well enough for successful completion;
- the recovered random forest is competitive with the residual family, but it does not beat it in this campaign;
- its runtime is the worst in the recovery set by a large margin, so the conservative memory-safe configuration trades efficiency for reliability.

Operationally, this is still an important success because the model family is now back inside the comparable result set instead of remaining missing due to runtime failure.

### Harmonic Regression

The harmonic family is now fully recovered, but it remains well behind the residual and tree candidates.

| Config | Harmonic Setup | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | ---: | ---: | ---: |
| `te_harmonic_order12_linear_conditioned_recovery` | order 12 + linear conditioning | 0.017004 | 0.020782 | 0.022405 |
| `te_harmonic_order12_static_recovery` | order 12 static | 0.040524 | 0.039404 | 0.042797 |
| `te_harmonic_order06_static_recovery` | order 6 static | 0.040529 | 0.039406 | 0.042796 |

Interpretation:

- the linear-conditioned harmonic variant is the only harmonic run that materially improves over the static harmonic baselines;
- the two static harmonic runs are effectively tied on held-out test metrics;
- even the best harmonic recovery variant remains far behind the residual and tree branches, so harmonic regression should stay a lightweight reference family rather than the main candidate for best TE prediction.

## Program-Level Context

The recovery campaign winner is not the global program leader.

According to `output/registries/program/current_best_solution.yaml`, the current program-level best solution remains:

- `te_hist_gbr_tabular`
- model type: `hist_gradient_boosting`
- test MAE: `0.002885 deg`
- test RMSE: `0.003607 deg`

This means the recovery campaign restored missing branches and produced a clear local winner, but it did not overturn the broader Wave 1 ranking.

The practical ranking state after the recovery campaign is:

1. global program best still belongs to the tree family through `hist_gradient_boosting`;
2. best recovered candidate is `te_residual_h12_small_joint_recovery`;
3. harmonic regression remains a weaker structured reference family.

## Main Conclusions

The recovery campaign supports five concrete conclusions.

### 1. The Operational Failures Were Resolved

The shared-summary fix and the conservative random-forest adjustment were sufficient to recover all previously missing results.

### 2. Residual Harmonic MLP Is The Best Recovered Family

Both residual runs outperform the harmonic and random-forest recovery entries. The joint residual variant is the best recovered run overall.

### 3. The Random-Forest Branch Is Now Runnable But Expensive

The memory-safe random-forest setup completed on the current workstation, but the runtime cost is high enough that a higher-memory machine is still worth testing as a follow-up.

### 4. Harmonic Regression Remains Useful Mainly As A Structured Reference

The linear-conditioned harmonic variant is meaningfully better than the static harmonic variants, but the family is still not competitive with the stronger nonlinear candidates.

### 5. The Broader Wave 1 Leaderboard Did Not Change At The Top

The recovery campaign repaired campaign completeness, but the repository-wide best solution remains the earlier `hist_gradient_boosting` tree model.

## Recommended Next Actions

The next technically useful steps are:

1. build the next campaign around best-training search per family rather than broad one-shot screening;
2. keep `te_residual_h12_small_joint_recovery` as the residual reference point for that next exploration;
3. test the conservative random-forest branch on a higher-memory machine to separate workstation memory pressure from model-quality limits;
4. compare the recovered residual winner directly against the existing `hist_gradient_boosting` leader under the same decision criteria before choosing the next mainline candidate.

## Artifact References

Campaign-level references:

- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_manifest.yaml`
- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_execution_report.md`
- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_leaderboard.yaml`
- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_best_run.yaml`
- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_best_run.md`

Winning recovered run:

- `output/training_runs/residual_harmonic_mlp/2026-03-20-16-58-34__te_residual_h12_small_joint_recovery/`

Program-level reference winner:

- `output/training_runs/tree/2026-03-20-15-17-30__te_hist_gbr_tabular/`

Each run folder includes:

- `metrics_summary.yaml`
- `training_test_report.md`
- model artifact or checkpoint pointer
