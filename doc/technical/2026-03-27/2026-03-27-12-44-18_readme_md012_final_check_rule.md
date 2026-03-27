# README MD012 Final Check Rule

## Overview

The user reported recurring Markdownlint warnings in `README.md` of the form:

- `MD012/no-multiple-blanks: Multiple consecutive blank lines [Expected: 1; Actual: 2]`

The repository should treat this as a repeatable README-quality check rather
than as a one-off cleanup request.

At the time of this document, the current `README.md` content does not show any
consecutive blank-line pairs, so no substantive README-content repair is needed
right now.

## Technical Approach

The repository workflow should keep a lightweight final-pass rule for
`README.md`:

- before closing documentation-oriented work, check the README for consecutive
  blank lines;
- remove any duplicated empty lines that would trigger `MD012`;
- keep the fix minimal and avoid unrelated README rewrites when the only issue
  is Markdown spacing.

This is a documentation-discipline rule, not a feature implementation change.

## Involved Components

- `README.md`
  Main project document that should be checked for repeated empty lines before
  finalizing documentation changes.
- `doc/technical/2026-03-27/2026-03-27-12-44-18_readme_md012_final_check_rule.md`
  This technical note recording the persistent check rule.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Inspect the current `README.md` for `MD012`-style repeated empty lines.
3. If repeated empty lines are present, remove them with a minimal patch.
4. If repeated empty lines are not present, leave README content unchanged.
5. Treat the README `MD012` check as a recurring final-pass step for future
   documentation edits.
