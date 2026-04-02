# Learning Guide PDF Exports And Post-Image-Approval Rule

## Overview

This document defines the requested follow-up work for the newly created `learning_guides`.

The user requested two related changes:

- generate PDF exports for the learning-guide reports that currently exist only as Markdown;
- add a persistent workflow rule stating that learning-guide PDFs must be created only after the user has explicitly approved the generated images, because figure layouts often need one or more correction passes.

This is not only a document-export task.

It also changes the repository workflow for a specific documentation family, so the rule must be written clearly and in a location that future repository work will actually follow.

## Technical Approach

### Scope Of The Export Task

The immediate export scope is the current learning-guide set under:

- `doc/reports/analysis/learning_guides/Neural Network Foundations/`
- `doc/reports/analysis/learning_guides/Training, Validation, And Testing/`
- `doc/reports/analysis/learning_guides/TE Model Curriculum/`

Each guide should eventually exist in both:

- Markdown form for repository reading and future editing;
- PDF form for polished distribution and consolidated study use.

### Required Export Behavior

The export path should follow the same discipline already used elsewhere in the repository for styled PDF generation:

1. confirm that the guide-local images are visually approved by the user;
2. generate or regenerate the PDF output;
3. validate the real exported PDF, not only the HTML or source Markdown;
4. confirm that page margins, image scaling, and text blocks remain balanced and readable.

The user explicitly asked that image approval happen before the PDF is generated or finalized.

That means the learning-guide workflow must not treat:

- Markdown complete;
- images generated;
- PDF exported

as a single automatic one-pass action.

Instead, it must preserve an explicit checkpoint:

`images generated -> user approval -> PDF export -> PDF validation`

### Rule To Add

The new persistent rule should say, in substance:

- when a new `learning_guide` is created, a PDF companion is also required;
- however, the PDF generation step must happen only after the user has explicitly approved the generated images for that guide;
- if the images need corrections, the guide remains open and the PDF export is deferred until those visual defects are resolved.

This rule is narrower than the broader model-report diagram rule already present in the repository.

It applies specifically to the `learning_guides` family because those guides are didactic and image-heavy, and the user wants an explicit approval gate for figures.

### Documentation Targets For The Rule

The rule should be written into the repository guidance where future work will naturally consult it.

Likely targets after approval:

- `AGENTS.md`
  to make the workflow rule explicit for future repository tasks;
- possibly the relevant technical planning note for the learning-guide family if a cross-reference improves traceability.

### Expected Deliverables After Approval

After user approval of this technical document, the implementation phase should produce:

- one PDF for each current learning guide;
- README index updates so the new PDFs are discoverable;
- the new explicit repository rule for post-image-approval PDF export;
- PDF-validation evidence or at least a validated manual check of the real exported files.

### Validation Requirements

The validation pass should check:

- no figure is clipped;
- no label touches or crosses its box boundary;
- diagrams remain readable at PDF scale;
- page breaks do not split major figure-caption or section-introduction pairs in a distracting way;
- margins stay consistent with the repository's restrained analytical PDF style.

Although these learning guides are not campaign reports, their PDFs should still follow the established project expectations for clean and readable exports.

## Involved Components

- `README.md`
  Main project document that must reference this technical planning note.
- `doc/README.md`
  Internal documentation index that should also reference this technical planning note.
- `AGENTS.md`
  Repository workflow rules that should receive the new learning-guide PDF rule after approval.
- `doc/technical/2026-03/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md`
  Original planning note for the learning-guide family.
- `doc/reports/analysis/learning_guides/`
  Current Markdown learning-guide outputs that need PDF companions.
- Existing report-export pipeline components under:
  - `scripts/reports/`
  - `doc/scripts/reports/`

## Implementation Steps

1. Create this technical planning document and register it in `README.md` and `doc/README.md`.
2. Wait for explicit user approval before generating any learning-guide PDFs or changing permanent workflow rules.
3. Confirm that the current guide-local images are approved by the user.
4. Export PDF companions for each current learning guide.
5. Validate the real exported PDFs for figure fit, margins, and readability.
6. Add the explicit repository rule that learning-guide PDFs are required, but only after user approval of the generated images.
7. Update the documentation indexes so the Markdown and PDF versions are both discoverable.
