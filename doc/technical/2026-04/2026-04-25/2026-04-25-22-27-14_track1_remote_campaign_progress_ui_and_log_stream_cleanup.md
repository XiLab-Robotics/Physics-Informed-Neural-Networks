# 2026-04-25-22-27-14 Track1 Remote Campaign Progress Ui And Log Stream Cleanup

## Overview

The current remote `Track 1` bidirectional mega-campaign launcher is
functionally working, but the operator-facing terminal stream is too noisy and
misleading during long runs.

The most visible problems are:

- the central `Write-Progress` bar stays on `Config 1/400` instead of showing
  the real active config index across the whole queue;
- the progress bar does not clearly separate total campaign completion from the
  local activity inside the currently running task;
- raw `GridSearchCV` `[CV] END ...` lines flood the terminal and bury the
  higher-level campaign state;
- the operator cannot quickly see:
  - which config is active now;
  - how many configs are done;
  - what percentage of the total campaign is complete;
  - whether the current task is fitting, exporting, syncing, or closing.

## Technical Approach

The cleanup should preserve the current remote execution contract and artifact
sync behavior, but redesign the terminal surface into a clearer two-level
status stream.

The first level should be the total campaign progress:

- current config index out of total queue size;
- percentage complete across all configs;
- active run name;
- completed count and remaining count.

The second level should be the active task status:

- current phase such as `preflight`, `sync`, `fit`, `grid_search`,
  `evaluation`, `onnx_export`, `artifact_sync`;
- last meaningful structured event from the active config;
- active remote log path when useful.

The noisy `GridSearchCV` cross-validation lines should no longer be streamed
verbatim into the main operator console. They should still be preserved in the
remote and local log files, but the main terminal should receive either:

- a compact sampled summary; or
- a suppressed stream with periodic high-level heartbeat updates.

The intended behavior is:

- the operator sees one stable total-progress bar that advances from `1/400`
  to `400/400`;
- the operator sees concise state lines for the active config;
- the raw grid-search chatter remains available in logs without dominating the
  terminal.

Because the affected launchers are currently listed in
`doc/running/active_training_campaign.yaml`, this change touches protected
campaign files and requires explicit approval before implementation.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md`

## Implementation Steps

1. Rework the remote wrapper progress bookkeeping so total queue progress is
   driven by the true active config index instead of the initial placeholder.
2. Split operator-facing progress into total campaign status and active-task
   status.
3. Suppress or compact the raw `GridSearchCV` `[CV] END ...` lines in the main
   terminal while keeping them in logs.
4. Update the mega-campaign launcher note so the new operator-facing behavior
   is documented.
5. Re-run targeted PowerShell validation and documentation QA before closing.
