# GitHub Pages Environment Protection Fix And Node24 Alignment

## Overview

The Sphinx Pages workflow now builds successfully after the repository became
public, but deployment is still blocked by GitHub-side environment protection
rules on `github-pages`. The current deploy error is:

- `Branch "standard-ml-codex" is not allowed to deploy to github-pages due to environment protection rules.`

The run also emits a separate warning about GitHub Actions JavaScript actions
still running on Node.js 20, with GitHub indicating that Node.js 24 should be
adopted.

## Technical Approach

This task will address the issue in two coordinated parts:

1. repository-side workflow alignment:
   update the Pages workflow to opt into Node.js 24 for JavaScript-based
   actions so the workflow is aligned with GitHub's current deprecation path;
2. GitHub-side environment alignment:
   document the exact required repository setting on the `github-pages`
   environment so the `standard-ml-codex` branch is allowed to deploy.

The deploy blocker is the environment rule, not the workflow logic itself, so
the final closure requires both the repository patch and the corresponding
GitHub setting update.

## Involved Components

- `.github/workflows/publish-sphinx-pages.yml`
- `site/getting_started/github_pages.rst`
- `site/getting_started/local_build.rst`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Update the Pages workflow to opt into Node.js 24 action execution.
2. Add a short operational note in the repository documentation explaining that
   the `github-pages` environment must allow the `standard-ml-codex` branch to
   deploy.
3. Re-run the local Sphinx warning-as-error build to confirm the documentation
   surface remains consistent.
4. Provide the exact GitHub UI action still required after the repository
   changes are committed:
   allow the `standard-ml-codex` branch in the `github-pages` environment
   protection rules, or remove the overly restrictive deployment-branch rule.
