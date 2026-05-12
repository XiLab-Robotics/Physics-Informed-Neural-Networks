# RCIM Original Launcher Live Log Capture Fix

## Overview

The recovered-original RCIM PowerShell launcher currently reports three stage
log files:

- `logs/<stage>.stdout.log`
- `logs/<stage>.stderr.log`
- `logs/<stage>.combined.log`

However, recent runs show that these files do not contain the Python training
stage's intermediate output. For example,
`output/training_campaigns/rcim_original/backward/2026-05-12-18-22-07__bw_eval_bundle/logs/eval.stdout.log`
contains only launcher metadata, the PowerShell transcript header/footer, and
the stage completion lines.

This contradicts the existing launcher contract. The shared helper currently
states that the combined transcript is the authoritative live log surface, and
the launcher notes state that each stage writes stdout, stderr, and combined
logs.

## Technical Approach

Replace the current `Start-Transcript`-based capture path in
`scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`.

The current design runs the environment-local `python.exe` in foreground mode
and expects `Start-Transcript` to capture native Python stdout/stderr. On
Windows PowerShell 5 this does not reliably capture output from native child
processes, so the operator can see progress in the terminal while the log files
remain incomplete.

The fix should use explicit native-process output mirroring instead:

- run the resolved Python command in unbuffered mode through a PowerShell
  pipeline that merges native stdout/stderr with `2>&1`;
- mirror the merged stream to the live console as it arrives;
- append the same live stream to `combined.log`;
- keep `stdout.log` as a compatibility mirror of the same stream;
- keep `stderr.log` for launcher metadata and completion compatibility, without
  claiming it is a reliable split native stderr stream;
- preserve the resolved command preview, stage metadata, exit-code handling, and
  launcher summary contract;
- preserve `-PrintOnly` behavior;
- keep the log format simple text so existing tailing and artifact inspection
  workflows continue to work.

The implementation should not change the recovered-original training,
evaluation, export, retune grids, model parameters, dataset selection, or output
artifact layout.

The main tradeoff is that reliable split stdout/stderr capture is not preserved
in this Windows PowerShell 5 launcher path. That tradeoff is acceptable here
because the current transcript path fails the persistent-log contract entirely,
while the combined log and compatibility stdout log can still mirror child
output to the active terminal in real time.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `doc/scripts/campaigns/run_rcim_original_forward_reference_training.md`
- `doc/scripts/campaigns/run_rcim_original_backward_reference_training.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`

No subagent is planned for this fix. If subagent use becomes necessary later,
the task boundary and approval requirement must be recorded before requesting
approval.

## Implementation Steps

1. Refactor `Invoke-RcimOriginalPythonStage` to replace `Start-Transcript` with
   explicit process stdout/stderr capture.
2. Keep the same stage result object fields so the unified launcher summary
   remains compatible.
3. Update the compatibility log metadata to describe the new mirrored live-log
   behavior instead of the failed transcript behavior.
4. Update the launcher notes to clarify that `combined.log` is authoritative,
   `stdout.log` is a compatibility mirror, and `stderr.log` is not a reliable
   split native-stderr stream in this launcher mode.
5. Run a narrow `-PrintOnly` command to verify argument construction remains
   unchanged.
6. Run a short real stage, preferably `Backward` plus `Eval` plus `HGBM`, and
   verify that the Python `[INFO]` and `[PROGRESS]` lines appear in both the
   terminal and the relevant log files.
7. Run PowerShell parser checks on touched `.ps1` files.
8. Run Markdown warning checks on all touched Markdown files.
