# English Subfolder Layout For Guide Exports

## Overview

The repository currently treats each topic root under `doc/guide/<Guide Name>/`
as the canonical home of:

- the authored guide Markdown and PDF;
- guide-local assets;
- `concept_video_package/`;
- `project_video_package/`;
- already integrated Italian `NotebookLM` exports.

The user added new `.temp/<Guide Name>/` folders containing English equivalents
of the concept-video exports generated from `concept_video_package/`, excluding
the mind map.

The user explicitly rejected:

- `localized/italian/...`
- `localized/english/...`
- separate top-level guide trees by language

and requested a simpler structure where Italian remains the default root and
English lives in a direct `English/` subfolder under each guide root, without
further `concept/` or `project/` subdivision.

## Technical Approach

The guide root should remain the Italian/default topic root.

The approved target pattern is:

- `doc/guide/<Guide Name>/`
  canonical Italian guide root
- `doc/guide/<Guide Name>/English/`
  English export companion folder for the same topic

Under this approach:

- the current Italian guide files and current Italian exports remain at the
  guide root;
- English `NotebookLM` exports are imported under `English/`;
- no `localized/` naming is introduced;
- no duplicated top-level guide tree is introduced;
- no extra `concept/` or `project/` subfolders are introduced inside
  `English/`.

This matches the user preference that:

- Italian is the default repository language for the guide roots;
- English is an explicit secondary export surface;
- filenames already carry enough topic-specific meaning that extra track
  subfolders are not required for this integration pass.

For the current scope, the imported English files should be renamed into stable
repository-owned names that fit the existing guide style and avoid temporary
NotebookLM names such as:

- `unnamed.png`
- `FeedForward_Baseline.pdf`
- `The_FeedForward_Network.mp4`

The imported English files should instead become guide-local English artifacts
with explicit filenames that declare at least:

- guide name;
- language (`English`);
- artifact role.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/guide/<Guide Name>/`
  Existing canonical guide roots that remain Italian/default.
- `doc/guide/<Guide Name>/English/`
  New per-guide English export folders to be created after approval.
- `.temp/<Guide Name>/`
  Temporary source location of the English concept exports.

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before reorganizing any guide-local export
   files.
3. After approval, create `English/` under each approved guide root.
4. Import the English exports from `.temp/<Guide Name>/` into the corresponding
   `doc/guide/<Guide Name>/English/` folder.
5. Rename the imported files to stable repository-owned filenames that preserve
   the guide name and clearly mark them as English artifacts.
6. Update the relevant guide documentation references so the English companion
   exports are discoverable.
7. Run Markdown checks on the touched Markdown files before closing the task.
