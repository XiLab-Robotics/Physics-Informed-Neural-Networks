# Guide And Model Reference Documentation Reorganization

## Overview

This document proposes a repository documentation reorganization focused on the current split between:

- `doc/reports/analysis/model_explanatory/`
- `doc/guide/`

The current structure reflects two partially different intents:

- model-specific explanatory reports stored under the analysis-report area;
- learning guides and user-facing educational material stored under the guide area.

In practice, the implemented model families currently appear in both places with substantial topical overlap. This makes the documentation harder to browse and raises a maintenance cost because model concepts are repeated in parallel documents.

The goal of this pass is to evaluate and, if approved, implement a clearer canonical structure where the repository-facing educational and reference material lives under a single discoverable documentation root while preserving the semantic distinction between:

- teaching-oriented learning guides;
- technical model-reference material;
- operational usage guidance.

## Technical Approach

### 1. Keep The Semantic Distinction But Unify The Root

The proposed direction is not to flatten all documents into one undifferentiated folder. Instead, the root should be unified under `doc/guide/`, with explicit subcategories that preserve the documentation purpose.

The proposed canonical structure is:

- `doc/guide/project_usage_guide.md`
- `doc/guide/learning/<Guide Name>/`
- `doc/guide/model_reference/<Model Name>/`

This keeps all human-facing guidance and reference content under one stable root while avoiding the current semantic mismatch where permanent model-reference documents live under `doc/reports/analysis/`.

### 2. Treat `project_usage_guide.md` As A Separate Operational Surface

`doc/guide/project_usage_guide.md` should remain a dedicated operational guide and should not be merged into the model-reference or learning-guide families.

Its function is different:

- runnable workflow reference;
- repository usage guidance;
- command and configuration orientation.

This file should remain a top-level guide entry point.

### 3. Preserve Both Learning And Reference Layers

The repository already treats learning guides and explanatory reports as different document classes.

That distinction should remain explicit:

- `learning`
  for beginner-to-university teaching material, curriculum-style explanations, slide packages, infographics, and `video_guide_package/` assets;
- `model_reference`
  for technical model explanations, architectural and conceptual diagrams, implementation mapping, and training-workflow explanations specific to one model family.

This avoids losing the higher technical density of the existing model explanatory reports while still consolidating the browsing experience.

### 4. Reduce Duplication Across The Four Implemented Model Families

The currently implemented overlap is strongest for:

- `FeedForward Network`
- `Harmonic Regression`
- `Periodic Feature Network`
- `Residual Harmonic Network`

For these four families, the approved implementation should define one canonical content hierarchy rather than keeping two near-duplicate long-form documents without a clear precedence.

The preferred consolidation direction is:

- keep a full technical reference document under `doc/guide/model_reference/<Model Name>/`;
- keep a learning-oriented guide under `doc/guide/learning/<Guide Name>/` only when it adds clear pedagogical value;
- where overlap is too strong, shorten the learning guide and make it explicitly bridge to the technical reference instead of repeating the same full explanation.

### 5. Migrate Links And Media References Carefully

The reorganization should update all active references that point to the current `doc/reports/analysis/model_explanatory/` paths, especially:

- `README.md`
- `doc/README.md`
- `doc/guide/TE Model Curriculum/TE Model Curriculum.md`
- any learning guides that cross-link to the current model-explanatory reports
- report or documentation tooling that assumes the old paths

The report-local assets should move with their canonical document family so relative image links remain stable and discoverable.

### 6. Avoid Mixing Permanent Reference Pages With Analytical One-Off Reports

The approved implementation should preserve a clear distinction between:

- permanent reference documentation;
- one-off analytical studies;
- campaign reports;
- campaign plans.

This means the move to `doc/guide/` should apply only to the permanent model explanatory material, not to the broader contents of `doc/reports/analysis/`.

## Involved Components

- `doc/reports/analysis/model_explanatory/`
- `doc/guide/`
- `doc/guide/project_usage_guide.md`
- `doc/guide/TE Model Curriculum/TE Model Curriculum.md`
- `README.md`
- `doc/README.md`
- any active documentation tooling or report scripts that still reference `doc/reports/analysis/model_explanatory/`

## Implementation Steps

1. Confirm the target canonical structure under `doc/guide/`.
2. Decide which current model-family documents remain as full learning guides and which should become lighter bridge documents.
3. Move the permanent model explanatory report folders from `doc/reports/analysis/model_explanatory/` into the approved substructure under `doc/guide/`.
4. Move or normalize the associated per-model assets so each canonical document keeps its diagrams locally.
5. Update cross-links in `README.md`, `doc/README.md`, `doc/guide/TE Model Curriculum/TE Model Curriculum.md`, and other active guide pages.
6. Review the four implemented model families for duplicated long-form content and reduce redundancy where appropriate.
7. Validate that no permanent reference links still point to obsolete `doc/reports/analysis/model_explanatory/` paths unless intentionally kept as historical references.
