# Polynomial-Fourier Common-Split Benchmark

## Overview

This technical project prepares the first analytical verification step of the
Wave 5.2 full-PINN program. It will reproduce and compare three distinct
Polynomial-Fourier Transmission Error formulations on identical forward and
backward dataset splits:

1. the Bauer complete quadratic coefficient law;
2. the recovered MATLAB workflow with ONNX-predicted Fourier coefficients;
3. the existing PLC implementation with its explicit polynomial evaluator.

The benchmark is not a training campaign and will not implement a PINN. Its
purpose is to establish a common, inspectable analytical reference from which
the first physics residual can be selected.

The broader Wave 5.2 program will remain open to multiple PINN variants derived
from the complete ingested theory. Candidate breadth is intentionally not
restricted to one final architecture. Experimental isolation remains required:
each physical mechanism must first be tested independently before mechanisms
are combined.

## Technical Approach

### Common Data Contract

The benchmark will use immutable, condition-level `Fw` and `Bw` partitions
derived from the canonical repository datasets. All three formulations will be
evaluated on the same curves, angular grid, units, direction labels, and
held-out conditions.

The data audit will establish:

- dataset root and manifest provenance;
- input-side and output-side angular conventions;
- TE units and sign convention;
- speed, torque, and temperature units;
- direction mapping;
- interpolation and extrapolation boundaries;
- leakage-safe fitting and held-out conditions.

### Bauer Reproduction

The implementation will reconstruct:

- spatial resampling;
- linear detrending;
- Hamming-window application;
- zero-padding and single-sided spectrum normalization;
- sine and cosine coefficient extraction;
- mean-offset estimation;
- complete quadratic coefficient surfaces in torque, speed, and temperature;
- separate `Fw` and `Bw` parameter sets;
- Fourier curve reconstruction with explicit intermediate coefficients.

The source paper's reducer-specific harmonic orders will not be transferred
automatically. The benchmark will compare paper orders, locally observed
orders, and the orders already encoded in the repository implementations.

### Recovered ONNX Reproduction

The recovered MATLAB path will be translated into a repository-owned,
inspectable Python evaluation path without retraining its ONNX models. The
benchmark will preserve:

- coefficient-model identity;
- input ordering and preprocessing;
- `A0`, amplitude, and phase outputs;
- orders `1`, `39`, and `40`;
- cosine-based reconstruction;
- exact canonical ONNX provenance.

### PLC Law Reconstruction

The PLC implementation will be audited term by term:

- direction-selection logic;
- coefficient table provenance;
- 35-term polynomial evaluator;
- offset, amplitude, and phase evaluation;
- orders `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`;
- angle and phase conventions;
- expected runtime units and validity domain.

The Python benchmark will reproduce the PLC calculations without changing the
reference PLC source.

### Comparison Surfaces

Every variant will expose:

- per-curve raw MAE and RMSE;
- mean-centered shape error;
- mean-offset error;
- amplitude and phase error by harmonic;
- dominant-order retention;
- derivative and continuity evidence;
- per-condition results;
- separate aggregate `Fw` and `Bw` results;
- coefficient and intermediate-value traces;
- measured-versus-predicted curve plots;
- computational and TwinCAT deployment implications.

Scalar MAE alone will not select the analytical reference.

### Multiple-PINN Continuation

The benchmark will feed a formulation catalog rather than force a single
terminal model. Later, separately approved pilots may include:

- Polynomial-Fourier residual PINN;
- harmonic-periodicity and phase-consistency PINN;
- quasi-static compliance PINN;
- Bouc-Wen or alternative hysteresis-state PINN;
- bidirectional TE and global-lost-motion compatibility PINN;
- acceleration and load-inertia dynamic PINN;
- reduced contact-stiffness or load-sharing PINN;
- energy- or efficiency-consistency PINN;
- wear-aware latent-state PINN;
- electromechanical consistency PINN when motor-current signals exist;
- hybrid combinations only after their individual contributions are proven.

Detailed contact, wear, MMT, and electromechanical formulations may initially
serve as synthetic or offline oracles when their required variables are not
available during inference. This preserves all recovered theory as useful
evidence without disguising unobserved quantities as measured physics.

## Involved Components

Planned implementation surfaces:

- `scripts/analysis/polynomial_fourier_benchmark/`
- `config/analysis/polynomial_fourier_benchmark/`
- `output/analysis/polynomial_fourier_benchmark/`
- `doc/reports/analysis/model_development_waves/wave_5_2/polynomial_fourier_benchmark/[2026-07-25]/`
- `doc/scripts/analysis/polynomial_fourier_benchmark/`

Canonical inputs:

- `reference/te_modeling/bibliography/polynomial_fourier/`
- `reference/te_modeling/implementations/polynomial_fourier_te_predictor_matlab/`
- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/06_PolynomialFourierSeriesModel/`
- `doc/reference_summaries/10_Polynomial_Fourier_TE_Model_Project_Summary.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/sharepoint_reference_evidence_matrix.md`
- canonical dataset and split manifests selected during implementation

No campaign state, model registry, accepted program leader, or training
artifact will be modified by this analytical benchmark.

## Implementation Steps

1. Audit the canonical dataset schemas and select immutable common `Fw` and
   `Bw` manifests.
2. Write the equation, unit, coordinate, sign, and input-observability contract.
3. Implement the Bauer preprocessing and quadratic coefficient law.
4. Implement the ONNX coefficient inference and harmonic reconstruction path.
5. Reconstruct the PLC evaluator and compare term-level intermediate values.
6. Add deterministic synthetic tests for coefficient evaluation, harmonic
   reconstruction, phase wrapping, and direction selection.
7. Run all three formulations on the common held-out curves.
8. Generate machine-readable metrics, coefficient traces, and curve plots.
9. Produce the analytical comparison report and formulation recommendation.
10. Update the Wave 5.2 evidence matrix, intake register, backlog, ledger, and
    master summary if the result changes the program decision.
11. Stop and request approval before preparing any PINN training campaign.

## Approval And Training Gates

Implementation may begin only after explicit user approval of this technical
document.

The benchmark itself is non-training analytical work. Any subsequent PINN
pilot will require:

- its own approved technical document;
- a campaign planning report;
- model and physics-loss documentation;
- campaign YAML and local or remote launcher package;
- explicit approval before training;
- multi-index curve-first verification before promotion.

## Verification Plan

- deterministic equation and reconstruction tests;
- ONNX runtime input and output contract checks;
- PLC term-by-term parity checks;
- manifest disjointness and leakage checks;
- `Fw` and `Bw` common-condition coverage report;
- Markdown style and Markdownlint on touched documentation;
- Python compilation and repository-specific analytical tests;
- `git diff --check`;
- Sphinx warning-free build if the implementation enters portal scope.
