# RCIM Validation Artifact Publication

## Overview

The recent `.gitignore` cleanup exposed previously hidden
`output/validation_checks/` artifacts for the completed paper-faithful RCIM
validation surface. The current workstation sees `2771` untracked pickle
bundles, totaling about `37.805 GiB`, split across the exact model-bank and
harmonic-wise RCIM validation roots.

This plan records the controlled publication path before changing Git
tracking, Git LFS attributes, or artifact staging. No subagent is planned.

## Technical Approach

- Keep the `.gitignore` cleanup intent intact: exposed artifacts must be
  reviewed explicitly instead of hidden by broad ignore rules.
- Treat pickle model bundles above `100 MB` and below `200 MB` as binary
  artifacts that require Git LFS tracking because they exceed the normal
  GitHub file-size limit but remain reasonable repository-owned artifacts.
- Keep pickle model bundles at or below `100 MB` in normal Git commits,
  split into bounded chunks below `1 GiB` each.
- Keep pickle model bundles at or above `200 MB` out of the first publication
  pass until their historical value is audited.
- Prefer path-scoped LFS rules for only the approved `100 MB < file < 200 MB`
  bundle files, so smaller pickle files are not silently converted to LFS.
- Stage artifacts in bounded chunks after LFS attributes are active, checking
  per-file size, aggregate staged size, and LFS pointer status before each
  commit.
- Preserve completed-run paths and legacy `track1` identifiers inside artifact
  directories because they belong to reproducibility-sensitive completed runs.

## Involved Components

- `.gitattributes`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`
- `doc/README.md`
- Git LFS local state and staged pointer verification

## Implementation Steps

1. Confirm the untracked artifact inventory by root, filename, largest files,
   and total payload size.
2. Add Git LFS tracking only for exposed RCIM validation bundles above
   `100 MB` and below `200 MB`.
3. Stage `.gitattributes` first and verify that new pickle artifacts are staged
   as LFS pointers for the approved LFS subset only.
4. Split artifact publication into multiple bounded commits by natural subtree
   or family grouping, keeping staged payloads below practical remote-pack risk.
5. Publish the at-or-below-`100 MB` artifacts as normal Git files in multiple
   commits below `1 GiB` each.
6. Publish the approved `100 MB < file < 200 MB` artifacts through Git LFS.
7. Before each commit, run `git status`, staged-size checks, per-file threshold
   checks, and `git lfs status`.
8. Leave the at-or-above-`200 MB` artifacts untracked for a later historical
   value audit.
