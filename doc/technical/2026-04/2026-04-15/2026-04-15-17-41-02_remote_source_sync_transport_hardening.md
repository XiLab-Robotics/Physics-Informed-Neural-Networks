# Remote Source Sync Transport Hardening

## Overview

The current remote `Track 1` `SVR` launcher now verifies source-config paths
correctly enough to expose the next real blocker: after `sync_up`, the remote
campaign directory contains the expected four YAML names, but the remote Python
runtime sees those entries as non-existent (`exists=False`, `is_file=False`)
while `README.md` in the same folder remains a normal file.

This means the current source-sync transport is creating broken or non-material
file entries on the remote workstation for at least part of the synchronized
campaign package. The path-resolution layer is no longer the primary problem;
the transport mechanism used to copy local source state to the LAN node is now
the primary failure surface.

## Technical Approach

The current `sync_up` path packages `scripts/`, `config/`, `doc/`, and
`requirements.txt` into one tar archive, uploads it, and extracts it on the
remote workstation with `tar.exe`.

The new evidence indicates that this transport is not reliable enough for the
Windows-to-Windows LAN workflow, at least for the campaign YAML payloads under
the remote clone.

The next fix should replace or narrow that sync-up transport so the launcher
materializes real source files on the remote workstation instead of broken
entries. The preferred direction is to align `sync_up` with the already more
robust `sync_down` philosophy:

1. avoid one opaque multi-root tar extraction for the full source payload;
2. copy the required source paths in smaller, explicit units;
3. verify each synced source file immediately after transfer on the remote
   node;
4. preserve repository-relative semantics so the remote training entrypoint can
   still consume the same config paths.

Practical candidate implementations include:

- path-by-path upload and remote materialization for the required source paths;
- smaller archive units per source root or per file instead of one large
  bundle;
- a remote copy strategy that writes a temporary file and then atomically
  replaces the destination path.

The key requirement is that the copied YAML files must become normal remote
files visible to both PowerShell and Python, not placeholder-like entries.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
  Canonical remote launcher whose `Invoke-RemoteTarExtract(...)` sync-up path
  currently produces broken remote YAML entries for this campaign.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Canonical operator note that should reflect the new sync-up transport if the
  launcher stops using the single-archive upload path.
- `doc/running/remote_training_campaign_status.json`
  Tracking surface that should continue to expose `sync_up` failures clearly if
  remote materialization still fails.
- `config/paper_reimplementation/.../2026-04-14_track1_svr_reference_grid_search_repair_campaign/`
  Immediate source payload whose four YAML files currently arrive as broken
  remote entries under the archive-based sync-up path.

## Implementation Steps

1. Replace the current archive-based `sync_up` transport in
   `run_remote_training_campaign.ps1` with a more explicit path-by-path source
   materialization flow suitable for the Windows LAN node.
2. Keep the sync-up scope limited to the approved source roots and preserve the
   current repository-relative destination layout on the remote clone.
3. Add a post-copy verification step that confirms each copied source file is a
   real remote file visible to Python before `remote_run`.
4. Retest the current `Track 1` `SVR` remote campaign launcher on the LAN node.
5. Update the launcher note if the transport model or operator-visible logging
   changes.
