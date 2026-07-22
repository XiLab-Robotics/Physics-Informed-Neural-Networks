# Remote Training Stream Completion Fix

## Overview

The shape-first training-rule distillation pilot completed successfully on the
remote workstation, but the local operator terminal remained in a running state
and the local sync-back did not complete. Remote evidence showed both campaign
runs completed with return code `0`, while the local tracking file stayed at
`running / remote_run`.

The failure mode is in the remote training wrapper, not in the training
campaign. The wrapper streams SSH output by repeatedly calling
`StandardOutput.Peek()` and `StandardError.Peek()` while the process is alive.
With SSH-backed remote PowerShell, those `Peek()` calls can block when the
remote process is quiet or when final buffered output is pending, preventing
the wrapper from reaching marker parsing and artifact sync-down.

## Technical Approach

Replace the blocking stream polling inside
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1` with
event-driven asynchronous stream readers:

- attach `OutputDataReceived` and `ErrorDataReceived` handlers before waiting;
- write every received line to the same log, collection list, and terminal
  output path used today;
- wait for process completion through `WaitForExit()` instead of polling
  `Peek()`;
- call final `WaitForExit()` after process completion so asynchronous handlers
  flush buffered lines before marker extraction;
- preserve existing exit-code, temporary-script cleanup, and local/remote
  artifact sync behavior.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
  Remote execution wrapper and SSH streaming implementation.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Operator documentation for the remote launcher behavior.
- `doc/running/remote_training_campaign_status.json`
  Local status file that should advance from `remote_run` to sync stages and
  completed after marker parsing succeeds.
- `doc/running/active_training_campaign.yaml`
  Campaign state to update during recovery after the completed remote run is
  synchronized locally.

## Implementation Steps

1. Patch the remote wrapper stream reader to avoid blocking `Peek()` calls.
2. Validate the PowerShell parser on the updated wrapper.
3. Recover the completed shape-first pilot artifacts from the remote
   workstation using the completed campaign manifest as source of truth.
4. Update local remote-status and active-campaign state to reflect the real
   completed run.
5. Complete normal closeout and analysis from local synchronized artifacts.
