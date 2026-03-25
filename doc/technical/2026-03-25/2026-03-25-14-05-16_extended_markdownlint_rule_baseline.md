# Overview

This document defines the next cleanup step for repository-authored Markdown
linting after the initial structural warning pass that covered only
`MD012/no-multiple-blanks`, `MD022/blanks-around-headings`, and
`MD025/single-title`.

The current broader scan on the canonical repository Markdown scope excluding
`reference/` shows that additional warning classes exist beyond those three
rules. The largest remaining warning family is `MD013/line-length`, while
`MD041/first-line-heading/first-line-h1` also appears in files that start with
MyST include directives rather than a literal H1 heading.

The user requested a robust solution that checks for other warning classes as
well, but without touching `reference/` and without introducing noisy or
misleading failures for repository structures that are intentionally valid.

## Technical Approach

## 1. Establish The Canonical Markdown Scope Explicitly

The lint workflow should treat the following repository-authored paths as the
default canonical scope:

- `README.md`
- `AGENTS.md`
- `config/**/*.md`
- `models/**/*.md`
- `doc/**/*.md`
- `docs/**/*.md`

The lint workflow should continue to exclude:

- `reference/**`
- `docs/_build/**`
- generated or transient folders such as `.temp/`, `.tools/`, `isolated/`, and
  `output/`

This keeps the check focused on maintained project Markdown rather than vendor,
archive, or generated content.

## 2. Split Structural Rules From Policy Rules

Not all Markdownlint warnings have the same value for this repository.

The workflow should distinguish:

- structural rules that usually indicate real formatting defects and should be
  enforced by default;
- policy rules that may be useful, but require repository-specific tuning
  before they become mandatory.

The structural baseline should continue to include:

- `MD012/no-multiple-blanks`
- `MD022/blanks-around-headings`
- `MD025/single-title`

The next reviewed rule families should include:

- `MD013/line-length`
- `MD041/first-line-heading/first-line-h1`
- any additional recurring rules surfaced by the canonical-scope scan once the
  lint configuration is made reproducible inside the repository

## 3. Handle MD013 As A Configured Repository Policy

`MD013/line-length` currently dominates the warning volume. Fixing it blindly
would produce a very large formatting churn across technical documents, guides,
and repository rules.

Therefore, `MD013` should not be treated as a binary default failure until the
repository defines a practical policy for:

- maximum line length;
- whether long tables, code blocks, URLs, or long technical paths are exempt;
- whether long list items and prose paragraphs should be wrapped automatically;
- which document families should be cleaned now versus later

The implementation should make this policy explicit in the lint configuration
instead of silently inheriting the external tool default.

## 4. Handle MD041 With Awareness Of Include-Wrapper Files

Some files under `docs/` act as include wrappers and begin with a MyST
directive such as:

```md
```{include} ../../doc/guide/project_usage_guide.md
```

Those files are structurally valid for the documentation pipeline even though
they do not begin with a literal H1 line.

The lint workflow should therefore either:

- exempt known include-wrapper patterns from `MD041`; or
- disable `MD041` for the wrapper-oriented subtree while keeping it enabled for
  normal authored Markdown files

The key point is to avoid false-positive failures for intentionally thin bridge
documents.

## 5. Use A Repository-Owned External-Lint Entry Point

The current custom checker is useful for lightweight structural checks, but it
does not expose the wider Markdownlint rule space.

The repository should gain a tracked external-lint entry point that:

- runs Markdownlint on the canonical scope;
- uses a tracked repository configuration file;
- makes exclusions and rule policy explicit;
- can be invoked from the terminal with a stable repository command

This can be implemented with a lightweight wrapper script under
`scripts/tooling/` that calls the external linter in a reproducible way,
provided the dependency and usage documentation are updated correctly if needed.

## 6. Preserve The Existing Lightweight Checker

The existing repository-owned structural checker should remain useful as a fast,
dependency-light validation path.

The extended workflow should decide whether to:

- keep both tools side by side, with the current script covering the guaranteed
  structural baseline and the external runner covering the broader configured
  Markdownlint policy; or
- expand the current script only if that remains maintainable without cloning a
  large subset of Markdownlint behavior

The preferred direction is likely a dual-layer workflow:

- fast internal structural checker;
- broader external Markdownlint runner with repository configuration

## 7. Fix The Warnings That Fall Inside The Approved Extended Baseline

Once the configuration is explicit, the implementation should:

- re-run the canonical-scope lint check;
- identify the remaining warning families that are still enabled;
- fix the warnings that belong to the approved baseline;
- verify that the canonical non-`reference/` scope passes cleanly

## Involved Components

- `README.md`
- `doc/technical/2026-03-25/2026-03-25-13-10-20_markdown_warning_cleanup_and_lint_workflow.md`
- new technical document in `doc/technical/2026-03-25/`
- `scripts/tooling/markdown_style_check.py`
- future repository lint configuration file in the repository root
- future external Markdown lint runner under `scripts/tooling/`
- `doc/scripts/tooling/markdown_style_check.md`
- future script documentation for the external lint runner
- `doc/guide/project_usage_guide.md`
- `requirements.txt` if the final implementation introduces a tracked
  dependency for the lint workflow

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Reproduce the broader canonical-scope Markdownlint results excluding
   `reference/`.
3. Decide the repository policy for `MD013` and the handling strategy for
   `MD041` on include-wrapper files.
4. Add a tracked repository lint configuration that makes the enabled rules and
   exclusions explicit.
5. Implement a repository-owned terminal entry point for the broader Markdown
   lint workflow.
6. Update the existing Markdown tooling documentation and usage guide.
7. Fix the warnings that remain inside the approved canonical baseline.
8. Re-run both the lightweight checker and the broader configured lint command
   to verify the non-`reference/` repository Markdown scope is clean.
