# Remote Campaign Source Sync Verification

## Overview

The current remote campaign launcher now tolerates benign remote `stderr`
warnings correctly, but the first real `Track 1` LAN launch still fails because
the remote runtime cannot find the synchronized campaign YAML files under the
expected `config\paper_reimplementation\...` path.

This means the next blocker is no longer the remote-run stream handling, but
the trust boundary between `sync_up` completion and actual file availability on
the remote workstation.

## Technical Approach

The launcher should no longer assume that a successful archive upload and
extract automatically implies that all required campaign source paths are
available on the remote workstation.

After `Invoke-RemoteTarExtract(...)` completes, the launcher should run an
explicit remote verification pass for the campaign YAML paths and any other
required launch inputs before entering the `remote_run` stage.

The verification should:

1. check each resolved campaign config path on the remote repository clone;
2. fail early with a clear message that identifies the first missing remote
   path;
3. record the failure before the actual remote campaign command is launched;
4. keep the failure semantics in the local launcher, not buried inside the
   later remote training process.

If the verification shows that sync-up is incomplete, the launcher should stop
before `run_training_campaign.py` is invoked. That makes the failure shorter,
clearer, and easier to debug than the current delayed assertion inside the
remote training script.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
  Canonical remote launcher whose `sync_up` stage needs a remote file-existence
  verification pass before `remote_run`.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Canonical launcher note that may need a short note about the new remote
  source-path verification behavior.
- `doc/running/remote_training_campaign_status.json`
  Tracking file that should surface the earlier failure stage if sync
  verification fails.
- `doc/running/active_training_campaign.yaml`
  Active protected campaign state for the current `Track 1` `SVR` remote
  attempt.

## Implementation Steps

1. Add a remote source-path verification helper to
   `run_remote_training_campaign.ps1`.
2. Run that helper immediately after `Invoke-RemoteTarExtract(...)` and before
   building the remote run script.
3. Make the failure message name the missing remote campaign path explicitly.
4. Smoke-test the verification with the current `Track 1` remote launcher flow
   so the failure either moves earlier and becomes clearer, or the launch now
   proceeds into the actual remote run.
5. Update the remote launcher note if the operator-visible behavior changes.
