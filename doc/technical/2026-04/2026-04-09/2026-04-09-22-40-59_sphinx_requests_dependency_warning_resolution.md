# Sphinx Requests Dependency Warning Resolution

## Overview

This document covers the follow-up on the previously observed
`RequestsDependencyWarning` emitted during one Sphinx build.

The problem is not currently reproducible in the active interpreter because the
local Python used for this check does not have `sphinx` installed at all, so
the issue should be treated as an environment-consistency problem in the
documentation build path rather than as a confirmed runtime bug inside the
repository Sphinx source tree.

The current repository state strongly suggests that the warning is caused by an
underspecified documentation environment:

- `site/requirements-docs.txt` declares Sphinx and core documentation/runtime
  packages, but it does not explicitly declare the `requests` stack;
- the repository contains tooling that imports `requests`, but the docs-only
  dependency file leaves the exact `requests` + `urllib3` +
  `charset-normalizer` resolution to transitive side effects;
- `RequestsDependencyWarning` is typically emitted when `requests` detects an
  unsupported dependency combination rather than when Sphinx itself is broken.

No subagent is planned for this task. The work is a local documentation and
dependency-alignment fix, and any future delegated environment diagnosis would
still require explicit user approval at runtime.

## Technical Approach

The safest fix should align the documentation build environment explicitly
instead of suppressing the warning.

### 1. Reproduce Or Bound The Problem

Inspect the current documentation dependency declarations and the GitHub
workflow installation path. If the active local interpreter cannot reproduce
the Sphinx build because `sphinx` is absent, treat that as evidence that the
warning belongs to a different docs environment rather than silently ignoring
it.

### 2. Make The Docs Environment Explicit

Update `site/requirements-docs.txt` so the documentation environment explicitly
installs the `requests` stack with compatible versions instead of relying on
whatever indirect resolution happens to be present at build time.

The likely target is to add explicit entries for:

- `requests`
- `urllib3`
- `charset-normalizer`

with bounds compatible with the main repository requirements and with current
`requests` expectations.

### 3. Keep The Canonical Sphinx Path Clean

If the fix touches user-facing documentation build instructions or canonical
dependency surfaces, update the relevant Sphinx and repository documentation so
the declared local-build path matches the actual warning-free environment.

### 4. Validate The Result

After the dependency alignment, run the canonical Sphinx build:

`python -m sphinx -W -b html site site/_build/html`

and confirm that the previous `RequestsDependencyWarning` no longer appears in
the validated build path.

## Involved Components

- `doc/README.md`
- `doc/technical/2026-04/2026-04-09/2026-04-09-22-40-59_sphinx_requests_dependency_warning_resolution.md`
- `site/requirements-docs.txt`
- `.github/workflows/ci.yml`
- `.github/workflows/publish-sphinx-pages.yml`
- `site/getting_started/local_build.rst`
- `site/getting_started/github_pages.rst`

## Implementation Steps

1. Confirm the current documentation dependency declarations and workflow
   installation path for the Sphinx build.
2. Update the docs dependency file so the `requests` dependency family is
   declared explicitly and consistently.
3. Adjust any affected documentation or workflow references if the canonical
   docs build path changes.
4. Run the canonical Sphinx build in the validated docs environment.
5. Run Markdown warning checks on the touched Markdown scope before closing the
   task.
6. Report the result and wait for explicit approval before creating any Git
   commit.
