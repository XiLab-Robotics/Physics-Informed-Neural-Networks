# GitHub Quality Check Markdown MD012 Fix

## Overview

This technical document records the planned repository change for the failing
GitHub quality check reported on April 13, 2026. The current failure is caused
by `MD012/no-multiple-blanks` warnings in repository-owned Markdown comparison
reports under `doc/reports/analysis/validation_checks/`.

The immediate objective is to remove the repeated blank-line pattern that makes
the GitHub Actions Markdownlint chunk fail, then re-run the repository-owned
Markdown checks on the touched Markdown scope to confirm a warning-free result.

No Codex subagent is planned for this task. The scope is narrow, local to the
repository, and does not justify delegated execution. If that changes later,
runtime launch would still require explicit user approval.

## Technical Approach

The first implementation step will be to inspect the exact failing report files
named in the GitHub Actions log and verify whether the `MD012` violations are
caused by doubled blank lines near the file tail or by a shared report-writing
path.

If the issue is limited to the generated Markdown artifacts already tracked in
the repository, the fix should remain minimal:

- remove the extra blank line from each failing report;
- preserve document content and line ordering;
- avoid modifications to the currently active campaign plan, queue, launcher,
  or other protected campaign files.

If inspection shows that the defect also comes from the report-generation code,
the implementation scope may be extended to the corresponding Markdown writer so
future comparison reports do not reintroduce the same warning. That decision
will be based on local evidence from the current files and generator path.

After the fix, the touched Markdown files will be checked with the repository
Markdown QA tooling and their final newline state will be verified to avoid a
doubled trailing blank line.

## Involved Components

- `doc/reports/analysis/validation_checks/*.md`
  Repository-owned harmonic-wise comparison reports implicated by the failing
  GitHub Actions Markdownlint run.
- `scripts/tooling/markdown/run_markdownlint.py`
  Canonical repository wrapper for Markdownlint execution on a targeted scope.
- `scripts/tooling/markdown/markdown_style_check.py`
  Repository structural Markdown checker that also validates `MD012`.
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`
  Candidate generator path if the repeated blank-line defect is proven to come
  from the report-writing implementation rather than only from existing files.
- `doc/technical/2026-04/2026-04-13/2026-04-13-15-22-14_github_quality_check_markdown_md012_fix.md`
  Canonical technical record for this fix.
- `doc/README.md`
  Canonical documentation index entry for the new technical document.

## Implementation Steps

1. Inspect the specific Markdown reports called out by the failed GitHub
   quality-check log and confirm the exact `MD012` pattern.
2. Apply the smallest safe fix to the failing report files and only extend the
   change into the report generator if the defect is clearly systematic.
3. Run the repository-owned Markdown QA commands on the touched Markdown scope.
4. Verify that the touched Markdown files end with a normal single final
   newline, not a doubled trailing blank line.
5. Report the completed fix and validation status, then wait for explicit user
   approval before any Git commit.
