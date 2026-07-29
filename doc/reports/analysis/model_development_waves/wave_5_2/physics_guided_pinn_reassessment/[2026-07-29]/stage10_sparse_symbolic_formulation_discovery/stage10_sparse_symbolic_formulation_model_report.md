# Stage 10 Sparse And Symbolic Formulation Model

## Model Description

The Stage 10 model is an explicit condition-to-harmonic-coefficient map. It
predicts the Fourier coefficients of a complete forward TE curve from torque,
speed, and oil-temperature setpoints, then reconstructs the curve through a
fixed sine/cosine basis.

It is not a free-form symbolic-regression claim. Candidate expressions come
from a predeclared, bounded, unit-aware term library and are retained only when
they remain stable across training-condition bootstraps.

## Operating Principle

For harmonic order `k`, the model predicts a sine and cosine coefficient:

```text
a_k(condition) = sum_j beta_sin[k, j] * phi_j(condition)
b_k(condition) = sum_j beta_cos[k, j] * phi_j(condition)
```

The TE curve is reconstructed as:

```text
TE(theta, condition) =
    a_0(condition)
    + sum_k [
        a_k(condition) * sin(k * theta)
        + b_k(condition) * cos(k * theta)
      ]
```

The fixed reconstruction makes the angular law periodic by construction.
Sparsity acts on the condition terms `phi_j`, not on the angular basis.

## Conceptual Structure

```text
torque, speed, temperature setpoints
    -> train-only normalization
    -> named condition-term library
    -> sparse coefficient matrices
    -> explicit complex harmonic coefficients
    -> fixed Fourier reconstruction
    -> complete forward TE curve
```

## Sparse Selection

Sequential thresholded ridge alternates between a regularized coefficient fit
and removal of normalized coefficients below a threshold. Bootstrap stability
selection repeats that process on deterministic resamples of training
conditions.

For each term and coefficient channel, the implementation records:

- selection probability;
- sign agreement;
- median normalized magnitude;
- bootstrap magnitude dispersion;
- parent-term availability for hierarchical interactions.

The stable refit uses only terms that pass all retained thresholds.

## Constrained Symbolic Search

The symbolic candidate searches a finite set of interpretable compositions:

- polynomial main effects and interactions;
- signed magnitudes;
- `log1p` magnitudes;
- bounded rational magnitudes;
- separable temperature modulation.

Unsafe division, arbitrary powers, exponentials, and unconstrained expression
growth are excluded. The search is therefore reproducible and PLC-oriented,
although less open-ended than genetic symbolic regression.

## Advantages

- compact and inspectable formulas;
- periodic output by construction;
- no runtime measured-TE input;
- deterministic CPU inference;
- explicit term-level stability evidence;
- direct comparison with the Bauer/PF-A polynomial family;
- straightforward translation to PLC arithmetic.

## Disadvantages

- the term library limits what can be discovered;
- bootstrap stability does not prove physical causality;
- coefficient-wise fitting may ignore cross-order covariance;
- correlated terms can exchange weight across resamples;
- compact formulas may underfit local condition regions;
- no temporal or hysteretic state is represented.

## Planned Python Components

`scripts/models/sparse_harmonic_condition_model.py`

- `NamedConditionTerm`;
- `SparseHarmonicConditionModel`;
- `build_complete_quadratic_library`;
- `build_extended_symbolic_library`;
- `fit_ridge_coefficients`;
- `fit_sequential_thresholded_ridge`;
- `run_bootstrap_stability_selection`;
- `enforce_strong_hierarchy`;
- `reconstruct_curve_matrix`.

`scripts/campaigns/wave_5_2/run_wave52r_stage10_sparse_symbolic_discovery.py`

- Stage 5 dataset reconstruction;
- PF-A, H04, and K01 replay;
- train-only library scaling;
- validation-time hyperparameter selection;
- ten-entry first screen;
- term stability and shuffled-label controls;
- curve-first metrics and qualification gates;
- immutable campaign artifacts.

## Qualification Boundary

A sparse expression may advance as an explicit ablation only when it is
stable, low-complexity, and improves held-out curves relative to the complete
quadratic control. It remains empirical until an independent mechanism maps
the discovered terms to reducer physics.

## Completed Evidence

All ten diagnostic and fitted entries completed without failure. The dense
extended-library ridge control `R00` improved raw MAE from `0.001820438 deg`
for complete-quadratic `Q00` to `0.001657140 deg`, confirming that the
predeclared nonlinear library contains useful condition interactions.

No sparse or constrained-symbolic formulation qualified:

- `S01` retained `86.9%` of coefficient slots;
- bootstrap-stable `S02` retained `57.4%`;
- hierarchy-constrained `S03` retained `67.0%`;
- symbolic-library `Y01` retained `46.4%`;
- no sparse candidate improved centered-shape MAE over `Q00`;
- the weakest selected-term sign agreement was approximately `0.53`, below
  the required `0.85`.

The sparse candidates beat the shuffled-label control, so their gain is real
within this library. It is not sufficiently stable or parsimonious to advance
as an explicit law. The extended-library result remains diagnostic evidence
for later feature design.
