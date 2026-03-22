# Code Documentation Platform Evaluation

## Overview

This document evaluates documentation-platform options for the repository-wide code documentation workflow requested by the user.

The goal is not only to pick a tool that can generate API reference pages, but to identify a maintainable documentation system for the current repository shape:

- Python source code under `scripts/`
- many Markdown documents already maintained under `doc/`
- YAML-driven workflows under `config/`
- a growing need to support an instruction such as:
  - `update code documentation`

The user already knows `Doxygen` by name, but is open to alternatives if they offer a better fit.

This evaluation therefore compares the main realistic candidates and judges them against the actual repository profile rather than against a generic Python-package scenario.

## Technical Approach

### Repository Fit Snapshot

The current repository is not a pure Python library with API docs as its only documentation need.

It is a mixed documentation repository with:

- heavy Markdown presence;
- moderate Python code volume;
- operational and analytical documents that already exist;
- guide-oriented content that should eventually live under `doc/guide/`.

A quick repository inspection shows:

- Markdown files are dominant;
- Python files are relatively limited in count;
- YAML configuration files are also significant.

This means the best documentation solution should support both:

- curated guide pages;
- generated API reference pages.

### Evaluation Criteria

The options below are compared using these criteria:

1. how well they document Python code;
2. how naturally they integrate existing Markdown documentation;
3. how easy they are to automate;
4. how good the generated output looks by default;
5. how suitable they are for a repository that mixes guides, reports, and code;
6. whether they require runtime imports or can work through static analysis;
7. whether they support future growth without a large documentation-maintenance burden.

## Option Comparison

### 1. MkDocs + Material + mkdocstrings

#### What It Is

`MkDocs` is a static documentation-site generator focused on Markdown.

`Material for MkDocs` is the most common premium-quality theme layer on top of `MkDocs`.

`mkdocstrings` injects code reference documentation from source objects into Markdown pages and supports multiple language handlers, including Python.

#### Supported Inputs And Outputs

Inputs:

- Markdown pages;
- Python modules through `mkdocstrings`;
- additional handlers are available for other languages, including shell and C.

Outputs:

- static HTML documentation site;
- the site can then be hosted anywhere or exported through external tooling.

#### Official References

- `MkDocs`: <https://www.mkdocs.org/>
- `Material for MkDocs`: <https://squidfunk.github.io/mkdocs-material/>
- `mkdocstrings`: <https://mkdocstrings.github.io/>
- `mkdocstrings` handlers: <https://mkdocstrings.github.io/usage/handlers/>
- `mkdocstrings` usage: <https://mkdocstrings.github.io/usage/>

#### Example / Look And Feel

The official documentation sites themselves are representative examples:

- `MkDocs` official site
- `Material for MkDocs` official site
- `mkdocstrings` official site

Those show the kind of navigation, search, tabbed content, admonitions, and code-reference rendering this stack can produce.

#### Pros

- best fit for a Markdown-first repository;
- very good default visual quality with `Material`;
- easy to combine hand-written guides and generated API pages;
- fast local preview with live reload;
- easy search experience;
- easy to automate in a single command;
- good long-term fit if the repository becomes a documentation portal, not just an API index.

#### Cons

- generated API docs are good, but less formal than a full Sphinx setup;
- some advanced cross-reference use-cases require configuration;
- API documentation quality still depends heavily on source docstrings;
- for very deep Python-library API trees, Sphinx can feel more native.

#### Automation Suitability

Very high.

This is one of the strongest candidates for a future command like:

- `update code documentation`

because the workflow can be reduced to:

- refresh API reference pages;
- build or serve the docs site;
- optionally validate links or build warnings.

#### Repository Fit

Excellent.

This is the most natural fit for the current repository shape.

### 2. Sphinx + autodoc + autosummary + apidoc

#### What It Is

`Sphinx` is the traditional documentation system used heavily in the Python ecosystem.

Its `autodoc` extension imports Python modules and reads docstrings.

Its `autosummary` extension generates summary tables and stub pages.

Its `apidoc` support generates source files for package documentation.

#### Supported Inputs And Outputs

Inputs:

- reStructuredText natively;
- Markdown with additional plugins;
- Python modules through `autodoc`.

Outputs:

- HTML;
- LaTeX and PDF-oriented paths;
- EPUB and other formats through the Sphinx builder ecosystem.

#### Official References

- `autodoc`: <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>
- `autosummary`: <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>
- `apidoc`: <https://www.sphinx-doc.org/en/master/usage/extensions/apidoc.html>
- automatic generation tutorial: <https://www.sphinx-doc.org/en/master/tutorial/automatic-doc-generation.html>

#### Example / Look And Feel

The official Sphinx documentation is itself an example of the ecosystem.

Many Python-library docs published on Read the Docs also follow this style.

The visual result is solid and familiar, though less modern by default than `Material for MkDocs`.

#### Pros

- mature and highly capable;
- strong Python-ecosystem standard;
- excellent cross-referencing model;
- good if the API reference is a first-class deliverable;
- large plugin ecosystem.

#### Cons

- heavier configuration burden;
- less natural than MkDocs for a Markdown-heavy repository;
- `autodoc` imports modules, so import side effects matter;
- can feel more mechanical for mixed guide-and-portal use cases.

#### Important Risk

The official `autodoc` and `apidoc` documentation explicitly warns that modules are imported during documentation generation, and import side effects will run.

That matters if this repository has scripts or modules that are not import-clean.

#### Automation Suitability

High, but slightly heavier than MkDocs.

A future `update code documentation` command is still realistic, but you need a cleaner and more disciplined documentation build pipeline.

#### Repository Fit

Good, but not optimal.

This is a strong technical choice if API reference becomes the primary goal.

### 3. Sphinx + AutoAPI

#### What It Is

`AutoAPI` is a Sphinx extension that generates API reference pages through analysis and Sphinx directives.

It is often used as a more automated alternative to hand-maintained `autodoc` trees.

#### Supported Inputs And Outputs

Inputs:

- Python source trees;
- Sphinx pages;
- manual narrative documentation.

Outputs:

- same Sphinx output families as standard Sphinx builds.

#### Official References

- `AutoAPI` directives: <https://sphinx-autoapi.readthedocs.io/en/latest/reference/directives.html>

#### Example / Look And Feel

The visual look depends mostly on Sphinx theme selection.

Functionally, it can provide a more automatically maintained API tree than plain `autodoc` alone.

#### Pros

- less manual API-page maintenance than plain `autodoc`;
- still lives in the strong Sphinx ecosystem;
- closer to a “generate the whole API tree” workflow.

#### Cons

- still carries Sphinx complexity;
- less natural than MkDocs for a docs portal centered on Markdown;
- may be overkill for the current amount of Python code.

#### Automation Suitability

High.

This is one of the better Sphinx-family options for a command like:

- `update code documentation`

because the API tree can be rebuilt more automatically.

#### Repository Fit

Good.

If you prefer the Sphinx ecosystem, this is stronger than plain `autodoc` alone for this repository.

### 4. Doxygen

#### What It Is

`Doxygen` is a long-established documentation generator, historically strongest in C and C++ but also supporting Python and other languages.

It parses code comments and can generate cross-linked documentation with diagrams and multiple output formats.

#### Supported Inputs And Outputs

Inputs:

- code comments in supported languages;
- Markdown files;
- configuration through `Doxyfile`.

Outputs:

- HTML;
- PDF through LaTeX;
- RTF;
- XML;
- additional downstream transformations are possible.

#### Official References

- overview: <https://www.doxygen.nl/manual/index.html>
- homepage / features: <https://www.doxygen.nl/>
- Markdown support: <https://www.doxygen.nl/manual/markdown.html>
- comment blocks: <https://www.doxygen.nl/manual/docblocks.html>
- output examples: <https://www.doxygen.nl/results.html>

#### Example / Look And Feel

The official output examples page lists real-world projects documented with Doxygen, such as:

- Eigen
- KDE API Reference
- Xerces-C++

Those examples are useful to understand the final navigation and API-page style.

#### Pros

- mature and battle-tested;
- multiple output formats;
- strong cross-reference support;
- good if the repository may later include more C/C++ or mixed-language code;
- familiar conceptually if you already think in terms of Doxygen comments.

#### Cons

- less natural than MkDocs or Sphinx for a Markdown-heavy Python-centric repository;
- default output feels more technical and less modern;
- Python support exists, but Doxygen is not the first-choice tool for modern Python doc portals;
- integration with the existing guide system would require more adaptation.

#### Automation Suitability

Good.

`Doxygen` is scriptable and could absolutely back a command like:

- `update code documentation`

but the generated experience would be more API-centric and less aligned with your current documentation ecosystem.

#### Repository Fit

Moderate.

Viable, but not the best fit for the current repository profile.

### 5. pdoc

#### What It Is

`pdoc` is a simpler Python API documentation generator with a strong focus on low setup overhead.

#### Supported Inputs And Outputs

Inputs:

- Python docstrings;
- Markdown-flavored documentation content inside docstrings.

Outputs:

- HTML pages;
- local web preview;
- custom templates.

#### Official References

- main docs: <https://pdoc.dev/docs/pdoc.html>
- math demo example output: <https://pdoc.dev/docs/math/math_demo.html>

#### Example / Look And Feel

The official `math_demo` page is a good example of the output style.

It is clean and readable, but intentionally minimal.

#### Pros

- extremely fast to start;
- low configuration burden;
- good for quick Python API sites;
- easy local preview.

#### Cons

- too limited for a full repository documentation portal;
- weaker fit for a repo with many Markdown guides and structured documentation families;
- best for API-only or small-project documentation.

#### Automation Suitability

Very high for API-only generation.

Lower for full repository documentation, because it is not really a guide portal system.

#### Repository Fit

Low to moderate.

Good as a quick experiment, not as the main long-term platform.

### 6. pydoctor

#### What It Is

`pydoctor` is a standalone Python API documentation generator based on static analysis.

Unlike `autodoc`, it is notable for not relying on importing modules in the normal runtime sense for its main API extraction model.

#### Supported Inputs And Outputs

Inputs:

- Python code;
- multiple documentation styles in docstrings.

Outputs:

- HTML API docs;
- publishable static output;
- Sphinx integration is also possible.

#### Official References

- introduction: <https://pydoctor.readthedocs.io/>
- quick start: <https://pydoctor.readthedocs.io/en/latest/quickstart.html>
- readme: <https://pydoctor.readthedocs.io/en/latest/readme.html>
- Read the Docs publishing example: <https://pydoctor.readthedocs.io/en/latest/publish-readthedocs.html>

#### Example / Look And Feel

The pydoctor documentation and quickstart pages show the expected style and publishing model.

The output is API-focused and functional rather than portal-oriented.

#### Pros

- static-analysis orientation is attractive for script-heavy repositories;
- strong support for Python-focused API extraction;
- supports multiple docstring formats;
- good if import side effects are a concern.

#### Cons

- not as broad a documentation-portal solution as MkDocs;
- smaller ecosystem than Sphinx;
- less natural if you want one integrated site for guides, usage docs, and code docs.

#### Automation Suitability

High for Python API generation.

Medium for full repository documentation unless paired with another site system.

#### Repository Fit

Moderate.

Potentially useful as a component, but probably not the top-level docs platform.

### 7. Doxygen + Sphinx/Breathe Hybrid

#### What It Is

This approach uses `Doxygen` for source extraction and XML generation, then feeds that into a Sphinx site through `Breathe`.

#### Supported Inputs And Outputs

Inputs:

- code comments through Doxygen;
- Sphinx narrative docs.

Outputs:

- Sphinx-generated site outputs.

#### Official References

- Doxygen helpers page referencing `Breathe`: <https://www.doxygen.nl/helpers.html>

#### Pros

- useful when a project has strong C/C++ needs plus a richer Sphinx site;
- separates code parsing from site rendering.

#### Cons

- too complex for the current repository;
- not a good first move here;
- adds a second layer of maintenance.

#### Automation Suitability

Good in expert setups, but unjustified for this repository now.

#### Repository Fit

Low.

This is only worth considering if the repository later becomes strongly mixed-language with serious non-Python API needs.

## Output And Format Comparison

### MkDocs Stack

Primary outputs:

- static HTML site

Strong native inputs:

- Markdown

Code reference path:

- `mkdocstrings` handlers

### Sphinx Stack

Primary outputs:

- HTML
- LaTeX/PDF-oriented paths
- EPUB and more

Strong native inputs:

- reStructuredText
- Markdown with plugins

Code reference path:

- `autodoc`, `autosummary`, `apidoc`, or `AutoAPI`

### Doxygen

Primary outputs:

- HTML
- PDF via LaTeX
- RTF
- XML

Strong native inputs:

- Doxygen-style code comments
- Markdown pages

Code reference path:

- built-in source analysis across supported languages

### pdoc

Primary outputs:

- HTML

Strong native inputs:

- Python docstrings

Code reference path:

- Python-first auto-generated API pages

### pydoctor

Primary outputs:

- HTML

Strong native inputs:

- Python source and docstrings

Code reference path:

- static-analysis-driven Python API docs

## Recommendation

### Best Overall Choice

`MkDocs + Material + mkdocstrings`

This is the best overall match for the repository because it combines:

- strong Markdown support;
- a high-quality navigable site;
- good Python API reference generation;
- a workflow that can absorb the existing `doc/` material cleanly.

### Strongest Traditional Alternative

`Sphinx + AutoAPI`

This is the best fallback if the priority becomes:

- formal API reference first;
- stronger Python-ecosystem conventions;
- deeper cross-reference control.

### Acceptable But Less Suitable Choice

`Doxygen`

It is viable and respected, but it is not the most natural foundation for this repository.

### Tools Better Treated As Secondary Experiments

- `pdoc`
- `pydoctor`

These are worth testing for API-only snapshots, but not as the main platform choice right now.

## Automation Recommendation

If the user wants to later say:

- `update code documentation`

the future workflow should be designed around three layers:

1. source discipline
   - docstrings and module comments in Python files;
2. site generation
   - one selected documentation platform;
3. automation wrapper
   - a repository script or command that rebuilds the documentation deterministically.

The most practical automation path is:

- choose a single site generator;
- define the source directories and exclusions clearly;
- make one command rebuild the API reference and the docs site;
- optionally add a CI check to ensure the docs build still succeeds.

For this repository, the cleanest future command would likely be backed by:

- `MkDocs + Material + mkdocstrings`

because it allows Codex to update:

- hand-written guide pages;
- generated code reference pages;
- navigation structure;
- site build output

through one coherent documentation system.

## Involved Components

- `scripts/`
  Primary Python source tree to be documented.
- `doc/`
  Existing repository documentation tree that should eventually connect to the documentation site.
- `config/`
  Workflow configuration material that may later deserve selected narrative documentation.
- Future candidate documentation platform files:
  - `mkdocs.yml`
  - or `docs/` / `conf.py` if a Sphinx route is chosen
- `readme.temp.md`
  Isolated handoff file that should record this evaluation for later synchronized integration.

## Implementation Steps

1. Keep this evaluation as a standalone isolated planning artifact for now.
2. Decide which documentation platform to test first.
3. If the user approves implementation, create a new technical project document for the actual documentation-platform setup task.
4. Re-check the synchronized repository state before adding any documentation-tool configuration.
5. Build a minimal proof of concept for the chosen platform on a limited subset of `scripts/`.
6. Evaluate the generated output quality and maintenance burden.
7. Only then roll the platform out to repository-wide code documentation.
