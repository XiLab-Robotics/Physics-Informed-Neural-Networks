# Archive Concept NotebookLM Video Prompts Into Guide-Local Packages

## Overview

The repository already contains:

- technical notes about the concept-video command archive;
- newly created guide-local `project_video_package/notebooklm_project_video_prompt.md`
  files across the current guide tree.

What is still missing is the guide-local counterpart for the neutral concept
track. The user explicitly requested that the `concept_video_package` prompt
files also be archived inside each guide folder so the two NotebookLM package
tracks remain structurally symmetric.

The intended scope of this task is the same current guide tree under
`doc/guide/`:

- `Neural Network Foundations`
- `Multilayer Perceptrons`
- `FeedForward Network`
- `Harmonic Regression`
- `Periodic Feature Network`
- `Residual Harmonic Network`
- `TE Model Curriculum`
- `Training, Validation, And Testing`

## Technical Approach

This task concerns the neutral concept-video track, not the repository-centered
project-video track.

The new prompt files should therefore:

- stay aligned with the existing `concept_video_package/` materials;
- preserve the ready-to-paste NotebookLM command style already documented in
  the repository;
- remain neutral and educational rather than repository-centered;
- be stored directly inside each guide-local `concept_video_package/`.

The archived prompt files should use the established filename:

- `concept_video_package/notebooklm_concept_video_prompt.md`

Where existing repository documentation already records canonical concept-video
command wording, that prior archive should be treated as the wording reference.
Where needed, the guide-local prompt should preserve the same operational
structure used for the new project-video prompt files while keeping the concept
track's neutral instructional intent.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/guide/Neural Network Foundations/concept_video_package/`
  Target package root for the foundations concept prompt archive.
- `doc/guide/Multilayer Perceptrons/concept_video_package/`
  Target package root for the bridge-topic concept prompt archive.
- `doc/guide/FeedForward Network/concept_video_package/`
  Target package root for the feedforward concept prompt archive.
- `doc/guide/Harmonic Regression/concept_video_package/`
  Target package root for the harmonic concept prompt archive.
- `doc/guide/Periodic Feature Network/concept_video_package/`
  Target package root for the periodic-feature concept prompt archive.
- `doc/guide/Residual Harmonic Network/concept_video_package/`
  Target package root for the residual-harmonic concept prompt archive.
- `doc/guide/TE Model Curriculum/concept_video_package/`
  Target package root for the curriculum concept prompt archive.
- `doc/guide/Training, Validation, And Testing/concept_video_package/`
  Target package root for the workflow concept prompt archive.

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before writing any guide-local concept
   prompt files.
3. Add one repository-owned `notebooklm_concept_video_prompt.md` file under the
   `concept_video_package/` folder of each current guide root.
4. Keep each prompt aligned with the corresponding concept-package source
   documents and with the previously archived concept-command wording.
5. Run Markdown checks on the touched Markdown files and fix straightforward
   local warning regressions before closing the task.
