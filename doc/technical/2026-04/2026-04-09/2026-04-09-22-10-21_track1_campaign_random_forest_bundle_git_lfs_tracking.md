# Track1 Campaign RandomForest Bundle Git LFS Tracking

## Overview

This document covers the repository change required to make the current commit
GitHub-safe while preserving the oversized harmonic-wise campaign artifact.

The blocking file is:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/baseline_reference/shared/2026-04-09-20-43-42__te_harmonic_wise_h013_random_forest_diagnostic_campaign_run/harmonic_model_bundle.pkl`

Its size exceeds the standard GitHub object limit for regular Git objects, so
the requested path is:

- track this file through Git LFS;
- keep the rest of the campaign package in the normal repository history;
- then create the approved commit.

## Technical Approach

The change should remain narrow and explicit.

The expected implementation path is:

1. add a Git LFS tracking rule in `.gitattributes` scoped to the oversized
   campaign artifact path or to a sufficiently narrow matching pattern;
2. ensure the targeted file is staged as an LFS pointer rather than as a
   regular Git blob;
3. re-run the commit preflight size check;
4. create the commit only after the worktree is confirmed GitHub-safe.

The preferred scope is as narrow as practical so the repository does not
accidentally move unrelated `.pkl` artifacts into LFS without an explicit
decision.

## Involved Components

- `.gitattributes`
- `doc/README.md`
- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/baseline_reference/shared/2026-04-09-20-43-42__te_harmonic_wise_h013_random_forest_diagnostic_campaign_run/harmonic_model_bundle.pkl`

## Implementation Steps

1. add the narrow Git LFS tracking rule
2. stage the oversized campaign bundle through Git LFS
3. verify that no commit-included file exceeds `100 MB` as a regular Git blob
4. proceed to the approved commit
