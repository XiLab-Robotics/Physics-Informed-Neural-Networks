# Campaign Runner Colorama Shutdown Fix

## Overview

The completed best-training logging-validation campaign exposed a shutdown bug in the campaign runner:

- `ValueError: I/O operation on closed file`

The traceback shows the failure path clearly:

1. `colorama` executes its `atexit` reset callback;
2. that callback writes `Style.RESET_ALL` to the active stdout wrapper;
3. the campaign runner tee stream still receives the write call;
4. the tee stream attempts to mirror the message into a log file that has already been closed.

The bug appears after successful campaign completion, so it does not invalidate training results. However, it leaves the terminal shutdown path noisy and makes the logging workflow look unfinished.

## Technical Approach

The fix should stay narrow and should not change the successful campaign behavior that was already validated.

The main idea is:

1. keep the terminal stream write active as long as the underlying terminal is available;
2. stop writing to the mirrored log file once the log file is closed or detached;
3. make the tee wrapper tolerant to late shutdown writes triggered by external `atexit` handlers such as `colorama`.

The expected implementation direction is:

- extend `TeeTerminalStream` with a safe log-write guard;
- catch `ValueError` or closed-file states when writing or flushing the mirrored log file;
- treat those late log-file failures as ignorable during shutdown instead of letting them surface to the terminal;
- preserve normal live terminal output and normal log mirroring during the actual training run.

This approach is preferable to trying to disable `colorama` shutdown behavior globally, because the real bug is in the runner wrapper lifecycle rather than in `colorama` itself.

## Involved Components

- `training/run_training_campaign.py`
  The tee stream is implemented here and is the direct source of the shutdown exception.
- `README.md`
  Main project document that must reference this technical note.
- `doc/reports/campaign_results/2026-03-14-02-08-12_best_training_logging_validation_campaign_results_report.md`
  The completed campaign report already documents the issue and should remain consistent with the eventual fix.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. After user approval, harden `TeeTerminalStream.write()` and `TeeTerminalStream.flush()` against closed-log-file access.
3. Keep terminal writes unchanged while making mirrored log writes conditional on the log file still being usable.
4. Run a focused verification of the runner shutdown path with a short campaign command.
5. Confirm that campaign completion no longer prints the `colorama` shutdown traceback.
