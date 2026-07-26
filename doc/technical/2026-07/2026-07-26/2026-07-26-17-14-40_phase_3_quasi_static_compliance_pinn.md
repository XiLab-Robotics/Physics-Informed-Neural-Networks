# Phase 3 Quasi-Static Compliance And Elastic-Offset PINNs

## Overview

This project implements Phase 3 of the sixteen-phase Wave 5.2 full-PINN
theory-validation roadmap. Phase 0 established the data and observability
contracts, Phase 1 selected the Polynomial-Fourier analytical reference, and
Phase 2 closed as a valid negative result without promoting oscillator,
periodic-boundary, or Bauer-anchor weights.

Phase 3 isolates the next source-supported mechanism: a quasi-static elastic
contribution whose deflection depends on transmitted torque, effective
stiffness, oil temperature, and direction. The source-backed decomposition is

```text
TE(theta, operating state) =
    angularly periodic contribution
  + quasi-static elastic or compliance contribution
  + unresolved residual
```

The phase will test whether a bounded, physically signed compliance component
improves held-out curve mean and raw error without damaging centered shape,
harmonic fidelity, or continuity. It will not introduce hysteretic memory,
friction state, dynamic acceleration, contact, wear, or MMT parameters.

This technical document and its associated campaign plan are automatically
approved under the user's ten-hour standing approval beginning on
`2026-07-26`. No subagent is planned.

## Technical Approach

### Source And Repository Evidence

The design is grounded in the Olabi, Ghorbel, and Mesmer syntheses, the RV
mechanics evidence matrix, and completed CVP offset investigations:

- compliance and kinematic error should remain separate, inspectable terms;
- direction-specific stiffness is a legitimate bounded intermediate model;
- torque, temperature, and direction are causal runtime inputs;
- positive stiffness and monotonic elastic deflection are required physical
  properties;
- `direction_torque` is the strongest conservative causal grouping observed
  by CVP 1.5, but offset-only correction was insufficient;
- target mean-centering is diagnostic only and must never enter inference;
- the local data do not identify contact stiffness, friction, backlash,
  hysteresis, and wear simultaneously.

The implementation will therefore expose the predicted periodic contribution,
elastic contribution, effective stiffness, and direction offset separately.

The Phase 3 entry audit resolved the local signed-torque convention before
training: eligible `Fw` curves carry negative measured torque and eligible
`Bw` curves carry positive measured torque, apart from the audited low-torque
boundary. This measured convention overrides generic mechanism intuition.

### Governing Formulations

Let `tau` be signed torque under the repository direction convention, `T` oil
temperature, `d` direction, `theta` output angle, `c = 1 / k` compliance, and
`e_elastic` the quasi-static elastic contribution.

The bounded formulations are:

1. `PINN-C0`, a learned periodic-plus-offset control with no compliance
   equation;
2. `PINN-C1`, bounded linear compliance,
   `e_elastic = tau / k_d`, with positive direction-specific `k_d`;
3. `PINN-C2`, temperature-conditioned stiffness,
   `e_elastic = tau / k_d(T)`, with bounded positive `k_d(T)`;
4. `PINN-C3`, direction-specific nonlinear compliance, combining a positive
   linear slope with a bounded odd nonlinear correction;
5. `PINN-C4`, a hard analytical elastic-offset component plus a learned
   zero-mean periodic residual;
6. `PINN-C5`, shared positive stiffness with explicit direction-specific
   backlash-like intercepts, evaluated jointly across `Fw` and `Bw`.

Positive stiffness will be enforced by bounded parameterization rather than
only penalized after the fact. Monotonicity, zero-torque intercept, and
temperature sensitivity will also be measured with target-free synthetic
collocation points. The periodic residual in `C4` will be mean-centered within
each curve by construction so that it cannot silently absorb the elastic
offset.

### Identifiability And Data Contract

Before training, a Phase 3 observability audit will use the exact Phase 0 and
Phase 1 common manifest to quantify:

- signed torque and temperature support by direction and split;
- torque-temperature correlation and condition coverage;
- measured curve mean and harmonic-zero behavior;
- zero- or low-torque support;
- repeated operating conditions and load-unload evidence;
- whether each candidate stiffness law is identifiable on training data
  without validation or test targets.

If the data lack a true zero-torque condition, zero-torque behavior will remain
a target-free physical boundary check rather than a fitted observation. If
load-unload trajectories are not recoverable, the phase will record that test
as an observability limitation and defer memory effects to Phase 4.

### Campaign Design

The bounded campaign will use:

- the exact 675 / 194 / 97 eligible common split per direction;
- identical causal inputs, point stride, curve cap, and checkpoint policy
  across comparable arms;
- `C0` through `C4` as separate `Fw` and `Bw` runs;
- a paired-direction `C5` run and paired control only if the pre-training audit
  proves a leakage-safe joint loader and split contract;
- zero, low, and moderate compliance-pressure levels only after deterministic
  validation;
- multiple bounded initializations for any arm whose stiffness appears
  promotable;
- accepted periodic MLP and GRU references in the bounded curve-first
  comparison;
- no inherited nonzero Phase 2 physics weights.

The launcher will support local execution, `-Remote`, and preflight-only mode.
The campaign package will persist immutable run instances, queue state, winner
artifacts, registries, and closeout evidence.

### Evaluation And Exit Gate

The phase decision will keep `Fw` and `Bw` visible and will report:

- raw MAE and RMSE;
- signed and absolute curve-mean error;
- centered-shape MAE and peak-to-peak fidelity;
- dominant-order amplitude and circular phase error;
- stiffness range, sign, and initialization sensitivity;
- monotonicity and zero-torque boundary violations;
- temperature-transfer and condition-held-out performance;
- data-loss versus physics-loss gradient behavior;
- compute cost and inspectable TwinCAT-facing intermediate quantities.

A compliance formulation is retained only if its stiffness-like parameters
remain bounded, positive, stable across initializations, and predictive outside
the fitting conditions while improving offset behavior without a material
shape or harmonic regression. Otherwise Phase 3 closes as a negative result
and Phase 4 proceeds without the rejected weights.

## Involved Components

Planned implementation and configuration surfaces:

- `scripts/analysis/pinn_program_compliance/`
- `scripts/models/quasi_static_compliance_pinn_network.py`
- `scripts/testing/validate_quasi_static_compliance_pinn.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/transmission_error_datamodule.py`
- `config/training/quasi_static_compliance_pinn/`
- `scripts/campaigns/wave_5_2/`
- `doc/scripts/campaigns/wave_5_2/`
- `doc/reports/analysis/model_development_waves/wave_5_2/`
- `doc/reports/campaign_plans/model_development_waves/wave_5_2/`
- `doc/reports/campaign_results/wave_5_2/`
- `doc/running/active_training_campaign.yaml`
- `output/analysis/pinn_program_compliance/`
- `output/training_campaigns/`
- `output/training_runs/`
- `output/validation_checks/`
- `output/registries/`

Canonical evidence inputs:

- Phase 0 foundation audit and exact eligible-condition manifest;
- Phase 1 common split and Polynomial-Fourier surfaces;
- Phase 2 negative-result decision and checkpoint diagnostics;
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`;
- `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md`;
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`;
- CVP 1.3 through CVP 1.5 offset evidence;
- Wave 3.1 through Wave 3.3 offset-aware experiments.

The active campaign is closed and its protected-file list is empty. No
subagent is planned.

## Implementation Steps

1. Register this automatically approved technical document.
2. Create and register the automatically approved Phase 3 campaign plan.
3. Build the compliance observability and identifiability audit.
4. Implement bounded compliance laws and explicit decomposition outputs.
5. Add deterministic equation, gradient, boundary, and factory tests.
6. Integrate Phase 3 losses and diagnostics into shared training.
7. Create the dedicated model report before campaign use.
8. Generate the campaign YAML package, queue, launcher, launcher note, and
   persistent campaign state.
9. Run all queue-item preflights and synthetic validation.
10. Execute the bounded campaign only after the audit passes its entry gate.
11. Run the common-split multi-index curve-first comparison.
12. Create and validate the campaign-results Markdown and styled PDF.
13. Synchronize registries, backlog, roadmap, ledger, guide, and Sphinx portal.
14. Run Markdown, Python, PowerShell, YAML, Sphinx, PDF, Git, and size QA.
15. Create the dedicated Phase 3 Git commit under the standing approval.
