# Wave 4B MMT Feature Generator Design

## Purpose

`Wave 4B` tests whether MMT analytical terms are useful as causal features or
pseudo-physical residual labels for repository ML models. It comes after
`Wave 4A` and before any MMT equation residual is used inside a PINN loss.

## Physical Idea

The MMT equation chain separates whole-machine rotational transmission error
into interpretable subsystem terms:

- high-speed involute contribution `f1`;
- crankshaft input-path contribution `f2i`;
- cycloid-pin contribution `f3`;
- crankshaft output-path contribution `f4i`;
- transfer coefficients `g1`, `g2`, `g3`, and `g4`.

If these terms correlate with model residuals, they can become feature
channels or residual labels even when the full analytical predictor is not
accurate enough alone.

## Design

| Element | Design Choice |
| --- | --- |
| Candidate name | `wave4b_mmt_feature_generator` |
| Inputs | Track 2 causal operating variables, angle grid, geometry constants, and calibrated equivalent-error parameters from training conditions. |
| Feature outputs | MMT `RTE`, subsystem terms, low-speed/high-speed contribution summaries, harmonic amplitudes, and calibrated residual channels. |
| Target outputs | Existing TE curve target, optional residual target after subtracting MMT baseline, and optional grouped-harmonic residual targets. |
| First consumer | Wave 3 hybrid structured models or Wave 4C MMT soft-constraint PINN. |

## Feature Groups

| Group | Candidate Features |
| --- | --- |
| Global analytical curve | MMT predicted `RTE`, mean, peak-to-peak, and centered curve. |
| Subsystem terms | `f1`, average `f2i`, `f3`, average `f4i`, and transfer-weighted contributions. |
| Harmonic terms | MMT harmonic amplitudes and phases for `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`. |
| Residual terms | Measured-minus-MMT mean offset, centered residual, and high-order residual energy. |

## Implementation Outline

1. Reuse `Wave 4A` parameter inventory and calibration outputs.
2. Generate MMT feature tables for train/validation/test splits.
3. Verify that every feature is computable without target leakage at
   inference time.
4. Train a lightweight diagnostic model or join features into an existing
   Wave 3 design.
5. Evaluate whether features reduce Track 2 offset or fragile-harmonic errors.

## Leakage Boundaries

- Equivalent-error calibration must be trained only on training conditions.
- Residual labels may be used for training diagnostics, but residual values
  computed from validation targets must not be inference features.
- Condition-cell memorization is not acceptable as physical feature learning.

## Decision Gate

Promote to `Wave 4C` if MMT features improve at least one Track 2 diagnostic
surface without degrading centered-shape, amplitude, or phase behavior.
