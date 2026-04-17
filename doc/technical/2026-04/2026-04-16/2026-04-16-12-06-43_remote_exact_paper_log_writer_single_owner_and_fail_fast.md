# Remote Exact-Paper Log Writer Single Owner And Fail-Fast

## Context

The latest killed remote `SVR` reference-grid campaign did not spend ten hours
doing useful `GridSearchCV` work. The local orchestration log stayed unchanged
for hours, the remote workstation had no active `python` process, and CPU/RAM
utilization stayed near zero.

Review of the most recent remote launcher traces showed that the remote wrapper
was still able to reach `REMOTE_RUN_START`, but at least one earlier attempt
failed while opening the first per-run log file:

- `The process cannot access the file ... 01_track1_svr_reference_grid_amplitude_pair.log because it is being used by another process.`

The failing code path currently launches `conda run ...` and simultaneously
tees the exact same child output stream into the per-run log file with
`Tee-Object -FilePath $runLogPath -Append`, while the surrounding orchestration
already captures and persists the remote wrapper output separately.

## Problem

The remote exact-paper wrapper still violates strict single-writer ownership for
the per-run `.log` file.

Observed failure mode:

1. the remote wrapper creates the per-run log file up front;
2. the child exact-paper process or another launcher path keeps a handle open or
   races on the same file;
3. `Tee-Object` fails with `FileOpenFailure`;
4. the wrapper does not always collapse into a clean terminal failure marker;
5. the local operator session can remain alive and look "silent" even though no
   real remote training process is still active.

## Required Fix

The remote exact-paper wrapper must have exactly one owner for each per-run
`.log` file.

Required implementation rules:

- remove the current `Tee-Object -FilePath $runLogPath -Append` path from the
  remote exact-paper wrapper;
- write remote child output to the terminal stream only, letting the outer
  local remote-campaign logger keep the orchestration transcript;
- keep the canonical per-run log file by using the same streaming-writer
  strategy as the local exact-paper launcher, not a second independent writer
  attached to the same stream;
- if a per-run log cannot be opened or written, fail immediately with an
  explicit remote marker and non-zero exit code;
- if the child `conda run` process terminates, the wrapper must always emit a
  terminal `REMOTE_RUN_EXIT_CODE::<n>` marker before exiting;
- no remote launcher path may remain alive after the child process is gone.

## Behavioral Target

After the fix:

- a failed remote exact-paper run must fail fast and visibly;
- a silent remote session must mean the child is genuinely still running, not
  that the wrapper is hung after a logging failure;
- local operator output and remote per-run logs must match the behavior of the
  local exact-paper launcher as closely as possible;
- the wrapper must not require operator-side guesswork about whether compute is
  still happening.

## Validation

Validate with the real command:

```powershell
.\scripts\campaigns\run_track1_svr_reference_grid_search_repair_campaign_remote.ps1
```

Success criteria:

- no `FileOpenFailure` on the remote per-run log;
- `REMOTE_ACTIVE_*` lines continue to appear normally;
- if the first exact-paper run fails, the wrapper exits promptly with
  `REMOTE_RUN_EXIT_CODE::<nonzero>`;
- if the first exact-paper run keeps running, the remote workstation must show a
  live `python` process and non-trivial resource usage;
- the local orchestration log must continue to advance while the remote child is
  alive.
