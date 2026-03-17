# Legacy Feedforward Output Migration

## Overview

The repository now uses the new output structure introduced by the training-output reorganization:

- `output/training_runs/`
- `output/validation_checks/`
- `output/smoke_tests/`
- `output/training_campaigns/`
- `output/registries/`

However, the legacy folder:

- `output/feedforward_network/`

still contains the historical feedforward run artifacts produced before the new layout was implemented.

The user now wants to complete the migration by:

1. moving the historical contents of `output/feedforward_network/` into the new structure;
2. updating the old technical documents, reports, guides, and other repository-authored references so they point to the new paths.

## Technical Approach

The migration should be treated as a historical artifact normalization task, not as a new training campaign.

### 1. Preserve Each Historical Run As A Distinct Training Run Folder

Each subdirectory currently under:

- `output/feedforward_network/<legacy_run_name>/`

will be migrated into:

- `output/training_runs/feedforward/<run_instance_id>/`

Because the old layout stored artifacts only under the logical run name, the migration must introduce a stable legacy `run_instance_id`.

Recommended convention:

- `legacy__<legacy_run_name>`

Examples:

- `output/feedforward_network/te_feedforward_baseline/`
  ->
  `output/training_runs/feedforward/legacy__te_feedforward_baseline/`

- `output/feedforward_network/te_feedforward_high_epoch/`
  ->
  `output/training_runs/feedforward/legacy__te_feedforward_high_epoch/`

This keeps the migrated folders:

- deterministic;
- human-readable;
- clearly distinguishable from new timestamped runs.

### 2. Preserve Existing Historical Artifacts As-Is Where Possible

Inside each migrated historical run folder, existing artifacts should remain intact:

- checkpoints;
- logs;
- `best_checkpoint_path.txt`;
- `training_test_metrics.yaml`;
- `training_test_report.md`;
- legacy config snapshots.

Additional normalization files may be added when useful, especially:

- `run_metadata.yaml`
- `metrics_summary.yaml` when the old run only has the legacy metric filename

The migration should avoid recomputing model outputs. It should only reorganize and normalize metadata.

### 3. Rebuild Family And Program Registries From The Migrated Historical Runs

After migrating the historical directories, the repository should rescan the migrated feedforward runs and rebuild:

- `output/registries/families/feedforward/leaderboard.yaml`
- `output/registries/families/feedforward/latest_family_best.yaml`
- `output/registries/program/current_best_solution.yaml`

This step is necessary so the best-result view reflects both:

- old migrated historical runs;
- new post-reorganization runs.

### 4. Update Repository-Authored Path References

The repository contains many historical documents that still reference:

- `output/feedforward_network/...`

These should be updated when they are part of the repository-authored active documentation or historical technical/reporting material that is expected to remain navigable.

The migration scope should include:

- `doc/guide/project_usage_guide.md`
- `doc/scripts/training/*.md`
- `doc/running/*.md` when applicable
- historical technical notes under `doc/technical/`
- historical analytical and campaign-result reports under `doc/reports/`
- top-level `README.md` and `doc/README.md` only if they contain such references

The path rewrite should be conservative and mechanical:

- old run path
  `output/feedforward_network/<run_name>/`
- new migrated path
  `output/training_runs/feedforward/legacy__<run_name>/`

### 5. Remove The Legacy Root Only After Migration Completes

The old directory:

- `output/feedforward_network/`

should be removed only after:

- all historical run folders have been migrated;
- registry rebuild is complete;
- repository-authored document references have been rewritten;
- verification confirms no remaining repository references point to the removed root unless intentionally left as historical prose.

## Involved Components

- `output/feedforward_network/`
- `output/training_runs/feedforward/`
- `output/registries/families/feedforward/`
- `output/registries/program/`
- `scripts/training/shared_training_infrastructure.py`
- migration helper logic, likely under `scripts/training/` or a one-off repository migration utility
- `doc/guide/project_usage_guide.md`
- `doc/scripts/training/`
- `doc/running/`
- `doc/technical/`
- `doc/reports/`
- `README.md`
- `doc/README.md`

## Implementation Steps

1. Inventory all legacy run folders under `output/feedforward_network/`.
2. Define the deterministic migrated target folder for each historical run:
   - `output/training_runs/feedforward/legacy__<run_name>/`
3. Move each historical run directory into the new training-run root.
4. Add or normalize metadata files where needed:
   - `run_metadata.yaml`
   - `metrics_summary.yaml` if missing
5. Rebuild the feedforward family leaderboard and best-run registry from all migrated and current feedforward runs.
6. Rebuild the program-level best-solution registry if the migrated historical best is stronger than the currently registered best.
7. Rewrite repository-authored path references from the old legacy root to the new migrated root.
8. Verify that no active repository documentation still relies on `output/feedforward_network/`.
9. Remove the now-empty legacy folder.

## Verification Plan

Verification should include:

- filesystem confirmation that all historical run folders now live under `output/training_runs/feedforward/`;
- validation that the family/program registries still resolve to real existing artifacts;
- `rg` confirmation that repository-authored active documents no longer contain stale `output/feedforward_network/` references unless intentionally preserved in explanatory historical context;
- syntax verification if any Python migration utility is introduced.

## Recommendation

The migration should be executed now in one controlled pass.

It is better to complete the transition fully than to keep both:

- the old flat legacy root;
- the new structured root

in parallel for an extended period.

The deterministic `legacy__<run_name>` convention is the safest way to normalize the old historical artifacts without pretending they were originally timestamped runs.
