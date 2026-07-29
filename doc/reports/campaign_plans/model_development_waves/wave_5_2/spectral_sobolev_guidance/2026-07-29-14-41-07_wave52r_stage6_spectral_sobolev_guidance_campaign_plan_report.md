# Wave 5.2R Stage 6 Spectral And Sobolev Guidance Campaign Plan

## Campaign Decision

Prepare one bounded matched-control campaign on `polished_dataset`, setpoint
inputs, and `Fw`. The campaign tests whether Stage 6 guidance adds predictive
value beyond the qualified Stage 5 H04 component.

This plan does not reopen MMT, change the accepted periodic GRU, or run the
heavy TE Curve Verification Pipeline.

## Approval

The user approved this campaign plan, its execution, closeout, PDF validation,
and commit at `2026-07-29T15:30:41+02:00`. The approval window expires at
`2026-07-30T15:30:41+02:00`.

## Frozen Evidence

- split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- accepted curves: `966`;
- train, validation, and test counts: `675`, `194`, and `97`;
- angular grid: `2048` uniform samples;
- analytical anchor: PF-A;
- qualified structured component: Stage 5 H04;
- Stage 5 H04 three-seed MAE:
  `0.00174908 +/- 0.00003982 deg`;
- accepted forward model-development reference:
  `polished_setpoints_periodic_gru_sequence_Fw`.

## First-Screen Matrix

| ID | Model | Guidance | Matched reference |
| --- | --- | --- | --- |
| C01 | bounded H04 core coefficient | curve only | Stage 6 base control |
| C02 | bounded H04 core coefficient | uniform complex spectrum | C01 |
| C03 | direct C04 core coefficient | uniform complex spectrum | C02 |
| C04 | direct data-selected coefficient | fragile spectrum | S02 |
| D01 | bounded H04 core coefficient | first Sobolev derivative | C01 |
| S02 | bounded H08 data-selected coefficient | fragile-band spectrum | C04 |
| DS01 | bounded H04 core coefficient | derivative plus spectrum | C02 |
| DS02 | bounded H08 data-selected coefficient | derivative plus fragile spectrum | C04 |
| CU01 | bounded H04 core coefficient | staged curve, spectrum, derivative curriculum | DS01 |
| FI01 | bounded H04 core coefficient | failure-informed angular weighting plus guidance | DS01 |
| FF00 | bounded PF-A coordinate residual | raw circular coordinate | FF01 |
| FF01 | bounded PF-A coordinate residual | frozen Fourier features | FF00 |
| SI00 | bounded PF-A coordinate residual | tanh angular basis | SI01 |
| SI01 | bounded PF-A coordinate residual | SIREN angular basis | SI00 |
| W01 | bounded H04 core coefficient | local Fourier-moment weak form | C01 |

The preflight may add one curvature ablation only if the training-only
second-derivative stability gate passes. Otherwise it records the arm as
blocked before training.

## Training Contract

- first-screen seed: `314159`;
- stability seeds: `271828` and `161803`;
- deterministic full-batch optimization;
- maximum `64` epochs with validation early stopping;
- one canonical full-curve reconstruction and evaluation surface;
- training-only feature scaling, derivative calibration, spectral weighting,
  weak-form basis, residual bounds, and failure weights;
- no measured or target-derived inference feature;
- immutable timestamped run directories.

## Loss Contract

The normalized primary objective is full-curve error. Candidate-specific
secondary terms are:

- circular first-derivative error in degrees per radian;
- normalized complex spectral error over declared harmonic bands;
- fixed local Fourier-moment error;
- bounded failure-informed angular reweighting;
- deterministic curriculum weights.

All active loss weights, normalized values, gradient norms, and validation
metrics must be persisted. The primary curve objective is never removed.

## Noise And Leakage Controls

- derivative window selection uses training curves only;
- `mode="wrap"` preserves the periodic boundary;
- target derivatives are labels only;
- spectral targets are labels only;
- no future sample is an inference input;
- unsupported high-frequency prediction energy is reported separately;
- second derivatives remain disabled if estimator sensitivity exceeds the
  predeclared threshold;
- failure weights are clipped and preserve a minimum effective sample size.

## Promotion Gate

The first-screen scalar winner is not promoted automatically.

The selected candidate must improve:

- derivative MAE and derivative correlation;
- retained harmonic amplitude and phase;
- P95 per-curve MAE;

while preserving within tolerance:

- raw MAE;
- centered MAE;
- offset;
- periodic closure;
- supported high-frequency energy.

It must also beat its matched control and repeat the decision across all three
seeds.

## Expected Artifacts

- campaign and queue YAML files;
- derivative calibration and sensitivity evidence;
- spectral-band and weak-form manifests;
- preflight validation summary;
- campaign leaderboard and explicit best-run artifacts;
- stability leaderboard;
- immutable checkpoints, histories, predictions, and metrics;
- Stage 6 Markdown results report;
- validated styled PDF and companion figures;
- synchronized operational and project-status documents.

## Launch Surfaces

The dedicated PowerShell launcher will support:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -Run

.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -Remote -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -Remote -Run
```

Normal closeout will not run the heavy TE Curve Verification Pipeline.
