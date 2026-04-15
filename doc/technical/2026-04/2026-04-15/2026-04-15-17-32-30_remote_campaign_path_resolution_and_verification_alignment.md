# Remote Campaign Path Resolution And Verification Alignment

## Overview

The current `Track 1` remote `SVR` campaign now reaches the post-sync
verification stage, but two path-related problems remain:

1. the new remote verification block is generated with malformed PowerShell
   array syntax, so the verification step emits parser errors instead of
   performing a real file-existence check;
2. the subsequent remote campaign run still reaches
   `run_training_campaign.py`, where the source configuration paths are
   resolved and then fail the canonical
   `Source Config Path does not exist` assertion.

This means the remote launcher hardening is not yet complete. The next fix must
align the launcher's remote path verification logic with the exact path format
that the remote training entrypoint expects, so the launcher can detect the
problem before training begins and so the real remote invocation uses the same
valid repository-relative paths.

## Technical Approach

The fix should stay inside the canonical remote launcher
`scripts/campaigns/run_remote_training_campaign.ps1`.

The implementation should:

1. repair the PowerShell script generation used for remote source verification
   so the required path list is serialized as a syntactically valid array;
2. verify the exact same repository-relative path strings that are later passed
   to `run_training_campaign.py`;
3. add short, explicit remote diagnostics when a path check fails, including
   the missing repository-relative path and the remote working directory used by
   the verification step;
4. confirm that the remote run script invokes the training campaign from the
   expected repository root and does not accidentally alter path interpretation
   between verification and training launch;
5. smoke-test the corrected launcher against the current LAN node so the
   failure either moves fully into the new verification block with a clean
   message or the training campaign proceeds past source-config enqueue.

The goal is not to redesign the remote workflow. The goal is to make the
existing repository-owned remote launcher internally consistent about path
resolution.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
  Canonical SSH-backed remote campaign launcher that currently generates the
  malformed verification script and owns the path handoff into the remote
  training entrypoint.
- `scripts/training/run_training_campaign.py`
  Canonical queue-driven training entrypoint whose
  `enqueue_configuration_paths(...)` function asserts that every resolved source
  config path exists.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Canonical operator note that may require a short update if the launcher now
  emits more explicit path-resolution diagnostics.
- `doc/running/remote_training_campaign_status.json`
  Local tracking file that should reflect the earlier, cleaner failure state if
  verification still fails.

## Implementation Steps

1. Fix the remote verification script builder so the required path list is
   emitted as a valid PowerShell array with proper separators.
2. Add short remote diagnostics that print the verification working directory
   and the exact missing repository-relative path.
3. Recheck the remote run script path handoff to ensure it uses the same
   repository-relative path strings that were just verified.
4. Run a targeted LAN smoke test of the remote launcher using the current
   `Track 1` `SVR` campaign command.
5. Update the remote launcher note if the operator-visible diagnostics change.
