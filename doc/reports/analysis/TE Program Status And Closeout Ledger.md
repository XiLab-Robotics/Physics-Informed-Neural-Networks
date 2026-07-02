# TE Program Status And Closeout Ledger

## Purpose

This document is the maintained official status ledger for the Transmission
Error modeling program. It replaces informal copied chat summaries with the
current repository-backed view of completed waves,
`TE Curve Verification Pipeline` diagnostics, campaign closeouts, official
verification decisions, and next modeling gates.

Update this ledger after every campaign or `TE Curve Verification Pipeline`
closeout that changes any of these surfaces:

- accepted or exploratory direction-parallel leaders;
- scalar campaign winner, program winner, or registry status;
- official `TE Curve Verification Pipeline` verification state;
- roadmap position for Waves `4.1`-`4.4`, `Wave 5.1`, `Wave 5.2`, or later
  integration;
- closeout interpretation of offset, centered shape, amplitude, phase,
  dispersion, or harmonic structure.

## Current Snapshot

| Surface | Current Status |
| --- | --- |
| Program state | Active |
| Active campaign | None locally; `polished_dataset_full_wave_retraining_2026_06_22` remains externally active on another workstation |
| Current scalar program winner | `te_periodic_gru_sequence_bw` |
| Current accepted forward curve-verified leader | `rcim_retuned_GBM19_Fw` |
| Current accepted backward curve-verified leader | `periodic_gru_sequence_Bw` |
| Current accepted global neural curve-verified leader | `periodic_gru_sequence_global` |
| Latest normal campaign closeout | `Wave 5.2B` offset and harmonic guided campaign |
| Latest official TE Curve Verification refresh | `Wave 5.2B` offset and harmonic guided refresh, dated `2026-07-02` |
| Latest curve-verification decision | pending operator review; no automatic promotion |
| Current TE Curve Verification Pipeline selection policy | multi-index curve-first selection, dated `2026-06-16` |
| Next modeling decision | keep the externally running full-wave `polished_dataset` retraining campaign isolated; review the completed Wave 5.2B curve-first evidence before opening `Wave 5.2C` dirty-to-clean transfer |

The repository remains direction-parallel. `Fw`, `Bw`, and `global` are not a
single destructive competition. Each surface keeps its own best candidate and
its own interpretation.

## Canonical Program Taxonomy

| Program layer | Canonical scope |
| --- | --- |
| RCIM Model-Bank Reproduction | Paper-faithful RCIM harmonic model-bank reproduction and reference comparison. |
| Model Development Waves | Model training and experimental architecture development. |
| TE Curve Verification Pipeline | Offline curve reconstruction, diagnostics, multi-index selection, visual evidence, and reports. |

| Identifier | Canonical module or model branch |
| --- | --- |
| `CVP 1.1` | Curve-First Reranking |
| `CVP 1.2` | Curve Payload Diagnostics |
| `CVP 1.3` | Mean-Centered Error Decomposition |
| `CVP 1.4` | Offset and Shape Matrix Audit |
| `CVP 1.5` | Causal Offset Feasibility Analysis |
| `Wave 3.1` | Residual Offset Models |
| `Wave 3.2` | Harmonic Residual Offset Models |
| `Wave 3.3` | Curve-Aware Objective Models |
| `Wave 4.1` | Robust-Loss Models |
| `Wave 4.2` | Quantile and Probabilistic Models |
| `Wave 4.3` | Mixture-Density Models |
| `Wave 4.4` | Latent-State and Hysteresis Models |
| `Wave 5.1` | Harmonic-Prior Residual Models |
| `Wave 5.2` | Dataset-Aware MMT/PINN-Guided Models |
| `Wave 6` | Integrated Multi-Task, Multi-Head, and Transfer Models |

Historical paths, run names, model-family keys, and script names retain their
legacy `track1`, `track2`, `wave3`, or `wave4` identifiers where changing them
would break reproducibility.

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

Official `TE Curve Verification Pipeline` decisions now use the multi-index
curve-first policy in
`doc/reports/analysis/track2/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`.
Raw `MAE`, `RMSE`, and mean percentage error remain required evidence, but they
do not by themselves decide promotion. Future reports must keep separate
raw-error, mean-centered shape, offset / continuity, harmonic / phase,
robustness, visual-evidence, and deployment-readiness axes visible.

## Current Direction-Parallel Leaders

| Surface | Accepted Leader | Evidence | Interpretation |
| --- | --- | --- | --- |
| `Fw` | `rcim_retuned_GBM19_Fw` | Official `TE Curve Verification Pipeline` MAE `0.001089 deg`, Mean `2.372%` | Strongest overall forward curve baseline remains paper-reference retuned. |
| `Bw` | `periodic_gru_sequence_Bw` | Official `TE Curve Verification Pipeline` MAE `0.002392 deg`, Mean `5.466%` | Strongest accepted repository-owned backward candidate remains the periodic GRU sequence branch. |
| `global` | `periodic_gru_sequence_global` | Official global forward MAE `0.002777 deg`; global backward MAE `0.002630 deg` | Strongest accepted bidirectional neural candidate remains periodic GRU sequence. |
| scalar registry | `te_periodic_gru_sequence_bw` | Test MAE `0.001084 deg` on `polished_dataset` early-wave parallel training | Scalar program winner is useful but does not replace TE Curve Verification Pipeline curve-first promotion. |

## Program Timeline

| Stage | Status | Main Result | Promotion Decision |
| --- | --- | --- | --- |
| Planning foundation | closed | TE roadmap, implementation backlog, and family priorities established. | Baseline governance accepted. |
| Wave 0 shared infrastructure | closed | Shared training infrastructure, smoke checks, registry roots, and artifact conventions established. | Infrastructure accepted. |
| RCIM Model-Bank Reproduction exact-paper and paper-reference bank | closed | Faithful RCIM model-bank and paper-reference comparison surface established. | Used as reference evidence, not reopened for all-green optimization. |
| Wave 1 structured baselines | closed | Feedforward, tree, harmonic regression, periodic MLP, and residual harmonic MLP families trained and exported. | Strong baselines retained; tree remains a scalar/static reference. |
| Wave 2.1 temporal entry | closed | Temporal convolution, GRU, and LSTM sequence families trained. | Verified baseline; periodic sequence work became more important in Wave 2.2. |
| Wave 2.2 harmonic temporal hybrid | closed | Periodic temporal convolution, periodic GRU, and periodic LSTM trained across `global`, `Fw`, and `Bw`. | `periodic_gru_sequence_Bw` became the scalar program winner and accepted backward curve-verified leader. |
| Wave 2.3 residual harmonic temporal hybrid | closed | Sparse and dense residual harmonic GRU/LSTM variants tested. | Verified exploratory baseline; not promoted over Wave 2.2. |
| CVP 1.1 curve-first reranking | closed | Existing curve-verification matrix reranked by full-curve metrics. | Established curve-first comparison without new training. |
| CVP 1.2 curve-payload diagnostics | closed | Peak-to-peak, harmonic amplitude/phase, derivative, smoothness, and closure diagnostics added. | Confirmed scalar metrics alone are insufficient. |
| CVP 1.3 mean-centered error decomposition | closed | Post-prediction curve mean-centering separated vertical offset from centered shape. | Offset emerged as a major raw-error component, but mean-centering is not a runtime correction. |
| CVP 1.4 mean-offset full-matrix audit | closed | `111` candidates and `12,416` curves audited for raw error, offset, centered shape, amplitude, phase, and regimes. | Full-matrix evidence confirmed offset-limited and mixed-limited failure modes. |
| CVP 1.5 offset-predictability feasibility | closed | Conservative causal grouping showed offset is partly predictable, especially by `direction_torque`. | Offset-only correction was judged insufficient; shape, amplitude, and phase remain active constraints. |
| Wave 3.1 sequential residual-offset probe | closed | Learned causal residual-offset branch added over a base TE prediction. | Verified exploratory baseline; not promoted. |
| Wave 3.2 harmonic-offset probe | closed | Clean and harmonic residual-offset variants compared across three surfaces. | Harmonic forcing helped `Fw` and `Bw` but did not solve global balance; not promoted. |
| Wave 3.3 curve-aware training | closed | Pointwise-control, raw-centered-shape, raw-offset, and full-curve-composite losses trained across three surfaces. | Verified exploratory baseline; not promoted. |
| Wave 4.1 robust-loss probes | closed | `MAE`, `SmoothL1`, and `log-cosh` robust losses tested. | Verified exploratory baseline; backward robust loss was useful but not promoted. |
| Wave 4.2 quantile / probabilistic probes | closed | Quantile `p10/p50/p90` and Gaussian NLL heads tested. | Verified exploratory baseline; global and backward scalar signals improved but not promoted. |
| Wave 4.3 mixture-density heads | closed | `mdn_k2` and `mdn_k3` heads tested. | Verified exploratory baseline; best Wave 4 backward branch so far, but not promoted. |
| Wave 4.4 latent-state hysteresis probes | closed | GRU and causal-TCN offset-residual probes completed across `global`, `Fw`, and `Bw`; official TE Curve Verification refresh added six candidates to the `165`-candidate matrix. | Verified exploratory baseline; not promoted over `rcim_retuned_GBM19_Fw`, `periodic_gru_sequence_Bw`, or the accepted global neural `periodic_gru_sequence_global`. |
| Wave 5.1 harmonic-prior residual campaign | closed | First real lightweight harmonic-prior residual campaign completed six runs. | Normal campaign closeout accepted; scalar program winner unchanged. |
| Wave 5.1 official TE Curve Verification refresh | closed | Six Wave 5.1 candidates added to the `159`-candidate official curve-verification matrix. | Verified exploratory baseline; not promoted. |
| Polished-dataset Stage 1 smoke | closed | Eight representative non-paper-original model families trained successfully on `polished_dataset`; best scalar run `te_periodic_gru_sequence_remote_global`, test MAE `0.001279 deg`. | Normal campaign closeout accepted; scalar registry changed, but official curve-verified leaders unchanged pending separate TE Curve Verification Pipeline refresh. |
| Polished-dataset early-wave parallel training | closed | Thirty-six early-wave model-development runs completed across `global`, `Fw`, and `Bw`; best scalar run `te_periodic_gru_sequence_bw`, test MAE `0.001084 deg`. | Normal campaign closeout accepted; scalar registry changed, but official curve-verified leaders unchanged pending separate TE Curve Verification Pipeline refresh. |
| Polished-dataset RCIM Model-Bank Reproduction | closed | Forward and backward paper-faithful RCIM model banks completed on `polished_dataset`; ERT won both surfaces, with `190` Python and `190` ONNX exports per direction. | Normal campaign closeout accepted; official curve-verified leaders unchanged because TE Curve Verification Pipeline refresh remains a separate optional workflow. |
| Polished-dataset full-wave retraining | externally active | The 108-run full-wave polished retraining campaign is operator-reported as running on another workstation. | Do not close out, refresh, or reinterpret polished final-model evidence from this checkout until completion artifacts are synchronized. |
| Wave 5.2 dataset-aware PINN / MMT track | closed scalar campaign branch | MMT diagnostic, parameter inventory, and full paired-dataset diagnostic exist; the branch now separates clean polished modeling, simplified noise-aware diagnostics, and paired dirty-to-clean or transfer tests. `Wave 5.2B` completed `12` polished offset/harmonic guided runs with `0` failures; `offset_centered_shape_harmonic` won `global`, `Fw`, and `Bw`. | Normal campaign closeout accepted; scalar program winner and official curve-verified leaders unchanged. |
| Wave 5.2B official TE Curve Verification refresh | pending human review | Three Wave 5.2B harmonic-profile candidates were added to the `168`-candidate official matrix; strongest refreshed candidate is `wave52b_offset_centered_shape_harmonic_Fw` with MAE `0.001695 deg` and Mean `3.391%`. | No automatic promotion; accepted curve-verified leaders remain unchanged until human review records a promotion decision. |
| Wave 6 integrated multi-task / multi-head / transfer model | deferred | Intended to combine proven offset, low-frequency, centered-shape, uncertainty, mixture, structured residual, dirty-to-clean, reduced-point, and fine-tuning mechanisms. | Deferred until full-wave polished evidence, paired dataset diagnostics, Waves 4.1-4.4, Wave 5.1, and Wave 5.2 identify what should be integrated. |

## Dataset-Aware Roadmap

Future `Wave 5.2` and `Wave 6` work must not treat the old
`simplified_dataset` evidence and the new `polished_dataset` evidence as the
same modeling surface.

The revised branch structure is:

| Branch | Dataset role | Purpose |
| --- | --- | --- |
| Clean deployment branch | `polished_dataset` is the primary surface. | Final comparable model selection, curve-first promotion, and deployment-oriented decisions after full-wave retraining and `TE Curve Verification Pipeline` refresh. |
| Noise-aware research branch | `simplified_dataset` is retained as the dirty or disturbed diagnostic surface. | Test whether robust losses, structured constraints, PINN-style soft losses, and multi-task denoising can handle offset, noise, and fragile curve regions. |
| Cross-dataset transfer branch | Paired `simplified_dataset` and `polished_dataset` evidence. | Evaluate backbone pretraining, fine-tuning on polished data, dirty-to-clean heads, and reduced-point robustness. |

The full `Wave 5.2A` paired diagnostic is available at
`doc/reports/analysis/wave5_2/paired_dataset_diagnostics/[2026-07-01]/wave52a_paired_dataset_diagnostics.md`.
It confirms and evaluates all `1938` paired directional records. The matrix
keeps peak-to-peak and smoothness deltas near zero, while mean absolute offset
delta is `0.003216838 deg`; classification finds `901` offset-shifted pairs,
`944` nonzero-harmonic changed pairs, `65` nearly identical pairs, `27`
sampling anomalies, and `1` smoothness-changed pair. It is a
dataset-alignment and noise-awareness artifact, not a training result and not
a `TE Curve Verification Pipeline` promotion.

The polishing workflow may be used as an offline diagnostic specification, but
future deployable models must not copy non-causal or full-curve cleaning logic
into runtime inference. Ideas from the polishing process should be translated
only into leakage-safe train-time losses, auxiliary heads, masks, or
diagnostic metrics.

## CVP Modules And Waves 3.1 Through 4.4

`CVP 1.1` changed the evaluation perspective. The repository no longer treats
pointwise scalar regression metrics as the only model-selection objective.
The practical target is TE compensation along continuous motor-curve sequences,
while preserving causal runtime inputs.

The `2026-06-16` multi-index policy formalizes that shift. Future official
reports should identify best raw-error, best shape-fidelity, best
offset-behavior, best robustness, and recommended candidates per `global`,
`Fw`, and `Bw` surface. A candidate can be valuable on one axis without being
the final recommended compensator.

`CVP 1.2` made the curve payload diagnostic rather than only aggregate. It
added physical curve-quality measures such as peak-to-peak behavior, harmonic
amplitude, harmonic phase, derivative behavior, smoothness, autocorrelation,
closure mismatch, and stitched-boundary surrogates.

The mean-centered diagnostic and `CVP 1.4` separated offset from shape. Many
models follow centered shape better than raw MAE suggests, but a vertical DC
offset or compressed mean surface remains a major failure mode. The offset
finding is real, but subtracting the target curve mean after inference is only
a diagnostic decomposition.

`CVP 1.5` tested whether offset is causally predictable. The conservative
answer was partial yes, especially through `direction_torque`, but not enough
to justify an offset-only solution. A complete model still needs raw error,
centered shape, offset, amplitude, and phase to improve together.

`Wave 3.1` and `Wave 3.2` implemented the first learned offset-aware
branches. The clean residual-offset model was a necessary control. The
harmonic version showed that harmonic structure helps direction-specific
branches, but global balance remains hard.

`Wave 3.3` tested curve-aware losses directly. The best scalar campaign
branches were:

| Surface | Best Wave 3.3 Training Branch | Loss Profile | Test MAE |
| --- | --- | --- | ---: |
| `global` | `te_track2g_curve_aware_full_curve_composite_global` | `full_curve_composite` | 0.003345 |
| `Fw` | `te_track2g_curve_aware_raw_centered_shape_fw` | `raw_centered_shape` | 0.003181 |
| `Bw` | `te_track2g_curve_aware_pointwise_control_bw` | `pointwise_control` | 0.003430 |

The official TE Curve Verification refresh accepted Wave 3.3 as an exploratory baseline, not
as a promoted leader. The main lesson is that curve-aware losses are useful
but not automatically better on every surface.

`Wave 4 series` moved from deterministic curve-aware losses to dispersion-aware
training pressure:

| Package | Branch Count | Strongest Scalar Signal | Official TE Curve Verification Pipeline Outcome |
| --- | ---: | --- | --- |
| robust losses | 9 | `te_track2h_smooth_l1_robust_bw`, test MAE `0.003074` | exploratory, not promoted |
| quantile / probabilistic | 6 | `te_track2h_quantile_p10_p50_p90_bw`, test MAE `0.002927` | exploratory, not promoted |
| mixture density heads | 6 | `te_track2h_mdn_k2_bw`, test MAE `0.002658` | exploratory, not promoted |
| latent-state hysteresis | 6 | `te_track2h_l_causal_tcn_offset_residual_global`, test MAE `0.003368` | exploratory, not promoted |

The strongest Wave 4 series result is backward and useful, but MDN diagnostics
mostly collapsed toward one effective component. The evidence supports keeping
MDN and probabilistic heads as later ingredients, not treating them as a
confirmed multimodal TE solution.

`Wave 4.4` added the causal latent-state / hysteresis-aware probe. The best
scalar branch was `te_track2h_l_causal_tcn_offset_residual_global` with test
MAE `0.003368 deg`. The official `2026-06-18` TE Curve Verification refresh added six
`Wave 4.4` candidates to the `165`-candidate matrix. The strongest
refreshed candidates were `track2h_l_causal_tcn_offset_residual_global`
combined curve MAE `0.003372 deg`,
`track2h_l_causal_tcn_offset_residual_Fw` forward curve MAE `0.003476 deg`,
and `track2h_l_gru_offset_residual_Bw` backward curve MAE `0.003542 deg`.
Those results are useful causal-history evidence, but they do not improve the
accepted `Fw`, `Bw`, or `global` curve-verified leaders. The branch is closed as a
verified exploratory baseline and should be carried forward only as later
integration evidence.

## Wave 5.1 Interpretation

The first real `Wave 5.1` harmonic-prior residual campaign validated a compact
structured branch with only `7,283` trainable parameters. All six runs
completed successfully:

| Surface | Best Wave 5.1 Training Branch | Profile | Test MAE | curve-verification MAE |
| --- | --- | --- | ---: | ---: |
| `global` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `smooth_l1_structured` | 0.003403 | 0.003399 |
| `Fw` | `te_wave3_harmonic_prior_residual_pointwise_control_fw` | `pointwise_control` | 0.003382 | 0.003374 |
| `Bw` | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `pointwise_control` | 0.003363 | 0.003360 |

Wave 5.1 is cleanly implemented and verified as an exploratory baseline. It is
not a program winner and does not replace the accepted curve-verified leaders. Its
value is architectural: it tests whether a compact harmonic prior plus learned
residual can become a useful building block for later structured or multi-head
models.

## Current Next Steps

1. Wait for the externally running full-wave `polished_dataset` retraining
   campaign to finish and be synchronized before polished closeout or official
   `TE Curve Verification Pipeline` refresh work.
2. Keep `Wave 4.1` robust, probabilistic, MDN, and latent-state branches as
   evidence for later multi-head integration, not as current promoted leaders.
3. Treat `Wave 5.2B` as completed scalar and curve-first evidence for the
   dataset-aware MMT/PINN-guided branch. The `2026-07-02` closeout shows that
   `offset_centered_shape_harmonic` is the best Wave 5.2B scalar profile on
   all surfaces, and the `2026-07-02` official `TE Curve Verification
   Pipeline` refresh identifies `wave52b_offset_centered_shape_harmonic_Fw`
   as the strongest refreshed curve candidate. No promotion is recorded until
   a human review applies the multi-index curve-first policy.
4. Defer `Wave 6` until the full-wave polished results, paired dataset
   diagnostics, and `Wave 5.2` evidence identify which heads, constraints, and
   transfer strategy are justified.

## Closeout Update Rule

Every future campaign closeout must check this ledger before closure is
declared complete. Update it when the closeout:

- completes a new campaign, wave, TE Curve Verification Pipeline diagnostic, or official TE Curve Verification Pipeline
  verification refresh;
- changes the scalar program winner, a direction-parallel accepted leader, or
  an exploratory branch leader;
- changes the multi-index raw-error, shape-fidelity, offset-behavior,
  robustness, or recommended candidate for any `TE Curve Verification Pipeline` surface;
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
- `doc/reports/analysis/track2/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-06-18]/track2_official_model_verification_report.md`
- `doc/reports/campaign_results/cross_wave/polished_dataset/2026-06-29-10-40-05_polished_early_wave_parallel_training_campaign_results_report.md`
- `doc/reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md`
