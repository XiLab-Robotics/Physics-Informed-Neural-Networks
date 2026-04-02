# Reference Code Submodule Migration

## Overview

This document defines the migration of three reference code archives currently stored as `.zip` files in `reference/codes/` to Git submodules that point directly to their upstream GitHub repositories.

The requested repositories are:

- `https://github.com/davideferrari95/blind_handover_controller`
- `https://github.com/davideferrari95/multimodal_fusion`
- `https://github.com/davideferrari95/mediapipe_gesture_recognition`

The current archived files are:

- `reference/codes/blind_handover_controller-master.zip`
- `reference/codes/multimodal_fusion-master.zip`
- `reference/codes/mediapipe_gesture_recognition-master.zip`

The goal is to keep these reference codebases directly accessible from GitHub, easier to update, and more traceable than binary archive snapshots.

## Technical Approach

The migration will replace each `.zip` archive with a Git submodule under `reference/codes/`.

The target layout will be:

- `reference/codes/blind_handover_controller`
- `reference/codes/multimodal_fusion`
- `reference/codes/mediapipe_gesture_recognition`

The change will be implemented by:

1. adding the three repositories as submodules under the target folder names;
2. removing the legacy `.zip` files from `reference/codes/`;
3. updating `.gitmodules` to include the new submodule entries;
4. updating project documentation where useful so the reference-code storage model is explicit.

This keeps `reference/codes/` as the place for external code references while replacing opaque binary archives with Git-tracked references.

## Involved Components

- `.gitmodules`
- `README.md`
- `doc/README.md`
- `reference/codes/blind_handover_controller-master.zip` -> `reference/codes/blind_handover_controller`
- `reference/codes/multimodal_fusion-master.zip` -> `reference/codes/multimodal_fusion`
- `reference/codes/mediapipe_gesture_recognition-master.zip` -> `reference/codes/mediapipe_gesture_recognition`
- `doc/technical/2026-03/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md`

## Implementation Steps

1. Add this technical document and reference it from the project documentation indexes.
2. After user approval, add the three requested GitHub repositories as submodules under `reference/codes/`.
3. Remove the existing `.zip` files that are being replaced by the new submodules.
4. Update `.gitmodules` and any relevant repository documentation to reflect the new reference-code layout.
5. Verify the final repository state with `git status` and submodule path checks.
6. Create a Git commit with a repository-aligned title and an accurate description of the migration.
