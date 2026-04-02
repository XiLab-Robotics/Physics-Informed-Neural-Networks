# Overview

This document defines the cleanup scope for the Markdownlint warning
`MD034/no-bare-urls`, which reports bare URLs written directly in Markdown
prose or list items instead of being wrapped as autolinks or normal Markdown
links.

The immediate reproduced failure appears in
`doc/reference_codes/testrig_twincat_ml_reference.md`, where a TwinCAT
reference-link list currently uses raw Beckhoff documentation URLs on their own
lines. A broader repository grep also shows additional bare-URL usage in
canonical Markdown files such as `README.md`, `doc/guide/project_usage_guide.md`,
older technical notes, and analysis reports.

The requested outcome is a repository-aligned fix strategy that removes the
warning without changing the meaning of the referenced sources or introducing
needless wording churn.

## Technical Approach

## 1. Reproduce The Active MD034 Failures First

The first step should continue to use the repository-owned lint entry point:

- `python -B scripts/tooling/run_markdownlint.py`

At the time of this document, that command reports active `MD034` failures in:

- `doc/reference_codes/testrig_twincat_ml_reference.md`

This establishes the currently failing baseline before editing any Markdown
source.

## 2. Normalize Bare URLs Using Stable Markdown Forms

The cleanup should replace raw URLs with one of these forms:

- autolinks such as `<https://example.com>`;
- descriptive Markdown links such as `[Beckhoff TF38x0 Documentation](https://...)`;
- fenced code formatting only when the URL is intentionally shown as a literal
  command-line value rather than as a document reference.

The preferred choice depends on context:

- prose references and source lists should use descriptive links when a short
  label improves readability;
- pure bibliography-style lists may use autolinks when the URL itself is the
  meaningful identifier;
- shell commands that require a URL argument should stay as executable command
  text, but the command examples should still avoid standalone bare URLs when
  Markdownlint treats them as plain text.

## 3. Preserve Documentation Intent Per File Type

Not every bare URL serves the same purpose.

The cleanup should preserve intent by treating file families differently:

- `README.md` and `doc/guide/project_usage_guide.md`
  Inline package-index URLs inside shell commands should remain runnable.
  If Markdownlint flags those lines, they should be handled in the smallest
  possible way that keeps copy-paste behavior obvious.
- `doc/reference_codes/*.md`
  External documentation references should become descriptive links or
  autolinks instead of raw lines.
- older technical or analysis documents
  Existing source citations should be normalized without rewriting the
  surrounding analysis unless readability clearly improves.

## 4. Keep The Fix Scope Narrow

This cleanup is about `MD034`, not a general rewrite of citation style.

The implementation should avoid:

- rephrasing unrelated text blocks;
- reformatting unaffected lists and headings;
- changing reference semantics or dropping source URLs;
- expanding the scope into unrelated Markdownlint rules unless the same edited
  lines require a tiny companion adjustment.

## 5. Verify With The Repository Lint Workflow

After the edits, the repository should re-run:

- `python -B scripts/tooling/run_markdownlint.py`

If the user wants only the active failing file fixed, verification can be done
against that path first and then against the default configured scope.

## Involved Components

- `README.md`
- `doc/guide/project_usage_guide.md`
- `doc/reference_codes/testrig_twincat_ml_reference.md`
- selected historical technical and analysis documents if they are included in
  the approved cleanup scope
- `scripts/tooling/run_markdownlint.py`
- `.markdownlint-cli2.jsonc`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Reproduce the current `MD034` failures with the repository Markdownlint
   runner.
3. Convert the active bare URLs in the approved target files to autolinks or
   descriptive Markdown links, depending on context.
4. Re-run Markdownlint on the edited files and then on the default repository
   scope.
5. Report the cleaned files and wait for approval before any commit step.
