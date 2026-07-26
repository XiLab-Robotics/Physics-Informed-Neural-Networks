# Wave 5.2 Full PINN Physics Formulation Roadmap

## Executive Decision

Wave 5.2 remains the physics-informed model-development wave. Its general
full-PINN program has completed Phases 0 through 4 and now advances to the
Phase 5 bidirectional TE, backlash, and lost-motion formulation gate.

Only the paper-faithful MMT implementation is deferred. The completed MMT
diagnostic established that the available geometry-locked signatures are
condition-invariant and that the required causal component-error and
contact-state quantities are unavailable. That result blocks the current MMT
parameterization; it does not disprove transmission-error physics or block
other physics-informed formulations.

No PINN implementation or training campaign is authorized by this roadmap.
Each bounded pilot will require a new approved technical document and campaign
plan.

The complete source-to-test sequence is defined in
`full_pinn_theory_validation_test_roadmap.md`. That roadmap preserves every
ingested theory through a direct-data, causal-reconstruction, offline-oracle,
instrumentation, isolated-PINN, or integration path.

## Corrected Program Structure

| Program branch | Current state | Decision |
| --- | --- | --- |
| General Wave 5.2 full-PINN program | Phases 0-4 complete; Phase 5 active next | Audit references, formalize candidate equations, and validate them before implementation. |
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
| WP2 Equation audit | Verified equations, units, assumptions, and observable-variable map | active across later mechanisms; harmonic and compliance equations audited |
| WP3 Analytical verification | Equation tests on measured curves plus synthetic or analytical oracles | Phase 1 benchmark, Phase 3 identifiability audit, and Phase 4 raw-chronology audit complete; later mechanisms pending |
| WP4 Bounded formulation pilots | One isolated formulation per approved campaign | Phases 2 and 3 complete as negative screens; Phase 4 closed without training after its feasibility gate failed |
| WP5 Curve-first verification | Separate raw, centered-shape, offset, harmonic, robustness, visual, and deployment surfaces | complete for Phases 2 and 3; retained as mandatory |
| WP6 Formulation decision | Accept, revise, combine, or reject each formulation | Phase 2 and Phase 3 constraints rejected; Phase 4 real-data hysteresis training rejected while synthetic and offline-oracle lanes are retained |
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

Phases 0 through 4 are complete. Phases 2 and 3 closed as valid negative
training results. Phase 4 scanned all `969` canonical raw conditions and found
one ordered `Fw`-to-`Bw` reversal per condition, but no repeated reversal
cycles, repeated major loops, minor-loop labels, controlled warm-up labels, or
deterministic reset markers. Real-data hysteresis training is therefore not
authorized; synthetic and offline reversal-oracle lanes remain reusable.

1. Begin Phase 5 with a paired-condition bidirectional TE and lost-motion
   identifiability audit.
2. Quantify `Fw`/`Bw` mean, centered-shape, offset, and phase compatibility on
   the common split without using target-derived component errors.
3. Classify `PINN-B1` through `PINN-B5` as directly trainable,
   offline-oracle-only, synthetic-oracle-only, or blocked.
4. Keep the Phase 4 raw reversal trajectories as offline evidence only; do not
   reinterpret a single reversal as an identified hysteresis state.
5. Keep Phase 2 and Phase 3 physics weights at zero by default.
6. Continue using the common split and accepted time-windowed and
   non-windowed references where the data contract remains valid.
7. Keep Wave 6 deferred until at least two complementary physical components
   pass isolated pilots.

Subsequent pilots follow the three-lane program defined in the complete test
roadmap:

- immediate analytical formulations;
- causal state and history formulations;
- offline physics, synthetic oracle, and instrumentation-dependent
  formulations.

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
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/full_pinn_theory_validation_test_roadmap.md`
- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/06_PolynomialFourierSeriesModel/`
- `reference/te_modeling/`
- `reference/MMT_TEModeling.pdf`
- `reference/Report Machine Learning.pdf`
