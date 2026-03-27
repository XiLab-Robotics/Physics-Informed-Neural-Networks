# Dual NotebookLM Video Package Strategy For Guides

## Overview

This document formalizes a new `NotebookLM` video-guide strategy for the
learning-guide tree under `doc/guide/`.

The user requested that each guide topic support two distinct video families:

- a neutral, model- or concept-centered educational video that explains what
  the topic is, how it works, the core principles behind it, the usual training
  and testing logic, and how it is used in practice outside this repository;
- a repository-specific explanatory video, similar to the current existing
  packages, that explains why the topic appears in this project, what role it
  plays in the TE workflow, and what its project-local advantages and
  disadvantages are.

The user also requested that:

- the repository prepare the source files that must be uploaded into
  `NotebookLM`;
- future imported `NotebookLM` exports be renamed so their filenames reflect
  their real content rather than generic names such as `Mind Map.png`,
  `Infographic.png`, or `Video Overview.mp4`;
- this dual-video workflow apply to all topics currently present under
  `doc/guide/`.

Current repository inspection shows that most guides already have one
repository-specific `video_guide_package/`, but the `Multilayer Perceptrons`
folder is an exception: it currently contains imported media files only and does
not yet contain the canonical guide Markdown/PDF pair or a guide-local
`video_guide_package/`.

## Technical Approach

### 1. Introduce Two Explicit Video-Source Tracks Per Guide

Each guide should expose two clearly separated `NotebookLM` source-package
tracks:

- `assets/concept_video_package/`
  neutral educational package focused on the general topic itself;
- `assets/project_video_package/`
  repository-specific package focused on the role of that topic inside this TE
  project.

This separation is better than trying to drive both outcomes from one mixed
package because the source-grounded `NotebookLM` workflow becomes easier to
control when:

- the neutral video is not polluted by repository status, roadmap, or TE
  implementation details;
- the repository-specific video is free to discuss tradeoffs, implementation
  choices, and project-local constraints directly.

### 2. Treat The Existing `video_guide_package/` As A Legacy Name To Retire

The current package name `video_guide_package/` is no longer precise enough once
two distinct video families are required.

The better long-term structure is:

- `doc/guide/<Guide Name>/assets/concept_video_package/`
- `doc/guide/<Guide Name>/assets/project_video_package/`

During the migration, existing package files should be reviewed and redistributed
into the correct new root rather than copied blindly.

For the guides that already have one package, the current package should be
treated as the starting point for the future `assets/project_video_package/`, because
its content is already repository-centered.

### 3. Standardize The Package File Set

Each package should contain a consistent, discoverable source set tailored for
`NotebookLM`.

#### Common Core Files For Both Package Types

- `video_source_brief.md`
- `video_terminology_sheet.md`
- `video_narration_outline.md`
- `video_figure_reference.md`

#### Conditional File

- `video_fact_boundary_notes.md`

This file is mandatory whenever the package contains implementation-status
boundaries, roadmap distinctions, repository capability claims, or scope limits
that the generated video must not overstate.

#### Additional Track-Specific File

To avoid mixing the framing of the two tracks, each package should also contain
one package-type note:

- `concept_video_scope_notes.md`
  for neutral package boundaries and pedagogical focus;
- `project_video_scope_notes.md`
  for repository role, intended comparison framing, and project-specific claims.

### 4. Define Different Content Responsibilities For The Two Tracks

#### Neutral `concept_video_package`

This package should explain:

- what the concept or model is;
- the operating principle;
- the usual structure or workflow;
- common training logic;
- common validation and testing logic;
- practical use cases;
- limitations and common failure modes;
- how to interpret the model or method at a general level.

It should avoid:

- repository roadmap details;
- TE-project status claims unless strictly needed as a short example;
- implementation-file walkthroughs unless the guide topic itself is explicitly a
  workflow concept such as `Training, Validation, And Testing`.

#### Repository-Specific `project_video_package`

This package should explain:

- why the topic exists in this repository;
- how it connects to TE modeling and comparison logic;
- what repository files, workflows, or reports implement it;
- why it was selected instead of simpler or more structured alternatives;
- project-local strengths, weaknesses, and current limitations;
- how the topic fits the broader repository roadmap.

### 5. Normalize Future NotebookLM Export Filenames

Imported or curated `NotebookLM` outputs should use filenames that describe both
their content type and their track.

Recommended naming pattern:

- `<Guide Name> - Concept Mind Map.png`
- `<Guide Name> - Concept Infographic.png`
- `<Guide Name> - Concept Slides.pdf`
- `<Guide Name> - Concept Slides.pptx`
- `<Guide Name> - Concept Supporting Brief.pdf`
- `<Guide Name> - Concept Video Overview.mp4`
- `<Guide Name> - Project Mind Map.png`
- `<Guide Name> - Project Infographic.png`
- `<Guide Name> - Project Slides.pdf`
- `<Guide Name> - Project Slides.pptx`
- `<Guide Name> - Project Supporting Brief.pdf`
- `<Guide Name> - Project Video Overview.mp4`

This naming rule preserves human readability while making the file purpose clear
without opening the media manually.

### 6. Apply The Strategy To Every Guide Topic Under `doc/guide/`

Current guide-topic roots are:

- `FeedForward Network`
- `Harmonic Regression`
- `Multilayer Perceptrons`
- `Neural Network Foundations`
- `Periodic Feature Network`
- `Residual Harmonic Network`
- `TE Model Curriculum`
- `Training, Validation, And Testing`

The intended rollout is repository-wide across all of them.

However, `Multilayer Perceptrons` is currently not aligned with the canonical
guide workflow because it lacks:

- a guide-local Markdown document;
- a guide-local PDF companion;
- a guide-local `assets/` folder;
- any current source package directory.

Therefore the implementation phase must either:

- first create the missing canonical guide baseline for `Multilayer
  Perceptrons`, or
- explicitly scope the first package-generation wave to the seven guides that
  already satisfy the current canonical guide prerequisites, then return to
  `Multilayer Perceptrons` as a follow-up.

The better repository direction is to normalize `Multilayer Perceptrons` into
the canonical guide structure so the full `doc/guide/` tree becomes consistent.

### 7. Keep NotebookLM Input Files Repository-Owned And Editable

The source files prepared for `NotebookLM` should remain Markdown-first and
repository-owned.

The repository should generate and maintain the package source documents, while
the user may later upload them into `NotebookLM` externally. When the user then
provides back the generated `NotebookLM` exports, those files can be renamed,
organized, and corrected in a second repository pass.

This preserves:

- version control over the intent and terminology;
- repeatability of later video generations;
- a clean workflow for post-generation cleanup of downloaded media.

## Involved Components

- `README.md`
  Main project document that must reference this technical planning note.
- `AGENTS.md`
  Repository workflow rules that currently describe a single
  `video_guide_package/` concept and will need to be updated after approval.
- `doc/guide/`
  Canonical learning-guide root that will receive the dual-package structure.
- Existing guide-local package folders such as:
  - `doc/guide/FeedForward Network/video_guide_package/`
  - `doc/guide/Harmonic Regression/video_guide_package/`
  - `doc/guide/Neural Network Foundations/video_guide_package/`
  - `doc/guide/Periodic Feature Network/video_guide_package/`
  - `doc/guide/Residual Harmonic Network/video_guide_package/`
  - `doc/guide/TE Model Curriculum/video_guide_package/`
  - `doc/guide/Training, Validation, And Testing/video_guide_package/`
- `doc/guide/Multilayer Perceptrons/`
  Outlier guide root that currently contains imported media but lacks the
  canonical guide/package baseline required by the proposed rollout.
- `doc/technical/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md`
  Existing rule document that established the current single-package workflow.

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before changing repository rules or creating
   any new package files.
3. Update the permanent workflow rules from one generic
   `video_guide_package/` model to the two-track `assets/concept_video_package/` and
   `assets/project_video_package/` model.
4. Define and document the standard file template for both package types.
5. Migrate the existing repository-specific package content from
   `video_guide_package/` into `assets/project_video_package/` for the already
   canonical guides.
6. Generate the new neutral `assets/concept_video_package/` source files for the same
   guides.
7. Normalize the asset and export naming convention for downloaded `NotebookLM`
   outputs so filenames explicitly declare guide name, track, and artifact type.
8. Resolve the `Multilayer Perceptrons` outlier by creating its missing
   canonical guide baseline or by formally deferring it in a tightly scoped
   follow-up if the user prefers a staged rollout.
9. After the user uploads generated `NotebookLM` exports back into the
   repository, run a separate cleanup/integration pass to rename, place, and fix
   the resulting media files consistently.
