# TE Program Status And Closeout Ledger

## Purpose

This document is the maintained official status ledger for the Transmission
Error modeling program. It replaces informal copied chat summaries with the
current repository-backed view of completed waves, `Track 2` diagnostics,
campaign closeouts, official verification decisions, and next modeling gates.

Update this ledger after every campaign or `Track 2` closeout that changes any
of these surfaces:

- accepted or exploratory direction-parallel leaders;
- scalar campaign winner, program winner, or registry status;
- official `Track 2` verification state;
- roadmap position for `Track 2H`, `Wave 3`, `Wave 4`, or later integration;
- closeout interpretation of offset, centered shape, amplitude, phase,
  dispersion, or harmonic structure.

## Current Snapshot

| Surface | Current Status |
| --- | --- |
| Program state | Active |
| Active campaign | None |
| Current scalar program winner | `te_periodic_gru_sequence_remote_Bw` |
| Current accepted forward Track 2 leader | `rcim_retuned_GBM19_Fw` |
| Current accepted backward Track 2 leader | `periodic_gru_sequence_Bw` |
| Current accepted global neural Track 2 leader | `periodic_gru_sequence_global` |
| Latest normal campaign closeout | `Wave 3` harmonic-prior residual campaign |
| Latest official Track 2 refresh | `Wave 3` harmonic-prior residual refresh, dated `2026-06-15` |
| Latest Track 2 decision | verified exploratory baseline; not promoted |
| Next modeling decision | use `Wave 3` curve evidence to decide between more `Wave 3`, `Wave 4`, or latent-state / hysteresis-aware work |

The repository remains direction-parallel. `Fw`, `Bw`, and `global` are not a
single destructive competition. Each surface keeps its own best candidate and
its own interpretation.

## Evaluation Boundary

The central modeling boundary has not changed:

- runtime inference may use the current point state, explicitly supported
  causal short history, and causal derived features;
- runtime inference may not use future curve samples, full-curve target means,
  centered windows containing future information, or post-hoc target
  statistics;
- offline training, diagnostics, checkpoint selection, visual comparison, and
  promotion decisions may use complete held-out TE curves as evaluation units.

This means that curve-first evaluation is valid and required, while
full-curve-dependent runtime corrections are not deployable unless they are
reformulated as causal predictors.

## Current Direction-Parallel Leaders

| Surface | Accepted Leader | Evidence | Interpretation |
| --- | --- | --- | --- |
| `Fw` | `rcim_retuned_GBM19_Fw` | Official `Track 2` MAE `0.001089 deg`, Mean `2.372%` | Strongest overall forward curve baseline remains paper-reference retuned. |
| `Bw` | `periodic_gru_sequence_Bw` | Official `Track 2` MAE `0.002392 deg`, Mean `5.466%` | Strongest accepted repository-owned backward candidate remains the periodic GRU sequence branch. |
| `global` | `periodic_gru_sequence_global` | Official global forward MAE `0.002777 deg`; global backward MAE `0.002630 deg` | Strongest accepted bidirectional neural candidate remains periodic GRU sequence. |
| scalar registry | `te_periodic_gru_sequence_remote_Bw` | Test MAE `0.002344 deg` | Scalar program winner is useful but does not replace Track 2 curve-first promotion. |

## Program Timeline

| Stage | Status | Main Result | Promotion Decision |
| --- | --- | --- | --- |
| Planning foundation | closed | TE roadmap, implementation backlog, and family priorities established. | Baseline governance accepted. |
| Wave 0 shared infrastructure | closed | Shared training infrastructure, smoke checks, registry roots, and artifact conventions established. | Infrastructure accepted. |
| Track 1 exact-paper and paper-reference bank | closed | Faithful RCIM model-bank and paper-reference comparison surface established. | Used as reference evidence, not reopened for all-green optimization. |
| Wave 1 structured baselines | closed | Feedforward, tree, harmonic regression, periodic MLP, and residual harmonic MLP families trained and exported. | Strong baselines retained; tree remains a scalar/static reference. |
| Wave 2 temporal entry | closed | Temporal convolution, GRU, and LSTM sequence families trained. | Verified baseline; periodic sequence work became more important in Wave 2B. |
| Wave 2B harmonic temporal hybrid | closed | Periodic temporal convolution, periodic GRU, and periodic LSTM trained across `global`, `Fw`, and `Bw`. | `periodic_gru_sequence_Bw` became the scalar program winner and accepted backward Track 2 leader. |
| Wave 2C residual harmonic temporal hybrid | closed | Sparse and dense residual harmonic GRU/LSTM variants tested. | Verified exploratory baseline; not promoted over Wave 2B. |
| Track 2B curve-first reranking | closed | Existing Track 2 matrix reranked by full-curve metrics. | Established curve-first comparison without new training. |
| Track 2C curve-payload diagnostics | closed | Peak-to-peak, harmonic amplitude/phase, derivative, smoothness, and closure diagnostics added. | Confirmed scalar metrics alone are insufficient. |
| Mean-centered Track 2 diagnostic | closed | Post-prediction curve mean-centering separated vertical offset from centered shape. | Offset emerged as a major raw-error component, but mean-centering is not a runtime correction. |
| Track 2D mean-offset full-matrix audit | closed | `111` candidates and `12,416` curves audited for raw error, offset, centered shape, amplitude, phase, and regimes. | Full-matrix evidence confirmed offset-limited and mixed-limited failure modes. |
| Track 2E offset-predictability feasibility | closed | Conservative causal grouping showed offset is partly predictable, especially by `direction_torque`. | Offset-only correction was judged insufficient; shape, amplitude, and phase remain active constraints. |
| Track 2F sequential residual-offset probe | closed | Learned causal residual-offset branch added over a base TE prediction. | Verified exploratory baseline; not promoted. |
| Track 2F-bis harmonic-offset probe | closed | Clean and harmonic residual-offset variants compared across three surfaces. | Harmonic forcing helped `Fw` and `Bw` but did not solve global balance; not promoted. |
| Track 2G curve-aware training | closed | Pointwise-control, raw-centered-shape, raw-offset, and full-curve-composite losses trained across three surfaces. | Verified exploratory baseline; not promoted. |
| Track 2H robust-loss probes | closed | `MAE`, `SmoothL1`, and `log-cosh` robust losses tested. | Verified exploratory baseline; backward robust loss was useful but not promoted. |
| Track 2H quantile / probabilistic probes | closed | Quantile `p10/p50/p90` and Gaussian NLL heads tested. | Verified exploratory baseline; global and backward scalar signals improved but not promoted. |
| Track 2H mixture-density heads | closed | `mdn_k2` and `mdn_k3` heads tested. | Verified exploratory baseline; best Track 2H backward branch so far, but not promoted. |
| Wave 3 harmonic-prior residual campaign | closed | First real lightweight harmonic-prior residual campaign completed six runs. | Normal campaign closeout accepted; scalar program winner unchanged. |
| Wave 3 official Track 2 refresh | closed | Six Wave 3 candidates added to the `159`-candidate official Track 2 matrix. | Verified exploratory baseline; not promoted. |
| Wave 4 PINN / MMT track | open design branch | MMT diagnostic and parameter inventory exist; feature and soft-constraint gates remain open. | Not campaign-ready. |
| Integrated multi-task / multi-head model | deferred | Intended to combine proven offset, low-frequency, centered-shape, uncertainty, mixture, and structured residual mechanisms. | Deferred until Track 2H, Wave 3, and Wave 4 evidence identifies what should be integrated. |

## Track 2B Through Track 2H Interpretation

`Track 2B` changed the evaluation perspective. The repository no longer treats
pointwise scalar regression metrics as the only model-selection objective.
The practical target is TE compensation along continuous motor-curve sequences,
while preserving causal runtime inputs.

`Track 2C` made the curve payload diagnostic rather than only aggregate. It
added physical curve-quality measures such as peak-to-peak behavior, harmonic
amplitude, harmonic phase, derivative behavior, smoothness, autocorrelation,
closure mismatch, and stitched-boundary surrogates.

The mean-centered diagnostic and `Track 2D` separated offset from shape. Many
models follow centered shape better than raw MAE suggests, but a vertical DC
offset or compressed mean surface remains a major failure mode. The offset
finding is real, but subtracting the target curve mean after inference is only
a diagnostic decomposition.

`Track 2E` tested whether offset is causally predictable. The conservative
answer was partial yes, especially through `direction_torque`, but not enough
to justify an offset-only solution. A complete model still needs raw error,
centered shape, offset, amplitude, and phase to improve together.

`Track 2F` and `Track 2F-bis` implemented the first learned offset-aware
branches. The clean residual-offset model was a necessary control. The
harmonic version showed that harmonic structure helps direction-specific
branches, but global balance remains hard.

`Track 2G` tested curve-aware losses directly. The best scalar campaign
branches were:

| Surface | Best Track 2G Training Branch | Loss Profile | Test MAE |
| --- | --- | --- | ---: |
| `global` | `te_track2g_curve_aware_full_curve_composite_global` | `full_curve_composite` | 0.003345 |
| `Fw` | `te_track2g_curve_aware_raw_centered_shape_fw` | `raw_centered_shape` | 0.003181 |
| `Bw` | `te_track2g_curve_aware_pointwise_control_bw` | `pointwise_control` | 0.003430 |

The official Track 2 refresh accepted Track 2G as an exploratory baseline, not
as a promoted leader. The main lesson is that curve-aware losses are useful
but not automatically better on every surface.

`Track 2H` moved from deterministic curve-aware losses to dispersion-aware
training pressure:

| Package | Branch Count | Strongest Scalar Signal | Official Track 2 Outcome |
| --- | ---: | --- | --- |
| robust losses | 9 | `te_track2h_smooth_l1_robust_bw`, test MAE `0.003074` | exploratory, not promoted |
| quantile / probabilistic | 6 | `te_track2h_quantile_p10_p50_p90_bw`, test MAE `0.002927` | exploratory, not promoted |
| mixture density heads | 6 | `te_track2h_mdn_k2_bw`, test MAE `0.002658` | exploratory, not promoted |

The strongest Track 2H result is backward and useful, but MDN diagnostics
mostly collapsed toward one effective component. The evidence supports keeping
MDN and probabilistic heads as later ingredients, not treating them as a
confirmed multimodal TE solution.

## Wave 3 Interpretation

The first real `Wave 3` harmonic-prior residual campaign validated a compact
structured branch with only `7,283` trainable parameters. All six runs
completed successfully:

| Surface | Best Wave 3 Training Branch | Profile | Test MAE | Track 2 MAE |
| --- | --- | --- | ---: | ---: |
| `global` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `smooth_l1_structured` | 0.003403 | 0.003399 |
| `Fw` | `te_wave3_harmonic_prior_residual_pointwise_control_fw` | `pointwise_control` | 0.003382 | 0.003374 |
| `Bw` | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `pointwise_control` | 0.003363 | 0.003360 |

Wave 3 is cleanly implemented and verified as an exploratory baseline. It is
not a program winner and does not replace the accepted Track 2 leaders. Its
value is architectural: it tests whether a compact harmonic prior plus learned
residual can become a useful building block for later structured or multi-head
models.

## Current Next Steps

1. Use the completed Wave 3 Track 2 curve, offset, collage, and overlay
   evidence to decide whether to continue Wave 3, move to Wave 4, or reopen
   latent-state / hysteresis-aware modeling.
2. Keep `Track 2H` robust, probabilistic, and MDN branches as evidence for
   later multi-head integration, not as current promoted leaders.
3. Keep `Wave 4` MMT/PINN work behind its dataset-aligned diagnostic and
   calibration gates.
4. Do not open the integrated multi-task / multi-head campaign until the
   chosen ingredients are justified by Track 2 curve evidence.

## Closeout Update Rule

Every future campaign closeout must check this ledger before closure is
declared complete. Update it when the closeout:

- completes a new campaign, wave, Track 2 diagnostic, or official Track 2
  verification refresh;
- changes the scalar program winner, a direction-parallel accepted leader, or
  an exploratory branch leader;
- adds evidence about offset, centered shape, amplitude, phase, dispersion,
  harmonic grouping, latent state, physics constraints, or deployment
  readiness;
- changes the next recommended modeling branch.

If a closeout does not affect this ledger, the closeout report should state
that the ledger was checked and did not require a content change.

## Canonical Sources

- `doc/running/active_training_campaign.yaml`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-06-15]/track2_official_model_verification_report.md`
- `doc/reports/campaign_results/wave3_wave4/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md`
- `doc/reports/campaign_results/track2/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md`
- `doc/reports/campaign_results/track2/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md`
- `doc/reports/campaign_results/track2/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md`
- `doc/reports/campaign_results/track2/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md`
