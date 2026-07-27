# Physics-Guided PINN Forward-Setpoint Report And Roadmap

## Overview

This project will produce two coordinated documentation deliverables for the
next physics-guided model-development cycle:

1. a detailed analytical report, delivered as both Markdown and a validated
   styled PDF;
2. a new staged implementation and experimental roadmap.

The scope is intentionally restricted to the `polished_dataset`, `setpoints`
input mode, and the forward (`Fw`) directional surface. No backward-surface,
actual-values, simplified-dataset, or multi-surface experiment will be included
in the proposed campaign sequence.

The report will correct an important interpretation of the completed Wave 5.2
work. The fact that no previously tested physical residual was promoted does
not demonstrate that physics-guided learning is ineffective. It demonstrates
that the specific formulations, observability assumptions, weights, and model
couplings tested so far did not outperform the accepted controls under their
respective evaluation contracts. The new work will distinguish exact physical
laws, mechanism-informed structure, mathematical signal priors, weak physical
constraints, and grey-box residual learning.

This technical project is documentation-only. It does not authorize model
implementation, campaign preparation, or training. Each later implementation
or training stage will require its own approval-gated technical document and,
where training is involved, a campaign planning report and repository-owned
campaign package.

## Technical Approach

The analytical report will synthesize the repository's ingested references,
reference summaries, completed Wave 5.2 evidence, RCIM findings, the Bauer
Polynomial-Fourier formulation, and the accepted forward-surface baselines.
Claims will be separated into three evidence classes:

- demonstrated by repository experiments;
- supported by references or mechanism knowledge but not yet trained;
- proposed as a falsifiable future hypothesis.

The report will explain the main ways in which physical knowledge can guide a
neural model:

- loss terms based on residuals, invariants, inequalities, or regularity;
- hard or semi-hard architectural constraints;
- analytical base models with learned corrections;
- physically interpretable latent variables or auxiliary prediction heads;
- weak priors on signs, bounds, smoothness, periodicity, or parameter ranges;
- staged curricula and adaptive balancing between data and physics objectives.

Particular attention will be given to harmonic modeling. Fourier decomposition
alone is a mathematical representation rather than a complete physical model.
It becomes mechanism-informed when harmonic orders, phase relationships, and
condition-dependent amplitudes are connected to reducer kinematics or known
excitation mechanisms. The report will therefore separate spectral
representation, physical interpretation, and predictive usefulness.

The preferred grey-box family will use an explicit analytical component and a
learned residual:

`TE_prediction = TE_analytical + TE_learned_residual`

The analysis will cover the benefits and risks of this formulation, including
residual cancellation, parameter non-identifiability, redundant constraints,
incorrect physical bias, and loss-scale imbalance. Candidate safeguards will
include residual capacity limits, staged freezing and unfreezing, harmonic
subspace separation, parameter priors, corruption controls, extrapolation
tests, and explicit residual diagnostics.

The roadmap will be organized as a sequence of evidence gates rather than one
large unrestricted campaign. Its initial candidate families will include:

- the accepted `Fw` control models under a frozen evaluation contract;
- the Bauer Polynomial-Fourier analytical predictor;
- Bauer plus a data-only residual multilayer perceptron;
- Bauer plus a learned residual with spectral guidance;
- Bauer plus a temporal residual model;
- harmonic multi-head models for mean, shape, amplitude, and phase;
- weak compliance, boundedness, smoothness, and closure priors;
- adaptive loss-weighting and curriculum variants;
- matched-capacity black-box controls.

A dedicated discovery stage will search the repository references and primary
scientific literature for additional techniques that can help a PINN learn the
forward TE phenomenon. The search will consider, where technically relevant:

- weak-form and variational PINNs;
- universal differential equations and grey-box system identification;
- constrained and augmented-Lagrangian training;
- adaptive or uncertainty-based loss balancing;
- spectral, complex-coefficient, phase-aware, and order-domain objectives;
- residual orthogonalization against analytical bases;
- curriculum learning and synthetic-to-real pretraining;
- sparse equation discovery and hybrid identification;
- monotonicity, inequality, symmetry, and bounded-parameter constraints;
- Bayesian or ensemble uncertainty for physics-prior trust calibration;
- neural operators and operator-learning methods when the data contract
  supports their use.

The discovery stage will not promote techniques by novelty alone. Every
candidate will be mapped to the available variables, observability,
identifiability, runtime inference contract, TwinCAT feasibility, and a
falsifiable ablation.

Because the scope is forward-only, direction-dependent backlash cannot be
identified from an `Fw/Bw` difference in this project. Backlash-related
knowledge may only enter as a carefully bounded forward load-path hypothesis
or a future-data recommendation. It will not be represented as an identified
directional physical law without the required bidirectional or loop evidence.

The report PDF will be generated with the repository-owned styled-report
pipeline and visually inspected against the repository's analytical-report
standard. The real PDF, not only the Markdown or HTML intermediate, will be
validated.

## Involved Components

The evidence review will include, at minimum:

- `doc/reference_summaries/10_Polynomial_Fourier_TE_Model_Project_Summary.md`;
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`;
- `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md`;
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`;
- the completed Wave 5.2 phase reports and campaign results;
- the RCIM Model-Bank Reproduction evidence relevant to harmonic TE behavior;
- current forward-surface control, registry, and curve-verification evidence;
- the existing full-PINN roadmap and project-status documents.

The proposed deliverables are:

- `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/physics_guided_pinn_reassessment_report.md`;
- `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/physics_guided_pinn_reassessment_report.pdf`;
- `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/polished_setpoint_fw_physics_guided_pinn_implementation_roadmap.md`.

The work will also update the appropriate topic index and `doc/README.md`.
Project status or backlog documents will be changed only where the approved
roadmap materially supersedes the current future-work description.

The repository-owned PDF and Markdown QA entry points will be used:

- `scripts/reports/pdf/run_report_pipeline.py`;
- `scripts/reports/pdf/generate_styled_report_pdf.py`;
- `scripts/reports/pdf/validate_report_pdf.py`;
- `scripts/tooling/markdown/markdown_style_check.py`;
- `scripts/tooling/markdown/run_markdownlint.py`.

No subagents are planned for this work.

## Implementation Steps

1. Freeze the exact `polished_dataset` plus `setpoints` plus `Fw` scope and
   build a source-to-claim evidence matrix.
2. Reconstruct the completed experimental record, separating trained results,
   analytical feasibility checks, deferred formulations, and untested ideas.
3. Write the detailed physics-guided PINN reassessment report, including the
   corrected interpretation of previous negative results.
4. Explain harmonic, Polynomial-Fourier, compliance, backlash, hysteresis,
   friction, contact, and grey-box knowledge at the level required to design
   measurable neural constraints.
5. Add a risk and identifiability analysis showing which quantities can and
   cannot be inferred from the forward-only data contract.
6. Perform the dedicated deep technique-discovery review and map every viable
   technique to a concrete hypothesis, required inputs, loss or architecture,
   control arm, failure criterion, and deployment implications.
7. Build the staged implementation roadmap with explicit evidence gates:
   baseline contract, analytical anchor, learned residuals, spectral guidance,
   temporal residuals, interpretable multi-head models, weak physical priors,
   adaptive training, and cross-formulation selection.
8. Define matched experimental controls, including identical splits, at least
   three seeds, capacity-matched black-box models, bounded normalized weight
   sweeps, and strict leakage checks.
9. Define curve-first success metrics for raw error, mean-centered shape,
   offset, peak-to-peak behavior, harmonic amplitude and phase, tail
   robustness, residual cancellation, and boundary extrapolation.
10. State the approval and campaign-package requirements for each future
    training step without executing training in the current task.
11. Export the analytical report to a styled PDF, validate its structure and
    content, rasterize representative pages, and visually inspect the actual
    deliverable.
12. Run zero-warning Markdown QA, final-newline checks, PDF validation, index
    checks, and `git diff --check` on the completed documentation scope.
13. Report completion and wait for explicit approval before creating any Git
    commit.
