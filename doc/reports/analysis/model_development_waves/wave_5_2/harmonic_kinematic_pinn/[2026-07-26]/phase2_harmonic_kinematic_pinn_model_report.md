# Phase 2 Harmonic And Kinematic PINN Model

## Model Description

`HarmonicKinematicPinnNetwork` is the first repository model designed to
support a genuine differentiable physical residual during training. It models
direction-specific Transmission Error as

```text
TE(theta, u) = offset(u) + sum over k of h_k(theta, u)
```

where:

- `theta` is the output angle;
- `u` contains causal operating-condition features;
- `offset(u)` is angle-independent;
- each `h_k` is an inspectable component associated with output order `k`.

The default Phase 2 orders are `1`, `3`, `39`, `40`, `78`, `81`, `156`,
`162`, and `240`, selected from the local Phase 0 and Phase 1 evidence. They
are configuration values, not universal constants.

## Operating Principle

### Explicit Fourier Control

In `explicit_fourier` mode, the condition encoder predicts one sine and one
cosine coefficient for every configured order. Reconstruction is exact:

```text
h_k(theta, u) =
    a_k(u) sin(k theta)
  + b_k(u) cos(k theta)
```

This path is a parameter-matched structured control. It is periodic by
construction and satisfies the harmonic oscillator equation, but it is not
called a full PINN because no governing residual is needed to constrain its
training.

### Implicit PINN

In `implicit_pinn` mode, each component head receives:

- the causal condition latent representation;
- normalized raw angle;
- `sin(k theta)`;
- `cos(k theta)`.

The raw-angle input permits the component to depart from a pure harmonic.
Training can then penalize the normalized governing residual:

```text
R_k = (1 / k^2) * d2 h_k / d theta2 + h_k
```

The derivatives are obtained through PyTorch higher-order automatic
differentiation. The physical residual does not use measured TE targets.

### Periodic Boundary Residuals

The model also exposes value and first-derivative closure:

```text
y(0, u) = y(2 pi, u)
dy/dtheta(0, u) = dy/dtheta(2 pi, u)
```

These terms are independently weighted. This makes it possible to distinguish
the contribution of the oscillator law from boundary consistency.

## Conceptual Structure

```text
causal condition features
          |
          v
  condition encoder
          |
          +--------------------> offset head
          |
          +--> order 1 component head -----+
          +--> order 3 component head -----|
          +--> order 39 component head ----|
          +--> ... -------------------------+--> summed TE prediction
          +--> order 240 component head ---|
                                           |
theta --> raw angle + sin/cos context ------+

each implicit component:
    autodiff(theta) --> first derivative --> second derivative
    second derivative / k^2 + component --> physics residual
```

There is deliberately no unconstrained free residual branch in the first
campaign. Such a branch could absorb the target while bypassing the physical
heads.

## Project Advantages

- implements an explicit differentiable governing residual;
- keeps offset and periodic shape separate;
- preserves one inspectable curve per harmonic order;
- uses causal operating inputs only;
- allows amplitude and phase to vary with condition;
- exposes oscillator and boundary terms independently;
- provides a Fourier-only control with the same condition contract;
- supports exact order-drop and order-add ablations;
- produces explicit intermediate quantities suitable for later TwinCAT
  simplification.

## Project Disadvantages And Risks

- second derivatives increase training memory and compute cost;
- high-order heads may create stiff optimization behavior;
- the oscillator prior describes synchronous periodic structure, not
  compliance, hysteresis, contact, wear, or dynamic load;
- the implicit model has more parameters than the minimal explicit Fourier
  control;
- a zero component satisfies the oscillator equation, so data loss and
  multi-index validation remain essential;
- periodic boundary terms may become redundant if the learned head converges
  to a pure sine/cosine law;
- the fallback normalized-only `forward` path cannot reconstruct a physical
  angle unless the raw-angle context is preserved by export tooling;
- improved training residual does not prove improved closed-loop compensation.

## Implemented Python Components

### `scripts/models/harmonic_kinematic_pinn_network.py`

`HarmonicKinematicPinnNetwork`
: Main Phase 2 model. It builds the condition encoder, offset head, explicit
  coefficient head or implicit component heads, and the target-free residual
  contract.

`compute_auxiliary_output_dictionary`
: Returns the condition latent tensor, offset prediction, per-order component
  matrix, summed harmonic prediction, and final prediction.

`compute_normalized_oscillator_residual`
: Computes first and second angular derivatives with `torch.autograd.grad` and
  returns the normalized order-specific governing residual.

`compute_physics_residual_dictionary`
: Selects bounded collocation points, evaluates every oscillator residual, and
  evaluates periodic value and slope closure on matched causal conditions.

### `scripts/models/model_factory.py`

`create_model`
: Recognizes `harmonic_kinematic_pinn` and instantiates either the explicit
  Fourier control or implicit PINN from configuration.

### `scripts/training/transmission_error_regression_module.py`

`_normalize_loss_configuration`
: Accepts physics diagnostic settings, collocation bounds, boundary bounds,
  and the three Phase 2 physics weights.

`compute_curve_aware_loss_dictionary`
: Adds weighted oscillator, periodic-value, and periodic-slope residuals to the
  existing data and curve-aware objective.

`compute_loss`
: Logs each physical loss separately for training, validation, and test
  surfaces.

### `scripts/testing/validate_harmonic_kinematic_pinn.py`

`validate_exact_oscillator_identity`
: Proves an exact order-39 sine/cosine signal has a near-zero residual and an
  order-5 signal tested as order 3 does not.

`validate_model_mode`
: Checks factory construction, auxiliary shapes, finiteness, physics
  gradients, and full-revolution shift behavior for both modes.

`validate_lightning_loss_integration`
: Proves the residual enters the repository Lightning loss, backpropagates to
  parameters, and remains evaluable inside an inference context.

## Current Deterministic Evidence

The non-training validator currently establishes:

- exact admissible maximum residual: approximately `1.19e-7`;
- inadmissible residual mean square: approximately `1.57`;
- explicit-control oscillator loss: approximately `7.5e-17`;
- implicit-PINN oscillator loss before training: approximately `1.97e-2`;
- implicit-PINN physics gradient norm: nonzero;
- integrated Lightning gradient norm: nonzero;
- finite physics evaluation inside a validation inference context.

These checks prove implementation correctness. The subsequent approval-gated
campaign completed `8 / 8` runs and supplied the held-out accuracy evidence
below.

## Campaign Outcome

The canonical Phase 2 campaign closed as a valid negative result:

- `H0-Fw` remained the scalar and curve-payload leader inside Phase 2;
- `H1-Bw` improved scalar test MAE and the dominant order-1 amplitude and
  phase errors relative to `H0-Bw`;
- `H1-Bw` nevertheless worsened aggregate amplitude fidelity across the
  selected harmonic set;
- periodic closure reduced the periodic-slope residual by several orders of
  magnitude but did not produce a curve-first promotion;
- the Bauer anchor was directionally unstable at the tested weight;
- no Phase 2 physical loss was promoted.

The full decision and validated PDF are in:

- `doc/reports/campaign_results/wave_5_2/2026-07-26-16-53-50_phase2_harmonic_kinematic_pinn_campaign_results_report.md`;
- `doc/reports/campaign_results/wave_5_2/2026-07-26-16-53-50_phase2_harmonic_kinematic_pinn_campaign_results_report.pdf`.

## Intended Use

Run the deterministic non-training validator with:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/testing/validate_harmonic_kinematic_pinn.py
```

The Phase 2 campaign package is now closed. Use the model as reproducible
experimental infrastructure or an explicit Fourier control. Do not reuse
nonzero Phase 2 physics weights as defaults in later phases.
