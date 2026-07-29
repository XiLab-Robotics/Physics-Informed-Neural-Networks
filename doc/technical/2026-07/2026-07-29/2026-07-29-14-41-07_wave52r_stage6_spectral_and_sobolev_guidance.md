# Wave 5.2R Stage 6 Spectral And Sobolev Guidance

## Overview

This project implements Stage 6 of the polished-setpoint forward
physics-guided PINN reassessment. It starts from the qualified Stage 5 H04
component and tests whether derivative-domain, complex-spectral, curriculum,
failure-informed, coordinate-network, or weak-form guidance produces
incremental held-out value.

The scope remains restricted to:

- `polished_dataset`;
- setpoint inputs;
- the `Fw` surface;
- the immutable split signature
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- the common uniform `2048`-point angular grid;
- causal inference inputs only.

The user approved this document and all required Wave 5.2R work for the
twenty-four-hour window from `2026-07-29T15:30:41+02:00` through
`2026-07-30T15:30:41+02:00`. No subagent is planned.

## Technical Approach

Stage 6 will use one bounded matched-screen design.

The primary baseline is Stage 5 H04: a deep condition network that predicts
bounded corrections to the nine core PF-A complex coefficients. Stage 6 will
compare it with:

- curve-only and uniform complex-coefficient controls;
- a direct-coefficient C04 control without the PF-A anchor;
- first-derivative Sobolev supervision;
- core and fragile-band complex spectral supervision;
- combined derivative and spectral objectives;
- a staged low-to-high frequency curriculum;
- training-only failure-informed angular weighting;
- bounded Fourier-feature and raw-angle coordinate residual branches;
- bounded SIREN and parameter-matched tanh coordinate residual branches;
- fixed local Fourier-moment weak-form supervision.

Every model produces a complete `2048`-point curve. Coordinate models use a
low-rank condition-by-angle factorization so the full curve remains tractable
and inspectable.

Derivative targets will be generated only from training labels. A circular
Savitzky-Golay estimator will use:

- `mode="wrap"` for the periodic boundary;
- `delta = 2*pi/2048` for derivative units in degrees per radian;
- a training-only window sensitivity screen;
- an analytical harmonic reconstruction oracle for window selection.

SciPy documents that `deriv` selects the derivative order, `delta` supplies the
sample spacing when differentiating, and `mode="wrap"` extends the signal with
samples from the opposite edge. These semantics are frozen in the Stage 6
preflight evidence.

Second-derivative guidance will remain disabled unless its training-only
window-sensitivity gate passes. Spectral targets and derivative targets are
training labels, never inference inputs.

## Involved Components

- Stage 5 model and representation:
  `scripts/models/complex_harmonic_coefficient_residual_network.py`
- Stage 5 campaign utilities:
  `scripts/campaigns/wave_5_2/run_wave52r_stage5_complex_harmonic_coefficient_residuals.py`
- Stage 6 guided model:
  `scripts/models/spectral_sobolev_guided_residual_network.py`
- Stage 6 campaign:
  `scripts/campaigns/wave_5_2/run_wave52r_stage6_spectral_sobolev_guidance.py`
- Stage 6 launcher:
  `scripts/campaigns/wave_5_2/run_wave52r_stage6_spectral_sobolev_guidance.ps1`
- Stage 6 closeout builder:
  `scripts/reports/closeout/wave_5_2/build_stage6_spectral_sobolev_closeout.py`
- campaign configuration:
  `config/training/spectral_sobolev_guidance/`
- analysis evidence:
  `output/analysis/wave_5_2r/stage6_spectral_sobolev_guidance/`
- immutable training runs:
  `output/training_runs/spectral_sobolev_guidance/`
- campaign package:
  `output/training_campaigns/`
- persistent campaign state:
  `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Freeze the Stage 5 H04 checkpoint, coefficient contract, and canonical
   train, validation, and test curves.
2. Calibrate the circular first-derivative estimator using only training curves
   and a training-derived analytical harmonic oracle.
3. Measure second-derivative sensitivity and activate no curvature loss unless
   its predeclared stability threshold passes.
4. Build fixed complex-spectral bands, local weak-form test functions, and
   failure-informed angular weights from training data only.
5. Implement bounded coefficient and low-rank coordinate residual models.
6. Generate the matched candidate matrix, campaign YAML, and queue entries.
7. Validate shapes, gradients, exact zero-correction PF-A replay, circular
   derivative parity, spectral parity, bounds, and absence of target leakage.
8. Execute the first-screen campaign with one frozen seed.
9. Select a candidate only through the complete curve-first gate, then execute
   two additional seeds for that candidate and its matched control.
10. Publish campaign leaderboards, explicit winner artifacts, a Markdown
    results report, a styled PDF, and visual validation evidence.
11. Synchronize the roadmap, live backlog, master summaries, status ledger,
    usage guide, Sphinx portal, and active campaign state.
12. Run Markdown, Python, PowerShell, Sphinx, PDF, file-size, staged-pack, and
    Git diff checks before the Stage 6 commit.

## Exit Decision

A Stage 6 formulation advances only if it:

1. improves first-derivative error and correlation;
2. improves retained harmonic amplitude and phase;
3. improves or matches per-curve P95 robustness;
4. does not materially degrade raw MAE, centered MAE, or offset;
5. beats its parameter-matched control;
6. does not amplify unsupported high-frequency energy;
7. remains bounded across the full forward support;
8. passes the same decision across three seeds.

If no formulation satisfies all gates, Stage 6 closes as a valid negative
result and H04 remains the qualified component entering Stage 7.
