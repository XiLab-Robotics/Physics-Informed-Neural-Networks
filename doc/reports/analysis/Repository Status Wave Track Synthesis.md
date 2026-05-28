# Repository Status Wave Track Synthesis

## Executive Summary

The repository is in an active but stable post-`Wave 2C` state. No training
campaign is currently prepared or running, and
`doc/running/active_training_campaign.yaml` has no protected files.

The current scalar program winner is:

| Surface | Run | Family | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | ---: | ---: |
| `Bw` | `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence_bw` | 0.002344 | 0.002747 |

That scalar winner is not the whole decision anymore. Commit
`b73220679410276246421b7e2832d8878cff90a0` moved promotion toward full
`Track 2` curve-following quality.

Current `Track 2` decision:

- accepted paper-derived baselines remain `paper_retuned_best_Fw` and
  `paper_retuned_best_Bw`;
- `tree` remains the strongest repository-owned static baseline;
- `Wave 2B` is the strongest repository-owned neural branch, while `Wave 2C`
  is verified only as an exploratory residual harmonic temporal baseline.

## Repository State

The program has closed the following major surfaces:

| Surface | Current State | Operational Meaning |
| --- | --- | --- |
| `Track 1` | closed | faithful full-bank RCIM paper reproduction surface |
| `Wave 1` | closed | structured static repository baselines |
| `Track 2` | closed through `Wave 2C` | official offline curve-verification matrix |
| `Wave 2` | completed | first temporal sequence baselines |
| `Wave 2B` | completed | harmonic temporal hybrids, current strongest neural branch |
| `Wave 2C` | completed | residual harmonic temporal hybrids, exploratory baseline |

The repository now has `53` implemented and benchmarked family surfaces in the
master summary. The next active work should not be another blind family
addition. The current focus is standardizing curve-first reranking on the
expanded `Track 2` metric surface.

Operationally, the repository is ready for decision-oriented analysis rather
than another bookkeeping pass. The available evidence now covers scalar
leaderboards, official curve reports, direction-aware comparisons, and
deployment plausibility for the strongest branches.

## Wave 1 Static Baselines

`Wave 1` remains the closed structured-static baseline wave. It covers
direction-separated `global`, `Fw`, and `Bw` surfaces for tree, feedforward,
periodic MLP, harmonic regression, and residual harmonic MLP families.

The scalar HPO closeout leader is:

| Rank | Family | Scope | Engine | Test MAE [deg] | Test RMSE [deg] |
| ---: | --- | --- | --- | ---: | ---: |
| 1 | `tree_fw` | `forward` | `bounded_grid` | 0.002743 | 0.003409 |
| 2 | `tree` | `global` | `bounded_grid` | 0.002782 | 0.003520 |
| 3 | `tree_bw` | `backward` | `bounded_grid` | 0.002954 | 0.003749 |

The post-closeout harmonic tracking campaigns improved the harmonic-specific
families but did not displace the tree baseline as the strongest `Wave 1`
scalar and `Track 2` static family.

Best current harmonic-oriented `Wave 1` scalar results:

| Family Surface | Best Run | Harmonic Basis | Test MAE [deg] |
| --- | --- | --- | ---: |
| `harmonic_regression_fw` | `te_harmonic_dense360_tracking_Fw` | dense `0..360` | 0.002916 |
| `residual_harmonic_mlp_bw` | `te_residual_harmonic_rcim_sparse_tracking_Bw` | sparse `RCIM` | 0.003042 |
| `periodic_mlp_fw` | `te_periodic_mlp_dense240_tracking_Fw` | dense `0..240` | 0.003055 |
| `residual_harmonic_mlp_fw` | `te_residual_harmonic_rcim_sparse_tracking_Fw` | sparse `RCIM` | 0.003089 |

Interpretation:

- dense harmonics can help simple harmonic regression in forward-only scalar
  training;
- sparse `RCIM` remains strong for residual harmonic MLP surfaces;
- `periodic_mlp_harmonic_*` is a report/candidate label for explicit-harmonic
  `periodic_mlp` candidates, not a separate architecture family;
- `tree` remains the strongest repository-owned static `Track 2` baseline.

## Wave 2 Temporal Sequence Models

`Wave 2` introduced temporal sequence baselines:

- `temporal_convolution`;
- `gru_sequence`;
- `lstm_sequence`.

The entry campaign completed all `9` planned runs. Its scalar campaign winner
was:

| Run | Family | Scope | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | ---: | ---: |
| `te_gru_sequence_remote_Fw` | `gru_sequence_fw` | `Fw` | 0.003333 | 0.003881 |

The best global and backward temporal-entry surfaces were:

| Surface | Run | Family | Test MAE [deg] |
| --- | --- | --- | ---: |
| `global` | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003482 |
| `Bw` | `te_lstm_sequence_remote_Bw` | `lstm_sequence_bw` | 0.003557 |

`Track 2` verified these models as useful exploratory temporal baselines, but
plain temporal recurrence did not improve enough over the static tree and
paper-derived reference candidates.

## Wave 2B Harmonic Temporal Hybrids

`Wave 2B` added explicit periodic harmonic features to temporal convolution,
`GRU`, and `LSTM` sequence windows. The first tier used the sparse `RCIM`
harmonic list:

```text
[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
```

The campaign completed all `9` planned runs. Its scalar winner is also the
current program scalar winner:

| Run | Family | Scope | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | ---: | ---: |
| `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence_bw` | `Bw` | 0.002344 | 0.002747 |

The strongest bidirectional neural candidate is:

| Run | Family | Scope | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | ---: | ---: |
| `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | `global` | 0.002681 | 0.002971 |

`Track 2` confirms the same qualitative result. The official visual and metric
reports identify:

| Candidate | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error [%] |
| --- | --- | ---: | ---: | ---: |
| `periodic_gru_sequence_Bw` | `Bw` | 0.002392 | 0.002639 | 5.466 |
| `periodic_gru_sequence_global` | `global` | 0.002704 | 0.002949 | 6.139 |
| `periodic_lstm_sequence_global` | `global` | 0.002707 | 0.002958 | 6.120 |

Interpretation:

- adding explicit sparse harmonic features to recurrent temporal models is the
  most successful neural move so far;
- `GRU` and `LSTM` are nearly tied in global scalar and curve metrics, but the
  backward-only periodic `GRU` is the clearest winner;
- the result is still less deployability-transparent than static tree or
  harmonic models, so the next decision must be curve-first and
  TwinCAT-aware.

## Wave 2C Residual Harmonic Temporal Hybrids

`Wave 2C` tested a stronger decomposition:

- structured harmonic branch for the base TE shape;
- recurrent temporal branch for sequence-local residual correction;
- final prediction as the sum of the two branches.

The campaign tested `18` runs:

- `residual_harmonic_gru_sequence`;
- `residual_harmonic_lstm_sequence`;
- `global`, `Fw`, and `Bw` surfaces;
- sparse `RCIM`, dense `0..240`, and dense `0..360` harmonic banks.

The scalar campaign winner was:

| Run | Family | Basis | Scope | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | --- | --- | ---: | ---: |
| `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence_fw_sparse_rcim` | sparse `RCIM` | `Fw` | 0.003200 | 0.003635 |

The scalar leaderboard showed dense variants close to sparse variants in some
forward-only pointwise metrics. `Track 2` changed the interpretation: when the
models are judged on full curves, dense residual harmonic banks are clearly
weaker.

Strongest `Wave 2C` `Track 2` candidates:

| Scope | Candidate | Basis | Curve MAE [deg] | Curve RMSE [deg] | Mean Error [%] |
| --- | --- | --- | ---: | ---: | ---: |
| `Fw` | `residual_harmonic_gru_sequence_sparse_rcim_Fw` | sparse `RCIM` | 0.003194 | 0.003499 | 7.083 |
| `Bw` | `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | sparse `RCIM` | 0.003440 | 0.003793 | 7.510 |
| `global` | `residual_harmonic_lstm_sequence_sparse_rcim_global` | sparse `RCIM` | 0.003368 | 0.003719 | 7.409 |

Dense `Wave 2C` `Track 2` examples:

| Scope | Candidate | Basis | Curve MAE [deg] | Mean Error [%] |
| --- | --- | --- | ---: | ---: |
| `Fw` | `residual_harmonic_gru_sequence_dense240_Fw` | dense `0..240` | 0.006983 | 15.722 |
| `Fw` | `residual_harmonic_gru_sequence_dense360_Fw` | dense `0..360` | 0.007869 | 17.740 |
| `Bw` | `residual_harmonic_lstm_sequence_dense240_Bw` | dense `0..240` | 0.007367 | 16.660 |
| `Bw` | `residual_harmonic_lstm_sequence_dense360_Bw` | dense `0..360` | 0.010268 | 23.355 |
| `global` | `residual_harmonic_lstm_sequence_dense240_global` | dense `0..240` | 0.006419 | 14.460 |
| `global` | `residual_harmonic_lstm_sequence_dense360_global` | dense `0..360` | 0.008810 | 19.916 |

Interpretation:

- sparse `RCIM` is the correct `Wave 2C` harmonic tier;
- dense residual harmonic expansion overfits or destabilizes the curve surface;
- residual decomposition is useful as a diagnostic branch, but it does not beat
  the simpler `Wave 2B` periodic recurrent formulation;
- `Wave 2C` should stay closed as a verified exploratory baseline.

## Track 2 Current Result

The official `Track 2` package now contains `111` candidates. It evaluates
direction-valid held-out TE curves and reports curve-level metrics separately
from scalar training metrics.

Current official leaders:

| Scope | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] |
| --- | --- | ---: | ---: | ---: |
| forward overall | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 |
| backward overall | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 |
| paper-derived forward | `paper_retuned_best_Fw` | 0.001839 | 0.002041 | 4.109 |
| paper-derived backward | `paper_retuned_best_Bw` | 0.003675 | 0.004284 | 7.572 |
| repository static backward | `tree_Bw` | 0.003258 | 0.003651 | 7.051 |
| repository global static | `tree_global` | 0.003144 | 0.003533 | 6.854 |
| repository global neural | `periodic_gru_sequence_global` | 0.002704 | 0.002949 | 6.139 |

The important split is:

- the recovered/retuned paper reference still owns the best forward curve
  result;
- `Wave 2B` owns the best repository neural backward and global neural result;
- `Wave 1` tree remains the most robust repository-owned static baseline;
- `Wave 2C` adds evidence about harmonic-bank choice, not a new promotion.

## Harmonic Bank Conclusions

The harmonic-bank evidence is direction- and family-dependent. There is no
single universal winner across every algorithm.

| Context | Best Observed Choice | Evidence |
| --- | --- | --- |
| `Wave 1` harmonic regression, `Fw` | dense `0..360` | `test_mae = 0.002916` |
| `Wave 1` periodic MLP, `Fw` | dense `0..240` | `test_mae = 0.003055` |
| `Wave 1` residual harmonic MLP, `Bw` | sparse `RCIM` | `test_mae = 0.003042` |
| `Wave 2B` periodic recurrent | sparse `RCIM` feature tier | `periodic_gru_sequence_Bw`, `test_mae = 0.002344` |
| `Wave 2C` residual harmonic temporal | sparse `RCIM` | best scalar and all best `Track 2` surfaces |
| `Wave 2C` dense residual temporal | dense `0..240` or `0..360` | poor `Track 2` curve metrics |

Practical conclusion:

- dense harmonic banks are useful as targeted stress tests and can help some
  static or low-capacity harmonic models;
- sparse `RCIM` harmonics are the better default for neural hybrid and residual
  temporal work;
- dense `0..240` and `0..360` should not be promoted into new temporal
  residual campaigns without a curve-first reason.

## Perspective Shift From Commit b73220679410276246421b7e2832d8878cff90a0

Commit `b73220679410276246421b7e2832d8878cff90a0` is titled:

```text
Define curve-first TE training strategy
```

Its change of vision is important. Before that commit, the repository could be
read as mostly scalar-registry driven: a lower `test_mae` moved the program
winner. After that commit, scalar error remains a sanity gate, but not the
final promotion rule for TE compensation.

The new interpretation is:

1. TE compensation is a continuous curve-following problem.
2. Full held-out curves are evaluation units, not future inputs supplied to the
   runtime model.
3. Future deployed models must remain causal: current operating state, optional
   short past history, or causal derived features only.
4. `Track 2` curve metrics and visual overlays become the promotion surface.
5. Scalar winner, curve-first winner, and deployment-ready candidate should be
   reported separately until `Track 3` online evidence exists.

This is a useful correction. It prevents the next work from chasing a small
pointwise `MAE` gain that may smooth out oscillations, shift harmonic phase, or
fail under repeated-revolution compensation.

## Future Development Plan

### Step 1: Track 2B Curve-First Reranking

Open the already planned `Track 2B Curve-First Reranking` branch before any new
training campaign.

Deliverables:

- expanded per-curve metric CSV;
- direction-separated reranking for `Wave 1`, `Wave 2`, `Wave 2B`, and
  `Wave 2C`;
- harmonic amplitude and harmonic phase diagnostics on the sparse `RCIM`
  harmonic set;
- P95 and worst-condition percentage-error tables;
- updated visual overlays if the screened candidate set changes;
- master-summary update separating scalar best from curve-first best.

### Step 2: Decide Whether To Retrain Or Promote

If reranking confirms that `Wave 2B` periodic recurrent models are also the
best curve-first neural branch, keep them as the neural reference and improve
checkpoint selection before changing families.

If a static or harmonic model is better curve-first despite weaker scalar
metrics, open a compact retraining branch around that family rather than
launching a broad new model wave.

### Step 3: Add Curve-First Checkpoint Selection

Update neural training infrastructure so checkpoint selection can monitor a
validation curve metric, for example:

```text
val_curve_mean_percentage_error_pct
```

Tie-breakers should include curve P95 error, harmonic phase error, then scalar
`val_mae`.

### Step 4: Add Curve-Aware Losses Only After Metrics Stabilize

Do not immediately train with complex curve losses. First standardize the
curve metrics. Then test a small composite loss:

```text
pointwise_normalized_mse
+ curve_mae_term
+ slope_or_derivative_term
+ selected_harmonic_amplitude_term
+ selected_harmonic_phase_term
```

Soft-DTW or other warp-tolerant objectives should remain secondary ablations,
because physical angular phase matters for compensation.

### Step 5: Preserve A TwinCAT-Friendly Path

The final target is not only an offline benchmark. The selected path must stay
credible for TwinCAT/TestRig compensation.

Preferred future candidates:

- sparse `RCIM` harmonic or periodic models with explicit intermediate
  quantities;
- curve-first selected periodic `GRU` or `LSTM` only if deployment cost and
  inspectability are acceptable;
- residual harmonic MLP or structured harmonic variants with harmonic-space
  diagnostics;
- later `Track 3` online compensation tests for uncompensated versus
  compensated `TE RMS` and `TE max`.

Deferred exploratory candidates such as lightweight transformers, state-space
sequence models, neural ODEs, and kernel/Gaussian-process baselines should stay
low priority until `Track 2B` clarifies what the existing candidates already
do on full curves.

## Bottom Line

The work is no longer in a raw model-search phase. The repository now has a
complete scalar and `Track 2` evidence surface through `Wave 2C`.

The best scalar neural result is `Wave 2B` `periodic_gru_sequence_Bw`. The best
repository static baseline remains `tree`. The best forward curve result is
still paper-derived retuned `GBM`. The most important technical next step is
not another large campaign, but a curve-first reranking and promotion policy
that decides which existing candidates are actually suitable for continuous TE
compensation.
