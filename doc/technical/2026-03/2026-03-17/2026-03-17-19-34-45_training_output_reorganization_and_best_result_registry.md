# Training Output Reorganization And Best Result Registry

## Overview

The current training artifact layout is functional but already shows an avoidable scaling problem.

Today the repository stores:

- per-run feedforward artifacts under `output/feedforward_network/<run_name>/`;
- campaign-level manifests and reports under `output/training_campaigns/<campaign_id>/`;
- validation and smoke-test artifacts mixed into the same family root through run-name suffixes such as `*_wave0_validation` and `*_wave0_smoke_test`.

This creates three practical issues:

1. the output root mixes different artifact categories;
2. repeated reruns of the same logical configuration are not clearly separated from each other;
3. the best result after one or more campaigns is not visible through a single canonical location.

The goal of this change is to define a scalable output layout that works not only for `feedforward`, but also for every future TE model family in the backlog.

## Technical Approach

The proposed reorganization uses four principles.

### 1. Separate By Artifact Type First

Training runs, validation checks, smoke tests, and campaign summaries should not compete in the same directory level.

Proposed top-level layout:

```text
output/
  training_runs/
    <model_family>/
      <run_instance_id>/
  validation_checks/
    <model_family>/
      <validation_id>/
  smoke_tests/
    <model_family>/
      <smoke_test_id>/
  training_campaigns/
    <campaign_id>/
  registries/
    families/
      <model_family>/
    program/
```

This keeps the output tree readable even when the number of families and campaigns grows.

### 2. Distinguish Logical Run Name From Physical Run Instance

The current layout uses `<run_name>` as the physical folder name.

That is convenient, but it has a structural weakness: rerunning the same configuration writes again into the same location and weakens traceability.

The proposal is to introduce:

- `run_name`: the logical experiment identity coming from the config;
- `run_instance_id`: the physical artifact folder identifier, for example:
  - `2026-03-17-20-05-11__te_feedforward_baseline`

This keeps the human-readable run name while making each execution immutable.

### 3. Add Stable Registries For Best Results

The best result should not be inferred manually by browsing checkpoints.

Instead, the repository should write explicit registry files:

```text
output/
  registries/
    families/
      feedforward/
        latest_family_best.yaml
        leaderboard.yaml
    program/
      current_best_solution.yaml
```

Recommended semantics:

- `latest_family_best.yaml`
  points to the current best training run for that family;
- `leaderboard.yaml`
  stores ranked run summaries for that family;
- `current_best_solution.yaml`
  stores the current program-wide best candidate across all implemented families.

These files should contain:

- run instance id;
- logical run name;
- campaign id if applicable;
- model family and model type;
- main selection metric;
- validation/test metrics;
- checkpoint path;
- metrics/report path;
- selection timestamp;
- optional note explaining why the run is currently considered best.

### 4. Make Campaign Winners Explicit Inside Campaign Folders

Each campaign folder should expose its own winner without requiring the user to inspect the full report first.

Recommended additions under:

- `output/training_campaigns/<campaign_id>/`

Artifacts:

- `campaign_manifest.yaml`
- `campaign_execution_report.md`
- `campaign_leaderboard.yaml`
- `campaign_best_run.yaml`
- `campaign_best_run.md`

The campaign-local winner should then be eligible for promotion into:

- `output/registries/families/<model_family>/latest_family_best.yaml`

and, if it is the best overall candidate so far:

- `output/registries/program/current_best_solution.yaml`

## Proposed Concrete Layout

The recommended concrete layout is:

```text
output/
  training_runs/
    feedforward/
      2026-03-17-20-05-11__te_feedforward_baseline/
        training_config.yaml
        metrics_summary.yaml
        training_test_report.md
        best_checkpoint_path.txt
        checkpoints/
        logs/
  validation_checks/
    feedforward/
      2026-03-17-20-05-11__te_feedforward_trial_validation/
        validation_summary.yaml
  smoke_tests/
    feedforward/
      2026-03-17-20-05-11__te_feedforward_trial_smoke/
        smoke_test_summary.yaml
  training_campaigns/
    2026-03-17-20-20-00_wave1_structured_baselines/
      campaign_manifest.yaml
      campaign_execution_report.md
      campaign_leaderboard.yaml
      campaign_best_run.yaml
      campaign_best_run.md
      logs/
  registries/
    families/
      feedforward/
        latest_family_best.yaml
        leaderboard.yaml
    program/
      current_best_solution.yaml
```

## Why This Is Better

Advantages:

- validation and smoke-test artifacts stop polluting the main training-run root;
- repeated reruns of the same configuration become traceable and non-destructive;
- campaign-level and family-level best results become explicit;
- the structure generalizes cleanly to `temporal`, `hybrid`, `pinn`, and future families;
- the user can answer three different questions immediately:
  - what did this specific run produce?
  - what was the winner of this campaign?
  - what is the best current solution for this family or for the full program?

Main tradeoff:

- the path structure becomes a little deeper;
- therefore a small registry/index layer is necessary.

This tradeoff is worth it because it removes ambiguity and avoids silent overwrites.

## Migration Strategy

The safest migration path is incremental.

### Phase 1. New Layout For Future Artifacts

Update the shared training infrastructure so new training runs, validation checks, and smoke tests write into the new category-specific roots.

### Phase 2. Campaign Best-Run Metadata

Extend the campaign runner so it always emits:

- `campaign_leaderboard.yaml`
- `campaign_best_run.yaml`
- `campaign_best_run.md`

### Phase 3. Family And Program Registries

Add a registry update step after campaign completion or after explicit best-run confirmation.

### Phase 4. Optional Historical Migration

Optionally migrate or index the existing `output/feedforward_network/` folders into the new structure.

This historical migration is useful, but not required to start.

## Recommended Selection Rules

To make the `best` concept stable, the repository should define an explicit selection policy.

Recommended default:

1. primary ranking metric:
   `test_mae`
2. first tie-breaker:
   `test_rmse`
3. second tie-breaker:
   `val_mae`
4. optional deployment tie-breaker:
   smaller parameter count or better deployment suitability

The chosen rule should be serialized into:

- `campaign_best_run.yaml`
- `latest_family_best.yaml`
- `current_best_solution.yaml`

so the decision remains inspectable.

## Involved Components

- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/validate_training_setup.py`
- `scripts/training/run_training_smoke_test.py`
- `scripts/training/run_training_campaign.py`
- `doc/guide/project_usage_guide.md`
- `doc/running/te_model_live_backlog.md`

## Implementation Steps

1. Introduce category-specific output roots for training runs, validation checks, and smoke tests.
2. Introduce timestamped `run_instance_id` paths while keeping `run_name` inside the metadata.
3. Extend the campaign runner to emit campaign-local best-run and leaderboard artifacts.
4. Add family-level and program-level best-result registry files.
5. Update the usage guide so users know where to inspect:
   - run artifacts;
   - campaign winners;
   - family best results;
   - global best solution.
6. Optionally add a historical indexing or migration step for the legacy `output/feedforward_network/` tree.

## Recommendation

The recommended direction is:

- keep `output/training_campaigns/` as the campaign root;
- replace the current family-root-only run layout with `output/training_runs/<family>/<run_instance_id>/`;
- move validation and smoke artifacts into dedicated roots;
- add stable best-result registries under `output/registries/`.

This gives the cleanest long-term structure and makes the best result visible at campaign, family, and program level without relying on manual folder inspection.
