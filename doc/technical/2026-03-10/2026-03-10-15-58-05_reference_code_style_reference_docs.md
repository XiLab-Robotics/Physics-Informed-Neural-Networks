# Reference Code Style Reference Docs

## Overview

This document defines the creation of persistent documentation files under `doc/reference_codes/` to analyze the three Git submodules currently stored in `reference/codes/`.

The target repositories are:

- `reference/codes/blind_handover_controller`
- `reference/codes/mediapipe_gesture_recognition`
- `reference/codes/multimodal_fusion`

The goal is to save a more detailed and reusable reference of their programming style, project organization, training patterns, utilities, and practical implementation conventions before starting the neural-network implementation in this repository.

This work extends the existing summary in `doc/reference_summaries/06_Programming_Style_Guide.md` with repository-specific notes that remain directly usable during future implementation tasks.

## Technical Approach

The new documentation will be created as a dedicated `doc/reference_codes/` section focused on code-analysis notes rather than source-code copies.

The planned documentation set is:

- one index document for the new section;
- one detailed reference document for `blind_handover_controller`;
- one detailed reference document for `mediapipe_gesture_recognition`;
- one detailed reference document for `multimodal_fusion`.

Each reference document will extract and preserve the most useful implementation signals from representative files already present in the submodules, including:

- naming conventions for variables, classes, callbacks, constants, and helper functions;
- import grouping and section-comment patterns;
- class and script structure for ROS nodes, utilities, and training modules;
- PyTorch and PyTorch Lightning usage patterns already proven in the reference code;
- configuration handling, debug-print style, assertions, and runtime checks;
- reusable conventions that should be mirrored in the future RV-reducer ML codebase.

The analysis will stay selective and engineering-oriented:

1. inspect only representative files from each submodule;
2. summarize stable conventions and recurring patterns;
3. distinguish the strict baseline (`blind_handover_controller`) from supporting references;
4. record practical rules that can be reused during the neural-network implementation phase.

The documentation will remain in English and will avoid repository-internal noise such as large datasets, binaries, or exhaustive file inventories unless they contribute directly to the coding-style reference.

## Involved Components

- `doc/technical/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md`
- `doc/reference_codes/README.md`
- `doc/reference_codes/blind_handover_controller_reference.md`
- `doc/reference_codes/mediapipe_gesture_recognition_reference.md`
- `doc/reference_codes/multimodal_fusion_reference.md`
- `README.md`
- `doc/README.md`
- `doc/reference_summaries/06_Programming_Style_Guide.md`
- Representative source files under:
  - `reference/codes/blind_handover_controller/`
  - `reference/codes/mediapipe_gesture_recognition/`
  - `reference/codes/multimodal_fusion/`

## Implementation Steps

1. Create this technical document as the approval gate for the requested repository change.
2. After user approval, create the new `doc/reference_codes/` folder and its index document.
3. Analyze representative source files in each submodule and write one detailed reference document per repository.
4. Cross-check the new documents against `doc/reference_summaries/06_Programming_Style_Guide.md` so the short summary and the detailed references stay consistent.
5. Update `README.md` and `doc/README.md` so the new technical document and the new `doc/reference_codes/` section are discoverable from the project documentation indexes.
6. Verify the created documentation files and repository status.
7. Create a Git commit with a repository-aligned title and body summarizing the new reference-code documentation.

