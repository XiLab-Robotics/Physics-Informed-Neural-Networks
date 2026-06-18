# Wave 4 PINN Formulation And First PINN

## Purpose

`Wave 4` defines the first physics-informed neural-network branch for TE curve
prediction. Its purpose is to test whether physically motivated soft
constraints improve the same failure modes seen in `Track 2`: mean-surface
bias, centered-shape error, amplitude error, phase error, and fragile harmonic
behavior.

This report is a design document only. It does not prepare runnable training
campaigns and does not modify the active `Track 2H` campaign.

## Reference Boundary

| Source | What It Supports | Wave 4 Consequence |
| --- | --- | --- |
| `MMT_TEModeling` summary | TE is structured by RV reducer kinematics, and frequency components can be interpreted with respect to physical error sources. | Use physics-informed constraints as soft regularizers, not as a black-box replacement for data fit. |
| `RCIM_ML_Compensation` summary | The practical ML model depends on speed, torque, oil temperature, angular position, and direction-separated behavior. | Preserve causal operating variables and report `global`, `Fw`, and `Bw` separately. |
| Recovered RCIM harmonic workflow | The recovered paper workflow predicts selected harmonic amplitude and phase components. | Include harmonic-consistency constraints around the recovered harmonic set. |
| `Track 2` h0 diagnostics | `h0` is the correct mean-like channel, but measured `h0` magnitude alone does not explain model failures. | Include offset/mean-surface diagnostics, but do not encode `h0` as the only physical cause. |
| Wave 3 design | Hybrid structured models separate harmonic structure and learned residual correction. | Let the first PINN reuse the same inspectable harmonic and residual split where useful. |
| `MMT_TEModeling` equation reproduction, commit `3d4b9b720471aa3aca461e94a9e14f353637b153` | The repository now has explicit Python and MATLAB implementations of the MMT equation chain, including `f1`, `f2i`, `f3`, `f4i`, transfer coefficients, and whole-machine `RTE`. | Promote MMT equations from background context to the first Wave 4 sub-branch. |
| External gear-dynamics literature | Transmission error is commonly linked to time-varying mesh stiffness, loaded static TE, backlash, contact force, support flexibility, and dynamic mesh force. | Add exploratory Wave 4 branches for mesh-stiffness, loaded-TE, nonlinear-dynamics, and cycloid-contact formulations. |

## PINN Scope

The first Wave 4 PINN should remain a soft-constraint TE model, but the scope
is now broader than a generic harmonic PINN. The MMT equation-chain
reproduction gives the repository a concrete analytical model to test. The
limitation is that the available dataset still does not expose every
component-level error, contact-geometry value, or equivalent-linkage parameter
needed to use the MMT model as a fully observed forward solver for every
measured curve.

Therefore, Wave 4 should use a staged integration path:

- first as diagnostics and interpretable equation outputs;
- then as features or pseudo-physical residual labels;
- then as soft loss terms;
- then as a calibrated analytical baseline;
- only later as a stronger PINN forward model if the calibrated baseline is
  empirically useful.

The first PINN constraints that can be validated from the current TE
representation remain:

- periodic curve closure over the angular cycle;
- smoothness of TE as a function of angular position;
- harmonic reconstruction consistency;
- operating-condition smoothness over speed, torque, and temperature;
- direction-separated behavior;
- optional residual regularization when combined with a structured harmonic
  branch.

## Candidate Loss Terms

| Loss Term | Purpose | Boundary |
| --- | --- | --- |
| Data-fit loss | Preserve direct agreement with measured TE curves. | This remains the primary loss because physics constraints are incomplete. |
| Periodicity loss | Enforce curve closure and derivative consistency at angular wraparound. | Valid only for curve segments that represent a full compatible angular period. |
| Smoothness loss | Penalize unrealistic local oscillation in angular TE prediction. | Must not erase legitimate high-order harmonics such as `156`, `162`, and `240`. |
| Harmonic-consistency loss | Keep predicted curves consistent with selected harmonic amplitudes and phases. | The recovered harmonic set is a structured basis, not proof that all error lives there. |
| Condition-surface smoothness | Encourage nearby speed, torque, and temperature conditions to have compatible mean and shape behavior. | Must avoid leaking held-out target statistics or memorizing full operating-condition cells. |
| Direction-consistency diagnostic | Compare `Fw` and `Bw` behavior under the same formulation without forcing equality. | Directional models remain separate because the paper and repository treat them separately. |
| Residual regularization | Keep learned residuals small or smooth when a harmonic prior branch is present. | The residual must still be allowed to correct real non-harmonic or unmodeled behavior. |
| MMT equation residual | Penalize disagreement between predicted TE or predicted equivalent-error channels and the MMT reconstructed `RTE`. | Requires calibrated or predicted equivalent errors; should start as a weak term. |
| Mesh-stiffness consistency | Penalize curve behavior incompatible with periodic mesh stiffness or loaded static TE trends. | Requires an assumed or learned stiffness surface; not directly observed in the current dataset. |
| Backlash / dead-zone consistency | Allow asymmetric or piecewise behavior under direction changes and preload release. | Must not be used to justify non-causal target-mean leakage. |

## Wave 4 Sub-Branch Roadmap

| Branch | Working Name | Scope | Readiness |
| --- | --- | --- | --- |
| `Wave 4A` | `mmt_equation_diagnostic` | Run the MMT reproduction as an analytical diagnostic and compare its harmonic/offset signatures against Track 2 curves. | Ready as documentation and script-level diagnostic; not yet a training campaign. |
| `Wave 4B` | `mmt_feature_generator` | Calibrate or infer a small set of equivalent-error channels and use MMT intermediate terms as model features or residual labels. | Needs parameter inventory and leakage-safe calibration split. |
| `Wave 4C` | `mmt_soft_constraint_pinn` | Add weak MMT equation residuals to a curve or harmonic-plus-residual neural model. | Needs differentiable or batch-callable MMT layer and stable loss scaling. |
| `Wave 4D` | `mesh_stiffness_loaded_te_pinn` | Add time-varying mesh stiffness and loaded static TE consistency terms. | Exploratory; needs stiffness approximation or learned stiffness head. |
| `Wave 4E` | `backlash_preload_state_pinn` | Use piecewise/dead-zone or hysteresis-like constraints for preload release, backlash, and direction/state dependence. | Exploratory; relevant to `h0`/`h1` dispersion but needs causal state features. |
| `Wave 4F` | `cycloid_contact_force_pinn` | Use cycloid-pin contact, profile modification, contact-force, and loaded-TE relations as soft constraints. | Exploratory; requires cycloid geometry/contact assumptions. |
| `Wave 4G` | `planetary_mesh_force_lste_pinn` | Test mesh-force, loaded static TE, elastic support, and planetary branch interaction constraints. | Exploratory; useful if support/load-sharing effects align with observed harmonics. |

Detailed design reports:

- `doc/reports/analysis/wave4/Wave 4A MMT Equation Diagnostic Design.md`;
- `doc/reports/analysis/wave4/Wave 4B MMT Feature Generator Design.md`;
- `doc/reports/analysis/wave4/Wave 4C MMT Soft Constraint PINN Design.md`;
- `doc/reports/analysis/wave4/Wave 4D Mesh Stiffness Loaded TE PINN Design.md`;
- `doc/reports/analysis/wave4/Wave 4E Backlash Preload State PINN Design.md`;
- `doc/reports/analysis/wave4/Wave 4F Cycloid Contact Force PINN Design.md`;
- `doc/reports/analysis/wave4/Wave 4G Planetary Mesh Force LSTE PINN Design.md`.

## MMT Equation Integration Path

The MMT paper equations are now repository-owned through:

- `doc/reports/analysis/mmt_te_modeling/MMT TE Modeling Equation Extraction And Reimplementation Plan.md`;
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.py`;
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.m`.

The implemented chain includes:

- kinematic speed-ratio and angle equations;
- equivalent linkage angles and loop equations;
- error-transfer ratios `g1`, `g2`, `g3`, and `g4`;
- subsystem contributions `f1`, `f2i`, `f3`, and `f4i`;
- whole-machine `RTE` equations;
- prototype test-bench `RTE` definition.

The immediate Wave 4 use should be:

1. run the MMT reproduction as a diagnostic on synthetic and dataset-aligned
   angle grids;
2. inventory which MMT inputs are known, configurable, calibratable, or
   unavailable for repository curves;
3. calibrate a small equivalent-error vector on training conditions only;
4. compare calibrated analytical curves against Track 2 raw, centered, offset,
   amplitude, and phase metrics;
5. if useful, convert the analytical residual into a weak PINN loss or a
   structured feature generator.

The MMT chain should not be used as a hard equality constraint until the
contact geometry and equivalent-error inputs are either measured or calibrated
with a split that prevents condition-cell memorization.

## Embryonic Implementation Status

The first `Wave 4A` skeleton has now been materialized as implementation-ready
diagnostic scaffolding, but it remains explicitly not campaign-ready.

| Item | Status |
| --- | --- |
| Diagnostic adapter | `scripts/models/wave4_mmt_diagnostic_adapter.py` exposes `Wave4MMTDiagnosticAdapter`. |
| Config template | `config/training/wave4_embryonic_skeleton/wave4a_mmt_equation_diagnostic_template.yaml` records `implementation_ready` and `not_campaign_ready`. |
| Validator | `scripts/campaigns/wave_4/validate_wave4_embryonic_skeleton_package.py` checks metadata and MMT demonstration-summary generation. |
| Dry-run launcher | `scripts/campaigns/wave_4/run_wave4_embryonic_skeleton_checks.ps1` runs compile and validator checks only. |

## Wave 4A Diagnostic Status

The first `Wave 4A` diagnostic report has been generated from the
repository-owned MMT equation-chain demonstration.

| Item | Status |
| --- | --- |
| Report builder | `scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py`. |
| Markdown report | `doc/reports/analysis/wave4/mmt_equation_diagnostic/[2026-06-11]/wave4a_mmt_equation_diagnostic.md`. |
| Companion artifacts | `output/validation_checks/wave4_mmt_equation_diagnostic/2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic/`. |
| Demonstration mean | `-565.628931` arcsec. |
| Demonstration peak-to-peak | `525.201502` arcsec. |
| Dominant demonstration harmonic | harmonic `18`, amplitude `152.451356` arcsec. |
| Suspicious Track 2 harmonics checked | `0`, `1`, `156`, `162`, and `240`. |

The diagnostic confirms that the MMT chain is callable and auditable, but it
does not yet prove dataset causality. The result remains diagnostic-only until
leakage-safe dataset calibration is resolved.

## Wave 4A Parameter Inventory Status

The `Wave 4A` parameter inventory has now been generated as a non-campaign
artifact.

| Item | Status |
| --- | --- |
| Report builder | `scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.py`. |
| Markdown report | `doc/reports/analysis/wave4/mmt_parameter_inventory/[2026-06-11]/wave4a_mmt_parameter_inventory.md`. |
| Companion artifacts | `output/validation_checks/wave4_mmt_parameter_inventory/2026-06-11-20-29-51__wave4a_mmt_parameter_inventory/`. |
| Inventory rows | `11`. |
| Train-only calibratable groups | `5`. |
| High leakage-risk groups | `3`. |

The inventory separates safe geometry constants from dataset metadata,
train-only equivalent-error channels, blocked contact geometry, and target-only
measured TE. It confirms that MMT can continue as a diagnostic and can seed
`Wave 4B` feature design, but it should not become a calibrated analytical
baseline or `Wave 4C` loss until dataset-aligned calibration is leakage-safe.

Before Wave 4 can become campaign-ready, the project still needs a decision on
whether `Wave 4A` remains diagnostic-only or becomes feature/loss material,
`Track 2H` loss-policy evidence, Wave 3 smoke evidence, dataset-aligned MMT
calibration checks, and an approved campaign plan for the selected sub-branch.

## External Equation Families To Explore

| Family | Source Signal | Possible Wave 4 Use | Main Risk |
| --- | --- | --- | --- |
| Time-varying mesh stiffness | Gear mesh stiffness varies with tooth contact number and rotation angle. | Add a learned or Fourier stiffness head and penalize non-periodic stiffness/TE coupling. | Stiffness is not measured directly. |
| Loaded static transmission error | Loaded TE can drive mesh deformation and differs from unloaded TE. | Condition TE constraints on torque/load regime. | Requires careful separation from target-mean leakage. |
| Nonlinear dynamic TE with backlash | Gear dynamics literature models backlash, clearance, and periodic TE excitations. | Add dead-zone or piecewise residual branches for preload/direction state. | May overfit if history/state variables are unavailable. |
| Cycloid profile and contact-force equations | Cycloid-pin studies optimize modification coefficients for TE and contact force. | Test constraints around high-order fragile harmonics and torque-sensitive loaded TE. | Geometry/contact assumptions may not match the test rig. |
| Planetary mesh force and LSTE | Planetary gear studies link mesh stiffness, mesh force, elastic supports, and loaded static TE. | Add branch-interaction or load-sharing diagnostics if harmonics suggest planetary support effects. | RV reducer topology differs from simple planetary models. |

Reference sources reviewed for the external candidates:

- NASA NTRS nonlinear geared-system analysis, including backlash,
  time-varying mesh stiffness, and internal static transmission-error
  excitation:
  <https://ntrs.nasa.gov/api/citations/19900014416/downloads/19900014416.pdf>
- Brunel thesis on static and dynamic finite-element TE in spur gears,
  including mesh-stiffness variation as a TE/noise driver:
  <https://bura.brunel.ac.uk/bitstream/2438/5100/5/FullTextThesis.pdf>
- MDPI cycloid transmission-characteristics study using modification,
  contact force, and loaded transmission error:
  <https://www.mdpi.com/2075-1702/11/8/775>
- SAGE planetary-gear mesh-stiffness and loaded-static transmission-error
  study:
  <https://journals.sagepub.com/doi/10.1177/16878132221123469>
- ResearchGate abstract page for planetary time-varying mesh stiffness via
  potential-energy method:
  <https://www.researchgate.net/publication/264816423_Evaluating_the_Time-Varying_Mesh_Stiffness_of_a_Planetary_Gear_Set_Using_the_Potential_Energy_Method>
- NSF-hosted ASME hypoid gear mesh-stiffness and dynamic TE paper:
  <https://par.nsf.gov/servlets/purl/10659215>

## First PINN Candidate

The first runnable Wave 4 candidate should now be
`wave4_mmt_soft_constraint_pinn`, with
`wave4_soft_constraint_harmonic_pinn` retained as the fallback if MMT
calibration is not stable:

1. Use a causal neural predictor for TE curve or harmonic-plus-residual output.
2. Compute the ordinary curve data-fit loss.
3. Add periodicity and angular smoothness penalties on the predicted curve.
4. Add harmonic-consistency penalties on the recovered harmonic set:
   `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`.
5. Add weak MMT equation residual penalties when equivalent-error calibration
   or prediction is available.
6. Add optional condition-surface smoothness only when the split design proves
   it does not leak held-out target information.
7. Evaluate by official `Track 2` raw, offset, centered-shape, amplitude,
   phase, and visual diagnostics.

This candidate is intentionally narrow. It tests whether soft physics helps
before adding a full physics model or combining PINN losses with the final
multi-task / multi-head architecture.

## Relationship To Wave 3

| Wave 3 Concept | Wave 4 Extension |
| --- | --- |
| Harmonic prior residual | Add periodicity, smoothness, and harmonic-consistency losses to the structured reconstruction path. |
| Grouped harmonic heads | Apply stronger or different regularization to low-order offset terms, stable middle harmonics, and fragile high harmonics. |
| Conditioned residual surface | Add condition-surface smoothness or residual regularization without assuming exact repeatability. |
| Basis-constrained decoder | Treat fixed harmonic basis functions as an inspectable constraint surface for PINN penalties. |

## Evaluation Plan

Wave 4 candidates should be compared against:

- accepted `Track 2` leaders;
- completed `Track 2G` curve-aware candidates;
- completed `Track 2H` robust-loss candidates;
- approved Wave 3 hybrid structured candidates;
- `Wave 2B` and `Wave 2C` sequence/harmonic baselines.

Promotion must use the official `Track 2` curve-facing diagnostics rather than
scalar validation loss alone.

## Decision Gates

Wave 4 should proceed to campaign preparation only if a later approval gate
accepts these choices:

- start with `wave4_soft_constraint_harmonic_pinn`;
- promote `wave4_mmt_soft_constraint_pinn` to first candidate if the MMT
  diagnostic/calibration branch is numerically stable;
- treat physics terms as soft regularizers, not hard truth constraints;
- keep the ordinary data-fit loss primary;
- avoid condition-surface smoothness unless leakage checks are explicit;
- wait for `Track 2H` and Wave 3 evidence before selecting final loss weights
  for a larger integrated architecture.

## Non-Goals

- Do not modify the active `Track 2H` campaign.
- Do not treat the embryonic template or dry-run launcher as a real campaign
  package.
- Do not claim that a full analytical RV reducer PINN has been implemented.
- Do not treat external gear-pair or planetary equations as directly valid for
  the RV reducer without validation against repository curves.
- Do not enforce equality between `Fw` and `Bw` behavior.
- Do not use measured curve means, future TE samples, or held-out target
  statistics at inference time.
