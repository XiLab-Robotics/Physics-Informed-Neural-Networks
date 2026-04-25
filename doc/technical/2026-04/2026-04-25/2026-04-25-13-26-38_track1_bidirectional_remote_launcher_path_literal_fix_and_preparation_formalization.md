# 2026-04-25-13-26-38 Track1 Bidirectional Remote Launcher Path Literal Fix And Preparation Formalization

## Overview

The prepared `Track 1` bidirectional original-dataset mega-campaign now uses
the remote exact-paper launcher path, but two bootstrap defects surfaced during
the first real remote launch.

The first defect was the use of fragile inline `python -c ...` calls inside the
PowerShell launch path. These failed on the remote workstation because of
PowerShell quoting and Conda argument parsing.

The second defect is narrower and happens later inside the remote
`run_track1_bidirectional_original_dataset_mega_campaign.ps1` launcher when it
materializes a temporary Python helper script. The script currently embeds
Windows paths through raw triple-quoted Python literals such as `r'''R:\'''`,
which is invalid Python syntax because a raw string cannot terminate with a
single trailing backslash.

This document formalizes both fixes as part of the durable campaign-preparation
pipeline instead of leaving them as one-off post-launch repairs.

## Technical Approach

The fix should harden the queue-bundle helper and the remote wrapper around one
simple rule: generated Python helper scripts must never rely on raw-string path
literals for Windows paths that may end with `\`.

The queue-bundle helper in the Track 1 launcher should serialize path inputs in
a Python-safe way, for example through JSON string emission or escaped regular
string literals, so both local paths and mapped remote paths like `R:\` remain
valid.

The earlier remote bootstrap repair should also be promoted from an ad hoc
launcher-only change into the canonical preparation/runtime contract:

- no inline `python -c ...` in this bidirectional mega-campaign path;
- use temporary Python script files for YAML parsing and remote Conda
  preflight checks;
- keep the campaign-preparation code aligned with the hardened remote launcher
  assumptions so future re-preparations emit the same stable contract.

The preparation formalization pass should therefore touch both the runtime
PowerShell scripts and the preparation-side notes so the remote launch path is
documented as using temporary Python helpers rather than inline code.

## Involved Components

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py`
- `doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Replace the raw triple-quoted Python path embedding in the queue-bundle
   helper with a Python-safe serialized representation that also works for
   `R:\`.
2. Verify that the local and remote bidirectional launchers no longer contain
   fragile inline `python -c ...` execution for queue parsing or remote Conda
   preflight.
3. Promote the launcher hardening into the preparation pipeline by updating the
   preparation script and launcher note to reflect the canonical remote runtime
   contract.
4. Re-run targeted PowerShell parsing and narrow launcher checks, then provide
   the exact relaunch command without committing.
