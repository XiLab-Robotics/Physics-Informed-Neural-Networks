# TwinCAT-Friendly Structured TE Modeling Reference Synthesis

## Overview

This note synthesizes the repository reference material most relevant to
TwinCAT-friendly Transmission Error modeling and maps it onto the current
structured-model direction implemented in StandardML - Codex.

The synthesis is intentionally implementation-facing. It separates:

1. what the reference material actually supports;
2. why it matters for this repository;
3. what is already implemented here;
4. what remains open or speculative.

## What The Reference Material Actually Supports

### Operating Variables Must Stay Explicit

Across the reference summaries, TE behavior is consistently tied to operating
variables that include:

- input speed;
- applied torque;
- oil temperature;
- angular position or phase context.

This means the prediction target is not just a generic scalar regression
problem. It is a condition-dependent signal tied to the real rig state.

The TwinCAT reference-code note reinforces the same constraint on the deployed
side: the predictor path is built around speed, temperature, torque, and the
current shaft angle rather than around anonymous latent features.

### `DataValid` Is Part Of The TE Definition

The data-series and machine-learning summaries both stress that TE computation
depends on a valid acquisition window selected through `DataValid`.

That requirement carries three consequences:

- transient samples must not be mixed with the valid steady-state segment;
- angular representations need careful interpretation after common zeroing;
- future raw-data or deployment workflows must preserve the meaning of the
  valid window instead of treating it as a disposable preprocessing detail.

### TwinCAT Compatibility Is A Design Constraint

The compensation-oriented reference material treats Beckhoff TwinCAT as a core
practical target rather than a later deployment afterthought.

The reference-backed constraints are:

- runtime simplicity matters;
- model export format matters;
- inspectable intermediate quantities matter;
- PLC task-cycle limits matter;
- robust handling of invalid numeric states matters.

The imported TestRig TwinCAT path makes this more concrete: it uses a dedicated
prediction task, multiple model assets, and explicit harmonic reconstruction in
Structured Text rather than one opaque end-to-end runtime model.

### Harmonic Structure Is Valuable On The Deployment Side

The reference summaries support the idea that selected TE harmonics are a
practical representation for PLC-side use.

That is not full proof that every harmonic-informed neural architecture will be
deployment-ready, but it does support a structured decomposition strategy more
strongly than a purely opaque black-box regressor.

## Why This Matters For This Repository

The repository is not optimizing only for offline benchmark accuracy.

The real project target is a TE workflow that can eventually support:

- interpretable analysis;
- stable training;
- inspectable intermediate quantities;
- plausible TwinCAT or PLC-oriented execution paths.

That immediately changes how model families should be judged.

The right question is not only:

- does this model lower MAE?

It is also:

- does this model preserve a credible path to deployment-friendly inference?

## What Is Already Implemented Here

### Structured And Hybrid Model Families Exist

The current repository already includes:

- harmonic regression;
- periodic-feature networks;
- residual harmonic networks;
- tree and feedforward baselines for comparison.

The strongest deployment-facing direction among the neural families is the
residual-harmonic line because it keeps an explicit structured branch while
still modeling the nonlinear remainder.

### The Residual Harmonic Network Preserves An Inspectable Split

The current guide and implementation framing show a model decomposition of the
form:

`TE = structured_harmonic_component + residual_component`

That matters because it preserves a visible distinction between:

- a structured periodic estimate;
- a learned correction term.

This is better aligned with TwinCAT-oriented engineering reasoning than a pure
MLP whose internal logic is fully opaque at runtime.

### Training And Campaign Infrastructure Are Already Inspectable

The repository has already built strong infrastructure around:

- validation checks;
- smoke tests;
- campaign planning;
- immutable run-instance artifacts;
- winner selection and registries.

That does not solve deployment, but it gives a solid offline governance layer
for deciding which family deserves export-oriented work next.

## What Remains Missing, Risky, Or Uncertain

### No Canonical Export Path Is Implemented Yet

The repository currently does not expose a canonical path from a trained
residual-harmonic model to:

- a TwinCAT-consumable representation;
- a structured-text approximation;
- or another explicitly inspectable PLC-friendly runtime package.

So any claim that the current model is already deployment-ready would be too
strong.

This is also consistent with the earlier repository-owned TwinCAT export
analysis: the imported reference proves one viable Beckhoff-side design, but
the current repository has not yet implemented its own matching export bridge.

### The Residual Branch Is Still A Real Deployment Question

The structured harmonic branch is intuitively deployment-friendly.

The residual neural branch is the main uncertainty because it raises practical
questions:

- parameter-count budget;
- activation-function portability;
- runtime latency;
- numeric robustness;
- how to surface intermediate values in a PLC-friendly way.

The current repository demonstrates a good architectural direction, but not yet
the final export story.

### `DataValid` Meaning Must Survive Any Future Online Path

Offline training currently benefits from curated datasets and documented
preprocessing.

A future online or semi-online compensation workflow would still need to keep
the semantics of:

- warm-up and temperature state;
- encoder zeroing interpretation;
- valid sample windows;
- operating-point consistency.

That remains more of a system-design problem than a solved model-export task.

## Repository Consequences

Based on the reference material and the current implementation state, the most
defensible repository consequences are:

1. keep structured and hybrid TE models in the foreground rather than pivoting
   too early to opaque black-box networks;
2. preserve speed, torque, temperature, and angular-context variables as
   first-class model inputs and documentation concepts;
3. keep `DataValid` semantics explicit in both documentation and future data
   workflows;
4. treat exportability and inspectability as co-equal evaluation criteria
   alongside offline error metrics;
5. prefer deployment work first on structured or hybrid families, especially
   the residual-harmonic family, rather than on the most opaque candidate.

## Bottom Line

The repository is already pointed in a direction that is compatible with the
reference material:

- TE remains the central target;
- operating variables remain explicit;
- structured and hybrid models are in scope;
- deployment constraints are recognized as real.

What is not implemented yet is the final bridge from the current offline model
families to a true TwinCAT-friendly export and runtime path.

So the correct conclusion is:

- the current direction is reference-backed and promising;
- the deployment story is plausible;
- the deployment workflow itself is still unfinished.
