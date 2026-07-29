# Wave 5.2R Stage 15 H04 Deployment Exports

## Purpose

Two repository-owned scripts prepare and validate the H04 deployment graph
without claiming TwinCAT runtime acceptance:

```text
scripts/export/wave_5_2r/
  export_stage15_h04_onnx_and_validate_parity.py
  build_stage15_h04_plc_reference_package.py
```

Both operate on the hash-locked H04 checkpoint nominated by Stage 14 and the
frozen PF-A causal setpoint anchor.

## Python And ONNX Parity

Run:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/export/wave_5_2r/export_stage15_h04_onnx_and_validate_parity.py
```

The exporter exposes:

- normalized causal condition inputs;
- PF-A analytical coefficients;
- final reconstructed curve;
- final coefficients;
- bounded learned coefficient corrections;
- analytical-only reconstructed curve.

It exports ONNX opset 17 with a dynamic batch axis and validates all outputs
through ONNX Runtime on the 97 frozen forward test conditions.

Observed maximum absolute differences:

| Output | Difference |
| --- | ---: |
| reconstructed curve | `2.2351742e-8 deg` |
| final coefficients | `3.7252903e-9 deg` |
| bounded corrections | `2.3283064e-10 deg` |
| analytical contribution | `2.9802322e-8 deg` |

The declared tolerances are `2e-6 deg` for the reconstructed curve and
`1e-6 deg` for coefficient outputs. Python/ONNX parity passes.

## PLC-Friendly Reference Package

Run:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/export/wave_5_2r/build_stage15_h04_plc_reference_package.py
```

The builder:

- exports all PF-A and neural parameters as float32 arrays;
- generates `GVL_Stage15H04Parameters.st`;
- generates `FB_Stage15H04CoefficientResidual.st`;
- executes an independent loop-by-loop NumPy emulator matching
  IEC 61131-3 `REAL` arithmetic;
- compares every coefficient, correction, and reconstructed curve against
  PyTorch for all 97 conditions.

Observed maximum absolute differences:

| Output | Difference |
| --- | ---: |
| reconstructed curve | `2.9802322e-8 deg` |
| final coefficients | `7.4505806e-9 deg` |
| bounded corrections | `2.3283064e-10 deg` |

Static PLC-reference parity passes. TwinCAT compilation, task-time measurement,
and runtime replay remain pending and must not be inferred from this result.

## Artifacts

The generated package is stored under:

```text
output/validation_checks/wave52r_stage15_deployment_parity/
```

The YAML summaries contain SHA-256 identities for the ONNX model, frozen parity
payload, parameter archive, global parameter declaration, and function block.
