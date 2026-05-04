# RCIM Original Unified Launcher And Best-Parameter Flow

## Overview

This document plans the unification of the recovered-original RCIM
paper-reference PowerShell launchers into one branch-aware operator entrypoint.
The goal is to make the `forward` and `backward` branches operationally
analogous, reduce stage-name ambiguity, and formalize a repository-owned best
hyperparameter persistence flow that can be reused across retune, evaluation,
and export stages.

## Technical Approach

The implementation will replace the current split launcher surface with one
canonical PowerShell entrypoint that accepts a branch selector and a normalized
stage selector. The proposed public CLI surface is:

- `-Branch Forward|Backward|Both`
- `-Stage Original|Retune|Eval|Export|LoadBest`
- `-NoEval`
- `-NoExport`
- `-BestParameterSummaryPath`

The unified behavior will follow these rules:

- `Original`:
  - `Forward`: use the recovered-original built-in tuned hyperparameter map
    that currently powers the `v18`-style replay, then automatically continue
    to `Eval` and `Export` unless explicitly suppressed.
  - `Backward`: do not run a fake `v18` replay. Instead, print a clear operator
    message that original paper-tuned backward hyperparameters are not
    available, then exit cleanly without pretending to have a valid tuned map.
- `Retune`:
  - run the recovered-original retune stage;
  - automatically continue to `Eval` and `Export` unless `-NoEval` and/or
    `-NoExport` are explicitly set;
  - use the just-generated `summaryBestParameter+...csv` as the parameter
    source for the downstream stages.
- `Eval`:
  - run the held-out replay/evaluation stage using either:
    - an explicit `-BestParameterSummaryPath`, or
    - a stored repository-owned best-parameter registry entry if one exists.
- `Export`:
  - run the full-dataset model export stage using the same parameter source
    resolution logic as `Eval`.
- `LoadBest`:
  - skip retuning and run the equivalent of `Eval` plus optional `Export` using
    the current repository-owned stored best-parameter registry entry.

The operator defaults will be adjusted so that `LoadBest` becomes the preferred
branch-aware tuned replay entrypoint whenever a stored best-parameter entry is
already present. If no stored best entry exists for the requested branch and
family set, the launcher will guide the operator toward `Retune` instead of
silently falling back to mismatched defaults.

Best-parameter persistence will be moved into a repository-owned config file,
preferably a YAML registry under a stable non-reference path. After each retune
run, the launcher will compare the newly produced family-wise best result
against the currently stored entry for the same branch and family. If the new
result is better according to the chosen canonical metric, the stored entry
will be updated.

The comparison rule must be explicit and deterministic. The initial plan is to
use the same summary metric already emitted by the retune flow, with
lower-is-better semantics, and to store both the selected parameter payload and
the supporting metric provenance in the registry entry.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/scripts/campaigns/run_rcim_original_forward_reference_training.md`
- `doc/scripts/campaigns/run_rcim_original_backward_reference_training.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/recovered_original_workflow.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Introduce a unified RCIM original paper-reference launcher under
   `scripts/campaigns/paper_reference/rcim_original/` and redefine the public
   branch/stage CLI surface around `Forward|Backward|Both` and
   `Original|Retune|Eval|Export|LoadBest`.
2. Refactor the shared launcher helper so branch-aware stage chaining,
   best-summary handoff, stage skipping, and branch-specific operator messages
   are centralized instead of split between two wrappers.
3. Decide the repository-owned best-hyperparameter registry path and schema,
   then add read/write/update support for family-wise stored tuned entries.
4. Wire retune completion so it can automatically feed the downstream `Eval`
   and `Export` stages through the generated best-summary artifact unless the
   operator explicitly disables those stages.
5. Rename user-facing stage terminology in the launcher and its documentation
   from `PaperEval` / `paper_export` language to the normalized operator-facing
   `Eval` / `Export` vocabulary, while preserving the underlying Python mode
   mapping where needed.
6. Update the workflow documentation, launcher notes, and user guide so the
   new branch/stage contract, best-parameter precedence rules, and backward
   `Original` limitation are documented clearly.
7. Verify the new launcher in print-only mode and with at least one narrow real
   branch-specific smoke run to confirm stage chaining, logging, and best-path
   resolution.
