# Campaign Launcher Interruptible Stop And Progress Heartbeat

## Overview

The current streaming campaign launcher solved buffered end-of-run output, but
two operational problems remain:

1. `Ctrl+C` in the terminal does not stop the active campaign run cleanly.
2. long-running exact-paper fits can still appear frozen for tens of minutes
   when no new line is emitted by the child process.

This document defines a launcher hardening pass so campaigns become
interruptible by the operator and expose a terminal-visible heartbeat while the
underlying child process remains alive.

## Technical Approach

The fix should stay in the shared PowerShell launcher helper rather than
campaign-specific scripts, because the behavior must apply to any future
campaign using the repository-standard streaming path.

The launcher should gain two pieces of behavior:

1. interrupt propagation:
   - detect user cancellation from the host terminal;
   - terminate the full launched process tree (`cmd.exe`, `conda run`,
     Python child) instead of leaving the child process alive;
   - return a non-zero exit code and print an explicit cancellation message.
2. terminal-only heartbeat:
   - while waiting for streamed child output, periodically print a compact
     progress line to the terminal;
   - include elapsed time and child-process liveness;
   - keep the heartbeat out of the persisted `.log` file so the file remains
     mostly child-process-authored output.

The heartbeat is not intended to claim candidate-level completion when that
information is unavailable. Its purpose is to prove that the launcher is still
attached to a live process and that the operator can still interrupt it.

The implementation should preserve:

- live log file writes for real child output lines;
- correct process exit-code propagation;
- the current launcher command surface;
- compatibility with the existing exact-paper campaign launchers already moved
  to the shared helper.

## Involved Components

- `scripts/campaigns/shared_streaming_campaign_launcher.ps1`
  Shared campaign helper that currently streams child output but does not yet
  provide an operator-visible heartbeat or explicit process-tree cancellation.
- `scripts/campaigns/*.ps1`
  Existing launchers that consume the shared helper and will inherit the new
  behavior without individual rewrites.
- `doc/scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign.md`
  Current launcher note that should reflect the new interrupt and heartbeat
  behavior if the implementation is approved.
- `doc/running/active_training_campaign.yaml`
  Relevant operational context because the current request was triggered during
  an active campaign, although the hardening itself should not edit this file.

## Implementation Steps

1. Refactor the shared launcher helper to run the child process in a way that
   allows periodic liveness checks instead of blocking indefinitely on line
   reads.
2. Add a terminal-only heartbeat message on a fixed interval while no new child
   output is available.
3. Add explicit stop handling so user cancellation terminates the child process
   tree and returns a clear non-zero launcher result.
4. Keep `.log` files limited to real child output lines and explicit launcher
   failure/cancellation summaries only when needed.
5. Smoke-test the helper with a controlled long-running child process to verify
   live output, heartbeat visibility, and operator-stop behavior.
