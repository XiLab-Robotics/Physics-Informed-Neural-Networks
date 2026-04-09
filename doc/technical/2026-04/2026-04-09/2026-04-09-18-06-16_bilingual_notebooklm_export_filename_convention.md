# Bilingual NotebookLM Export Filename Convention

## Overview

This document proposes a small clarification to the repository rules for
imported `NotebookLM` exports inside bilingual guide bundles.

The current rule already requires imported `NotebookLM` exports to avoid vague
names such as `Mind Map.png` or `Video Overview.mp4` and to declare explicit
information such as guide name, track, and artifact type.

What is not yet explicit in the rule set is how language should be handled when
the exports are already stored under language-specific folders such as:

- `English/`
- `Italiano/`

The user requested that the convention be clarified so language is not repeated
in the filename when it is already clear from the parent folder.

## Technical Approach

Keep the existing rule that imported `NotebookLM` exports must declare:

- guide name;
- track;
- artifact type.

Add one clarifying rule for bilingual guide folders:

- if the parent folder already declares the language, do not repeat the
  language again inside the filename.

This keeps exported names explicit while avoiding redundant suffixes such as:

- `- English`
- `- Italian`

The change is rule-level only. It does not require a broader workflow redesign.

## Involved Components

- `AGENTS.md`
- `doc/README.md`

## Implementation Steps

1. Add a concise rule to `AGENTS.md` clarifying that language should not be
   repeated in imported export filenames when the parent guide folder already
   declares the language.
2. Keep the existing explicit naming requirement for guide name, track, and
   artifact type unchanged.
3. Register this clarification in `doc/README.md`.
4. Run scoped Markdown checks on the touched Markdown files and confirm normal
   final-newline state before closing the task.
