# GitHub Quality Check MD012 And Node24 Action Alignment

## Overview

This technical document defines the repository fix required after the latest
GitHub `Repository Quality Checks` failure on commit `01f1c9c`.

The failure has two distinct parts:

1. one real Markdownlint error:
   `MD012/no-multiple-blanks` in
   `doc/reports/analysis/validation_checks/2026-04-13-15-27-41_paper_reimplementation_rcim_harmonic_wise_track1_hgbm_h0181_heavy_reference_campaign_run_harmonic_wise_comparison_report.md`;
2. one GitHub Actions platform warning stating that several marketplace
   actions still target `Node.js 20` and are being forced to run on
   `Node.js 24`.

The Markdown issue is the direct job failure.

The Node warning does not currently fail the job, but it should be cleaned up
so the workflow stays aligned with GitHub's Node 24 migration path and does
not keep emitting avoidable warnings on future runs.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The fix should stay narrow and inspectable.

For the Markdown failure:

- open the reported harmonic-wise comparison report;
- remove the accidental doubled blank-line sequence that triggers `MD012`;
- rerun the repository Markdown checks on the touched Markdown scope.

For the GitHub Actions warning:

- update the workflow `.github/workflows/ci.yml`;
- keep the existing job logic unchanged;
- only move the affected marketplace actions to Node 24-compatible major
  versions so the warning source is removed without changing the substantive
  quality-check behavior.

Based on current official upstream action release information, the narrow
workflow upgrade direction is:

- `actions/checkout@v4` -> `actions/checkout@v5`;
- `actions/setup-node@v4` -> `actions/setup-node@v5`;
- `actions/setup-python@v5` -> `actions/setup-python@v6`.

The repository already forces JavaScript actions onto Node 24 through
`FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true`, so this task is not about changing
the chosen runtime policy. It is about aligning the action versions so the
workflow no longer depends on forced compatibility shims for Node 20-targeting
action builds.

## Involved Components

- `.github/workflows/ci.yml`
- `doc/reports/analysis/validation_checks/2026-04-13-15-27-41_paper_reimplementation_rcim_harmonic_wise_track1_hgbm_h0181_heavy_reference_campaign_run_harmonic_wise_comparison_report.md`
- `doc/technical/2026-04/2026-04-13/README.md`
- `doc/README.md`

## Implementation Steps

1. Fix the exact `MD012` blank-line violation in the reported Markdown file.
2. Update `.github/workflows/ci.yml` to use Node 24-compatible marketplace
   action majors for checkout, Node setup, and Python setup.
3. Rerun the scoped Markdown checks for the touched Markdown files.
4. Run a syntax or structural sanity check on the touched workflow file where
   practical from local context.
5. Confirm normal final-newline state on the touched Markdown files before
   closing the task.
