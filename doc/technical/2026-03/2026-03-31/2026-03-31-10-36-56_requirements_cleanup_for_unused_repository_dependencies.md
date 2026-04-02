# Requirements Cleanup For Unused Repository Dependencies

## Overview

This document defines the approved scope for cleaning `requirements.txt` by
removing third-party packages that are no longer used by the current canonical
repository workflows.

The goal is to reduce unnecessary installation weight and dependency-resolution
surface without breaking active training, reporting, documentation, TwinCAT
video-analysis, LAN AI node, or presentation workflows.

## Technical Approach

The cleanup will be based on current repository inspection rather than on
package popularity or historical usage.

The current evidence supports these candidate removals:

- `torchmetrics`
  no current imports were found in `scripts/`, `site/`, or active user-facing
  workflow code;
- `scipy`
  no current imports were found in `scripts/`, `site/`, or active workflow
  code;
- `onnx`
  the repository discusses ONNX in documentation and TwinCAT export planning,
  but no current Python workflow imports the `onnx` package itself.

The following packages appear to remain required and should not be removed in
this task:

- `torch`, `lightning`, `numpy`, `pandas`, `scikit-learn`, `matplotlib`,
  `tensorboard`, `colorama`, `PyYAML`
- `pymupdf`, `python-pptx`
- `faster-whisper`, `opencv-python-headless`, `pytesseract`,
  `imageio-ffmpeg`, `google-genai`
- `requests`, `fastapi`, `uvicorn`, `python-multipart`, `paddleocr`
- `sphinx`, `sphinx-rtd-theme`, `myst-parser`

The implementation will update `requirements.txt`, then refresh any README or
usage wording only if it currently claims that a removed package is part of the
canonical environment.

No subagent is planned for this task.

## Involved Components

- `requirements.txt`
- `README.md` if dependency-facing setup wording changes
- `doc/guide/project_usage_guide.md` if dependency-facing setup wording changes

## Implementation Steps

1. Remove the unused dependency entries from `requirements.txt`.
2. Re-scan the repository for direct usage of the removed packages to confirm no
   active code paths still depend on them.
3. Update dependency-facing documentation only if the removed packages are
   explicitly presented as required parts of the canonical environment.
4. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
