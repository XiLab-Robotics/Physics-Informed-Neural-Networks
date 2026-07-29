# Stage 13 Synthetic And Weak-Form Oracle Model Report

## Model Description

Stage 13 is an analytical certification workflow rather than a deployable
predictor. It creates signals whose generating equations and parameters are
known exactly, corrupts them in controlled ways, and tests whether candidate
physics-guided diagnostics recover the truth or reject an incorrect law.

## Operating Principle

The Polynomial-Fourier H04 representation supplies realistic forward
conditions, coefficient magnitudes, and harmonic orders. The workflow then
adds one controlled perturbation at a time:

- an injected or omitted harmonic;
- a condition-dependent coefficient correction;
- a biased analytical anchor;
- a torque-dependent compliance nonlinearity;
- measurement noise or reduced angular sampling.

For the oscillator identity `u'' + n^2 u = 0`, the pointwise diagnostic
differentiates the observed signal numerically. The weak diagnostic instead
integrates the observed signal against the known differentiated test function.
This moves derivatives away from noisy observations and is the central
Stage 13 comparison.

## Conceptual Structure

```text
H04 forward-domain anchor
          |
          v
known analytical perturbation ---> exact oracle truth
          |                              |
          v                              v
noise and density corruption ---> estimator or residual
                                         |
                                         v
                         recovery and negative-control gates
```

## Project Advantages

- Known truth separates implementation errors from model misspecification.
- Controlled corruption quantifies detection power before real-data use.
- Weak residuals can test differential structure without differentiating noisy
  TE observations.
- Explicit negative controls expose non-specific residuals.
- Realistic H04 scales keep the tests relevant to the forward operating domain.

## Project Disadvantages

- A successful synthetic recovery is not evidence that the mechanism exists in
  the measured reducer.
- Oracle generators omit unmodeled rig, encoder, contact, and assembly effects.
- Detection thresholds depend on the chosen perturbation scale.
- The workflow does not produce a deployable PINN or change the accepted
  real-data leader.

## Implemented Components

- `scripts/models/synthetic_weak_form_oracle.py` contains Fourier synthesis and
  projection, parameter recovery, pointwise oscillator residuals, smooth
  periodic weak test functions, and normalized residual metrics.
- `scripts/campaigns/wave_5_2/run_wave52r_stage13_synthetic_weak_form_oracle_lane.py`
  owns provenance checks, the ten-entry campaign, gates, and artifacts.
- `scripts/campaigns/wave_5_2/run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1`
  supplies local and remote execution.

## Interpretation Boundary

The strongest permitted conclusion is that a formulation is correctly
implemented and has quantified synthetic detection power. Any future use in a
real-data loss must pass a separate isolated matched-control experiment.

## Completed Evidence

The completed campaign certified all ten analytical cases. Exact synthesis,
harmonic injection and omission, coefficient perturbation, misspecified-anchor
recovery, and compliance recovery passed their declared gates. The weak
oscillator residual was lower than the matched pointwise residual in all
`12 / 12` noisy comparisons at densities of at least `256`, remained below its
threshold at `128` samples, and rejected wrong-order and shuffled-angle
controls by at least `141.08` times.

No result changed an accepted real-data registry or created Stage 14
eligibility.
