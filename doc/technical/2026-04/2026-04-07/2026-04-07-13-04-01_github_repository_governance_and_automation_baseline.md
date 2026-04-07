# GitHub Repository Governance And Automation Baseline

## Overview

This task defines a practical GitHub governance and automation baseline for the
now-public repository. The goal is to add only the controls and automation that
materially improve repository safety, review discipline, documentation hygiene,
and release readiness without over-engineering a research-heavy workflow.

The current GitHub surface is still minimal: the repository already has a live
GitHub Pages publication workflow, but it does not yet have a dedicated CI
workflow, pull-request templates, issue templates, labels, or repository-owned
governance files such as `CODEOWNERS` or `dependabot.yml`.

## Technical Approach

The proposed baseline will focus on six concrete layers:

1. branch governance:
   define a recommended `Ruleset` for `standard-ml-codex` with pull-request
   discipline, no force-push, no branch deletion, and resolved-review-thread
   requirements;
2. repository CI:
   add a separate lightweight `ci.yml` so branch protection can require a real
   repository-quality signal instead of overloading the Pages workflow;
3. review ergonomics:
   add a pull-request template plus issue templates aligned with the
   repository's existing technical-document and approval discipline;
4. ownership hints:
   add a small `CODEOWNERS` baseline so future PR review routing can become
   explicit without being heavy-handed;
5. maintenance automation:
   add a minimal `dependabot.yml` focused on GitHub Actions and optionally a
   cautious Python update cadence;
6. project hygiene:
   define a recommended starter label set and operational GitHub settings that
   should be configured directly in the GitHub UI.

The implementation should remain lightweight and repository-compatible. The
goal is not to impose an enterprise-style process on every change, but to make
the public repository harder to break and easier to review.

## Involved Components

- `.github/workflows/ci.yml` (new)
- `.github/PULL_REQUEST_TEMPLATE.md` (new)
- `.github/ISSUE_TEMPLATE/` (new)
- `.github/CODEOWNERS` (new)
- `.github/dependabot.yml` (new)
- `README.md` (only if the public-facing contribution or quality signals need
  a short entry-point note)
- `doc/guide/project_usage_guide.md` (only if user-facing workflow changes are
  introduced)
- `doc/README.md`

## Implementation Steps

1. Create the repository governance baseline package with:
   - a lightweight CI workflow;
   - a PR template;
   - issue templates;
   - `CODEOWNERS`;
   - `dependabot.yml`.
2. Keep the CI scope intentionally fast and high-signal:
   - Markdown checks;
   - Sphinx warning-as-error build;
   - Python syntax validation on the repository-owned script surface or on the
     touched scope, depending on the final workflow design.
3. Document the recommended GitHub-side settings that cannot be fully stored in
   the repository itself:
   - branch ruleset for `standard-ml-codex`;
   - required status checks;
   - merge policy such as squash-only or linear-history preference;
   - label set.
4. Update the public-facing or usage-facing documentation only where the new
   governance surface becomes part of the expected repository workflow.
5. Run the touched-Markdown warning checks and relevant repository verification
   before closing the task.
