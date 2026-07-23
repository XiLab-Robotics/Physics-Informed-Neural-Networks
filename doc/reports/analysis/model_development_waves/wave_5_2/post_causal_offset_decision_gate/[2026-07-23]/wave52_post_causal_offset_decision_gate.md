# Wave 5.2 Post-Causal-Offset Decision Gate

## Overview

This report closes the `Wave 5.2` decision gate after the causal offset / mean
calibration pilot and its bounded `TE Curve Verification Pipeline` screen.

The purpose is to select the next evidence-backed branch without starting
another training campaign. The recent sequence of shape-aware, offset-aware,
and harmonic-guided pilots has not displaced the accepted polished-setpoint
baselines under curve-first evaluation. The next useful step is therefore to
prove whether MMT-derived physical signatures explain held-out model residuals
before using those signatures as learned features or soft constraints.

## Decision

Keep the MMT path diagnostic-only for the next step.

Prepare a leakage-safe MMT residual-explanatory diagnostic against both the
time-windowed and non-windowed accepted baselines. Do not prepare another
training pilot until that diagnostic demonstrates stable held-out explanatory
value beyond operating metadata alone.

If the diagnostic passes, the preferred first implementation is a compact
MMT-derived feature or auxiliary-prediction path. A weak MMT soft constraint
remains secondary. A full analytical surrogate, full PINN, and Wave 6
multi-head integration remain deferred.

This decision does not authorize training.

## What The Reference Establishes

The repository-owned MMT paper develops an analytical rotational transmission
error model by replacing higher pairs with lower pairs, building an equivalent
multi-loop mechanism, and applying a loop incremental method. Manufacturing
and assembly errors are represented as equivalent linkage-length errors.

The paper supports three conclusions that are relevant here:

- rotational transmission error is explicitly related to original
  high-speed-stage and low-speed-stage errors;
- cycloidal-stage errors produce strong mesh-frequency components and their
  multiples;
- low-speed-stage error sources have larger influence than the tested
  high-speed-stage error, while the output-disc hole-position deviation is
  associated with frequency component 1.

The paper validated its model on two prototypes under low-speed, near-no-load
conditions. It does not prove that its calibrated component-error parameters
transfer directly to the repository's broader speed, torque, and temperature
matrix. That transfer remains an engineering hypothesis.

## What Is Implemented And Observed

### MMT And Dataset Evidence

The current MMT parameter inventory contains `11` parameter groups:

- `3` known geometry-constant groups;
- `1` known operating-metadata group;
- `5` train-only calibratable equivalent-error groups;
- `1` unavailable or ambiguous contact-geometry group;
- measured TE as target-only information.

The inventory classifies the MMT path as `not_campaign_ready`. Contact geometry
blocks a calibrated analytical baseline, and target-derived curve means or
held-out curves are forbidden as inference inputs.

The completed `Wave 5.2A` paired-dataset diagnostic evaluated `1938`
directional pairs:

| Signal | Value |
| --- | ---: |
| Mean absolute offset delta [deg] | 0.003216838 |
| Mean absolute peak-to-peak delta [deg] | 0.000000134 |
| Mean absolute smoothness delta [deg] | 0.000000003 |
| Mean maximum nonzero-harmonic delta [deg] | 0.001749405 |
| Offset-shifted pairs | 901 |
| Nonzero-harmonic changed pairs | 944 |
| Shape-changed pairs | 0 |
| Sampling anomalies | 27 |

This supports offset and nonzero-harmonic diagnostics. It does not prove that
an MMT term will improve a predictor.

### Wave 5.2B Evidence

The completed `Wave 5.2B` offset-and-harmonic-guided branch provided useful
architecture evidence but did not become the accepted curve-verified leader.
Its compact full-matrix results included:

| Candidate | Surface | Curve MAE [deg] | P95 Error [%] |
| --- | --- | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Fw` | forward | 0.001695 | 8.270 |
| `wave52b_offset_centered_shape_harmonic_Bw` | backward | 0.002266 | 9.758 |
| `wave52b_offset_centered_shape_harmonic_global` | combined | 0.002221 | 9.818 |

These results justify retaining offset and harmonic structure as diagnostic
signals. They do not justify rerunning `Wave 5.2B` unchanged.

### Recent Bounded Screens

The recent bounded screens repeatedly selected the accepted
`polished_setpoints_periodic_gru_sequence_Fw` baseline over new candidates.

The final causal-offset screen evaluated `100` forward held-out curves:

| Candidate | Rank | Raw MAE [deg] | Centered MAE [deg] | Harmonic Amp Error [%] | Shape Pass |
| --- | ---: | ---: | ---: | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Fw` | 1 | 0.001837 | 0.001483 | 17.555 | 0.950 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | 2 | 0.001938 | 0.001490 | 15.624 | 0.920 |
| `causal_offset_mean_periodic_mlp_harmonic_Fw` | 4 | 0.002075 | 0.001652 | 19.655 | 0.920 |
| `causal_offset_mean_gru_sequence_Fw` | 5 | 0.002392 | 0.002024 | 77.579 | 0.000 |

The direct causal-offset GRU failed on harmonic amplitude, phase, derivative,
FFT, and peak-to-peak behavior. The non-windowed causal MLP also remained
behind both accepted baselines.

## Interpretation

Three statements are now supported by implemented evidence:

1. Offset and harmonic structure matter diagnostically.
2. Directly adding offset, shape-threshold, or harmonic training pressure has
   not produced a curve-first promotion.
3. The repository does not yet know whether the available MMT terms explain
   held-out residual structure or merely restate operating-condition
   correlations.

It is therefore premature to encode the MMT equations as a soft loss. A soft
constraint could force the model toward an incompletely calibrated analytical
surface, especially outside the paper's low-speed, near-no-load validation
conditions.

The next diagnostic should test explanatory value first. This is an inference
from the combined paper and repository evidence, not a claim proven by the
paper.

## Selected Next Diagnostic

### Scope

| Item | Decision |
| --- | --- |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Surfaces | `Fw` and `Bw`; keep `global` paused |
| Windowed baseline | accepted `periodic_gru_sequence` candidate per surface |
| Non-windowed baseline | accepted `periodic_mlp_harmonic` candidate per surface |
| Training | none |
| Registry promotion | none |
| Full Track 2 refresh | none |

### Diagnostic Design

The diagnostic should:

1. Reconstruct only geometry-locked MMT signatures and allowed
   operating-condition terms.
2. Calibrate any equivalent-error group on training partitions only, separated
   by direction and allowed operating strata.
3. Compute baseline residual summaries for raw error, curve mean, centered
   shape, harmonic amplitude and phase, and derivative behavior.
4. Test whether MMT signatures explain held-out residual structure beyond:
   - operating metadata alone;
   - direction and load grouping alone;
   - shuffled-signature controls.
5. Repeat the test for both the windowed and non-windowed baselines so a useful
   signature is not confused with one architecture's residual pattern.
6. Keep all target-derived curve statistics out of inference-side inputs.

### Pass Gate

The diagnostic passes only if:

- explanatory value survives held-out evaluation;
- the result is stronger than metadata-only and shuffled controls;
- the relationship is stable across the relevant direction surface;
- the identified signature improves understanding of offset or fragile
  harmonics without degrading centered-shape interpretation;
- every required runtime quantity is available, reconstructable, or explicitly
  predicted from causal inputs.

No arbitrary scalar threshold should be treated as sufficient by itself.

## Deferred Alternatives

| Alternative | Decision | Reason |
| --- | --- | --- |
| Rerun direct causal offset calibration | Reject | The bounded screen did not promote either candidate, and the GRU failed the shape gate. |
| Rerun `Wave 5.2B` unchanged | Reject | Existing results are useful evidence but did not establish a new curve-first leader. |
| MMT-derived feature or auxiliary head | Conditional next implementation | Preferred only if the residual-explanatory diagnostic passes. |
| Weak MMT soft constraint | Defer | Physical terms are incompletely calibrated and have not yet shown held-out residual explanatory value. |
| Full MMT analytical surrogate or full PINN | Defer | Contact geometry and multiple original error channels are unavailable or train-only calibratable. |
| Wave 6 integrated multi-head model | Defer | No new mechanism has yet beaten the accepted baselines under the bounded curve-first gate. |

## Next Action

Create a separate technical document for the non-training MMT
residual-explanatory diagnostic.

That future document should define the train/validation partition boundary,
MMT signature inventory, metadata-only and shuffled controls, per-surface
baseline set, machine-readable outputs, and report QA. If the diagnostic later
supports a training pilot, campaign YAML files, a planning report, launchers,
and active campaign state will require a separate approval gate.
