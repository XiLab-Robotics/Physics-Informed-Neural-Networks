# Wave 5.2 Full-PINN Theory Validation Test Roadmap

## Program Decision

Wave 5.2 will systematically implement and evaluate the complete usable physics
portfolio extracted from the curated TE reference library.

The program is intentionally broad. It does not assume that one paper, one
equation, or one neural architecture can represent the complete reducer.
Instead, every physical mechanism receives an explicit falsification path and
one or more isolated candidate models.

The absence of a currently measured variable does not remove a theory from the
program. It changes its first validation route from online PINN training to
offline oracle, reduced-order modeling, causal reconstruction, or future
instrumentation.

No training is authorized by this roadmap.

## Program Objectives

1. Reproduce every locally testable analytical formulation.
2. Determine which physical relationships are supported by the current data.
3. Determine which relationships require temporal reconstruction or new
   instrumentation.
4. Build multiple interpretable PINN families rather than one premature
   monolithic model.
5. Reject or revise physical losses that fail equation-level or curve-level
   tests.
6. Preserve useful negative results and blocked formulations.
7. Integrate only independently validated physical ingredients in Wave 6.

## Common Validation Stack

Every formulation must pass the same validation layers.

| Layer | Required evidence |
| --- | --- |
| Source fidelity | Equation, symbols, assumptions, geometry, and validity domain match the source. |
| Dimensional correctness | Units and coordinate transforms close without hidden scale factors. |
| Numerical correctness | Deterministic equation tests pass over nominal and boundary conditions. |
| Synthetic correctness | The implementation recovers known parameters or curves from controlled synthetic cases. |
| Observability | Every training and inference input is measured, causally reconstructed, or explicitly latent. |
| Identifiability | Parameter recovery is stable under noise, initialization, and correlated inputs. |
| Leakage safety | No validation or test TE value enters features, states, parameters, or normalization. |
| Data falsification | The predicted physical trend survives held-out operating conditions. |
| Incremental value | The physical term beats metadata-only, shuffled, zero-weight, and matched-complexity controls. |
| Curve fidelity | Raw error, centered shape, offset, amplitude, phase, slope, and continuity are reported. |
| Directionality | `Fw`, `Bw`, and global or lost-motion implications remain separate. |
| Robustness | Noise, missing signals, extrapolation, parameter perturbation, and regime boundaries are tested. |
| Deployment | Causal availability, execution cost, state initialization, and TwinCAT inspectability are documented. |

## Mandatory Controls

Every PINN campaign must contain:

- an identical neural architecture without the physical loss;
- a zero-weight physical-loss arm;
- a shuffled or mismatched-physics control where meaningful;
- a matched-parameter-count data-driven comparator;
- the accepted time-windowed periodic GRU reference;
- the accepted non-windowed periodic harmonic MLP reference;
- direction-specific evaluation;
- at least one synthetic case with known physical truth;
- per-term loss and gradient-scale logging;
- sensitivity to physical-loss weight;
- repeat-seed evidence;
- explicit failure criteria.

## Readiness Lanes

### Lane A: Directly Testable

Current signals substantially support:

- angular periodicity;
- Polynomial-Fourier coefficient surfaces;
- harmonic amplitude and phase consistency;
- direction-specific curve reconstruction;
- mean-offset and quasi-static torque dependence;
- local smoothness and periodic boundary conditions.

### Lane B: Reconstructable

These require causal preprocessing or ordered trajectories:

- angular acceleration;
- temporal history;
- reversal and hysteresis state;
- temperature-rate effects;
- approximate compliance;
- global lost-motion proxies;
- load-cycle counters.

### Lane C: Offline Oracle Or Instrumentation

These require variables not presently available for online inference:

- component manufacturing errors;
- bearing and mesh stiffness;
- clearances and contact forces;
- load sharing;
- frictional power loss and efficiency;
- load inertia where it varies by setup;
- wear depth and lubrication state;
- motor current and electromechanical fault state.

Lane C formulations remain active research branches. They begin with synthetic
or reduced-order oracle tests and may move to Lane B or Lane A when measurement
or causal-estimation support exists.

## Phase 0: Program Foundations

### Current Progress

Phase 0 is complete and passed:

- all 1,938 directional curves and 75,585,373 numeric rows were scanned;
- `Fw`, `Bw`, and global-pairable coverage each contain 969 conditions;
- all curves cover one output-equivalent revolution and pass direction-sign
  checks;
- the nominal grid is the complete `17 x 19 x 3` Cartesian product;
- all 291 validation and test conditions remain inside training-supported axis
  values;
- causal, PLC, temporal, acceleration, inertia, and unavailable-signal
  classifications are versioned;
- harmonics 1 through 400 were audited on 2,048-point normalized revolutions;
- three nominal-versus-measured metadata anomalies are retained for provenance
  but excluded from Phase 1 fitting, leaving 966 eligible paired conditions.

### Purpose

Create the shared contracts required by all later experiments.

### Tests

- canonical dataset and manifest inventory;
- `Fw`, `Bw`, and global surface coverage;
- angular-grid and revolution segmentation audit;
- input-side versus output-side angle reconciliation;
- speed, torque, temperature, TE, phase, and time unit audit;
- sign and direction convention audit;
- interpolation versus extrapolation condition map;
- temporal ordering and reversal-cycle inventory;
- acceleration and load-inertia availability audit;
- signal-causality and PLC-availability matrix;
- harmonic-order map from reducer geometry and measured spectra;
- duplicate-condition and leakage audit.

### Exit Gate

No physical formulation advances until its required inputs and held-out
conditions are represented in a versioned contract.

## Phase 1: Polynomial-Fourier Analytical Benchmark

### Completion Evidence

The common-data foundation and analytical comparison are implemented:

- 969 nominal operating conditions are paired across `Fw` and `Bw`;
- the pair is assigned once to 678 training, 194 validation, and 97 test
  conditions;
- all 1,938 directional CSV files carry SHA-256 provenance;
- split disjointness, exact pairing, schema compatibility, sizes, and content
  hashes pass the repository validator;
- the stable split-assignment signature is
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.
- the Phase 0 measurement audit excludes three anomalous training conditions,
  leaving 675 training, 194 validation, and 97 test conditions eligible for
  Phase 1;
- all 1,932 eligible directional curves are normalized to 2,048 angular
  samples and evaluated through six analytical variants;
- deterministic Fourier, phase-wrapping, quadratic-recovery, PLC-basis, PLC
  parser, and ONNX I/O contracts pass;
- the local-order Bauer quadratic wins the held-out multi-index rank with
  combined-direction mean raw MAE `0.001887 deg`;
- the reduced common-order quadratic is retained as the alternative comparator
  with combined-direction mean raw MAE `0.001906 deg`;
- the paper-order transfer is weaker, recovered ONNX remains a forward-only
  comparator, PLC degree 10 is unstable on parts of the forward common domain,
  and the direct Fourier oracle remains target-leaking.

### Source Basis

- Bauer et al.;
- internal Fourier and Polynomial design note;
- recovered MATLAB ONNX predictor;
- PLC Polynomial-Fourier implementation.

### Candidate Models

- `PF-A`: Bauer complete quadratic coefficient law;
- `PF-B`: recovered ONNX coefficient predictor;
- `PF-C`: PLC 35-term polynomial evaluator;
- `PF-D`: direct per-condition Fourier oracle;
- `PF-E`: reduced common-order formulation.

### Tests

- preprocessing parity;
- coefficient extraction and reconstruction identity;
- sine-versus-cosine and phase-wrapping parity;
- local harmonic-order selection;
- quadratic-term collinearity and coefficient stability;
- common-split `Fw` and `Bw` interpolation;
- operating-domain edge tests;
- paper-order versus local-order ablation;
- offset-included versus centered-shape comparison;
- coefficient smoothness over torque, speed, and temperature;
- PLC intermediate-value parity;
- ONNX runtime parity against MATLAB examples;
- compute-time and memory audit.

### Exit Gate

Select one analytical reference and one alternative comparator. Do not call
either a full PINN yet.

**Status: passed.** `PF_A_LOCAL_QUADRATIC` is the analytical reference and
`PF_E_REDUCED_QUADRATIC` is the alternative comparator. Phase 2 is the active
next phase; no PINN training has yet been authorized.

## Phase 2: Harmonic And Kinematic Constraint PINNs

### Source Basis

- Ghorbel;
- Iwasaki;
- Bauer;
- MMT harmonic mapping;
- Waves 3.1 through 3.3 and Wave 5.1 evidence.

### Candidate Models

- `PINN-H1`: periodic-boundary residual;
- `PINN-H2`: admissible-order spectral residual;
- `PINN-H3`: amplitude and phase consistency residual;
- `PINN-H4`: direction-conditioned coefficient-surface residual;
- `PINN-H5`: mechanism-grouped harmonic-head model;
- `PINN-H6`: Polynomial-Fourier analytical component plus learned residual.

### Tests

- exact periodic-boundary closure;
- angular-shift equivariance;
- dominant-order retention;
- unseen-condition amplitude and phase interpolation;
- phase-wrap stability;
- spurious-harmonic suppression;
- order-drop and order-add ablations;
- geometry-order perturbation;
- harmonic-loss weight sweep;
- gradient conflict between data and harmonic residuals;
- comparison with Fourier-head-only models to prove genuine physics value.

### Exit Gate

Promote only constraints that improve held-out harmonic fidelity without
degrading raw error, offset behavior, or direction-specific continuity.

**Status: completed negative result.** The canonical eight-run campaign
completed without failures and the bounded common-split curve-payload
diagnostic evaluated `97` held-out curves per direction. `H1-Bw` improved raw
error and selected orders relative to the Fourier control but worsened
aggregate harmonic-amplitude fidelity. No oscillator, periodic-boundary, or
Bauer-anchor constraint was promoted. Phase 3 subsequently completed without
promoting a compliance constraint.

## Phase 3: Quasi-Static Compliance And Elastic Offset PINNs

### Source Basis

- Olabi;
- Ghorbel;
- Mesmer;
- bidirectional TE and rigidity studies;
- completed offset investigations.

### Candidate Models

- `PINN-C1`: bounded linear compliance;
- `PINN-C2`: temperature-conditioned stiffness;
- `PINN-C3`: direction-specific nonlinear compliance;
- `PINN-C4`: analytical offset component plus learned periodic residual;
- `PINN-C5`: shared stiffness with direction-specific backlash offsets.

### Tests

- torque-sign symmetry and asymmetry;
- zero-torque intercept;
- monotonic elastic-deflection checks;
- positive-stiffness constraints;
- temperature-transfer tests;
- stiffness identifiability under correlated torque and temperature;
- load-unload consistency;
- condition-held-out compliance recovery;
- raw-offset versus centered-shape separation;
- bounded-parameter and initialization sensitivity.

### Exit Gate

Retain a compliance residual only if stiffness-like parameters are stable,
physically signed, and predictive outside the fitting conditions.

**Status: completed negative result.** The twelve-arm campaign and two-run
C1-Fw stability follow-up completed without failures. Bounded stiffness was
stable with a `2.48%` coefficient of variation, but only two of three C1-Fw
initializations improved the matched control across raw, offset, centered,
harmonic-amplitude, and phase gates. C2-Bw and C5-global exposed useful
tradeoffs but failed the joint exit rule. No Phase 3 compliance residual was
promoted. Phase 4 subsequently closed as a non-training feasibility result.

## Phase 4: Hysteresis, Friction, And Memory PINNs

### Source Basis

- Iwasaki;
- Ruderman and Iwasaki;
- Mesmer 2022 and 2023;
- Wave 4.4 stateful evidence.

### Candidate Models

- `PINN-Y1`: Bouc-Wen state residual;
- `PINN-Y2`: rolling-friction hysteresis residual;
- `PINN-Y3`: rate-independent play or stop operator;
- `PINN-Y4`: temperature- and load-conditioned hysteresis;
- `PINN-Y5`: white-box hysteresis state plus learned residual;
- `PINN-Y6`: NARX or GRU comparator with matched causal history.

### Tests

- ordered-cycle reconstruction;
- state-initialization and warm-up sensitivity;
- minor-loop and major-loop reproduction;
- direction-reversal holdout;
- rate-independence falsification;
- temperature and load transfer;
- state saturation and boundedness;
- memory-length ablation;
- shuffled-time negative control;
- static-sample versus sequential evaluation;
- noise accumulation and long-rollout stability;
- deterministic PLC state reset.

### Exit Gate

No hysteresis model advances without repeated reversal cycles and stable causal
state evolution.

**Status: completed feasibility result; no training authorized.** The audit
scanned all `969` canonical raw operating-condition files. Every file
preserves one ordered `Fw`-to-`Bw` transition and therefore supports an
offline reversal oracle, but none contains repeated reversal cycles or
repeated major loops. Minor-loop labels, controlled warm-up labels, and
deterministic reset markers are also absent. `PINN-Y1`, `PINN-Y2`, `PINN-Y3`,
and `PINN-Y5` remain synthetic-oracle-only; `PINN-Y4` is blocked by the data
contract; `PINN-Y6` is offline-oracle-only. No Phase 4 physical residual is
promoted.

## Phase 5: Bidirectional TE, Backlash, And Lost-Motion PINNs

### Source Basis

- Wang bidirectional drive TE;
- Xu rigidity and lost motion;
- Iwasaki and Mesmer hysteresis evidence;
- repository `Fw`, `Bw`, and global policy.

### Candidate Models

- `PINN-B1`: separate `Fw` and `Bw` heads with shared periodic trunk;
- `PINN-B2`: forward-reverse compatibility loss;
- `PINN-B3`: global lost-motion latent variable;
- `PINN-B4`: backlash dead-zone or smooth complementarity residual;
- `PINN-B5`: direction-transition state model.

### Tests

- paired-condition `Fw` and `Bw` consistency;
- reversal gap and global lost-motion estimation;
- zero-crossing and dead-zone behavior;
- smooth and nonsmooth residual comparison;
- direction-label perturbation;
- shared-versus-independent parameter ablation;
- output-mechanism contribution sensitivity;
- unavailable-component-error identifiability test;
- transition-state causality and initialization;
- separate raw, centered, offset, and continuity surfaces.

### Exit Gate

Advance only reduced compatibility laws that remain identifiable without
target-derived component errors.

**Status: completed identifiability result; no training authorized.** All
`969` paired conditions and `37,805,294` simplified-source rows were audited.
Median centered `Fw`/`Bw` correlation is `0.985-0.990`, but the median
absolute directional mean gap is `3.79-4.78 arcmin`. The paired gap and the
`0.703125 deg` median target-derived alignment are offline target evidence,
not independent lost-motion or backlash states. `PINN-B1` remains a
real-data-trainable empirical comparator but is not a full PINN; `PINN-B2` is
blocked by missing component errors and geometry-specific equivalence
parameters; `PINN-B3` and `PINN-B5` are offline-oracle-only; `PINN-B4` is
synthetic-oracle-only. No Phase 5 physical residual is promoted.

## Phase 6: Dynamic Acceleration, Inertia, And Trajectory PINNs

### Source Basis

- Xu variable-speed dynamic TE;
- Ghorbel inertial dependence;
- temporal model evidence.

### Candidate Models

- `PINN-D1`: acceleration-conditioned TE residual;
- `PINN-D2`: reduced inertia and acceleration balance;
- `PINN-D3`: causal state-space dynamic residual;
- `PINN-D4`: periodic analytical component plus temporal dynamic residual;
- `PINN-D5`: learned latent inertia with bounded prior.

### Tests

- acceleration reconstruction and noise amplification;
- constant-speed null test;
- acceleration-sign reversal;
- drive-law transfer;
- load-inertia sensitivity;
- temporal-window length;
- derivative smoothing ablation;
- causal versus centered numerical derivatives;
- transient versus steady-state separation;
- rollout stability;
- missing-inertia identifiability;
- input-speed-only negative control.

### Exit Gate

Dynamic residuals advance only if acceleration or inertia adds held-out value
beyond causal temporal baselines and remains robust to derivative noise.

**Status: completed observability result; no training authorized.** The audit
scanned `99,696,607` raw rows across all `969` conditions. Every directional
validity window passes the speed-stability check, but no inter-window
transition achieves a fourfold P95 acceleration separation after a 101-row
causal filter; median valid-to-transition ratios are `0.996-1.005`. Raw upper
tails are contaminated by encoder discontinuities. Load inertia, commanded
drive law, repeated dynamic trajectories, and a validated transient TE target
are unavailable. `PINN-D1` and `PINN-D3` remain offline-oracle-only;
`PINN-D2` and `PINN-D5` are blocked; `PINN-D4` is an empirical trainable
comparator but not a full PINN. No Phase 6 physical residual is promoted.

## Phase 7: Contact, Mesh Stiffness, And Load-Sharing PINNs

### Source Basis

- Xu contact and rigidity model;
- Chen tooth and load contact analysis;
- MMT equivalent mechanism;
- Wang efficiency force analysis.

### Candidate Models

- `PINN-K1`: reduced positive mesh-stiffness residual;
- `PINN-K2`: non-penetration and contact-activation constraint;
- `PINN-K3`: smooth complementarity contact PINN;
- `PINN-K4`: normalized load-sharing constraint;
- `PINN-K5`: reduced contact oracle plus learned correction;
- `PINN-K6`: latent contact-state model bounded by offline simulations.

### Tests

- synthetic single-contact and multi-contact cases;
- force balance;
- positive stiffness and contact force;
- non-penetration;
- load-share sum;
- contact transition smoothness;
- clearance and stiffness perturbation;
- parameter-recovery identifiability;
- reduced-order versus detailed-oracle parity;
- noisy geometry and force robustness;
- inference-time observability;
- computational reduction and PLC feasibility.

### Exit Gate

Detailed contact equations remain offline until a reduced formulation is both
identifiable and supported by causally available inputs.

**Status: completed feasibility result; no training authorized.** Six evidence
files, eleven required quantities, and six contact formulations were audited.
Angle, torque, and direction are causal, but component errors, bearing and
mesh stiffness, clearances, contact force, load share, active contact state,
and a trusted local solver are unavailable for real-data identification.
`PINN-K1` through `PINN-K5` remain synthetic-oracle-only and `PINN-K6` is
blocked. No Phase 7 physical residual is promoted.

## Phase 8: Energy, Friction, And Efficiency PINNs

### Source Basis

- Wang nonlinear transmission-efficiency analysis;
- Mesmer friction and temperature dependence;
- electromechanical coupling evidence.

### Candidate Models

- `PINN-E1`: non-negative dissipation constraint;
- `PINN-E2`: bounded efficiency surface;
- `PINN-E3`: load- and speed-dependent friction residual;
- `PINN-E4`: temperature-conditioned loss model;
- `PINN-E5`: auxiliary energy-consistency head.

### Tests

- zero-load and low-speed limits;
- non-negative dissipated power;
- efficiency bounds;
- speed and load monotonicity within the stated domain;
- temperature sensitivity;
- sign and direction consistency;
- missing-force proxy sensitivity;
- source-domain versus local-domain mismatch;
- auxiliary-loss gradient conflict;
- comparison with metadata-only regularization.

### Exit Gate

Energy constraints may be retained as auxiliary physics only when their
required power or force quantities are measured or validated causally.

**Status: completed feasibility result; no training authorized.** Five
evidence files, eleven required quantities, and five energy formulations were
audited. Output torque, speed, temperature, and direction are causal, but
input torque or power, internal contact force, friction loss, and efficiency
are absent. `PINN-E1/E2` remain synthetic-oracle-only, `PINN-E5` is
offline-oracle-only, and `PINN-E3/E4` are blocked. No Phase 8 physical
residual is promoted.

## Phase 9: Geometry, Tolerances, MMT, And Manufacturing Priors

### Source Basis

- MMT paper and MATLAB demonstrator;
- Jin tolerance virtual prototype;
- Chen geometric-error model;
- Wang FEA and ensemble study.

### Candidate Models

- `PINN-G1`: manufacturing-prior parameter regularization;
- `PINN-G2`: geometry-to-harmonic sensitivity surrogate;
- `PINN-G3`: MMT synthetic-oracle PINN;
- `PINN-G4`: condition-varying MMT model if measurements become available;
- `PINN-G5`: geometry-latent hierarchical model across reducer instances.

### Tests

- known-geometry synthetic recovery;
- tolerance perturbation and ranking;
- harmonic-source attribution;
- shuffled-geometry control;
- unit-to-unit transfer;
- latent-parameter identifiability;
- target-leakage audit;
- condition-invariance negative control;
- MMT equation-chain reproduction;
- reduced versus full mechanism parity;
- calibration only from independent physical measurements.

### Exit Gate

Paper-faithful MMT remains deferred until condition-varying causal component
errors exist. Synthetic and manufacturing-prior branches may proceed
independently.

**Status: active next.** Start with geometry, tolerance, component-error, MMT,
synthetic-population, instance-identity, and transfer-protocol audits.

## Phase 10: Wear And Degradation PINNs

### Source Basis

- Chen Archard-wear and contact model;
- tolerance and geometry sensitivity studies.

### Candidate Models

- `PINN-W1`: cumulative load-cycle wear state;
- `PINN-W2`: Archard-inspired latent degradation residual;
- `PINN-W3`: monotonic health-state constraint;
- `PINN-W4`: contact-oracle wear surrogate;
- `PINN-W5`: multi-session hierarchical degradation model.

### Tests

- synthetic monotonic wear progression;
- load-cycle accumulation;
- no-load null progression;
- long-horizon rollout;
- session and reducer identity separation;
- maintenance-event reset;
- extrapolation in accumulated usage;
- confounding by temperature and lubrication;
- identifiability without direct wear labels;
- TE-drift correlation versus causal prediction.

### Exit Gate

Wear PINNs remain research models until longitudinal data or validated wear
labels distinguish degradation from operating-condition drift.

## Phase 11: Electromechanical Coupling PINNs

### Source Basis

- E et al. electromechanical RV fault model;
- motor, reducer, and frequency-sideband relationships.

### Candidate Models

- `PINN-M1`: current-sideband consistency loss;
- `PINN-M2`: motor-torque and mechanical-state coupling;
- `PINN-M3`: joint TE and fault-health multi-task model;
- `PINN-M4`: electromechanical state observer plus TE residual.

### Tests

- motor-current signal availability and synchronization;
- supply and mesh-order sideband extraction;
- healthy-condition null test;
- synthetic fault injection;
- speed-varying frequency normalization;
- current-to-TE incremental value;
- sensor latency and noise;
- false-positive resistance;
- causal observer stability;
- TwinCAT acquisition and runtime feasibility.

### Exit Gate

This branch activates only when synchronized motor-current and drive-state
signals are available.

## Phase 12: Hybrid Analytical And Learned Residual PINNs

### Source Basis

- Steinle hybrid compensation pattern;
- validated outputs from Phases 1 through 11.

### Candidate Models

- `PINN-R1`: analytical law plus bounded MLP residual;
- `PINN-R2`: analytical law plus temporal residual;
- `PINN-R3`: global physical component plus localized tree or neural residual;
- `PINN-R4`: uncertainty-aware physical residual;
- `PINN-R5`: mixture model gated by validated physical regime;
- `PINN-R6`: shared physical trunk with direction-specific residuals.

### Tests

- analytical-only, learned-only, and combined ablation;
- residual magnitude and localization;
- physical-component corruption test;
- matched-capacity control;
- residual smoothness and extrapolation;
- uncertainty calibration;
- regime-gate interpretability;
- physical-loss and data-loss gradient compatibility;
- deployment cost;
- closed-loop compensation simulation when available.

### Exit Gate

Hybrid models advance only when the learned residual adds held-out value
without erasing the interpretability or stability of the physical component.

## Phase 13: Cross-Formulation Tournament

Every surviving isolated formulation enters a common comparison.

### Required Surfaces

- `Fw`;
- `Bw`;
- global or lost-motion where available;
- interpolation;
- operating-domain boundary;
- extrapolation;
- steady state;
- transient and reversal conditions;
- noise and missing-signal stress tests;
- TwinCAT deployment readiness.

### Required Rankings

- best raw error;
- best centered-shape fidelity;
- best offset behavior;
- best harmonic fidelity;
- best direction and reversal behavior;
- best robustness;
- best physical identifiability;
- best causal deployability;
- best computational efficiency.

There will be no single scalar winner. A formulation may remain valuable as an
offset, harmonic, dynamic, state, uncertainty, or diagnostic component.

## Phase 14: Integrated Multi-Physics PINNs

Only independently validated components may be combined.

### Integration Sequence

1. periodic plus compliance;
2. periodic plus hysteresis;
3. periodic plus dynamic state;
4. periodic plus bidirectional compatibility;
5. compliance plus hysteresis;
6. reduced contact plus dynamic state;
7. uncertainty or mixture treatment around validated physical components;
8. wear or electromechanical heads when their datasets exist.

### Combination Tests

- factorial component ablation;
- pairwise and higher-order interaction analysis;
- loss-weight Pareto fronts;
- gradient-conflict diagnostics;
- parameter-identifiability degradation;
- error-compensation cancellation;
- over-constraint detection;
- runtime and memory growth;
- cross-condition and cross-session transfer;
- failure-mode localization.

### Exit Gate

An integrated model must outperform its strongest isolated components on
multiple curve-first surfaces and retain inspectable intermediate quantities.

## Phase 15: Wave 6 Entry

Wave 6 may begin when:

- at least two complementary physical components pass isolated pilots;
- their causal inputs are available;
- their combination passes interaction and identifiability tests;
- the multi-index curve-first pipeline supports integration;
- the resulting architecture has a credible TwinCAT execution path.

Wave 6 will then treat validated physics as explicit multi-task or multi-head
ingredients rather than speculative regularization.

## Experiment Package Required For Every Pilot

Every phase that reaches training requires:

- a dedicated technical document;
- an explanatory model and physics-loss report;
- a campaign planning report;
- campaign YAML and immutable run-instance paths;
- a local and `-Remote` PowerShell launcher;
- synthetic-oracle tests;
- one-batch validation;
- baseline and negative-control arms;
- campaign leaderboard and explicit winner artifacts;
- Markdown and PDF campaign-results report;
- optional separate TE Curve Verification Pipeline launcher after closeout;
- backlog, ledger, registry, and master-summary synchronization.

## Decision Vocabulary

| Decision | Meaning |
| --- | --- |
| accepted component | Physical contribution is supported and may enter integration tests. |
| accepted diagnostic | Useful for interpretation or validation, but not as a training residual. |
| offline oracle | Retained for synthetic or simulator-backed validation. |
| revise | Evidence supports the mechanism but not the current equation or parameterization. |
| instrumentation required | Cannot advance without new measured or synchronized signals. |
| deferred | Preserved with an explicit reopening condition. |
| rejected | Failed its source, equation, falsification, leakage, or incremental-value gate. |

## Execution Order

The phases are not a single rigid serial queue. They form three parallel lanes:

1. **Immediate analytical lane:** Phases 0, 1, 2, and 3.
2. **Causal-state lane:** Phases 4, 5, and 6.
3. **Offline-physics lane:** Phases 7 through 11.

Phase 12 begins as soon as one analytical and one learned residual component
are validated. Phase 13 compares all survivors. Phase 14 integrates them.
Phase 15 opens Wave 6.

The immediate next implementation remains Phase 1: reproduce the Bauer
preprocessing, coefficient fitting, and Fourier reconstruction on the frozen
common split before adding the recovered ONNX and PLC paths.
