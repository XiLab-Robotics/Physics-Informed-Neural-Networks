# Remote PowerShell Transport Replacement

## Overview

The remote launcher has now cleared the original path-resolution and
Windows-`MAX_PATH` blockers for the `Track 1` `SVR` campaign. The remaining
failure is narrower and infrastructure-specific:

- the remote run no longer dies on the first campaign YAML path;
- the launcher reaches the `remote_run` stage;
- but no remote `stdout` markers are captured locally, even for a minimal
  remote script that only emits simple `Write-Output` lines and exits `0`.

This means the current remote PowerShell transport contract based on:

- `ssh ... "powershell ... -Command -"`
- plus local stdin redirection of the script body

is not reliable enough on this LAN workstation for marker-bearing remote
execution.

## Technical Approach

The launcher should stop depending on `powershell -Command -` plus stdin-fed
script bodies for the critical remote execution phases.

Instead, it should switch to a file-based remote execution transport:

1. write the intended remote PowerShell script to a temporary `.ps1` file in a
   remote staging directory;
2. launch that file explicitly on the remote node with
   `powershell -File <remote_temp_script.ps1>`;
3. capture `stdout`, `stderr`, and exit code from that explicit remote file
   execution;
4. remove the remote temporary script after execution.

This replacement should be applied to the canonical helper path rather than as
an ad hoc special case, so the same reliable transport is used for:

- remote preflight;
- sync-up extract helpers;
- post-sync verification;
- remote campaign run;
- sync-down helper steps.

The short-path execution alias introduced for the Windows path-length issue
should remain in place. This transport fix is orthogonal: it replaces how the
remote script is launched, not where it runs inside the remote filesystem.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
  Canonical SSH-backed remote launcher whose helper currently feeds script text
  through stdin to `powershell -Command -`.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Canonical operator note that may need a short update once the launcher uses a
  remote temporary script transport instead of stdin-fed script bodies.
- `doc/running/remote_training_campaign_status.json`
  Local tracking file that should become more informative once the remote run
  markers can actually be captured again.

## Implementation Steps

1. Replace the stdin-fed remote PowerShell transport in the canonical launcher
   helper with a remote temporary-script file execution path.
2. Keep `stdout`, `stderr`, and exit-code streaming behavior unchanged from the
   operator point of view.
3. Preserve the current short-path execution alias logic for the Windows LAN
   node.
4. Retest a minimal remote marker script first.
5. Retest the real `Track 1` `SVR` remote campaign launcher after the transport
   swap.
6. Update the launcher note if the remote execution model changes in an
   operator-visible way.
