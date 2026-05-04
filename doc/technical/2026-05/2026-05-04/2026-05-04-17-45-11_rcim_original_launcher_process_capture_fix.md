# RCIM Original Launcher Process Capture Fix

## Overview

This document plans the repository-owned fix for the shared PowerShell
launcher wrapper used by the recovered original RCIM paper-reference
campaigns.

The current bug is reproducible on both launchers:

- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`

Observed failure mode:

- the underlying `training_models.py` stage completes successfully when run
  directly through `conda run`;
- the shared PowerShell wrapper exits with non-zero status;
- the stage log files remain empty;
- the launcher does not transition from `paper_eval` to `paper_export`;
- the final `launcher_summary.json` is never written.

## Technical Approach

The fix will target the shared helper:

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`

The goal is to keep the existing operator-facing commands unchanged while
repairing the process-capture layer.

The most likely fault surface is the current asynchronous
`BeginOutputReadLine` / `BeginErrorReadLine` event-based wrapper around:

- `cmd.exe /d /c`
- `conda.bat run -n ...`
- `python -B training_models.py ...`

The implementation will replace or materially simplify that capture path so
that:

1. the Python subprocess exit code is preserved correctly;
2. stdout and stderr are written to the stage log files reliably;
3. the wrapper no longer reports a failure when the underlying stage actually
   completed;
4. the launcher can continue automatically into `paper_export`;
5. the same fix applies to both the forward and backward launchers because
   they share the helper.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `doc/scripts/campaigns/run_rcim_original_forward_reference_training.md`
- `doc/scripts/campaigns/run_rcim_original_backward_reference_training.md`
- `doc/guide/project_usage_guide.md`

Protected campaign state acknowledged and intentionally left untouched:

- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Refactor the shared launcher helper so stdout/stderr capture does not rely
   on the currently broken event-drain pattern.
2. Re-run the forward launcher to confirm:
   - `paper_eval` completes;
   - `paper_export` starts automatically;
   - stage logs are populated;
   - `launcher_summary.json` is written.
3. Re-run the backward launcher in `-PrintOnly` and, if needed, one narrow
   real stage to confirm the shared fix also covers the backward surface.
4. Update the launcher notes and usage guide if the implementation details or
   operational guarantees changed.
