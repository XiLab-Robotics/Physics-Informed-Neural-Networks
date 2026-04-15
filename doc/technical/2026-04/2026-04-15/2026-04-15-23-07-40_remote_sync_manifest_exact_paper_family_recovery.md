# Remote Sync Manifest Exact-Paper Family Recovery

## Overview

The remote `Track 1` `SVR` campaign now reaches and completes the actual
queue-driven remote execution phase. The latest blocker is no longer in:

- path resolution;
- Windows path length handling;
- remote script transport;
- or remote campaign launch.

The current failure occurs later, during the remote sync-manifest generation
step:

- `scripts/training/build_remote_training_sync_manifest.py`
- `resolve_run_output_directory_relative_path(run_dictionary)`

The failing assertion is:

- `Could not resolve model family for one campaign run while building the remote sync manifest`

The relevant run output directory belongs to the exact-paper validation surface:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/...`

That path does not follow the standard:

- `output/training_runs/<model_family>/<run_instance_id>`

family layout that the current sync-manifest helper assumes when trying to
recover `model_family`.

## Technical Approach

The sync-manifest helper currently infers `model_family` only from
`output/training_runs/<model_family>/...` style paths. That logic is too narrow
for exact-paper campaign runs whose outputs are stored under:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/...`

The fix should extend the helper so it can recover the appropriate family or
sync target for exact-paper validation artifacts without forcing them into the
standard `training_runs` assumption.

The expected direction is:

1. keep the current fast path for standard `training_runs/<family>/...`
   outputs;
2. add an exact-paper path branch that accepts
   `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/...`
   as a valid canonical output surface;
3. derive the registry family or sync grouping explicitly for that branch
   instead of asserting that the path must look like `training_runs`;
4. keep the returned sync list repository-relative and manifest-driven.

This should be implemented in the sync-manifest helper itself, not hidden in
the launcher, because the helper owns the contract that converts one remote
campaign manifest into the canonical sync-back path set.

## Involved Components

- `scripts/training/build_remote_training_sync_manifest.py`
  Canonical helper that fails while trying to recover `model_family` from an
  exact-paper validation output path.
- `scripts/training/shared_training_infrastructure.py`
  May be needed for family naming or registry target alignment if the helper
  delegates exact-paper family recovery to an existing utility.
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/...`
  Exact-paper output surface that must be accepted as a first-class sync-back
  artifact source.
- `output/registries/families/`
  Family registry surface that the helper includes in the sync manifest and may
  still need to update coherently for exact-paper runs.

## Implementation Steps

1. Extend `resolve_run_output_directory_relative_path(...)` so it accepts and
   preserves exact-paper validation output directories as canonical remote sync
   targets.
2. Add exact-paper family recovery logic that does not assume a
   `training_runs/<family>/...` layout.
3. Keep the existing standard training-run behavior unchanged for non
   exact-paper campaigns.
4. Run a focused local check of the sync-manifest helper against the failing
   exact-paper campaign manifest shape.
5. Retest the current `Track 1` `SVR` remote launcher on the LAN node.
