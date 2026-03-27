# Archive Project NotebookLM Video Prompts For All Guides

## Overview

The repository already stores guide-local `concept_video_package/` and
`project_video_package/` folders for the current `doc/guide/` topic roots.

The user requested that the repository also archive the final ready-to-paste
`NotebookLM` command text for the repository-specific video track in the same
practical style already used elsewhere, and to do so as-is for each guide
folder rather than keeping the prompts only in conversational history.

The intended scope of this task is the current guide tree under `doc/guide/`:

- `Neural Network Foundations`
- `Multilayer Perceptrons`
- `FeedForward Network`
- `Harmonic Regression`
- `Periodic Feature Network`
- `Residual Harmonic Network`
- `TE Model Curriculum`
- `Training, Validation, And Testing`

## Technical Approach

The project already distinguishes between:

- neutral concept-video prompts for `concept_video_package/`;
- repository-centered prompts for `project_video_package/`.

This request concerns the repository-centered project-video track. The prompt
text should therefore remain aligned with the existing package documents,
especially:

- `video_source_brief.md`
- `video_narration_outline.md`
- `video_terminology_sheet.md`
- `video_figure_reference.md`
- `video_fact_boundary_notes.md`
- `project_video_scope_notes.md`

The archived prompt files should be written directly under each
`project_video_package/` as a stable repository-owned Markdown artifact using
the established filename:

- `project_video_package/notebooklm_project_video_prompt.md`

The content should remain ready to paste into `NotebookLM`, should preserve the
user's preferred structure (`Goal`, `Requirements`, and `Desired output
style`), and should stay explicitly repository-centered instead of collapsing
back into a neutral concept-style explanation.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/guide/Neural Network Foundations/project_video_package/`
  Target package root for the foundations prompt archive.
- `doc/guide/Multilayer Perceptrons/project_video_package/`
  Target package root for the bridge-topic prompt archive.
- `doc/guide/FeedForward Network/project_video_package/`
  Target package root for the feedforward baseline prompt archive.
- `doc/guide/Harmonic Regression/project_video_package/`
  Target package root for the harmonic baseline prompt archive.
- `doc/guide/Periodic Feature Network/project_video_package/`
  Target package root for the periodic-feature baseline prompt archive.
- `doc/guide/Residual Harmonic Network/project_video_package/`
  Target package root for the residual-harmonic prompt archive.
- `doc/guide/TE Model Curriculum/project_video_package/`
  Target package root for the TE-curriculum prompt archive.
- `doc/guide/Training, Validation, And Testing/project_video_package/`
  Target package root for the workflow-discipline prompt archive.

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before writing any guide-local prompt files.
3. Add one repository-owned `notebooklm_project_video_prompt.md` file under the
   `project_video_package/` folder of each current guide root.
4. Keep each prompt aligned with the corresponding project-package source
   documents and project-local scope boundaries.
5. Run Markdown checks on the touched Markdown files and fix straightforward
   local warning regressions before closing the task.
