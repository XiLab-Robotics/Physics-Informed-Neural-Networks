# Sphinx Canonical Integration Phase1

## Overview

This document defines the first canonical integration phase after the validated Batch 0 `Sphinx` foundation.

The user requested continuing the integration of the isolated documentation work rather than stopping at the empty portal shell.

Phase 1 should therefore promote the highest-value isolated outcomes into canonical repository structure without yet attempting the most conflict-heavy migrations.

The intended outcomes are:

- integrate canonical Markdown content into the `Sphinx` portal without duplicating source-of-truth documents;
- expose the selected `Sphinx` backlog and the documentation-platform comparison report inside the canonical portal;
- surface the recovered `NotebookLM` archive state as a canonical documentation status page;
- add the first real API-reference slice for:
  - `scripts/models/feedforward_network.py`
  - `scripts/training/train_feedforward_network.py`

## Technical Approach

### Scope For Phase 1

Phase 1 should extend the Batch 0 foundation with:

- `MyST` support for Markdown integration inside `Sphinx`;
- a canonical `Project Guide` page sourced from `doc/guide/project_usage_guide.md`;
- a canonical `Technical Notes` page sourced from the recovered `Sphinx` backlog master note;
- a canonical `Selected Reports` page sourced from the recovered documentation-platform comparison report;
- a canonical learning-guide/archive status page that records the recovered `NotebookLM` archive inventory;
- canonical API pages for the first two repository modules selected in the backlog.

### Why MyST Is Needed Now

Batch 0 deliberately deferred Markdown integration.

Phase 1 now needs it because the repository sources to expose canonically already exist in Markdown:

- `doc/guide/project_usage_guide.md`
- `doc/technical/...sphinx_documentation_architecture_backlog_and_github_pages_plan.md`
- `doc/reports/analysis/...code_documentation_platform_comparison_report.md`

Using `MyST` allows the `Sphinx` portal to include those canonical Markdown files through wrappers instead of duplicating or rewriting them into `.rst` immediately.

### API Integration Strategy

The first API slice should remain conservative.

It should not try to expose every helper in the training module yet. Instead:

- add richer Google-style docstrings to the module-level entry points and primary public objects;
- create explicit API pages with `autoclass` and `autofunction` directives for the selected callables;
- avoid expanding into broader training infrastructure modules until the first slice renders cleanly.

### Explicit Non-Goals

Phase 1 still does not include:

- migration of learning-guide folders from `doc/reports/analysis/learning_guides/` to `doc/guide/`
- movement of imported `NotebookLM` media into canonical guide folders
- `GitHub Pages` workflow implementation
- `README.md` link to a live documentation site
- broad repository-wide docstring rewrites beyond the two selected modules

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Internal documentation index that must also reference this technical note.
- `requirements.txt`
  Dependency list that must start tracking `myst-parser`.
- `docs/conf.py`
  Canonical Sphinx configuration to extend with Markdown support.
- `docs/index.rst`
  Portal home page that must expose the new integrated sections.
- `doc/guide/project_usage_guide.md`
  Canonical usage guide to expose inside the Sphinx portal through a wrapper.
- `doc/technical/2026-03-22/2026-03-22-12-40-00_sphinx_documentation_architecture_backlog_and_github_pages_plan.md`
  Canonical backlog master note to expose through the portal.
- `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.md`
  Canonical analysis report to expose through the portal.
- `doc/imports/notebooklm_exports/`
  Recovered archive tree to document canonically without yet migrating files into guide folders.
- `scripts/models/feedforward_network.py`
  First canonical model API module to document.
- `scripts/training/train_feedforward_network.py`
  First canonical training API module to document.

## Implementation Steps

1. Create this technical note and register it in `README.md` and `doc/README.md`.
2. Add `myst-parser` to the canonical dependency list and enable it in `docs/conf.py`.
3. Add canonical wrapper pages for:
   - the project usage guide
   - the Sphinx backlog master note
   - the documentation-platform comparison report
4. Add a canonical archive-status page for the recovered `NotebookLM` imports.
5. Improve the docstrings and module descriptions for the first API slice.
6. Add canonical API pages for the selected model and training modules.
7. Validate the integrated portal with a real `Sphinx -W` HTML build.
