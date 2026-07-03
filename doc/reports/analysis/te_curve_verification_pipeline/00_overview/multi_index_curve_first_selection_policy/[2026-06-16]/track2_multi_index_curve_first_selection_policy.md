# TE Curve Verification Pipeline Multi-Index Curve-First Selection Policy

## Purpose

This document is the canonical `TE Curve Verification Pipeline` selection
policy after the project shift from point-to-point scalar ranking to
curve-first model evaluation.
Scalar `MAE`, `RMSE`, and percentage error remain required operational
metrics, but they are no longer sufficient by themselves to promote or reject a
model family.

The practical target is transmission-error compensation over continuous held-out
TE curves. A model that follows curve shape, phase, amplitude, offset behavior,
and worst-case operating regimes well may be more useful than a model that only
improves one pointwise scalar. Conversely, a model with attractive centered
shape cannot be promoted if raw error, offset, robustness, or deployment
constraints are unacceptable.

## Scope

This policy applies to all official `TE Curve Verification Pipeline`
model-verification reports, candidate refreshes, closeout ledgers, backlog
updates, and future reranking reports for:

- paper-reference and `RCIM Model-Bank Reproduction` banks;
- `Wave 1` exported model families;
- Waves `2.1` through `2.3` temporal families;
- `CVP 1.1` through `CVP 1.5` verification modules;
- Waves `3.1` through `4.4` modeling branches;
- `Wave 5.1` and later structured or physics-informed branches.

The policy does not retroactively change historical run artifacts. Historical
reports remain valid snapshots of the metrics and decisions available when they
were generated. New official decisions must use this policy.

## Evaluation Boundary

Runtime inference may use only deployable information:

- current point-level operating state;
- explicitly supported short causal history;
- causal derived features available before or at the current sample.

Offline validation may use complete held-out TE curves to measure performance,
diagnose failure modes, select representative visual evidence, and decide
whether a family is promoted, rejected, or retained as an exploratory baseline.

Mean-centering, full-curve residual summaries, harmonic decomposition of the
truth curve, and post-prediction diagnostic scores are validation tools. They
are not deployable runtime corrections unless later reformulated as causal
predictors.

## Official Selection Axes

Every future official `TE Curve Verification Pipeline` refresh should report the strongest candidate
for each axis where the required artifacts are available:

| Axis | Primary Evidence | Meaning |
| --- | --- | --- |
| Raw error | curve `MAE`, curve `RMSE`, mean percentage error | Direct operating error against measured TE. |
| Mean-centered shape | centered curve `MAE` / `RMSE`, centered overlays | Shape tracking after separating vertical offset. |
| Offset and continuity | mean offset, absolute offset, closure mismatch, stitched-boundary mismatch | Whether the curve level and revolution boundaries are stable. |
| Harmonic / phase fidelity | harmonic amplitude error, wrapped phase error, peak-to-peak error | Whether dominant TE structure is reproduced. |
| Robustness | P95 error, worst-condition error, condition spread | Whether the candidate avoids fragile operating regimes. |
| Visual evidence | collage and overlay report inspection | Whether tables agree with real plotted curve behavior. |
| Deployment readiness | model kind, export path, causal input contract, runtime complexity | Whether the candidate can plausibly become a practical compensator. |

## Per-Surface Winners

`TE Curve Verification Pipeline` remains direction-parallel. Each official refresh must preserve
separate `global`, `Fw`, and `Bw` selection surfaces.

For each surface, official reporting should expose:

| Winner Type | Required Meaning |
| --- | --- |
| `best_raw_error` | Lowest raw operating-error candidate on the valid direction surface. |
| `best_shape_fidelity` | Strongest centered-shape, amplitude, and phase behavior. |
| `best_offset_behavior` | Strongest offset, closure, and low-frequency behavior. |
| `best_robustness` | Strongest P95 / worst-case operating-regime behavior. |
| `recommended_candidate` | Final human-readable recommendation after multi-index scoring, visual review, and veto checks. |

A single model may win several axes, but the report must not hide meaningful
tradeoffs. If one model is best by raw error and another is best by shape, both
must remain visible.

## Composite Ranking Policy

Composite scores must be transparent and normalized. Metrics with different
physical units must not be added directly as raw values unless a report clearly
states that the score is exploratory.

The preferred official scoring policy is:

1. Compute each metric on the candidate's valid direction surface.
2. Normalize each metric within the compared candidate set using rank,
   percentile, or another stable bounded transformation.
3. Group normalized metrics into interpretable blocks.
4. Compute one composite score per candidate and surface.
5. Report the block scores beside the final recommendation.

The default block weights for the next implementation pass are:

| Block | Weight | Included Evidence |
| --- | ---: | --- |
| Shape and harmonic fidelity | 35% | centered shape, peak-to-peak, harmonic amplitude, harmonic phase |
| Raw operating error | 20% | curve `MAE`, curve `RMSE`, mean percentage error |
| Offset and continuity | 20% | mean offset, absolute offset, closure, boundary behavior |
| Robustness | 15% | P95, worst-condition, condition spread |
| Deployment readiness | 10% | causal inputs, exportability, runtime complexity, inspectability |

Reports may adjust weights only if the change is documented in the report and
the machine-readable artifact records the active policy.

## Veto Conditions

The recommended candidate for a surface must be rejected or demoted to
exploratory status when any of these conditions apply:

- invalid direction scope or missing direction-specific evidence;
- extreme raw error despite good centered shape;
- unstable P95 or worst-condition behavior;
- severe offset or closure failure that would make compensation unsafe;
- missing or broken visual evidence for the candidate group;
- known runtime leakage, future-curve input use, or undeployable inference
  contract;
- missing registry provenance or model artifact required for reproducibility.

## Required Report Outputs

Every future official `TE Curve Verification Pipeline` refresh should produce or reference:

- the raw directional matrix;
- the multi-index ranking table;
- one per-surface winner table for `global`, `Fw`, and `Bw`;
- the visual collage report;
- the overlay or multi-model curve comparison report;
- mean-centered or offset diagnostics when they are relevant to the decision;
- machine-readable CSV/YAML artifacts recording metric values, score blocks,
  weights, veto flags, and final recommendation labels.

The final decision wording must explicitly state whether the accepted baseline
changed. If no model is promoted, the report must still state which candidates
are best by raw error, shape fidelity, offset behavior, and robustness.

## Implementation Status

As of `2026-06-16`, the repository already contains the ingredients for this
policy:

- `CVP 1.1` curve-first reranking over matrix-level curve metrics;
- `CVP 1.2` curve-payload diagnostics for harmonic, derivative, smoothness,
  closure, and peak-to-peak behavior;
- mean-centered collage diagnostics;
- `CVP 1.4` mean-offset full-matrix audit;
- `CVP 1.5` offset-predictability feasibility;
- visual collage and overlay report families.

The next implementation step is to consolidate those ingredients into a
complete multi-index reranking pass over the current official `TE Curve Verification Pipeline`
candidate set, including `Wave 1`, `Wave 2.1`, `CVP 1.1` through `CVP 1.5` and Waves `3.1` through `4.4`,
and `Wave 5.1`.
