# Realign Project Status NotebookLM Documentation To notebook_lm_assets Layout

## Overview

The project-status report bundle under
`doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/` was recently
reorganized manually.

The real current filesystem state now differs from the documentation written in
the earlier integration note
`2026-03-28-12-06-26_integrate_notebooklm_project_status_presentation_and_video_exports.md`:

- the former `notebooklm/` folder was renamed to `notebook_lm_assets/`;
- the three generated NotebookLM output files were moved out of that folder and
  now live directly under the project-status asset root;
- the NotebookLM source-package files now live under
  `notebook_lm_assets/` instead of `notebooklm/`.

The repository documentation should now be realigned to this updated canonical
layout so paths, narrative descriptions, and index links remain accurate.

No subagent is planned for this task. The work is a constrained documentation
realignment pass.

## Technical Approach

Treat the manually updated filesystem layout as the new canonical structure for
the project-status bundle.

Canonical project-status layout after the manual reorganization:

- `doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/`
  - repository-owned presentation artifacts;
  - NotebookLM-generated presentation `.pptx`;
  - NotebookLM-generated presentation `.pdf`;
  - NotebookLM-generated video overview `.mp4`;
  - `notebook_lm_assets/` containing the NotebookLM source-package Markdown
    files and prompts.

The documentation realignment should therefore:

1. replace project-status-specific references to `notebooklm/` with
   `notebook_lm_assets/` when they refer to the source package;
2. update any project-status-specific text that still says the generated
   NotebookLM `.pptx`, `.pdf`, and `.mp4` live inside the old subfolder;
3. keep the distinction clear between:
   - the NotebookLM source-package folder;
   - the generated NotebookLM media now stored at the project-status asset
     root.

This task should not rewrite older historical technical notes unrelated to the
current project-status bundle unless they are directly part of the active
documentation surface being used now.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Documentation index containing active links to the project-status NotebookLM
  prompt files.
- `doc/technical/2026-03/2026-03-28/2026-03-28-12-06-26_integrate_notebooklm_project_status_presentation_and_video_exports.md`
  Recent technical note that currently describes the outdated layout.
- `doc/technical/2026-03/2026-03-27/2026-03-27-18-09-50_project_status_report_presentation_and_notebooklm_source_bundle.md`
  Foundational technical note for the project-status bundle, to update only if
  path-level clarification is needed.
- optionally `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.md`
  if it contains active discoverability references to the old folder name.

## Implementation Steps

1. Create this technical planning document and register it from `README.md`.
2. Wait for explicit user approval before modifying the active documentation.
3. Update the active project-status documentation references from `notebooklm/`
   to `notebook_lm_assets/` where they refer to the source package.
4. Update the recent integration note so it accurately describes the generated
   NotebookLM media as asset-root files rather than files inside the source
   package folder.
5. Update the documentation index links in `doc/README.md` to the renamed
   source-package folder.
6. Run Markdown warning checks on the touched Markdown files and confirm they
   end with a normal single final newline before closing the task.
