# Sphinx Pages Build Repair

## Overview

The GitHub Pages Sphinx build currently fails because the warning-as-error
Sphinx invocation imports
`scripts.reports.analysis.build_track2_dataset_difference_report`, which imports
`matplotlib`. The Pages workflow installs `site/requirements-docs.txt`, and that
documentation dependency set does not currently include `matplotlib`, even
though the root project `requirements.txt` does.

The Pages workflow also emits a GitHub Actions runtime warning because it still
uses `actions/checkout@v4` and `actions/setup-python@v5` while opting into the
Node.js 24 transition.

## Technical Approach

Keep the fix narrow and documentation-build specific:

- add `matplotlib` to `site/requirements-docs.txt` so autodoc can import the
  report module in the same dependency surface used by GitHub Pages;
- update `.github/workflows/publish-sphinx-pages.yml` to match the already
  updated CI workflow action versions for checkout and Python setup;
- avoid changing report-generation code or full training dependencies, because
  the failing import is a documentation build dependency issue.

No subagent is planned for this task.

## Involved Components

- `.github/workflows/publish-sphinx-pages.yml`
- `site/requirements-docs.txt`
- `site/getting_started/github_pages.rst`, only if the dependency description
  needs alignment after the dependency change
- `doc/README.md`
- GitHub Pages Sphinx build command:
  `python -m sphinx -W -b html site site/_build/html`

## Implementation Steps

1. Update the Pages workflow from `actions/checkout@v4` to
   `actions/checkout@v5`.
2. Update the Pages workflow from `actions/setup-python@v5` to
   `actions/setup-python@v6`.
3. Add the missing documentation-build dependency to
   `site/requirements-docs.txt`.
4. Run the Sphinx warning-as-error build locally from an environment with Sphinx
   available.
5. Run Markdown QA on the touched Markdown files.
6. Report completion and wait for explicit approval before any commit.
