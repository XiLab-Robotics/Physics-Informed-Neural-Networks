# Remote Exact-Paper Config Resolution And Conda Stderr Fix

## Overview

The restored remote exact-paper launcher now reaches the correct execution
phase, but two residual bugs still block a clean remote run:

- the exact-paper validation entrypoint still resolves relative config paths
  through the long physical repository path instead of the short remote working
  root `R:\`, so `Training Config Path does not exist` is raised again on the
  LAN node;
- the remote PowerShell loop still surfaces `conda` warning lines on `stderr`
  as noisy `NativeCommandError` records while the process continues, which
  makes the terminal output harder to trust during long runs.

This fix is a continuation of the already approved remote exact-paper parity
work. It addresses the last path-resolution and wrapper-noise defects before
the operator relaunches the campaign manually.

## Technical Approach

The path bug will be fixed at the training-config loading boundary so exact-paper
and future remote workflows can honor the current working directory when a
relative config path is supplied. The remote wrapper will also invoke `conda`
in a way that preserves streamed output and real exit codes without letting
benign warning lines collapse into misleading PowerShell-native error records.

The target behavior is:

1. relative config paths resolve against the live working directory first;
2. project-root fallback remains available for normal local use;
3. the remote launcher still streams full output;
4. wrapper failure is driven by the real process exit code, not by benign
   warning text written to `stderr`.

## Involved Components

- `scripts/training/shared_training_infrastructure.py`
- `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1`
- `doc/technical/2026-04/2026-04-16/README.md`

Protected campaign file expected to require modification:

- `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1`

No subagent is planned for this implementation.

## Implementation Steps

1. Add a working-directory-aware relative config-path resolver in
   `shared_training_infrastructure.load_training_config()`.
2. Keep the existing project-root fallback so local repository behavior stays
   stable.
3. Update the remote exact-paper wrapper so the `conda` invocation streams to
   the per-run log without letting warning-only `stderr` lines become
   misleading wrapper-level errors.
4. Re-run syntax checks and scoped Markdown QA on the touched files.
