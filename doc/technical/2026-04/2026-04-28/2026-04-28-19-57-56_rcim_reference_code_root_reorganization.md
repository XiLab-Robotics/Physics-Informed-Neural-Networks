# 2026-04-28-19-57-56 Rcim Reference Code Root Reorganization

## Overview

The recovered RCIM reference-code root currently mixes three different
surfaces under:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot`
- `reference/rcim_ml_compensation_recovered_assets/code/backup_legacy`

The user has now recovered the entire original RCIM repository and wants that
full repository to become the canonical content of:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline`

At the same time, the current contents of `latest_snapshot/` and the current
`original_pipeline/` are understood to be later or split fragments of the last
known paper-era code surface, while `backup_legacy/` is understood to be a
much earlier backup.

The immediate goal of this work is therefore not to merge code, but to
reorganize the reference-code root so the three historical strata are named
and placed coherently before the full recovered repository is installed.

## Technical Approach

The reorganization should treat the `reference/.../code/` root as a
history-preserving archive surface with one canonical active root and explicit
backup roots.

The proposed target model is:

1. `original_pipeline/`
   This becomes the canonical location for the newly recovered full original
   RCIM repository.
2. `backup_legacy/`
   This should stop pretending to be a generic backup name and instead become
   an explicitly early backup surface.
3. current `latest_snapshot/` plus current `original_pipeline/`
   These should move into clearly named backup folders that explain they are
   partial or reorganized late-stage recovered fragments rather than the full
   original repository.

The practical implementation should happen in two phases.

Phase 1: stabilize naming and archival layout

- inspect the new recovered repository root supplied by the user;
- rename or move the existing three surfaces into backup names that describe
  their historical role;
- reserve `original_pipeline/` for the full recovered repository.

Phase 2: install the newly recovered full repository

- copy or move the newly recovered full original repository into
  `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline`;
- verify that the expected stage roots and key scripts are present after the
  move;
- update reference-facing documentation so later analysis and script-copy work
  points at the correct canonical reference root.

The naming pass should avoid vague labels once the move is complete. A likely
backup taxonomy is:

- `backup_legacy_early_snapshot/`
  for the content currently under `backup_legacy/`
- `backup_latest_snapshot_fragment/`
  for the content currently under `latest_snapshot/`
- `backup_split_original_pipeline_fragment/`
  for the content currently under the current `original_pipeline/`

These exact names can still be refined after inspecting the full recovered
repository, but the plan should preserve these distinctions:

- early backup
- late split snapshot
- canonical full recovered original repository

This work should also treat the current user interpretation as canonical:

- current `backup_legacy/` = very early backup
- current `latest_snapshot/` + current `original_pipeline/` = misnamed split
  view of a later code generation
- future `original_pipeline/` = full recovered original RCIM repository

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/code/backup_legacy/`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- the newly recovered full RCIM original repository source provided by the user
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- any repo-owned analysis or workflow document that currently references the
  old reference-code root naming
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
  because its explanatory material may need to keep pointing to the renamed
  reference roots accurately after the archival move

## Implementation Steps

1. Inspect the newly recovered full original RCIM repository supplied by the
   user and compare its root structure against the current three recovered
   code folders.
2. Define the final backup names for:
   - the early legacy backup;
   - the current split late snapshot surface;
   - the current split original-pipeline fragment.
3. Move the three existing reference-code folders into their new backup
   locations without deleting history.
4. Install the newly recovered full original repository into
   `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline`.
5. Verify the canonical files and stage directories now live under the new
   `original_pipeline/` root.
6. Update reference-facing documentation and any repo-owned notes that need to
   explain the new archive taxonomy.
7. Run Markdown QA on touched documentation before closing the task.
