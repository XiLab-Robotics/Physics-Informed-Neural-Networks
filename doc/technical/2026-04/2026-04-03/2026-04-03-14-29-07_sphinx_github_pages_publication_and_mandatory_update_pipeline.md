# Sphinx GitHub Pages Publication And Mandatory Update Pipeline

## Overview

This document defines the next canonical documentation phase for the repository:

1. publish the repository Sphinx portal through GitHub Pages;
2. formalize the repository rule that new scripts, new functionality, and other
   user-facing implementation changes must update the canonical Sphinx portal as
   part of the normal completion workflow.

The current repository already contains the canonical Sphinx source tree under
`site/` and the local warning-as-error build command:

- `python -m sphinx -W -b html site site/_build/html`

The current repository state also confirms that GitHub Pages was already chosen
earlier as the intended publication target, but the actual publication workflow
was still deferred and has not yet been implemented.

## Technical Approach

The implementation should deliver two coordinated outcomes.

### 1. GitHub Pages Publication

Add the canonical repository-owned publication path for the Sphinx portal.

The expected implementation is:

- a GitHub Actions workflow under `.github/workflows/`;
- build the Sphinx site from the canonical `site/` tree;
- publish the generated HTML output from `site/_build/html/` to GitHub Pages;
- keep the publication workflow aligned with the repository-owned Python
  environment and documented local build path;
- avoid introducing a second competing documentation stack or a parallel manual
  publish path.

If a repository setting or Pages source configuration cannot be changed from the
local repository alone, the implementation should still prepare the complete
workflow files and document the remaining repository-settings step explicitly.

### 2. Mandatory Sphinx Update Rule

Formalize the repository rule so future changes do not leave the Sphinx portal
stale.

The new rule should state that when approved work introduces or materially
changes:

- a new script;
- a new runnable feature;
- a new user-facing workflow;
- a new API surface that belongs in the code reference;
- a changed usage path that affects docs navigation or examples,

the task must also update the canonical Sphinx source tree under `site/` as
needed, regenerate the Sphinx build, and keep the portal warning-free before
task closure.

This rule should be recorded in the canonical repository rule surfaces,
especially:

- `AGENTS.md`
- `doc/reference_summaries/06_Programming_Style_Guide.md` only if the rule also
  belongs in the persistent Python/documentation style guidance;
- `doc/guide/project_usage_guide.md` when the user-facing local and published
  documentation workflow changes;
- optionally `README.md` if the public-facing landing page should expose the
  future live documentation URL or the publication status.

## Involved Components

- `.github/workflows/`
- `site/`
- `site/conf.py`
- `site/getting_started/local_build.rst`
- `AGENTS.md`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`
- optionally `README.md`

## Implementation Steps

1. Keep this technical document as the approval gate for the GitHub Pages and
   mandatory-update documentation phase.
2. Create the repository-owned GitHub Actions workflow that builds the Sphinx
   portal and publishes it to GitHub Pages.
3. Update the canonical documentation notes so the local build and publication
   workflow are explicit and discoverable.
4. Formalize the repository rule that approved implementation work must also
   update the Sphinx portal when the change affects scripts, features, usage,
   or API documentation.
5. Regenerate the Sphinx portal and verify that the warning-as-error build still
   succeeds after the workflow and rule updates.
6. Run Markdown warning checks on the touched Markdown scope.
7. Stop after implementation and verification, report the outcome, and wait for
   explicit approval before creating any Git commit.
