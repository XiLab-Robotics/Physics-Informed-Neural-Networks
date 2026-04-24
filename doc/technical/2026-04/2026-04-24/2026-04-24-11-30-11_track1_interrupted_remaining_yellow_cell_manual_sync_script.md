# 2026-04-24-11-30-11 Track1 Interrupted Remaining Yellow Cell Manual Sync Script

## Overview

The interrupted `Track 1` remaining-yellow-cell overnight bundle cannot be
closed out yet because the local repository still has no synchronized `SVM`
artifacts from the long-running remote wave.

The user asked for one complete local PowerShell script that performs the
entire manual sync sequence from the local workstation, instead of pasting
individual ad hoc `ssh`, `scp`, and `tar` commands into the terminal.

The script should target only the interrupted `SVM` wave and should not touch
campaign closeout, benchmark refresh, or the deferred forward-only asset-root
migration.

## Technical Approach

Implement one repository-owned local helper under `scripts/campaigns/track1/`
or `scripts/training/` that:

1. reads the canonical remote assumptions from
   `doc/running/active_training_campaign.yaml`;
2. validates that the active campaign still matches
   `track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43`;
3. connects to the remote workstation through the existing SSH alias and uses
   uploaded temporary remote `.ps1` execution rather than inline `-Command`
   quoting, because the current ad hoc quoting path is brittle and already
   failed in practice;
4. creates remote tar payloads for:
   - the `SVM` campaign output directory;
   - the interrupted-wave exact-paper validation directories;
   - the interrupted-wave exact-paper per-run reports;
5. copies those tar payloads back to a local `.temp/` staging area;
6. extracts them into the local repository root;
7. optionally cleans up the temporary remote tar payloads;
8. prints a compact post-sync verification summary so the operator can confirm
   that the artifacts are now present locally before the partial closeout
   starts.

The script should stay deliberately narrow:

- `SVM` only;
- interrupted `remaining_yellow_cell` wave only;
- manual artifact recovery only.

It should not mutate:

- `doc/running/active_training_campaign.yaml`;
- benchmark reports;
- registries;
- closeout reports.

Those changes belong to the later partial closeout step after the sync
completes successfully.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/running/track1_interrupted_remaining_yellow_cell_manual_sync_checklist.md`
- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
- `scripts/training/build_track1_interrupted_remaining_yellow_cell_manual_sync_plan.py`
- new local sync helper script for the interrupted `SVM` wave
- matching launcher note under `doc/scripts/campaigns/`
- `.temp/manual_sync_track1_svm/`
- `output/training_campaigns/track1/exact_paper/forward/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- `doc/reports/analysis/validation_checks/`

## Implementation Steps

1. Add one local PowerShell helper that encodes the remote PowerShell blocks
   safely and avoids inline command-quoting failure modes.
2. Make the helper pull the three required artifact groups for the interrupted
   `SVM` wave:
   campaign output, validation directories, and per-run reports.
3. Stage the downloaded tar files under local `.temp/` and extract them into
   the repository root.
4. Emit a short verification summary showing local counts and the key target
   directories now present after extraction.
5. Add the matching launcher note under `doc/scripts/campaigns/`.
6. Run PowerShell parse validation and touched-Markdown QA.
7. Stop and wait for the user's next instruction before performing the partial
   closeout.
