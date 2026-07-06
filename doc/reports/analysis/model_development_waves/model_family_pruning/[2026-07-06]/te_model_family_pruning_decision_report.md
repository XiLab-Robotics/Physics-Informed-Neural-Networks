# TE Model Family Pruning Decision Report

## Overview

This report reduces the near-term TE model-selection surface after the
polished-dataset retraining and the official `2026-07-03`
`TE Curve Verification Pipeline` refresh.

The practical goal is not to delete historical artifacts. The goal is to stop
carrying every implemented family into the next design cycle. The next
candidate set should be small enough to reason about, inspect visually, and
prepare for deployment-facing work.

## Decision Scope

Near-term decisions use these rules:

- `global` is paused everywhere for model-family selection.
- `global` artifacts stay preserved, but they are excluded from current
  candidate ranking and reduced-pipeline planning.
- `forward` is the primary decision driver.
- `backward` is the consistency check.
- If `forward` and `backward` disagree slightly, the decision follows
  `forward` and records the mismatch.
- If they disagree substantially, the family is marked for explicit later
  review rather than silently splitting the program.

The postponed `global` review should be reopened only when it is the last
remaining modeling item in the backlog.

## Evidence Sources

The decisions use current repository-backed evidence:

- official polished-dataset `TE Curve Verification Pipeline` refresh:
  `output/validation_checks/track2_reference_comparison/2026-07-03-17-46-19__track2_full_directional_family_matrix_polished_dataset_te_curve_verification_refresh_2026_07_03_fix3/`;
- Wave 5.2B offset and harmonic guided refresh:
  `output/validation_checks/track2_reference_comparison/2026-07-02-12-43-56__track2_full_directional_family_matrix_wave52b_offset_harmonic_guided_track2_refresh_2026_07_02/`;
- campaign results under `doc/reports/campaign_results/`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`;
- family registries under `output/registries/families/`.

The `2026-07-03` polished refresh is the primary comparison surface. The older
pre-polished candidate rows remain useful as historical baselines, but they do
not override the polished model-development evidence.

## Decision Labels

| Label | Meaning |
| --- | --- |
| `continue` | Keep in the active reduced candidate set or next design gate. |
| `baseline-only` | Keep as a comparison anchor; do not extend or tune now. |
| `pause` | Preserve evidence and artifacts, but remove from near-term training and reduced-pipeline candidate sets. |
| `retire` | Stop considering for future model development unless new evidence explicitly reopens it. |

## Reduced Candidate Recommendation

The next reduced `TE Curve Verification Pipeline` or equivalent comparison
should not include every implemented family. A practical reduced set is:

| Role | Candidate Family | Reason |
| --- | --- | --- |
| Historical forward reference | `rcim_retuned_GBM19_Fw` | Full-matrix forward leader: Mean `2.372%`, MAE `0.001089 deg`. |
| Polished forward reference bank | `polished_rcim_model_bank_reproduction_ET19_Fw` | Best polished reference-bank forward candidate: Mean `2.401%`, MAE `0.001155 deg`. |
| Primary deployable neural family | `polished_periodic_gru_sequence_Fw/Bw` | Best polished model-development family on both active surfaces: Fw Mean `2.559%`, Bw Mean `2.228%`. |
| Lightweight harmonic comparator | `polished_periodic_mlp_harmonic_Fw/Bw` | Compact, simple, and useful as a harmonic-feature baseline; weaker than periodic GRU. |
| Uncertainty / distributional comparator | `polished_wave4_3_mixture_density_k3_Fw/Bw` | Best non-periodic advanced branch on both active surfaces: Fw Mean `3.161%`, Bw Mean `3.405%`. |
| Dataset-aware structure ingredient | `wave52b_offset_centered_shape_harmonic_Fw/Bw` | Confirms offset plus centered-shape plus harmonic guidance is useful; not promoted as a standalone leader. |
| Plain anchors | `feedforward`, `tree`, `harmonic_regression` | Keep only as interpretability and regression anchors. |

Everything else should be excluded from the next reduced candidate set unless a
specific diagnostic question requires it.

## Forward-Led Evidence Snapshot

| Family | Fw Mean [%] | Fw MAE [deg] | Bw Mean [%] | Bw MAE [deg] | Params | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `rcim_retuned_GBM19` | 2.372 | 0.001089 | 5.398 | 0.002766 | N/A | `baseline-only` |
| `polished_rcim_ET19` | 2.401 | 0.001155 | 7.021 | 0.003441 | N/A | `baseline-only` |
| `periodic_gru_sequence` | 2.559 | 0.001195 | 2.228 | 0.001129 | 157,569 | `continue` |
| `wave4_3_mixture_density_k3` | 3.161 | 0.001528 | 3.405 | 0.001930 | 86,976 | `continue` |
| `wave4_3_mixture_density_k2` | 3.202 | 0.001545 | 3.526 | 0.001995 | 86,400 | `pause` |
| `wave52b_offset_centered_shape_harmonic` | 3.391 | 0.001695 | 3.986 | 0.002266 | 22,593 | `continue` |
| `wave3_3_curve_aware_pointwise_control` | 3.407 | 0.001701 | 3.909 | 0.002172 | 85,440 | `pause` |
| `wave4_2_gaussian_nll` | 3.424 | 0.001711 | 3.758 | 0.002133 | 85,632 | `baseline-only` |
| `wave3_3_raw_centered_shape_curve_aware` | 3.450 | 0.001716 | 3.790 | 0.002133 | 85,440 | `pause` |
| `wave4_2_quantile_p10_p50_p90` | 3.466 | 0.001727 | 3.778 | 0.002133 | 85,824 | `pause` |
| `periodic_mlp_harmonic` | 3.511 | 0.001735 | 4.137 | 0.002396 | 28,417 | `continue` |
| `wave3_2_harmonic_residual_offset` | 3.526 | 0.001756 | 3.805 | 0.002142 | 85,440 | `pause` |
| `wave4_1_log_cosh_robust_loss` | 3.566 | 0.001764 | 3.787 | 0.002131 | 85,440 | `pause` |
| `wave4_1_mae_robust_loss` | 3.569 | 0.001775 | 3.754 | 0.002133 | 85,440 | `pause` |
| `wave5_1_harmonic_prior_smooth_l1_structured` | 3.630 | 0.001795 | 4.377 | 0.002528 | 7,168 | `pause` |
| `residual_harmonic_gru_sequence_sparse_rcim` | 3.700 | 0.001832 | 4.234 | 0.002331 | 150,676 | `pause` |
| `residual_harmonic_lstm_sequence_sparse_rcim` | 3.839 | 0.001892 | 4.242 | 0.002343 | 200,852 | `pause` |
| `periodic_temporal_convolution` | 4.123 | 0.002004 | 4.277 | 0.002326 | 157,889 | `pause` |
| `wave3_2_clean_sequential_residual_offset` | 4.192 | 0.002052 | 4.469 | 0.002439 | 92,418 | `retire` |
| `wave3_1_sequential_residual_offset_probe` | 4.236 | 0.002071 | 4.412 | 0.002411 | 92,418 | `retire` |
| `lstm_sequence` | 4.261 | 0.002083 | 4.452 | 0.002430 | 200,833 | `retire` |
| `gru_sequence` | 4.308 | 0.002102 | 4.438 | 0.002425 | 150,657 | `retire` |
| `periodic_mlp` | 4.351 | 0.002118 | 4.910 | 0.002769 | 28,417 | `retire` |
| `feedforward` | 4.378 | 0.002130 | 4.708 | 0.002655 | 109,953 | `baseline-only` |
| `tree` | 4.355 | 0.002125 | 4.934 | 0.002756 | 4 | `baseline-only` |
| `temporal_convolution` | 4.557 | 0.002210 | 4.674 | 0.002530 | 146,369 | `retire` |
| `harmonic_regression` | 7.534 | 0.003394 | 8.171 | 0.003745 | 125 | `baseline-only` |
| dense residual harmonic GRU/LSTM | 6.811-10.094 | 0.003186-0.004652 | 6.794-10.455 | 0.003416-0.005031 | 151k-202k | `retire` |

The table is intentionally forward-led. Backward confirms the main decision:
`periodic_gru_sequence` is the only polished model-development family that is
both simple enough and best-in-class on the active backward surface. The main
forward/backward disagreement is RCIM reference behavior: forward is still
excellent for retuned or polished tree-bank models, while backward is weaker
than the polished periodic GRU.

## Family Decisions

### RCIM And Paper-Reference Banks

| Family | Decision | Motivation |
| --- | --- | --- |
| `rcim_retuned_GBM19_Fw` | `baseline-only` | It remains the full-matrix forward leader. Keep it as the hard forward reference, but do not spend model-development effort extending the old retuned bank. |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | `baseline-only` | It is the strongest polished forward reference-bank candidate and should remain in reduced comparisons. |
| Other RCIM tree-bank families | `pause` | ERT and LGBM are close on forward, but they do not justify carrying the whole RCIM bank forward. Keep artifacts; compare only the selected leaders. |
| RCIM MLP / ELM / weak banks | `retire` | They are not competitive and add no useful deployment or diagnostic signal. |

### Simple Repository Baselines

| Family | Decision | Motivation |
| --- | --- | --- |
| `feedforward` | `baseline-only` | Useful as the plain neural anchor, but too weak to extend. |
| `tree` | `baseline-only` | Extremely simple and useful as a static tabular anchor, but not a next modeling branch. |
| `harmonic_regression` | `baseline-only` | Keep for interpretability, harmonic sanity checks, and offset diagnostics; do not treat as a production candidate. |
| `periodic_mlp` | `retire` | The harmonic variant is better and still compact, so the plain periodic MLP is redundant. |
| `periodic_mlp_harmonic` | `continue` | It is weaker than periodic GRU but compact and harmonic-aware. Keep as the lightweight deployability comparator. |

### Temporal Sequence Families

| Family | Decision | Motivation |
| --- | --- | --- |
| `periodic_gru_sequence` | `continue` | Primary model-development family. It is the accepted polished baseline and the strongest active backward candidate. |
| `periodic_lstm_sequence` | `baseline-only` | Backward is good, but it is heavier than GRU and forward is weaker. Keep as backup evidence, not as a branch to extend now. |
| `gru_sequence` | `retire` | Periodic GRU dominates it with no practical reason to carry the non-periodic variant. |
| `lstm_sequence` | `retire` | Heavier than GRU and weaker than periodic sequence variants. |
| `temporal_convolution` | `retire` | Weaker than periodic GRU and not simpler enough to justify continuation. |
| `periodic_temporal_convolution` | `pause` | Better than non-periodic TCN but still weaker than periodic GRU; keep only if a later latency test needs a convolutional comparator. |

### Residual Harmonic Sequence Families

| Family | Decision | Motivation |
| --- | --- | --- |
| sparse RCIM residual harmonic GRU/LSTM | `pause` | Sparse variants are not disastrous but are heavier and weaker than periodic GRU. Keep as evidence that harmonic residual sequence structure did not pay off enough. |
| dense240 / dense360 residual harmonic GRU/LSTM | `retire` | Too heavy and clearly worse on the polished curve metrics. |
| residual harmonic MLP | `retire` | The compact harmonic MLP and Wave 5.2B structure cover the useful idea with better evidence. |

### Offset And Curve-Aware Waves

| Family | Decision | Motivation |
| --- | --- | --- |
| `wave3_1_sequential_residual_offset_probe` | `retire` | Superseded by later offset / harmonic evidence and not competitive. |
| `wave3_2_clean_sequential_residual_offset` | `retire` | The clean offset branch is weaker than the harmonic offset branch and no longer worth carrying. |
| `wave3_2_harmonic_residual_offset` | `pause` | Confirms harmonic offset value, but Wave 5.2B is the cleaner current carrier of that idea. |
| `wave3_3_curve_aware_pointwise_control` | `pause` | Good enough to preserve as evidence, but not selected for reduced active candidates. |
| `wave3_3_raw_centered_shape_curve_aware` | `pause` | Useful diagnostic evidence for centered-shape loss, but not a next branch by itself. |
| `wave3_3_raw_offset_curve_aware` | `pause` | Similar to centered-shape variant; keep evidence, do not extend. |
| `wave3_3_full_curve_composite` | `retire` | More complex and weaker than the simpler curve-aware variants. |

### Robust, Probabilistic, And Mixture Models

| Family | Decision | Motivation |
| --- | --- | --- |
| `wave4_1` robust losses | `pause` | Robust losses are useful as loss-design evidence, but they do not beat the stronger candidates. |
| `wave4_2_gaussian_nll` | `baseline-only` | Keep one probabilistic baseline because it is simpler than MDN and close to the curve-aware branches. |
| `wave4_2_quantile_p10_p50_p90` | `pause` | Similar performance to Gaussian NLL but more output bookkeeping; not needed in the reduced set. |
| `wave4_3_mixture_density_k3` | `continue` | Best advanced probabilistic branch on both active surfaces. Keep one MDN representative. |
| `wave4_3_mixture_density_k2` | `pause` | K3 is slightly better on both active surfaces; K2 is redundant for near-term selection. |
| `wave4_4` latent-state / hysteresis | `retire` | The branch did not justify its added state complexity. Reopen only if new physical evidence requires hysteresis-specific modeling. |

### Harmonic-Prior And Dataset-Aware Waves

| Family | Decision | Motivation |
| --- | --- | --- |
| `wave5_1_harmonic_prior_pointwise_control` | `pause` | Compact and conceptually useful, but weaker than the selected harmonic comparators. |
| `wave5_1_harmonic_prior_smooth_l1_structured` | `pause` | Keep as compact harmonic-prior evidence; do not extend as an active branch now. |
| `wave52b_offset_centered_shape_harmonic` | `continue` | Not a standalone leader, but it is the clearest current evidence that offset, centered shape, and harmonic guidance should feed Wave 5.2C / Wave 6 design. |
| Other Wave 5.2B ablations | `retire` | `offset_centered_shape_harmonic` won the internal ablation; weaker ablations are no longer needed. |

### Pre-Polished Track 2 Variants

| Family | Decision | Motivation |
| --- | --- | --- |
| old `track2f`, `track2g`, `track2h` directional candidates | `retire` | They are superseded by polished reruns or by later families. Several old forward rows are catastrophically worse under the current matrix and should not shape near-term selection. |
| old `track2h` global-only conclusions | `pause` | Global is explicitly paused. Preserve the evidence, but exclude it from current decisions. |

## Simplified Decision Policy

The next model-development discussion should use this reduced hierarchy:

1. `periodic_gru_sequence` is the primary deployable neural family.
2. `rcim_retuned_GBM19_Fw` and `polished_rcim_ET19_Fw` are forward reference
   anchors, not new development branches.
3. `periodic_mlp_harmonic` is the lightweight harmonic comparator.
4. `wave4_3_mixture_density_k3` is the only advanced uncertainty branch to
   keep active.
5. `wave52b_offset_centered_shape_harmonic` is an integration ingredient for
   Wave 5.2C / Wave 6, not a standalone promoted model.
6. Plain `feedforward`, `tree`, and `harmonic_regression` stay only as anchors.
7. All `global` reasoning is paused until the last backlog stage.

## Proposed Reduced Pipeline Shape

If a new reduced `TE Curve Verification Pipeline` package is prepared later,
it should start with these forward/backward candidates only:

- `rcim_retuned_GBM19_Fw` and `rcim_retuned_GBM19_Bw`;
- `polished_rcim_model_bank_reproduction_ET19_Fw` and the best available
  polished RCIM backward reference-bank candidate for traceability;
- `polished_periodic_gru_sequence_Fw` and `polished_periodic_gru_sequence_Bw`;
- `polished_periodic_mlp_harmonic_Fw` and
  `polished_periodic_mlp_harmonic_Bw`;
- `polished_wave4_3_mixture_density_k3_Fw` and
  `polished_wave4_3_mixture_density_k3_Bw`;
- `wave52b_offset_centered_shape_harmonic_Fw` and
  `wave52b_offset_centered_shape_harmonic_Bw`;
- optional anchors: `feedforward`, `tree`, and `harmonic_regression`.

That reduced run should report raw error, P95, centered-shape behavior, offset
behavior, harmonic / phase evidence, visual overlays, and artifact complexity.
It should not include `global` rows.

## Backward Divergence Notes

Backward does not overturn the forward-led pruning. It strengthens the case
for `periodic_gru_sequence`, because the polished periodic GRU is the strongest
accepted backward candidate.

The main divergence is that RCIM banks remain very strong forward references
but are not the best backward practical choice. The correct response is not to
drop RCIM evidence; it is to keep RCIM as forward/reference-bank evidence and
keep periodic GRU as the deployable neural baseline.

## Final Decision

The active model-development set is now:

- `periodic_gru_sequence`;
- `periodic_mlp_harmonic`;
- `wave4_3_mixture_density_k3`;
- `wave52b_offset_centered_shape_harmonic`;
- selected baseline anchors only.

All other families are paused, retired, or baseline-only as listed above. This
is sufficient to continue the work without carrying every historical model
family into the next step.
