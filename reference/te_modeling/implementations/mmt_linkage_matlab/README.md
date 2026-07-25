# MMT Linkage MATLAB Diagnostic

This directory preserves a simplified MATLAB implementation inspired by the
MMT paper stored at `reference/MMT_TEModeling.pdf`.

## Files

- `main.m`: loads the experimental TE curve, defines geometry and equivalent
  error amplitudes, executes the model, and plots measured versus modeled TE.
- `mmt_linkage_TE.m`: maps equivalent error sources into subsystem terms and
  combines them through the paper's Equation 30 structure.
- `plot_spectrum.m`: compares measured and modeled spatial-order spectra.
- `TE_experimental.csv`: experimental curve used by the diagnostic.

## Implemented Structure

The diagnostic uses the output-angle orders:

- `1`: output-side eccentricity;
- `3`: crank-related effects;
- `39`: cycloidal tooth and center effects;
- `40`: pin and pitch effects;
- `81`: input-stage effects.

The final mapping is:

```text
TE = (-(f1 / z4) - (f2mean / z4) + f3 + f4mean) / Derr + C0
Derr = 1 + (z1 + z2) / (z2 * z4)
```

This is not a complete reproduction of the paper's multi-loop incremental
solver. It is a transparent harmonic-equivalent diagnostic with manually
provided error amplitudes and phases. Its paper-faithful use remains blocked
by unavailable condition-varying component-error and contact-state inputs.
