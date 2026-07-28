# Stage 4 Data-Only Residual Capacity Model

## Overview

The Stage 4 family measures the value of an explicit analytical-plus-neural
decomposition before any physics-guided objective is introduced.

The experiment is restricted to:

- `polished_dataset`;
- setpoint inputs;
- forward (`Fw`) curves;
- the frozen paired split with signature
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- normalized pointwise mean-squared data loss;
- one optional residual-energy penalty.

The family is intentionally not called a PINN. It is the data-only capacity
floor that later PINN formulations must beat.

## Causal Analytical Anchor

The preparation audit found that the exact Stage 3/Phase 1 PF-A replay used
measured operating averages while its report declared a setpoint-only
contract. The difference is not permitted in this campaign.

Stage 4 refits the same complete-quadratic, nine-order Polynomial-Fourier
formulation on the `675` forward training curves using only:

- negative nominal torque setpoint for forward motion;
- absolute nominal speed setpoint;
- nominal oil-temperature setpoint.

The dataset tensor stores torque setpoint as a positive magnitude. The
analytical branch converts it explicitly with
`signed_torque = -direction_flag * abs(torque_setpoint)`, yielding negative
torque for `Fw` and positive torque for `Bw`. The learned branch continues to
receive the declared raw setpoint feature.

Validation and test targets do not enter the surface fit. The resulting
`PF_A_SETPOINT_QUADRATIC` anchor is serialized independently from every neural
checkpoint.

| Replay | Test MAE [deg] | Centered MAE [deg] | Offset error [deg] |
| --- | ---: | ---: | ---: |
| Legacy PF-A with measured averages | 0.001807084 | 0.001384816 | 0.000965090 |
| Legacy surface evaluated on setpoints | 0.001801461 | 0.001382771 | 0.000980712 |
| Causal setpoint PF-A refit | 0.001808977 | 0.001381875 | 0.000975232 |

The causal refit is only `0.000001893 deg` worse in raw MAE than the legacy
measured-input replay. That small numerical difference does not justify
retaining a non-causal runtime input.

The same correction is applied to the support geometry. The training-only
setpoint envelope classifies:

| Split | Core | Sparse/corner | Extrapolation |
| --- | ---: | ---: | ---: |
| Train | 675 | 0 | 0 |
| Validation | 192 | 2 | 0 |
| Test | 96 | 1 | 0 |

All `966` eligible forward predictions and all `27` center/face/corner stress
points are finite. Promotion uses the `96`-curve causal `supported_core` test
surface; the one sparse test condition stays visible but cannot create a pass.

## Operating Principle

The primary hybrid contract is:

```text
predicted TE =
    frozen causal PF-A contribution
  + learned data-only residual contribution
```

The direct control contract is:

```text
predicted TE = direct learned contribution
```

All learned branches receive the same normalized causal features. The angle is
expanded into the declared fixed sine/cosine bank. Speed, torque, temperature,
and the constant forward direction flag condition the learned output.

## Formulations

### R0: Frozen Analytical Control

`R0` is the causal setpoint PF-A surface without training. It establishes the
error that a hybrid must improve and remains independently reconstructable.

### R1: Direct Periodic MLP

`R1` predicts normalized TE directly. It never evaluates the analytical
anchor during its forward path. Six R1 instances match the trainable parameter
count and depth of the residual candidates.

### R2: Unconstrained Pointwise Residual

`R2` adds a periodic MLP residual to the frozen analytical prediction. Its
output layer starts at exactly zero, so initialization reproduces R0 bit for
bit in normalized space.

### R3: Bounded Pointwise Residual

`R3` applies a differentiable physical-unit bound:

```text
residual_deg = residual_bound_deg * tanh(raw_residual)
```

The bound is the training-only `99.5` percentile of the absolute PF-A residual:
`0.016873775 deg`.

### R4: Low-Rank Residual Basis

`R4` predicts one offset and sine/cosine coefficients for four fixed residual
orders. A training-only spectrum screen selected:

`[2, 80, 159, 237]`.

These orders exclude the nine PF-A anchor orders. The reconstructed residual
remains explicit and compact.

### R5: Coefficient Correction

`R5` predicts nineteen condition-dependent corrections:

- one offset correction;
- nine sine-coefficient corrections;
- nine cosine-coefficient corrections.

The primary R5 arms keep the PF-A coefficient surface frozen. Two ablations
allow either the offset plus orders `1` and `3`, or the complete surface, to
move through a separately masked `anchor_surface_delta`. The original surface
always remains an immutable serialized buffer.

## Conceptual Structure

```text
setpoint condition + angle
          |
          +-------------------------------+
          |                               |
          v                               v
causal PF-A coefficient surface     learned branch
          |                               |
          v                               v
 explicit analytical curve        explicit residual/direct curve
          |                               |
          +---------------+---------------+
                          |
                          v
                   combined TE curve
```

The direct R1 controls use only the right-hand learned path.

## Training Objective

Every learned candidate uses:

```text
L_data = mean((normalized_prediction - normalized_target)^2)
```

Only A01 and A02 add:

```text
L_total = L_data + lambda_energy * mean(normalized_residual^2)
```

The immutable energy weights are:

- zero: `0`;
- weak: `0.01`;
- moderate: `0.10`.

There is no coefficient-target loss, harmonic-target loss, derivative loss,
periodic loss, physical-equation loss, or adaptive weighting in Stage 4.

## Capacity And Parameter Matching

| Pair | Direct parameters | Hybrid parameters | Mismatch |
| --- | ---: | ---: | ---: |
| C01 / H01-H03 | 1,825 | 1,825 | 0.00% |
| C02 / H02-H04 | 7,745 | 7,745 | 0.00% |
| C03 / H05 | 1,485 | 1,513 | 1.85% |
| C04 / H06 | 6,901 | 6,857 | 0.64% |
| C05 / H07 | 1,825 | 1,843 | 0.98% |
| C06 / H08 | 7,139 | 7,187 | 0.67% |

Every primary pair passes the predeclared `5%` gate.

## Implementation Map

### Model

`scripts/models/data_only_residual_capacity_network.py` defines
`DataOnlyResidualCapacityNetwork`.

Important methods are:

- `_build_analytical_design_tensor`: constructs the explicit quadratic
  setpoint basis;
- `_resolve_anchor_coefficient_matrix`: exposes frozen or masked adjusted
  anchor coefficients;
- `_reconstruct_from_coefficient_tensor`: performs explicit Fourier
  reconstruction;
- `_compute_anchor_dictionary`: returns frozen and adjusted analytical
  contributions;
- `_compute_basis_residual_dictionary`: reconstructs R4;
- `_compute_coefficient_residual_dictionary`: reconstructs R5;
- `compute_auxiliary_output_dictionary`: exposes the complete decomposition.

### Factory

`scripts/models/model_factory.py` registers model type
`data_only_residual_capacity` and accepts both legacy nested PF-A payloads and
the Stage 4 causal top-level surface payload.

### Training

`scripts/training/transmission_error_regression_module.py`:

- consumes the model auxiliary decomposition;
- adds the optional residual-energy term;
- records Stage 2 raw-loss, EMA, gradient-norm, gradient-cosine, and update
  diagnostics;
- excludes every `requires_grad=False` parameter from AdamW state.

### Campaign And Validation

- campaign preparation:
  `prepare_wave52r_stage4_data_only_residual_capacity_ladder_campaign.py`;
- deterministic validator:
  `validate_stage4_model_and_campaign.py`;
- campaign manifest and eighteen queue configurations under
  `config/training/data_only_residual_capacity/campaigns/`.

## Preflight Evidence

The deterministic implementation preflight proves:

- all `18` configurations instantiate through the model factory;
- R1 never calls the analytical path;
- R2-R5 frozen hybrids reproduce PF-A with maximum initialization error `0`;
- R3 remains at or below `0.016873775 deg` under saturating output;
- R4 reconstruction error is `2.33e-10 deg`;
- R5 reconstruction error is `1.40e-9 deg`;
- partial unfreezing reaches only offset and orders `1` and `3`;
- the full-unfreeze model preserves the frozen surface buffer;
- frozen parameters are absent from optimizer groups;
- all synthetic-batch losses and gradients are finite;
- same-seed DataLoaders have identical SHA-256 fingerprints;
- a different seed changes the shuffled-order fingerprint;
- every primary control/hybrid pair passes the parameter gate.

The real-dataset one-batch and launcher preflights remain separate execution
gates before full training.

## Advantages

- separates analytical and learned contributions;
- makes direct-versus-residual capacity comparisons fair;
- starts hybrids at the exact analytical prediction;
- permits hard physical-unit bounds without calling them physical laws;
- supports explicit coefficient and low-rank inspection;
- keeps deployment-facing arithmetic visible;
- provides a clean baseline for later physics-guided stages.

## Disadvantages And Risks

- PF-A is a grey-box approximation, not a first-principles contact model;
- an unconstrained residual can still cancel the anchor opaquely;
- pointwise data loss does not guarantee curve-shape or phase quality;
- the R4 basis is dataset-derived and may omit useful broadband content;
- partial or full anchor unfreezing can undermine interpretability;
- a low scalar error does not prove a stable or deployable residual;
- this stage cannot attribute any gain to physics.

## Decision Boundary

No hybrid is promoted merely because it wins the campaign leaderboard.
Promotion requires full-resolution supported-core evidence against both R0 and
the matched R1 control, no material curve-first regression, bounded and finite
decomposition, and no opaque cancellation.

If no arm passes, Stage 4 closes as a useful negative result. Later PINN stages
must then treat residual architecture value as unproven rather than assuming
that the analytical anchor automatically helps a network.
