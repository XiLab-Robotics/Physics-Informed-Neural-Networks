# Shape-First Training Rule Distillation

## Overview

This document records the next model-development idea after the bounded
shape-objective Track 2 screen. The goal is to distill selected
`TE Curve Verification Pipeline` shape-first screen rules into training-time
signals, checkpoint-selection monitors, or conservative auxiliary losses.

The idea is intentionally not a continuation of the failed scalar
shape-objective branch. The bounded screen showed that scalar improvement does
not guarantee curve-first promotion. The next design should treat the
shape-first screen as the source of normalized evidence and only promote
training objectives that improve the same evidence used by the verification
pipeline.

## Technical Approach

The first implementation stage should be design-first and monitor-first:

- keep `polished_dataset` setpoints `Fw` anchored to the accepted
  `periodic_gru_sequence` forward candidate;
- map verification evidence into explicitly named training diagnostics before
  making each term a loss;
- reuse existing curve-aware hooks where they already match the screen:
  centered curve shape, curve offset, curve amplitude, sparse harmonic shape,
  and derivative shape;
- keep frequency-domain similarity, dominant-harmonic phase error, derivative
  agreement, and per-curve pass-rate thresholds as checkpoint-selection or
  validation monitors unless a bounded pilot proves that turning them into loss
  terms improves Track 2 behavior;
- keep time-windowed and non-windowed variants active in every future bounded
  pilot design instead of choosing one family type prematurely;
- compare every pilot against both the accepted windowed GRU baseline and the
  best non-windowed harmonic baseline.

The expected structure is a small `Fw` pilot, not a full multi-surface Aries
campaign. The pilot should answer whether Track 2 shape-first evidence can
guide training without degrading raw curve error, offset behavior, or harmonic
phase fidelity. Unless a later evidence gate explicitly closes one branch, the
pilot package should include at least one time-windowed candidate and one
non-windowed candidate so both development paths remain comparable.

## Involved Components

- `scripts/training/transmission_error_regression_module.py`
  Existing curve-aware loss hooks and training diagnostics.
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
  Source of the current shape-gated screen metrics and threshold policy.
- `config/training/`
  Future pilot queue entries and loss-profile configuration.
- `scripts/campaigns/`
  Future approved pilot launcher with local and `-Remote` support.
- `doc/running/te_model_live_backlog.md`
  Canonical operational backlog entry for the idea.
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
  Canonical program-status decision record.
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
  Campaign and family-status synchronization point after any completed pilot.

## Implementation Steps

1. Record this design direction in the live backlog and closeout ledger as a
   distinct follow-up from the failed shape-objective bounded screen.
2. Audit the current regression-module loss diagnostics against the
   shape-gated reranker metrics and identify which metrics are already
   differentiable, which are checkpoint monitors, and which should stay purely
   post-hoc.
3. Prepare a small planning report for a `polished_dataset` setpoint `Fw`
   pilot that includes both a time-windowed candidate and a non-windowed
   candidate.
4. Generate only the minimal approved queue/config and launcher package needed
   for one bounded pilot.
5. Run local preflight and one-batch validation before any remote training.
6. After the pilot finishes, close it out normally, then run a bounded
   `TE Curve Verification Pipeline` screen before any promotion decision.

No subagent is planned for the first implementation pass. If later code review
or parallel design auditing is needed, the subagent name, scope, and approval
requirement must be recorded before launch.
