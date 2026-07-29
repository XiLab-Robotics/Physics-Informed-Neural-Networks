# Wave 5.2R Stage 12 Advanced Constraint Optimization

## Overview

Stage 12 tests whether advanced multi-objective and constrained optimization
improves the already qualified Stage 9 K01 causal coefficient-residual model.
The scope remains exclusively `polished_dataset`, setpoint inputs, and `Fw`.

This stage does not introduce a new physical equation. It obeys the roadmap
ordering rule by applying heavier optimization only to the two isolated
ingredients that survived earlier gates:

- the frozen Stage 5 H04 bounded Polynomial-Fourier coefficient component;
- the Stage 9 K01 causal coefficient-residual GRU.

Stage 10 laws and Stage 11 trust scores remain diagnostic evidence only. They
are not admitted as trainable constraints because they did not qualify.

The technical document and campaign plan are covered by the user's active
blanket approval. No subagent is planned.

## Technical Approach

### Frozen Contract

Every candidate uses the Stage 0 split, the same H04 anchor, the same K01
architecture, the same causal inputs, the same coefficient representation, and
the same deployment-facing chunk contract. Test labels remain unavailable to
optimizer selection and checkpoint selection.

The decomposed training objective exposes:

- pointwise data error;
- curve-mean error;
- mean-centered shape error;
- bounded coefficient-correction magnitude;
- periodic endpoint closure;
- an optional high-error smooth surrogate fitted from training residuals only.

The first-screen matrix contains ten entries:

| ID | Method | Purpose |
| --- | --- | --- |
| C00 | frozen accepted K01 replay | immutable Stage 9 reference |
| C01 | standard AdamW retrain | matched optimizer control |
| G01 | gradient-statistics annealing | equalize component gradient scales |
| R01 | ReLoBRaLo-style balancing | react to relative loss progress |
| P01 | main-loss-preserving projection | remove auxiliary conflicts without reversing the data gradient |
| S01 | self-adaptive curve weighting | focus bounded weights on difficult training curves |
| A01 | augmented Lagrangian | enforce closure and correction-budget inequalities |
| U01 | curriculum regularization | introduce qualified constraints progressively |
| F01 | failure-informed resampling | revisit high-error training curves without test leakage |
| L01 | AdamW plus L-BFGS refinement | test deterministic second-order finishing |

All adaptive state is derived from training data. Validation selects
checkpoints and tuning constants. The frozen test split is evaluated once per
completed candidate.

### Qualification Logic

An advanced method cannot qualify by scalar MAE alone. Relative to both C00
and C01 it must:

- improve raw MAE or mean-centered shape MAE by at least `1%`;
- avoid more than `0.5%` regression on the other metric;
- avoid mean-MAE and P95 regression greater than `1%`;
- reduce the Stage 9 periodic-closure failure materially;
- preserve reset reproducibility and meet the declared chunk-equivalence gate;
- keep coefficient corrections inside the H04 bounded-correction contract;
- beat shuffled-method or disabled-adaptation checks where applicable.

The strongest first-screen candidate advances to seeds `271828` and `161803`
only if the complete first-screen gate passes. Repeatability is compared with
the five recorded standard-K01 seeds from Stages 9 and 11. No threshold may be
changed after test results are observed.

## Involved Components

- `scripts/models/causal_temporal_analytical_residual_network.py`
  remains the frozen K01 architecture.
- `scripts/training/physics_guided_optimization_instrumentation.py`
  supplies gradient statistics, ReLoBRaLo-style weighting, schedules, gradient
  diagnostics, and main-loss-preserving projection.
- A Stage 12 optimization helper under `scripts/training/` will add bounded
  adaptive curve weights, augmented-Lagrangian state, and deterministic
  failure-informed sampling.
- A Stage 12 campaign driver under `scripts/campaigns/wave_5_2/` will own
  replay, training, evaluation, immutable artifacts, and gates.
- A dedicated PowerShell launcher and launcher note will support local and
  `-Remote` execution.
- Campaign YAML and queue entries will live under
  `config/training/advanced_constraint_optimization/`.
- Campaign artifacts will use the immutable training-run and
  training-campaign directory conventions.
- A model report, campaign result report, styled PDF, backlog update, ledger
  update, usage-guide update, and Sphinx API page will close the stage.

## Implementation Steps

1. Freeze the Stage 0, H04, K01, seed, and checkpoint provenance contract.
2. Create the campaign plan, candidate queue, launcher contract, and model
   explanation.
3. Implement decomposed K01 losses and deterministic optimizer adapters.
4. Add leakage, gradient, constraint, sampling, and optimizer-state preflight
   checks.
5. Run the ten-entry first screen.
6. Run conditional stability only if the complete first-screen gate passes.
7. Generate leaderboard, best-run, gate, optimizer-diagnostic, and failure
   artifacts.
8. Produce and visually validate the Markdown and styled PDF closeout.
9. Synchronize backlog, ledger, guide, master summaries, and Sphinx portal.
10. Run repository QA and create the separately approved Stage 12 commit.
