# Wave 1 Closeout Status And Consolidated Summary Report

## Executive Summary

`Wave 1` is now closed at `100%` for repository-tracked execution and
documentation purposes.

The required closeout conditions are satisfied:

- the planned `Wave 1` campaigns were executed;
- campaign-level winner artifacts exist;
- family-level and program-level registries exist and are aligned with the
  final ranking;
- the recovery campaign has a final Markdown report and validated PDF;
- the residual-harmonic follow-up campaign has a final Markdown report and
  validated PDF;
- the running-state backlog now reflects that `Wave 1` reporting is complete.

The only meaningful open item related to `Wave 1` is a future engineering
follow-up, not a closeout blocker:

- retry the random-forest branch on a higher-memory machine to separate model
  quality limits from the workstation-specific memory ceiling seen in the first
  campaign.

The current global program leader remains:

- family: `tree`
- model type: `hist_gradient_boosting`
- run: `te_hist_gbr_tabular`
- validation MAE: `0.002719 deg`
- test MAE: `0.002885 deg`

The strongest current neural challenger remains:

- family: `residual_harmonic_mlp`
- run: `te_residual_h12_deep_joint_wave1`
- validation MAE: `0.003024 deg`
- test MAE: `0.003152 deg`

## What Wave 1 Was Supposed To Answer

`Wave 1` was the first structured-baseline comparison stage after the
feedforward infrastructure and baseline were already stable.

Its core questions were:

1. can explicit periodic or structured bias beat the existing feedforward
   baseline?
2. is the next useful TE model family analytical, hybrid-neural, or purely
   tabular?
3. which family deserves a narrower follow-up campaign before the project
   moves toward later waves?

The formal feedforward comparison anchor was:

| Family | Run | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | ---: | ---: | ---: |
| `feedforward` | `te_feedforward_stride5_long_large_batch` | 0.003109 | 0.003301 | 0.003791 |

## Wave 1 Execution Sequence

`Wave 1` unfolded in three operational stages.

### 1. Initial Cross-Family Structured-Baseline Campaign

Planned campaign:

- `wave1_structured_baseline_campaign_2026_03_17_21_01_47`

Campaign goal:

- compare harmonic, periodic-feature, residual-harmonic, and tree-based
  baselines against the formalized feedforward reference.

Planned candidate set:

- `te_harmonic_order06_static`
- `te_harmonic_order12_static`
- `te_harmonic_order12_linear_conditioned`
- `te_periodic_mlp_h04_standard`
- `te_periodic_mlp_h08_standard`
- `te_periodic_mlp_h08_wide`
- `te_residual_h12_small_frozen`
- `te_residual_h12_small_joint`
- `te_random_forest_tabular`
- `te_hist_gbr_tabular`

Operational result:

- completed runs: `4`
- failed runs: `6`

The initial run surfaced two issues:

- a schema-aware summary bug affecting the harmonic and residual branches;
- a `RandomForestRegressor` memory failure on the current workstation.

Completed entries from the first campaign:

| Rank | Run | Family | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | ---: | ---: | ---: |
| `1` | `te_hist_gbr_tabular` | `tree` | 0.002719 | 0.002885 | 0.003607 |
| `2` | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003097 | 0.003317 | 0.003793 |
| `3` | `te_periodic_mlp_h08_standard` | `periodic_mlp` | 0.003086 | 0.003395 | 0.003951 |
| `4` | `te_periodic_mlp_h08_wide` | `periodic_mlp` | 0.003089 | 0.003590 | 0.004143 |

Immediate interpretation:

- the tree family produced the strongest early result;
- the low-depth periodic model was competitive with the feedforward baseline;
- widening the periodic network did not improve held-out performance.

### 2. Recovery Campaign

Recovery campaign:

- `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42`

Campaign goal:

- rerun the branches that failed for operational reasons in the first pass and
  restore a complete family-level comparison.

Recovered candidate set:

- `te_harmonic_order06_static_recovery`
- `te_harmonic_order12_static_recovery`
- `te_harmonic_order12_linear_conditioned_recovery`
- `te_residual_h12_small_frozen_recovery`
- `te_residual_h12_small_joint_recovery`
- `te_random_forest_tabular_recovery`

Operational result:

- completed runs: `6`
- failed runs: `0`

Recovery ranking:

| Rank | Run | Family | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | ---: | ---: | ---: |
| `1` | `te_residual_h12_small_joint_recovery` | `residual_harmonic_mlp` | 0.003016 | 0.003466 | 0.003967 |
| `2` | `te_residual_h12_small_frozen_recovery` | `residual_harmonic_mlp` | 0.003030 | 0.003554 | 0.004061 |
| `3` | `te_random_forest_tabular_recovery` | `tree` | 0.003792 | 0.003833 | 0.004809 |
| `4` | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 0.017004 | 0.020782 | 0.022405 |
| `5` | `te_harmonic_order12_static_recovery` | `harmonic_regression` | 0.040524 | 0.039404 | 0.042797 |
| `6` | `te_harmonic_order06_static_recovery` | `harmonic_regression` | 0.040529 | 0.039406 | 0.042796 |

Immediate interpretation:

- the residual-harmonic family was clearly the strongest recovered family;
- the random-forest branch became runnable but remained slower and weaker than
  the existing histogram-boosting leader;
- harmonic regression stayed useful mainly as a structured reference, not as a
  performance leader.

### 3. Residual-Harmonic Family Optimization Follow-Up

Familywise follow-up campaign:

- `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00`

Campaign goal:

- test whether the strongest structured-neural family could close the gap to
  the tree-based program leader under a broader family-specific search.

Explored axes:

- harmonic order and structured-branch regime;
- joint versus frozen training;
- residual-head capacity;
- dropout and layer-normalization variants;
- longer schedules and lower learning rates;
- denser sampling and larger curve batches.

Operational result:

- completed runs: `15`
- failed runs: `0`

Top campaign entries:

| Rank | Run | Parameters | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | ---: | ---: | ---: | ---: |
| `1` | `te_residual_h12_deep_joint_wave1` | 26266 | 0.003024 | 0.003152 | 0.003640 |
| `2` | `te_residual_h12_small_joint_high_dropout_wave1` | 4890 | 0.003001 | 0.003230 | 0.003704 |
| `3` | `te_residual_h16_small_joint_wave1` | 4898 | 0.003020 | 0.003274 | 0.003747 |
| `4` | `te_residual_h12_wide_joint_low_lr_long_wave1` | 17946 | 0.002924 | 0.003278 | 0.003814 |
| `5` | `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | 4890 | 0.002935 | 0.003302 | 0.003909 |

Key familywise outcome:

- the deeper joint residual branch produced the best held-out test result;
- the residual family improved meaningfully over the recovery-stage reference;
- even after this improvement, the tree leader still remained the global best.

## Complete Wave 1 Family Summary

The following table captures the best final result per relevant family after all
`Wave 1` execution and recovery work.

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `tree` | `te_hist_gbr_tabular` | `hist_gradient_boosting` | 0.002719 | 0.002885 | 0.003607 | Current global program leader |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003024 | 0.003152 | 0.003640 | Strongest neural family |
| `feedforward` | `te_feedforward_stride5_long_large_batch` | `feedforward` | 0.003109 | 0.003301 | 0.003791 | Historical neural baseline |
| `periodic_mlp` | `te_periodic_mlp_h04_standard` | `periodic_mlp` | 0.003097 | 0.003317 | 0.003793 | Competitive hybrid baseline |
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | 0.017004 | 0.020782 | 0.022405 | Structured interpretability reference |

## All Executed Wave 1 Training Runs

Total executed `Wave 1` runs across the three campaign stages: `25`

### Initial Structured-Baseline Campaign

| Run | Family | Status | Test MAE [deg] | Notes |
| --- | --- | --- | ---: | --- |
| `te_harmonic_order06_static` | `harmonic_regression` | failed | N/A | summary bug |
| `te_harmonic_order12_static` | `harmonic_regression` | failed | N/A | summary bug |
| `te_harmonic_order12_linear_conditioned` | `harmonic_regression` | failed | N/A | summary bug |
| `te_periodic_mlp_h04_standard` | `periodic_mlp` | completed | 0.003317 | best periodic result |
| `te_periodic_mlp_h08_standard` | `periodic_mlp` | completed | 0.003395 | richer encoding did not win |
| `te_periodic_mlp_h08_wide` | `periodic_mlp` | completed | 0.003590 | extra width hurt test-side ranking |
| `te_residual_h12_small_frozen` | `residual_harmonic_mlp` | failed | N/A | summary bug |
| `te_residual_h12_small_joint` | `residual_harmonic_mlp` | failed | N/A | summary bug |
| `te_random_forest_tabular` | `tree` | failed | N/A | workstation memory failure |
| `te_hist_gbr_tabular` | `tree` | completed | 0.002885 | current global winner |

### Recovery Campaign

| Run | Family | Status | Test MAE [deg] | Notes |
| --- | --- | --- | ---: | --- |
| `te_harmonic_order06_static_recovery` | `harmonic_regression` | completed | 0.039406 | static low-order reference |
| `te_harmonic_order12_static_recovery` | `harmonic_regression` | completed | 0.039404 | static high-order reference |
| `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` | completed | 0.020782 | best harmonic result |
| `te_residual_h12_small_frozen_recovery` | `residual_harmonic_mlp` | completed | 0.003554 | frozen branch remained competitive |
| `te_residual_h12_small_joint_recovery` | `residual_harmonic_mlp` | completed | 0.003466 | best recovered neural run |
| `te_random_forest_tabular_recovery` | `tree` | completed | 0.003833 | runnable but slower and weaker than histogram boosting |

### Residual-Harmonic Family Follow-Up

| Run | Test MAE [deg] | Notes |
| --- | ---: | --- |
| `te_residual_h08_small_frozen_wave1` | 0.003384 | harmonic order 8, frozen |
| `te_residual_h08_small_joint_wave1` | 0.003385 | harmonic order 8, joint |
| `te_residual_h12_small_frozen_wave1` | 0.003368 | harmonic order 12, frozen |
| `te_residual_h12_small_joint_anchor_wave1` | 0.003557 | anchor rerun |
| `te_residual_h16_small_joint_wave1` | 0.003274 | harmonic order 16, joint |
| `te_residual_h12_medium_joint_wave1` | 0.003406 | medium residual branch |
| `te_residual_h12_wide_joint_wave1` | 0.003376 | wide residual branch |
| `te_residual_h12_deep_joint_wave1` | 0.003152 | family winner |
| `te_residual_h12_small_joint_low_dropout_wave1` | 0.003359 | lower dropout |
| `te_residual_h12_small_joint_high_dropout_wave1` | 0.003230 | strongest regularized small model |
| `te_residual_h12_small_joint_no_layer_norm_wave1` | 0.003360 | no layer norm |
| `te_residual_h12_small_joint_low_lr_long_wave1` | 0.003465 | longer lower-LR schedule |
| `te_residual_h12_wide_joint_low_lr_long_wave1` | 0.003278 | strong wide low-LR variant |
| `te_residual_h12_small_joint_dense_wave1` | 0.003410 | dense full-point regime |
| `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | 0.003302 | denser regime with larger batches |

## Final Cross-Family Interpretation

`Wave 1` supports five high-confidence conclusions.

### 1. The Tree Baseline Won The Accuracy Race

The best empirical result is still:

- `te_hist_gbr_tabular`
- `test_mae = 0.002885 deg`

This means the repository should not assume that a neural model is justified
simply because it is more expressive or more aligned with later hybrid work.

### 2. The Residual-Harmonic Family Won The Neural Race

The best neural result is now:

- `te_residual_h12_deep_joint_wave1`
- `test_mae = 0.003152 deg`

This family clearly outperformed the periodic MLP and the historical
feedforward baseline on held-out test error.

### 3. Periodic Features Helped, But Did Not Produce The Best Family

The best periodic model:

- `te_periodic_mlp_h04_standard`
- `test_mae = 0.003317 deg`

This result is respectable and close to the feedforward baseline, but it does
not displace the residual family or the tree leader.

### 4. Harmonic Regression Is Best Kept As A Structured Reference

The best harmonic result:

- `te_harmonic_order12_linear_conditioned_recovery`
- `test_mae = 0.020782 deg`

This family remains valuable for interpretability and explicit periodic
reasoning, but not as the current best predictive candidate.

### 5. Wave 1 Did What It Needed To Do

`Wave 1` successfully identified:

- the strongest non-neural practical baseline;
- the strongest current structured-neural direction;
- the fact that later waves should not ignore deployment-oriented tabular
  simplicity just because more complex neural directions exist.

## Exact Closeout Audit

The closeout audit checked the following repository conditions.

### Confirmed Present

- initial `Wave 1` campaign execution artifacts under
  `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/`
- recovery campaign execution artifacts plus campaign-level winner artifacts
- residual-family follow-up campaign execution artifacts plus campaign-level
  winner artifacts
- family registries under `output/registries/families/`
- program-level best registry under
  `output/registries/program/current_best_solution.yaml`
- final recovery campaign Markdown report and PDF
- final residual-family campaign Markdown report and PDF

### Running-State Issues Found

Before this closeout pass, the running-state documents still had stale wording:

- the live backlog still marked the `Wave 1` results report as pending;
- the live backlog still described the recovery campaign as merely prepared;
- the live backlog still listed already-completed reporting tasks as next
  steps;
- `active_training_campaign.yaml` used `status: finished`, while the running
  policy documents the canonical terminal state as `status: completed`.

### Closeout Resolution

Those running-state inconsistencies are now resolved through:

- backlog synchronization to the completed state;
- terminal campaign status normalization from `finished` to `completed`;
- this consolidated report, which fills the previous gap of a single
  repository-owned `Wave 1` closeout summary.

### Remaining Non-Blocking Follow-Up

- run a higher-memory random-forest retry only if the project wants to separate
  hardware memory pressure from family-level model quality.

This is a future comparison refinement, not a blocker for declaring
`Wave 1` closed.

## Recommended Post-Wave 1 Direction

The most defensible next steps are:

1. keep `te_hist_gbr_tabular` as the current global reference winner;
2. keep `te_residual_h12_deep_joint_wave1` as the neural family anchor;
3. move the main repository execution focus toward TwinCAT deployment
   evaluation and `Wave 2` temporal-model planning;
4. treat any random-forest retry as a narrow follow-up experiment rather than a
   reason to reopen `Wave 1` closeout.

## Artifact References

- Initial `Wave 1` campaign:
  `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/`
- Recovery campaign:
  `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/`
- Residual-family follow-up campaign:
  `output/training_campaigns/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/`
- Recovery campaign final report:
  `doc/reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md`
- Residual-family final report:
  `doc/reports/campaign_results/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md`
- Family registries:
  `output/registries/families/`
- Program registry:
  `output/registries/program/current_best_solution.yaml`
- Live backlog:
  `doc/running/te_model_live_backlog.md`
- Campaign state:
  `doc/running/active_training_campaign.yaml`
