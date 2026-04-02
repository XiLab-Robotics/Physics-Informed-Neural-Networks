# Integrate Italian Project NotebookLM Exports For Multilayer Perceptrons

## Overview

The guide root `doc/guide/Multilayer Perceptrons/` already uses the established
language-aware export layout:

- `English/`
- `Italiano/`

At the moment, `doc/guide/Multilayer Perceptrons/Italiano/` contains only the
Italian concept-track exports.

The user added a new `.temp/Multilayer Perceptrons/` folder containing the
Italian media generated from `assets/project_video_package/`. Unlike the recent
English import pass, this temporary folder includes the full project-track set,
including the mind map.

These project-track Italian exports now need to be integrated into the
canonical `Italiano/` folder for the `Multilayer Perceptrons` guide.

No subagent is planned for this task. The scope is a small guide-local media
integration with direct filename normalization and Markdown QA.

## Technical Approach

Keep the current guide-local language split unchanged and populate the missing
Italian project-track artifacts directly under:

- `doc/guide/Multilayer Perceptrons/Italiano/`

Rename the temporary source files from `.temp/Multilayer Perceptrons/` to the
repository-owned canonical naming convention already used by the other Italian
guide folders:

- `Multilayer Perceptrons - Project Infographic.png`
- `Multilayer Perceptrons - Project Mind Map.png`
- `Multilayer Perceptrons - Project Slides.pdf`
- `Multilayer Perceptrons - Project Slides.pptx`
- `Multilayer Perceptrons - Project Supporting Brief.pdf`
- `Multilayer Perceptrons - Project Video Overview.mp4`

This keeps the `Multilayer Perceptrons` guide aligned with the rest of the
repository, where `Italiano/` stores both concept-track and project-track
NotebookLM exports.

The task is documentation/media integration only. No code, dependency, or
training workflow change is expected.

## Involved Components

- `.temp/Multilayer Perceptrons/`
  Temporary source folder for the new Italian project-track exports.
- `doc/guide/Multilayer Perceptrons/Italiano/`
  Canonical target folder that currently lacks the project-track Italian media.
- `README.md`
  Main project document that must reference this technical note.

## Implementation Steps

1. Create this technical planning document and register it from `README.md`.
2. Wait for explicit user approval before integrating any `.temp` media into
   the canonical guide folder.
3. After approval, inspect the six source artifacts in
   `.temp/Multilayer Perceptrons/` and map them to the canonical project-track
   filenames.
4. Copy the Italian project exports into
   `doc/guide/Multilayer Perceptrons/Italiano/` without altering the already
   integrated concept-track Italian exports.
5. Normalize temporary generic names such as `unnamed.png` and
   `NotebookLM Mind Map.png` into the explicit repository-owned naming scheme.
6. Run Markdown warning checks on the touched Markdown files and confirm they
   end with a normal single final newline before closing the task.
