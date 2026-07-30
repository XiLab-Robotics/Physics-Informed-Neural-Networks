# Wave 5.2R Full-Candidate TE Curve Verification Decision

## Decision Summary

The bounded forward-only `TE Curve Verification Pipeline` refresh evaluated
all `98` eligible candidates on the same `97` held-out
`polished_dataset + setpoints + Fw` curves.

The official direction-parallel decision is:

- `wave52r_stage9_k01` becomes the verified offline temporal-lane leader;
- `wave52r_stage5_h08_seed_314159` becomes the verified offline
  non-temporal balanced leader;
- `wave52r_stage12_f01` remains visible as the strongest centered-shape
  specialist;
- `wave52r_stage12_s01` remains visible as the strongest harmonic-amplitude
  and phase specialist in the diagnostic shortlist;
- the accepted periodic GRU and periodic harmonic MLP remain the deployable
  reference models until the new lane leaders pass export, parity, runtime,
  and PLC-facing acceptance checks.

This is not a backward or global decision. No `Bw` or `global` result is
inferred from forward-only checkpoints.

## Evaluation Scope

| Item | Value |
| --- | --- |
| Dataset | `polished_dataset` |
| Input contract | setpoints |
| Surface | `Fw` |
| Held-out curves | 97 |
| Matrix candidates | 98 |
| Temporal candidates | 18 |
| Non-temporal candidates | 79 |
| Analytical anchors | 1 |
| Full-payload diagnostic shortlist | 10 |
| Exact duplicate prediction groups | 3 |

The complete inventory also records 27 calibration-only, replay, or synthetic
artifacts that are not distinct real-data TE predictors.

## Curve-First Leaders

### Temporal Lane

| Axis | Leader | Evidence |
| --- | --- | --- |
| Raw error | `wave52r_stage9_k01` | Mean MPE `2.716282%`; mean curve MAE `0.001374 deg` |
| Centered shape | `wave52r_stage12_f01` | Centered curve MAE `0.001147 deg` |
| Offset | `wave52r_stage9_k01` | Mean absolute curve-mean error `0.000496 deg` |
| Harmonic amplitude | `wave52r_stage12_s01` | Mean amplitude error `5.702734%` |
| Harmonic phase | `wave52r_stage12_s01` | Mean phase error `3.166801 deg` |
| Robust P95 | `wave52r_stage12_f01` | P95 MPE `6.554012%` |
| Balanced recommendation | `wave52r_stage9_k01` | Best raw, offset, and full diagnostic score |

`K01` improves the accepted periodic GRU reference from `3.278427%` to
`2.716282%` mean MPE, a relative reduction of approximately `17.15%`.
Its centered curve MAE also improves from `0.001382 deg` to `0.001230 deg`,
and its mean harmonic amplitude and phase errors are materially lower.

`F01` has the best centered-shape and P95 evidence, but its worst-condition MPE
is `14.230071%`, above the `12.059574%` recorded by `K01`. It therefore remains
a specialist rather than the balanced temporal recommendation.

### Non-Temporal Lane

| Axis | Leader | Evidence |
| --- | --- | --- |
| Raw error | `wave52r_stage10_r00` | Mean MPE `3.422123%`; mean curve MAE `0.001658 deg` |
| Robust P95 | `wave52r_stage10_s01` | P95 MPE `6.751695%`; worst MPE `11.301458%` |
| Centered shape in shortlist | `wave52r_stage5_h04_seed_314159` | Centered curve MAE `0.001357 deg` |
| Harmonic and phase balance | `wave52r_stage5_h08_seed_314159` | Amplitude `10.375270%`; phase `4.087762 deg` |
| Balanced recommendation | `wave52r_stage5_h08_seed_314159` | Best multi-index compromise without Stage 10 harmonic collapse |

The accepted periodic harmonic MLP remains slightly better than `H08` by raw
mean MPE, `3.438600%` versus `3.483289%`. However, `H08` improves centered
curve MAE from `0.001390 deg` to `0.001364 deg`, harmonic amplitude error from
`14.751961%` to `10.375270%`, and phase error from `10.572248 deg` to
`4.087762 deg`.

Stage 10 `R00` and `S01` are raw and robustness leaders, but their mean
harmonic amplitude errors exceed `34%` and their mean phase errors exceed
`31 deg`. The multi-index policy therefore vetoes them as balanced
recommendations despite their attractive scalar error.

H04 remains an important structured grey-box result, but it is not the
non-temporal lane leader in this expanded comparison. H08 has better raw error
and materially stronger harmonic and phase fidelity.

## Cross-Lane Interpretation

The temporal road remains strongest on this forward surface. `K01` leads
`H08` in raw error, centered shape, offset, harmonic amplitude, harmonic phase,
and the combined curve-payload diagnostic score.

The two-road strategy remains useful:

- advance `K01` as the primary temporal export and runtime-validation target;
- advance `H08` as the primary inspectable non-temporal research target;
- retain `F01` and `S01` as temporal specialists for future multi-head or
  constrained optimization work;
- retain the accepted GRU and harmonic MLP as operational fallbacks until the
  new leaders pass deployment acceptance.

## Deployment Decision

The offline lane-leader status changes, but the deployment baseline does not
change automatically.

`K01` and `H08` currently rely on reproducible training or prediction
artifacts and passed the forward curve-verification checks. Promotion into the
accepted deployable model set requires:

1. a frozen standalone export;
2. Python-to-export numerical parity;
3. bounded runtime and memory evidence;
4. causal full-curve replay without hidden future information;
5. TwinCAT or PLC-facing integration checks where applicable.

Until those gates pass, the periodic GRU and periodic harmonic MLP remain the
accepted deployable references.

## Evidence

- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-07-30-10-45-46__wave52r_full_candidate_parallel_temporal_non_temporal_wave52r_full_candidate_parallel_temporal_non_temporal/validation_summary.yaml`;
- curve-first ranking:
  `output/validation_checks/wave52r_full_candidate_track2_curve_first_reranking/2026-07-30-11-09-17__track2b_curve_first_reranking/`;
- curve-payload diagnostics:
  `output/validation_checks/wave52r_full_candidate_track2_curve_payload_diagnostics/2026-07-30-11-00-18__track2c_curve_payload_diagnostics/`;
- candidate collage:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/wave52r_full_candidate_best_model_collage_report/[2026-07-30]/`;
- finalist overlay:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/wave52r_full_candidate_multi_model_curve_comparison_report/[2026-07-30]/`.

## Final Status

The Wave 5.2R full-candidate forward verification is closed.

- Temporal offline lane leader: `wave52r_stage9_k01`.
- Non-temporal offline balanced leader:
  `wave52r_stage5_h08_seed_314159`.
- Accepted deployment baselines: unchanged pending export and runtime gates.
- Backward and global surfaces: unchanged and outside this verification scope.
