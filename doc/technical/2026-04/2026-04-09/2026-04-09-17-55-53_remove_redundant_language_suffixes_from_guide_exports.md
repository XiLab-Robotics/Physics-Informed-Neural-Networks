# Remove Redundant Language Suffixes From Guide Exports

## Overview

This document proposes a small normalization pass on the imported `NotebookLM`
exports inside the harmonic-wise guide bundle.

The current export filenames already live inside language-specific folders:

- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/English/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Italiano/`

Because of that folder split, the trailing language suffixes in filenames such
as `- English` and `- Italian` are redundant and add unnecessary visual
length.

The user requested that these redundant suffixes be removed.

## Technical Approach

Keep the current naming structure for:

- guide name;
- track (`Concept` or `Project`);
- artifact type (`Guide`, `Presentation`, `Video Overview`, `Mind Map`,
  `Infographic`).

Remove only the final language suffix from the imported export filenames,
because language is already expressed by the containing folder name.

The normalization should apply consistently across all imported files in:

- `English/`
- `Italiano/`

Update the harmonic-wise guide wording only if it currently implies that the
language must remain embedded in each filename. No broader documentation
restructure is needed.

## Involved Components

- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/English/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Italiano/`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Harmonic-Wise Paper Reimplementation Pipeline.md`
- `doc/README.md`

## Implementation Steps

1. Enumerate the imported guide-local exports in `English/` and `Italiano/`.
2. Rename each file by removing the redundant trailing language suffix.
3. Update the guide wording if a filename-policy note needs to reflect the
   shorter naming pattern.
4. Run scoped Markdown checks on every touched repository-authored Markdown
   file and confirm normal final-newline state before closing the task.
