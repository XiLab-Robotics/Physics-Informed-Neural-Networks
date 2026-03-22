# Documentation Platform Direction, Docstring Standard, And Dual POC Plan

## Overview

This document defines the next isolated documentation phase for the repository.

The user requested four related outcomes:

1. define an official repository docstring standard;
2. run an isolated proof of concept by rewriting the documentation for:
   - `scripts/models/feedforward_network.py`
   - `scripts/training/train_feedforward_network.py`
3. create a parallel `Sphinx + Read the Docs` proof of concept to compare API readability and site structure against the existing `MkDocs` direction;
4. prepare the future publication path on `GitHub Pages`, including a later documentation link from `README.md`.

The user also provided a strong visual and structural reference:

- `ur_rtde`
- site root:
  <https://sdurobotics.gitlab.io/ur_rtde/>
- API reference:
  <https://sdurobotics.gitlab.io/ur_rtde/api/api.html>
- local visual reference PDF:
  - `.temp/example.pdf`

The local PDF reference was later added to the workspace and inspected directly.
It confirms that the desired direction is strongly API-first, with:

- compact left-navigation hierarchy;
- clear visual separation of signatures and descriptions;
- prominent note blocks;
- dense but readable parameter lists;
- overall emphasis on clarity over decorative styling.

This phase remains in isolated mode. Therefore, the implementation must avoid risky canonical repository edits and instead build a reusable comparison package that can later be integrated after synchronization on the other PC.

## Technical Approach

### Hosting Decision

No external documentation hosting platform is required.

`GitHub Pages` is sufficient for both:

- `MkDocs`
- `Sphinx`

because both stacks generate static HTML output.

Relevant official references:

- `GitHub Pages`:
  <https://docs.github.com/en/pages>
- `MkDocs` deployment:
  <https://www.mkdocs.org/user-guide/deploying-your-docs/>
- `Material for MkDocs` publishing guidance:
  <https://squidfunk.github.io/mkdocs-material/publishing-your-site/>
- `Sphinx` HTML builders:
  <https://www.sphinx-doc.org/>

The hosting question is therefore settled:

- future online publication can stay on `GitHub Pages`.

### Official Repository Docstring Standard

The official recommended docstring standard for this repository is:

- `Google-style docstrings`

Reasoning:

- readable inside the code editor;
- supported by `mkdocstrings-python`;
- supported by `Sphinx` through `napoleon`;
- expressive enough for parameters, returns, raises, examples, and notes;
- compatible with gradual adoption rather than an all-at-once rewrite.

The standard should apply primarily to modules that will appear in generated API documentation.

Minimum section policy for important public functions and methods:

- one summary sentence;
- one short descriptive paragraph when the behavior is not obvious;
- `Args` for non-trivial inputs;
- `Returns` when something is returned;
- `Raises` when runtime validation is meaningful;
- `Notes` when there are repository-specific constraints or workflow semantics;
- `Examples` when usage clarity materially improves the page.

This standard does not replace internal section comments in function bodies. Both are still needed:

- docstrings explain the API contract;
- code comments keep the implementation readable.

### Isolated Real-Module Documentation POC

The user explicitly asked for an isolated rewrite of the documentation for:

- `scripts/models/feedforward_network.py`
- `scripts/training/train_feedforward_network.py`

Because the repository is still in isolated mode, the safest strategy is not to rewrite the canonical source files yet.

Instead, the isolated proof of concept should:

1. create mirrored standalone copies of the two modules under an isolated source root;
2. rewrite the mirrored copies with rich Google-style docstrings;
3. preserve the original runtime logic as closely as practical for documentation purposes;
4. point the documentation generators to the isolated mirrored modules instead of the canonical ones.

This approach demonstrates the real output quality without touching conflict-prone shared files.

Recommended isolated source root:

- `poc_sources/mirrored_repo/`

Recommended mirrored module names:

- `poc_sources/mirrored_repo/feedforward_network_documented.py`
- `poc_sources/mirrored_repo/train_feedforward_network_documented.py`

### MkDocs POC Extension

The current `MkDocs` proof of concept should be extended so it contains both:

- the current low-docstring repository pages;
- the new isolated rich-docstring mirrored pages.

This side-by-side structure is important because it makes the quality difference explicit.

Recommended `MkDocs` additions:

- one page for the documented mirrored feedforward model module;
- one page for the documented mirrored training script;
- clear labels distinguishing:
  - current repository module output;
  - isolated documented mirror output.

### Sphinx + Read The Docs POC

A second isolated portal should be created using:

- `Sphinx`
- `sphinx-rtd-theme`
- `sphinx.ext.autodoc`
- `sphinx.ext.napoleon`

The purpose is not to replace `MkDocs` immediately.

The purpose is to answer a design question with direct evidence:

- how close can the project get to the `ur_rtde` API style under `MkDocs`?
- how much closer does `Sphinx + RTD` get with the same documented content?

To keep the comparison fair, the `Sphinx` proof of concept should document the same isolated mirrored modules used in the richer `MkDocs` proof of concept.

Recommended isolated structure:

- `sphinx_poc/`
  - `conf.py`
  - `index.rst` or `index.md`
  - `api/`
  - `guide/`

### Reference-Driven Design Criteria

The visual comparison should be judged against the user reference using these criteria:

- left navigation clarity;
- readability of long signatures;
- clarity of parameter and return sections;
- density without crowding;
- discoverability of classes, functions, and anchors;
- consistency between guide pages and API pages.

This is more important than simply adopting the nominally more popular tool.

### GitHub Pages Publication Path

After the preferred stack is selected, the future synchronized integration should add:

- a static-site build workflow for the chosen documentation stack;
- `GitHub Pages` publication configuration;
- an online documentation link in `README.md`.

Because the repository is still in isolated mode, the current phase should limit itself to:

- designing and possibly prototyping the publication path in isolated files;
- recording the exact integration steps for later;
- avoiding canonical `README.md` modification until synchronized integration is intentionally performed.

## Involved Components

- current isolated MkDocs POC:
  - `mkdocs.poc.yml`
  - `doc_site_poc/`
- new isolated mirrored source tree:
  - `poc_sources/mirrored_repo/`
- existing canonical source modules used as documentation reference:
  - `scripts/models/feedforward_network.py`
  - `scripts/training/train_feedforward_network.py`
- new isolated `Sphinx` proof of concept tree:
  - `sphinx_poc/`
- isolated handoff log:
  - `readme.temp.md`
- future synchronized integration targets:
  - `README.md`
  - documentation deployment workflow files if adopted later

## Implementation Steps

1. Keep this document as the approval gate for the docstring-standard and dual-portal proof-of-concept phase.
2. Record the official repository docstring standard as Google-style in the isolated handoff materials.
3. Create isolated mirrored copies of:
   - `feedforward_network.py`
   - `train_feedforward_network.py`
4. Rewrite the mirrored copies with rich Google-style docstrings while keeping the code behavior representative.
5. Extend the existing `MkDocs` proof of concept with pages that document the mirrored rich-docstring modules.
6. Create an isolated `Sphinx + Read the Docs` proof of concept that documents the same mirrored modules.
7. Build both documentation portals locally and compare their readability against the `ur_rtde` reference criteria.
8. Update `readme.temp.md` with:
   - the chosen docstring standard;
   - the new isolated documentation assets;
   - the comparison outcome;
   - the future GitHub Pages integration notes.
9. Defer canonical `README.md` linking and actual GitHub Pages repository integration to the synchronized post-campaign integration step, unless the user later explicitly decides to leave isolated mode for those shared-file edits.
