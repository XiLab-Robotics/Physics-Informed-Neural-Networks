# Remote Training Validation Campaign Plan Report

## Overview

This report defines the first real campaign intended to validate the new remote
LAN training workflow on the stronger workstation.

The campaign has two goals:

1. answer the already-open higher-memory follow-up question for the tree
   baselines, especially the random-forest branch;
2. validate that the new remote launcher can execute and synchronize both
   `scikit-learn` tree runs and Lightning-based feedforward runs.

This campaign is intentionally not a broad new model-family research wave. It
is a narrow operational plus engineering-value campaign:

- small enough to inspect carefully;
- broad enough to exercise both the CPU-heavy and GPU-heavy training paths;
- meaningful enough that the results are still worth keeping even if the main
  purpose is workflow validation.

## Why This Plan Makes Sense

The current repository state already gives a clear baseline.

Current global program leader:

- family: `tree`
- model type: `hist_gradient_boosting`
- test MAE: `0.002885 deg`
- output: `output/training_runs/tree/2026-03-20-15-17-30__te_hist_gbr_tabular/`

Current feedforward family best:

- family: `feedforward`
- test MAE: `0.003301 deg`
- output: `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/`

Current random-forest recovery reference:

- family: `tree`
- model type: `random_forest`
- test MAE: `0.003833 deg`
- output: `output/training_runs/tree/2026-03-20-17-15-25__te_random_forest_tabular_recovery/`

The random-forest branch is the clearest candidate for a stronger workstation
retry because:

- the original less-constrained configuration failed locally with a
  `MemoryError`;
- the later conservative recovery variant completed, but it was intentionally
  clamped by depth, leaf size, and single-process fit;
- the repository still records the higher-memory retry as a worthwhile open
  engineering question.

The feedforward branch should also be part of the campaign because the new
remote workflow must validate more than a CPU-only `tree_model.pkl` path. It
should also validate:

- remote Lightning execution;
- checkpoint-bearing run trees;
- feedforward family registry updates;
- mixed campaign synchronization across more than one family.

## Technical Context

The new remote launcher is already implemented, but not yet validated through a
real SSH-backed run on the stronger workstation.

The real validation should therefore check:

- remote workstation reachability;
- remote repository path correctness;
- remote Conda environment correctness;
- source sync from local to remote;
- remote campaign execution through `run_training_campaign.py`;
- sync back of:
  - `output/training_campaigns/`
  - `output/training_runs/`
  - `config/training/queue/completed/`
  - affected family registries
  - program best registry

The campaign should also avoid unnecessary novelty. It is better to validate
the remote workflow using configurations that are already coherent with the
repository's existing model space than to mix workflow testing with too many new
model-design assumptions.

## Technical Approach

The campaign should contain five runs split into two blocks.

### Block 1 - Tree Higher-Memory Follow-Up

This block answers the main workstation-upgrade question.

It should include:

1. one stronger but still bounded random forest;
2. one more aggressive random forest;
3. one stronger histogram-gradient-boosting reference probe.

The purpose is:

- check whether the random-forest family meaningfully benefits from the stronger
  workstation;
- check whether a stronger `hist_gradient_boosting` configuration can improve
  the already-leading tree baseline;
- keep the tree interpretation grounded in the current best family.

### Block 2 - Feedforward Remote GPU Validation

This block validates the non-tree remote path.

It should include:

1. one currently supported high-compute feedforward preset;
2. one denser and larger feedforward configuration from the earlier mixed
   campaign family.

The purpose is:

- validate remote Lightning execution on a heavier configuration;
- validate synchronization of checkpoints and full neural run artifacts;
- check whether stronger hardware makes one of the heavier feedforward
  configurations practically attractive again.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
- `scripts/training/run_training_campaign.py`
- `scripts/training/train_tree_regressor.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/tree_regression_support.py`
- `config/training/feedforward/`
- `config/training/tree/` through generated campaign YAML files
- `doc/running/active_training_campaign.yaml`
- `doc/scripts/campaigns/run_remote_training_campaign.md`

## Candidate Exploratory Matrix

| Config ID | Family | Planned Name | Main Parameters | Main Question |
| --- | --- | --- | --- | --- |
| 1 | Tree / Random Forest | `random_forest_remote_medium` | `n_estimators=500`, `max_depth=24`, `min_samples_leaf=3`, `n_jobs=8`, stride `5` | Does a materially less-constrained random forest become competitive when the stronger workstation removes the earlier local memory pressure? |
| 2 | Tree / Random Forest | `random_forest_remote_aggressive` | `n_estimators=800`, `max_depth=null`, `min_samples_leaf=2`, `n_jobs=8`, stride `5` | Does the more aggressive random-forest regime stay executable and improve enough to justify keeping the family alive beyond the conservative local rerun? |
| 3 | Tree / HistGradientBoosting | `hist_gbr_remote_deep` | `learning_rate=0.03`, `max_iter=800`, `max_depth=12`, `min_samples_leaf=10`, `max_bins=255` | Can a stronger histogram-gradient-boosting configuration improve over the current global tree leader on the stronger workstation? |
| 4 | Feedforward | `feedforward_high_compute_remote` | existing `high_compute` preset: `256-256-128-64`, stride `5`, batch `6`, long schedule | Does the current high-compute feedforward preset become a more practical contender when trained on the stronger remote GPU path? |
| 5 | Feedforward | `feedforward_stride1_big_remote` | `256-256-128-64`, stride `1`, batch `2`, long schedule | Does the full-density larger-model feedforward regime justify its cost when run on the stronger machine instead of the current workstation? |

## Parameter Notes

### Random Forest

- `n_estimators` scales ensemble strength and memory cost.
- `max_depth` is the main lever separating the previous conservative recovery
  run from the higher-memory retry.
- `min_samples_leaf` controls how fragmented the trees become.
- `n_jobs=8` is intentionally more aggressive than the local conservative path,
  but still bounded enough to avoid turning the first remote validation into a
  blind full-socket stress test.

Expected effect:

- if the earlier failure was mainly workstation memory pressure, the medium
  remote random forest should complete cleanly and may improve materially over
  the conservative local rerun;
- if the aggressive variant still fails or gives only weak gains, that is also
  useful evidence.

### HistGradientBoosting

- this family already leads the repository, so the remote follow-up should not
  ignore it;
- a stronger iteration budget and deeper trees test whether the current leader
  was already near saturation or still under-explored.

Expected effect:

- if the deeper boosting run improves the current best tree result, the remote
  campaign immediately produces a practically useful new reference;
- if it does not improve, the existing winner is strengthened as the stable
  tree anchor.

### Feedforward

- the `high_compute` preset is the cleanest supported heavy preset already
  exposed in the repository;
- the stride-1 larger-model configuration is the denser stress case worth
  checking on a stronger remote GPU.

Expected effect:

- the high-compute run validates the remote neural path with moderate risk;
- the stride-1 large-model run validates a clearly heavier checkpoint-producing
  branch that was more expensive to justify locally.

## Evaluation Rules

The campaign should still use the repository-standard selection policy:

- primary metric: `test_mae`
- first tie breaker: `test_rmse`
- second tie breaker: `val_mae`
- third tie breaker: `trainable_parameter_count`

The interpretation should also explicitly track:

- random-forest completion success versus memory instability;
- tree-family ranking change, if any;
- feedforward cost-versus-gain relative to the current best feedforward
  baseline;
- whether the remote synchronization path preserved all expected artifacts and
  registries without manual cleanup.

## Step-By-Step Operational Guide To Prepare

The implementation phase should provide an explicit operator guide that covers:

### Local Workstation

1. confirm SSH alias access, for example `ssh xilab-remote`;
2. confirm `STANDARDML_REMOTE_TRAINING_REPO_PATH` and
   `STANDARDML_REMOTE_TRAINING_CONDA_ENV` if those variables are being used;
3. confirm the approved campaign YAML package exists locally;
4. launch the remote campaign through the repository-owned launcher;
5. monitor:
   - `doc/running/remote_training_campaign_status.json`
   - `doc/running/remote_training_campaign_checklist.md`
   - `.temp/remote_training_campaigns/`

### Remote Workstation

1. confirm the repository clone exists at the expected path;
2. confirm the training Conda environment exists;
3. confirm the dataset path used by the configs is reachable on the remote
   machine;
4. confirm `ssh` and `tar.exe` based sync can operate against that clone;
5. confirm enough free disk space exists for the campaign outputs.

## Execution Gate

Before this campaign is launched:

1. the remote-validation technical document must be approved;
2. this campaign planning report must be approved;
3. the dedicated campaign YAML files must be generated;
4. the campaign state must be written to `doc/running/active_training_campaign.yaml`;
5. the exact local launch command must be provided;
6. the user must explicitly approve the prepared campaign before execution.

## Next Step

If this planning report is approved, generate the remote-validation campaign
YAML package, prepare the campaign state, add the step-by-step local/remote
operator guide, and provide the exact command for the first real SSH-backed
remote training validation run.
