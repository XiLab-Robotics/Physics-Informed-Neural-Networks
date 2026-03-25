# `markdown_style_check.py`

## Overview

`scripts/tooling/markdown_style_check.py` checks repository-authored Markdown
files for the warning classes that currently create the most editor noise in
this repository.

The initial rule set covers:

- `MD012/no-multiple-blanks`
- `MD022/blanks-around-headings`
- `MD025/single-title`

The checker is repository-owned and dependency-free. It does not require a
separate external Markdown linter installation.

By default, it scans the canonical Markdown source roots:

- `README.md`
- `AGENTS.md`
- `config/`
- `models/`
- `doc/`
- `site/`

It excludes generated or non-canonical paths such as:

- `site/_build/`
- `.temp/`
- `.tools/`
- `isolated/`
- `output/`

## Usage

### Run The Default Repository Scan

```powershell
python -B scripts/tooling/markdown_style_check.py --fail-on-warning
```

This prints warnings in a terminal-friendly format:

```text
README.md:56 MD022/blanks-around-headings Heading should be followed by one blank line.
```

The `--fail-on-warning` flag makes the command return a non-zero exit code when
warnings are found.

### Scan Specific Paths Only

```powershell
python -B scripts/tooling/markdown_style_check.py README.md doc site
```

This is useful when you only want to re-check the files touched by the current
task.

## Current Behavior

- fenced code blocks are ignored when detecting heading-related rules;
- the checker only targets `.md` and `.markdown` source files;
- `MD025` reports each extra H1 after the first one in the same document;
- the checker is intended for repository-authored Markdown sources, not for
  generated HTML outputs.
