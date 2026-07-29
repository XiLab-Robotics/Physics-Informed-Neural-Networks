# Stage 6 Spectral And Sobolev Guided Residual Model

## Model Description

Stage 6 tests whether explicit derivative-domain and frequency-domain guidance
improves the qualified Stage 5 H04 component.

The primary coefficient candidates preserve the H04 structure:

```text
causal setpoints
    -> bounded complex-coefficient correction
PF-A core coefficients
    -> corrected explicit coefficients
    -> exact uniform Fourier reconstruction
```

The coordinate ablations add a bounded low-rank residual:

```text
condition weights(z) x shared angular basis(theta)
    -> bounded residual curve
PF-A curve + residual curve
    -> complete prediction
```

## Operating Principle

Every candidate retains full-curve data loss. Secondary training-only guidance
can add:

- circular first-derivative error;
- normalized complex coefficient error;
- fragile-band spectral weighting;
- fixed local Fourier moments;
- clipped failure-informed angular weights;
- deterministic curve-to-spectrum-to-derivative curriculum.

The first derivative target uses a circular Savitzky-Golay estimator selected
from training evidence. The filter uses the true angular sample spacing and
wraps the periodic boundary. Derivatives and spectra are labels during
training, not runtime inputs.

## Conceptual Structure

```text
                         +-> curve loss
predicted full curve ----+-> circular derivative loss
                         +-> complex spectral loss
                         +-> local weak moments

all guidance is training-only
             |
             v
runtime remains setpoints -> bounded model -> TE curve
```

## Coordinate Architecture Variants

### Fourier Feature

A fixed bank of known angular orders feeds a tanh angular basis network. A
parameter-matched raw circular-coordinate model is its control.

### SIREN

A sine-activated angular basis network uses SIREN-compatible initialization.
An equal-topology tanh coordinate network is its control.

Both branches use a low-rank factorization and a training-only physical-unit
residual envelope. Zero condition weights reproduce PF-A exactly.

## Advantages

- derivative and harmonic targets directly match curve-first diagnostics;
- training guidance adds no inference feature;
- PF-A and learned residual remain separately inspectable;
- complete curves retain exact periodic evaluation;
- coordinate networks test representational bias without abandoning bounds;
- weak moments test integrated guidance without a fabricated governing law;
- matched controls separate guidance from capacity.

## Disadvantages

- measured derivatives require filtering and remain estimator-dependent;
- complex spectral loss can be redundant with explicit coefficient training;
- SIREN and coordinate branches are less PLC-friendly than coefficient heads;
- failure weights can over-focus noisy angular regions;
- weak moments may improve their own residual without improving prediction;
- success would qualify guidance, not establish a governing-equation PINN.

## Implemented Python Components

### Guided Coordinate Model

`scripts/models/spectral_sobolev_guided_residual_network.py`

- `SineLayer`
- `BoundedCoordinateResidualNetwork`
- `reconstruct_anchor_curve`
- `forward`

### Campaign

`scripts/campaigns/wave_5_2/run_wave52r_stage6_spectral_sobolev_guidance.py`

The campaign script:

- reuses the immutable Stage 5 representation;
- calibrates circular derivative targets on training curves only;
- gates second derivatives by window sensitivity;
- builds failure weights, weak test functions, and residual bounds;
- prepares fifteen matched queue entries;
- validates operators, bounds, gradients, and parameter matching;
- executes first-screen and conditional stability training;
- persists checkpoints, predictions, histories, metrics, and campaign state.

## Qualification Boundary

A formulation advances only after improving derivative, harmonic, and P95
behavior without materially degrading raw, centered, offset, closure, or
unsupported-frequency behavior. It must beat its matched control and repeat
the same decision across three seeds.

## Completed Campaign Result

The Stage 6 campaign completed all `15 / 15` first-screen runs without a
failure. The derivative, spectrum, coordinate-bound, model-shape, and leakage
preflight passed. The training-only second-derivative sensitivity gate failed,
so curvature supervision remained disabled.

FI01 was the raw-error leader at `0.001710638 deg`, a `0.88%` improvement over
the frozen Stage 5 H04 seed. It preserved raw, centered, offset, amplitude,
phase, P95, matched-control, and unsupported-frequency gates, but failed the
required derivative-MAE and derivative-correlation improvements.

W01 achieved the best derivative MAE and correlation, demonstrating that the
weak local Fourier moments affected the intended domain. It nevertheless
regressed raw error, harmonic amplitude, P95, and its C01 matched-control
comparison.

No candidate passed the complete gate. Stability continuation was correctly
skipped, no Stage 6 model was promoted, and Stage 5 H04 remains the qualified
structured component entering Stage 7.
