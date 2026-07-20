# Selected Report Markdownlint Spacing Fix

## Overview

The GitHub quality check failed during the `Run Markdownlint In Chunks` step
because ten selected-model `TE Curve Verification Pipeline` reports contain
condition-list bullets that are not surrounded by blank lines. The reported
rule is `MD032/blanks-around-lists`.

## Technical Approach

Apply a minimal Markdown-only repair by inserting the missing blank line before
the affected condition lists. Preserve the report wording, metrics, links, and
artifact references exactly.

No subagent is planned. If a subagent becomes useful later, the delegated scope
and approval requirement must be recorded before launch.

## Involved Components

- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-06]/`
- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-19]/`
- `scripts/tooling/markdown/run_markdownlint.py`
- `scripts/tooling/markdown/markdown_style_check.py`

## Implementation Steps

1. Inspect the affected report lines and confirm the MD032 context.
2. Insert blank lines before the affected lists only.
3. Run Markdownlint on the touched selected-model reports.
4. Run the repository Markdown style checker on the touched Markdown scope.
5. Report the result and stop before any commit.
