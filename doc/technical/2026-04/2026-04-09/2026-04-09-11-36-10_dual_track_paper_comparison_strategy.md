# Dual-Track Paper Comparison Strategy

## Overview

This document formalizes how the repository should compare its current TE model
families against the benchmark paper `reference/RCIM_ML-compensation.pdf`
without collapsing two different questions into one.

The first question is whether the repository can reproduce the paper's own
harmonic-wise modeling logic. The second question is whether the repository's
already trained direct-TE model families can be compared against the paper at
the level of final offline TE-curve accuracy, even if their internal modeling
path is different.

These two questions should not be merged. They must be tracked as separate but
coordinated implementation tracks.

This document therefore proposes a dual-track comparison strategy:

1. a `paper-faithful harmonic-wise track`;
2. a `repository direct-TE comparable track`.

## Technical Approach

### What The Paper Actually Requires

The paper models selected TE harmonics through operating-condition inputs such
as speed, torque, and oil temperature. It then reconstructs the TE curve from
those harmonic predictions and evaluates the resulting compensation path.

In paper-faithful terms, a model is not equivalent to the paper unless it is
trained to predict harmonic quantities such as harmonic coefficients or
amplitude/phase terms across operating conditions before TE reconstruction.

### Why Existing Repository Models Cannot Be Reused As-Is For Harmonic-Wise Prediction

The current best repository models were trained as direct TE predictors.

Their input/output structure is currently:

- input: `angle + speed + torque + temperature + direction`;
- output: TE value at that angle.

That is not the same task as the paper-faithful harmonic prediction path, where
the input/output structure is conceptually:

- input: `speed + torque + temperature (+ direction when needed)`;
- output: harmonic terms such as `A_k / phi_k` or equivalent harmonic
  coefficients.

Therefore, the already trained direct-TE models cannot be reused directly as
paper-faithful harmonic predictors.

If the repository later wants to compare one of those families inside the
paper-faithful harmonic pipeline, that family must be retrained on harmonic
targets.

### Why The Existing Repository Models Are Still Valuable

Even though the current model families are not paper-faithful harmonic
predictors, they still produce full TE-curve predictions.

This means they can still be evaluated under the same final offline TE-curve
metric protocol used for paper comparison, provided the repository makes the
scope explicit:

- they are comparable at the level of final offline TE output;
- they are not equivalent to the paper's internal harmonic-wise pipeline.

This distinction is important because it allows the repository to compare:

- `paper-faithful harmonic-wise models`;
- `repository direct-TE models`;

under a shared final offline TE-curve evaluation protocol without pretending
that both families solve the same internal prediction task.

### Proposed Dual-Track Benchmark Structure

#### Track 1. Paper-Faithful Harmonic-Wise Benchmark

This track is the repository-owned reproduction path for the paper logic.

Its purpose is to answer:

- can the repository reproduce the paper's harmonic-wise offline benchmark?

This track should:

1. train harmonic-wise predictors on harmonic targets;
2. reconstruct TE from the predicted harmonic stack;
3. evaluate held-out TE curves with the paper-comparable offline percentage
   metric;
4. later feed the online compensation branch.

This track is the canonical path for `Target A` and the prerequisite offline
base for `Target B`.

#### Track 2. Repository Direct-TE Comparable Benchmark

This track uses the repository's already trained or future direct-TE model
families without forcing them into a harmonic-wise reparameterization first.

Its purpose is to answer:

- how do the repository's best direct-TE families compare with the paper at
  the level of final offline TE-curve prediction quality?

This track should:

1. take the current best direct-TE models from the existing family registries;
2. run them through a shared paper-style offline TE-curve evaluator;
3. compute mean percentage error on held-out TE curves;
4. report those results as `result-level comparable`, not as
   `paper-faithful pipeline equivalent`.

### Reporting Rule

Future colleague-facing comparison tables should explicitly mark each evaluated
entry with its prediction style:

- `harmonic-wise`;
- `direct-TE`.

This lets the project present both:

- a true paper-reproduction benchmark;
- and a broader repository-vs-paper offline accuracy comparison;

without mixing implementation-faithfulness and final-output quality.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/te_model_live_backlog.md`
- `scripts/training/run_harmonic_wise_comparison_pipeline.py`
- `scripts/training/harmonic_wise_support.py`
- current family-best registries under `output/registries/families/`
- current program-best registry under `output/registries/program/`

## Implementation Steps

1. Keep the existing harmonic-wise branch as the canonical `Track 1` paper-
   faithful path.
2. Extend the backlog so `Track 1` and `Track 2` are both explicit and ordered.
3. Define a repository-owned shared offline evaluator for full TE-curve
   percentage-error reporting.
4. Use that evaluator on the current best direct-TE families so they can be
   compared against the paper at the final TE-curve level.
5. Keep the reporting language explicit:
   - `paper-faithful` for harmonic-wise reproductions;
   - `result-level comparable` for direct-TE models.
6. Only later decide whether selected direct-TE families should also receive
   dedicated harmonic-wise retraining.
