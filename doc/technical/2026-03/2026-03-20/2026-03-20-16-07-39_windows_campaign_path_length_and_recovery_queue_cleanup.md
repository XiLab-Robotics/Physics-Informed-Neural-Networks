# Windows Campaign Path Length And Recovery Queue Cleanup

## Overview

The Wave 1 recovery campaign launcher exposed a Windows path-length failure in the campaign runner.

The issue is not the training logic itself. The generated per-run log path became too long because it combined:

- the repository root path;
- a long campaign output directory name;
- the `logs/` folder;
- a long queue-derived log filename.

Repeated failed launch attempts also left recovery YAML files in the queue, causing the launcher to process stale pending items together with newly enqueued ones.

This document defines the fix needed to keep the short launcher usable on Windows.

## Technical Approach

The fix should remain narrow and should not alter the current logging behavior.

1. Shorten generated campaign output directory names to a safe Windows-friendly length.
2. Shorten generated campaign log filenames while preserving traceability in the manifest and report.
3. Keep the existing live terminal logging and per-run campaign log files unchanged in behavior.
4. Make the recovery launcher clean only its own stale pending or running queue items before enqueuing the approved recovery configs again.

## Involved Components

- `scripts/training/run_training_campaign.py`
- `scripts/campaigns/wave1/run_wave1_structured_baseline_recovery_campaign.ps1`
- `doc/scripts/training/run_training_campaign.md`
- `doc/scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Add a bounded-length helper for campaign directory and log filenames in the campaign runner.
2. Use that helper when creating the campaign output folder and per-run log path.
3. Update the recovery launcher to remove only stale pending or running YAML files that belong to the recovery campaign.
4. Verify the short launcher in a dry run and then rerun the recovery campaign on Windows.
5. Keep the manifest and campaign report as the canonical source of full run identity so shorter filenames do not reduce traceability.
