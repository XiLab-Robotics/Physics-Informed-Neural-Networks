# Wave 5.2R Stage 10 Sparse And Symbolic Formulation Discovery Campaign Plan

## Overview

This bounded campaign identifies stable, compact condition laws for the Stage
5 complex harmonic coefficients. It evaluates whether predeclared sparse and
constrained-symbolic libraries improve the complete quadratic
Polynomial-Fourier control on the frozen polished-setpoint forward split.

The campaign is formulation discovery, not a claim that data-discovered terms
are governing physics.

## Approval And Scope

- Technical document:
  `doc/technical/2026-07/2026-07-29/2026-07-29-20-07-54_wave52r_stage10_sparse_and_symbolic_formulation_discovery.md`
- Approval source: user blanket approval for twenty-four hours.
- Approval recorded at: `2026-07-29T15:30:41+02:00`.
- Approval expiry: `2026-07-30T15:30:41+02:00`.
- Dataset: `polished_dataset`.
- Input mode: setpoints.
- Surface: `Fw`.
- Frozen split: `675 / 194 / 97`.
- Test access: one final evaluation after validation-time choices are frozen.
- Runtime target-derived inputs: zero.

## Scientific Inputs

- Stage 1 `W52R-T20`: SINDy-style sparse harmonic-condition library.
- Stage 1 `W52R-T21`: constrained symbolic residual search.
- Brunton, Proctor, and Kutz: sparse identification over a predeclared
  nonlinear library.
- Udrescu and Tegmark: separability, symmetry, and compositional structure as
  useful symbolic-search biases.
- Stage 5: canonical complex harmonic coefficient representation.
- Stage 9: H04 and K01 qualified research references.

## Candidate Matrix

| Queue | ID | Formulation | Fit or replay |
| ---: | --- | --- | --- |
| 1 | `D00` | frozen PF-A | replay |
| 2 | `D01` | frozen H04 | replay |
| 3 | `D02` | frozen Stage 9 K01 | replay |
| 4 | `Q00` | complete quadratic coefficient law | fit |
| 5 | `R00` | dense ridge complete library | fit |
| 6 | `S01` | sequential thresholded ridge | fit |
| 7 | `S02` | bootstrap stability-selected sparse refit | fit |
| 8 | `S03` | hierarchy-constrained stable sparse refit | fit |
| 9 | `Y01` | bounded separable symbolic-library refit | fit |
| 10 | `N01` | shuffled-label stability selection | fit |

## Predeclared Libraries

### Complete Quadratic Control

- `1`;
- normalized torque, speed, and temperature;
- their squares;
- all pairwise products.

### Extended Sparse Library

The quadratic control plus:

- cubic main effects;
- triple interaction;
- signed torque magnitude and speed magnitude terms;
- `log1p` condition magnitudes;
- bounded rational magnitudes `x / (1 + abs(x))`;
- squared-condition pair interactions;
- temperature-modulated torque and speed terms.

All term names, formulas, parent terms, and scaling rules are serialized before
the campaign fit.

### Constrained Symbolic Library

The extended library is reduced to unit-safe, bounded, and separable
compositions. Division by a learned or near-zero quantity, arbitrary powers,
trigonometric transforms of operating conditions, and exponentials are
excluded.

## Selection Protocol

1. Build coefficient targets and all scalers from training conditions only.
2. Fit each coefficient channel independently with shared term definitions.
3. Select ridge and threshold settings on validation coefficient and
   reconstructed-curve metrics.
4. Run `96` deterministic training bootstraps for stability candidates.
5. Retain terms with selection probability at least `0.75`, sign agreement at
   least `0.85`, and normalized median magnitude above the frozen threshold.
6. Enforce strong heredity in `S03`: an interaction requires its parent main
   effects.
7. Freeze the selected term set.
8. Refit coefficient values on train plus validation conditions.
9. Evaluate the test split once.

## Metrics

- raw curve MAE;
- mean / offset MAE;
- mean-centered shape MAE;
- circular derivative MAE;
- periodic closure error;
- retained harmonic amplitude and phase errors;
- per-curve MAE P95;
- active term count and maximum terms per coefficient;
- bootstrap selection probability;
- bootstrap sign agreement;
- coefficient validation and test MAE;
- shuffled-label specificity;
- deterministic replay parity;
- runtime target-derived input count.

## First-Screen Gate

A discovered formulation qualifies only if it:

- beats `Q00` on raw and centered-shape test MAE;
- preserves closure, amplitude, phase, and P95 within `1.02` times the better
  of `Q00` and frozen H04;
- uses at most `40%` of the dense library coefficient slots;
- satisfies the selection-probability and sign-agreement thresholds;
- beats `N01` on raw and coefficient error;
- has deterministic reconstruction and zero target-derived runtime inputs.

The report separately states whether a candidate beats H04 or K01. Those
comparisons do not replace the sparse-discovery gate.

## Artifacts

- candidate YAML files and campaign manifest;
- serialized term-library definition;
- bootstrap term-selection matrix;
- term stability and coefficient tables;
- leaderboard and exit-gate summary;
- reconstructed test predictions;
- explanatory and campaign-results reports;
- styled and validated PDF;
- backlog, ledger, master-summary, guide, and Sphinx synchronization.

## Launch Commands

Local preflight:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -PreflightOnly
```

Local run:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -Run
```

Remote preflight:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -Remote -PreflightOnly
```

Remote run:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -Remote -Run
```
