# Wave 5.2A MMT Equation Diagnostic Design

## Purpose

`Wave 5.2A` turns the repository-owned `MMT_TEModeling` equation reproduction
into a diagnostic tool for TE Curve Verification Pipeline curves. It does not train a model. Its goal
is to test whether the analytical equation chain can explain offset,
harmonic, or condition-regime patterns before it is used as a feature
generator or PINN loss.

## Source Boundary

The primary implementation source is the repository MMT extraction and
reproduction package introduced by commit
`3d4b9b720471aa3aca461e94a9e14f353637b153`:

- `doc/reports/analysis/te_modeling/analytical_mmt/MMT TE Modeling Equation Extraction And Reimplementation Plan.md`;
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.py`;
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.m`.

The current reproduction implements the analytical chain but still uses a
placeholder contact sweep for the demo. Therefore, this branch is diagnostic
until reducer-specific contact geometry and equivalent-error inputs are
available or calibrated.

## Design

| Element | Design Choice |
| --- | --- |
| Candidate name | `wave4a_mmt_equation_diagnostic` |
| Inputs | TE Curve Verification Pipeline angle grid, direction, speed, torque, temperature, reducer geometry assumptions, and candidate equivalent-error vectors. |
| Outputs | MMT predicted `RTE`, `f1`, `f2i`, `f3`, `f4i`, harmonic summary, mean offset, and residual to measured TE. |
| Metrics | Raw curve error, centered-shape error, signed mean offset, harmonic amplitude/phase error, and condition-stratified residuals. |
| Comparison targets | Accepted curve-verified leaders, Wave 3.3, Wave 4 series, Wave 2.2, Wave 2.3, and Wave 5.1 designs. |

## Implementation Outline

1. Run the existing MMT reproduction smoke check.
2. Build a parameter-inventory table for every required MMT input.
3. Create a dataset-aligned angle-grid adapter.
4. Evaluate fixed geometry and simple equivalent-error vectors.
5. Export per-curve MMT diagnostics and TE Curve Verification Pipeline metric joins.
6. Decide whether the MMT terms are useful as diagnostics, features, losses,
   calibrated baselines, or not useful.

Current implementation state:

- steps `1` and `2` have generated real diagnostic and parameter-inventory
  artifacts;
- the parameter inventory report is
  `doc/reports/analysis/model_development_waves/wave_4/mmt_parameter_inventory/[2026-06-11]/wave4a_mmt_parameter_inventory.md`;
- `Wave 5.2A` remains not campaign-ready because dataset-aligned calibration,
  contact-geometry reconstruction, and leakage-safe equivalent-error fitting
  are still open.

## Leakage Boundaries

- Do not fit equivalent-error parameters on the same condition cells used for
  validation.
- Do not use measured curve means as inference inputs.
- Do not claim physical causality for `h0` or high harmonics unless the MMT
  residual analysis supports it.

## Decision Gate

Promote to `Wave 5.2B` only if at least one MMT intermediate term or calibrated
analytical residual aligns with TE Curve Verification Pipeline offset, harmonic, or condition-regime
failure modes.
