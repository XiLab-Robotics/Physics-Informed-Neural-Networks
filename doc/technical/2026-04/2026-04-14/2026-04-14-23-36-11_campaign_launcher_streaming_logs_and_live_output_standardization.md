# Campaign Launcher Streaming Logs And Live Output Standardization

## Overview

Current repository campaign launchers capture the full output of each run into a
PowerShell variable and only print and write the log after that run finishes.
This makes long-running exact-paper and training campaigns appear stalled even
when the underlying Python process is still active.

The goal of this future change is to make live progress visible for any
repository campaign by promoting streaming console output and streaming log-file
updates to the default launcher behavior.

This document is preparation only. It must not be implemented until the user
explicitly asks for it after the currently active campaign is fully analyzed
and closed.

## Technical Approach

The implementation should replace the current buffered campaign-launcher
pattern with a streaming execution pattern that:

- writes runner output to the console in real time;
- appends the same output to the per-run log file in real time;
- preserves native exit codes correctly;
- works consistently for exact-paper campaign launchers and future repository
  training campaigns;
- keeps the launcher structure simple enough that new campaign scripts inherit
  the same behavior by default.

The standardization should be applied at the launcher-helper level rather than
through one-off fixes in single campaign scripts. The repository should have one
preferred PowerShell execution pattern for campaign runs, and all future
campaign launchers should follow it.

The intended behavioral improvements are:

- operators can see that a run is alive while `GridSearchCV` or export is
  running;
- the per-run log file is usable during execution, not only after completion;
- a VS Code UI hiccup or terminal redraw issue is easier to distinguish from a
  real workflow failure;
- campaign progress becomes inspectable without waiting for a run boundary.

## Involved Components

- `scripts/campaigns/`
  PowerShell launchers that currently use the buffered
  `Invoke-CondaRunWithLoggedOutput` pattern.
- `doc/scripts/campaigns/`
  Launcher notes that should eventually document the new streaming behavior.
- exact-paper campaign launchers such as
  `run_track1_svr_reference_grid_search_repair_campaign.ps1`
  Representative current examples of the buffered output pattern.
- future training and validation campaign launchers
  The standardized behavior must apply repository-wide, not only to the
  currently active `SVR` repair package.

## Implementation Steps

1. Review the current PowerShell helper pattern used by repository campaign
   launchers and identify the exact buffering point that delays console/log
   output.
2. Replace that helper with a streaming-safe execution pattern that mirrors
   output to both console and log file while preserving native process failure
   detection.
3. Promote the streaming helper to the repository campaign-launcher standard
   and update the active campaign scripts that still use the buffered pattern.
4. Update the corresponding launcher notes so operators know logs are expected
   to grow live during execution.
5. Validate the new behavior on a real campaign run and confirm that:
   console output is live,
   log files grow during execution,
   and non-zero exit codes still stop the umbrella campaign immediately.
