# MkDocs Proof Of Concept

## Overview

This document defines an isolated proof of concept for a repository-wide code documentation system based on:

- `MkDocs`
- `Material for MkDocs`
- `mkdocstrings`

The goal is to validate whether this stack can become the future documentation platform for the repository and support a later workflow such as:

- `update code documentation`

The proof of concept should remain limited, isolated, and conflict-safe.

It should not attempt a full repository migration yet.

Instead, it should demonstrate:

- a documentation site configuration;
- one small API reference slice generated from the repository code;
- one or more existing repository-authored Markdown pages integrated into the site;
- a navigation structure that shows how guides and API reference could coexist.

## Technical Approach

### Why MkDocs Is The First Candidate To Test

The preceding evaluation selected the `MkDocs + Material + mkdocstrings` stack as the best fit for the current repository profile because:

- the repository is heavily Markdown-oriented;
- the Python codebase is important, but not the only documentation target;
- future docs should present guides and API reference in one coherent portal;
- the stack is well suited to a single rebuild command.

### Official Setup Direction

The proof of concept should follow the current official setup model:

- `MkDocs` uses a root `mkdocs.yml` configuration file and a docs source directory;
- `Material for MkDocs` is enabled through the `theme` section;
- `mkdocstrings` is enabled through the `plugins` section;
- Python API reference blocks can then be embedded directly into Markdown pages.

Official references used for this planning note:

- `MkDocs` getting started:
  <https://www.mkdocs.org/getting-started/>
- `MkDocs` configuration:
  <https://www.mkdocs.org/user-guide/configuration/>
- `Material for MkDocs` getting started:
  <https://squidfunk.github.io/mkdocs-material/getting-started/>
- `Material for MkDocs` site creation:
  <https://squidfunk.github.io/mkdocs-material/creating-your-site/>
- `mkdocstrings` overview:
  <https://mkdocstrings.github.io/>
- `mkdocstrings` handlers:
  <https://mkdocstrings.github.io/usage/handlers/>

### Recommended Proof-Of-Concept Scope

The proof of concept should document only a narrow, representative subset of the repository.

Recommended initial scope:

- one code reference page for:
  - `scripts/models/feedforward_network.py`
- one guide page imported from or mirrored after:
  - `doc/guide/project_usage_guide.md`
- one landing page describing the repository documentation portal concept

This scope is intentionally small because it should validate:

- visual quality;
- code-reference extraction quality;
- navigation quality;
- maintenance burden

without prematurely restructuring the full repository documentation tree.

### Recommended Output Layout

Because the work is still in isolated mode, the proof of concept should not immediately become a canonical repository feature.

The safest isolated structure is:

- `mkdocs.yml`
- a standalone docs-source tree for the proof of concept, for example:
  - `doc_site/`
    - `index.md`
    - `guide/`
    - `reference/`

The exact folder name may be adjusted during implementation, but it should remain clearly separated from the existing canonical `doc/` tree until synchronized integration is approved.

### Recommended Navigation For The Proof Of Concept

Initial navigation should be intentionally small:

1. `Home`
2. `Usage Guide`
3. `API Reference`
   - `FeedForward Network Module`

This is enough to validate:

- narrative docs;
- generated Python API docs;
- cross-navigation between both.

### Dependency Strategy

The proof of concept will likely require adding or tracking these dependencies:

- `mkdocs`
- `mkdocs-material`
- `mkdocstrings[python]`

However, because the work is still isolated:

- the proof of concept should not yet modify `requirements.txt` unless explicitly approved as part of implementation;
- dependency changes should remain part of the isolated branch until later synchronized integration.

### Automation Goal

The proof of concept should be designed so it can later evolve into a stable repository command that:

- rebuilds the docs portal;
- refreshes API reference pages;
- validates that the documentation site still builds.

The proof-of-concept implementation should therefore aim to make the future automation path obvious, even if the final command is not yet fully formalized.

## Involved Components

- `scripts/models/feedforward_network.py`
  Small representative Python module for generated API reference.
- `doc/guide/project_usage_guide.md`
  Representative narrative guide for portal integration.
- future proof-of-concept configuration:
  - `mkdocs.yml`
- future proof-of-concept docs source tree:
  - isolated docs-site source directory to be created during implementation
- `readme.temp.md`
  Isolated handoff log that must record the proof-of-concept work.

## Implementation Steps

1. Keep this planning document as the approval gate for the proof-of-concept implementation.
2. After approval, create the isolated MkDocs proof-of-concept structure.
3. Add the minimal `mkdocs.yml` configuration.
4. Add one landing page and one guide page into the proof-of-concept docs source tree.
5. Add one API-reference page for `scripts/models/feedforward_network.py` using `mkdocstrings`.
6. Install or otherwise prepare the needed documentation dependencies in an isolated-safe way.
7. Build and preview the site locally.
8. Evaluate the resulting UX, navigation clarity, and API rendering quality.
9. Record the outcome in `readme.temp.md` so the synchronized integration phase can later decide whether to promote the proof of concept into a canonical repository documentation platform.
