# Neural Network Foundations And TE Model Learning Guide

## Overview

This document defines the repository plan for a new educational guide requested by the user.

The requested deliverable is not a short model note. It is a structured learning path that should help a reader with no prior neural-network background progress from first principles to a university-level understanding of the model families used or planned in this repository.

The guide must explain:

- what a neural network is and why it works as a function approximator;
- how forward propagation, loss functions, gradients, and backpropagation interact;
- the practical meaning of training, validation, and testing;
- the difference between data fitting, generalization, underfitting, and overfitting;
- how the repository-specific TE problem maps onto these concepts;
- the detailed logic of each model family in the approved roadmap, starting with `MLP / feedforward` and `harmonic_regression`.

The goal is to create a didactic layer above the existing implementation and analysis material so that a new reader can understand both the generic ML foundations and the TE-specific model progression.

## Technical Approach

### Deliverable Strategy

The guide should be implemented as a curriculum rather than as one oversized undifferentiated document.

The recommended structure is:

1. one foundations guide that explains neural-network basics from zero;
2. one training-and-evaluation guide that explains dataset splits, optimization, validation logic, and test interpretation in repository terms;
3. one architecture curriculum guide that explains the model families in the same order used by the approved TE roadmap;
4. reuse and expand the existing model-explanatory reports for already implemented architectures instead of rewriting parallel disconnected documents.

This keeps the material readable for beginners while still allowing deeper model-specific sections for advanced readers.

### Proposed Documentation Layout

The new documentation should live under a dedicated analysis subfolder so it remains separate from campaign reports and implementation notes.

Recommended target layout after approval:

- `doc/reports/analysis/learning_guides/Neural Network Foundations/`
  - main foundations report;
  - report-local `assets/` folder for conceptual diagrams and learning figures.
- `doc/reports/analysis/learning_guides/Training, Validation, And Testing/`
  - split logic, optimization loop explanation, metric interpretation, and overfitting examples;
  - report-local `assets/` folder.
- `doc/reports/analysis/learning_guides/TE Model Curriculum/`
  - high-level sequence of the planned architectures;
  - links into the model-specific explanatory reports already present under `doc/reports/analysis/model_explanatory/`;
  - new report-local `assets/` folder.

### Pedagogical Scope

The guide should use a progressive depth model.

Each chapter should move through four levels:

1. intuitive explanation;
2. mathematical or algorithmic formulation;
3. TE-project interpretation;
4. repository implementation mapping.

This structure is important because the user explicitly asked for coverage from a basic level up to a university-level understanding.

### Foundations Topics To Cover First

The foundations portion should explain at minimum:

- supervised learning as function approximation;
- dataset samples, features, targets, and labels in the TE context;
- neuron, weight, bias, activation function, layer, and hidden representation;
- forward pass and prediction generation;
- loss functions, especially regression losses used in the repository;
- gradient descent and optimizer updates;
- backpropagation at a conceptual and practical level;
- batch, mini-batch, epoch, learning rate, regularization, and checkpointing;
- train, validation, and test split purpose and failure modes;
- common pitfalls such as leakage, overfitting, and unstable comparisons.

### Architecture Sequence To Follow

The architecture guide should follow the already approved model-family roadmap so the educational material stays aligned with the execution program.

The first sequence should be:

1. `feedforward` / `MLP`;
2. `harmonic_regression`;
3. `periodic_mlp`;
4. `residual_harmonic_mlp`;
5. tree-based benchmarks as a contrast case, clearly marked as non-neural baselines;
6. lagged-feature `MLP`;
7. `GRU`;
8. `LSTM`;
9. `TCN`;
10. `Mixture-of-Experts / regime-conditioned` model;
11. Fourier-feature network;
12. harmonic-head network;
13. Laplacian-regularized network;
14. `SIREN`;
15. `Lightweight Transformer`;
16. `State-Space Sequence Model`;
17. `Neural ODE`;
18. `PINN`.

The guide should clearly distinguish among:

- already implemented families;
- approved-but-not-yet-implemented families;
- low-priority exploratory families.

That distinction is necessary so the educational guide remains accurate and does not imply that every planned model is already available in code.

### Reuse Of Existing Material

The repository already contains detailed model-explanatory reports for:

- `feedforward`;
- `harmonic_regression`;
- `periodic_mlp`;
- `residual_harmonic_mlp`.

Those reports should not be duplicated blindly. Instead, the new educational guide should:

- introduce the common concepts once;
- point the reader to the existing detailed reports for implementation-level depth;
- retrofit or extend only the parts that are too advanced, too repository-specific, or not sufficiently beginner-friendly.

### Visual Material

The user asked for explanation quality, and the repository rules already favor diagrams in model reports.

The approved implementation should therefore include visual material such as:

- simple neuron and layer diagrams;
- train/validation/test workflow diagrams;
- loss-and-optimization loop schematics;
- model-family progression charts;
- conceptual architecture maps for the planned families that do not yet have implementation reports.

Every new guide-specific figure should live in a report-local `assets/` folder and should be checked after generation for label overflow, spacing defects, and readability.

### Consistency With Project Constraints

The guide must stay aligned with the repository domain constraints:

- TE is the central target quantity;
- operating variables must remain explicit: speed, torque, temperature, angular position, and valid windows;
- interpretability and TwinCAT/PLC deployment relevance must be explained whenever architectures are compared;
- the difference between analytical modeling, standard ML compensation, hybrid structured models, and full PINNs must remain explicit.

## Involved Components

- `README.md`
  Main project document that must reference this technical planning note.
- `doc/README.md`
  Internal documentation index that should also reference this technical planning note.
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
  Summary of the ML compensation and TwinCAT deployment constraints.
- `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`
  Summary of the practical TE workflow, harmonic selection, and PLC integration logic.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
  Approved roadmap that defines the model-family sequence the educational guide must follow.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
  Execution backlog that clarifies which families are implemented, planned, or exploratory.
- `doc/reports/analysis/model_explanatory/`
  Existing model-level reports that should be reused as advanced architecture chapters for implemented families.
- Future target after approval:
  - `doc/reports/analysis/learning_guides/`
  - report-local `assets/` folders under that tree.

## Implementation Steps

1. Create this technical planning document and register it in `README.md` and `doc/README.md`.
2. Wait for explicit user approval before creating the educational guide files themselves.
3. Create the foundations guide for readers with no prior neural-network background.
4. Create the training, validation, and testing guide with TE-specific examples and common failure cases.
5. Create the architecture curriculum guide that explains the roadmap sequence from `MLP / feedforward` onward.
6. Integrate the existing model-explanatory reports into that curriculum through cross-links and, where needed, beginner-oriented bridge sections.
7. Create conceptual diagrams and workflow figures in report-local `assets/` folders.
8. Add new conceptual architecture chapters for approved-but-not-yet-implemented families, clearly labeled as roadmap explanations rather than implementation reports.
9. Review the final guide set for terminology consistency, TE-domain accuracy, and pedagogical progression from beginner to advanced depth.
