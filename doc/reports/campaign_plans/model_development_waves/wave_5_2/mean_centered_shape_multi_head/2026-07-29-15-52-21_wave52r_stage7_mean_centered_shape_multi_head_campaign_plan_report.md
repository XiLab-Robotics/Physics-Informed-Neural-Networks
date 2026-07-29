# Wave 5.2R Stage 7 Mean And Centered-Shape Multi-Head Campaign Plan

## Campaign Decision

Execute one matched mean/shape decomposition screen on `polished_dataset`,
setpoint inputs, and `Fw`. The campaign tests whether an explicit offset head
and exactly centered periodic-shape head resolve the competition observed in
Stage 6.

This plan does not reopen MMT, alter the accepted periodic GRU, or execute the
heavy TE Curve Verification Pipeline.

## Approval

The user approved this campaign, execution, closeout, PDF validation, and
commit within the window from `2026-07-29T15:30:41+02:00` through
`2026-07-30T15:30:41+02:00`.

## Frozen Evidence

- split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- accepted curves: `966`;
- train, validation, and test counts: `675`, `194`, and `97`;
- angular grid: `2048` uniform samples;
- analytical anchor: PF-A;
- qualified structured component: Stage 5 H04;
- Stage 6 decision: no promoted candidate;
- accepted forward model-development reference:
  `polished_setpoints_periodic_gru_sequence_Fw`.

## First-Screen Matrix

| ID | Architecture | Mean path | Shape path | Training mode |
| --- | --- | --- | --- | --- |
| C01 | monolithic H04 | shared output | shared output | joint |
| S01 | fully shared | separate head | separate head | joint |
| P01 | partially shared | private branch | private branch | joint |
| I01 | independent | independent network | independent network | joint |
| G01 | fully shared | separate head | separate head | projected conflict gradients |
| A01 | analytical mean | frozen PF-A | learned centered shape | joint |
| A02 | analytical shape | learned mean | frozen PF-A shape | joint |

The frozen Stage 5 H04 checkpoint is evaluated as the external baseline and is
not counted as a new training run.

## Training Contract

- first-screen seed: `314159`;
- conditional stability seeds: `271828` and `161803`;
- deterministic full-batch optimization;
- maximum `64` epochs with validation early stopping;
- normalized full-curve, mean, and centered-shape objectives;
- one canonical full-resolution evaluation surface;
- immutable timestamped run directories;
- exact component outputs and parameter counts persisted.

## Loss And Gradient Contract

Every candidate optimizes a primary full-curve loss plus named mean and
centered-shape losses. The gradient-conflict candidate:

- measures the mean-versus-shape cosine over shared parameters;
- records negative-conflict frequency;
- projects only conflicting mean and shape gradients;
- retains the full-curve gradient;
- never changes held-out metrics or target definitions.

## Leakage And Structural Controls

- mean and centered-shape targets derive from training labels only;
- no target-derived value becomes an inference input;
- all feature scaling and correction bounds remain training-only;
- the centered shape must have cycle mean below `1e-7 deg`;
- reconstruction identity error must remain below `1e-7 deg`;
- periodicity remains exact through the frozen Fourier basis.

## Promotion Gate

A shared or partially shared model advances only if it:

1. preserves raw MAE within `1%` of frozen H04;
2. improves both mean/offset and centered-shape MAE by at least `0.5%`;
3. preserves derivative, closure, amplitude, phase, and P95 metrics;
4. beats I01 on the declared composite score, or matches within `0.5%` using
   no more than `80%` of I01 parameters;
5. passes component invariants;
6. repeats across three seeds.

If no candidate passes, the campaign closes as a valid negative result and
H04 remains the qualified component for Stage 8.

## Exact Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -Run

.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -Remote -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -Remote -Run
```
