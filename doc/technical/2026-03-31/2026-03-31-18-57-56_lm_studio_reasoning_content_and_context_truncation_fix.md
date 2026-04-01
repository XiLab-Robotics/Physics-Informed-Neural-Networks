# LM Studio Reasoning Content And Context Truncation Fix

## Overview

The first validated LAN cleanup/report run against `LM Studio` exposed a
provider-shape mismatch rather than a transport failure. For
`qwen/qwen3.5-9b`, the OpenAI-compatible response can return an empty
`message.content` while placing the generated text into
`message.reasoning_content`. The current repository client only reads
`message.content`, so it raises `AssertionError: LM Studio returned empty text.`

The same run also showed context saturation in the `LM Studio` server logs:
`total_tokens = 4096` with `truncated = 1`. That means the cleanup prompt is
already pushing the configured context window to its limit, so the workflow
needs better diagnostics and safer fallback behavior.

## Technical Approach

Update the LAN/LM Studio client to support the provider response shape actually
observed in the validated run:

- use `message.content` when present;
- fall back to `message.reasoning_content` when `content` is empty;
- preserve explicit diagnostics when both fields are empty.

Additionally, improve the failure message when the response indicates likely
context truncation or token-budget exhaustion, so the operator can distinguish
between:

- unloaded or invalid model ids;
- empty output because the provider used `reasoning_content`;
- degraded output caused by context saturation.

If needed after the parsing fix, the cleanup/report workflow can also be tuned
to reduce prompt size or switch to a less context-hungry LM Studio model.

## Involved Components

- `scripts/tooling/lan_ai_node_client.py`
- `scripts/tooling/extract_video_guide_knowledge.py`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md`
- `README.md`

## Implementation Steps

1. Extend the LM Studio client response parser to read `reasoning_content` when
   `content` is empty.
2. Add explicit diagnostics for context-window saturation indicators where
   possible.
3. Update the relevant usage documentation to mention the validated provider
   behavior and the recommended troubleshooting path.
4. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
