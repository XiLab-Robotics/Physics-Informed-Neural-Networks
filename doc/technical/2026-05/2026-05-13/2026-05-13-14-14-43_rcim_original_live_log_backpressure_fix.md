# RCIM Original Live Log Backpressure Fix

## Overview

The recovered-original RCIM unified launcher currently captures live child
process output in
`scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
by merging native stdout and stderr, printing each incoming line to the active
terminal, and appending the same text to multiple stage log files.

The new live-log capture introduced by commit `ba0dec42caa8188a617894334a6949f1235f3c12`
successfully persists the training output, but long retune stages can now stall
the operator terminal. The user observed two recurring trigger patterns:

- the integrated terminal freezes after opening the growing log file in VS Code;
- the integrated terminal freezes near the end of a verbose retune stage.

The current forward repro is:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Forward -Stage Retune -Families "DT"
```

The existing `retune.stdout.log` shows that the Python stage reaches its final
grid-search lines and records `Stage Exit Code | 0`, which strongly suggests
that the freeze is caused by the PowerShell live-log mirroring path rather than
by the recovered-original training logic itself.

## Technical Approach

Replace the current synchronous per-line mirroring path with a more robust
split between:

- authoritative persistent log capture;
- lightweight operator-facing terminal progress output.

The current implementation performs all of the following for each merged output
line from the native child process:

- write to the integrated terminal;
- append to `combined.log`;
- append again to `stdout.log`.

That design is vulnerable to backpressure because the child process can block on
its stdout pipe whenever the PowerShell consumer becomes slower than the
producer. Large verbose retune stages and an open VS Code log tab likely make
that bottleneck worse through terminal rendering and file-watcher overhead.

The fix should preserve complete stage logs while reducing the amount of
synchronous work done in the live output path. The implementation target is:

- capture the full merged native output into one authoritative log file with a
  buffered writer path;
- keep `stdout.log` as a compatibility artifact, but stop treating it as a
  second live append target during the hot path;
- mirror to the terminal only the lines that matter operationally, or mirror
  from a throttled or tailable path instead of from the child stdout pipe
  itself;
- tolerate non-line-perfect native output chunks such as adjacent `[CV]` and
  cross-validation summary text sharing the same final newline;
- preserve the existing stage exit code handling and automatic
  `Retune -> Eval -> Export` chaining contract.

This fix must not change the recovered-original training behavior, parameter
search grids, model export logic, or campaign artifact roots.

No subagent is planned for this fix. If subagent use becomes necessary later,
the planned scope and approval requirement must be recorded before delegation.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/campaigns/run_rcim_original_reference_training.md`
- `doc/scripts/campaigns/run_rcim_original_forward_reference_training.md`
- `doc/scripts/campaigns/run_rcim_original_backward_reference_training.md`

## Implementation Steps

1. Inspect the current shared PowerShell helper and isolate the synchronous
   operations that run on every child-process output line.
2. Refactor the stage log capture so one authoritative persistent log is written
   efficiently without duplicating live `Add-Content` work on the hot path.
3. Reduce terminal mirroring pressure by filtering, throttling, or otherwise
   decoupling operator-visible output from the raw persisted stream.
4. Preserve the existing stage result object shape and launcher summary
   contract.
5. Preserve compatibility log files while clarifying their semantics if the
   authoritative live path changes.
6. Validate with a narrow forward `DT` retune repro and confirm that the
   launcher no longer stalls when the log grows and when the stage completes.
7. Run PowerShell parser checks on touched launcher files.
8. Run Markdown warning checks on the touched documentation scope.
