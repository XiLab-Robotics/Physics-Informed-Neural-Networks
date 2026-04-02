# LM Studio Resilient Chunked Cleanup For LAN Workflow

## Overview

The validated remote workflow shows that the current `LM Studio` integration is
failing for two different reasons:

1. some `LM Studio` models can return `reasoning_content` while leaving
   `message.content` empty;
2. the current LAN cleanup path sends the entire raw transcript into one large
   prompt for `correct_and_segment_full_transcript`, pushing the local
   `LM Studio` context window to its limit and increasing the probability of GPU
   instability, truncation, and model reloads.

The logs show both failure modes in practice:

- `qwen/qwen3.5-9b`: successful generation with empty `content`,
  non-empty `reasoning_content`, and `total_tokens = 4096` with
  `truncated = 1`;
- `google/gemma-3-4b`: GPU-side `llama.cpp` abort followed by
  `{"error":"Model reloaded."}`.

## Technical Approach

Resolve the problem at both layers:

- make the LM Studio client more resilient by handling provider-specific
  response shapes and transient model reloads;
- reduce prompt size materially by replacing the full-transcript LM Studio
  cleanup path with a chunked cleanup path that reuses the existing
  `TranscriptChunk` abstraction and the already-implemented
  `correct_transcript_chunk_list` workflow.

For the LAN transcription path, the server/client contract should be extended to
return timestamped segment data from `faster-whisper`. Those segment timestamps
can then be grouped into repository-sized transcript chunks without asking the
LLM to invent approximate timing from one giant prompt.

That gives a more stable pipeline:

1. LAN node returns transcript text plus timestamped segment list.
2. The local workflow groups segments into time-window chunks.
3. LM Studio only cleans each chunk text instead of segmenting the full video
   from scratch.
4. The report step consumes the smaller, already-structured chunk list.

## Involved Components

- `scripts/tooling/lan_ai_node_server.py`
- `scripts/tooling/lan_ai_node_client.py`
- `scripts/tooling/extract_video_guide_knowledge.py`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md`
- `README.md`

## Implementation Steps

1. Extend the LAN transcription API to optionally return timestamped transcript
   segments.
2. Update the LAN client to consume the richer transcript payload.
3. Build a chunked LAN transcript-cleanup path in
   `extract_video_guide_knowledge.py` that uses actual timestamps and
   `correct_transcript_chunk_list` instead of the giant full-transcript cleanup
   prompt.
4. Make the LM Studio client resilient to:
   - empty `content` with non-empty `reasoning_content`;
   - transient `Model reloaded.` errors via a guarded retry path.
5. Update the LAN setup and usage documentation to describe the new stable
   workflow and troubleshooting behavior.
6. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
