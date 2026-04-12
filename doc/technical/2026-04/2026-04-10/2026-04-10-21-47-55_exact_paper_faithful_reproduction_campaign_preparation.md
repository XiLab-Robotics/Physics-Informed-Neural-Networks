# Exact Paper Faithful Reproduction Campaign Preparation

## Overview

This technical document opens the next `Track 1` step after the completed
exact-paper model-bank stabilization campaign.

The repository now has:

- a completed second harmonic-wise `Track 1` campaign with best offline test
  mean percentage error `8.877%`;
- a completed exact-paper family-bank campaign with stable per-target ONNX
  export across the recovered family inventory;
- a clear remaining gap between the current repository state and the paper
  benchmark, especially the paper offline threshold `Target A` and the later
  online compensation benchmark.

The next task is therefore not another narrow export-stability pass. It is the
preparation of a paper-faithful reproduction campaign that treats exact-paper
training reproduction as one required stage inside a broader benchmark-facing
workflow.

## Technical Approach

The campaign preparation should define a reproducible path that answers two
different questions cleanly:

1. can the recovered exact-paper family bank be reproduced as faithfully as
   the available scripts and assets allow, including paper-era hyperparameters,
   target parameterization, and training structure;
2. can those reproduced models be evaluated through the harmonic-wise
   prediction and TE-reconstruction path needed to approach the paper offline
   benchmark rather than only a component-wise family ranking.

The preparation phase should separate these layers explicitly:

- `exact-paper training reproduction`
  reproduce recovered training assumptions, family inventory, target schema,
  hyperparameters, and export behavior as faithfully as the recovered evidence
  permits;
- `paper-faithful offline benchmark`
  use harmonic-wise `A_k` / `phi_k` prediction and TE reconstruction to obtain
  the comparable offline percentage-error metric anchored to `Target A`;
- `future online benchmark handoff`
  keep the campaign outputs structured so the later `Robot` / `Cycloidal`
  playback and online compensation stage can consume them without inventing a
  new incompatible artifact layer.

The immediate deliverable of this task is campaign preparation, not execution.
That means:

- a technical document;
- a planning report;
- a candidate run matrix;
- the definition of the success criteria and artifact surface to generate in
  the implementation phase after approval.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `reference/rcim_ml_compensation_recovered_assets/`
- `scripts/paper_reimplementation/rcim_ml_compensation/`
- `config/paper_reimplementation/rcim_ml_compensation/`
- `doc/reports/campaign_plans/`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`

No subagent is planned for this task. The preparation scope is local and
bounded, and the current repository evidence is sufficient to define the first
campaign package without delegation.

## Implementation Steps

1. Formalize the exact scope boundary between the stabilized exact-paper branch
   and the broader paper-faithful reproduction goal.
2. Write a campaign planning report that defines the candidate runs,
   comparison questions, and success criteria.
3. Specify how recovered paper-era parameters will be treated:
   exact reuse where recovered, explicit approximation where missing, and
   serialized provenance notes for every unresolved training assumption.
4. Define the expected artifacts for both component-wise exact-paper validation
   and TE-level offline benchmark comparison.
5. After approval, generate the campaign YAML package, launcher, launcher
   note, and prepared campaign state for operator-driven execution.
