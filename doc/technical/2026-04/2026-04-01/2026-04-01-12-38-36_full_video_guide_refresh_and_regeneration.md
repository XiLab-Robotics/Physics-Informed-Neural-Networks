# Full Video Guide Refresh And Regeneration

## Overview

This scope covers a full refresh of the repository-owned TwinCAT/TestRig video
guide outputs after the LM Studio prompt-budget fixes, local LM Studio
validation, and LAN workflow stabilization work completed on `2026-04-01`.

The goal is to re-test the end-to-end video workflow, then regenerate or repair
the outstanding video-guide artifacts that are currently untracked or outdated
in the repository working tree.

The expected output includes refreshed analysis artifacts, corrected transcript
artifacts, regenerated per-video reports, refreshed report indexes, and any
supporting script updates needed to keep the generated material consistent with
the latest validated workflow behavior.

## Technical Approach

The implementation will proceed in three stages.

First, validate the stabilized workflow against the currently available runtime
topology. The preferred path is:

- remote `LM Studio` on the remote workstation;
- remote `lan_ai_node_server.py` on the remote workstation;
- repository orchestration from the current workstation.

If the remote launch path blocks, the already-validated local path remains the
fallback for workflow verification before wider regeneration.

Second, identify the current repository-owned video-guide outputs that are
stale, partially generated, or untracked. This includes the existing
`doc/reference_codes/video_guides/` artifacts and the supporting analysis roots
under `.temp/video_guides/`.

Third, rerun the high-quality extraction workflow across the required videos and
repair any resulting documentation indexes or generated report trees so that
the repository reflects one coherent analysis state built with the current
workflow logic.

## Involved Components

- `scripts/tooling/extract_video_guide_knowledge.py`
- `scripts/tooling/analyze_video_guides.py`
- `scripts/tooling/generate_video_guide_reports.py`
- `scripts/tooling/lan_ai_node_client.py`
- `scripts/tooling/lan_ai_node_server.py`
- `.temp/video_guides/`
- `doc/reference_codes/video_guides/`
- `doc/reference_codes/README.md`
- `doc/reference_codes/video_guides/README.md`

## Implementation Steps

1. Verify the currently reachable runtime path for `LM Studio` and the LAN AI
   node.
2. Run an end-to-end workflow smoke test on one representative video.
3. Inspect the untracked and outdated video-guide artifacts and determine the
   exact regeneration scope.
4. Regenerate the required per-video outputs with the current workflow.
5. Refresh the generated Markdown indexes and repository-owned guide/report
   trees affected by the new analysis outputs.
6. Run scoped Markdown checks on the touched repository-owned Markdown files.
7. Report completion and wait for explicit approval before creating any commit.
