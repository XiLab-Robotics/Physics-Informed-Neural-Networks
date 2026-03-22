# Docstring Standard And Rich API POC

## Overview

This document defines the next isolated step after the MkDocs proof of concept.

The user clarified two important requirements:

1. the future documentation site should be publishable on GitHub;
2. the generated API documentation must be richer than the current minimal output and should include detailed explanations of:
   - what functions do;
   - their inputs;
   - their outputs;
   - practical usage context.

The user also provided a style reference:

- `ur_rtde`
- site root:
  <https://sdurobotics.gitlab.io/ur_rtde/>
- API reference:
  <https://sdurobotics.gitlab.io/ur_rtde/api/api.html>

The purpose of this task is not to fully replicate that site exactly, but to move the current proof of concept closer to the same level of API documentation richness.

## Technical Approach

### Hosting Decision

No separate hosting platform is required.

Both `MkDocs` and `Sphinx` generate static HTML sites that can be published on `GitHub Pages`.

Relevant official references:

- `MkDocs` can be hosted on GitHub Pages:
  <https://www.mkdocs.org/user-guide/deploying-your-docs/>
- `MkDocs` builds static HTML sites that can be hosted anywhere:
  <https://www.mkdocs.org/>
- `Material for MkDocs` also documents GitHub Pages publishing:
  <https://squidfunk.github.io/mkdocs-material/publishing-your-site/>
- GitHub currently recommends GitHub Actions for GitHub Pages automation:
  <https://docs.github.com/pages>
  and:
  <https://docs.github.com/en/articles/setting-a-markdown-processor-for-your-github-pages-site-using-jekyll>

Therefore, if the project later stays on `MkDocs`, GitHub Pages remains a valid deployment target.

### Important Architectural Clarification

The current poor richness of the generated API documentation is not primarily a `MkDocs` limitation.

It is mostly a source-docstring limitation.

At the moment, many repository Python functions use very short docstrings such as:

- `Forward Pass`
- `Parse Command Line Arguments`
- `Print Key Value`

Those short docstrings do not contain enough semantic structure for a documentation generator to render sections such as:

- description;
- arguments;
- returns;
- raised errors;
- examples;
- notes.

### Recommended Docstring Standard

For this repository, the recommended future standard is:

- `Google-style docstrings`

Reason:

- officially supported by `mkdocstrings-python`;
- also well supported by `Sphinx` through `napoleon`;
- readable directly inside the code;
- expressive enough for rich API pages.

Official references:

- `mkdocstrings-python` docstring styles:
  <https://mkdocstrings.github.io/python/usage/configuration/docstrings/>
- Google-style rendering reference:
  <https://mkdocstrings.github.io/python/usage/docstrings/google/>
- `Sphinx napoleon` support for Google-style docstrings:
  <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>

### Rich API Proof Of Concept Strategy

Because the repository is still in isolated mode, this task should not rewrite canonical project source files yet.

Instead, the proof of concept should:

1. keep the current MkDocs proof of concept;
2. configure `mkdocstrings` explicitly for Google-style docstrings;
3. add a standalone demonstration module with rich docstrings;
4. add one API page for that demonstration module;
5. compare its rendering with the existing sparse-docstring module pages.

This keeps the experiment conflict-safe while still demonstrating the intended future documentation quality.

### Recommended Demonstration Module

Create a standalone proof-of-concept Python module outside the canonical source tree, for example under:

- `poc_sources/`

The module should mirror the style and topics of the current training scripts while using rich Google-style docstrings.

Recommended content:

- one formatting helper;
- one configuration helper;
- one orchestration-style function;
- one small dataclass or typed structure.

This should be enough to show:

- sectioned arguments;
- return-value documentation;
- note blocks;
- example blocks;
- a richer API page than the current minimal repository source pages.

### Expected Outcome

After implementation, the proof of concept should show:

- existing API pages generated from current project modules;
- a richer API page generated from a standalone demo module using structured docstrings;
- a clearer basis for deciding whether the repository should:
  - adopt Google-style docstrings broadly;
  - stay on MkDocs;
  - or switch to Sphinx later if even more API-centric structure is required.

## Involved Components

- `mkdocs.poc.yml`
  Existing isolated MkDocs proof-of-concept configuration.
- `doc_site_poc/`
  Existing isolated docs source tree.
- new isolated proof-of-concept source tree:
  - `poc_sources/`
- `readme.temp.md`
  Isolated handoff log.

## Implementation Steps

1. Keep this document as the approval gate for the rich-API proof-of-concept step.
2. Update the MkDocs proof-of-concept configuration to use Google-style docstring parsing.
3. Add a standalone demonstration Python module with rich Google-style docstrings.
4. Add a new API reference page for that demonstration module.
5. Rebuild the MkDocs proof of concept.
6. Record the result in `readme.temp.md` so the synchronized integration phase can later decide whether to formalize the docstring standard and promote the documentation portal.
