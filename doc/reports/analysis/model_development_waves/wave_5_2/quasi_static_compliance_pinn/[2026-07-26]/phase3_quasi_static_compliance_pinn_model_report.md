# Phase 3 Quasi-Static Compliance PINN Model

## Model Description

`QuasiStaticCompliancePinnNetwork` separates the predicted Transmission Error
into an angle-independent quasi-static mean and a zero-mean periodic
contribution:

```text
TE(theta, u, d) =
    mean_elastic(u, d)
  + sum over k of periodic_k(theta, u, d)
```

Here `theta` is output angle, `u` contains causal speed, torque, and oil
temperature, and `d` is the measured-direction flag. The Phase 3 family tests
six controlled formulations named `C0` through `C5`.

`C0` is a learned-mean control and is not a PINN. `C1` through `C3` learn the
mean but constrain its torque derivative through automatic differentiation.
`C4` and `C5` embed the compliance equation directly in the forward path.

## Operating Principle

### Signed-Torque Contract

The dataset audit established the local measured convention:

- `Fw` measured torque is negative;
- `Bw` measured torque is positive.

Setpoint training supplies positive nominal torque magnitude and a direction
flag. The model reconstructs signed torque as:

```text
tau_signed = -direction_flag * abs(tau_nominal)
```

This transformation is explicit, testable, and independent of measured TE.

### Bounded Stiffness

All physical formulations parameterize effective stiffness between strict
positive bounds:

```text
k = k_min + (k_max - k_min) * sigmoid(raw_k)
```

The initial value, approximately `27.25 kNm/deg`, comes from the Phase 3
training-only identifiability audit. It is an initialization, not a fixed
answer.

### Soft-Residual Formulations

`C1` prescribes linear direction-specific compliance:

```text
d mean_TE / d tau_signed = 1 / k_d
```

`C2` allows bounded stiffness to vary with oil temperature. `C3` adds a
nonnegative bounded odd nonlinear contribution:

```text
mean_nonlinear =
    amplitude_d * tanh(tau_signed / torque_scale)
```

The derivative residual, zero-torque intercept residual, monotonicity test,
stiffness-bound test, and periodic-mean test use only model outputs and causal
collocation inputs. No TE target enters these physics residuals.

### Hard-Equation Formulations

`C4` uses separate direction-specific stiffness and intercepts:

```text
mean_TE = intercept_d + tau_signed / k_d
```

`C5` uses one shared stiffness with separate direction intercepts. Both retain
a learned condition-dependent Fourier branch for curve shape. Because the
periodic branch contains only sine and cosine terms with positive integer
orders, its continuous-cycle mean is zero by construction.

### Initialization-Stability Contract

The twelve-arm screening campaign uses one initialization per formulation.
That screen can identify a candidate worth repeating, but it cannot establish
parameter stability. The campaign plan therefore authorizes additional seeds
only after an arm passes the initial multi-index gate.

The C1-Fw stability package preserves its architecture, split, loss weights,
and runtime profile while setting `training.random_seed` to `314159` and
`271828`. Before constructing the model and dataloaders, the shared training
entry point calls:

```text
seed_everything(training_random_seed, workers=True)
```

This seeds Python, NumPy, PyTorch, samplers, and DataLoader workers. It makes
initialization sensitivity inspectable without claiming bitwise deterministic
GPU execution, because the original runtime keeps `deterministic: false`.

## Conceptual Structure

```text
angle -------------------------> Fourier reconstruction --------+
                                                               |
speed, torque, temperature, direction                           |
       |                                                        |
       v                                                        |
condition encoder --> sine/cosine coefficients -----------------+--> TE
       |
       +--> learned mean (C0-C3)
       |       |
       |       +--> autodiff with respect to signed torque
       |                 |
       |                 +--> compliance residual (C1-C3)
       |
       +--> bounded stiffness and explicit elastic law (C4-C5)
```

## Project Advantages

- tests a source-supported elastic mechanism independently of Phase 2;
- preserves causal runtime inputs and the exact common split;
- exposes signed torque, effective stiffness, intercept, elastic prediction,
  periodic components, and final prediction;
- guarantees positive bounded stiffness by parameterization;
- separates soft differential residuals from hard equation embedding;
- permits direction-specific and shared-stiffness ablations;
- keeps the periodic branch angle-mean-free by construction;
- retains explicit intermediate quantities for TwinCAT-oriented inspection.

## Project Disadvantages And Risks

- the available data do not identify friction, clearance, contact stiffness,
  wear, and hysteresis simultaneously;
- setpoint torque is a nominal magnitude, not the measured load signal;
- a learned soft mean can satisfy data loss while resisting the compliance
  residual if its weight is poorly scaled;
- hard equations can underfit condition-dependent offsets;
- temperature coverage is bounded and correlated operating coverage is not a
  designed factorial experiment;
- direction intercepts are not themselves proof of physical backlash;
- one screening seed cannot establish parameter stability;
- lower residual loss does not prove better curve-first performance or
  closed-loop compensation.

## Implemented Python Components

### `scripts/models/quasi_static_compliance_pinn_network.py`

`QuasiStaticCompliancePinnNetwork`
: Main Phase 3 family implementing formulations `C0` through `C5`.

`compute_signed_torque_tensor`
: Converts nominal torque magnitude and direction into the audited measured
  sign convention, or accepts measured signed torque explicitly.

`compute_effective_stiffness_tensor`
: Returns positive bounded direction-specific, temperature-conditioned, or
  shared stiffness.

`compute_target_compliance_derivative_tensor`
: Evaluates the linear or nonlinear compliance derivative prescribed by the
  selected formulation.

`compute_physics_residual_dictionary`
: Computes target-free compliance, zero-torque, monotonicity, stiffness-bound,
  and periodic-mean losses on bounded deterministic collocation points.

`compute_auxiliary_output_dictionary`
: Exposes the complete physical and periodic decomposition.

### `scripts/models/model_factory.py`

`create_model`
: Recognizes `quasi_static_compliance_pinn` and maps YAML configuration into
  the six formulations.

### `scripts/training/transmission_error_regression_module.py`

`_normalize_loss_configuration`
: Accepts five independent Phase 3 physics weights.

`compute_curve_aware_loss_dictionary`
: Adds enabled compliance constraints to the data and curve-aware objective.

`set_normalization_statistics`
: Propagates training-only normalization statistics into the model so physical
  units remain available to the residual and diagnostic paths.

### `scripts/testing/validate_quasi_static_compliance_pinn.py`

The deterministic validator checks:

- Fw-negative and Bw-positive signed-torque reconstruction;
- positive bounded stiffness;
- all six factory-created formulations;
- finite outputs and residuals;
- nonzero soft-residual gradients;
- exact hard-equation reconstruction;
- positive temperature-conditioned compliance;
- nonnegative nonlinear compliance increments;
- shared `C5` stiffness;
- near-zero periodic mean;
- Lightning loss and inference-context compatibility.

### `scripts/training/train_feedforward_network.py`

The training entry point accepts the optional `training.random_seed` field,
validates its unsigned 32-bit range, and seeds all model and data-worker random
number generators before constructing the training components.

### Phase 3 Campaign Tooling

`prepare_phase3_quasi_static_compliance_pinn_campaign.py`
: Generates the twelve-arm C0-C5 screen.

`prepare_phase3_c1_fw_stability_repeat_campaign.py`
: Generates the two C1-Fw initialization repeats after the initial curve-first
  gate.

`run_phase3_quasi_static_compliance_pinn_campaign.ps1`
: Runs the main campaign locally or through the repository remote workflow.

`run_phase3_c1_fw_stability_repeat_campaign.ps1`
: Runs the bounded stability repeats under the same local and remote
  contracts.

## Deterministic Evidence

The current validator establishes:

- exact signed-torque reconstruction;
- initial stiffness of approximately `27,250 Nm/deg`;
- zero hard-equation compliance and boundary residuals within float32
  precision;
- nonzero `C1`, `C2`, and `C3` compliance gradients;
- periodic-mean residuals below `3e-12`;
- positive `C2` compliance throughout the synthetic temperature range;
- nonnegative `C3` nonlinear derivative increments;
- finite integrated training and inference-context losses.

These checks prove the implementation contract. They do not determine which
formulation, if any, improves held-out TE curves.

## Intended Use

Run the deterministic validator with:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/testing/validate_quasi_static_compliance_pinn.py
```

Use `C0` only as a matched learned control. Phase 3 is closed with no promoted
compliance residual: `C1` passed the initial Fw screen but failed the
three-initialization stability gate, while `C2` through `C5` failed their
joint surface gates. Retain `C1` through `C5` as reproducible experimental and
falsification infrastructure only. Do not interpret fitted stiffness as a
uniquely identified reducer property outside the audited operating domain.
