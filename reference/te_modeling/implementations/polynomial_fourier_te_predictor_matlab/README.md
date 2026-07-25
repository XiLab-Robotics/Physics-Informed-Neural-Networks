# Polynomial-Fourier TE Predictor MATLAB Reference

This directory preserves the MATLAB predictor and five experimental curves
from the imported SharePoint package.

## Runtime Path

`TE_Predictor_FromONNX.m`:

1. defines speed, output torque, and oil temperature;
2. loads ONNX regressors through MATLAB's Python bridge and `onnxruntime`;
3. predicts `A0`, the amplitudes for orders `1`, `39`, and `40`, and their
   phases;
4. reconstructs the curve as:

```text
TE(theta) = A0
          + A1  * cos(theta      + phi1)
          + A39 * cos(39 * theta + phi39)
          + A40 * cos(40 * theta + phi40)
```

5. compares the prediction against an experimental CSV.

The regressor input order is `[speed_rpm, oil_temperature_deg_c,
output_torque_nm]`.

## ONNX Dependencies

The 16 ONNX files found beside this MATLAB code were byte-identical to the
canonical RCIM paper-release models already stored under:

- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`.

They were not duplicated here. The current script retains its original local
filenames for provenance and therefore requires either a copied runtime bundle
or path adaptation before execution from this directory.

## Important Distinction

This implementation is not the Bauer quadratic polynomial model. It predicts a
small set of Fourier coefficients with heterogeneous ONNX regressors. The
Bauer paper instead fits quadratic polynomial surfaces for every selected
amplitude, phase, and offset. Both reconstruct TE harmonically, but their
coefficient models and harmonic sets differ.
