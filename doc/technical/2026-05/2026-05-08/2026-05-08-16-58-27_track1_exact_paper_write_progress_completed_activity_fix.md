# Track1 Exact-Paper Write-Progress Completed Activity Fix

## Overview

The exact-paper remote wrapper currently prompts interactively for `Activity`
when the new sub-progress bar is completed. This blocks normal non-interactive
launcher execution during remote training runs.

## Technical Approach

Apply a narrow PowerShell wrapper fix that adds an explicit `-Activity` value
to every `Write-Progress ... -Completed` call associated with the exact-paper
sub-progress bar. Do not change the training protocol, search surface, or
launcher semantics.

## Involved Components

- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `doc/technical/2026-05/2026-05-08/README.md`
- `doc/README.md`

## Implementation Steps

1. Register this narrow launcher fix in the daily and canonical technical
   indices.
2. Add `-Activity "Active exact-paper substage"` to the sub-progress
   `Write-Progress -Completed` calls.
3. Re-parse the touched PowerShell wrapper and rerun Markdown QA on the touched
   Markdown scope.
