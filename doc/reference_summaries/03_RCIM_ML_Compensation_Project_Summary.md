# RCIM ML Compensation - Project Summary

## Source

- Reference PDF: `reference/RCIM_ML-compensation.pdf`

## Work Objective

The paper proposes a strategy for online modeling and compensation of Transmission Error in industrial servomechanisms using Machine Learning, followed by integration into a Beckhoff TwinCAT PLC for real-time compensation.

## Fundamental Operating Variables

- Input speed.
- Applied torque.
- Oil temperature.

These three variables describe a large part of the operating dependence of the TE observed on the test rig.

## Directional Clarification

- The paper explicitly distinguishes `forward` and `backward` TE behavior.
- These are analogous phenomena under the same physical and mathematical
  treatment, but they are modeled with distinct datasets and distinct trained
  models.
- Equation `(2)` uses a generalized direction subscript, so later symbols such
  as amplitudes, phases, datasets, and tables must be read as valid for both
  the forward and backward formulations.
- The repository's currently recovered paper assets correspond only to the
  `forward` branch.

## Process Architecture

- Data collection on a dedicated test rig.
- Training of ML models to predict TE or its relevant components.
- Export of the model in a PLC-usable representation.
- Online compensation during real motion profiles.

## Key Messages From The Paper

- ML models are suitable for the problem because they provide fast predictions.
- TwinCAT integration is a central practical requirement, not a secondary detail.
- Compensation is designed to stay compatible with PLC task-cycle constraints.
- The experimental results show TE reductions above 80-90% in different scenarios.

## Relevant Implementation Elements

- Industrial deployment requires lightweight, interpretable, and stable models.
- Selected TE harmonics are a practical and effective representation on the PLC side.
- The system separates faster compensation tasks from slower ML prediction tasks.

## Implications For This Repository

- Models must be designed with export and deployment constraints in mind, not only offline accuracy.
- Every training pipeline should consider a TwinCAT-compatible or Structured Text-compatible final output.
- Input features must stay aligned with the real test rig: speed, torque, temperature, and angular position.
- Paper-faithful comparisons must keep `forward` and `backward` model banks
  separate.
- The current recovered RCIM reference package in the repository must be read
  as a `forward-only` asset surface.

## Design Decisions To Preserve

- Favor simple and stable architectures.
- Keep physical input and output quantities explicit.
- Keep the prediction model separate from the compensation module.
- Evaluate latency, updatable frequency range, and PLC task constraints from the beginning.

## Use In The Current Project

- This document is the main reference for the ML-driven compensation side of the project.
- Every new implementation should be assessed both offline and in terms of TwinCAT deployment viability.
