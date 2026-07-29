# Stage 15 TwinCAT Deployment Preparation

## Status

`H04` is export-prepared but not deployment-ready. The Python/ONNX and static
PLC-reference parity gates pass on all 97 frozen forward conditions. Official
curve-first verification is complete without promotion: H04 improved PF-A and
selected shape metrics but did not displace the periodic GRU. TwinCAT
compilation, execution-time measurement, and PLC runtime replay remain
pending. No PLC runtime claim is made.

## Inference Graph

The forward-only H04 graph is:

```text
nominal output torque setpoint
absolute input speed setpoint
nominal oil-temperature setpoint
  -> input validity and finite-value checks
  -> frozen Stage 5 normalization
  -> deep 64-64-32 tanh correction network
  -> per-coefficient tanh bounds

same three raw setpoints
  -> frozen quadratic PF-A coefficient surface

PF-A coefficients + bounded learned corrections
  -> corrected offset and sine/cosine coefficients
  -> explicit orders 1, 3, 39, 40, 78, 81, 156, 162, 240
  -> deterministic harmonic reconstruction at the current output angle
  -> configurable output saturation
  -> TE prediction and diagnostic outputs
```

The runtime path must not use measured TE, target-derived features, future
samples, or a validation/test-derived parameter.

## Inspectable Intermediate Quantities

The export contract must expose:

- signed torque, absolute speed, and oil temperature before normalization;
- normalized condition vector;
- 19 PF-A coefficients;
- 19 raw network outputs;
- 19 bounded coefficient corrections;
- 19 final coefficients;
- analytical-only reconstructed TE;
- learned correction contribution;
- final unsaturated and saturated TE;
- input-valid, in-envelope, saturation-active, and model-valid flags.

The coefficient order is frozen as:

```text
[offset,
 sin(1), cos(1),
 sin(3), cos(3),
 ...,
 sin(240), cos(240)]
```

Changing this order is a model-contract break.

## Runtime State

H04 is non-temporal and therefore has no learned recurrent state. TwinCAT state
initialization is limited to:

- clearing prior diagnostic flags;
- validating that the coefficient and normalization arrays have loaded;
- initializing output and intermediate arrays to zero;
- holding compensation disabled until input validity is true.

This is materially simpler than the accepted GRU path. It does not remove the
need to validate task timing and online behavior.

## Operating Envelope And Saturation

The model is valid only for forward rotation and the polished-setpoint training
contract. The exported runtime must check the Stage 4 causal setpoint envelope
before enabling compensation. Out-of-envelope behavior must be explicit:

1. set `in_envelope := FALSE`;
2. retain the analytical PF-A output as the inspectable fallback;
3. disable the learned correction unless an approved bounded extrapolation
   policy is later documented;
4. log which feature violated the envelope.

Final TE saturation must be configurable and applied after harmonic
reconstruction. Saturation thresholds must be derived from training-only or
approved engineering limits, not tuned on the official test surface.

## Numerical Parity Contract

Parity uses one frozen payload containing all 97 forward test conditions and a
declared set of angular samples. It compares:

| Layer | Required comparison |
| --- | --- |
| Python checkpoint | reference coefficients and TE |
| ONNX Runtime | normalized inputs, corrections, final coefficients, TE |
| PLC implementation | the same intermediates and final TE |

The initial numerical tolerances are:

- coefficient maximum absolute difference: `1e-6 deg`;
- reconstructed TE maximum absolute difference: `2e-6 deg`;
- no non-finite value;
- identical validity and saturation flags.

The completed Python/ONNX comparison observed:

- reconstructed curve maximum difference: `2.2351742e-8 deg`;
- final coefficient maximum difference: `3.7252903e-9 deg`;
- bounded correction maximum difference: `2.3283064e-10 deg`.

The independent float32 PLC-reference emulator observed:

- reconstructed curve maximum difference: `2.9802322e-8 deg`;
- final coefficient maximum difference: `7.4505806e-9 deg`;
- bounded correction maximum difference: `2.3283064e-10 deg`.

Both static gates pass their declared tolerances. The generated Structured Text
and parameter archive are preparation evidence, not TwinCAT runtime evidence.

If the PLC numeric format or trigonometric implementation cannot satisfy these
limits, the tolerance may be revised only through a documented engineering
analysis. It must not be relaxed solely to pass a failing export.

## TwinCAT Integration Choice

The preferred first integration is an explicit deterministic coefficient and
harmonic-reconstruction graph, aligned with the existing TestRig
Polynomial-Fourier implementation and its inspectable intermediate quantities.
The newer asynchronous Machine Learning Server path remains an alternative for
the learned network block, but asynchronous execution must not silently change
the compensation timing contract.

The intended task interface retains the test-rig semantics already documented
in the reference material:

- encoder zeroing completes before TE use;
- `DataValid` gates extraction and compensation evidence;
- the ML task does not block the high-priority control task;
- raw and compensated TE remain separately observable.

## Acceptance Gates

Deployment acceptance requires all of the following:

1. H04 passes the official forward multi-index curve-first comparison.
2. Python checkpoint replay matches the frozen Stage 5 payload.
3. ONNX reproduces Python within the declared coefficient and TE tolerances.
4. PLC reproduces the same frozen payload and intermediate quantities.
5. Worst-case execution time fits the selected TwinCAT task budget.
6. envelope, invalid-input, saturation, and fallback behavior are exercised.
7. online compensation is validated with encoder-zeroing and `DataValid`
   semantics.

Until these gates pass, H04 remains an exploratory Stage 15 candidate even if
its offline centered-shape score is favorable.

Current status:

- Python checkpoint replay: passed;
- Python/ONNX parity: passed;
- independent PLC-reference parity: passed;
- official forward curve verification: completed without promotion;
- TwinCAT compile and runtime parity: pending.
