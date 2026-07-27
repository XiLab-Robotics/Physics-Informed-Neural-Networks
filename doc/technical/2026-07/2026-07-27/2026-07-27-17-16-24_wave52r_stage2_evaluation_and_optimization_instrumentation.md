# Wave 5.2R Stage 2 Evaluation And Optimization Instrumentation

## Overview

Stage 2 implements the reusable instrumentation required to observe how
data-fit, curve-shape, harmonic, derivative, and future physics losses interact
before additional physical formulations are trained. The scope is restricted
to the `polished_dataset`, setpoint-input, forward-surface contract frozen in
Stage 0.

This stage does not execute a training campaign. It implements and validates
the instrumentation on deterministic synthetic tensors so later campaign
packages can adopt it without changing the canonical split or silently
altering an accepted reference.

The technical document is automatically approved under the user's standing
authorization for all sixteen Wave 5.2R stages. No subagent is planned because
repository instructions require separate explicit approval before delegation.

## Technical Approach

The implementation will add an opt-in PyTorch utility layer that operates on a
dictionary of named differentiable loss components and a declared set of
shared parameters. Every component will carry an explicit unit-normalization
scale, fixed control weight, and activation schedule.

The utility will:

1. record raw and normalized component values plus exponential moving
   averages;
2. obtain per-component gradients with functional `torch.autograd.grad`
   without mutating parameter gradient buffers;
3. report per-component gradient norms, pairwise cosine similarity, and the
   optimizer update-to-parameter ratio;
4. implement fixed, manually normalized, gradient-statistics,
   ReLoBRaLo-style relative-progress, and main-loss-preserving conflict-aware
   adapters;
5. implement staged activation and parameter freeze-unfreeze schedules;
6. expose deterministic seed, algorithm, dataloader-generator, and batch
   fingerprint helpers;
7. serialize diagnostics into inspectable CSV and JSON evidence.

Conflict-aware behavior will preserve the declared main data loss and project
only conflicting auxiliary gradients. The implementation will not claim that
adaptive optimization can rescue an invalid or unobservable physical
equation.

## Involved Components

- `scripts/training/physics_guided_optimization_instrumentation.py`
  - named loss definitions;
  - loss and gradient diagnostics;
  - weighting adapters;
  - conflict-aware gradient composition;
  - staged activation and freeze schedules;
  - deterministic execution helpers.
- `scripts/analysis/wave_5_2r/stage2_evaluation_and_optimization_instrumentation/`
  - deterministic validation harness;
  - exit-gate assertions;
  - machine-readable evidence generation.
- `output/analysis/wave_5_2r/stage2_evaluation_and_optimization_instrumentation/`
  - control matrix;
  - diagnostic records;
  - exit-gate summary.
- `doc/scripts/training/` and `doc/scripts/analysis/`
  - implementation and validation usage notes.
- Stage 2 analytical report and validated PDF under the dated Wave 5.2R
  analysis bundle.
- Canonical roadmap, backlog, master summary, closeout ledger, usage guide,
  Sphinx portal, and documentation index.

## Implementation Steps

1. Freeze the named loss-component and adapter configuration contract.
2. Implement raw and normalized loss tracking with exponential moving
   averages.
3. Implement functional per-loss gradient extraction, gradient norms, and
   pairwise cosine diagnostics.
4. Implement update-to-parameter ratio measurement.
5. Implement fixed, manual-normalization, gradient-statistics,
   ReLoBRaLo-style, and conflict-aware adapters.
6. Implement staged loss activation and freeze-unfreeze schedules.
7. Implement deterministic seed and dataloader fingerprint checks.
8. Build a synthetic shared-parameter smoke harness covering the four required
   controls and all Stage 2 exit conditions.
9. Generate machine-readable evidence and the detailed Markdown/PDF report.
10. Synchronize the roadmap and project-status documents.
11. Run Python compilation, deterministic validation, Markdown QA, Sphinx QA,
    PDF raster validation, Git diff checks, and commit-size preflight.
12. Create the dedicated Stage 2 commit and report the conclusions before
    beginning Stage 3.

## Outcome

Implemented the opt-in loss-interaction layer and passed all twelve Stage 2
checks on a deterministic shared-parameter smoke problem. The durable evidence
contains four matched controls, four adapter modes, exact loss and gradient
diagnostics, schedule checks, dataloader fingerprints, and a
main-loss-preserving conflict projection. No project-data training was
executed and existing campaign behavior remains unchanged. Stage 3 is
authorized.
