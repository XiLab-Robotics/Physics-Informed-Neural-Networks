# Project-Status Presentation PPTX And Slide PDF Pipeline

## Overview

This task adds a first-class repository-owned export path for the existing
English project-status presentation so that the current Markdown slide deck can
also be delivered as:

- a real `.pptx` presentation file;
- a slide PDF export generated from that `.pptx`.

The immediate target is the already authored project-status deck under
`doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/`. The work
should establish a reusable local presentation pipeline rather than producing a
one-off manual export.

## Technical Approach

The repository already owns the presentation content as Markdown, but it does
not yet expose a native slide-export pipeline. The current environment also
does not provide a Python slide library by default, while PowerPoint COM is
available on this Windows machine.

The implementation should therefore use a two-stage pipeline:

1. Parse the repository-owned Markdown slide deck into an intermediate
   presentation structure.
2. Generate a `.pptx` file from that structure with `python-pptx`.
3. Export the generated `.pptx` to slide PDF through Microsoft PowerPoint COM.
4. Validate the real exported slide PDF and register the new artifacts in the
   repository documentation indexes.

This keeps the authored source in Markdown while still producing the two real
presentation deliverables requested by the user.

### Presentation Scope For The First Pipeline Pass

The current deck is intentionally simple:

- one title slide;
- multiple content slides;
- slide boundaries expressed with `---`;
- compact bullets and one simple table.

The first implementation should support this current scope cleanly instead of
over-generalizing immediately. In practice, the parser and renderer should
cover:

- H1 title slide handling;
- H2 content-slide titles;
- bullet lists;
- short paragraphs;
- basic Markdown tables;
- slide separators.

If a later presentation needs richer constructs, that can extend the same
pipeline.

### Environment And Dependency Strategy

The environment check shows:

- `python-pptx` is not currently declared in `requirements.txt`;
- PowerPoint COM is available locally;
- a direct PowerShell-based export path to PDF is therefore realistic.

The task should add the missing third-party dependency needed for `.pptx`
generation:

- `python-pptx`

The export-to-PDF stage should avoid adding a separate Python COM dependency
unless it proves necessary. A repository-owned PowerShell or Python-invoked
PowerShell export step is sufficient and reduces dependency churn.

### Output And Naming

The new outputs should live next to the current presentation source so the
bundle remains discoverable:

- Markdown source:
  `doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/2026-03-27-18-13-19_project_status_presentation_english.md`
- `.pptx` export:
  `doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/2026-03-27-18-13-19_project_status_presentation_english.pptx`
- slide PDF export:
  `doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/2026-03-27-18-13-19_project_status_presentation_english.pdf`

The documentation index under `doc/README.md` should be updated so all three
artifacts are discoverable together.

### Validation Strategy

This task is not complete when the `.pptx` file exists. The real deliverables
must be checked.

Validation should include:

- successful `.pptx` generation;
- successful slide PDF export;
- existence and non-trivial file size of both artifacts;
- PDF page-count sanity check against the authored slide count;
- visual sanity sampling to catch obvious clipping, crushed tables, or broken
  slide flow.

The PDF validation can be lighter than the styled analytical report workflow,
but it still must check the actual exported PDF rather than only the Markdown
or the `.pptx` source.

### Planned Subagent Usage

Planned subagent use during implementation:

- none required.

This task is implementation-heavy but self-contained. It does not currently
benefit from runtime delegation.

## Involved Components

- `README.md`
- `doc/README.md`
- `requirements.txt`
- `scripts/reports/`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/`
- `doc/technical/2026-03/2026-03-27/2026-03-27-19-38-55_project_status_presentation_pptx_and_slide_pdf_pipeline.md`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before implementing the presentation
   pipeline.
3. Add the required dependency for repository-owned `.pptx` generation.
4. Implement a presentation-generation script under `scripts/reports/` that
   parses the current Markdown slide deck and writes a `.pptx` file.
5. Implement or wire an export step that uses PowerPoint COM to convert the
   generated `.pptx` into a slide PDF.
6. Generate the `.pptx` and PDF artifacts for the current project-status deck.
7. Update `doc/README.md` so the new presentation outputs are indexed.
8. Run scoped Markdown checks on touched repository-owned Markdown files and
   confirm correct final newline state.
9. Report completion and wait for explicit commit approval.
