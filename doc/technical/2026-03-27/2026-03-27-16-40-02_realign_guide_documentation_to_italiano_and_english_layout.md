# Realign Guide Documentation To Italiano And English Layout

## Overview

The guide tree under `doc/guide/` has been manually reorganized so that each
topic root now uses explicit language folders:

- `Italiano/`
- `English/`
- `assets/`

The Italian guide exports were moved under `Italiano/`.
The English concept exports remain under `English/`.
The English filenames were also normalized so they no longer include the
explicit `English` token in the artifact filename itself.

This manual refactor changed the real guide structure, but the repository-owned
documentation still reflects older assumptions from previous integration steps,
including:

- references to `English/` as an English-only side folder without the matching
  `Italiano/` folder;
- references to old `English Concept ...` filenames;
- notes that still describe the pre-`Italiano/` layout;
- references that still assume the Italian exports live directly at the guide
  root rather than under `Italiano/`.

The repository documentation now needs a full consistency pass so it matches
the real guide layout.

## Technical Approach

The documentation should be updated to treat the current guide layout as the
canonical structure:

- `doc/guide/<Guide Name>/Italiano/`
- `doc/guide/<Guide Name>/English/`
- `doc/guide/<Guide Name>/assets/`

The intended alignment pass should:

1. update user-facing guide references so they mention `Italiano/` and
   `English/` explicitly;
2. update technical notes that still describe the old layout;
3. remove stale wording about `English` filename prefixes when the current files
   no longer carry them;
4. preserve the distinction between:
   - Italian concept and project exports in `Italiano/`;
   - English concept exports in `English/`;
   - package source material in `assets/`.

The pass is documentation-only. It should not rename or move the guide export
files again unless a new inconsistency is discovered during verification.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- guide Markdown files under `doc/guide/<Guide Name>/`
  User-facing topic guides that should describe the new folder layout.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide that must explain the current guide organization.
- touched technical notes under `doc/technical/`
  Prior planning and archive notes that still describe older guide-layout
  assumptions.

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before editing the guide and technical
   documentation.
3. Update user-facing guide references from the older layout to the
   `Italiano/` plus `English/` layout.
4. Update the touched technical notes so their recorded structure matches the
   current guide tree.
5. Run Markdown checks on the touched Markdown files before closing the task.
