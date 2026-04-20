# Exact-Paper Runner Progress Logging Standardization

## Overview

The current exact-paper campaign launcher now streams console output and writes
per-run logs in real time, but the underlying exact-paper validation runner can
still remain silent for hours during long `GridSearchCV` fits. This makes it
impossible to distinguish between a legitimately expensive search, a stalled
workflow phase, and a silent failure path inside the runner itself.

This document defines a narrow workflow-observability upgrade for the
exact-paper validation path so long-running campaigns emit frequent,
high-signal, line-oriented progress messages while preserving the current
paper-faithful training behavior.

## Technical Approach

The change should stay inside the exact-paper Python workflow and should not
rely on further launcher-side buffering work. The runner should expose progress
at the phase boundaries that currently hide the expensive work:

1. configuration and resolved search settings;
2. dataset build completion with target scope details;
3. per-family fit start and finish, including elapsed time;
4. paper-reference grid-search metadata before fit;
5. best-parameter and best-score summary immediately after fit;
6. evaluation progress and winner summary;
7. ONNX export progress and per-family export completion.

The logging should remain simple `print(...)` based, with explicit `[INFO]`,
`[DONE]`, and, if needed, `[WARN]` prefixes so the existing streaming launcher
can surface the lines immediately in both the terminal and the per-run log
file. The messages should be line-oriented and compact rather than verbose
dumps.

The fit path should additionally expose enough metadata to explain why a run is
slow:

- family name;
- search mode;
- target count;
- harmonic or target-name list;
- parameter-grid size;
- configured `n_jobs`;
- threadpool limit;
- elapsed time after the fit completes.

The implementation should avoid changing model selection semantics, search
space semantics, scoring semantics, or artifact formats beyond adding the extra
observability fields already compatible with the current workflow.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
  Main exact-paper validation entry point that currently only logs coarse
  phase-level status.
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
  Exact-paper family fitting, search, evaluation, and export support module
  where the long silent `GridSearchCV.fit(...)` phase currently occurs.
- `doc/running/active_training_campaign.yaml`
  Active campaign state file that remains relevant context because the logging
  upgrade is motivated by an active campaign, even though the implementation
  itself should not modify this file.
- `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`
  Already-fixed launcher helper that will surface the new runner-side lines
  live once the Python workflow emits them.

## Implementation Steps

1. Add runner-level progress prints before and after each major exact-paper
   phase in `run_exact_paper_model_bank_validation.py`, including resolved
   target scope and enabled family list details.
2. Add per-family fit diagnostics in
   `exact_paper_model_bank_support.fit_exact_family_model_bank(...)`,
   including search mode, target count, parameter-grid cardinality, `n_jobs`,
   and elapsed timing for each family.
3. Add narrow progress prints around evaluation and ONNX export so expensive
   post-fit phases are also visible in streaming logs.
4. Keep the messages compact and stable so they can be searched easily inside
   campaign logs and future results debugging.
5. Run a small exact-paper smoke check after implementation to verify that the
   new lines appear during execution without breaking the existing artifact
   workflow.
