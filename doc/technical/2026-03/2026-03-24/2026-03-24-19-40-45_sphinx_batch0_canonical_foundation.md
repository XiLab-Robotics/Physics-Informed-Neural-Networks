# Sphinx Batch0 Canonical Foundation

## Overview

This document defines the canonical implementation of Batch 0 for the repository documentation portal on the `integration/sphinx-docs` branch.

The user approved moving from isolated analysis into canonical implementation, but only for the minimal `Sphinx` foundation identified in the integration analysis:

- create the canonical `docs/` tree;
- configure `Sphinx + RTD`;
- add a minimal section skeleton;
- document how to build the portal locally;
- avoid broader guide migration and broader docstring rewrites for now.

Batch 0 is intentionally narrow. It should establish a stable canonical portal root without yet migrating the whole documentation program.

## Technical Approach

### Scope Included In Batch 0

Batch 0 should implement only the portal foundation:

- `docs/conf.py`
- `docs/index.rst`
- `docs/getting_started/index.rst`
- `docs/getting_started/local_build.rst`
- `docs/getting_started/documentation_scope.rst`
- `docs/guide/index.rst`
- `docs/api/index.rst`
- empty structural folders such as `_static/` and `_templates/`

The configuration should enable:

- `sphinx.ext.autodoc`
- `sphinx.ext.napoleon`
- `sphinx.ext.viewcode`
- `sphinx_rtd_theme`

### Scope Explicitly Excluded From Batch 0

The following work must remain deferred:

- moving learning guides out of `doc/reports/analysis/learning_guides/`
- moving imported `NotebookLM` assets into canonical guide folders
- linking the live documentation site from `README.md`
- adding `GitHub Pages` CI or deployment
- large-scale canonical docstring rewrites
- promoting `MkDocs` proof-of-concept files into canonical infrastructure

### Dependency Strategy

Batch 0 introduces canonical `Sphinx` build dependencies. The repository should therefore start tracking:

- `sphinx`
- `sphinx-rtd-theme`

`myst-parser` remains deferred because Batch 0 does not yet import Markdown guides into the canonical portal.

### Usage Documentation

Because Batch 0 adds a new runnable documentation build workflow, `doc/guide/project_usage_guide.md` should gain a dedicated section covering:

- required dependencies;
- the local HTML build command;
- the output folder.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Internal documentation index that should also reference this technical note.
- `requirements.txt`
  Dependency list that must start tracking the canonical Sphinx stack.
- `doc/guide/project_usage_guide.md`
  Usage guide that should document the new local docs-build workflow.
- `docs/`
  New canonical Sphinx source tree introduced by Batch 0.
- `doc/technical/2026-03/2026-03-24/2026-03-24-19-40-45_sphinx_batch0_canonical_foundation.md`
  This technical implementation note.

## Implementation Steps

1. Create this technical note with a timestamp read from the real local machine clock.
2. Register this technical note in `README.md` and `doc/README.md`.
3. Add the canonical `docs/` Sphinx foundation tree and minimal section pages.
4. Add `sphinx` and `sphinx-rtd-theme` to `requirements.txt`.
5. Update `doc/guide/project_usage_guide.md` with the local Sphinx build workflow.
6. Validate the new foundation with at least a configuration-level review and, if the environment permits, a local Sphinx HTML build.
