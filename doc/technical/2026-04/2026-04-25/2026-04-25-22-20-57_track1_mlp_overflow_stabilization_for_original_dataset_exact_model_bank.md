# 2026-04-25-22-20-57 Track1 Mlp Overflow Stabilization For Original Dataset Exact Model Bank

## Overview

The relaunched `Track 1` bidirectional original-dataset mega-campaign is now
past the remote-launcher and ONNX-toolchain failures, but the `MLP` family is
still numerically unstable during training.

The current remote logs show three related symptoms on the scikit-learn
`MLPRegressor` branch:

- repeated `RuntimeWarning: overflow encountered in matmul`;
- repeated `RuntimeWarning: overflow encountered in dot` and
  `overflow encountered in square`;
- `ConvergenceWarning: Maximum iterations (1000) reached`.

This branch currently builds paper-compatible exact-model-bank dataframes and
feeds the raw `rpm`, `deg`, and `tor` features directly into
`MultiOutputRegressor(MLPRegressor(...))` without an explicit feature-scaling
stage. That is the most likely root cause, and it is also aligned with the
official `scikit-learn` guidance that `MLPRegressor` is highly sensitive to
feature scaling and may require different solver/runtime choices on small
tabular datasets.

## Technical Approach

The stabilization pass should stay narrow and target only the `MLP`
family-path inside the exact-model-bank workflow.

The first change should introduce an explicit feature-scaling stage for the
`MLP` estimator only. The safest implementation is to wrap the base estimator
inside a scikit-learn `Pipeline` with `StandardScaler` followed by
`MLPRegressor`. This keeps the other exact-paper families unchanged and makes
the preprocessing contract explicit and inspectable. It also follows the
official scikit-learn recommendation that MLP inputs should be standardized or
otherwise scaled before training.

The second change should revisit the current `MLPRegressor` defaults. The
diagnostic run already raised `max_iter` from `200` to `1000`, but that alone
was not enough. The follow-up should reduce the likelihood of exploding
updates, for example by tightening the optimization regime around:

- solver choice;
- hidden-layer width;
- regularization `alpha`;
- `learning_rate_init`;
- early-stopping behavior.

Given the dataset size of this branch, the most defensible first stabilization
surface is:

- keep the family isolated to the same workflow;
- add scaling;
- reduce the effective step size;
- increase regularization;
- keep the architecture conservative rather than wide.

The implementation should also preserve the ONNX export contract already
validated in the diagnostic campaign. That means the revised `MLP` path must
still export correctly through the existing scikit-learn ONNX branch after the
feature-scaling wrapper is introduced.

Because the mega-campaign is already running, the work should avoid touching
protected launcher and campaign-state files unless a later explicit approval is
given. The intended code surface is the model-bank support path only.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `reference/RCIM_ML-compensation.pdf`
- `doc/guide/project_usage_guide.md`
- `site/`

## Implementation Steps

1. Inspect the current exact-model-bank `MLP` estimator path and confirm that
   no feature scaling is applied before `MLPRegressor`.
2. Introduce an `MLP`-only scikit-learn preprocessing wrapper based on
   `StandardScaler` plus `MLPRegressor`.
3. Tighten the `MLPRegressor` defaults to reduce overflow risk and improve
   convergence behavior on the original-dataset exact-model-bank branch.
4. Verify that the updated `MLP` path still fits, evaluates, and exports ONNX
   through the exact-model-bank validation workflow.
5. Update user-facing documentation if the runnable workflow contract changes,
   then rerun scoped Markdown QA and a warning-free Sphinx build.
