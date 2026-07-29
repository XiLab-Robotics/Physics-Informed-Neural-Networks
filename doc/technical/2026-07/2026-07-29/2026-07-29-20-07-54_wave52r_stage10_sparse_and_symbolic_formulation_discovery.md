# Wave 5.2R Stage 10 Sparse And Symbolic Formulation Discovery

## Overview

Stage 10 searches for compact condition-dependent harmonic laws that improve
on the complete quadratic Polynomial-Fourier formulation while remaining
inspectable, periodic by construction, and suitable for explicit PLC
evaluation.

The scope remains restricted to `polished_dataset`, setpoint inputs, and the
forward surface. The frozen Stage 0 grouped split is mandatory. All sparse
selection, bootstrap stability estimation, scaling, and hyperparameter choice
use training and validation conditions only. The test split remains untouched
until the candidate definitions are frozen.

Discovered expressions are empirical structure. They are not called physical
laws unless a later independent mechanism analysis supports that
interpretation.

## Technical Approach

The response representation is the Stage 5 uniform `2048`-sample curve and its
explicit complex harmonic coefficients. Each retained harmonic coefficient is
modeled as a condition law over normalized torque, speed, and temperature.
Reconstruction through a fixed sine/cosine basis guarantees angular
periodicity.

The predeclared condition library contains:

- intercept, linear, square, and cubic condition terms;
- pairwise and triple polynomial interactions;
- signed and magnitude-preserving torque terms;
- bounded rational and logarithmic magnitude terms;
- temperature-modulated torque and speed terms;
- harmonic-order metadata used only to group and audit coefficient laws.

No measured TE, held-out coefficient, test-derived scaler, or future curve
value becomes an inference input.

The first screen compares:

| ID | Formulation | Role |
| --- | --- | --- |
| `D00` | frozen PF-A curve | analytical anchor |
| `D01` | frozen H04 coefficient component | qualified nonlinear reference |
| `D02` | frozen Stage 9 K01 prediction | temporal research reference |
| `Q00` | complete quadratic coefficient law | mandatory simple control |
| `R00` | ridge fit on the complete library | dense same-library control |
| `S01` | sequential thresholded ridge | sparse-library candidate |
| `S02` | bootstrap stability-selected sparse refit | primary sparse candidate |
| `S03` | hierarchy-constrained stable sparse refit | strong-heredity ablation |
| `Y01` | bounded separable symbolic-library refit | symbolic candidate |
| `N01` | label-shuffled stability selection | specificity control |

Sparse selection uses repeated training-condition bootstraps. A term is stable
only if its selection probability, sign agreement, and normalized magnitude
meet predeclared thresholds. Validation chooses the threshold and ridge
regularization from a bounded grid; the frozen choice is then refit on
train-plus-validation before one test evaluation.

The complete exit gate requires:

- lower held-out raw and mean-centered shape error than `Q00`;
- no material regression in closure, retained harmonic amplitude, phase, or
  per-curve P95;
- materially fewer active terms than the dense same-library control;
- bootstrap selection probability at least `0.75`;
- selected-term sign agreement at least `0.85`;
- no shuffled-label candidate with comparable held-out gain;
- deterministic reconstruction and zero target-derived runtime inputs.

Beating H04 or K01 is reported but is not required to qualify an explicit
ablation term set. Qualification means that stable sparse structure advances
to later formulation tests, not that the sparse predictor becomes the program
winner.

## Involved Components

- `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/polished_setpoint_fw_physics_guided_pinn_implementation_roadmap.md`
- `output/analysis/wave_5_2r/stage1_extended_scientific_technique_discovery/stage1_technique_register.yaml`
- `scripts/campaigns/wave_5_2/run_wave52r_stage5_complex_harmonic_coefficient_residuals.py`
- `output/analysis/wave_5_2r/stage9_temporal_analytical_residual_models/closeout/stage9_exit_gate_summary.yaml`
- new sparse-library and stability-selection implementation under
  `scripts/models/`
- new Stage 10 campaign runner and PowerShell launcher under
  `scripts/campaigns/wave_5_2/`
- campaign configuration under
  `config/training/sparse_symbolic_formulation_discovery/`
- campaign plan under
  `doc/reports/campaign_plans/model_development_waves/wave_5_2/`
- immutable run, campaign, analysis, report, and PDF artifacts
- backlog, ledger, master-summary, usage-guide, and Sphinx entry points

No subagent is planned. Any later delegation requires a declared scope and
fresh explicit user approval before launch.

## Implementation Steps

1. Freeze the Stage 0 split, Stage 5 harmonic representation, PF-A, H04, and
   Stage 9 K01 comparison payloads.
2. Create the preliminary campaign plan and ten-entry candidate matrix.
3. Implement the named, unit-aware condition-term library and deterministic
   coefficient reconstruction.
4. Implement complete-quadratic, ridge, thresholded-ridge, bootstrap
   stability, hierarchy, separable-symbolic, and shuffled-label paths.
5. Add train-only scaling, nested validation selection, deterministic
   bootstrap identities, and term-level selection/sign/magnitude evidence.
6. Add preflight checks for representation parity, split integrity,
   periodicity, reconstruction, leakage, and synthetic sparse-law recovery.
7. Generate campaign YAML, active state, local and remote PowerShell launcher,
   and launcher documentation.
8. Execute the bounded first screen under the active blanket approval.
9. Evaluate raw, mean, shape, derivative, closure, harmonic amplitude, phase,
   P95, complexity, stability, and shuffled-specificity gates.
10. Generate the explanatory report, campaign-results report, plots, styled
    PDF, and real PDF validation.
11. Synchronize the live backlog, status ledger, master summaries, usage
    guide, documentation index, and Sphinx portal.
12. Run Python, PowerShell, Markdown, Sphinx, PDF, Git-size, and commit
    preflight checks, then create the Stage 10 commit under the active blanket
    approval.
