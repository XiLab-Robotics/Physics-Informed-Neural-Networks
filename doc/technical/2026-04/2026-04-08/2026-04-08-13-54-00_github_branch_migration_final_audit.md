# GitHub Branch Migration Final Audit

## Overview

This document defines the final audit scope for the recently completed GitHub
branch-topology migration.

The repository has already moved from `standard-ml-codex` to `main`, and the
follow-up cleanup commits have already updated the repository-owned workflows
and current-facing documentation. The goal of this audit is to verify that the
live repository state is now coherent across:

- local Git tracking;
- remote branch topology;
- active GitHub workflow triggers;
- current repository documentation;
- residual active references to the pre-rename branch names.

## Technical Approach

The audit remains read-only. It should inspect the current tracked repository
state and validate the migration from three angles:

1. Git topology:
   - local branch name;
   - remote tracking target;
   - `origin/HEAD`;
   - remaining remote legacy branches.
2. Repository-owned automation:
   - workflow trigger branches in `.github/workflows/`;
   - active Pages/quality documentation references.
3. Current-facing documentation:
   - `site/`;
   - `doc/guide/project_usage_guide.md`;
   - launcher notes or runtime notes that still belong to the active workflow
     surface.

Historical technical notes may still mention the old branch names and should
not be treated as migration defects if they are clearly documenting past
repository state rather than current instructions.

## Involved Components

- `.github/workflows/ci.yml`
- `.github/workflows/publish-sphinx-pages.yml`
- `site/getting_started/local_build.rst`
- `site/getting_started/github_pages.rst`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/campaigns/`
- local Git branch metadata
- remote-tracking branch metadata

## Implementation Steps

1. Inspect local and remote Git branch state.
2. Search the active repository surface for stale pre-rename branch references.
3. Compare the current workflow triggers against the canonical `main` branch
   policy.
4. Record whether the migration is fully aligned or whether any live
   follow-up is still required.
