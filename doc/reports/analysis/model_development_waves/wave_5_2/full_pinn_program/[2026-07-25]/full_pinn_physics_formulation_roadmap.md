# Wave 5.2 Full PINN Physics Formulation Roadmap

## Executive Decision

Wave 5.2 remains the physics-informed model-development wave. Its general
full-PINN program is active at the reference-intake and formulation-design
stage.

Only the paper-faithful MMT implementation is deferred. The completed MMT
diagnostic established that the available geometry-locked signatures are
condition-invariant and that the required causal component-error and
contact-state quantities are unavailable. That result blocks the current MMT
parameterization; it does not disprove transmission-error physics or block
other physics-informed formulations.

No PINN implementation or training campaign is authorized by this roadmap.
Each bounded pilot will require a new approved technical document and campaign
plan.

## Corrected Program Structure

| Program branch | Current state | Decision |
| --- | --- | --- |
| General Wave 5.2 full-PINN program | active formulation research | Audit references, formalize candidate equations, and validate them before implementation. |
| MMT-paper-faithful full PINN | deferred future TODO | Reopen only with condition-varying causal component-error measurements or a validated causal contact-state reconstruction. |
| Wave 6 integrated multi-task and multi-head models | sequenced after Wave 5.2 evidence | Do not design a training campaign until bounded PINN pilots identify useful physics-informed components. |

## Definition Of A Full PINN

For this program, a model qualifies as a full physics-informed neural network
only when its training objective contains explicit differentiable physical
residuals, compatibility equations, or mathematically specified physical
constraints.

The following elements are useful but are not sufficient by themselves:

- harmonic or angular input features;
- a Fourier-structured output head;
- curve-shape metrics used only for evaluation;
- a soft regularizer without a stated physical equation;
- a learned residual attached to an empirical model without a physical
  consistency constraint.

The current TE problem is not assumed to have a single fully observed governing
partial differential equation. Every candidate formulation must identify which
part is analytical, empirical, reconstructed, or learned.

## Evidence Carried Forward

| Evidence source | PINN design consequence |
| --- | --- |
| Waves 3.1 through 3.3 | Separate raw offset from mean-centered shape; retain curve-level, slope, amplitude, phase, and continuity evidence. |
| Wave 4.1 | Preserve robust-loss behavior as a candidate safeguard for noisy or regime-limited residuals. |
| Wave 4.2 | Treat uncertainty and quantile behavior as secondary evidence, not as a replacement for a physical residual. |
| Waves 4.3 and 4.4 | Use mixture and latent-state findings to test regime ambiguity and causal history only where the formulation requires them. |
| Wave 5.1 | Reuse the harmonic-prior and structured-residual findings while distinguishing a harmonic prior from a full PINN. |
| Six-cell reduced comparison | Keep periodic GRU as the primary time-windowed reference and periodic harmonic MLP as the non-windowed structured reference. |
| MMT residual diagnostic | Preserve its equations and negative evidence; do not use unavailable or target-derived MMT variables. |
| Polynomial Fourier Series reference implementation | Audit it as the first explicit semi-analytical curve law and a possible differentiable analytical component. |
| SharePoint reference intake | The 31 unique-file library establishes explicit periodic, hysteretic, dynamic, bidirectional, contact, tolerance, efficiency, wear, and electromechanical branches with separate feasibility decisions. |

## Candidate Formulation Portfolio

### Formulation A: Polynomial-Fourier Structured Residual PINN

The existing TwinCAT reference computes direction-specific TE curves from:

- operating torque, speed, and temperature;
- an order-10 polynomial parameterization;
- a constant term;
- direction-specific harmonic amplitudes and phases;
- the harmonic set currently encoded in the reference implementation.

The first audit will reconstruct the equations, coefficient provenance, units,
direction logic, angular convention, and validity domain. A candidate PINN may
then combine a differentiable Polynomial-Fourier analytical component with a
bounded learned residual and explicit consistency constraints.

This is initially classified as a semi-analytical structured formulation, not
automatically as a governing-law PINN.

The imported source set establishes three variants that must be benchmarked
separately:

- the Bauer complete quadratic law for operating-condition-dependent
  coefficients;
- the recovered MATLAB predictor using heterogeneous ONNX coefficient models;
- the PLC reference using an explicit 35-term polynomial evaluator.

### Formulation B: Harmonic-Kinematic Constraint PINN

This formulation family will test physically defensible relations involving:

- angular periodicity;
- admissible harmonic frequencies;
- amplitude and phase consistency;
- curve mean and offset behavior;
- slope and local continuity;
- direction-specific or shared parameters;
- operating-condition dependence.

The audit must distinguish mechanism-backed constraints from empirical
regularization observed only in the dataset.

### Formulation C: Contact-Regime Or Energy-Consistency PINN

New references may justify equations based on mesh stiffness, backlash,
contact transitions, work, energy, or load sharing. These equations will be
considered only when their variables can be measured or causally reconstructed
and their assumptions match the reducer and test-rig configuration.

### Formulation D: Reference-Derived Alternatives

Each supplied theoretical source will produce a separate candidate evidence
packet. Incompatible coordinate systems, assumptions, or physical regimes will
not be combined until they have been reconciled experimentally and
mathematically.

### Deferred Formulation: Paper-Faithful MMT PINN

The MMT formulation remains preserved but inactive. Its reopening gate is:

1. obtain independent component-error measurements or a validated causal
   contact-state reconstruction;
2. prove that the resulting variables vary by operating condition;
3. prove that they are available without validation or test TE targets;
4. repeat the explanatory and identifiability checks;
5. approve a new implementation and campaign package.

## Formulation Audit Contract

Every candidate must document:

- equations and physical interpretation;
- symbols, variables, units, and coordinate transforms;
- reducer geometry and operating assumptions;
- measured, reconstructed, learned, and unavailable quantities;
- boundary, initial, periodic, continuity, and interface conditions;
- differentiability and numerical conditioning;
- identifiability and parameter-correlation risks;
- causal inference-time availability;
- target-leakage controls;
- expected behavior for `Fw`, `Bw`, and `global`;
- TwinCAT and PLC execution implications;
- equation-level falsification tests;
- pilot acceptance and rejection criteria.

## Work Packages And Gates

| Work package | Deliverable | Current state |
| --- | --- | --- |
| WP1 Reference intake | Source inventory and per-reference synthesis | SharePoint bundle complete; future sources remain append-only |
| WP2 Equation audit | Verified equations, units, assumptions, and observable-variable map | active; Polynomial-Fourier benchmark is first |
| WP3 Analytical verification | Equation tests on measured curves plus synthetic or analytical oracles | pending WP2 |
| WP4 Bounded formulation pilots | One isolated formulation per approved campaign | not authorized |
| WP5 Curve-first verification | Separate raw, centered-shape, offset, harmonic, robustness, visual, and deployment surfaces | pending pilots |
| WP6 Formulation decision | Accept, revise, combine, or reject each formulation | pending verification |
| WP7 Wave 6 design | Integrate only validated physics-informed ingredients into multi-task or multi-head models | blocked by WP4 through WP6 |

## Pilot Acceptance Policy

A bounded pilot will not be promoted on scalar MAE alone. It must be evaluated
through the multi-index curve-first policy and must expose:

- raw error;
- mean-centered shape fidelity;
- offset and continuity behavior;
- harmonic amplitude and phase fidelity;
- robustness and per-condition behavior;
- measured-versus-predicted visual evidence;
- causal input availability;
- deployment readiness;
- separate `Fw`, `Bw`, and `global` interpretations where available.

The first pilot should test one formulation against the accepted periodic GRU
and periodic harmonic MLP references. Multiple unverified physics laws should
not be mixed in the first experiment.

## Immediate TODO

1. Reproduce the Bauer signal-processing and complete quadratic coefficient
   law on the repository dataset.
2. Reconstruct the recovered ONNX and PLC coefficient conventions, units,
   directions, and harmonic sets.
3. Benchmark all three Polynomial-Fourier variants on identical `Fw` and `Bw`
   held-out conditions.
4. Complete the equation, variable, unit, and observability matrix for the
   selected compatibility residual.
5. Select the first full-PINN formulation only after the analytical audit.
6. Create the implementation-specific technical document and campaign plan.
7. Run a bounded single-formulation pilot before any Wave 6 campaign design.

## Canonical Inputs

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/mmt_residual_explanatory_diagnostic/[2026-07-24]/wave52_mmt_residual_explanatory_rerun.md`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/non_mmt_cross_wave_comparison/[2026-07-24]/non_mmt_cross_wave_comparison_report.md`
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`
- `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`
- `doc/reference_summaries/09_TE_Modeling_Reference_Library_Summary.md`
- `doc/reference_summaries/10_Polynomial_Fourier_TE_Model_Project_Summary.md`
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`
- `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
- `doc/reference_summaries/14_MMT_Linkage_Matlab_Project_Summary.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/sharepoint_reference_evidence_matrix.md`
- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/06_PolynomialFourierSeriesModel/`
- `reference/te_modeling/`
- `reference/MMT_TEModeling.pdf`
- `reference/Report Machine Learning.pdf`
