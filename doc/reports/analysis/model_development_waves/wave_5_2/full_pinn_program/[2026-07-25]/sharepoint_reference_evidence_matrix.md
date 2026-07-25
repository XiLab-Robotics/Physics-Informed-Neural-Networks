# Wave 5.2 SharePoint Reference Evidence Matrix

## Decision

The 2026-07-25 SharePoint bundle has been fully inventoried, deduplicated, and
reviewed. It materially strengthens the Wave 5.2 physics program, but it does
not authorize an immediate monolithic full-PINN implementation.

The evidence selects a staged path:

1. reproduce and audit the direction-specific Polynomial-Fourier law;
2. formulate one additional physical compatibility residual;
3. test each contribution independently against the accepted time-windowed and
   non-windowed references;
4. retain detailed contact, wear, and paper-faithful MMT models as deferred or
   offline-oracle branches until their required variables are available.

## Evidence Classification

| Classification | Meaning |
| --- | --- |
| immediately auditable | Inputs and target behavior are substantially available; equation reconstruction can proceed. |
| partial constraint | A bounded relation may be testable, but the complete source model is not observable. |
| offline oracle | Valuable for synthetic tests, sensitivity, or interpretation, but too detailed for current causal inference. |
| reference only | Supports architecture or evaluation, not a local physical residual. |
| deferred | The intended paper-faithful model is blocked by missing causal variables or identifiability. |

## Bibliography Evidence

| ID | Source | Main extracted contribution | Missing or risky quantities | Wave 5.2 classification |
| --- | --- | --- | --- | --- |
| `PINN-REF-006` | Bauer et al., 2025, Polynomial-Fourier cycloidal TE | Direction-specific Fourier series; quadratic torque, velocity, and temperature laws for offset, amplitude, and phase; in-range validation | Reducer-specific orders, exact local coordinate and unit reconciliation, extrapolation evidence | immediately auditable |
| `PINN-REF-007` | Internal Fourier and Polynomial design note | XiLab reproduction decisions, Bauer versus Bilancia preprocessing, input-side versus load-side comparison, preliminary errors, dataset-design gaps | Formal experiment provenance and a controlled same-split rerun | immediately auditable |
| `PINN-REF-008` | Ghorbel, 2001 | Kinematic and torsional-flexibility decomposition; speed and inertia dependence | Harmonic-drive-to-RV transfer, load and friction closure | partial constraint |
| `PINN-REF-009` | Iwasaki et al., 2009 | Synchronous Fourier component plus nonlinear elastic hysteresis; compensation evidence | Harmonic-drive geometry, hysteresis state and local parameterization | partial constraint |
| `PINN-REF-010` | Ruderman and Iwasaki, 2016 | Causal inverse hysteresis map, sensorless torsion estimate, state-initialization issue | Motor-torque observer validation and local hysteresis calibration | partial constraint |
| `PINN-REF-011` | Mesmer et al., 2022 | Bouc-Wen and NARX cycloidal-joint hysteresis models | Ordered reversal data, initial state, locally identifiable parameters | partial constraint |
| `PINN-REF-012` | Mesmer et al., 2023 | Load- and temperature-dependent friction; approximately rate-independent hysteresis; temperature-dependent stiffness | Local friction and stiffness identification, temperature-observer validation | partial constraint |
| `PINN-REF-013` | Olabi et al., 2012 | Separation of joint compliance and kinematic error; axis-specific stiffness identification | Full robot versus reducer transfer, local stiffness measurements | reference only |
| `PINN-REF-014` | Steinle et al., 2024 | Two-stage global elasticity and localized learned compensation; backlash handling | Different rack-and-pinion mechanism and controller | reference only |
| `PINN-REF-015` | Steinle et al., 2025 | Superposition and control insertion for two preloaded drives | Different mechanism, preload state, dual-loop controller | reference only |

## Theoretical Mechanics Evidence

| ID | Source | Main extracted contribution | Missing or risky quantities | Wave 5.2 classification |
| --- | --- | --- | --- | --- |
| `PINN-REF-016` | Wang et al., 2024, nonlinear efficiency | Multi-source force and loss model; speed and load trends | Forces, friction, bearing losses, local parameters | offline oracle |
| `PINN-REF-017` | Xu et al., 2025, variable-speed dynamic TE | Dominant effects of acceleration and load inertia; contact dynamics | Causal acceleration, load inertia, dynamic contact state | partial constraint |
| `PINN-REF-018` | Xu et al., 2025, hysteresis and rigidity | Contact stiffness, bearing clearance, torsional rigidity, and lost-motion relations | Interface stiffness, clearances, geometry, torque history | offline oracle |
| `PINN-REF-019` | E et al., 2026, electromechanical faults | PMSM and RV coupling; current sidebands tied to mechanical faults | Motor current and fault labels | reference only |
| `PINN-REF-020` | Wang et al., 2024, bidirectional TE | Forward TE, reverse TE, and global lost-motion compatibility; output-mechanism contribution | Measured component errors and geometry-specific equivalence parameters | partial constraint |
| `PINN-REF-021` | Jin et al., 2025, tolerance virtual prototype | Manufacturing tolerance sensitivity and validated virtual prototype | Unit-specific manufacturing tolerances | offline oracle |
| `PINN-REF-022` | Chen et al., 2026, geometric errors and wear | Archard wear, contact analysis, 20-degree-of-freedom quasi-static model, long-term TE degradation | Geometry, force, lubrication, wear state, clearances | offline oracle |
| `PINN-REF-023` | Wang et al., 2026, FEA and ensemble prediction | FEA sampling, error sensitivity, stacked surrogate, TE optimization | Paper excludes clearance, dynamics, friction, and thermal effects | offline oracle |

## Implementation Evidence

| ID | Implementation | Observed law | Decision |
| --- | --- | --- | --- |
| `PINN-REF-003` | Existing PLC Polynomial-Fourier block | Direction-specific offset, amplitude, and phase polynomials; orders `1, 3, 39, 40, 78, 81, 156, 162, 240`; explicit 35-term polynomial evaluator | Continue theory audit; compare its law and coefficients with Bauer and the recovered MATLAB path. |
| `PINN-REF-024` | Recovered MATLAB ONNX TE predictor | ONNX-predicted `A0`, order-1, order-39, and order-40 amplitudes and phases | Treat as a hybrid learned-coefficient baseline, not as the Bauer polynomial model. |
| `PINN-REF-025` | MMT linkage MATLAB demonstrator | Manual component-error-to-order mapping for orders `1, 3, 39, 40, 81` | Preserve as a diagnostic and synthetic oracle; paper-faithful full-PINN remains deferred. |

## Candidate Formulation Matrix

| Formulation | Equations | Current observability | Identifiability risk | First falsification test | Decision |
| --- | --- | --- | --- | --- | --- |
| `PINN-FORM-A1` Bauer Polynomial-Fourier baseline | Explicit quadratic coefficient laws plus direction-specific Fourier reconstruction | Torque, speed, temperature, angle, direction, and TE are substantially available | Moderate; phase wrapping and correlated polynomial terms | Reproduce preprocessing and in-range held-out curves on identical Fw and Bw splits | advance to equation audit |
| `PINN-FORM-A2` PLC Polynomial-Fourier baseline | Explicit recovered polynomial coefficient evaluator plus fixed harmonic set | Basic inputs available; coefficient provenance unresolved | High until units, coefficients, and domain are reconstructed | Recalculate stored curves and compare intermediate coefficients term by term | continue audit |
| `PINN-FORM-A3` ONNX-coefficient Fourier baseline | Learned coefficient maps plus orders 1, 39, and 40 | Basic inputs available; canonical ONNX models available | Moderate; coefficient models may be weakly constrained | Run all coefficient models on known CSV cases and reconstruct TE | bounded baseline only |
| `PINN-FORM-B1` Periodic and directional compatibility | Periodicity, direction-specific coefficients, amplitude and phase continuity | Directly observable | Low to moderate | Check violations independently of TE training loss | candidate physical constraint |
| `PINN-FORM-B2` Fw, Bw, and global lost-motion compatibility | Source-derived bidirectional relation | Direction available; global lost motion and component errors incomplete | High | Determine whether an observable reduced relation survives without target-derived inputs | research only |
| `PINN-FORM-C1` Quasi-static compliance | Torque-dependent elastic offset or stiffness relation | Torque and TE available; stiffness not directly measured | Moderate to high | Fit bounded stiffness on training conditions and test direction and temperature transfer | candidate after A1 |
| `PINN-FORM-C2` Bouc-Wen hysteresis state | Differential memory law | Requires ordered torque-angle reversal trajectories | High without rich reversal cycles | State initialization, closed-loop curve, and reversal holdout tests | observability audit first |
| `PINN-FORM-D1` Dynamic acceleration and inertia | Contact-dynamic relation or reduced surrogate | Acceleration may be reconstructable; load inertia uncertain | High | Add causal acceleration and test incremental held-out value | dataset audit first |
| `PINN-FORM-E1` Contact, stiffness, and wear | Detailed multi-contact or reduced-order equations | Key geometry and contact variables unavailable | Very high | Synthetic equation and sensitivity oracle only | offline oracle |
| `PINN-FORM-MMT` Paper-faithful MMT | Equivalent multi-loop component-error equations | Condition-varying component errors unavailable | Critical | Reopen only after independent causal measurement or reconstruction | deferred |

## Recommended First Program Slice

The next technical task should not implement a neural network. It should build
one auditable analytical benchmark package that:

1. reproduces the Bauer signal-processing pipeline;
2. implements the complete quadratic coefficient law;
3. maps the repository's reducer-specific harmonic orders;
4. reconciles the Bauer, ONNX, and PLC conventions;
5. evaluates all three on identical `Fw` and `Bw` held-out conditions;
6. reports raw, centered-shape, offset, amplitude, phase, and continuity
   evidence;
7. exposes every coefficient and intermediate quantity.

Only after that benchmark should the project select one physical residual for
the first full-PINN pilot.

## Complete Program Routing

The remaining evidence is not discarded after the first pilot. Its complete
test sequence is defined in `full_pinn_theory_validation_test_roadmap.md`.

That roadmap routes:

- Polynomial-Fourier, harmonic, and compliance formulations through the
  immediate analytical lane;
- hysteresis, bidirectional lost motion, and dynamic formulations through the
  causal-state lane;
- contact, efficiency, geometry, MMT, wear, and electromechanical formulations
  through the offline-physics and instrumentation lane;
- validated components through hybrid, cross-formulation, and integrated
  multi-physics tests before Wave 6.

## Explicit Non-Decisions

- MMT has not been reactivated.
- The imported contact equations have not been accepted as trainable losses.
- FEA or synthetic labels do not by themselves make a model a PINN.
- The Polynomial-Fourier law has not yet been declared a full PINN.
- No training campaign is authorized by this report.
