# Track 1 Second Iteration Harmonic-Wise Campaign Results Report

## Overview

This report closes the second paper-faithful `Track 1` campaign prepared in:

- `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-09-18-56-03_track1_second_iteration_harmonic_wise_campaign_plan_report.md`

The campaign executed `8` harmonic-wise validation runs through the dedicated
paper-reimplementation launcher:

- completed runs: `8`
- failed runs: `0`
- execution window: `2026-04-09T20:43:53+02:00` to `2026-04-09T21:06:13+02:00`
- campaign artifact root:
  `output/training_campaigns/track1/harmonic_wise/2026-04-09-20-41-59_track1_second_iteration_harmonic_wise_campaign_2026_04_09_18_56_03/`

Unlike the earlier generic training campaigns, this package evaluates the
repository-owned RCIM paper reimplementation path:

- harmonic-wise prediction from operating conditions;
- TE reconstruction from predicted harmonics;
- offline paper-comparable TE-curve validation;
- staged comparison between reduced harmonic subsets and the full RCIM set.

## Objective And Outcome

The campaign had four concrete questions:

1. can staged reduced harmonic sets make the predictor easier to learn before
   promoting back to the full RCIM harmonic set?
2. do engineered operating-condition features improve the harmonic predictor?
3. does a diagnostic `RandomForest` baseline reveal that the issue is
   estimator-family specific rather than pipeline specific?
4. can this second iteration close or materially narrow `Target A`, which
   requires `<= 4.7%` mean percentage error on held-out TE curves?

The answers are now clear:

- the campaign improved the best full-RCIM harmonic-wise result from `9.403%` to `8.877%`;
- the winning run was the refined full-RCIM full-set configuration without engineered features;
- the reduced harmonic subsets were all worse than the full-RCIM runs;
- the engineered feature variants did not improve the full-RCIM result in this
  iteration;
- `Target A` remains open and is still far from the paper threshold.

## Ranking Policy

The campaign ranking follows the paper-comparable offline validation priority:

- primary metric: `test_curve_mean_percentage_error_pct`
- first tie breaker: `test_curve_rmse_deg`
- second tie breaker: `validation_curve_mean_percentage_error_pct`
- third tie breaker: `harmonic_target_mae`

## Campaign Ranking

### Ranked Completed Runs

| Rank | Config | Harmonic Set | Feature Set | Test % Error | Oracle Test % | Test MAE [deg] |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `1` | `te_harmonic_wise_full_rcim_no_engineering_reference` | `full RCIM` | `base_only` | `8.877` | `2.749` | `0.002613` |
| `2` | `te_harmonic_wise_full_rcim_baseline_reference` | `full RCIM` | `base_only` | `9.403` | `2.749` | `0.002726` |
| `3` | `te_harmonic_wise_full_rcim_engineered_deeper` | `full RCIM` | `engineered` | `9.562` | `2.749` | `0.002671` |
| `4` | `te_harmonic_wise_full_rcim_engineered_balanced` | `full RCIM` | `engineered` | `9.672` | `2.749` | `0.002720` |
| `5` | `te_harmonic_wise_h0134078_engineered_stage3` | `0,1,39,40,78` | `engineered` | `10.625` | `4.676` | `0.003114` |
| `6` | `te_harmonic_wise_h013_engineered_stage1` | `0,1,39` | `engineered` | `10.656` | `5.310` | `0.003168` |
| `7` | `te_harmonic_wise_h01340_engineered_stage2` | `0,1,39,40` | `engineered` | `10.797` | `5.178` | `0.003213` |
| `8` | `te_harmonic_wise_h013_random_forest_diagnostic` | `0,1,39` | `engineered + RF` | `12.084` | `5.310` | `0.003702` |

## Campaign Winner

The explicit campaign winner is:

- `te_harmonic_wise_full_rcim_no_engineering_reference`

Its result was:

- validation mean percentage error: `9.229%`
- test mean percentage error: `8.877%`
- oracle test mean percentage error: `2.749%`
- test MAE: `0.002613 deg`
- test RMSE: `0.002812 deg`

This run won because it produced the lowest held-out paper-comparable TE-curve
percentage error across all `8` completed configurations.

## Interpretation By Experiment Block

### 1. Full RCIM Won Again, And The Best Variant Improved The Baseline

The most important positive result is that the best full-RCIM run improved over
the first harmonic-wise baseline:

- previous full-RCIM baseline: `9.403%`
- new campaign winner: `8.877%`
- absolute gain: `0.526` percentage points

Interpretation:

- the second iteration did produce a real improvement;
- the full RCIM harmonic set remains the best-performing branch;
- the harmonic-wise path is now stronger than before, but still not close
  enough to the paper threshold.

### 2. Reduced Harmonic Staging Did Not Help The Predictor

The reduced-set progression was meant to test whether the predictor would
benefit from a simpler target space before promotion back to the full RCIM set.
That did not happen.

Observed held-out errors:

- `0,1,39`: `10.656%`
- `0,1,39,40`: `10.797%`
- `0,1,39,40,78`: `10.625%`

Interpretation:

- the predictor does not currently improve by dropping to the reduced subsets;
- the best reduced subset is still materially worse than the best full-RCIM
  configuration;
- the campaign therefore does not support keeping the reduced sets as the main
  deployment-facing offline branch.

### 3. The Oracle Results Explain Why Reduced Sets Are Weak Closing Targets

The oracle truncation results are as important as the predictor results.

Oracle held-out mean percentage errors:

- `0,1,39`: `5.310%`
- `0,1,39,40`: `5.178%`
- `0,1,39,40,78`: `4.676%`
- `full RCIM`: `2.749%`

Interpretation:

- the `0,1,39` and `0,1,39,40` subsets cannot realistically beat the paper
  threshold because even their truncation-only oracle remains above `4.7%`;
- the `0,1,39,40,78` subset is only barely good enough in oracle form and
  leaves almost no slack for predictor error;
- the full RCIM set is the only branch in this campaign with substantial
  headroom below the paper threshold.

This is the strongest argument against continuing to simplify the harmonic set
as the main optimization axis.

### 4. Engineered Features Did Not Improve The Full-RCIM Branch

The campaign explicitly tested engineered operating-condition features on the
full RCIM set:

- `full_rcim_engineered_balanced`: `9.672%`
- `full_rcim_engineered_deeper`: `9.562%`
- winning `base_only` full-RCIM run: `8.877%`

Interpretation:

- the added feature terms did not help on the full set in this iteration;
- deeper estimator capacity plus engineered features also failed to beat the
  simpler full-RCIM reference;
- the next step should therefore not prioritize more feature engineering of the
  same type.

### 5. RandomForest Confirmed That The Main Issue Is Not Just Estimator Choice

The diagnostic `RandomForest` run on the smallest staged set reached only:

- test mean percentage error: `12.084%`

Interpretation:

- `RandomForest` is clearly worse than the tuned harmonic-wise
  `HistGradientBoosting` baseline;
- this weakens the idea that the main problem is simply choosing the wrong
  tree family;
- the real bottleneck still looks more like target parameterization and error
  concentration than like missing estimator variety.

## Harmonic Error Findings

The winning full-RCIM run shows a very uneven error profile.

Dominant held-out per-harmonic coefficient errors:

- `h0`: coefficient MAE `0.002394`
- `h156`: coefficient MAE `0.000058`
- `h162`: coefficient MAE `0.000039`
- `h240`: coefficient MAE `0.000035`
- `h40`: coefficient MAE `0.000031`

Interpretation:

- the DC or offset term `h0` still dominates the harmonic prediction error by a
  wide margin;
- the next error cluster is concentrated in the higher-order harmonics
  `156`, `162`, and `240`;
- the next iteration should focus on target parameterization and per-harmonic
  specialization around these terms rather than further shrinking the harmonic
  set.

## Paper Alignment Impact

This campaign materially changes the `Track 1` picture in three ways.

### What Improved

- the repository-owned paper-faithful offline pipeline is no longer only a
  baseline proof of concept;
- the best full-RCIM result improved from `9.403%` to `8.877%`;
- the campaign clarified that the full RCIM harmonic set is still the correct
  optimization target.

### What Remains Open

- `Target A` remains `not_yet_met`;
- the remaining gap from the best campaign run to the paper threshold is
  `4.177` percentage points;
- the repository still cannot claim an offline match to the RCIM paper.

### What The Campaign Ruled Out

- reduced-set staging as the main optimization direction;
- repeated engineered-feature expansion as the main next lever;
- `RandomForest` as the likely missing estimator fix.

## Main Conclusions

The second `Track 1` campaign supports five conclusions.

### 1. Track 1 Improved, But It Is Not Closed

The pipeline is better than before, but the best result is still well above the
paper's `4.7%` offline threshold.

### 2. The Full RCIM Harmonic Set Must Remain The Mainline Branch

The reduced harmonic subsets are not strong enough, and their oracle limits
show that two of them cannot realistically satisfy `Target A`.

### 3. The Most Useful New Signal Is Structural, Not Merely Numerical

The campaign did not just say that one run was better. It showed that the next
optimization axis should move away from harmonic-count reduction and toward
better target representation plus per-harmonic specialization.

### 4. Feature Expansion Did Not Earn Promotion

The engineered feature variants were useful diagnostics, but they did not
improve the winning full-RCIM path and should not become the default branch.

### 5. The Offset Term And Late Harmonics Need Special Treatment

The dominant error ranking points directly at `h0` first, then `h156`, `h162`,
`h240`, and `h40`. That gives the next code pass a much sharper target.

## Recommended Next Actions

The next technically justified steps are:

1. keep `Track 1` as the immediate active branch;
2. start a third harmonic-wise iteration focused on target parameterization,
   especially:
   - explicit treatment of `h0` as its own target path;
   - selective target-format comparison between `cos/sin` and
     `amplitude/phase` on the dominant harmonics;
   - per-harmonic estimator overrides for the dominant error terms;
3. retain the full RCIM harmonic set as the promotion target for all serious
   `Target A` attempts;
4. delay `Track 2` until this next `Track 1` pass shows whether the paper-
   faithful branch can close more of the remaining offline gap.

## Artifact References

- Campaign artifact root:
  `output/training_campaigns/track1/harmonic_wise/2026-04-09-20-41-59_track1_second_iteration_harmonic_wise_campaign_2026_04_09_18_56_03/`
- Winning validation summary:
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-09-20-45-48__te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run/validation_summary.yaml`
- Winning run report:
  `doc/reports/analysis/validation_checks/track1/harmonic_wise/2026-04-09-20-46-45_paper_reimplementation_rcim_harmonic_wise_te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run_harmonic_wise_comparison_report.md`
- Planning report:
  `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-09-18-56-03_track1_second_iteration_harmonic_wise_campaign_plan_report.md`
