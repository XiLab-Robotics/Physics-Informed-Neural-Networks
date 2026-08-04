# Wave 5.2R Integrated Specialist Residual Model

## Model Description

The integrated specialist residual model is a compact empirical correction
layer above a frozen K01 temporal prediction. It tests complementary behavior
without averaging complete models or importing failed candidates as trusted
experts. The model belongs to Wave 5.2R and is not a PINN or Wave 6 model.

## Operating Principle

The final curve is the frozen K01 curve plus independently bounded,
mean-centered residuals. A deterministic direction flag enables the H08
residual on `Fw` and makes it exactly zero on `Bw`. H04 contributes only
through an explicit centered analytical-control difference. Learned shape and
condition branches reconstruct fixed sine/cosine orders from causal setpoints.

All learned heads initialize to zero. Before training, the output is therefore
numerically identical to K01. The model exposes K01 mean, K01 centered curve,
direction gate, every specialist residual, and final prediction separately.

## Conceptual Structure

```text
frozen K01 curve ------------------------------+----> final TE
                                               |
forward flag -> centered H08 difference -> bound+
                                               |
condition -> H04 centered gate ----------> bound+
                                               |
condition -> harmonic shape head --------> bound+
                                               |
condition -> Stage 10 feature library ---> bound+
```

The H08 path never transfers its mean or `a0` coefficient. The condition
library uses normalized torque, speed, temperature, direction, and explicit
polynomial interactions. Its thresholded form is a compactness control, not a
claim of a discovered physical law.

## Project Advantages

- Starts from the strongest verified K01 cross-surface offline baseline.
- Preserves direction routing and blocks the known H08 backward defect.
- Exposes small, inspectable residuals instead of one opaque ensemble output.
- Supports exact single-branch ablations and conditional integration.
- Uses fixed tensor shapes and registered buffers suitable for later export.
- Keeps target-derived quantities out of runtime inputs.

## Project Disadvantages And Risks

- Frozen K01 remains the dominant recurrent cost and retains its state and
  chunk contract.
- Adding specialists can regress offset, envelope, closure, or robustness even
  when scalar MAE improves.
- H04 and Stage 10 ingredients are empirical controls, not identified physics.
- The campaign runner currently supplies frozen expert curves outside the
  integrated module; a deployable package would need an explicitly composed
  export graph and parity evidence.
- Offline, ONNX, static PLC, and commissioned TwinCAT evidence remain separate.

## Implemented Python Components

`scripts/models/integrated_specialist_residual_network.py` defines
`IntegratedSpecialistResidualNetwork`. Its main methods are:

- `normalize_condition`, which applies immutable training-only scaling;
- `build_condition_library`, which exposes dense or compact causal features;
- `reconstruct_centered_harmonics`, which creates zero-mean residual curves;
- `forward_components`, which returns every branch and routing value;
- `forward`, which returns a tensor-only final prediction for export tooling.

`scripts/campaigns/wave_5_2/run_wave52r_integrated_specialist_model.py`
replays frozen checkpoints, aligns directional outputs, trains single-branch
arms, applies validation-only advancement gates, conditionally constructs
`A08`, and performs one final test evaluation after selection freezes.

The PowerShell launcher and campaign YAML provide local/remote synchronization,
approval enforcement, immutable paths, seeds, thresholds, and artifact
contracts.

## Current Qualification State

The approved campaign completed all `24 / 24` entries without failure. A02 was
the only branch to pass its forward-specialty and multi-index non-regression
gates at all three seeds. The separate official curve-first review recommends
A02 seed `314159` on `Fw` and as the routed `global` candidate, while K01 seed
`271828` remains recommended on `Bw`. Accepted deployment registries remain
unchanged.

The selected A02 path has now passed exact campaign reconstruction, ONNX
Runtime, and independent float32 PLC-reference parity on all 194 official test
conditions. The maximum errors were `1.4901161e-08 deg`, `5.9604645e-08 deg`,
and `1.6391277e-07 deg`, respectively. Its backward residual and backward
prediction-versus-K01 error were exactly zero.

The curated archive contains the fixed-shape A02 curve composer and explicit
K01/H08 dependencies. Beckhoff TF3820 preparation and the 40-package
standalone catalog pass static validation. A02 has a dedicated full-curve
runner and is not selectable through the generic 39-model pointwise predictor.
TwinCAT XAE build, activated-target inference, timing, end-to-end upstream
curve production, and commissioned TestRig compensation remain pending.
