# Post-Rename Branch Reference Realignment

## Overview

This document defines the narrow follow-up cleanup required after the GitHub
branch-topology migration was executed successfully in the repository hosting
settings.

The migration is already live:

- `standard-ml-codex` has been renamed to `main`;
- `main` is now the default branch;
- the old secondary branches were renamed to:
  - `test-manual-ml`
  - `test-codex-agent-pinns`
- `base` remains available as a legacy historical branch.

The repository itself still contains a few stale references to the pre-rename
branch names. These are now inconsistent with the actual remote topology and
should be realigned.

## Technical Approach

The cleanup should stay intentionally narrow and only touch current
repository-owned behavior or current-facing documentation. Historical technical
documents should remain unchanged unless they are part of the current active
operational surface.

The required scope is:

- remove the stale `standard-ml-codex` fallback from GitHub workflow branch
  filters now that `main` exists and is active;
- update the current documentation pages that still describe the old legacy
  branch names `standard-ml` and `codex-agent-pinns`;
- keep historical notes intact when they are documenting past repository state
  rather than current instructions.

## Involved Components

- `.github/workflows/ci.yml`
- `.github/workflows/publish-sphinx-pages.yml`
- `site/getting_started/local_build.rst`
- `site/getting_started/github_pages.rst`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Remove `standard-ml-codex` from the workflow trigger filters and leave
   `main` as the only active canonical branch trigger.
2. Update the current branch-policy documentation to use the real legacy branch
   names:
   - `base`
   - `test-manual-ml`
   - `test-codex-agent-pinns`
3. Keep older historical technical documents unchanged unless they are part of
   the live operational path.
4. Run the touched Markdown warning checks and rebuild the Sphinx portal.
