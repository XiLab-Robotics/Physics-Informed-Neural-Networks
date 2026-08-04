# Wave 5.2R A02 Export And TwinCAT Qualification

## Overview

This document defines the approval-gated deployment-preparation path for
`wave52r_integrated_a02_seed_314159`, the verified offline forward specialist
and routed global candidate selected by the completed Wave 5.2R Integrated
Specialist TE Curve Verification Pipeline review.

The work is a non-training qualification package. It must preserve the exact
campaign topology: global K01 seed `271828` is the temporal backbone, forward
H08 seed `161803` supplies the centered harmonic candidate curve, and the A02
seed `314159` gate applies that contribution only on `Fw`. On `Bw`, the H08
contribution remains exactly zero and the result must reproduce global K01.

A02 is not currently a self-contained deployable graph. The campaign model
received precomputed K01 and H08 curves as inputs. The first engineering task
is therefore to reconstruct and freeze the complete inference contract before
choosing whether the deliverable should use one composed ONNX graph or an
explicit multi-model package with PLC-visible composition.

This package can establish export readiness, host-side numerical parity, and
static PLC integration evidence. TwinCAT build, target activation, Machine
Learning Server availability, ADS communication, latency, and commissioned
runtime compensation remain separate evidence gates.

The user approved this technical document before implementation on
`2026-08-04`.

## Technical Approach

### 1. Freeze Provenance And Runtime Semantics

Record the exact A02, K01, and H08 checkpoints, SHA-256 digests, model
configuration, normalization constants, harmonic orders, branch bound, tensor
shapes, and direction convention. Preserve speed, applied torque, oil
temperature, angular position, encoder-zeroing provenance, and `DataValid`
dataset boundaries in the package documentation.

The runtime contract must expose the following quantities independently:

- K01 prediction curve and recurrent hidden state;
- H08 prediction curve without mean or `a0` transfer;
- per-curve K01 and H08 centered components;
- normalized operating condition;
- learned scalar A02 H08 gate;
- deterministic forward direction gate;
- bounded H08 residual;
- final TE prediction.

### 2. Select The Export Topology From Evidence

Evaluate two bounded representations against the exact campaign replay:

1. a composed ONNX graph containing K01, H08, A02 normalization, centering,
   direction gating, clamping, and final addition;
2. an explicit package that keeps the already exportable K01 and H08 models
   separate and performs the small A02 gate and curve composition in an
   inspectable host or PLC layer.

The explicit package is the initial reference architecture because the
standalone TF3820 project already contains dedicated K01 and H08 runners and
because it preserves intermediate signals. A monolithic export may be added
only if it reproduces the same state, chunk, centering, and direction
semantics without hiding required diagnostics.

The first TwinCAT-facing contract is fixed-grid full-curve preparation and
replay. K01 produces 32-sample stateful chunks, while H08 produces a
2048-sample curve. The package must assemble the complete K01 revolution,
compute curve means deterministically, apply the A02 residual, and then expose
the resulting curve to the standalone replay path. This does not yet claim
causal continuously varying online compensation.

### 3. Build Layered Numerical Qualification

Create persistent repository-owned export and validation tooling that checks:

- reconstructed PyTorch composition against the original A02 checkpoint and
  saved campaign predictions;
- exported ONNX component or composed-graph output against PyTorch;
- float32 PLC-reference arithmetic against the ONNX result;
- exact zero H08 residual on every backward case;
- fixed tensor shapes, finite outputs, recurrent-state reset, 32-sample K01
  chunk continuity, 2048-sample curve assembly, and deterministic replay;
- parity on the official 194-curve global test surface and focused difficult
  forward/backward conditions.

Validation thresholds must be declared before results are inspected. No
artifact enters the curated `models/` archive until provenance, ONNX Runtime
parity, PLC-reference parity, and package validation all pass.

### 4. Extend The Standalone TF3820 Harness

After export qualification, extend the maintained standalone module with an
explicit A02 orchestration path that reuses the existing K01 and H08 runners.
Expose operator-visible K01, centered H08 difference, learned gate, direction
gate, residual, final prediction, busy/error states, and reset behavior.

The standalone integration must retain manual and CSV replay modes and must
not alter the accepted model behavior or registry by default. Any changes in
the nested TwinCAT repository require their own narrow commit before the
parent gitlink is updated.

### 5. Preserve Evidence Boundaries

Report each achieved level separately:

- Python reconstruction parity;
- ONNX Runtime parity;
- float32 PLC-reference parity;
- static TwinCAT source/package validation;
- TwinCAT XAE build;
- activated-target inference;
- commissioned TestRig compensation.

Success at one level must not be presented as evidence for a later level.

## Involved Components

- `output/training_runs/integrated_specialist_models/2026-08-03-17-49-51__a02__seed_314159/`
  Exact selected A02 checkpoint and prediction evidence.
- `output/training_runs/temporal_analytical_residual_models/2026-07-31-11-11-39__stage9_k01__seed_271828/`
  Frozen global K01 backbone used by the campaign.
- `output/training_runs/complex_harmonic_coefficient_residuals/2026-07-31-10-45-42__stage5_h08__seed_161803/`
  Frozen forward H08 specialist used by the campaign.
- `scripts/models/integrated_specialist_residual_network.py`
  Current A02 branch and component semantics.
- `scripts/export/wave_5_2r/`
  Planned home for persistent A02 export and parity tooling.
- `models/polished_dataset/setpoints/integrated_specialist_a02/global/`
  Proposed curated archive destination after all pre-archive gates pass.
- `output/deployment/wave52r_integrated_specialist_a02/`
  Proposed immutable validation and generated-package evidence root.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/`
  Maintained standalone TF3820 harness containing the existing K01 and H08
  runners and the later A02 orchestration implementation.
- `doc/scripts/deployment/`
  Planned operator note for export, parity, model copying, and TwinCAT checks.
- `doc/guide/project_usage_guide.md` and the canonical Sphinx source tree
  User-facing documentation targets after runnable behavior exists.

No training configuration, training campaign, or accepted program registry is
part of this scope.

## Implementation Steps

1. Obtain explicit approval for this technical document before modifying any
   export, model, deployment, PLC, guide, or portal implementation file.
2. Audit and hash the exact A02/K01/H08 checkpoints and reconstruct the full
   selected inference path from campaign code and artifacts.
3. Write the export contract and fixed test-vector manifest, including tensor
   names, shapes, units, state/reset rules, direction semantics, and numerical
   tolerances.
4. Implement persistent Python tooling for the explicit multi-model A02
   package and evaluate whether a semantically equivalent composed ONNX export
   is supportable.
5. Run PyTorch-to-campaign, ONNX Runtime, float32 PLC-reference, backward-zero,
   chunk-continuity, and full 194-curve parity checks.
6. If every pre-archive gate passes, create the curated A02 archive with source
   snapshots, hashes, model card, and reproducible validation references.
7. Extend the standalone TF3820 catalog, data types, orchestration function
   block, replay controls, validator, and operator documentation for A02.
8. Run static PLC package checks and preserve the result without claiming an
   XAE build or runtime qualification.
9. Stop for operator-side TwinCAT build and runtime testing; record build,
   activation, ADS, license, latency, and replay evidence independently.
10. Update the usage guide, Sphinx portal, live backlog, and status ledger to
    the evidence level actually achieved, then run Python, model-package,
    Markdown, Sphinx, and relevant PLC validation checks.
11. Report completion and wait for explicit approval before creating the
    nested TwinCAT commit and the parent repository commit. Do not push unless
    requested.

No subagent is planned for this implementation. If parallel review becomes
useful, its name and exact scope will be proposed to the user before launch.
