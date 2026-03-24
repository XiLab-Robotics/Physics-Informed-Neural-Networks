# UR RTDE Visual Reference Archival

## Overview

This note records the archival of the external `ur_rtde` visual reference PDF used
for documentation-platform comparison work.

The PDF was originally provided in `.temp/` only for quick inspection.

To keep it as a stable repository-local reference for later synchronized
integration, it should be moved into a discoverable non-temporary location.

## Technical Approach

The file should be moved from the temporary workspace area into the repository
`reference/` tree under a documentation-specific subfolder.

Recommended destination:

- `reference/documentation_visual_references/ur_rtde_api_reference_example.pdf`

This keeps the file:

- out of the temporary area;
- discoverable for later documentation work;
- clearly identified as an external visual reference rather than canonical
  repository-authored documentation.

## Involved Components

- source file:
  - `.temp/example.pdf`
- destination folder:
  - `reference/documentation_visual_references/`
- isolated handoff log:
  - `readme.temp.md`

## Implementation Steps

1. Create the destination folder under `reference/` if it does not exist.
2. Move `.temp/example.pdf` into the stable reference folder.
3. Update `readme.temp.md` so the other Codex instance can locate the file.
4. Include the archived reference PDF in the next isolated commit.
