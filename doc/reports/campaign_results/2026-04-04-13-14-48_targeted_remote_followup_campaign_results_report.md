# Targeted Remote Follow-Up Campaign Results Report

## Overview

This report summarizes the focused LAN-remote follow-up campaign prepared in:

- `doc/reports/campaign_plans/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`

The campaign was intentionally narrow and tested only the branches that still
looked worth pushing on the stronger LAN workstation:

- `residual_harmonic_mlp`
- `feedforward`
- `hist_gradient_boosting`

The campaign completed all planned runs on the remote workstation:

- completed runs: `5`
- failed runs: `0`
- remote execution window: `2026-04-04T11:49:11` to `2026-04-04T13:03:55`
- campaign artifact root:
  `output/training_campaigns/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/`

One operational caveat remains:

- the remote training itself completed successfully;
- the local launcher still failed during the post-run return path;
- the canonical local artifact set for this report was recovered manually from
  the remote workstation after the run.

## Objective And Outcome

The campaign had three concrete questions:

1. can `residual_harmonic_mlp` close more of the gap to the tree leader with a
   stronger remote compute budget?
2. can the refreshed `feedforward` family improve again now that the remote GPU
   path is already validated?
3. does a narrow `hist_gradient_boosting` refinement recover the small margin
   between the current global best and the previous remote tree probe?

The answers are clear:

- `hist_gradient_boosting` won the campaign again, but the refined run was
  worse than both the global tree leader and the earlier remote deep tree run;
- the `feedforward` family improved again and now has a new family best;
- the `residual_harmonic_mlp` family did not improve and remained behind its
  earlier `Wave 1` best.

## Ranking Policy

The campaign ranking follows the repository-standard policy stored in
`campaign_leaderboard.yaml`:

- primary metric: `test_mae`
- first tie breaker: `test_rmse`
- second tie breaker: `val_mae`
- third tie breaker: `trainable_parameter_count`

## Campaign Ranking

### Ranked Completed Runs

| Rank | Config | Family | Runtime | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `1` | `te_hist_gbr_remote_refined` | `tree` | 1.8 min | 0.003101 | 0.003781 | 0.002809 |
| `2` | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` | 30.1 min | 0.003264 | 0.003679 | 0.003044 |
| `3` | `te_residual_h12_deep_dense_remote` | `residual_harmonic_mlp` | 13.5 min | 0.003365 | 0.003868 | 0.003018 |
| `4` | `te_residual_h12_deep_long_remote` | `residual_harmonic_mlp` | 16.0 min | 0.003384 | 0.003908 | 0.002973 |
| `5` | `te_feedforward_high_compute_long_remote` | `feedforward` | 13.4 min | 0.003542 | 0.004228 | 0.003058 |

## Campaign Winner

The explicit campaign winner is:

- `te_hist_gbr_remote_refined`

Its result was:

- validation MAE: `0.002809 deg`
- validation RMSE: `0.003687 deg`
- test MAE: `0.003101 deg`
- test RMSE: `0.003781 deg`

This run won the campaign because it remained the lowest-test-MAE entry among
the five completed candidates.

## Interpretation By Family

### 1. HistGradientBoosting Still Owns The Overall Program Lead, But This Refinement Did Not Help

The tree-only refinement completed quickly and cleanly:

- runtime: `1.8 min`
- validation MAE: `0.002809 deg`
- test MAE: `0.003101 deg`

Interpretation:

- the family still owns the global leaderboard through
  `te_hist_gbr_tabular` at `test_mae = 0.002885 deg`;
- this refined remote run is worse than the global best;
- it is also worse than the earlier remote tree probe
  `te_hist_gbr_remote_deep` at `test_mae = 0.002920 deg`.

So this campaign does not justify more immediate tree refinement. It instead
strengthens the view that the current tree leader was already near saturation.

### 2. Feedforward Improved Again And Produced A New Family Best

The two feedforward follow-ups diverged clearly.

`te_feedforward_stride1_high_compute_long_remote`:

- validation MAE: `0.003044 deg`
- test MAE: `0.003264 deg`
- test RMSE: `0.003679 deg`
- runtime: `30.1 min`

`te_feedforward_high_compute_long_remote`:

- validation MAE: `0.003058 deg`
- test MAE: `0.003542 deg`
- test RMSE: `0.004228 deg`
- runtime: `13.4 min`

Interpretation:

- the stride-1 longer-budget variant became the new `feedforward` family best;
- it improved over the previous family best
  `te_feedforward_high_compute_remote` at `test_mae = 0.003274 deg`;
- the gain is small but real, and it also came with a strong `test_rmse`;
- the longer stride-5 follow-up did not help and regressed materially.

This confirms that the remote GPU path is still worth using for selective
plain-MLP densification, but not every longer-budget extension is useful.

### 3. Residual-Harmonic Did Not Improve On Its Existing Neural Anchor

The two residual-harmonic follow-ups both completed:

`te_residual_h12_deep_dense_remote`:

- validation MAE: `0.003018 deg`
- test MAE: `0.003365 deg`
- test RMSE: `0.003868 deg`

`te_residual_h12_deep_long_remote`:

- validation MAE: `0.002973 deg`
- test MAE: `0.003384 deg`
- test RMSE: `0.003908 deg`

Interpretation:

- both runs underperformed the family anchor
  `te_residual_h12_deep_joint_wave1` at `test_mae = 0.003152 deg`;
- the denser run was the better of the two new residual variants, but still
  clearly behind the existing family best;
- the longer-budget variant improved validation MAE but did not translate that
  into better held-out test error.

This suggests that the current residual-harmonic family is not benefiting from
these particular deeper-and-denser remote follow-ups.

## Family Registry Impact

The campaign changed the family picture in only one place.

### Updated Family Bests

| Family | Best Run After This Campaign | Test MAE [deg] | Status |
| --- | --- | ---: | --- |
| `tree` | `te_hist_gbr_tabular` | 0.002885 | Unchanged global program leader |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | 0.003152 | Unchanged neural family leader |
| `feedforward` | `te_feedforward_stride1_high_compute_long_remote` | 0.003264 | New family best |

### Program-Level Context

According to the synced registries:

- `feedforward` has a new family best;
- `residual_harmonic_mlp` did not change family leader;
- `tree` still owns the program-level best through `te_hist_gbr_tabular`.

So the broader ranking after this campaign is:

1. global program best still belongs to `te_hist_gbr_tabular`;
2. best current neural family remains `residual_harmonic_mlp`;
3. best current plain MLP is now
   `te_feedforward_stride1_high_compute_long_remote`.

## Remote Workflow Findings

The campaign also produced a useful workflow conclusion.

### Remote Training Execution Worked

The remote workstation completed:

- all `5` queued runs;
- all per-run artifact trees;
- the campaign manifest;
- the campaign leaderboard and best-run artifacts;
- the updated family and program registries.

### Local Return Path Still Needs Hardening

The current launcher transport fix removed the original Windows
`command line is too long` blocker.

However, the local launcher still did not finish the run end to end:

- remote execution completed;
- local stdout capture failed again during the remote-run stage;
- the final local repository state had to be recovered manually from the remote
  artifacts.

This is now a narrower remaining launcher issue than before:

- remote execution is real and stable;
- artifact identity is correct;
- the remaining defect is in local post-run command handling and automated
  sync completion.

## Main Conclusions

The targeted follow-up campaign supports five concrete conclusions.

### 1. The Stronger LAN Workstation Was Worth Using Selectively

The campaign delivered one real family-level improvement and one clear negative
result, which is exactly what a selective follow-up should do.

### 2. Feedforward Still Had A Small Remaining Upside

The stride-1 longer-budget remote variant became the new feedforward family
best and confirms that plain MLP tuning was not yet fully exhausted.

### 3. Residual-Harmonic Did Not Benefit From This Specific Follow-Up Shape

The two tested residual variants did not beat the existing family anchor, so
the next residual campaign should not simply repeat the same axes with more
budget.

### 4. HistGradientBoosting Does Not Currently Need More Immediate Refinement

The refined tree run won the local campaign ranking, but it did not improve the
actual global tree leader. That lowers the priority of near-term tree retuning.

### 5. The Remote Launcher Is Operationally Closer, But Still Not Fully Closed

The campaign no longer fails on command-line length, but the local completion
path still needs one more hardening pass before the launcher can be treated as
fully hands-off for long mixed campaigns.

## Recommended Next Actions

The next technically useful steps are:

1. keep `te_feedforward_stride1_high_compute_long_remote` as the new
   `feedforward` family anchor;
2. keep `te_residual_h12_deep_joint_wave1` as the `residual_harmonic_mlp`
   family anchor until a more meaningfully different residual idea is tested;
3. keep `te_hist_gbr_tabular` as the global program reference and deprioritize
   immediate tree retuning;
4. harden the remaining local sync-completion path in
   `run_remote_training_campaign.ps1` so long remote runs return cleanly to the
   local repository without manual recovery;
5. if another model-side campaign is planned soon, prioritize a more targeted
   neural follow-up rather than another broad mixed family sweep.

## Artifact References

Campaign-level references:

- `output/training_campaigns/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/campaign_manifest.yaml`
- `output/training_campaigns/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/campaign_execution_report.md`
- `output/training_campaigns/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/campaign_leaderboard.yaml`
- `output/training_campaigns/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/campaign_best_run.yaml`
- `output/training_campaigns/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/campaign_best_run.md`

Key per-run references:

- `output/training_runs/residual_harmonic_mlp/2026-04-04-11-49-11__te_residual_h12_deep_long_remote/`
- `output/training_runs/residual_harmonic_mlp/2026-04-04-12-05-09__te_residual_h12_deep_dense_remote/`
- `output/training_runs/feedforward/2026-04-04-12-18-37__te_feedforward_high_compute_long_remote/`
- `output/training_runs/feedforward/2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote/`
- `output/training_runs/tree/2026-04-04-13-02-09__te_hist_gbr_remote_refined/`
