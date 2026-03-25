# Overview

This document defines a repository-wide cleanup pass for Markdown formatting
warnings and a lightweight workflow to prevent the same warning classes from
reappearing in future generated or edited `.md` files.

The immediate trigger is the presence of editor/linter warnings such as:

- `MD022/blanks-around-headings`
- `MD012/no-multiple-blanks`
- `MD025/single-title`

Observed examples already include:

- `README.md`
  - `## Repository Structure` missing a blank line below the heading;
  - multiple blank lines at the end of the file.
- `doc/technical/2026-03-24/2026-03-24-23-25-32_isolated_handoff_and_provenance_root_retirement.md`
  - multiple top-level headings caused by repeated `#` section headers inside
    the same Markdown document.

The user also requested a broader solution so existing and future Markdown
files can be checked systematically rather than only fixed ad hoc when an
editor highlights a warning.

## Technical Approach

## 1. Fix The Known Warning Classes In Current Source Files

The repository should first fix the confirmed source-level warnings already
identified in canonical Markdown files.

That includes:

- adding missing blank lines around headings where required;
- reducing repeated trailing blank lines to one blank line at most;
- normalizing technical documents so they use one top-level title only and
  lower heading levels such as `##`, `###`, and `####` for internal sections.

This should target source files, not generated HTML or build artifacts.

## 2. Distinguish Canonical Markdown From Generated Outputs

The cleanup and the future lint workflow should focus on repository-authored
Markdown sources such as:

- `README.md`
- `AGENTS.md`
- `doc/**/*.md`
- `docs/**/*.md`
- relevant `config/**/README.md`
- relevant repository-owned `reference/**/README.md` files when they are part of
  the maintained project surfaces

It should avoid treating generated outputs such as:

- `docs/_build/**`

as the primary cleanup target.

## 3. Add A Repository-Owned Markdown Lint Workflow

The repository should gain an explicit Markdown-lint entry point so warning
review is reproducible from the terminal rather than only visible in the editor.

The preferred shape is:

- a tracked Markdown lint configuration file in the repository root;
- a small repository-owned script entry point under `scripts/tooling/`;
- script documentation under `doc/scripts/tooling/`;
- usage-guide documentation for how to run the lint check.

The script should:

- scan the intended Markdown source roots;
- exclude generated folders such as `docs/_build/`;
- print a clean per-file warning list;
- return a non-zero exit code when warnings are found.

## 4. Keep The Rule Set Practical

The goal is not maximum stylistic strictness. The goal is to eliminate noisy,
low-value warnings that make repository-authored Markdown harder to maintain.

Therefore, the first rule set should focus on the warning classes already known
to be useful and noisy:

- heading-blank-line discipline;
- multiple blank lines;
- single top-level heading;
- possibly a small number of additional structural rules if the current scan
  shows they recur heavily and can be fixed safely.

If some warning classes produce more churn than value for the repository's
technical-writing style, they should be configured deliberately rather than
accepted by accident.

## 5. Align Future Generated Markdown With The Same Rules

Once the repository has an explicit lint workflow, future Markdown created by
Codex should be written to pass the same source-level checks by default.

That means future technical documents should follow these baseline rules:

- one H1 only;
- blank line before and after headings;
- no repeated trailing blank lines;
- stable list spacing;
- no accidental heading-level resets inside the same file.

## 6. Environment Strategy

If a Markdown lint dependency is introduced for this workflow, it must be added
to:

- `requirements.txt`

and the relevant setup or usage documentation must be updated before the final
commit, following the existing repository rules.

If an already-available local tool can be used cleanly, the implementation may
prefer that route, but the final workflow should still be documented and
reproducible from the repository itself.

## Involved Components

- `README.md`
- `AGENTS.md`
- `doc/technical/2026-03-24/2026-03-24-23-25-32_isolated_handoff_and_provenance_root_retirement.md`
- potentially other repository-authored Markdown files under `doc/`, `docs/`,
  `config/`, `models/`, and selected maintained `reference/` subtrees
- future Markdown lint configuration file in the repository root
- future tooling entry point under `scripts/tooling/`
- `doc/scripts/tooling/`
- `doc/guide/project_usage_guide.md`
- `requirements.txt` if a new dependency is required

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Inspect the current repository-authored Markdown sources and identify the
   recurring warning classes and affected files.
3. Fix the already confirmed warnings in `README.md` and in the affected
   technical document with multiple H1 headings.
4. Decide the practical Markdown lint rule set and add a repository-owned
   lint configuration.
5. Implement a small repository-owned lint runner under `scripts/tooling/` so
   warnings can be inspected directly from the terminal.
6. Document the lint runner under `doc/scripts/tooling/`.
7. Update `doc/guide/project_usage_guide.md` so the Markdown-check workflow is
   part of the maintained repository usage instructions.
8. If the lint workflow requires a new dependency, add it to `requirements.txt`
   and update the relevant setup references.
9. Run the lint workflow on the intended Markdown source roots, fix the current
   warnings that fall inside the approved scope, and verify that the checked
   files are clean.
