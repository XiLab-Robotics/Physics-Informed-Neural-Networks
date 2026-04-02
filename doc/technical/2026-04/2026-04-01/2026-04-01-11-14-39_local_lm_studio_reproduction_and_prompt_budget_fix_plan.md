# Local LM Studio Reproduction And Prompt Budget Fix Plan

## Overview

The remote LAN workflow is still failing during the `LM Studio` cleanup stage.
The latest diagnostics show that the immediate blocker is no longer transport or
basic parsing, but prompt budget exhaustion inside `LM Studio` itself:

- the request reaches `LM Studio` correctly;
- `LM Studio` rejects the request because `n_keep` exceeds `n_ctx`;
- the remote machine also mixes in GPU-specific instability for some models.

To resolve this cleanly, the workflow must first be reproduced on the current
local workstation with a lightweight `LM Studio` model and a local server. That
lets us distinguish:

- repository prompt-construction bugs;
- repository response-parsing bugs;
- `LM Studio` runtime limitations tied to context size or GPU execution.

## Technical Approach

Set up `LM Studio` locally on the current workstation with a lightweight chat
model, then run the repository workflow against `127.0.0.1:1234` while keeping
the remote LAN transcription path for audio only. Use the local reproduction to
measure prompt size pressure and fix the repository workflow where needed.

The likely repository-side fixes are:

- reduce cleanup prompt size further when using `LM Studio`;
- add explicit prompt-budget guards before sending large requests;
- preserve the existing `reasoning_content` and retry handling already added to
  the client;
- keep the LAN node remote-only for transcription/OCR while localizing the text
  generation backend during debugging.

## Involved Components

- `scripts/tooling/extract_video_guide_knowledge.py`
- `scripts/tooling/lan_ai_node_client.py`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md`
- `README.md`

## Implementation Steps

1. Verify whether `LM Studio` is installed and reachable on the local
   workstation; if not, configure a local lightweight model and local server.
2. Reproduce the cleanup/report stage locally while still using the remote LAN
   node for transcription.
3. Measure prompt-budget pressure and identify the remaining repository-side
   causes of `LM Studio` rejection.
4. Apply the minimal workflow fixes needed to make the local run stable.
5. Update the LAN setup and usage documentation with the validated local-debug
   fallback path if the workflow changes.
6. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
