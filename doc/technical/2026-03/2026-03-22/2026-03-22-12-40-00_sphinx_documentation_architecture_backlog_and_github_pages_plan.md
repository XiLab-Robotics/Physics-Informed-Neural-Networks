# Sphinx Documentation Architecture, Backlog, And Integration Plan

## Overview

This document defines the full isolated backlog for migrating the repository
code-documentation effort toward `Sphinx + Read the Docs theme`.

The decision is now clear from the isolated platform comparison work:

- `Sphinx + RTD` is the preferred target documentation stack because it is much
  closer to the desired `ur_rtde` API-reference style;
- `GitHub Pages` remains the approved publication target;
- `Google-style docstrings` remain the approved repository docstring standard
  for generated API documentation.

This document is not the implementation itself.

It is the execution backlog and integration plan that the other Codex instance
should use after the training campaign is finished and the repository is fully
synchronized.

## Technical Approach

### Target Documentation Stack

The target portal stack is:

- `Sphinx`
- `sphinx-rtd-theme`
- `sphinx.ext.autodoc`
- `sphinx.ext.napoleon`
- `sphinx.ext.viewcode`

Optional later additions if needed:

- `myst-parser` for broader Markdown integration
- `sphinx-copybutton`
- `sphinx-design`

### Official Docstring Standard

The repository-standard docstring format for generated API documentation should
be:

- `Google-style docstrings`

Reasoning:

- readable in source files;
- supported by `Sphinx napoleon`;
- structured enough for `Args`, `Returns`, `Raises`, `Notes`, and `Examples`;
- compatible with gradual migration.

### Final Documentation Objectives

The final documentation portal should combine these content families:

- landing and orientation pages;
- operational usage guide;
- learning guides;
- generated API reference for Python modules;
- selected technical and report documentation where helpful;
- online publication through `GitHub Pages`.

### Migration Strategy

The migration should be incremental and batch-based.

Do not attempt a repository-wide documentation rewrite in one pass.

Preferred execution order:

1. lock down the canonical `Sphinx` project structure;
2. integrate the high-value guide pages and entry points;
3. improve docstrings for the highest-value Python modules;
4. publish a first online version through `GitHub Pages`;
5. expand in small batches while preserving readability and low conflict risk.

## Involved Components

### Existing Documentation Content

- `doc/guide/project_usage_guide.md`
- `doc/reports/analysis/learning_guides/`
- `doc/reports/analysis/model_explanatory/`
- selected technical documents under `doc/technical/`
- selected reports under `doc/reports/analysis/`

### Existing Python Code Surface

- `scripts/models/`
- `scripts/training/`
- `scripts/datasets/`
- `scripts/reports/`

### Future Documentation Portal Components

- future canonical `Sphinx` source tree
- future publication workflow for `GitHub Pages`
- `README.md` online documentation link

## Implementation Steps

1. Use this document as the master isolated backlog for the `Sphinx` direction.
2. Re-check repository synchronization before touching canonical files.
3. Create the canonical `Sphinx` project structure in the synchronized branch.
4. Integrate the first narrative pages and the first API-reference batch.
5. Add `GitHub Pages` publication support.
6. Add the online documentation link to `README.md`.
7. Continue integrating guides and modules in planned small batches.

## Target Sphinx Architecture

Recommended canonical documentation tree:

- `docs/`
  - `conf.py`
  - `index.rst`
  - `getting_started/`
  - `guide/`
  - `learning_guides/`
  - `model_reference/`
  - `api/`
  - `technical/`
  - `reports/`
  - `_static/`
  - `_templates/`

Recommended homepage structure:

- `Overview`
- `Project Usage`
- `Learning Guides`
- `Model Reference`
- `API Reference`
- `Technical Notes`
- `Selected Reports`

Recommended top-level toctree sections:

1. `Getting Started`
2. `Project Guide`
3. `Learning Guides`
4. `Model Reference`
5. `API Reference`
6. `Technical Notes`
7. `Selected Reports`

## Final Site Section Structure

### 1. Getting Started

Purpose:

- orient new readers quickly;
- explain what the repository does;
- explain how to build and browse the docs locally.

Planned pages:

- `docs/getting_started/index.rst`
- `docs/getting_started/local_build.rst`
- `docs/getting_started/documentation_scope.rst`

### 2. Project Guide

Purpose:

- expose operational repository usage documentation.

Primary source:

- `doc/guide/project_usage_guide.md`

Planned canonical documentation page:

- `docs/guide/project_usage_guide.rst` or a Markdown-integrated equivalent

### 3. Learning Guides

Purpose:

- provide didactic, reader-facing educational material.

Current source family:

- `doc/reports/analysis/learning_guides/`

Current canonical guide inventory:

1. `Neural Network Foundations`
2. `Training, Validation, And Testing`
3. `TE Model Curriculum`
4. `FeedForward Network`
5. `Harmonic Regression`
6. `Periodic Feature Network`
7. `Residual Harmonic Network`

Planned future target in synchronized integration:

- preferred canonical root remains the user-approved direction:
  - `doc/guide/<Guide Name>/`

For the documentation portal itself, planned pages should live under:

- `docs/learning_guides/<guide_slug>/index.rst`

and either:

- re-render or include the canonical guide Markdown;
- or mirror it into reStructuredText / MyST pages during integration.

Planned future additional guide:

- `Multilayer Perceptrons`

which currently exists only in imported NotebookLM material and should remain in
backlog until canonical integration decisions are executed.

### 4. Model Reference

Purpose:

- provide a conceptual bridge between learning guides and low-level API docs.

Current source family:

- `doc/reports/analysis/model_explanatory/`

Current model-reference inventory:

1. `FeedForward Network`
2. `Harmonic Regression`
3. `Periodic Feature Network`
4. `Residual Harmonic Network`

Planned portal location:

- `docs/model_reference/<model_slug>/index.rst`

### 5. API Reference

Purpose:

- provide generated developer-facing reference for Python modules.

Planned section grouping:

- `API / Models`
- `API / Training`
- `API / Datasets`
- `API / Reports`

### 6. Technical Notes

Purpose:

- preserve the most useful technical decision documents without exposing the
  full historical backlog on the front page.

Current source family:

- `doc/technical/`

Approach:

- select important current-state technical notes;
- do not indiscriminately dump the full timestamped archive into the portal.

### 7. Selected Reports

Purpose:

- surface a small number of high-value analytical and campaign reports.

Approach:

- curate, do not mirror everything.

## Python Module Integration Inventory

Current Python module inventory under `scripts/`:

### Models

1. `scripts/models/feedforward_network.py`
2. `scripts/models/harmonic_regression.py`
3. `scripts/models/periodic_feature_network.py`
4. `scripts/models/residual_harmonic_network.py`
5. `scripts/models/model_factory.py`
6. `scripts/models/__init__.py`

### Training

1. `scripts/training/train_feedforward_network.py`
2. `scripts/training/train_tree_regressor.py`
3. `scripts/training/run_training_campaign.py`
4. `scripts/training/run_training_smoke_test.py`
5. `scripts/training/validate_training_setup.py`
6. `scripts/training/shared_training_infrastructure.py`
7. `scripts/training/transmission_error_datamodule.py`
8. `scripts/training/transmission_error_regression_module.py`
9. `scripts/training/tree_regression_support.py`
10. `scripts/training/__init__.py`

### Datasets

1. `scripts/datasets/transmission_error_dataset.py`
2. `scripts/datasets/visualize_transmission_error.py`
3. `scripts/datasets/__init__.py`

### Reports

1. `scripts/reports/generate_styled_report_pdf.py`
2. `scripts/reports/generate_model_report_diagrams.py`
3. `scripts/reports/run_report_pipeline.py`
4. `scripts/reports/validate_report_pdf.py`
5. `scripts/reports/__init__.py`

### Root Package Files

1. `scripts/__init__.py`

## Planned API Batch Roadmap

### Batch 0: Portal Foundation

Scope:

- create canonical `Sphinx` project tree;
- add landing page;
- add project guide section shell;
- add empty API section shells;
- integrate local build instructions.

Checklist:

- [ ] create `docs/` root
- [ ] create `conf.py`
- [ ] create root `index.rst`
- [ ] enable `autodoc`, `napoleon`, `viewcode`
- [ ] enable `sphinx-rtd-theme`
- [ ] verify local HTML build

### Batch 1: First API Slice

Scope:

- `feedforward_network.py`
- `train_feedforward_network.py`

Checklist:

- [ ] rewrite key public docstrings in canonical source files
- [ ] add API pages under `docs/api/models/`
- [ ] add API pages under `docs/api/training/`
- [ ] validate signature readability
- [ ] validate parameter-section readability
- [ ] compare against isolated POC output

### Batch 2: Core Training Infrastructure

Scope:

- `shared_training_infrastructure.py`
- `transmission_error_datamodule.py`
- `transmission_error_regression_module.py`
- `validate_training_setup.py`

Checklist:

- [ ] identify public classes and functions
- [ ] rewrite high-value docstrings
- [ ] add API pages
- [ ] check cross-links between training workflow and infrastructure

### Batch 3: Model Family API Coverage

Scope:

- `harmonic_regression.py`
- `periodic_feature_network.py`
- `residual_harmonic_network.py`
- `model_factory.py`

Checklist:

- [ ] document model constructors and forward methods
- [ ] document model-selection factory logic
- [ ] add model-family API pages
- [ ] cross-link to learning guides and model-reference pages

### Batch 4: Training Entry Points And Orchestration

Scope:

- `run_training_campaign.py`
- `run_training_smoke_test.py`
- `train_tree_regressor.py`
- `tree_regression_support.py`

Checklist:

- [ ] document campaign execution entry points
- [ ] document smoke-test workflow
- [ ] document tree-regression support utilities
- [ ] clarify output-artifact conventions in docstrings

### Batch 5: Dataset API Coverage

Scope:

- `transmission_error_dataset.py`
- `visualize_transmission_error.py`

Checklist:

- [ ] document dataset semantics
- [ ] document split and sample structure
- [ ] document visualization utilities

### Batch 6: Report Tooling API Coverage

Scope:

- `generate_styled_report_pdf.py`
- `generate_model_report_diagrams.py`
- `run_report_pipeline.py`
- `validate_report_pdf.py`

Checklist:

- [ ] document report pipeline entry points
- [ ] document diagram generation flow
- [ ] document PDF validation flow
- [ ] expose relevant helper classes and functions

### Batch 7: Learning Guide Portal Integration

Scope:

- integrate the 7 current learning guides into the `Sphinx` portal

Checklist:

- [ ] decide `MyST` vs mirrored RST strategy
- [ ] import `Neural Network Foundations`
- [ ] import `Training, Validation, And Testing`
- [ ] import `TE Model Curriculum`
- [ ] import `FeedForward Network`
- [ ] import `Harmonic Regression`
- [ ] import `Periodic Feature Network`
- [ ] import `Residual Harmonic Network`
- [ ] preserve local assets and figures
- [ ] preserve PDF companion discoverability where useful

### Batch 8: Model Reference Portal Integration

Scope:

- integrate the model explanatory reports

Checklist:

- [ ] integrate `FeedForward Network`
- [ ] integrate `Harmonic Regression`
- [ ] integrate `Periodic Feature Network`
- [ ] integrate `Residual Harmonic Network`
- [ ] preserve architecture and conceptual diagrams

### Batch 9: Imported NotebookLM Learning Materials

Scope:

- migrate the imported external guide materials into the user-approved guide
  subtree during synchronized integration

Checklist:

- [ ] re-check conflicts against synchronized repo state
- [ ] move canonical guides toward `doc/guide/<Guide Name>/`
- [ ] move imported guide media into the matching guide folders
- [ ] normalize filenames to readable final names
- [ ] decide final handling of `Multilayer Perceptrons`

### Batch 10: Selected Technical And Report Pages

Scope:

- curate a small set of technical notes and reports into the portal

Checklist:

- [ ] choose current-state technical notes only
- [ ] choose high-value analytical or campaign reports only
- [ ] avoid overwhelming the main portal navigation

### Batch 11: GitHub Pages Publication

Scope:

- publish the chosen `Sphinx` site online

Checklist:

- [ ] decide output folder strategy for deployment
- [ ] add documentation build workflow
- [ ] configure `GitHub Pages`
- [ ] verify published site path
- [ ] verify navigation and assets on the live site

### Batch 12: Repository README Integration

Scope:

- add the online documentation entry point to the repository `README.md`

Checklist:

- [ ] add a short `Documentation` section or link block to `README.md`
- [ ] point it to the live `GitHub Pages` URL
- [ ] verify the link after publication

## Recommended Final Navigation Map

Recommended top-level navigation:

1. `Home`
2. `Getting Started`
3. `Project Guide`
4. `Learning Guides`
5. `Model Reference`
6. `API Reference`
7. `Technical Notes`
8. `Selected Reports`

Recommended API subsection navigation:

1. `Models`
2. `Training`
3. `Datasets`
4. `Reports`

Recommended learning-guide subsection navigation:

1. `Neural Network Foundations`
2. `Training, Validation, And Testing`
3. `TE Model Curriculum`
4. `FeedForward Network`
5. `Harmonic Regression`
6. `Periodic Feature Network`
7. `Residual Harmonic Network`
8. later optional:
   - `Multilayer Perceptrons`

## Canonical Docstring Migration Checklist

Apply this checklist for every Python file integrated into the portal:

- [ ] identify public classes and functions
- [ ] add a summary sentence to each public callable
- [ ] add descriptive paragraph where behavior is not obvious
- [ ] add `Args` for non-trivial inputs
- [ ] add `Returns` where applicable
- [ ] add `Raises` where validations matter
- [ ] add `Notes` for repository-specific workflow semantics
- [ ] add `Examples` where usage is easier to understand with concrete calls
- [ ] keep internal section comments in function bodies
- [ ] verify generated page readability after build

## Synchronized Integration Checklist

When the other PC is ready and the repo is synchronized, the implementation pass
should first run this checklist before touching canonical files:

- [ ] verify current branch and synchronization state
- [ ] inspect whether `README.md` changed on the other PC
- [ ] inspect whether `doc/README.md` changed on the other PC
- [ ] inspect whether `doc/guide/project_usage_guide.md` changed on the other PC
- [ ] inspect whether learning guides moved or were edited meanwhile
- [ ] inspect whether additional Python modules were added meanwhile
- [ ] inspect whether documentation-related dependencies changed meanwhile
- [ ] re-run conflict analysis for imported NotebookLM materials
- [ ] create a fresh integration technical document
- [ ] create an integration checklist specific to the synchronized state

## GitHub Pages Integration Notes

The user approved `GitHub Pages` as the final online publication target.

Recommended future implementation tasks:

- build the `Sphinx` HTML site in CI;
- publish it through `GitHub Pages`;
- keep the live documentation URL stable;
- add one repository `README.md` link to the live site.

This part must remain deferred until synchronized integration, because both the
workflow files and `README.md` are shared repository files.

## Recommended Execution Order After Synchronization

1. implement canonical `Sphinx` project foundation
2. integrate `README`-independent local build first
3. complete Batch 1 on the feedforward slice
4. publish first online version through `GitHub Pages`
5. add online docs link to `README.md`
6. continue with Batch 2 onward in small increments
7. move learning guides and imported guide media only when conflict checks are
   complete

## Deliverables Expected From The Future Integration Phase

The future synchronized implementation should eventually produce:

- canonical `Sphinx` documentation tree
- generated API reference for the highest-value Python modules
- integrated project guide pages
- integrated learning guides
- published `GitHub Pages` documentation site
- repository `README.md` link to the live documentation
- updated handoff and technical documentation for traceability
