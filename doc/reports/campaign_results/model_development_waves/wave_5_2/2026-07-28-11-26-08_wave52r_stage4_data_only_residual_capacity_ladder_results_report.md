# Wave 5.2R Stage 4 Data-Only Residual Capacity Ladder Results

## Executive Summary

Wave 5.2R Stage 4 is complete as a valid negative result.

The campaign trained all `18 / 18` planned polished-dataset, setpoint-only,
forward-direction runs without a training failure. Two hybrids appeared to
beat their parameter-matched data-only controls on the trainer's scalar test
surface:

- `H02` improved test MAE by about `8.2%` relative to `C02`;
- `H08` improved test MAE by about `12.6%` relative to `C06` and was the
  campaign's scalar winner at `0.001454936 deg`.

Neither candidate survived the predeclared curve-first and cancellation gates.
On the canonical uniformly resampled supported-core curves, every primary
hybrid failed at least one required comparison against both the frozen causal
`PF-A` anchor and its capacity-matched direct control. No residual
architecture is promoted and no stability-repeat campaign is required.

The result is scientifically useful. It demonstrates that a residual network
can obtain an attractive point-sampled MAE by learning a large correction
that cancels the analytical anchor. That behavior is not evidence that the
anchor helped the network. Stage 5 must therefore train and evaluate in the
same canonical complex-coefficient and full-curve representation instead of
relying on the Stage 4 point-sampled objective.

## Experimental Contract

- Dataset: `polished_dataset`.
- Input mode: setpoints only.
- Direction: `Fw` only.
- Split: frozen common split signature
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.
- Curves: `675` training, `194` validation, and `97` test.
- Primary promotion surface: `96` supported-core test conditions.
- Full finiteness and decomposition population: `966` eligible forward
  conditions.
- Random seed: `314159`.
- Official heavy TE Curve Verification Pipeline: not executed.

The bounded closeout diagnostic reused the repository's curve-payload
infrastructure but did not change any official TE Curve Verification Pipeline
decision.

## Causal Anchor Correction

Preparation exposed a provenance issue in the legacy Stage 3 replay. The
previous artifact declared a setpoint-only contract but used measured
operating averages. Stage 4 preserved that artifact for provenance and fitted
a new training-only causal `PF-A` surface from:

- negative physical forward torque derived from the positive setpoint
  magnitude;
- absolute nominal input speed;
- nominal oil temperature.

The causal anchor achieves the following independent test metrics:

- raw MAE: `0.001808977 deg`;
- centered MAE: `0.001381875 deg`;
- absolute offset error: `0.000975232 deg`.

The deployment envelope classifies `96` of the `97` test conditions as
supported core and one as sparse/corner support. All `966` eligible forward
conditions and all `27` envelope stress points produce finite outputs.

## Implementation And Preflight

Stage 4 introduced:

- a direct data-only pointwise control (`R1`);
- frozen-anchor pointwise residuals (`R2`);
- physically bounded pointwise residuals (`R3`);
- low-rank Fourier residuals (`R4`);
- explicit analytical-coefficient corrections (`R5`);
- frozen, partial-unfreeze, and full-unfreeze anchor modes;
- residual-energy losses and decomposition metrics;
- deterministic parameter-matched campaign generation;
- local, remote, preflight-only, one-batch, and enqueue-only launcher paths.

The consolidated preflight passed `16 / 16` gates. All `18 / 18` real-dataset
one-batch checks passed. Zero-initialized hybrids reproduced their anchor
exactly, the independent signed-torque replay error was zero, the R3 residual
never exceeded `0.016873775 deg`, and frozen analytical parameters were absent
from the optimizer.

The first campaign launch stopped before training because the central runner
did not yet dispatch the new model type. The failed queue and output were
preserved as diagnostic evidence. After adding and validating the dispatch
entry, the clean retry completed all planned runs.

## Scalar Campaign Results

| ID | Family | Validation MAE [deg] | Test MAE [deg] |
| --- | --- | ---: | ---: |
| C01 | `stage4_c01_r1_compact` | 0.001835 | 0.001624 |
| C02 | `stage4_c02_r1_deep` | 0.002001 | 0.001760 |
| C03 | `stage4_c03_r1_compact` | 0.001874 | 0.001620 |
| C04 | `stage4_c04_r1_deep` | 0.001828 | 0.001609 |
| C05 | `stage4_c05_r1_compact` | 0.001835 | 0.001624 |
| C06 | `stage4_c06_r1_deep` | 0.001915 | 0.001665 |
| H01 | `stage4_h01_r2_compact` | 0.002123 | 0.001940 |
| H02 | `stage4_h02_r2_deep` | 0.001630 | 0.001617 |
| H03 | `stage4_h03_r3_compact` | 0.058291 | 0.046115 |
| H04 | `stage4_h04_r3_deep` | 0.058330 | 0.046188 |
| H05 | `stage4_h05_r4_compact` | 0.002346 | 0.002111 |
| H06 | `stage4_h06_r4_deep` | 0.002177 | 0.001965 |
| H07 | `stage4_h07_r5_compact` | 0.001765 | 0.001725 |
| H08 | `stage4_h08_r5_deep` | 0.001490 | 0.001455 |
| A01 | `stage4_a01_r2_compact` | 0.002265 | 0.001878 |
| A02 | `stage4_a02_r2_compact` | 0.006336 | 0.005241 |
| A03 | `stage4_a03_r5_compact` | 0.002057 | 0.001926 |
| A04 | `stage4_a04_r5_compact` | 0.003065 | 0.002846 |

The scalar leaderboard alone would select `H08`. That selection is rejected
by the required closeout audit.

## Curve-First And Cancellation Audit

The frozen causal `R0` anchor achieves, on the `96` supported-core test curves:

- raw curve MAE: `0.001824548 deg`;
- centered curve MAE: `0.001394187 deg`;
- absolute curve-mean error: `0.000981458 deg`;
- P95 curve MAE: `0.003970491 deg`;
- worst-curve MAE: `0.009475513 deg`.

| Hybrid | Matched control | Curve MAE [deg] | Residual/anchor RMS | Gate |
| --- | --- | ---: | ---: | --- |
| H01 | C01 | 0.060060 | 1.3883 | fail |
| H02 | C02 | 0.059691 | 1.3812 | fail |
| H03 | C01 | 0.014912 | 0.2687 | fail |
| H04 | C02 | 0.015179 | 0.2707 | fail |
| H05 | C03 | 0.060221 | 1.3885 | fail |
| H06 | C04 | 0.060441 | 1.3929 | fail |
| H07 | C05 | 0.059974 | 1.3871 | fail |
| H08 | C06 | 0.060538 | 1.3955 | fail |

All decompositions were finite on `966 / 966` curves. R3 respected its hard
bound with zero violations. The other primary hybrids used residual energy
larger than the analytical anchor, with population RMS ratios between
`1.3812` and `1.3955`. They therefore acted as cancellation networks rather
than small physics-guided corrections.

The R3 candidates preserved analytical dominance, but their bounded residual
could not bridge the mismatch and their raw curve MAE remained about one order
of magnitude above the anchor and direct controls.

## Interpretation

The apparent contradiction between scalar and curve-first results comes from
the representation used by the two surfaces:

1. the analytical Polynomial-Fourier anchor is fitted and validated on one
   canonical uniformly resampled periodic curve per condition;
2. the Stage 4 pointwise trainer samples the longer polished curve payload;
3. an unconstrained residual can learn the difference between those
   representations and improve sampled-point MAE;
4. replaying that correction on the canonical curve cancels an anchor that was
   already accurate there.

This does not invalidate the Polynomial-Fourier theory. It invalidates the
tested strategy of combining that anchor with an independently point-sampled
residual objective and then interpreting scalar MAE as physics-guided gain.

## Exit Decision

- Stage 4 status: completed negative.
- Promoted residual architecture: none.
- Stability repeats: not required.
- Official TE Curve Verification Pipeline decision: unchanged.
- Accepted periodic GRU and periodic harmonic MLP controls: unchanged.
- Frozen causal `PF-A`: retained as an analytical comparator inside its
  supported-core envelope.

## Stage 5 Entry Contract

Stage 5 is authorized as the next roadmap step, with these lessons carried
forward:

1. train sine/cosine coefficient targets on the same canonical resampled
   curves used for evaluation;
2. reconstruct full curves inside the training objective;
3. keep offset, low-order, reducer-related, and high-order bands explicit;
4. compare direct coefficient prediction, frozen-base correction, and
   data-only coefficient controls at matched capacity;
5. gate every candidate on full-curve raw, centered-shape, offset, derivative,
   amplitude, phase, P95, and worst-case metrics;
6. reject any candidate whose learned correction dominates or cancels the
   analytical base without an explicit, interpretable reason.

## Canonical Evidence

- Campaign output:
  `output/training_campaigns/2026-07-28-10-01-40_wave52r_stage4_data_only_residual_capacity_2026_07_28/`
- Causal anchor:
  `output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_causal_setpoint_pf_a_surface.yaml`
- Preflight summary:
  `output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_preflight_validation_summary.json`
- Curve diagnostics:
  `output/validation_checks/wave52r_stage4_data_only_residual_curve_diagnostics/2026-07-28-15-44-59__track2c_curve_payload_diagnostics/`
- Exit-gate summary:
  `output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/closeout/stage4_exit_gate_summary.yaml`
- Detailed cancellation audit:
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-28]/stage4_data_only_residual_capacity_ladder/stage4_curve_first_and_cancellation_audit.md`

## Closeout Integrity

Together, these artifacts provide the reproducible evidence for the Stage 4
negative closeout and the Stage 5 entry decision.
