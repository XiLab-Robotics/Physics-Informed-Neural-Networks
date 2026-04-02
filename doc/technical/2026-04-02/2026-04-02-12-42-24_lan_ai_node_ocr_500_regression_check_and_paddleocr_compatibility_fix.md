# LAN AI Node OCR 500 Regression Check And PaddleOCR Compatibility Fix

## Overview

This scope verifies a previously observed `500 Internal Server Error` on the
remote LAN AI node `/ocr` endpoint and determines whether the issue has already
been eliminated or is still latent in the current repository code.

The reported remote traceback shows:

- `POST /ocr` failed with `500 Internal Server Error`;
- the failure occurred during `PaddleOCR(...)` construction;
- the concrete exception was `ValueError: Unknown argument: show_log`.

The user also observed an earlier client-side message mentioning:

- `500 Server Error: Internal Server Error for url: http://155.185.226.100:8765/ocr`
- `Selected model is at capacity. Please try a different model.`

This task must determine which part of that behavior is still relevant to the
current codebase and, if needed, make the OCR path robust against current
`paddleocr` versions and future recoverable OCR initialization issues.

## Technical Approach

The verification will proceed in three layers.

First, inspect the current repository version of:

- `scripts/tooling/lan_ai_node_server.py`
- `scripts/tooling/lan_ai_node_client.py`

to compare the user-provided traceback with the exact live code path.

Second, separate the two observed failures:

- the server-side `PaddleOCR` constructor crash on unknown argument
  `show_log`;
- the earlier client-visible `/ocr` `500` with the text
  `Selected model is at capacity. Please try a different model.`

The first one can be verified directly from current code. The second one will
be treated as either:

- a stale symptom from an older runtime combination;
- a misleading downstream body propagated by another component;
- or a still-possible failure mode if the client/server error handling is too
  loose.

Third, if the current code is still vulnerable, apply a compatibility fix in the
LAN node server and strengthen the OCR error surface so future failures become
explicit and diagnosable instead of surfacing as opaque `500` crashes.

## Involved Components

- `scripts/tooling/lan_ai_node_server.py`
  Remote FastAPI node exposing `/transcribe` and `/ocr`.
- `scripts/tooling/lan_ai_node_client.py`
  Current workstation client used by the extraction workflow.
- `scripts/tooling/extract_video_guide_knowledge.py`
  Main workflow consumer of the OCR path.
- `doc/scripts/tooling/lan_ai_node_server.md`
  Setup and troubleshooting guide for the remote node.
- `doc/scripts/tooling/remote_high_quality_video_pipeline.md`
  Formal pipeline note for the remote-strong path.
- `README.md`
  Main project index that must register this technical document.

## Implementation Steps

1. Verify the current OCR path in the server and client against the reported
   traceback.
2. Determine whether the `show_log` constructor incompatibility is still
   present in the repository code.
3. If present, remove or adapt the incompatible PaddleOCR arguments and align
   the code with the current supported constructor surface.
4. Improve OCR-side error handling so server-side initialization failures become
   explicit `HTTPException` messages instead of generic unhandled `500`
   crashes.
5. Update the remote-node and pipeline documentation with the confirmed root
   cause and the new behavior.
6. Re-run scoped QA on the touched Markdown and Python files.
