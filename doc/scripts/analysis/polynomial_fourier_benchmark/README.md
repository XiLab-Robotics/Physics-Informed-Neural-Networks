# Polynomial-Fourier Common-Split Tooling

## Purpose

These non-training analysis scripts create and validate the paired forward and
backward operating-condition split used by the Wave 5.2 Polynomial-Fourier
benchmark.

The manifest builder indexes the canonical polished dataset, checks the exact
CSV schema, pairs `Fw` and `Bw` curves by nominal speed, torque, and
temperature, assigns the pair to one split, and records a SHA-256 hash for
every source file.

## Configuration

The canonical configuration is:

`config/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml`

It declares the dataset root, direction mapping, units, split fractions,
random seed, and output paths.

## Build Command

From the repository root:

```powershell
conda run --no-capture-output -n pinns_env python `
  scripts/analysis/polynomial_fourier_benchmark/build_common_split_manifest.py
```

The command writes:

- `output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml`
- `output/analysis/polynomial_fourier_benchmark/common_split_manifest.csv`
- the dated common-split data-contract report under the Wave 5.2 analysis
  tree.

## Validation Command

Run the full content-addressed validation:

```powershell
conda run --no-capture-output -n pinns_env python `
  scripts/analysis/polynomial_fourier_benchmark/validate_common_split_manifest.py
```

For a faster structural check that retains pairing, leakage, existence, and
file-size validation without recomputing all SHA-256 values:

```powershell
conda run --no-capture-output -n pinns_env python `
  scripts/analysis/polynomial_fourier_benchmark/validate_common_split_manifest.py `
  --skip-content-hashes
```

## Interpretation

The split unit is one nominal operating condition. The condition's `Fw` and
`Bw` files always remain together. A successful validation does not establish
the accuracy of any analytical formulation; it only freezes a fair common
evaluation surface for the later Bauer, ONNX, and PLC reproductions.
