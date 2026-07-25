# Polynomial-Fourier Common-Split Data Contract

## Overview

This document freezes the first dataset surface of the Wave 5.2
Polynomial-Fourier benchmark. It is a non-training analytical contract for
comparing the Bauer, recovered ONNX, and PLC formulations on exactly the same
paired forward and backward operating conditions.

## Canonical Inputs

- Dataset: `polished_dataset`
- Dataset schema: `polished_setpoint_curve_v1`
- Dataset root: `data/polished_dataset`
- Assignment unit: `paired_operating_condition`
- Random seed: `42`
- Validation fraction: `0.2`
- Test fraction: `0.1`
- Content hash: `SHA-256` for every directional CSV
- Stable split-assignment SHA-256:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`

Nominal speed, torque, and temperature are parsed from each filename and
cross-checked against the speed and temperature parent directories. The exact
ordered CSV schema is checked before a curve enters the manifest.

## Paired Split

| Split | Paired Conditions | Directional Curves |
| --- | ---: | ---: |
| Train | 678 | 1356 |
| Validation | 194 | 388 |
| Test | 97 | 194 |
| Total | 969 | 1938 |

The operating-condition key is shuffled once. Its `Fw` and `Bw` files are then
assigned together. No condition or directional file may appear in more than
one split.

## Units And Coordinates

- `theta`: output-equivalent reducer angle in degrees
- `theta_dot`: measured input or motor-side speed in revolutions per minute
- `tau_load`: measured signed output-side torque in newton-metres
- `T`: measured oil temperature in degrees Celsius
- `theta_TE`: measured transmission error in degrees

The directory direction is authoritative for the `Fw` or `Bw` surface. The
filename values define the nominal operating-condition key; measured
condition channels inside each curve remain available for later formulation
audits and must not be silently replaced by the nominal values.

## Immutable Artifacts

- YAML manifest: `output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml`
  - SHA-256: `1d65c12211de66c2924fe12e4b976983517811610eb45fbf5d1845cf1a215973`
- CSV manifest: `output/analysis/polynomial_fourier_benchmark/common_split_manifest.csv`
  - SHA-256: `32a3a77b8b7a5c49b44c72d16c002d929634026d9294026e163f1b75eb6e39d4`
- Source configuration:
  `config/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml`
  - SHA-256: `3e2c267de626c0ee1f205883f91e896666840e0ffeec02cc8f79c47dfe1cf80a`

The YAML file is the canonical machine-readable manifest. The CSV file is a
flat audit view. Each entry records the nominal condition, split, Fw and Bw
paths, file sizes, and source hashes.

## Validation Gates

The repository validator confirms:

1. exact equality of the Fw and Bw operating-condition sets;
2. one paired entry per nominal condition;
3. split disjointness at condition level;
4. unique directional source paths;
5. exact CSV header compatibility;
6. current source-file sizes and SHA-256 hashes;
7. source-configuration identity and stable assignment signature;
8. agreement between the YAML manifest and flat CSV audit rows;
9. agreement between declared and recomputed split counts.

This contract completes only the common-data portion of benchmark Phase 1.
The Bauer, recovered ONNX, and PLC formulation reproductions remain pending.
