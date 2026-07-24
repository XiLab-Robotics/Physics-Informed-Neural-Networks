# Defer Wave 5.2 MMT To Future TODO

## Overview

This document records the approved roadmap decision to defer the Wave 5.2 MMT
branch after the leakage-safe residual-explanatory rerun closed with
`blocked_by_parameter_availability`.

MMT will remain preserved as an inactive future TODO rather than an active
model-development dependency. The rest of the non-MMT roadmap may proceed
without waiting for new MMT work.

This is a documentation-only status synchronization. It does not authorize
training, change model artifacts, update registries, or reopen campaign state.
No subagent is planned.

## Technical Approach

The canonical backlog and status documents will distinguish:

- completed MMT diagnostics and residual-replay evidence;
- the current deferred state;
- the physical evidence required to reopen the branch;
- the fact that MMT no longer blocks the remaining Wave 5, Wave 6, or Track 3
  planning sequence.

The future TODO will be reopened only if independent component-error
measurements or a validated causal contact-state reconstruction provides
condition-varying MMT inputs without deriving inference features from held-out
TE targets.

## Involved Components

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- `doc/README.md`.

The active campaign state is closed and its protected-file list is empty.

## Implementation Steps

1. Register this technical document from `doc/README.md`.
2. Change Wave 5.2 MMT from an active blocked branch to an inactive future
   TODO.
3. Record the exact physical-input trigger required to reopen it.
4. Remove MMT as a blocker for the remaining non-MMT roadmap.
5. Synchronize the backlog, closeout ledger, and both master-summary views.
6. Run repository Markdown QA, final-newline checks, and Sphinx validation if
   portal-backed documentation changes.
7. Stop without committing and wait for explicit commit approval.
