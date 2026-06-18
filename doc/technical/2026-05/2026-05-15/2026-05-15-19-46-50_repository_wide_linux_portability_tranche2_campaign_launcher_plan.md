# Repository-Wide Linux Portability Tranche 2 Campaign Launcher Plan

## Overview

This document starts the second repository-wide Linux portability tranche after
the baseline inventory commit. It records the remaining work as an explicit
backlog and scopes the next implementation pass to campaign launcher coverage.

The current portability backlog is:

- port or classify `97` PowerShell scripts that still have no Linux
  equivalent;
- add `--linux` / `--windows` to the remaining Python CLI-like scripts that
  still lack platform flags;
- finish report, PDF, closeout, and presentation workflow coverage;
- classify Windows-only LAN or workstation workflows explicitly instead of
  leaving them as missing;
- add non-training dry-run checks where launchers would otherwise start
  training immediately;
- verify the final state on the real Unimore Aries Linux clone before claiming
  repository-wide Linux readiness;
- keep documentation and Sphinx portal pages aligned after each tranche.

The first implementation item from this backlog is:

- port the protected campaign launcher layer to Bash equivalents and update
  the inventory after each batch.

No subagent is planned for this tranche. If the launcher scope is later split
across independent domains, subagent use must be proposed and approved
explicitly before launch.

## Technical Approach

The campaign launcher tranche should prioritize reusable launcher infrastructure
before duplicating dozens of one-off wrappers. The guiding rule is:

- every runnable `.ps1` campaign launcher should either have an adjacent `.sh`
  equivalent, call a shared Bash helper, or be explicitly marked
  Windows-only with a documented Linux-safe replacement.

The first Bash coverage should target the files that unlock the largest
campaign surface:

1. protected Track 1 exact-paper launch stack;
2. shared campaign streaming helper behavior;
3. Wave 1 launcher surface;
4. recovered-original RCIM launcher surface;
5. older Track 1 family wrappers and watcher/sync scripts.

For launchers that start training, every Bash equivalent must expose a
`--dry-run` mode that resolves paths, selected configs, commands, and logs
without launching model training.

## Involved Components

- Protected campaign state:
  - `doc/running/active_training_campaign.yaml`

- Protected Track 1 campaign launcher files:
  - `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
  - `scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.ps1`
  - `scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.ps1`
  - `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`
  - `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`

- Existing Linux launcher from tranche 1:
  - `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh`

- Candidate new Bash helper surfaces:
  - `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh`
  - `scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.sh`
  - selected adjacent `.sh` siblings for campaign `.ps1` launchers

- Inventory and documentation:
  - `scripts/tooling/linux_portability/build_script_portability_inventory.py`
  - `doc/reports/analysis/utilities/linux_script_portability/[2026-05-15]/script_portability_inventory.md`
  - `doc/reports/analysis/utilities/linux_script_portability/[2026-05-15]/script_portability_inventory.yaml`
  - `doc/scripts/campaigns/`
  - `doc/scripts/tooling/linux_portability/build_script_portability_inventory.md`
  - `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Re-read `doc/running/active_training_campaign.yaml`.
   Confirm the campaign status and protected-file list before touching any
   protected launcher or launcher note.

2. Request protected-file authorization before implementation.
   This tranche will modify protected Track 1 launcher files and related
   launcher documentation, so it must not proceed without explicit protected
   scope approval.

3. Create the shared Bash launcher helper.
   Implement a small Bash helper that mirrors the current PowerShell streaming
   behavior where practical:
   - resolve repository root from the script location;
   - resolve Conda through `conda`, `CONDA_EXE`, or explicit command;
   - create log directories;
   - run `conda run --no-capture-output`;
   - tee complete output to the per-run log;
   - preserve exit codes;
   - support dry-run command printing.

4. Refactor the existing Track 1 Bash launcher to use the shared helper.
   Keep its current queue selection and `--linux` pass-through behavior while
   reducing duplicated subprocess/logging logic.

5. Add a Linux local invocation helper for exact-paper campaign packages.
   Provide the Bash analogue of `invoke_exact_paper_campaign_local.ps1` for
   campaign wrappers that execute a list of config files through a Python
   runner.

6. Port the first protected Track 1 launcher batch.
   Start with the bidirectional paper-faithful launcher stack because it is the
   current canonical campaign surface and already has one Bash entry point.

7. Regenerate the portability inventory.
   The expected immediate improvement is a lower
   `missing_linux_equivalent` count and additional `linux_equivalent_present`
   rows for the protected Track 1 stack.

8. Update launcher documentation.
   Add Bash examples beside PowerShell examples in `doc/scripts/campaigns/`
   for every launcher touched in this tranche.

9. Verify without training.
   Required checks:
   - `bash -n` on every new or touched `.sh`;
   - PowerShell parser check on touched `.ps1` if edited;
   - Python compile on touched Python helpers or inventory tooling;
   - `--help` and `--dry-run` for touched Bash launchers;
   - regenerated inventory;
   - Markdown style check and Markdownlint on touched Markdown;
   - Sphinx build if `doc/guide/` or portal-scoped docs change.

10. Stop before commit.
    Report the updated inventory counts and the exact file list. Commit only
    after explicit approval.

CRITICAL WARNING: this tranche intentionally targets files currently listed in
`doc/running/active_training_campaign.yaml` under `protected_file_list`.
Implementation must wait for explicit user approval of the protected file
scope.
