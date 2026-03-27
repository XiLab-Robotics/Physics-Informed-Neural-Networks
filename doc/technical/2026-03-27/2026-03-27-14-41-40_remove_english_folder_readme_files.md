# Remove English Folder README Files

## Overview

The recent English-export integration introduced one `README.md` file inside
each guide-local `English/` folder to make the imported English assets
discoverable.

The user explicitly rejected those files and requested that they be removed.

This affects the following locations:

- `doc/guide/FeedForward Network/English/README.md`
- `doc/guide/Harmonic Regression/English/README.md`
- `doc/guide/Multilayer Perceptrons/English/README.md`
- `doc/guide/Neural Network Foundations/English/README.md`
- `doc/guide/Periodic Feature Network/English/README.md`
- `doc/guide/Residual Harmonic Network/English/README.md`
- `doc/guide/TE Model Curriculum/English/README.md`
- `doc/guide/Training, Validation, And Testing/English/README.md`

## Technical Approach

The `English/` folders should remain as asset containers only.

The `README.md` files are not required for the repository structure to remain
valid because:

- the imported English files already use explicit repository-owned filenames;
- the topic-level guides already contain the minimal English companion note;
- the folder name `English/` is self-descriptive enough for navigation.

The cleanup should therefore:

1. remove the eight guide-local `English/README.md` files;
2. leave the English export files themselves untouched;
3. preserve the topic-level guide references that point readers to the
   `English/` folder rather than to a folder-local README.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/guide/<Guide Name>/English/README.md`
  The guide-local README files to remove after approval.
- guide Markdown files that already reference the `English/` folder
  These may remain valid without further changes if they do not depend on the
  folder-local README path specifically.

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before removing any guide-local `README.md`
   files.
3. Remove the eight `English/README.md` files.
4. Update any repository-owned references that still point to
   `English/README.md` instead of the `English/` folder itself.
5. Run Markdown checks on the touched Markdown files before closing the task.
