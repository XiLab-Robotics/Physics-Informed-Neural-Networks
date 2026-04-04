# Docs Requirements Location Alignment

## Overview

This task relocates the documentation-only requirements file introduced for the
GitHub Pages workflow so it no longer lives in the repository root. The current
root-level placement is inconsistent with the repository structure because this
file is a workflow-specific support asset rather than a canonical top-level
runtime environment entry point.

## Technical Approach

The fix will move the documentation-specific dependency file into a repository
location that better matches its purpose, then update every workflow or
documentation reference that points to it.

The implementation will:

1. move the docs-only requirements file out of the repository root;
2. update the GitHub Pages workflow to install from the new path;
3. update the affected Sphinx and user-facing documentation references so the
   documented build and publication flow stays accurate;
4. preserve the existing dependency split between the full runtime
   `requirements.txt` and the lightweight documentation build environment.

No subagent is planned for this implementation. The change is small, local, and
does not justify delegation.

## Involved Components

- the current root-level `requirements-docs.txt`
- `.github/workflows/publish-sphinx-pages.yml`
- `site/getting_started/local_build.rst`
- `site/getting_started/github_pages.rst`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Relocate the docs-only requirements file into a repository-consistent
   support path.
2. Update the GitHub Pages workflow and all documentation references to the new
   path.
3. Rebuild the Sphinx portal locally to verify the documentation path remains
   valid.
4. Run the required Markdown checks on the touched Markdown scope.
5. Report completion and wait for explicit approval before creating the commit.
