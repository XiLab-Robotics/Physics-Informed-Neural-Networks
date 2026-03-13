# Campaign Training Terminal Logging Alignment

## Overview

The mixed training campaign exposed a usability regression in `training/run_training_campaign.py` compared to direct execution of `training/train_feedforward_network.py`.

The current campaign runner launches each training job through a subprocess with captured stdout. In practice this causes three visible issues:

- the terminal can stay silent at the beginning of a run because the child process no longer writes to an interactive line-buffered terminal;
- Unicode progress-bar glyphs and table separators are decoded incorrectly in the parent terminal and in the stored campaign logs;
- Lightning progress bars are flattened into repeated noisy prints instead of behaving like the direct single-run terminal workflow.

The user requested campaign execution that shows the same terminal logging quality as the single training script, while still preserving campaign-level logs and giving a clear indication of overall campaign progress.

## Technical Approach

The implementation should preserve the current queue lifecycle and reporting artifacts, but change how each training run is executed and mirrored to disk.

1. Replace the current subprocess-only training dispatch with a direct Python callable dispatch for supported model types.
   - For the current `feedforward` campaign flow, the runner can call `train_feedforward_network(config_path=...)` directly.
   - This keeps the training loop inside the same terminal session and avoids the pseudo-noninteractive stdout behavior introduced by `subprocess.PIPE`.
2. Introduce a lightweight terminal tee context for campaign runs.
   - Mirror `sys.stdout` and `sys.stderr` to the per-run campaign log file while delegating terminal-facing behavior such as `isatty()` to the original console stream.
   - Flush immediately so early initialization prints remain visible.
   - Keep the console stream authoritative so Lightning and `tqdm` continue to behave like a direct run.
3. Preserve per-run and campaign-level reporting.
   - Keep the existing queue transitions, manifest generation, execution report generation, and output artifact discovery unchanged.
   - Continue storing one log file per queued configuration under `output/training_campaigns/.../logs/`.
4. Add explicit campaign progress messaging that does not fight the Lightning progress bars.
   - Print a compact campaign status block before and after each run, including `current/total`, run name, source config, and cumulative completed/failed counts.
   - Prefer a static text or ASCII progress indicator updated between runs rather than a second live nested `tqdm` bar, because Lightning already owns the interactive training bars.
5. Normalize terminal encoding and error propagation for the remaining wrapper layer.
   - Ensure the campaign log file is always written as UTF-8.
   - Capture unexpected runner exceptions in the same mirrored log stream so failures stay diagnosable.

This design gives the campaign runner the same terminal surface as the single training script, removes the current buffering and mojibake path, and adds campaign-level visibility without introducing a second competing live progress renderer.

## Involved Components

- `training/run_training_campaign.py`
  Main campaign runner that currently launches training through a piped subprocess and must be updated to dispatch supported trainers directly.
- `training/train_feedforward_network.py`
  Existing single-run training workflow whose terminal behavior should remain the source of truth for campaign execution.
- `doc/scripts/training/run_training_campaign.md`
  Script documentation that must describe the new direct terminal logging behavior and the campaign progress summary.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide that must be updated because campaign execution changes visible runtime behavior.
- `README.md`
  Main project document that must reference this technical note.

## Implementation Steps

1. Refactor the campaign runner model-dispatch layer from entrypoint paths to callable training handlers for supported model types.
2. Add a reusable tee stream/context manager that mirrors stdout and stderr to both terminal and campaign log file with immediate flush behavior.
3. Wrap each campaign run in that tee context so the underlying trainer prints directly to the active terminal while still generating the stored log file.
4. Replace the current subprocess-specific execution metadata with equivalent in-process timing, exception, and artifact handling.
5. Add compact campaign progress summaries before and after each run, including `queue_index/queue_total` and cumulative status counts.
6. Update `doc/scripts/training/run_training_campaign.md` and `doc/guide/project_usage_guide.md` to reflect the revised runtime behavior.
7. Verify the campaign runner with a short feedforward configuration and confirm:
   - early startup messages appear immediately;
   - Lightning progress bars render correctly in the terminal;
   - campaign log files are still created;
   - queue transitions and reports still update correctly.
