# Remote Exact-Paper Wrapper Missing Output Root Compatibility Fix

## Overview

The reused remote exact-paper wrapper fails before remote execution starts when
the bidirectional original-dataset mega-campaign launcher passes a campaign
output root that does not yet exist locally.

The current shared helper resolves several repository-relative paths through
`Resolve-Path`, which is valid for already materialized inputs such as configs
and planning reports, but invalid for future output directories that are
supposed to be created only during campaign execution.

This blocks the remote launch of the newly repackaged bidirectional
mega-campaign even though the queue and remote metadata are otherwise valid.

## Technical Approach

The fix should keep the shared remote wrapper reusable while distinguishing two
path categories:

- existing repository inputs that must be validated through `Resolve-Path`;
- repository-relative output roots that may not exist yet and therefore must be
  normalized without requiring filesystem presence.

The preferred repair is:

- add a helper that converts a repository-relative path to canonical Windows
  relative form without `Resolve-Path`;
- use that helper only for output roots that may not exist yet;
- keep `Resolve-Path` for required existing inputs so the preflight still fails
  early on real missing source files.

## Involved Components

- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md`
- `doc/guide/project_usage_guide.md` if the user-facing launcher note changes
  materially

## Implementation Steps

1. Patch the shared remote wrapper so non-existent output roots are converted
   to repository-relative form without `Resolve-Path`.
2. Keep source-path validation strict for inputs that must exist before launch.
3. Re-run a remote-launch bootstrap check up to the point before real remote
   execution work begins.
4. Run Markdown QA on touched documentation and rebuild Sphinx if portal-facing
   docs change.
