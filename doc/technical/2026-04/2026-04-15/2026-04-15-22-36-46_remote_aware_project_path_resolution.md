# Remote-Aware Project Path Resolution

## Overview

The remote launcher is now far enough along that the remaining blocker is no
longer in the SSH wrapper itself.

Current verified state:

- the LAN launcher reaches `remote_run`;
- the short execution alias `R:\` is active;
- the remote source verification step succeeds for all required campaign YAML
  files and the planning report;
- `run_training_campaign.py` still fails at
  `enqueue_configuration_paths(...)` with:
  `Source Config Path does not exist`.

The critical observation is that the failing path printed by the training
entrypoint is not the short `R:\...` path. It is the fully expanded long path
under:

- `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\...`

That means the launcher-side short-path fix is working, but the Python
repository path resolver is undoing it.

## Technical Approach

The root cause is the current repository-wide helper:

- `scripts/datasets/transmission_error_dataset.py`
  `resolve_project_relative_path(path_value: str | Path) -> Path`

which currently calls `.resolve()` for both:

1. already absolute paths;
2. project-relative paths joined under `PROJECT_PATH`.

On the LAN node, when the process runs from the short alias `R:\`, the later
`.resolve()` expands that short path back to the long physical Windows path.
That reintroduces the exact path-length problem we just avoided at the launcher
level.

The fix should make project-path resolution remote-aware and short-path-safe:

1. keep normal absolute/project-relative behavior for local workflows;
2. avoid expanding a valid short Windows execution alias into its long backing
   path when doing so would break exact-paper campaign execution on the LAN
   node;
3. preserve `Path`-based semantics for the rest of the training stack.

The cleanest approach is to update `resolve_project_relative_path(...)` so it
returns normalized absolute paths without forcing a dereference that destroys an
intentional short alias such as `R:\`.

## Involved Components

- `scripts/datasets/transmission_error_dataset.py`
  Defines the canonical `resolve_project_relative_path(...)` helper currently
  used across dataset, training, and validation code paths.
- `scripts/training/run_training_campaign.py`
  Fails in `enqueue_configuration_paths(...)` because it relies on that helper
  before asserting source-config existence.
- `scripts/training/shared_training_infrastructure.py`
  Also depends on the same resolver and must stay behaviorally compatible after
  the fix.
- `doc/guide/project_usage_guide.md`
  May need a short note only if the path-resolution behavior becomes
  user-visible or configurable, which is not expected for the first fix pass.

## Implementation Steps

1. Update `resolve_project_relative_path(...)` to avoid unwanted expansion of
   valid short execution aliases during remote LAN execution.
2. Check the immediate call sites in `run_training_campaign.py` and
   `shared_training_infrastructure.py` to ensure the adjusted resolver remains
   compatible with local workflows.
3. Run a focused smoke check on local path-resolution behavior.
4. Retest the current `Track 1` `SVR` remote launcher on the LAN node.
5. If the training queue now advances beyond source-config enqueue, stop there
   and reassess campaign runtime behavior before making further launcher
   changes.
