# Track 1 Overnight Gap-Closure Campaign Results Report

## Overview

This report closes the overnight `Track 1` campaign prepared in:

- `doc/reports/campaign_plans/2026-04-13-00-55-21_track1_overnight_gap_closure_campaign_plan_report.md`

The package executed `20` repository-owned harmonic-wise validation runs
through one coordinated launcher:

- completed runs: `20`
- failed runs: `0`
- execution window: `2026-04-13T01:42:34+02:00` to `2026-04-13T02:00:49+02:00`
- campaign artifact root:
  `output/training_campaigns/track1_overnight_gap_closure_campaign_2026_04_13_01_02_23/`

The overnight batch was organized into four logical experiment blocks:

- `Campaign A`: low-order `HGBM` ladder
- `Campaign B`: late-harmonic repair ladder
- `Campaign C`: `RandomForest` counterfactuals
- `Campaign D`: engineered-term recovery

## Objective And Outcome

The campaign had four concrete questions:

1. can the current harmonic-wise baseline improve through stronger low-order
   treatment on `h0` and `h1`;
2. can late-harmonic specialization reduce the remaining paper-table pressure
   around `162` and `240`;
3. does `RandomForest` become competitive when tuned around the open harmonics;
4. do engineered operating-condition terms help when combined with targeted
   harmonic overrides instead of broad promotion.

Outcome:

- the batch completed successfully with `20/20` runs and no observed launcher
  failures;
- the campaign winner is `track1_hgbm_h01_shallow_regularized`;
- the best test mean percentage error improved from the previous repository
  best `8.877%` to `8.774%`;
- the improvement is real but still small, so `Target A` remains
  `not_yet_met` against the paper threshold `4.7%`;
- the strongest alternatives are still `HGBM`, especially the low-order and
  late-harmonic repair ladders;
- `RandomForest` remained clearly non-competitive for the shared offline
  evaluator in this campaign;
- the engineered-term re-check did not justify promotion over the best
  no-engineering `HGBM` runs.

## Ranking Policy

The campaign winner uses the explicit ranking rule approved in the campaign
plan:

- eligible winner set: all completed runs that emit the shared offline
  evaluator;
- primary metric: `test_mean_percentage_error_pct`;
- first tie breaker: `test_curve_mae_deg`;
- second tie breaker: `test_curve_rmse_deg`;
- third tie breaker: lexical `run_name`;
- direction: minimize.

This policy is serialized under:

- `output/training_campaigns/track1_overnight_gap_closure_campaign_2026_04_13_01_02_23/campaign_leaderboard.yaml`

## Ranked Completed Runs

<!-- markdownlint-disable MD013 -->
| Rank | Config | Block | Test MPE [%] | Curve MAE [deg] | Curve RMSE [deg] |
| ---: | --- | --- | ---: | ---: | ---: |
| `1` | `track1_hgbm_h01_shallow_regularized` | `A` | 8.774 | 0.002578 | 0.002776 |
| `2` | `track1_hgbm_h162_h240_repair` | `B` | 8.795 | 0.002578 | 0.002776 |
| `3` | `track1_hgbm_h013_deeper_low_order` | `A` | 8.954 | 0.002626 | 0.002823 |
| `4` | `track1_hgbm_h081_h162_h240_repair` | `B` | 8.959 | 0.002600 | 0.002797 |
| `5` | `track1_hgbm_h01_ultradeep_guarded` | `A` | 8.996 | 0.002672 | 0.002869 |
| `6` | `track1_hgbm_h013_h162_h240_joint` | `B` | 9.067 | 0.002674 | 0.002870 |
| `7` | `track1_hgbm_h156_h162_h240_repair` | `B` | 9.162 | 0.002665 | 0.002866 |
| `8` | `track1_hgbm_h039_h162_h240_bridge` | `B` | 9.167 | 0.002665 | 0.002866 |
| `9` | `track1_hgbm_h01_deeper_low_order` | `A` | 9.199 | 0.002697 | 0.002890 |
| `10` | `track1_hgbm_h240_extreme_focus` | `B` | 9.273 | 0.002703 | 0.002903 |
| `11` | `track1_hgbm_h0139_low_order_anchor` | `A` | 9.288 | 0.002738 | 0.002932 |
| `12` | `track1_hgbm_h014078_low_order_anchor` | `A` | 9.305 | 0.002744 | 0.002939 |
| `13` | `track1_hgbm_h162_h240_engineered_recheck` | `D` | 9.408 | 0.002655 | 0.002857 |
| `14` | `track1_hgbm_h013_engineered_recheck` | `D` | 9.501 | 0.002650 | 0.002852 |
| `15` | `track1_hgbm_h01_engineered_recheck` | `D` | 9.532 | 0.002671 | 0.002873 |
| `16` | `track1_rf_h01_h081_engineered_recheck` | `D` | 10.936 | 0.003234 | 0.003426 |
| `17` | `track1_rf_h081_focus` | `C` | 11.166 | 0.003315 | 0.003500 |
| `18` | `track1_rf_h156_h162_h240_focus` | `C` | 11.176 | 0.003318 | 0.003502 |
| `19` | `track1_rf_full_rcim_reference` | `C` | 11.183 | 0.003318 | 0.003502 |
| `20` | `track1_rf_h01_focus` | `C` | 11.190 | 0.003319 | 0.003503 |

| Config | Validation MPE [%] | Oracle Test MPE [%] | Delta Vs `8.877%` Baseline |
| --- | ---: | ---: | ---: |
| `track1_hgbm_h01_shallow_regularized` | 9.611 | 2.749 | -0.103 |
| `track1_hgbm_h162_h240_repair` | 9.448 | 2.749 | -0.082 |
| `track1_hgbm_h013_deeper_low_order` | 9.479 | 2.749 | +0.078 |
| `track1_hgbm_h081_h162_h240_repair` | 9.361 | 2.749 | +0.082 |
| `track1_hgbm_h01_ultradeep_guarded` | 9.804 | 2.749 | +0.119 |
<!-- markdownlint-enable MD013 -->

## Best Run Per Block

<!-- markdownlint-disable MD013 -->
| Block | Best Config | Test MPE [%] | Interpretation |
| --- | --- | ---: | --- |
| `A` | `track1_hgbm_h01_shallow_regularized` | 8.774 | Mildly regularized low-order specialization worked better than deeper aggressive variants. |
| `B` | `track1_hgbm_h162_h240_repair` | 8.795 | Late-harmonic repair is still useful and nearly tied with the winner. |
| `C` | `track1_rf_h081_focus` | 11.166 | `RandomForest` remained far from competitive on the shared evaluator. |
| `D` | `track1_hgbm_h162_h240_engineered_recheck` | 9.408 | Engineered terms did not recover enough value to beat the best no-engineering runs. |
<!-- markdownlint-enable MD013 -->

## Campaign Winner

The explicit campaign winner is:

- `track1_hgbm_h01_shallow_regularized`

Its result was:

- test mean percentage error: `8.774%`
- test curve MAE: `0.002578 deg`
- test curve RMSE: `0.002776 deg`
- oracle test mean percentage error: `2.749%`
- previous shared-evaluator best: `8.877%`
- absolute improvement versus previous best: `0.103 percentage points`
- Target A threshold: `4.7%`
- Target A status: `not_yet_met`

This run won because it is the lowest-error completed candidate under the
shared offline evaluator, and it beat both the previous repository best and
the strongest late-harmonic repair variant.

## Interpretation By Experiment Block

### 1. Low-Order Treatment Still Matters Most

The campaign winner came from the low-order `HGBM` ladder.

Important evidence:

- `track1_hgbm_h01_shallow_regularized`: `8.774%`
- `track1_hgbm_h013_deeper_low_order`: `8.954%`
- `track1_hgbm_h01_ultradeep_guarded`: `8.996%`
- `track1_hgbm_h01_deeper_low_order`: `9.199%`

Interpretation:

- `h0 / h1` are still the main leverage point for TE-level improvement;
- more capacity was not automatically better;
- the winning direction was not the deepest ladder, but the more controlled
  low-order regularized variant.

### 2. Late-Harmonic Repair Is Real But Secondary

The best late-harmonic run finished almost tied with the winner:

- `track1_hgbm_h162_h240_repair`: `8.795%`

Interpretation:

- the late-harmonic block around `162` and `240` still matters;
- however, late-harmonic repair alone did not surpass the best low-order run;
- the next iteration should probably keep both directions alive instead of
  replacing one with the other.

### 3. `RandomForest` Did Not Reproduce The Paper Direction Here

All `RandomForest` runs ranked at the bottom:

- best `RF`: `track1_rf_h081_focus` at `11.166%`
- worst `RF`: `track1_rf_h01_focus` at `11.190%`

Interpretation:

- under the current coefficient-based shared evaluator, `RF` is not a viable
  promotion candidate;
- this does not invalidate the paper's per-harmonic family choices, but it
  does show that the current repository harmonic-wise path still strongly
  favors `HGBM` over `RF`.

### 4. Engineered Terms Did Not Earn Promotion

The best engineered run was:

- `track1_hgbm_h162_h240_engineered_recheck`: `9.408%`

Interpretation:

- the engineered operating-condition terms remain weaker than the best
  no-engineering `HGBM` configurations for this branch;
- the overnight batch therefore does not justify making engineered terms the
  new `Track 1` default.

## Recommended Next Step

The batch improved the shared evaluator, but not enough to change the overall
`Track 1` verdict.

The most defensible next step is:

1. promote `track1_hgbm_h01_shallow_regularized` as the new shared-evaluator
   reference;
2. keep `track1_hgbm_h162_h240_repair` as the strongest late-harmonic repair
   companion;
3. start the next `Track 1` iteration around a combined low-order plus
   late-harmonic specialization path;
4. if that still plateaus near `8.7-8.8%`, move the next research step to a
   new target-parameterization implementation rather than another `RF` or
   engineered-feature retry.

## Artifact References

- `output/training_campaigns/track1_overnight_gap_closure_campaign_2026_04_13_01_02_23/campaign_leaderboard.yaml`
- `output/training_campaigns/track1_overnight_gap_closure_campaign_2026_04_13_01_02_23/campaign_best_run.yaml`
- `output/training_campaigns/track1_overnight_gap_closure_campaign_2026_04_13_01_02_23/campaign_best_run.md`
