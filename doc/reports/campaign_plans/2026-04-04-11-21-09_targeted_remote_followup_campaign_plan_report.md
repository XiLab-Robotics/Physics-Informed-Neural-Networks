# Targeted Remote Follow-Up Campaign Plan Report

## Overview

This report defines the next focused training campaign to run on the stronger
LAN workstation after the first real remote validation campaign.

The earlier remote pass already answered one important negative question:
`random_forest` is not worth promoting as a mainline family. It remains heavy,
artifact-expensive, and weaker than `hist_gradient_boosting` even on the
stronger workstation.

This follow-up campaign therefore stays selective and tests only the branches
that still have a credible path to changing the current ranking picture:

1. `residual_harmonic_mlp` as the strongest current neural family;
2. `feedforward` as the refreshed plain-MLP family now improved by the remote
   GPU path;
3. `hist_gradient_boosting` as the current global program leader with a small
   remaining tuning margin.

## Why This Plan Makes Sense

The current registry-backed anchors are:

- global program best:
  - family: `tree`
  - run: `te_hist_gbr_tabular`
  - validation MAE: `0.002719 deg`
  - test MAE: `0.002885 deg`
- strongest neural family:
  - family: `residual_harmonic_mlp`
  - run: `te_residual_h12_deep_joint_wave1`
  - validation MAE: `0.003024 deg`
  - test MAE: `0.003152 deg`
- refreshed `feedforward` family best:
  - family: `feedforward`
  - run: `te_feedforward_high_compute_remote`
  - validation MAE: `0.003059 deg`
  - test MAE: `0.003274 deg`

The first remote validation campaign also established three practical facts:

- the remote GPU path is real and stable enough for Lightning-based neural
  runs;
- the remote CPU path is useful for tree follow-ups;
- broad `random_forest` scaling is not attractive enough to justify another
  sweep right now.

## Technical Context

The campaign should remain narrow for two reasons:

1. the remote workflow is already validated, so the next step should prioritize
   model value rather than repeating a broad infrastructure test;
2. the families now deserve asymmetric treatment based on evidence:
   `residual_harmonic_mlp`, `feedforward`, and `hist_gradient_boosting` still
   have a plausible upside, while `random_forest` does not.

The intended use of the stronger workstation is therefore:

- longer neural schedules without overloading the local machine;
- denser curve sampling and moderate model-capacity increases where justified;
- a bounded tree-only refinement around the existing histogram-boosting leader.

## Technical Approach

The campaign should contain five runs.

### Block 1 - Residual-Harmonic Family Follow-Up

This block targets the strongest current neural family.

It should include:

1. one deeper-and-longer joint residual variant;
2. one denser or wider residual variant that tests whether the stronger remote
   machine helps this family more than the earlier local campaigns could.

### Block 2 - Feedforward Family Follow-Up

This block targets the refreshed plain-MLP baseline.

It should include:

1. one longer or slightly larger follow-up around
   `te_feedforward_high_compute_remote`;
2. one denser stride-1 follow-up that keeps the same core architecture but
   increases the compute budget more explicitly.

### Block 3 - HistGradientBoosting Refinement

This block remains intentionally narrow.

It should include:

1. one bounded refinement around the current tree leader so the stronger LAN
   workstation is also used for the globally leading family.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
- `scripts/training/run_training_campaign.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/train_residual_harmonic_mlp.py`
- `scripts/training/train_tree_regressor.py`
- `config/training/feedforward/`
- `config/training/residual_harmonic_mlp/`
- generated campaign YAML files for this campaign
- `doc/running/active_training_campaign.yaml`
- `doc/scripts/campaigns/run_remote_training_campaign.md`

## Candidate Exploratory Matrix

| Config ID | Family | Planned Name | Main Parameters | Main Question |
| --- | --- | --- | --- | --- |
| 1 | `residual_harmonic_mlp` | `residual_h12_deep_long_remote` | order `12`, hidden `128-128-64`, joint mode, stride `5`, max epochs `320`, patience `45` | Does the current best neural family improve further when the deeper joint variant gets the longer optimization budget that was only lightly explored before? |
| 2 | `residual_harmonic_mlp` | `residual_h12_deep_dense_remote` | order `12`, hidden `128-128-64`, joint mode, stride `3`, curve batch `4`, max epochs `250` | Does a denser angular sampling regime help the stronger residual architecture more than the earlier stride-5 search? |
| 3 | `feedforward` | `feedforward_high_compute_long_remote` | hidden `256-256-128-64`, stride `5`, curve batch `6`, max epochs `320`, patience `45` | Does the new feedforward family best still improve when given a longer schedule without changing the data regime too aggressively? |
| 4 | `feedforward` | `feedforward_stride1_high_compute_long_remote` | hidden `256-256-128-64`, stride `1`, curve batch `2`, max epochs `320`, patience `45` | Does the denser full-resolution feedforward branch become more attractive when the remote GPU absorbs the heavier runtime budget? |
| 5 | `tree` | `hist_gbr_remote_refined` | learning rate `0.025`, max iter `1000`, max depth `10`, min samples leaf `8`, max bins `255`, stride `5` | Can a bounded refinement around histogram boosting recover the small remaining gap between the current global best and the earlier remote deep probe? |

## Parameter Notes

### Residual-Harmonic MLP

- the family already leads the neural branches, so the strongest case for more
  remote compute is here;
- the deeper joint residual branch is the cleanest current anchor;
- testing a denser regime is worth it because the family may benefit from a
  better-resolved angular signal without collapsing into the extreme cost of a
  full broad sweep.

Expected effect:

- if the longer or denser residual variants improve materially, the repository
  gets a stronger neural comparison anchor;
- if they plateau, that also sharpens the evidence that the family is already
  near its current ceiling.

### Feedforward

- the remote validation already proved that the plain feedforward branch still
  improves under stronger compute;
- the next useful question is whether the improvement saturates quickly or
  whether longer schedules and denser point sampling still move the metric.

Expected effect:

- the longer stride-5 variant is the lower-risk extension of the current family
  best;
- the denser stride-1 variant is the more compute-hungry probe that the remote
  GPU can justify better than the local workstation.

### HistGradientBoosting

- this family still owns the overall leaderboard, so it should not be left
  untouched while only neural families receive more budget;
- the refinement must remain bounded because the earlier remote deep run was
  already strong and the remaining margin is small.

Expected effect:

- a small gain would immediately matter because it would improve the global best
  solution;
- a null result would still validate that the current leader is already close
  to saturation.

## Evaluation Rules

The campaign should keep the repository-standard ranking policy:

- primary metric: `test_mae`
- first tie breaker: `test_rmse`
- second tie breaker: `val_mae`
- third tie breaker: `trainable_parameter_count`

The final interpretation should also track:

- whether the residual family closes part of the gap to the tree leader;
- whether the plain `feedforward` branch still improves with more budget;
- whether the refined histogram-boosting run can beat the current global best;
- whether the remote workflow stays clean across a mixed campaign without
  manual artifact recovery.

## Step-By-Step Operational Guide To Prepare

The implementation phase should provide an explicit operator guide that covers:

### Local Workstation

1. confirm the SSH alias still resolves, for example `ssh xilab-remote`;
2. confirm the remote repository path and Conda environment variables or pass
   them explicitly at launch;
3. confirm the approved campaign YAML package exists locally;
4. launch the dedicated remote campaign launcher;
5. monitor:
   - `doc/running/remote_training_campaign_status.json`
   - `doc/running/remote_training_campaign_checklist.md`
   - `.temp/remote_training_campaigns/`

### Remote Workstation

1. confirm the repository clone exists at
   `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`;
2. confirm the environment `standard_ml_lan_node` exists and still exposes
   `torch.cuda.is_available() == True`;
3. confirm the dataset path used by the configs is available on the remote
   machine;
4. confirm enough free disk space exists for campaign outputs and checkpoints.

## Execution Gate

Before this campaign is launched:

1. the technical document must be approved;
2. this planning report must be approved;
3. the dedicated YAML package must be generated;
4. the campaign state must be written to `doc/running/active_training_campaign.yaml`;
5. the exact launch command must be provided;
6. the user must explicitly approve the prepared campaign before execution.

## Next Step

If this planning report is approved, generate the targeted remote follow-up
campaign package, create the dedicated launcher and launcher note, update the
active campaign state, and provide the exact command for the real LAN-remote
execution.
