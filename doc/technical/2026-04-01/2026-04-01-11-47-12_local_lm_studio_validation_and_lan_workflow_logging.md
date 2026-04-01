# Local LM Studio Validation And LAN Workflow Logging

## Overview

The LAN video-guide workflow now needs a local validation phase on the current
workstation before returning to the remote workstation. The user has installed a
local `LM Studio` instance, created a dedicated `LM_STUDIO_LOCAL_URL`
environment variable, and wants the repository workflow validated locally with a
lightweight model while the remote `LM Studio` and LAN node are stopped.

The current workflow also lacks useful terminal visibility during long-running
video-guide extraction. Until an error occurs, the terminal mostly shows a
`RequestsDependencyWarning`, which makes it difficult to understand the current
stage, selected providers, active URLs, model ids, and progress.

## Technical Approach

Use the current workstation as the primary debug target:

- verify local `LM Studio` reachability and the environment variables used for
  local testing;
- create a local Conda environment dedicated to the LAN AI node dependencies so
  local endpoint testing can run without relying on the remote workstation;
- make the `LM Studio` routing explicit in the tooling so local tests can point
  to `LM_STUDIO_LOCAL_URL` without overwriting the remote configuration;
- improve `extract_video_guide_knowledge.py` terminal logging with concise,
  stage-oriented, training-style status messages;
- keep the logging elegant and high-signal rather than verbose dumps.

The likely code changes are:

- environment resolution updates in the `LM Studio` client/workflow path;
- local setup guidance updates;
- structured progress logging inside
  `scripts/tooling/extract_video_guide_knowledge.py`.

## Involved Components

- `scripts/tooling/extract_video_guide_knowledge.py`
- `scripts/tooling/lan_ai_node_client.py`
- `scripts/tooling/lan_ai_node_server.py`
- `requirements-lan-ai-node.txt`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md`
- `README.md`

## Implementation Steps

1. Verify local `LM Studio` availability, token visibility, and the dedicated
   local URL environment variable.
2. Create and validate a local Conda environment for the LAN AI node
   dependencies.
3. Update the workflow so local `LM Studio` routing can be selected cleanly
   during testing without overwriting the remote server configuration.
4. Add structured, elegant terminal logging to the video-guide extraction
   workflow.
5. Run local validation against the local `LM Studio` instance and iterate on
   any remaining prompt-budget or provider-shape issues.
6. Update the relevant setup and usage documentation.
7. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
