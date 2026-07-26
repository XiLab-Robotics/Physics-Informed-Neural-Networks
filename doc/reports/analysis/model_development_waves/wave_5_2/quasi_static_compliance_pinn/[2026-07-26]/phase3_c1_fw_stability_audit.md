# Phase 3 C1-Fw Stability Audit

## Overview

This audit compares the initial C1-Fw screening run with two reproducibly seeded repeats on the
same immutable 97-curve Fw held-out surface. It combines fitted physical parameters with CVP 1.2
raw, offset, centered-shape, harmonic, phase, and peak-to-peak evidence.

## Reproducibility Contract

The repeat runs preserve architecture, data split, loss weights, and runtime profile. Only
`training.random_seed` changes. `seed_everything(seed, workers=True)` seeds Python, NumPy,
PyTorch, samplers, and DataLoader workers before model creation.

| Run | Seed | Stiffness [Nm/deg] | Raw MAE [deg] | Offset [deg] | Centered [deg] | Harmonic amp [%] | Phase [deg] | P2P [%] | Gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `phase3_c1_linear_compliance_soft_Fw` | screening run | 28275.59 | 0.001843 | 0.000932 | 0.001481 | 34.128 | 21.434 | 10.009 | pass |
| `phase3_c1_fw_seed_271828` | 271828 | 28958.11 | 0.002198 | 0.001350 | 0.001605 | 45.693 | 22.966 | 6.828 | fail |
| `phase3_c1_fw_seed_314159` | 314159 | 27259.39 | 0.001816 | 0.000872 | 0.001513 | 41.194 | 20.030 | 6.384 | pass |

## Aggregate Stability

- fitted stiffness mean: 28164.36 Nm/deg;
- fitted stiffness population CV: 0.0248;
- per-run curve-first gate passes: 2/3;
- all stiffness-bound losses are zero: `true`;
- accepted-reference replacement: `false`.

The peak-to-peak column remains visible as a separate caution. It is not hidden by the aggregate
gate.

## Decision

C1-Fw is not retained as a stable Phase 3 physical ingredient. The linear-compliance residual
remains documented evidence only.

This is a Phase 3 ingredient-selection decision, not an official TE Curve Verification Pipeline
promotion and not a claim that the C1 model is the best deployed predictor.

## Machine-Readable Evidence

- `output/analysis/pinn_program_compliance/phase3_c1_fw_stability_audit.yaml`
- `output/analysis/pinn_program_compliance/phase3_c1_fw_stability_audit.csv`
