# Remote Campaign Marker Emission And Capture Alignment

## Overview

The remote launcher no longer fails on the `Track 1` campaign YAML path itself
after the short-path execution fix. The latest remote attempt now gets through:

1. remote preflight;
2. source sync-up;
3. post-sync source verification;
4. remote campaign launch.

The remaining failure is later and narrower:

- the launcher exits with
  `Remote campaign completed without returning a manifest path marker`;
- the previous `Source Config Path does not exist` failure is gone.

So the current blocker is no longer path materialization. It is the contract
between the remote run wrapper and the local marker parser:

- either the remote run script is not printing the expected
  `REMOTE_CAMPAIGN_*` lines;
- or those lines are emitted but not captured into the local
  `output_line_list`.

## Technical Approach

The fix should stay inside
`scripts/campaigns/run_remote_training_campaign.ps1` and focus on the final
marker-emission stage of the remote run.

The launcher should:

1. make the remote run script print an explicit start marker before launching
   the training campaign;
2. print an explicit marker immediately after the training command returns,
   including the remote exit code;
3. print the resolved campaign output directory, manifest path, and sync
   manifest path with unambiguous marker lines after the post-run resolution
   step;
4. if those markers are still absent, emit a compact remote diagnostic summary
   before returning so the local wrapper fails with actionable evidence rather
   than an empty marker parse.

On the local side, the launcher should preserve the current marker parser but
also capture a small tail sample from `remoteOutputLineList` when marker
extraction fails, so the failure surface records what the remote side did emit.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
  Canonical SSH-backed remote launcher whose `remote_run` stage currently
  completes without returning the required `REMOTE_CAMPAIGN_*` markers to the
  local parser.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Canonical launcher note that may need a short update if the remote run now
  emits additional lifecycle markers or diagnostic lines.
- `doc/running/remote_training_campaign_status.json`
  Tracking file that should become more informative if marker extraction still
  fails.

## Implementation Steps

1. Add explicit remote lifecycle markers around the `run_training_campaign.py`
   invocation and around the post-run manifest-resolution block.
2. Add compact diagnostic marker lines for the remote output directory search
   and manifest-generation phase.
3. Update the local failure path so missing-marker failures record the last
   emitted remote lines.
4. Retest the current `Track 1` `SVR` remote launcher on the LAN node.
5. Update the launcher note if the operator-visible marker output changes.
