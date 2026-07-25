# TE Modeling Reference Library Summary

## Purpose

This document describes the curated Transmission Error modeling library under
`reference/te_modeling/`. The library consolidates the SharePoint source bundle
received on 2026-07-25 and separates scientific literature, internal design
notes, and executable reference implementations.

The source files remain the authority. The companion summaries identify what
each source contributes to this repository and, just as importantly, which
claims or equations cannot yet be used in a Wave 5.2 full-PINN implementation.

## Ingestion Result

- 48 source files were inventoried.
- 31 unique files were moved into the curated library.
- 17 byte-identical duplicates were not copied again.
- Every move and duplicate decision was verified with SHA-256.
- The source staging tree contains no remaining files.
- The exact path, size, and hash record is stored in
  `reference/te_modeling/source_inventory.yaml`.

The 17 duplicate files consisted of:

- one copy of the MMT paper already stored as
  `reference/MMT_TEModeling.pdf`;
- sixteen ONNX models already stored in the recovered RCIM asset archive.

No source was discarded merely because its title was similar to another
document.

## Library Structure

| Area | Contents | Primary use |
| --- | --- | --- |
| `bibliography/harmonic_transmission_error/` | Harmonic-drive kinematic error and synchronous TE modeling | Mechanism-linked periodic structure |
| `bibliography/hysteresis_and_backlash/` | Hysteresis, torsional friction, stiffness, and lost-motion studies | Memory, direction, and load-path constraints |
| `bibliography/lookup_table_compensation/` | Offline robot-joint error compensation | Separation of compliance and kinematic error |
| `bibliography/machine_learning_compensation/` | State-dependent and preloaded-drive compensation | Hybrid analytical and learned compensation patterns |
| `bibliography/polynomial_fourier/` | Bauer paper and internal OneNote export | First bounded semi-analytical Wave 5.2 candidate |
| `theoretical_mechanics/kinematics_and_transmission_error/` | Bidirectional TE and positioning-accuracy theory | Forward, backward, and global lost-motion compatibility |
| `theoretical_mechanics/dynamics_hysteresis_and_efficiency/` | Dynamic TE, hysteresis, efficiency, and electromechanical coupling | Dynamic and state-dependent physics |
| `theoretical_mechanics/numerical_and_fea_models/` | Tolerance, wear, finite-element, and surrogate studies | Latent geometry, wear, and synthetic-oracle design |
| `implementations/mmt_linkage_matlab/` | Simplified MMT-to-harmonic MATLAB demonstrator | Diagnostic mapping of component errors to orders |
| `implementations/polynomial_fourier_te_predictor_matlab/` | ONNX coefficient-prediction MATLAB workflow | Recovered hybrid harmonic predictor |

## Main Knowledge Distilled

The source collection supports six conclusions.

1. TE is naturally decomposable into a periodic angular component, a mean or
   offset component, and operating-condition-dependent changes.
2. Forward and backward behavior cannot be collapsed safely when backlash,
   hysteresis, lost motion, or load-path reversal is relevant.
3. Torque, velocity, temperature, acceleration, and load inertia affect
   different parts of the phenomenon. Speed alone is not a complete dynamic
   state.
4. Several strong mechanical models require geometry, contact, stiffness,
   wear, friction, or component-error variables that are absent from the
   current dataset.
5. Harmonic structure is physically motivated, but a Fourier head or harmonic
   feature set is not by itself a full PINN.
6. The best immediately auditable candidate is the direction-specific
   Polynomial-Fourier formulation. It is semi-analytical and falsifiable with
   the existing operating variables, while more complete contact or MMT laws
   require additional evidence.

## Companion Documentation

- `doc/reference_summaries/10_Polynomial_Fourier_TE_Model_Project_Summary.md`
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`
- `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
- `doc/reference_summaries/14_MMT_Linkage_Matlab_Project_Summary.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/sharepoint_reference_evidence_matrix.md`

## Use Rule

These sources may inform equation audits, analytical baselines, synthetic
oracles, and bounded experiment plans. They do not authorize implementation or
training. A source-specific equation must first pass the Wave 5.2 observability,
causality, unit, identifiability, and falsification gates.
