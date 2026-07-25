# MMT Linkage MATLAB Project Summary

## Source Set

- Canonical paper: `reference/MMT_TEModeling.pdf`
- MATLAB demonstrator:
  `reference/te_modeling/implementations/mmt_linkage_matlab/`

The SharePoint paper was byte-identical to the canonical repository copy and
was therefore not duplicated.

## Implemented Geometry

The MATLAB demonstrator fixes:

```text
z1 = 22
z2 = 44
z4 = 39
z5 = 40
transmission ratio = 81
```

It represents TE through output orders `1`, `3`, `39`, `40`, and `81`.

## Error-To-Order Mapping

| MATLAB parameters | Intermediate term | Output order |
| --- | --- | ---: |
| `EH` | `f4` | 1 |
| `Ea`, `Ec` | `f2`, `f4` | 3 |
| `Ev`, `delta` | `f3` | 39 |
| `dr`, `dlR`, `AP` | `f3` | 40 |
| `Eb1`, `Eb2`, `dtheta` | `f1` | 81 |

The final demonstrator combines the terms as:

```text
Derr = 1 + (z1 + z2) / (z2 * z4)

TE =
    (-(f1 / z4) - (mean(f2) / z4) + f3 + mean(f4)) / Derr
    + C0
```

`plot_spectrum.m` provides the associated frequency-domain inspection, while
`TE_experimental.csv` supplies one comparison curve.

## What The Demonstrator Establishes

- It preserves an interpretable mapping from component-error classes to
  characteristic output harmonics.
- It offers a compact mechanism-aware diagnostic for checking whether measured
  spectra contain compatible orders.
- It shows how high-speed and low-speed stage terms enter a combined TE curve.

## What It Does Not Establish

- It is not a complete reproduction of the paper's multi-loop derivation.
- It does not estimate condition-dependent component errors from independent
  measurements.
- Several error magnitudes are entered manually.
- It does not establish identifiability of the individual error sources.
- It does not prove causal availability of its parameters at inference time.
- Matching a measured spectrum does not prove that the selected component
  errors are the true physical cause.

## Relationship To The MMT Diagnostic

The repository's leakage-safe diagnostic found no held-out gain from the
available geometry-locked MMT signatures over metadata and shuffled controls.
The negative result means that the present condition-invariant parameterization
does not add explanatory information. It does not invalidate the paper or the
harmonic source mapping.

Paper-faithful MMT remains deferred until independent component-error
measurements or a validated causal contact-state reconstruction is available.
The MATLAB implementation is retained as:

- an interpretable harmonic diagnostic;
- a source of synthetic equation tests;
- a future comparison oracle if the missing physical parameters become
  available.

It must not be presented as an authorized full-PINN implementation.
