# Move Guide Video Packages Under Assets

## Overview

The current guide roots under `doc/guide/<Guide Name>/` store the package
folders:

- `assets/concept_video_package/`
- `assets/project_video_package/`

directly at the topic-root level.

The user requested a structural cleanup so that, for each guide folder in
`doc/guide/`, both package folders are moved under the existing `assets/`
directory.

This affects the current guide tree:

- `FeedForward Network`
- `Harmonic Regression`
- `Multilayer Perceptrons`
- `Neural Network Foundations`
- `Periodic Feature Network`
- `Residual Harmonic Network`
- `TE Model Curriculum`
- `Training, Validation, And Testing`

## Technical Approach

The intended target layout per guide is:

- `doc/guide/<Guide Name>/assets/concept_video_package/`
- `doc/guide/<Guide Name>/assets/project_video_package/`

This change is a repository-structure cleanup. It does not alter the prompt
contents or the export artifacts themselves, but it does change the canonical
paths of the two package folders.

That means the migration must include:

- moving the directories;
- updating any repository-owned Markdown references that still point to the old
  root-level package paths;
- checking the touched Markdown files for warning regressions after the path
  updates.

Because `Multilayer Perceptrons` currently does not have an `assets/` folder,
the migration must create it before moving the package folders there.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/guide/<Guide Name>/assets/`
  Existing or newly created asset roots that will hold the package folders.
- `doc/guide/<Guide Name>/assets/concept_video_package/`
  Current source location of the concept package folder.
- `doc/guide/<Guide Name>/assets/project_video_package/`
  Current source location of the project package folder.
- touched guide Markdown files and package-local README/prompt files
  Any files that reference the old package paths and need path updates.

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before moving any guide-local package
   folders.
3. Create missing `assets/` directories where required.
4. Move each `assets/concept_video_package/` and `assets/project_video_package/` folder under
   the corresponding `assets/` directory.
5. Update repository-owned references that still point to the old root-level
   package paths.
6. Run Markdown checks on the touched Markdown files before closing the task.
