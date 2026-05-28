# Causal Input Constraint Clarification

## Overview

The curve-first TE training strategy correctly shifts model evaluation and
promotion toward complete TE-curve tracking quality. However, the current
wording can be misread as if future training or deployment should receive a
complete future curve as model input.

That is not the intended constraint. In the real TestRig / TwinCAT application,
the runtime model input remains causal:

- the current point-level operating state;
- optionally a short historical window of already observed points;
- derived causal features computed only from the current point and past
  samples.

The model must not depend on future TE samples, future angular samples, or a
pre-known complete revolution curve at inference time.

No subagent is planned for this clarification.

## Technical Approach

The documentation should explicitly separate:

- input contract: causal point or causal short-history window;
- output/evaluation contract: curve-first offline validation on reconstructed
  TE curves;
- dataset contract: preserve the current source data and valid-window
  semantics instead of redesigning the dataset around non-causal curve inputs;
- training contract: curve-aware losses and reranking may aggregate predictions
  over curves, but the per-sample feature payload must remain compatible with
  the deployed online predictor.

This clarification should be added to the curve-first strategy report and the
operational backlog. The Track 2 official report and Wave 1 closeout can remain
unchanged unless they need a short pointer to the clarified input contract.

## Involved Components

- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/README.md`

Potential future implementation surfaces, not modified by this documentation
clarification:

- `scripts/training/transmission_error_datamodule.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/train_feedforward_network.py`
- Track 2 validation and report scripts under `scripts/reports/analysis/`

## Implementation Steps

1. Add a dedicated causal-input clarification to the curve-first strategy
   report.
2. Update the live backlog selection rule so future campaign plans preserve
   the pointwise or short-history online input contract.
3. Update the master summary ranking policy note to distinguish scalar
   registry metrics, curve-first promotion metrics, and causal input
   constraints.
4. Register this technical note in `doc/README.md`.
5. Run Markdown QA on touched Markdown files.
6. Run Sphinx only if the touched scope affects the portal build surface.

The intended outcome is a clearer strategy: evaluate and select by curves, but
do not make future complete curves part of the deployed model input.
