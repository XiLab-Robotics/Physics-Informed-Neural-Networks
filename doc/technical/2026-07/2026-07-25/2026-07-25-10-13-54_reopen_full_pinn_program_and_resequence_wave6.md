# Reopen Full PINN Program And Resequence Wave 6

## Overview

This document proposes a correction to the model-development roadmap after the
Wave 5.2 MMT residual-explanatory diagnostic closed with
`blocked_by_parameter_availability`.

The blocker applies to a paper-faithful full PINN based on the currently
available MMT formulation and parameter set. It does not invalidate physics-
informed model development in general. The general full-PINN program should
therefore return to the active core of Wave 5.2, while the MMT-paper-faithful
implementation remains a separately identified deferred subbranch with an
explicit reopening gate.

The renewed Wave 5.2 program will evaluate multiple defensible formulations of
the known transmission-error physics. Its starting evidence includes:

- the measured harmonic structure of the transmission-error curves;
- the existing direction-specific Polynomial Fourier Series computation;
- the empirical findings from Waves 3 and 4 about offset, shape, robustness,
  probabilistic behavior, state, and curve-level selection;
- the Wave 5.1 harmonic-prior residual results;
- the current MMT analysis, retained as useful theory even though its
  paper-faithful parameterization is not currently implementable;
- additional scientific and engineering references that will be supplied and
  audited before formulation selection.

Wave 6 integrated multi-task and multi-head work should follow the bounded
Wave 5.2 PINN formulation and pilot evidence. It should use the validated
physics-informed ingredients instead of preceding their evaluation.

This document authorizes no implementation or training. It defines the
documentation reorganization that may be performed only after explicit user
approval. No subagent is planned.

## Technical Approach

### Roadmap correction

The canonical roadmap will separate two decisions that are currently
conflated:

1. **MMT-paper-faithful full PINN:** deferred until condition-varying causal
   physical parameters or a validated causal reconstruction become available.
2. **General full-PINN program:** active Wave 5.2 work based on other explicit,
   testable physics formulations.

Historical diagnostic reports will remain unchanged as evidence. Current
status documents will explain that the MMT result blocks one formulation, not
the wider PINN objective.

### Meaning of full PINN in this program

A candidate will qualify as a full physics-informed model only when training
contains one or more explicit differentiable physical residuals, conservation
or compatibility equations, or mathematically specified physical constraints.
Adding harmonic input features, a Fourier output head, or curve-shape metrics
alone will not be labeled a full PINN.

The repository does not yet claim that transmission error is governed by a
single known partial differential equation that is observable from the current
dataset. Each proposed formulation must therefore state:

- its equations and physical interpretation;
- variables, units, coordinate system, and sign conventions;
- assumptions and validity domain;
- which quantities are measured, reconstructed, learned, or unavailable;
- differentiability and numerical-conditioning requirements;
- identifiability and information-leakage risks;
- causal availability at inference time;
- expected TwinCAT and PLC deployment implications;
- falsification and acceptance criteria.

### Initial formulation families

The first formulation inventory will include, without treating any item as
preselected:

- **Polynomial-Fourier structured residual PINN:** translate the existing
  direction-specific Polynomial Fourier Series law into an inspectable,
  differentiable analytical component, then learn a bounded residual subject
  to explicit consistency constraints.
- **Harmonic-kinematic constraint PINN:** enforce defensible periodicity,
  harmonic-frequency, phase, amplitude, offset, slope, and continuity
  relations derived from the measured mechanism behavior.
- **Contact-regime or energy-consistency PINN:** admit continuity, work,
  stiffness, backlash, or contact-transition constraints only where the
  supplied references and available variables support the equations.
- **Reference-derived formulations:** convert each new theoretical source into
  a separate evidence packet and candidate formulation rather than combining
  incompatible assumptions prematurely.
- **MMT-paper-faithful formulation:** retain as deferred until its explicit
  physical-input gate is satisfied.

The existing Polynomial Fourier Series implementation is evidence for a
structured semi-analytical formulation. It must not be presented as a
governing-law PINN until its equations, fitted coefficients, provenance, and
physical constraints have been audited.

### Use of Waves 3, 4, and 5.1

Waves 3 and 4 will be treated as an experimental evidence library for PINN
design. Their results will guide decisions about:

- offset versus mean-centered shape treatment;
- curve-level objectives and checkpoint selection;
- robust losses and outlier behavior;
- probabilistic or mixture outputs where uncertainty is physically relevant;
- stateful or temporal inputs;
- direction-specific versus shared parameters;
- failure modes that should not be repeated in the physics-informed pilots.

Wave 5.1 supplies direct evidence about harmonic priors and residual learning.
These findings constrain candidate selection but do not by themselves prove a
full-PINN formulation.

### Reference intake and evidence gates

Before implementation, each supplied paper or theoretical source will be
registered and synthesized against the repository's real dataset and
deployment context. The audit will distinguish:

- source-backed equations and claims;
- repository-implemented facts;
- assumptions requiring experimental verification;
- missing physical quantities;
- contradictory formulations;
- open questions and proposed tests.

The formulation program will then proceed through evidence gates:

1. reference intake and theory audit, without training;
2. equation specification and unit or coordinate verification;
3. equation-level tests against measured curves and available metadata;
4. synthetic or analytical-oracle validation where possible;
5. bounded single-formulation PINN pilots;
6. multi-index TE Curve Verification Pipeline comparison;
7. selection of validated physics-informed ingredients for Wave 6.

Each later training pilot will require its own approved technical document and
campaign-planning report before execution.

## Involved Components

The documentation-only roadmap reorganization is expected to update:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`;
- the corresponding canonical master-summary view, if it is still maintained;
- a new current Wave 5.2 full-PINN roadmap under
  `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/`;
- `doc/README.md` and any narrower topic index created for the program.

The first formulation audit will include the existing reference implementation
under:

- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/06_PolynomialFourierSeriesModel/`.

The current MMT diagnostic, reference summaries, Wave 3 through Wave 5.1
results, curve-first selection policy, and future supplied references remain
in scope as evidence.

Historical approved technical documents and completed reports will not be
rewritten to simulate a different past decision. The new roadmap report and
current status surfaces will supersede the overly broad interpretation of the
MMT deferral.

The active campaign state is closed and its protected-file list is empty.

## Implementation Steps

1. Register this technical document from `doc/README.md`.
2. Wait for explicit user approval of this technical plan.
3. Create the canonical Wave 5.2 full-PINN future-work roadmap and formulation
   intake structure.
4. Reorganize the live backlog so the general full-PINN program is active,
   the MMT-paper-faithful subbranch is deferred, and Wave 6 follows the PINN
   evidence gates.
5. Synchronize the closeout ledger and master-summary surfaces with the same
   distinction and sequence.
6. Record Waves 3, 4, and 5.1 as input evidence for formulation design rather
   than as substitutes for the full-PINN program.
7. Add a structured reference-intake checklist for the papers and theoretical
   formulations supplied by the user.
8. Run Markdown warning checks, final-newline checks, `git diff --check`, and
   Sphinx validation if the approved changes affect the canonical portal.
9. Stop and report the documentation reorganization without committing.
10. After the references are supplied, perform the theory audit before
    proposing implementation or a training campaign.
