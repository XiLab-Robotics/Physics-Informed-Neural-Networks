# Wave 5.2R Stage 9 Temporal Analytical-Residual Models Campaign Plan

## Campaign Objective

Test whether causal angular context improves `polished_dataset`, setpoint-only,
forward (`Fw`) transmission-error prediction and whether PF-A or qualified H04
provides a useful anchor for a causal GRU residual.

The campaign is falsification-first. It does not interpret angular context as
load-history hysteresis because setpoints remain constant inside each recorded
steady-state curve and the dataset does not preserve an ordered trajectory
between operating conditions.

## Approval

- technical document:
  `doc/technical/2026-07/2026-07-29/2026-07-29-18-35-28_wave52r_stage9_temporal_analytical_residual_models.md`;
- technical-document status: approved automatically;
- campaign-plan status: approved automatically;
- approval source: user blanket approval for twenty-four hours;
- approval recorded at: `2026-07-29T15:30:41+02:00`;
- approval expires at: `2026-07-30T15:30:41+02:00`.

## Frozen Evidence Contract

| Item | Contract |
| --- | --- |
| Dataset | `polished_dataset` |
| Inputs | setpoints only |
| Direction | `Fw` |
| Curves | `966` |
| Split | `675 / 194 / 97` |
| Grid | `2048` angular points |
| Split signature | `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16` |
| Structured baseline | Stage 5 H04 |
| Temporal benchmark | accepted `periodic_gru_sequence_Fw` |
| First-screen seed | `314159` |
| Conditional seeds | `271828`, `161803` |

The accepted periodic GRU artifact reports `1356 / 388 / 194` curves despite
its forward registry label. Its historical training split and centered-window
contract therefore differ from the Stage 9 causal contract. The campaign will
replay it on the Stage 0 forward test curves as an external performance
benchmark and will not call it a causal or split-matched control.

## Causal Runtime Contract

New temporal candidates may use:

- current and previous angular position;
- current and previous setpoint torque, speed, and temperature;
- sine/cosine angle features;
- explicitly carried GRU hidden state within one contiguous curve;
- PF-A or frozen H04 predictions computed from causal setpoints and angle.

They may not use:

- future angular samples;
- centered sequence windows;
- bidirectional recurrence;
- measured TE as an input or warm start;
- measured curve mean or centered target;
- offline fitted target coefficients;
- validation or test targets for normalization, selection, or prior fitting;
- hidden state carried across curve boundaries.

Each curve starts from an explicit zero hidden state. Repeating inference after
reset must reproduce the same output within floating-point tolerance.

## Candidate Matrix

| ID | Formulation | Anchor | Temporal role |
| --- | --- | --- | --- |
| `D00` | frozen H04 replay | H04 | static baseline |
| `G00` | accepted periodic GRU replay | none | external benchmark |
| `C00` | causal periodic GRU | none | direct temporal control |
| `R00` | causal residual GRU | zero | parameter-matched residual control |
| `P01` | PF-A plus residual GRU | frozen PF-A | analytical hybrid |
| `H01` | H04 plus residual GRU | frozen H04 | qualified-anchor hybrid |
| `K01` | H04 coefficient-residual GRU | frozen H04 | coefficient hybrid |
| `M01` | static mean plus temporal shape | H04 mean | decomposed hybrid |
| `L01` | H04 residual GRU curriculum | frozen H04 | context-length curriculum |
| `N01` | shuffled angular-order residual GRU | frozen H04 | specificity control |

`D00` and `G00` are diagnostics. The eight trainable candidates use the same
Stage 0 split and bounded first-screen budget.

## Sequence Construction

- unidirectional GRU;
- `batch_first=True`;
- `33` causal points in the first screen;
- last-position target only;
- circular prefix padding is forbidden;
- the first `32` curve positions use shorter valid prefixes and explicit zero
  state;
- training windows are grouped by curve and never cross curve boundaries;
- setpoint features repeat along a steady-state curve but remain explicit;
- recurrent dropout is disabled for single-layer variants and bounded for
  stacked variants;
- sequence order is deterministic under the campaign seed.

L01 starts from short prefixes and increases context to `33`. N01 uses a fixed
training-only angular permutation while preserving targets and setpoints; it
tests whether chronological angular order, rather than extra parameter count,
creates the gain.

## Preflight

The launcher must pass:

1. exact Stage 0 split and curve-count checks;
2. accepted GRU checkpoint and architecture reconstruction;
3. H04 checkpoint and coefficient representation reconstruction;
4. zero target-derived runtime inputs;
5. strictly causal input-index audit;
6. curve-boundary reset audit;
7. repeated reset reproducibility;
8. chunked versus one-pass hidden-state equivalence;
9. candidate parameter-count report;
10. finite forward/backward gradients;
11. deterministic queue and immutable run-instance paths;
12. local and remote launcher syntax validation.

## First-Screen Metrics

Every candidate reports:

- raw MAE and RMSE;
- curve-mean MAE;
- centered-shape MAE and RMSE;
- offset absolute error;
- peak-to-peak error;
- derivative MAE and Sobolev derivative correlation;
- periodic closure;
- retained harmonic amplitude and phase;
- per-curve P95 and worst-case MAE;
- residual-to-anchor RMS;
- hidden-state mean and maximum norm;
- reset maximum absolute difference;
- chunked-inference maximum absolute difference;
- prefix-length error curve;
- shuffled-order prediction sensitivity;
- runtime target-derived input count.

## First-Screen Gate

P01, H01, K01, M01, and L01 must each:

- beat D00 raw and mean error;
- beat G00 raw and mean error on the Stage 0 test surface;
- beat R00 raw and mean error;
- beat N01 raw and mean error;
- preserve or improve centered shape;
- preserve derivative, closure, amplitude, phase, and P95 within the declared
  tolerances;
- keep residual-to-anchor RMS bounded;
- pass exact reset and chunk-equivalence thresholds;
- remain finite for every prefix length;
- report zero target-derived runtime inputs.

No arm advances because it beats only H04 or only a historical scalar metric.

## Conditional Stability

Only candidates passing every first-screen gate continue to seeds `271828` and
`161803`. Promotion requires:

- `3 / 3` seeds passing all gates;
- median raw and mean improvement versus G00 and R00;
- no seed-specific reset or prefix instability;
- no reversal of the centered-shape or harmonic decision;
- inspectable hidden-state and anchor-residual behavior.

## Stop Conditions

Stop escalation when:

- the accepted GRU cannot be reconstructed or replayed faithfully;
- a new candidate consumes future samples;
- the model crosses curve boundaries without reset;
- chunked and one-pass inference disagree beyond tolerance;
- H04 or PF-A reconstruction drifts;
- any target-derived runtime input appears;
- no first-screen hybrid beats both G00 and R00;
- the shuffled-order control matches the claimed temporal gain.

## Campaign Artifacts

The approved preparation will create:

- `config/training/temporal_analytical_residual_models/`;
- `scripts/models/causal_temporal_analytical_residual_network.py`;
- `scripts/campaigns/wave_5_2/run_wave52r_stage9_temporal_analytical_residual_models.py`;
- `scripts/campaigns/wave_5_2/run_wave52r_stage9_temporal_analytical_residual_models.ps1`;
- `doc/scripts/campaigns/wave_5_2/run_wave52r_stage9_temporal_analytical_residual_models.md`;
- `output/analysis/wave_5_2r/stage9_temporal_analytical_residual_models/`;
- immutable training-run and campaign-output directories;
- Markdown and validated PDF campaign-results report.

## Launch Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -Run
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -Remote -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage9_temporal_analytical_residual_models.ps1 -Remote -Run
```

The campaign does not run the heavy TE Curve Verification Pipeline. If a
candidate is promoted after normal closeout, official offline verification
remains a separate user-approved step.
