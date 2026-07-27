# Wave 5.2R Stage 1 Extended Scientific Technique Discovery

## Overview

This project implements Stage 1 of the approved `Wave 5.2R` roadmap. It will
perform an implementation-facing scientific search restricted to the
`polished_dataset`, setpoint inputs, and `Fw` evidence contract frozen by
Stage 0.

The purpose is to freeze a candidate register before model implementation.
Every retained technique must have an observable local formulation, a matched
control, a falsification rule, and an explicit causal-input and deployment
assessment.

The user has authorized automatic approval of technical documents for all
sixteen `Wave 5.2R` stages, so this document is approved immediately after
registration.

## Technical Approach

The search will combine repository-ingested TE and mechanical references with
current primary literature and official implementations. It will cover all
thirteen technique families required by the roadmap:

1. model discrepancy and grey-box residual learning;
2. weak-form, variational, and Petrov-Galerkin PINNs;
3. adaptive loss weighting and augmented Lagrangian constraints;
4. gradient conflict and multi-objective optimization;
5. spectral-bias mitigation and coordinate networks;
6. Sobolev and derivative-aware training;
7. sparse equation discovery and symbolic regression;
8. uncertainty-aware physics weighting;
9. curriculum, transfer, and synthetic-to-real learning;
10. failure-informed sampling;
11. certified residual bounds;
12. reduced-order neural operators;
13. physics-guided mechanical-system identification.

For every technique, the resulting register will record the source, claimed
benefit, required variables, local formulation, matched control, falsification
criterion, deployment impact, and priority.

The analysis will distinguish:

- direct source-backed claims;
- repository-observed facts;
- proposed local hypotheses;
- excluded or oracle-only mechanisms.

## Involved Components

The stage will add:

- a canonical research report and styled PDF under
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/stage1_extended_scientific_technique_discovery/`;
- a machine-readable candidate register under
  `output/analysis/wave_5_2r/stage1_extended_scientific_technique_discovery/`;
- source and decision tables supporting the Stage 1 exit gate;
- synchronized roadmap, backlog, master summary, ledger, and documentation
  index entries.

The stage will read the relevant material under `reference/` and
`doc/reference_summaries/` before finalizing priorities.

No training, model implementation, campaign preparation, protected campaign
file modification, or subagent use is planned.

## Implementation Steps

1. Inventory the repository reference summaries relevant to harmonic,
   polynomial, mechanical, uncertainty, and identification formulations.
2. Search primary literature and official implementations for each required
   technique family.
3. Map every required variable to the Stage 0 causal forward contract.
4. Define a local equation, loss, architecture, or analysis-only role.
5. Define matched controls and predeclared falsification criteria.
6. Exclude mechanisms that cannot be tested without target leakage or missing
   causal state.
7. Write the machine-readable candidate and source registers.
8. Write the detailed Stage 1 report and explicit exit-gate decision.
9. Export and visually validate the real styled PDF.
10. Synchronize canonical status documents and the roadmap.
11. Run Markdown, PDF, Sphinx, whitespace, and file-size preflight checks.
12. Commit the completed Stage 1 package with a dedicated commit.

## Outcome

Stage 1 completed successfully. The machine-readable register contains thirty
techniques across all thirteen required search families: thirteen active
real-data techniques, eleven conditional real-data techniques, three
oracle-only techniques, and three excluded techniques.

The validation gate confirms that the real-data roster contains no missing
variables and no target-derived runtime quantities. The detailed decision
report is:

`doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/stage1_extended_scientific_technique_discovery/stage1_extended_scientific_technique_discovery_report.md`.

Stage 2, Evaluation And Optimization Instrumentation, is authorized as the next
non-training implementation stage. Later training retains its separate
campaign-plan and explicit-approval gates.
