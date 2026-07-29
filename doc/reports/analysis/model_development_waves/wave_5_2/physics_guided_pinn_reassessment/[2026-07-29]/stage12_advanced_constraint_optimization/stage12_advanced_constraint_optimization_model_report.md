# Stage 12 Advanced Constraint Optimization Model Report

## Model Description

Stage 12 retains the Stage 9 K01 causal coefficient-residual GRU without
changing its inference graph. K01 predicts bounded causal corrections to the
qualified Stage 5 H04 Polynomial-Fourier coefficients and reconstructs the
current transmission-error value at each angular sample.

The new element is the training strategy. Ten profiles compare standard AdamW
with adaptive loss balancing, gradient projection, adaptive sample emphasis,
constraint multipliers, curricula, resampling, and second-order refinement.

## Operating Principle

```text
causal angle and setpoints
    -> unchanged K01 GRU
    -> bounded correction to frozen H04 coefficients
    -> Fourier reconstruction
    -> decomposed data and constraint losses
    -> declared Stage 12 optimizer adapter
```

The raw data gradient remains the primary learning signal. Auxiliary objectives
express already accepted structure:

- mean and centered-shape decomposition;
- small bounded departure from H04;
- periodic endpoint closure;
- causal reset and chunk invariance as evaluation gates.

## Conceptual Structure

Gradient-statistics annealing and ReLoBRaLo-style balancing change scalar loss
weights. Main-loss-preserving projection modifies the combined gradient only
when an auxiliary gradient conflicts with the raw-error gradient.

Self-adaptive weighting assigns bounded training-curve weights. Failure-informed
resampling changes the next epoch's training draw probabilities from
training-only residuals. Augmented Lagrangian optimization updates multipliers
for closure and correction-budget violations. Curriculum regularization
introduces these constraints gradually. L-BFGS provides a bounded full-batch
refinement after AdamW.

## Advantages In This Project

- tests optimizer limitations without changing the qualified model;
- isolates optimization effects from equation and architecture effects;
- preserves the H04 analytical interpretation;
- records gradient conflict and update behavior explicitly;
- can improve closure without adding deployment-time computation;
- compares repeatability against the recorded multi-seed K01 evidence.

## Disadvantages And Risks

- adaptive weighting can overfocus on a small number of curves;
- closure improvement can trade against interior curve accuracy;
- relative-loss balancing can amplify noisy objectives;
- projected gradients and L-BFGS increase training cost;
- augmented multipliers can become unstable when constraints are infeasible;
- no optimizer can make an uninformative physical law valid;
- improved training behavior does not by itself authorize Wave 6.

## Implemented Component Contract

The Stage 12 helper will provide:

- decomposed loss records;
- bounded adaptive curve weights;
- augmented-Lagrangian multiplier updates;
- deterministic failure-informed sampling;
- optimizer-state serialization;
- gradient and update diagnostics.

The campaign driver will provide:

- frozen Stage 0, H04, and K01 replay;
- ten-entry preparation and execution;
- conditional stability;
- test-once evaluation;
- immutable per-run and campaign artifacts;
- curve-first and repeatability gates.

## Qualification Boundary

An optimizer qualifies only if it improves K01 against matched standard
training while repairing closure and preserving shape, mean, tail, bounded
correction, causality, chunk behavior, and deployment cost. A scalar-MAE win,
a closure-only win, or a single-seed win is insufficient.

## Completed Evidence

The campaign
`2026-07-29-21-52-53_wave52r_stage12_advanced_constraint_optimization_2026_07_29`
completed all `10 / 10` first-screen entries. The initial P01 gradient
assignment and L01 L-BFGS-mode implementation faults were corrected and
recovered; the final campaign has zero residual failures.

- Frozen K01 C00 remained the raw leader at `0.001371553 deg`.
- F01 was the best trained raw and shape candidate at `0.001440558 deg` raw
  MAE and `0.001144384 deg` centered-shape MAE, but mean MAE, closure,
  correction magnitude, chunk equivalence, and frozen-C00 comparison failed.
- S01 improved raw, mean, shape, P95, and closure relative to C01, but its raw
  MAE remained `8.75%` worse than C00 and its correction and chunk gates failed.
- A01 reproduced C01 because the predeclared augmented-Lagrangian constraints
  remained inactive.
- L01 performed seven L-BFGS closure evaluations; validation rejected the
  refinement and restored C01 exactly.
- No candidate passed chunk equivalence or the complete first-screen gate.

No optimizer qualified, conditional stability was skipped, and no Stage 12
component was promoted. The canonical result report and validated PDF are
stored under `doc/reports/campaign_results/model_development_waves/wave_5_2/`
with timestamp `2026-07-29-23-10-48`.
