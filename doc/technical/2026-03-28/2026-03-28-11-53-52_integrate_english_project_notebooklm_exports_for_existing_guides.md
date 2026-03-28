# Integrate English Project NotebookLM Exports For Existing Guides

## Overview

The repository already contains guide-local bilingual media folders under
`doc/guide/<Guide Name>/English/` and `doc/guide/<Guide Name>/Italiano/`.

For the eight guides:

- `FeedForward Network`
- `Harmonic Regression`
- `Multilayer Perceptrons`
- `Neural Network Foundations`
- `Periodic Feature Network`
- `Residual Harmonic Network`
- `TE Model Curriculum`
- `Training, Validation, And Testing`

the current `English/` folders only contain the concept-track media derived
from `assets/concept_video_package/`.

The user added new `.temp/<Guide Name>/` folders containing the English
equivalents of the media generated from `assets/project_video_package/`,
excluding the mind map. These exports now need to be integrated into the
canonical repository guide tree.

No subagent is planned for this task. The file mapping, naming normalization,
and Markdown QA are small enough to be handled directly in the main session.

## Technical Approach

Keep the current language-aware guide structure unchanged:

- `doc/guide/<Guide Name>/English/`
- `doc/guide/<Guide Name>/Italiano/`

The approved integration should populate the missing English project-track
artifacts directly under each existing `English/` folder.

Each temporary source file from `.temp/<Guide Name>/` should be renamed to the
repository-owned explicit naming convention already used for the concept-track
English exports and the Italian project-track exports:

- `<Guide Name> - Project Infographic.png`
- `<Guide Name> - Project Slides.pdf`
- `<Guide Name> - Project Slides.pptx`
- `<Guide Name> - Project Supporting Brief.pdf`
- `<Guide Name> - Project Video Overview.mp4`

This keeps the repository consistent with the established guide-local language
split while avoiding a second structural migration.

The task is documentation/media integration only. No Python implementation,
training workflow, or dependency changes are expected.

## Involved Components

- `.temp/<Guide Name>/`
  Temporary source folders for the new English project-track exports.
- `doc/guide/<Guide Name>/English/`
  Canonical target folders that currently miss the project-track English media.
- `README.md`
  Main project document that must reference this technical note.
- touched guide-local Markdown files, if discoverability notes need updating
  after approval.

## Implementation Steps

1. Create this technical planning document and register it from `README.md`.
2. Wait for explicit user approval before integrating any `.temp` media into the
   canonical guide folders.
3. After approval, inspect the five source artifacts in each `.temp/<Guide
   Name>/` folder and map them to the canonical project-track filenames.
4. Copy the English project exports into `doc/guide/<Guide Name>/English/`
   without altering the existing Italian deliverables or the already integrated
   English concept deliverables.
5. Normalize any temporary generic names such as `unnamed.png` into the
   explicit repository-owned naming scheme.
6. Update any guide-local discoverability notes only if needed to keep the new
   English project exports easy to find.
7. Run Markdown warning checks on the touched Markdown files and confirm they
   end with a normal single final newline before closing the task.
