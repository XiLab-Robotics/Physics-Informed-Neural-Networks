# `run_markdownlint.py`

## Overview

`scripts/tooling/run_markdownlint.py` runs the repository Markdownlint profile
defined in `.markdownlint-cli2.jsonc`.

This complements the lightweight structural checker
`scripts/tooling/markdown_style_check.py`.

The intended split is:

- `markdown_style_check.py`
  fast repository-owned structural validation for the core warning families;
- `run_markdownlint.py`
  broader Markdownlint validation with explicit repository rule policy and
  scope exclusions

The default Markdownlint scope is the canonical repository-authored Markdown
surface outside `reference/`:

- `README.md`
- `AGENTS.md`
- `config/**/*.md`
- `models/**/*.md`
- `doc/**/*.md`
- `docs/**/*.md`

The tracked configuration excludes non-canonical or generated locations such as:

- `reference/**`
- `docs/_build/**`
- `.temp/**`
- `.tools/**`
- `isolated/**`
- `output/**`

## Current Rule Policy

The current tracked Markdownlint profile:

- disables `MD013/line-length` because the repository has not yet adopted a
  practical wrapped-prose policy for all technical documents;
- disables `MD029/ol-prefix` because the repository sometimes uses meaningful
  ordered-list numbering that should not be forced to restart at `1`;
- keeps `MD024/no-duplicate-heading` enabled, but only for sibling headings, so
  repeated labels in different nested sections do not create false positives;
- disables `MD041/first-line-heading` inside `docs/` wrappers through
  `docs/.markdownlint.jsonc`, because those files intentionally begin with MyST
  include directives

## Usage

### Run The Default Canonical Scan

```powershell
python -B scripts/tooling/run_markdownlint.py
```

This uses the tracked root configuration and scans the default canonical scope.

### Apply Fixable Corrections

```powershell
python -B scripts/tooling/run_markdownlint.py --fix
```

This applies fixable Markdownlint changes in place.

### Lint Specific Files Or Folders

```powershell
python -B scripts/tooling/run_markdownlint.py README.md doc docs
```

When explicit paths are passed, the script disables the config-level default
globs and lints only the provided repository-relative targets.

## Environment Notes

The script invokes `markdownlint-cli2` through `npx.cmd` on Windows.

The current workflow therefore assumes:

- `node`
- `npm`
- `npx`

are available on the machine.

The repository does not currently pin `markdownlint-cli2` as a tracked project
dependency. Instead, the runner uses the current `npx`-resolved tool version at
execution time, while keeping the repository rule profile and scope definition
tracked locally.
