# Sphinx Canonical Integration Phase 3 Core Training Infrastructure

## Overview

This document defines the next canonical Sphinx integration batch after the
completed Phase 2 documentation-asset integration.

The goal of this phase is to expose the shared training infrastructure used by
the TE regression workflows, rather than jumping immediately to broader model
family coverage or learning-guide migration.

This scope is the most defensible next step because it captures the reusable
training backbone that all current neural training flows depend on.

## Technical Approach

The implementation should follow the existing incremental Sphinx strategy:

- improve only the high-value public docstrings needed for readable generated
  API pages;
- add canonical API pages under `docs/api/training/`;
- keep the scope on reusable infrastructure instead of one-off entry points;
- cross-link the infrastructure pages with the already integrated training
  entry page for `train_feedforward_network.py`.

The selected modules for this batch are:

- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/transmission_error_datamodule.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/validate_training_setup.py`

This intentionally excludes:

- model-family coverage, which remains a later batch;
- tree-regression orchestration, which remains a later batch;
- dataset API coverage, which remains a later batch;
- learning-guide migration, which remains a separate content-integration task.

## Involved Components

- `docs/api/index.rst`
- `docs/api/training/index.rst`
- `docs/api/training/`
- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/transmission_error_datamodule.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/validate_training_setup.py`
- `doc/guide/project_usage_guide.md` if the runnable documentation surface
  changes materially

## Implementation Steps

1. Inspect the four target training-infrastructure modules and identify the
   public classes and functions worth exposing.
2. Rewrite the high-value public docstrings in canonical source files using the
   current repository style and Google-style API structure where useful.
3. Add canonical Sphinx API pages for the infrastructure modules under
   `docs/api/training/`.
4. Update the training API index so the new pages become navigable from the
   portal.
5. Build the Sphinx site with warnings treated as errors and fix any signature,
   import, or cross-link issues.
6. Reassess whether the batch changed runnable user-facing workflows enough to
   require a `project_usage_guide.md` update before the final commit.
