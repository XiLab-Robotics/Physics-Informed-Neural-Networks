# Wave 5.2 Physics Reference Intake Register

## Purpose

This register is the controlled intake surface for scientific papers,
engineering reports, equations, and implementation references that may support
the Wave 5.2 full-PINN program.

Registration does not imply acceptance. Each source must pass equation,
observability, identifiability, causal-availability, and deployment checks
before it can justify implementation or training.

## Intake Status Vocabulary

| Status | Meaning |
| --- | --- |
| queued | Source is available but has not been reviewed. |
| screening | Scope, relevance, and provenance are being checked. |
| theory audit | Equations, variables, units, and assumptions are being reconstructed. |
| experiment mapping | The formulation is being mapped to available data and falsification tests. |
| candidate | Evidence is sufficient to propose a bounded implementation plan. |
| reference only | Useful context, but not a defensible physical residual for the current dataset. |
| deferred | Potentially relevant, but blocked by missing physical quantities or incompatible assumptions. |
| rejected | The formulation failed a stated evidence or feasibility gate. |

## Current Seed Sources

| ID | Source | Current status | Intended use | Main gate |
| --- | --- | --- | --- | --- |
| `PINN-REF-001` | `reference/MMT_TEModeling.pdf` | deferred for paper-faithful implementation | Equivalent mechanism, loop increments, component-error structure, and frequency interpretation | Condition-varying causal component-error and contact-state inputs are unavailable. |
| `PINN-REF-002` | `reference/Report Machine Learning.pdf` | reference only | Test-rig behavior, harmonic content, operating variables, TE extraction, and deployment context | Separate source-backed physics from empirical workflow guidance. |
| `PINN-REF-003` | Polynomial Fourier Series PLC implementation | theory audit in progress | First explicit semi-analytical curve law and candidate differentiable analytical component | Reconcile its 35-term evaluator, coefficients, units, angular convention, fit provenance, and validity range with the Bauer and MATLAB variants. |
| `PINN-REF-004` | `reference/RCIM_ML-compensation.pdf` | reference only | Baseline modeling, compensation context, and deployability constraints | It must not be presented as a governing physical formulation without separate equations. |
| `PINN-REF-005` | SharePoint TE reference library | intake complete | Curated source inventory, deduplication record, and traceable source paths | Use the per-source records below; library membership does not imply equation acceptance. |

## Imported Source Records

The full evidence, limitation, and decision record is maintained in
`sharepoint_reference_evidence_matrix.md`.

| ID range | Source group | Status | Principal result |
| --- | --- | --- | --- |
| `PINN-REF-006` to `PINN-REF-007` | Bauer paper and internal Polynomial-Fourier note | theory audit | Strongest immediately auditable semi-analytical baseline |
| `PINN-REF-008` to `PINN-REF-013` | Harmonic, hysteresis, and offline-compensation bibliography | experiment mapping | Supports separation of periodic, compliance, and causal memory terms |
| `PINN-REF-014` to `PINN-REF-015` | ML compensation bibliography | reference only | Supports interpretable-plus-learned residual architectures and controller-aware validation |
| `PINN-REF-016` to `PINN-REF-023` | RV theoretical mechanics | theory audit or reference only | Supplies dynamic, bidirectional, contact, tolerance, efficiency, wear, and electromechanical evidence |
| `PINN-REF-024` | Recovered MATLAB ONNX TE predictor | theory audit | Hybrid learned-coefficient Fourier baseline; not the Bauer quadratic law |
| `PINN-REF-025` | MMT linkage MATLAB demonstrator | deferred for full-PINN use | Retain as a harmonic diagnostic and synthetic oracle |

## Required Per-Source Record

For every new reference, the analysis must record:

1. full citation and repository path;
2. source type and provenance;
3. reducer or mechanism type;
4. stated phenomenon and validity domain;
5. complete equations and symbol definitions;
6. units, coordinates, directions, and sign conventions;
7. boundary, initial, periodic, contact, or interface conditions;
8. required geometry and material parameters;
9. required measured or reconstructed operating variables;
10. quantities unavailable in the current dataset;
11. assumptions that can and cannot be tested;
12. differentiability and numerical-conditioning considerations;
13. identifiability and parameter-correlation risks;
14. causal availability during PLC inference;
15. target-leakage risks;
16. candidate PINN residual, constraint, or analytical component;
17. proposed equation-level and curve-level falsification tests;
18. TwinCAT and PLC implementation implications;
19. conflicts or compatibility with other sources;
20. final status and evidence-backed recommendation.

## Evidence Separation

Each synthesis must keep four categories separate:

- source-backed claims;
- repository-observed or implemented facts;
- proposed interpretations and experiments;
- unresolved questions.

An equation will not enter an implementation plan if its required variables are
derived from validation or test TE targets, if its units cannot be reconciled,
or if its assumptions cannot be mapped to the current reducer and test-rig
conditions.

## Formulation Mapping Table

This table will be expanded as references arrive.

| Formulation ID | Supporting reference IDs | Equation audit | Observable-variable audit | Oracle test | Pilot state |
| --- | --- | --- | --- | --- | --- |
| `PINN-FORM-A` Polynomial-Fourier structured residual | `PINN-REF-003`, `PINN-REF-006`, `PINN-REF-007`, `PINN-REF-024` | partial; three distinct coefficient laws identified | basic operating variables available | common-split reproduction pending | benchmark audit approved; training not authorized |
| `PINN-FORM-B` Harmonic and directional constraints | `PINN-REF-008`, `PINN-REF-009`, `PINN-REF-020` | partial | periodicity and direction observable; component errors incomplete | reduced compatibility test pending | research candidate |
| `PINN-FORM-C` Compliance and hysteresis | `PINN-REF-010` to `PINN-REF-013`, `PINN-REF-018` | partial | ordered trajectory and stiffness audit pending | reversal and initialization tests pending | observability audit first |
| `PINN-FORM-D` Dynamic acceleration and inertia | `PINN-REF-017` | partial | acceleration may be reconstructable; inertia uncertain | causal incremental-value test pending | dataset audit first |
| `PINN-FORM-E` Contact, efficiency, tolerance, and wear | `PINN-REF-016`, `PINN-REF-018`, `PINN-REF-021` to `PINN-REF-023` | source equations identified | key physical variables unavailable | synthetic oracle tests only | offline-oracle branch |
| `PINN-FORM-MMT` Paper-faithful MMT | `PINN-REF-001` | partial | blocked | blocked | deferred |

## Next Intake Action

The supplied source intake is complete. The next action is a common-split
analytical benchmark audit of the Bauer quadratic law, recovered ONNX
coefficient predictor, and existing PLC polynomial implementation.

No formulation will be selected merely by publication authority or conceptual
appeal; it must survive the project-specific evidence gates.
