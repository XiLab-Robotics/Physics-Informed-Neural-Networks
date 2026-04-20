# Remote Campaign Launcher Stderr Tolerance And Smoke Test

## Overview

The current SSH-backed remote campaign launcher can abort locally even when the
remote campaign is still healthy, because warning lines emitted on remote
`stderr` are being surfaced by PowerShell as `NativeCommandError` records under
`$ErrorActionPreference = "Stop"`. The first concrete case is the benign
`triton not found` warning printed during the remote exact-paper launch.

This document defines a narrow hardening pass so the remote launcher continues
streaming remote output and only fails on the real remote exit code rather than
on warning text alone.

## Technical Approach

The fix should stay inside `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
and should preserve the existing canonical SSH-based workflow:

1. keep streaming remote output to the local terminal;
2. keep writing the local remote campaign log file;
3. stop treating remote warning text on `stderr` as a fatal local exception;
4. continue to use the actual remote exit code and manifest markers as the real
   success/failure criteria.

The most likely hardening is to replace the current pipeline-driven launch path
with an explicit process invocation or another PowerShell-safe pattern that
captures both output streams without letting `stderr` records become
terminating errors in the local shell.

The implementation should additionally verify that:

- remote marker lines such as `REMOTE_CAMPAIGN_MANIFEST_PATH::...` are still
  captured correctly;
- the local tracking log path is always created before the remote run starts;
- warning-rich remote stdout/stderr mixes remain visible but non-fatal.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
  Canonical SSH-backed remote campaign launcher whose remote-run stage needs
  stderr-tolerant streaming behavior.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Canonical operator note that may need a small clarification if the remote log
  behavior becomes more explicit after the fix.
- `doc/running/remote_training_campaign_status.json`
  Local tracking file used to confirm whether the launcher reaches the
  `remote_run` stage and writes a usable local log path.
- `doc/running/active_training_campaign.yaml`
  Relevant protected campaign state because the current `Track 1` `SVR`
  campaign is prepared for remote execution through this launcher.

## Implementation Steps

1. Refactor the remote-run section of
   `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1` so remote `stderr`
   warning lines do not become fatal local pipeline errors.
2. Ensure the local remote-run log file is created deterministically before the
   remote command starts streaming.
3. Preserve collection of remote marker lines and remote exit-code handling.
4. Run a smoke test against the real SSH path with a controlled remote command
   that emits both stdout and stderr but exits successfully.
5. Only after the smoke test succeeds, consider the launcher ready for the real
   remote `Track 1` campaign relaunch.
