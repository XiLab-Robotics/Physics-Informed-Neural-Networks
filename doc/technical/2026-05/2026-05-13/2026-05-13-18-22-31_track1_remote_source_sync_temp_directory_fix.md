# Track 1 Remote Source Sync Temp Directory Fix

## Overview

The Track 1 paper-faithful remote launcher now passes the remote dependency
preflight, including `scikit-elm`, but fails before training starts while
syncing the local source archive to the remote workstation.

The failure occurs during the `scp` upload to:

```text
C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\.temp\remote_training_source_sync.tar
```

The launcher creates the remote `.temp` directory inside the later extraction
script, after the archive upload has already succeeded. On a clean remote
workspace this ordering is wrong: `scp` cannot create the destination file
because the parent `.temp` directory does not exist yet.

The campaign should not be treated as running after this failure because the
error happens before the remote exact-paper training launcher starts.

## Technical Approach

Patch the remote source-sync workflow so the destination directory exists
before the source archive upload.

The durable fix is to add a small remote directory preparation step in
`Invoke-RemoteTarExtract` before this line:

```powershell
& scp $localArchivePath "${RemoteHostAlias}:${remoteScpArchivePath}"
```

The step should create both:

- the remote staging root used by temporary helper scripts; and
- the repository-local `.temp` directory that receives
  `remote_training_source_sync.tar`.

The existing extraction script can keep its defensive `New-Item -Force` calls,
but the upload path must no longer depend on them.

## Involved Components

- `scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.ps1`
  Remote exact-paper wrapper that builds the source archive, uploads it over
  `scp`, extracts it on the remote repository, and then launches the canonical
  exact-paper campaign launcher.
- `doc/running/active_training_campaign.yaml`
  Persistent campaign state. Since the latest attempt failed before training
  began, it should be returned from `running` to `prepared` with an
  interruption note after approval.
- `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`
  Launcher note, only if the operator-facing remote troubleshooting behavior
  needs to mention the clean-workspace `.temp` preparation.

No subagent is planned for this change.

## Implementation Steps

1. Wait for explicit approval because the remote launcher and active campaign
   state are protected campaign files.
2. Update `Invoke-RemoteTarExtract` so it creates the remote destination
   `.temp` directory before `scp`.
3. Return `doc/running/active_training_campaign.yaml` to `prepared`, clear
   `started_at`, and record that the latest failed attempt stopped before
   training at remote source-sync upload.
4. Parse-check the touched PowerShell launcher.
5. Parse-check the active campaign YAML.
6. Run Markdown QA if any Markdown files beyond this technical document and
   indexes are touched.
7. Provide the corrected relaunch command and stop without launching training.
