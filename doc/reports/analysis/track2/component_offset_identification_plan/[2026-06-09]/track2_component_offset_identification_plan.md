# Track 2 Component Offset Identification Plan

## Purpose

This analysis plan records the next separate diagnostic branch for the
`Track 2` curve-offset problem. The current evidence shows that vertical
curve offset is a major contributor to raw TE-curve prediction error, but it
does not yet identify one confirmed source.

`a_0` / `Component 0` is a priority suspect because it is the dominant
mean-like component and can strongly affect the reconstructed TE curve. The
branch must still verify whether the observed offset is mainly caused by
`a_0`, by several harmonics/components together, by condition-dependent model
error, or by experimental repeatability limits.

## Current Evidence

| Evidence | Current Interpretation | Boundary |
| --- | --- | --- |
| Mean-centering strongly improves selected candidates. | Curve mean / `DC` offset is a real diagnostic symptom. | Mean-centering is not a runtime correction because it uses target-curve information unavailable during deployment. |
| `Track 2D` labels many candidates as `offset` or mixed offset cases. | Offset must stay separate from centered-shape, amplitude, and phase diagnostics. | The existing full-matrix audit does not prove that `a_0` alone caused the offset. |
| `Track 2E` finds `direction_torque` as the strongest conservative causal grouping. | Offset has an operating-condition signal. | Full operating-condition grouping can overstate deployable predictability when it collapses to one curve. |
| Colleague feedback reports possible `Component 0` repeatability variation. | Experimental variability may affect the target itself, especially preload or state-dependent initialization. | The reported variation must be treated as external evidence until matched against repository data or imported repeat measurements. |
| `Track 2F`, `Track 2F-bis`, and `Track 2G` test offset-aware and curve-aware branches. | Offset-aware modeling helps in some branches but has not closed the full curve-following gap. | Further training should wait for the component-identification result unless explicitly approved as a separate branch. |
| Measured h0 diagnostic is complete. | Harmonic zero / `h0` is the largest average measured component and the correct mean-like channel to inspect. | This does not prove that `h0` is the only source of model offset failures. |
| `Track 2D` h0/error cross-check is complete. | Large absolute measured `h0` does not reliably identify the cases where models have the largest mean-offset errors. | Filtering or reweighting high-`h0` curves alone is not a sufficient plan. |
| Predicted-mean h0 surface diagnostic is complete. | The actionable symptom is model-side mean-surface bias or compression against measured `h0`. | The diagnostic does not yet select the best modeling intervention. |

## Analysis Questions

1. Is the curve mean / `DC` offset numerically aligned with experimental
   `a_0` / `Component 0`, or only correlated with it?
2. Do high-offset curves show a dominant `a_0` discrepancy, or do other
   harmonics/components contribute materially?
3. Are `a_0` outliers structured by direction, torque, speed, oil temperature,
   or combinations of these conditions?
4. Are repeated operating points available, and if so, does repeatability
   variance explain part of the apparent model error?
5. Does the answer differ for `global`, `Fw`, and `Bw` surfaces?

## Planned Diagnostics

| Diagnostic | Output | Decision Value |
| --- | --- | --- |
| Experimental `a_0` surfaces | `a_0` over speed and torque, split by oil temperature and direction | Shows whether `a_0` follows a stable physical trend or contains isolated outliers. |
| Curve-mean surfaces | Measured TE mean over speed and torque, split by oil temperature and direction | Checks whether the curve-offset symptom follows the same pattern as `a_0`. |
| Component contribution table | Per-component contribution to curve offset or reconstruction residual | Separates `a_0` dominance from multi-component offset behavior. |
| Outlier map | Operating-condition rows with large `a_0`, curve mean, or residual mismatch | Identifies whether filtering or robust aggregation is justified. |
| Repeatability check | Per-condition variance for repeated experiments, if available | Tests whether the target mean is deterministic enough for direct regression. |
| Model-family comparison | Component-level comparison for available polynomial, `ONNX`, `ET`, `SVR`, and repository candidates | Confirms whether the issue is family-specific or common to the target data. |

## Prepared Entry Point

The first input-table preparation script is available at:

- `scripts/reports/analysis/build_track2_component_offset_identification_inputs.py`

Smoke-test command:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_component_offset_identification_inputs.py --max-files 2 --run-id 2026-06-09-18-22-15__track2_component_offset_identification_inputs_smoke --skip-report
```

Full input-table command:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_component_offset_identification_inputs.py
```

The script prepares:

- `track2_component_offset_per_curve_components.csv`;
- `track2_component_offset_condition_summary.csv`;
- `track2_component_offset_identification_inputs_summary.yaml`;
- a lightweight Markdown input report unless `--skip-report` is set.

The script computes measured curve mean / harmonic `0` proxy plus selected
harmonic coefficients for orders `0`, `1`, `3`, `39`, `40`, `78`, `81`,
`156`, `162`, and `240`. These tables are inputs for the later surface plots
and outlier analysis; they do not prove that `a_0` is the confirmed cause.

## Documentation Corrections To Defer Until Evidence

- Do not state that `a_0` / `Component 0` is the confirmed cause of the
  Track 2 curve offset.
- Do not rewrite `Track 2D` or `Track 2E` conclusions as component-level
  conclusions until component diagnostics are generated.
- After the diagnostic, update the backlog and Track 2 reports with one of
  these outcomes:
  - `a_0`-dominant offset;
  - multi-component offset;
  - condition/regime-dependent offset;
  - experimental repeatability-limited target;
  - mixed cause requiring separate shape, amplitude, phase, and offset
    treatment.

## Next Decision Gate

This diagnostic should run in parallel with, but separate from, the operator
workflow that closes or refreshes `Track 2G`. Its result should decide whether
the next approved step is:

- a `Track 2H` dispersion-aware probe stage with robust losses, quantile or
  probabilistic regression, mixture-density heads, and latent-state /
  hysteresis-aware models;
- `Wave 3` hybrid structured models that separate stable middle harmonics from
  fragile low-order and high-order components;
- `Wave 4` first-PINN formulation to test soft physics, periodicity,
  smoothness, harmonic-consistency, and operating-condition constraints;
- or a later integrated multi-task / multi-head architecture after the smaller
  probes identify which mechanisms are worth combining.
