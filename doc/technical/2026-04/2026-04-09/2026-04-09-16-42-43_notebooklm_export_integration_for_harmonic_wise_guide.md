# NotebookLM Export Integration For Harmonic-Wise Guide

## Overview

This document proposes the repository-owned integration of the generated
`NotebookLM` exports for the harmonic-wise paper-reimplementation guide.

The user placed the generated artifacts in temporary staging folders under
`.temp/`:

- `.temp/concept_video_guide_english`
- `.temp/concept_video_guide_italiano`
- `.temp/project_video_guide_english`
- `.temp/project_video_guide_italiano`

These folders contain externally generated deliverables such as `PDF`, `PPTX`,
`MP4`, and image assets. They are not yet aligned with the repository naming
rules, guide-local placement rules, or final documentation references.

The goal of this task is to integrate those exports into the canonical guide
bundle under `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/` so the
artifacts become repository-owned, discoverable, and ready for colleague-facing
reuse.

## Technical Approach

Treat the `.temp/` folders as staging inputs only.

Promote the generated exports into the guide-local bilingual folders:

- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/English/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Italiano/`

During promotion, rename every imported `NotebookLM` export so the filenames
explicitly declare:

- guide name;
- track (`Concept` or `Project`);
- language (`English` or `Italian`);
- artifact type (`PDF`, `PPTX`, `MP4`, `Mind Map`, `Infographic`, or similar).

This task should not silently preserve vague names such as `unnamed.png`,
`NotebookLM Mind Map.png`, or title-only filenames with no track/language
boundary.

After the files are renamed and moved into the canonical guide-local folders,
update the guide Markdown only if a compact artifact inventory or export note is
needed for discoverability. Avoid turning the guide into a raw file manifest.

Also update the Sphinx-facing guide bridge if a short note about the bilingual
exports or the final deliverable structure improves discoverability in the
portal.

The integration should keep the two explanatory tracks distinct:

- neutral concept-oriented educational exports;
- repository-specific project-oriented exports.

## Involved Components

- `.temp/concept_video_guide_english/`
- `.temp/concept_video_guide_italiano/`
- `.temp/project_video_guide_english/`
- `.temp/project_video_guide_italiano/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/English/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Italiano/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Harmonic-Wise Paper Reimplementation Pipeline.md`
- `site/guide/harmonic_wise_paper_reimplementation_pipeline.md`
- `doc/README.md`

## Implementation Steps

1. Inspect the four `.temp/` staging folders and enumerate the generated export
   files by track, language, and artifact type.
2. Define repository-consistent final filenames for each export so the guide
   name, track, language, and artifact type are explicit.
3. Move the exports from `.temp/` into the canonical guide-local `English/` and
   `Italiano/` folders using the final filenames.
4. Add or update a compact documentation note in the guide bundle only if it
   materially improves discoverability of the integrated exports.
5. Update the Sphinx guide bridge only if the exported deliverables need a
   portal-facing note.
6. Run scoped Markdown checks on every touched repository-authored Markdown file
   and confirm normal final-newline state before closing the task.
