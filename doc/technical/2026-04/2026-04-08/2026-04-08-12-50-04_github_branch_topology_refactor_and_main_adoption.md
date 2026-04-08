# GitHub Branch Topology Refactor And Main Adoption

## Overview

This document defines the repository-owned plan for cleaning up the current
GitHub branch topology:

- promote `standard-ml-codex` into the canonical `main` branch;
- make `main` the GitHub default branch;
- declassify `standard-ml` and `codex-agent-pinns` into explicit legacy/test
  branches that are no longer part of the active delivery path;
- decide how the existing GitHub ruleset, GitHub Pages workflow, and branch
  references must be updated after the rename.

The current remote state is:

- `standard-ml-codex`: active canonical branch and current protected branch;
- `base`: obsolete bootstrap branch and current `origin/HEAD` target;
- `standard-ml`: historical secondary branch;
- `codex-agent-pinns`: historical secondary branch.

GitHub supports both default-branch changes and branch renames. GitHub also
updates branch protection policies when a branch is renamed and redirects web
URLs that include the old branch name. However, local clones do not follow the
rename automatically, raw file URLs are not redirected, and repository-owned
workflow filters that still name `standard-ml-codex` must be updated
explicitly. These points are confirmed by the current GitHub Docs for changing
the default branch, renaming a branch, and managing rulesets.

GitHub does not expose a native "archive branch" feature in the repository
branch-management workflow. Based on the current official documentation, the
correct repository policy is to treat `standard-ml` and
`codex-agent-pinns` as legacy/stale secondary branches, document that status,
and optionally retain or delete them later based on whether they still provide
historical value.

## Technical Approach

The safest sequence is:

1. Update repository-owned files that hardcode `standard-ml-codex`.
2. Push those changes while `standard-ml-codex` still exists.
3. In GitHub UI, rename `standard-ml-codex` to `main`.
4. Confirm `main` is the default branch.
5. Repoint rulesets, bypass assumptions, and the `github-pages` environment
   branch filter from `standard-ml-codex` to `main`.
6. Reclassify `standard-ml` and `codex-agent-pinns` as legacy/test branches in
   repository documentation and branch-management guidance.
7. Reclassify `base` as a legacy historical branch after `origin/HEAD` moves to
   `main`, without keeping it in the active delivery path.

Recommended branch policy after the refactor:

- `main`: only active canonical branch;
- `base`: legacy historical branch, retained for provenance only and not for
  new work;
- `standard-ml`: legacy historical branch, not for new work;
- `codex-agent-pinns`: legacy experimental branch, not for new work;
- no non-`main` branch should remain part of the active repository delivery
  path unless explicitly reactivated later.

Recommended GitHub-side policy after the refactor:

- keep the current ruleset, but retarget it to `main`;
- keep the current admin-role bypass temporarily during active development;
- later, narrow the bypass from `Repository admin Role` to the maintainer user
  or remove it entirely when PR-only flow becomes mandatory;
- keep `Repository Quality Checks` as the required status check on `main`.

## Involved Components

- `.github/workflows/ci.yml`
- `.github/workflows/publish-sphinx-pages.yml`
- `site/getting_started/local_build.rst`
- `site/getting_started/github_pages.rst`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/campaigns/run_remote_training_validation_campaign.md`
- `doc/scripts/campaigns/run_targeted_remote_followup_campaign.md`
- `doc/README.md`
- GitHub repository settings:
  - default branch;
  - ruleset target branch;
  - `github-pages` environment deployment branch filter;
  - branch list and stale/legacy branch handling.

## Implementation Steps

1. Update repository-owned workflow filters and documentation references that
   still hardcode `standard-ml-codex`.
2. Add a branch-management note in the repository documentation that declares
   `main` as the canonical branch after migration and marks `standard-ml` plus
   `codex-agent-pinns` as legacy/test branches.
3. Verify the modified repository-owned Markdown scope is warning-free.
4. After approval, instruct the maintainer to execute the GitHub UI migration:
   rename `standard-ml-codex` to `main`, confirm `main` as default branch, and
   move the `github-pages` environment rule to `main`.
5. After the rename is live, revalidate:
   - `Repository Quality Checks`;
   - `Publish Sphinx Pages`;
   - ruleset target branch;
   - local clone update commands.
6. Keep `base`, `standard-ml`, and `codex-agent-pinns` visible only as
   documented legacy branches unless a later explicit cleanup task decides
   otherwise.
