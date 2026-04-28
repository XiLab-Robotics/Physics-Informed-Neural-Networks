# Rewrite Recent Commits And Separate Paper Reimplementation From Campaign Artifacts

## Overview

This technical document defines the local-history repair needed after the recent
commit packaging error that mixed two different scopes:

- completed `Track 1` forward last-non-green-cells campaign artifacts and
  campaign-owned documentation;
- unrelated `paper_reimplementation` reorganization and documentation changes.

The goal is to rewrite the recent local commits so that the campaign closeout
and campaign artifact package remain separated from the RCIM
`paper_reimplementation` reorganization surface.

## Technical Approach

The rewrite will be performed locally by reworking the recent commit range near:

- `d2a88548c` `Add remaining Track 1 forward last non-green campaign docs`
- `2523e8f4d` `Close out Track 1 forward last non-green cells campaign`
- nearby `paper_reimplementation` commits already present above them in the
  local history

The safe strategy is:

1. inspect the exact file ownership of the recent commits;
2. reset or replay the local tip to a clean pre-rewrite point;
3. rebuild the intended history as separate commits with explicit path-owned
   staging only;
4. verify the resulting commit boundaries before stopping.

Because the worktree is dirty and earlier staging leakage already happened, the
rewrite should use an isolated Git-index workflow or equivalent explicit
pathspec-based staging so that campaign files and `paper_reimplementation`
files cannot be mixed accidentally again.

## Involved Components

- `git` local history for the recent commit range
- `doc/technical/2026-04/2026-04-28/2026-04-28-17-09-01_rewrite_recent_commits_and_separate_paper_reimplementation_from_campaign_artifacts.md`
- `doc/technical/2026-04/2026-04-28/README.md`
- `doc/README.md`
- recent commit scopes around:
  - `d2a88548c`
  - `2523e8f4d`
  - `98c34adad`
  - `0818f968e`
  - `65de69e49`

## Implementation Steps

1. Audit the exact recent commit boundaries and classify each changed file as:
   campaign closeout core, campaign artifact/documentation, or
   `paper_reimplementation`.
2. Choose the minimal local rewrite base that preserves the intended closeout
   result while removing the accidental scope mixing.
3. Rebuild the local commits as at least two clean packages:
   one for campaign-owned artifacts and one for `paper_reimplementation`.
4. Verify each rebuilt commit with explicit file lists and diff stats.
5. Report the rewritten commit hashes and the final separation outcome before
   any further push-related action.
