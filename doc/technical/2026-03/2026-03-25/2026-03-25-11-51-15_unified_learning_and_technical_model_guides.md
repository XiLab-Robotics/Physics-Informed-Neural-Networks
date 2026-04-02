# Unified Learning And Technical Model Guides

## Overview

This document proposes the unification of the currently duplicated per-model documentation under:

- `doc/guide/<Model Name>/<Model Name>.md`
- `doc/guide/model_reference/<Model Name>/<Model Name>.md`

The current split preserves two useful perspectives:

- a learning-oriented guide written for broader conceptual understanding;
- a technical model-reference document written for implementation-aware reading.

However, both documents now overlap heavily for the implemented model families, which increases maintenance cost and creates parallel explanations of the same architecture.

The goal of this pass is to create one canonical per-model guide that integrates both dimensions:

- an explanation-oriented section for learning and conceptual understanding;
- a technical section for repository implementation, training flow, and code mapping.

The same unification pattern should be applied across the implemented model families, starting from `FeedForward Network` and then extending to the other currently documented models.

## Technical Approach

### 1. Keep `doc/guide/<Model Name>/` As The Canonical Home

The final documentation direction already favors `doc/guide/<Model Name>/` as the surviving guide family.

Therefore, the unified model document should live at:

- `doc/guide/<Model Name>/<Model Name>.md`

The former `doc/guide/model_reference/<Model Name>/<Model Name>.md` should no longer remain a parallel long-form canonical page once the content is merged.

### 2. Structure Each Unified Guide In Two Explicit Layers

Each unified guide should remain one document, but internally it should keep the two currently useful reading modes visible.

The preferred structure is:

- an introductory and conceptual learning-oriented layer;
- a later technical-reference layer.

For example, a unified model guide can include sections such as:

- `Overview`
- `Model Description`
- `Operating Principle`
- `Conceptual Map`
- `Architecture Diagram`
- `Why This Model Exists`
- `Advantages`
- `Disadvantages`
- `Expected Behavior In The TE Context`
- `Repository Implementation`
- `Training Workflow`
- `Training Logic In This Repository`
- `Summary`

This preserves the pedagogical readability of the learning guide while retaining the technical density of the model-reference report.

### 3. Preserve Existing Diagrams And Regenerate The PDF Companion

The unified Markdown guide should continue to use the guide-local canonical SVG assets under:

- `doc/guide/<Model Name>/assets/`

Once the Markdown content is unified, the corresponding PDF companion in the same folder must be regenerated so the canonical guide and its PDF remain aligned.

This applies to each affected model family.

### 4. Retire Parallel `model_reference` Markdown Pages Gradually

After a unified guide is created and validated for a given model family, the old parallel Markdown page under:

- `doc/guide/model_reference/<Model Name>/<Model Name>.md`

should no longer remain an independently maintained long-form source of truth.

The safer migration order is:

1. merge the content into the guide-local canonical Markdown;
2. regenerate and validate the guide-local PDF;
3. update active links if they still point to the old model-reference Markdown;
4. only then decide whether to remove or archive the old model-reference Markdown and PDF.

### 5. Apply The Same Pattern Across The Implemented Model Families

The same unification pattern should be applied to:

- `FeedForward Network`
- `Harmonic Regression`
- `Periodic Feature Network`
- `Residual Harmonic Network`

The wording and balance may vary slightly by model, but the structure should stay consistent so the documentation family remains easy to browse.

## Involved Components

- `doc/guide/FeedForward Network/`
- `doc/guide/Harmonic Regression/`
- `doc/guide/Periodic Feature Network/`
- `doc/guide/Residual Harmonic Network/`
- `doc/guide/model_reference/`
- `doc/guide/TE Model Curriculum/TE Model Curriculum.md`
- `README.md`
- `doc/README.md`

Potentially affected PDF-generation tooling or guide indexes:

- any guide-local PDF export workflow used for the model guides

## Implementation Steps

1. Define the unified section structure that combines learning-oriented explanation and technical reference content.
2. Merge the current `FeedForward Network` learning guide and model-reference Markdown into one canonical guide under `doc/guide/FeedForward Network/`.
3. Regenerate and validate the corresponding `FeedForward Network.pdf`.
4. Apply the same merge pattern to `Harmonic Regression`, `Periodic Feature Network`, and `Residual Harmonic Network`.
5. Regenerate and validate the PDF companion for each unified guide.
6. Update active repository links that should now point only to the unified guide-local canonical pages.
7. Review whether the old `model_reference` Markdown/PDF pairs can be retired or should remain temporarily as migration residue pending a later cleanup pass.
