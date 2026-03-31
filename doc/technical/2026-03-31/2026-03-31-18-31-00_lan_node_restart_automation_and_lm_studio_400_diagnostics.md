# LAN Node Restart Automation And LM Studio 400 Diagnostics

## Overview

The first validated remote end-to-end run exposed two usability gaps in the
LAN workflow:

1. restarting `scripts/tooling/lan_ai_node_server.py` on the remote workstation
   can fail with WinError `10048` when a previous instance still owns port
   `8765`, forcing manual termination from Task Manager;
2. `LM Studio` request failures currently surface as a generic HTTP 400
   exception without the response body, so the operator cannot immediately see
   whether the problem is an unloaded model, an invalid model id, or a request
   payload issue.

## Technical Approach

Add a guarded automatic restart path for the LAN AI node server: when the
target port is already bound, detect whether the owning process corresponds to a
previous `lan_ai_node_server.py` instance and terminate that stale process
before binding again. Keep the failure explicit if the port is owned by some
other program.

For the client path, preserve the existing request flow but improve failure
diagnostics by surfacing the LM Studio response payload on non-2xx responses and
optionally preflighting the requested chat model against `/v1/models` before
sending the completion request.

## Involved Components

- `scripts/tooling/lan_ai_node_server.py`
- `scripts/tooling/lan_ai_node_client.py`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md`
- `README.md`

## Implementation Steps

1. Add remote server startup logic that can reclaim port `8765` when the port
   owner is a stale `lan_ai_node_server.py` process.
2. Keep the bind failure explicit for unrelated processes on the same port.
3. Improve LM Studio client diagnostics so HTTP failures include the response
   body and model-context details.
4. Document the new automatic-restart and LM Studio-validation behavior in the
   user-facing LAN guide material.
5. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
