# Track 1 Remote Campaign Total Progress Monitor

## Overview

The current exact-paper `Track 1` remaining-yellow-cell bundle is running on
the remote LAN workstation while the local wrapper state is stale because the
local PC was force-powered off.

The repository needs one operator-facing monitoring script that can be run
manually to inspect the real remote execution state without modifying the
campaign itself.

## Technical Approach

Add one repository-owned PowerShell status script under
`scripts/campaigns/track1/exact_paper/` that reports the live aggregate
progress of the prepared bundle launched through:

- `run_track1_remaining_yellow_cell_campaigns.ps1 -Remote`

The script should stay read-only and focus on:

1. current remote process and active config path;
2. family-by-family completed validation count versus expected count;
3. total completed validations across the full `660`-run bundle;
4. latest produced validation directory and latest campaign log;
5. duplicate run-name warning for the known early `SVM` retry edge case.

The script should query the remote workstation over SSH and print compact
operator-readable output that works even when the original local launcher
terminal no longer exists.

## Involved Components

- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Create one remote-monitor PowerShell script for the current remaining
   yellow-cell bundle.
2. Keep the script read-only: no campaign state edits, no process control, and
   no artifact mutation.
3. Add one short launcher note describing usage and the reported fields.
4. Validate PowerShell parsing and touched Markdown quality.
