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
| Active campaign | None; the Wave 5.2R integrated-specialist campaign completed normal closeout and its protected-file list is cleared |
| Current scalar program winner | `te_periodic_gru_sequence_bw` |
| Current accepted forward curve-verified leader | `rcim_retuned_GBM19_Fw`; polished refreshed-source leader `polished_rcim_model_bank_reproduction_ET19_Fw`; polished model-development fallback `polished_periodic_gru_sequence_Fw` |
| Current accepted backward curve-verified leader | `polished_periodic_gru_sequence_Bw` |
| Current accepted global neural curve-verified leader | `polished_periodic_gru_sequence_global` |
| Latest normal campaign closeout | Wave 5.2R integrated-specialist campaign, `24 / 24` entries completed on `2026-08-03` with zero failures; A02 is the only gate-qualified branch and A04 is an unpromoted failed-gate scalar winner |
| Latest non-training tournament closeout | Wave 5.2R Stage 15 completed the official 97-curve forward comparison. H04 led centered shape, derivative, and mean harmonic phase, but the accepted GRU retained raw, P95, offset, and peak-to-peak leadership. H04 remains exploratory and no registry changed. |
| Latest non-training PINN gate | Phase 15 audited four evidence files and all five physics-integrated Wave 6 prerequisites; all five fail, so the sixteen-phase roadmap closed without training or automatic advancement |
| Latest official TE Curve Verification refresh | Wave 5.2R K01/H08 cross-surface refresh, dated `2026-07-31`; `24` candidates evaluated separately on `97` Fw, `97` Bw, and `194` global curves, followed by CVP 1.2 diagnostics and visual review |
| Latest curve-verification decision | K01 seed `271828` is promoted as the cross-surface temporal offline leader. H08 remains a forward non-temporal specialist and fails global promotion because of backward/global raw and offset regressions. Periodic GRU and periodic harmonic MLP remain accepted unchanged. |
| Latest non-training defect diagnostic | The `2026-08-02` frozen-payload H08 analysis confirms an offset-dominant backward defect and global-fit interference on both direction subsets. H08 remains the non-temporal `Fw` offline specialist; no checkpoint or registry changed. |
| Latest deployment-preparation gate | K01 and H08 passed local replay, causal/state, ONNX-parity, fallback, and host-latency gates. TwinCAT runtime and cross-surface acceptance remain pending. |
| Latest curated model-archive refresh | Five Wave 5.2R leaves were added on `2026-07-31`: K01 seed `271828` for `Fw`, `Bw`, and `global`; H08 seed `161803` for `Fw`; and exploratory Stage 15 H04 for `Fw`. The polished-setpoint aggregate now contains `113` leaves. Archive preservation does not change accepted registries or deployment leaders. |
| Latest pruning decision | `2026-07-17` shape-first intermediate model-selection cleanup; `global` remains paused until final backlog stage |
| Active report generation | six reduced selected-model reports completed for polished setpoints, simplified setpoints, and polished actual values, each split into `forward` and `backward` |
| Current TE Curve Verification Pipeline selection policy | multi-index curve-first selection, dated `2026-06-16` |
| Next modeling decision | Continue standalone TF3820 PLC qualification in parallel. Optionally prepare and operator-run the separate Fw/Bw/global TE Curve Verification Pipeline refresh for A02; do not promote A04 from scalar evidence. |

The repository remains direction-parallel. `Fw`, `Bw`, and `global` are not a
single destructive competition. Each surface keeps its own best candidate and
its own interpretation.

Near-term pruning temporarily pauses `global` model selection. This does not
delete the `global` branch or change its historical status. It only excludes
`global` from current model-family pruning and reduced-pipeline planning until
it is the final remaining modeling item in the backlog.

The `2026-07-17` intermediate cleanup adds a shape-first gate to that pruning
rule. Scalar leaders that smooth, shift, or lose the measured harmonic TE
shape are not active development roads. The practical consequence is that
`periodic_lstm_sequence_Bw` is demoted as a false scalar leader, while
`periodic_gru_sequence_Fw/Bw` remains the temporal-window path.

Routine `TE Curve Verification Pipeline` report generation is now reduced to
six selected-model reports: polished-setpoint, simplified-setpoint, and
polished-actual-values evidence, each split into forward and backward. Broad
full-matrix regeneration, `global` reports, overlay reports, and
simplified-vs-polished dataset-difference reports are paused and should be
regenerated only after an explicit request. The current reduced report bundle
is
`doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-24]/`.

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
| `Wave 5.2` | MMT/PINN-Guided Models: general full-PINN program active; MMT-paper-faithful subbranch deferred |
| `Wave 6` | Integrated Multi-Task and Multi-Head Models |

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
`doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`.
Raw `MAE`, `RMSE`, and mean percentage error remain required evidence, but they
do not by themselves decide promotion. Future reports must keep separate
raw-error, mean-centered shape, offset / continuity, harmonic / phase,
robustness, visual-evidence, and deployment-readiness axes visible.

## Current Direction-Parallel Leaders

| Surface | Accepted Leader | Evidence | Interpretation |
| --- | --- | --- | --- |
| `Fw` | `rcim_retuned_GBM19_Fw`; polished refreshed-source leader `polished_rcim_model_bank_reproduction_ET19_Fw`; model-development fallback `polished_periodic_gru_sequence_Fw` | Full-matrix official MAE `0.001089 deg`, Mean `2.372%` for `rcim_retuned_GBM19_Fw`; polished refresh MAE `0.001155 deg`, Mean `2.401%` for RCIM ET19; `0.001195 deg`, Mean `2.559%` for periodic GRU. | Historical retuned reference remains the full-matrix forward leader. RCIM ET19 is the strongest polished forward reference-bank candidate; periodic GRU is the strongest polished model-development forward candidate. |
| `Bw` | `polished_periodic_gru_sequence_Bw` | Official `2026-07-03` polished refresh MAE `0.001129 deg`, Mean `2.228%` | Strongest accepted polished backward and aggregate candidate. |
| `global` | `polished_periodic_gru_sequence_global` | Official `2026-07-03` polished refresh MAE `0.001279 deg`, Mean `2.636%` | Strongest accepted bidirectional polished model-development candidate. |
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
| Polished-dataset full-wave retraining | closed | One hundred eight full model-development runs completed across `36` families and `global`, `Fw`, and `Bw`; full-wave scalar winner `te_periodic_gru_sequence_fw`, test MAE `0.001121 deg`. | Normal campaign closeout accepted; scalar program winner remains the earlier polished early-wave `te_periodic_gru_sequence_bw` at `0.001084 deg`; official curve-verified leaders unchanged pending separate TE Curve Verification Pipeline refresh. |
| Polished-dataset official TE Curve Verification refresh | closed | `128` polished RCIM and model-development candidates added to the official `293`-candidate matrix using `data\polished_dataset`; visual collage, overlay, official report, and PDFs regenerated. | Accepted. `polished_periodic_gru_sequence` becomes the model-development baseline; `rcim_retuned_GBM19_Fw` remains the full-matrix forward leader; `polished_rcim_model_bank_reproduction_ET19_Fw` is retained as the polished refreshed-source forward reference-bank leader. |
| Intermediate model-selection cleanup | closed | Post-retraining familywise ONNX reports were consolidated into a shape-first selection report using `polished_dataset + setpoints` as the primary evidence surface and `polished_dataset + actual_values` as a sensitivity check. | Active development set reduced to `periodic_gru_sequence`, `wave4_1_mae_robust_loss`, `wave4_2_quantile_p10_p50_p90`, and `periodic_mlp_harmonic`; `periodic_lstm_sequence_Bw`, Wave 4.3 MDN, Wave 4.4 latent-state, and Wave 5.1 harmonic-prior branches are closed as active roads unless future shape-gated evidence reopens them. |
| Shape-gate loss pilot patched Track 2 expansion | closed diagnostic | Corrected polished setpoint playback was used to compare the one-run shape-gate loss pilot against the reduced active polished-setpoint Fw/Bw candidate set and to generate bounded Track 2 plots. | The pilot is viable but not promoted: `polished_setpoints_periodic_gru_sequence_Fw` remains the forward recommendation, `polished_setpoints_periodic_mlp_harmonic_Bw` is the backward recommendation, and the pilot ranks fifth on forward. The next training step should be a stricter second pilot or checkpoint-selection variant, not a full Aries campaign from this exact profile. |
| Shape-gate loss v2 checkpoint-selection pilot | closed pilot | One remote `polished_dataset` setpoint `Fw` run completed successfully; best checkpoint `periodic_gru_sequence-epoch=008-val_mae=0.00198279.ckpt`, validation MAE `0.001983 deg`, test MAE `0.001463 deg`. | Accepted as a completed pilot and scalar improvement over the first shape-gate loss pilot. Not promoted until a bounded checkpoint-level `TE Curve Verification Pipeline` screen and calibrated shape-gated reranker confirm curve-shape, harmonic, derivative, and phase behavior. |
| Shape-gate loss v2 bounded Track 2 screen | closed diagnostic | Remote bounded `polished_dataset` setpoint `Fw` screen completed on `2026-07-21`; matrix evaluated 9 candidates over 100 forward held-out curves and the shape-gated reranker wrote `2026-07-21-16-04-28__shape_gated_te_curve_reranker`. | Not promoted. `polished_setpoints_periodic_gru_sequence_Fw` remains the forward recommendation; shape-gate loss v2 ranks fifth by composite score (`0.541641`) with raw MAE `0.001973 deg`, centered MAE `0.001541 deg`, and shape pass rate `0.960`. It improves over the first shape-gate loss pilot but does not justify full-matrix expansion. |
| Parallel shape-objective follow-up | closed pilot | Three remote `polished_dataset` setpoint `Fw` arms completed: windowed GRU, non-windowed MLP, and curve-aware residual. The non-windowed `shape_objective_periodic_mlp_harmonic_fw` arm won the scalar pilot with validation MAE `0.001429 deg` and test MAE `0.001236 deg`; the closeout report includes pilot graphs and validated PDF export. | Accepted as the next bounded screen candidate, not promoted. The result argues against continuing the v3 windowed GRU branch as the immediate road and reopens the non-windowed `periodic_mlp_harmonic` road only behind a bounded curve-first screen against both windowed and non-windowed references. |
| Shape-objective bounded Track 2 screen | closed diagnostic | Remote bounded `polished_dataset` setpoint `Fw` screen completed on `2026-07-22`; matrix evaluated 3 candidates over 100 forward held-out curves and the shape-gated reranker wrote `2026-07-22-12-16-27__shape_gated_te_curve_reranker`. | Not promoted. `polished_setpoints_periodic_gru_sequence_Fw` remains recommended with raw MAE `0.001837 deg`, centered MAE `0.001483 deg`, and shape pass rate `0.950`; `shape_objective_periodic_mlp_harmonic_Fw` ranked third with raw MAE `0.002035 deg`, centered MAE `0.001578 deg`, and shape pass rate `0.910`. The scalar pilot win did not survive curve-first validation. |
| Shape-first training-rule distillation pilot | closed pilot | Two remote `polished_dataset` setpoint `Fw` arms completed: time-windowed `shape_first_distilled_periodic_gru_sequence_fw` and non-windowed `shape_first_distilled_periodic_mlp_harmonic_fw`. The non-windowed harmonic MLP won scalar selection with validation MAE `0.001573 deg` and test MAE `0.001420 deg`; the time-windowed GRU retained better test offset and amplitude losses. | Accepted as a completed pilot, not promoted. The next step is a bounded `TE Curve Verification Pipeline` screen against both `polished_setpoints_periodic_gru_sequence_Fw` and `polished_setpoints_periodic_mlp_harmonic_Fw`, keeping both time-windowed and non-windowed roads alive until curve-first evidence separates them. |
| Shape-first distillation bounded Track 2 screen | closed diagnostic | Remote bounded `polished_dataset` setpoint `Fw` screen completed on `2026-07-22`; matrix evaluated 4 candidates over 100 forward held-out curves, generated 8 measured-vs-predicted Track 2 plots, and the shape-gated reranker wrote `2026-07-22-15-59-37__shape_gated_te_curve_reranker`. | Not promoted. `polished_setpoints_periodic_gru_sequence_Fw` remains recommended with raw MAE `0.001837 deg`, centered MAE `0.001483 deg`, and shape pass rate `0.950`; the non-windowed distillation scalar winner ranked fourth with raw MAE `0.002079 deg`, centered MAE `0.001637 deg`, and shape pass rate `0.900`; the time-windowed distillation GRU ranked third with raw MAE `0.002032 deg`, centered MAE `0.001561 deg`, and shape pass rate `0.920`. |
| Wave 5.2 post-shape-loss decision gate | closed design gate | The gate compared recent shape-gate, shape-objective, and shape-first distillation screens against prior `Wave 5.2A/B` evidence. Direct shape-threshold loss was rejected for now, unchanged `Wave 5.2B` rerun was rejected, and `Wave 5.2C`, full PINN, and Wave 6 were deferred. | Next branch selected: prepare a narrow causal offset / mean calibration pilot on `polished_dataset` setpoint `Fw`, anchored to `polished_setpoints_periodic_gru_sequence_Fw` and screened against the non-windowed `polished_setpoints_periodic_mlp_harmonic_Fw` comparator before any expansion. |
| Causal offset / mean calibration pilot | closed pilot | Two remote/manual-recovery `polished_dataset` setpoint `Fw` arms completed. The non-windowed `causal_offset_mean_periodic_mlp_harmonic_fw` arm won scalar selection with validation MAE `0.001469 deg` and test MAE `0.001277 deg`; the time-windowed residual-offset GRU finished at test MAE `0.002100 deg`. | Accepted as a completed pilot, not promoted. The non-windowed MLP improves against the original non-windowed harmonic comparator but does not beat the accepted forward GRU scalar baseline or the prior shape-objective scalar high-water mark. Next step is a bounded `TE Curve Verification Pipeline` screen; do not expand the residual-offset GRU profile from this result. |
| Causal offset bounded Track 2 screen | closed diagnostic | Remote bounded `polished_dataset` setpoint `Fw` screen completed on `2026-07-23`; matrix evaluated 5 candidates over 100 forward held-out curves and the shape-gated reranker wrote `2026-07-23-13-09-03__shape_gated_te_curve_reranker`. The measured-versus-predicted plot package and remote-output readability gaps were subsequently repaired. | Not promoted. `polished_setpoints_periodic_gru_sequence_Fw` remains recommended with raw MAE `0.001837 deg`, centered MAE `0.001483 deg`, and shape pass rate `0.950`; the non-windowed causal MLP ranked fourth with raw MAE `0.002075 deg`; the time-windowed causal GRU failed the shape gate with pass rate `0.000`. |
| Wave 5.2 post-causal-offset decision gate | closed design gate | The gate combined the MMT paper, parameter inventory, paired-dataset diagnostics, completed `Wave 5.2B` evidence, and bounded shape and causal-offset screens. Its follow-up residual replay and leakage-safe diagnostic are complete. | Final outcome `blocked_by_parameter_availability`; preserve MMT as an inactive future TODO and continue non-MMT work. |
| Wave 5.2 frozen-baseline residual replay | completed | Four accepted polished-setpoint ONNX baselines were replayed over their exact direction-specific manifests, producing 3,876 per-curve residual rows: 678 training, 194 validation, and 97 test rows per candidate. The selected July archive IDs differ from older June family-registry entries and are recorded explicitly. | Provenance blocker closed. Use these immutable split labels for the leakage-safe MMT rerun; do not substitute the earlier combined-direction audit split. |
| Wave 5.2 MMT residual-explanatory diagnostic | completed with parameter blocker | The rerun fitted 224 permitted comparisons on training residuals and evaluated validation and test across seven residual targets for four `Fw` / `Bw` baselines. Geometry-locked MMT signatures were condition-invariant: metadata-plus-MMT and shuffled-control gains were both exactly zero. All 56 calibrated equivalent-error arms were blocked without using target-derived proxies. | Decision `blocked_by_parameter_availability`; current MMT evidence does not justify a feature, auxiliary head, weak soft constraint, or full PINN. |
| Wave 5.2 Phase 2 harmonic and kinematic PINN | completed negative result | Eight canonical direction-separated runs completed with no failures. The common-split curve-payload diagnostic evaluated all checkpoints and accepted references over `97` held-out curves per direction. `H1-Bw` improved raw error and selected orders but worsened aggregate harmonic-amplitude fidelity; periodic closure improved its own residual without curve-first gain; the Bauer anchor was directionally unstable. | Promote no Phase 2 physics constraint. Retain the implementation and `H1-Bw` as exploratory evidence only. |
| Wave 5.2 Phase 3 quasi-static compliance PINN | completed negative result | Twelve C0-C5 main runs and two C1-Fw stability repeats completed without failures. Bounded forward stiffness was stable with `2.48%` population CV, but only `2 / 3` C1-Fw initializations passed the raw, offset, centered-shape, harmonic-amplitude, and phase gate. C2-Bw and C5-global exposed tradeoffs but failed the joint rule. | Promote no Phase 3 compliance residual. Retain the implementation and parameter audit as falsification evidence; accepted periodic GRU and harmonic MLP references remain unchanged. |
| Wave 5.2 Phase 4 hysteresis, friction, and memory | completed feasibility result | All `969` canonical raw files preserve one ordered `Fw`-to-`Bw` transition with a `2.00175-9.72225 s` inter-window interval. None preserves repeated reversal cycles, repeated major loops, minor-loop labels, controlled warm-up labels, or deterministic reset markers. | Authorize no real-data hysteresis training and promote no residual. Retain `PINN-Y1/Y2/Y3/Y5` for synthetic oracles, `PINN-Y6` for offline reversal comparison, and keep `PINN-Y4` blocked. |
| Wave 5.2 Phase 5 bidirectional TE, backlash, and lost motion | completed identifiability result | All `969` paired conditions and `37,805,294` rows were audited. Median centered correlation is `0.985-0.990`; median absolute mean gap is `3.79-4.78 arcmin`. | Authorize no full-PINN training and promote no residual. Retain `PINN-B1` as an empirical comparator, `PINN-B3/B5` as offline oracles, `PINN-B4` as synthetic-only, and keep `PINN-B2` blocked. |
| Wave 5.2 Phase 6 dynamic acceleration, inertia, and trajectory | completed observability result | All `969` raw conditions and `99,696,607` rows were audited with causal derivatives. All valid windows have stable speed, but no transition passes the fourfold P95 acceleration-separation gate. | Authorize no dynamic full-PINN training and promote no residual. Retain `PINN-D1/D3` as offline oracles and `PINN-D4` as an empirical comparator; keep `PINN-D2/D5` blocked. |
| Wave 5.2 Phase 7 contact, mesh stiffness, and load sharing | completed feasibility result | Six source and implementation files, eleven required quantities, and six `PINN-K` candidates were audited. Basic operating inputs are causal, but contact parameters and states are unavailable. | Authorize no contact training and promote no residual. Retain `PINN-K1-K5` as synthetic-oracle work and keep `PINN-K6` blocked. |
| Wave 5.2 Phase 8 energy, friction, and efficiency | completed feasibility result | Five evidence files, eleven required quantities, and five `PINN-E` candidates were audited. Output power is reconstructable, but the input and internal loss sides of the balance are absent. | Authorize no energy training and promote no residual. Retain `PINN-E1/E2` as synthetic, `PINN-E5` as offline, and keep `PINN-E3/E4` blocked. |
| Wave 5.2 Phase 9 geometry, tolerances, MMT, and manufacturing priors | completed feasibility result | Six evidence files, eight quantities, and five `PINN-G` candidates were audited. Nominal constants exist, but unit-specific and transfer evidence do not. | Authorize no geometry training and promote no residual. Retain `PINN-G1/G2/G3` as synthetic, keep `PINN-G4/G5` blocked, and preserve MMT deferral. |
| Wave 5.2 Phase 10 wear and degradation | completed feasibility result | Three evidence files, eight quantities, and five `PINN-W` candidates were audited. Operating conditions exist, but longitudinal identity, chronology, load cycles, wear, lubrication, and maintenance evidence do not. | Authorize no wear training and promote no residual. Retain `PINN-W2/W3/W4` as synthetic and keep `PINN-W1/W5` blocked. |
| Wave 5.2 Phase 11 electromechanical coupling | completed feasibility result | Three evidence files, eight quantities, and four `PINN-M` candidates were audited. Mechanical channels exist, but synchronized electrical, sideband, health-label, and latency evidence do not. | Authorize no electromechanical training and promote no residual. Retain `PINN-M2/M4` as synthetic and keep `PINN-M1/M3` blocked. |
| Wave 5.2 Phase 12 hybrid analytical and learned residual | completed qualification result | Four evidence files, eight quantities, and six `PINN-R` candidates were audited. Five are empirically trainable, but no candidate includes a promoted physical residual. | Authorize no full-PINN campaign. Preserve `PINN-R1/R2/R3/R4/R6` as empirical designs and keep `PINN-R5` blocked. |
| Wave 5.2 Phase 13 cross-formulation tournament | completed no-contest result | Thirteen phase-evidence files and twelve formulation families were audited. Zero isolated candidates passed full-PINN entry. | Authorize no tournament training and declare no winner. Preserve every candidate state for future reopening. |
| Wave 5.2 Phase 14 integrated multi-physics | completed no-integration result | Four evidence files, eight requirements, and eight planned combinations were audited. Zero promoted components exist against the minimum of two. | Authorize no integrated campaign or combined residual. Preserve every planned pair with reopening conditions. |
| Wave 5.2 Phase 15 Wave 6 entry | completed no-entry closeout | Four evidence files and five entry prerequisites were audited. All five physics-integrated prerequisites fail. | Authorize no physics-integrated Wave 6 campaign and no automatic phase advance. Empirical multi-task research remains separate. |
| Wave 5.2 general full-PINN program | Phases 0 through 15 complete; evidence closeout | All mechanisms are preserved with explicit empirical, rejected, offline, synthetic, deferred, blocked, or no-entry decisions. | Reopen only when a recorded evidence gate changes. |
| Wave 5.2 complete theory-validation program | completed 16 of 16 | The program covered foundations, isolated formulations, synthetic and offline oracles, causal reconstruction, instrumentation, tournament, integration, and Wave 6 entry. | Preserve the closeout; do not weaken full-PINN or Wave 6 entry definitions. |
| Wave 5.2R polished-setpoint forward physics-guided reassessment | completed 16 of 16 without promotion | Stage 15 compared H04, PF-A, harmonic MLP, and periodic GRU on 97 held-out forward curves. H04 improved PF-A raw MAE by `4.59%` and led centered shape, derivative, and mean harmonic phase. The GRU remained `6.82%` better on raw MAE and retained P95, offset, and peak-to-peak leadership. Static export parity passed; TwinCAT runtime remains unclaimed. | Preserve H04 as an exploratory export-prepared grey-box candidate, retain the periodic GRU incumbent, and make no family or program registry changes. |
| Wave 5.2R full-candidate forward verification | closed official diagnostic | Ninety-eight eligible candidates were compared over 97 polished-setpoint forward curves. K01 led raw and offset evidence; F01 led centered shape; S01 led shortlist harmonic amplitude and phase; H08 provided the strongest balanced non-temporal tradeoff. | K01 becomes the temporal offline lane leader and H08 the non-temporal offline balanced leader. Deployment baselines remain the periodic GRU and periodic harmonic MLP until export and runtime gates pass. |
| Wave 5.2R K01/H08 local promotion gate | qualified for conditional campaign | Both candidates passed deterministic replay, ONNX parity, validity/fallback, and local latency checks; K01 also passed reset, causal-prefix, state-carry, and chunk-equivalence checks. | Authorize only the prepared cross-surface campaign. Do not promote globally and do not replace periodic GRU or periodic harmonic MLP. |
| Wave 5.2R K01/H08 cross-surface campaign | completed normal closeout | All `27` runs and checkpoints are present. K01 led mean scalar MAE on `Fw`, `Bw`, and `global`; H08 remained highly repeatable and beat its matched H04 raw-MAE anchor on all three surfaces. | Advance K01 and H08 to a separate official curve-first verification. Make no incumbent or accepted-registry change from scalar evidence alone. |
| Wave 5.2R K01/H08 cross-surface Track 2 | completed partial promotion | Twenty-four candidates were evaluated over separate Fw, Bw, and global matrices, CVP 1.2 diagnostics, three visual shortlist bundles, and three seeds. K01 seed `271828` improved matched-GRU raw, offset, and shape metrics on every surface; H08 regressed matched-MLP raw and offset on Bw/global. | Promote K01 as cross-surface temporal offline leader. Retain H08 as forward specialist. Preserve periodic GRU and periodic harmonic MLP unchanged; do not claim the four-global-leader target. |
| Wave 5.2R H08 backward/global defect analysis | completed non-training diagnostic | Nine frozen H08 payloads and official CVP 1.2 curve evidence separate raw, offset, centered shape, direction, condition, seed, coefficient `a0`, and harmonic-band behavior. Backward H08 retains a `1.13%` shape gain but has a `14.95%` offset regression; the global model is worse than the directional H08 specialists on both directions. | Keep H08 frozen as the non-temporal `Fw` specialist. Exclude the current global formulation from later integration; use its offset and global-interference findings as an ablation contract. Authorize no repair or training. |
| Wave 5.2R integrated specialist package | prepared and approved | The technical roadmap and campaign plan are approved. The empirical K01-based model, three replay controls, eighteen single-branch runs, three conditional `A08` runs, local/remote launcher, frozen-checkpoint hashes, and exact K01/Bw-H08 preflight are prepared. | The operator may launch locally or remotely. Do not promote, alter accepted registries, or claim TwinCAT readiness until the applicable later gates pass. |
| Wave 5.2R integrated specialist campaign | completed normal closeout | All `24` entries completed with zero failure. A02 passed its forward-phase specialty and multi-index non-regression gates for all three seeds. A08 therefore contains A02 alone and reproduces it. A04 seed `271828` is the scalar validation winner but failed both its specialty and non-regression gates. | Record `forward_harmonic_specialist_added` as the empirical campaign outcome. Preserve all incumbents and accepted registries. Advance only A02 to a separately approved Fw/Bw/global curve-first verification; do not promote A04 or claim TwinCAT readiness. |
| Wave 5.2R integrated specialist Track 2 | completed official review | The separate run completed all three matrices and the recovered evidence passed CVP 1.2, multi-index scoring, collage, overlay, Markdown, and real-PDF review. A02 seed `314159` is the veto-free `Fw` and routed `global` recommendation; K01 seed `271828` remains the `Bw` recommendation. A03-A07 win isolated axes but retain failed-gate vetoes. | Record `forward_harmonic_specialist_verified_offline`. Preserve accepted registries and make no deployment claim. Advance A02 to export and TwinCAT qualification only through a separate approved step. |
| Wave 5.2 paper-faithful MMT full PINN | deferred future TODO | MMT diagnostics, parameter inventory, `Wave 5.2B`, the post-causal-offset gate, exact-manifest replay, and leakage-safe explanatory rerun are complete. Contact geometry and causal observations for five equivalent-error groups remain unavailable. | Inactive without blocking the general full-PINN program. Reopen only after independent component-error measurements or validated causal contact-state reconstruction provides condition-varying physical inputs. |
| Six-cell non-MMT reduced cross-wave comparison | closed diagnostic | Six remote selected-model reports and three direction-paired shape-gated reranks covered polished setpoints, simplified setpoints, and polished actual values. Forty-six curve collages were reviewed. | No official promotion. Periodic GRU wins four cells, periodic harmonic MLP wins two, Wave 4.1 remains the raw-error/offset ingredient, and sparse-RCIM temporal models remain reference-only. |
| Wave 6 physics-integrated multi-task / multi-head model | entry not authorized | Intended to combine proven offset, low-frequency, centered-shape, uncertainty, mixture, and validated physics-informed mechanisms. | Reopen only after at least two complementary physical components pass isolated and integrated gates. |
| Future integrated specialist model | empirical campaign closed | K01, forward-only centered H08, H04, F01/S01 objective hypotheses, and Stage 10 R00/S01 controls were evaluated through `A00`-`A08`. Only A02 passed; no multi-specialist combination qualified. | Preserve A02 as a forward-only candidate for separate curve-first verification. Keep A04 provisional and unpromoted. |

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

1. Treat Phases 0 through 15 as complete and preserve the Wave 5.2 evidence
   closeout.
2. Use the approved `Wave 5.2R` roadmap only for `polished_dataset`, setpoint
   inputs, and the `Fw` surface.
3. Preserve the completed Stage 0 forward freeze: `97` eligible test
   conditions and the accepted periodic GRU, periodic harmonic MLP, and
   `PF-A` references reproduce on one contract.
4. Preserve the Stage 4 negative result: do not promote its H08 from scalar
   MAE because the learned correction cancels the analytical anchor.
5. Preserve the Stage 5 positive component result: freeze bounded
   PF-A-anchored core-order H04 as the qualified structured coefficient
   component, and retain the Stage 5 H08 only as a raw-error diagnostic.
6. Preserve the Stage 6 negative result: do not promote FI01 from raw MAE or
   W01 from derivative metrics because neither passed the complete gate.
7. Preserve the Stage 7 negative result: exact decomposition improves
   interpretability, but no shared formulation improved the complete held-out
   curve surface and C01 did not improve centered shape.
8. Preserve the Stage 8 negative result: the positive population slope does
   not identify a pointwise stiffness residual, no weak prior beat data-only
   C00, and the hard equation underfit raw and mean TE.
9. Preserve the Stage 9 qualified-component result: K01 demonstrates that a
   causal coefficient residual can improve H04, but it is not promoted because
   closure, P95, and declared chunk-equivalence gates failed.
10. Preserve the Stage 10 negative qualification result: useful nonlinear
    condition interactions exist, but no stable low-complexity law passed.
11. Preserve the Stage 11 negative qualification result: D01, M01, and E01
    expose partial uncertainty structure, but no trust component passed the
    complete error-localization, selective-risk, interval, subgroup, and cost
    gate.
12. Preserve the Stage 12 negative qualification result: hard-curve emphasis
    can improve selected raw, shape, P95, or closure metrics, but no advanced
    optimizer beat frozen K01 while preserving the complete gate.
13. Preserve the completed Stage 13 synthetic certification: the weak harmonic
    residual is implementation-valid, noise-robust, and specific under its
    oracle contract, but it is not real-data promotion evidence.
14. Preserve the Stage 14 entry result: H04 is the sole eligible entrant and is
    nominated for Stage 15 verification only; K01 and synthetic weak-form
    evidence do not satisfy tournament entry.
15. Preserve the completed Stage 15 decision: H04 improves PF-A and selected
    shape metrics, but the GRU remains the balanced forward incumbent.
    Python/ONNX and static PLC-reference parity pass; TwinCAT runtime remains
    a separate unclaimed deployment task.
16. Keep physics-integrated Wave 6 closed until at least two complementary
   physical components pass isolated and integrated gates.
17. Keep the paper-faithful MMT full PINN as an inactive future TODO. Reopen it
   only with new condition-varying causal physical inputs; do not let it block
   other physics-informed formulations.
18. Do not expand the causal offset / mean calibration profile: its bounded
   `polished_dataset` setpoint `Fw` screen retained
   `polished_setpoints_periodic_gru_sequence_Fw` as the accepted forward
   recommendation, ranked the non-windowed causal MLP fourth, and rejected the
   time-windowed causal GRU through the shape gate.
19. Do not expand the current shape-first distillation pilot: the bounded
   `polished_dataset` setpoint `Fw` screen retained
   `polished_setpoints_periodic_gru_sequence_Fw` as the accepted forward
   recommendation and ranked the distillation candidates behind both
   polished-setpoint baselines.
20. Keep both time-windowed and non-windowed roads active as comparison
   categories for future designs, but require bounded curve-first evidence
   before promotion.
21. Do not expand the current `shape_objective_periodic_mlp_harmonic_fw` pilot:
   the bounded `polished_dataset` setpoint `Fw` screen retained
   `polished_setpoints_periodic_gru_sequence_Fw` as the accepted forward
   recommendation and ranked the shape-objective candidate third.
22. Do not expand the current shape-gate loss v2 checkpoint into a full matrix:
   the bounded `polished_dataset` setpoint `Fw` screen retained
   `polished_setpoints_periodic_gru_sequence_Fw` as the accepted forward
   recommendation.
23. Use Waves 3, 4, and 5.1 as formulation evidence for offset, centered shape,
   robustness, uncertainty, state, harmonic structure, and residual learning;
   do not treat them as substitutes for a full PINN.
24. Keep the shape-gated reranker as the gate before reopening any scalar
   leader: FFT
   amplitude similarity, dominant-harmonic retention, dominant-harmonic phase
   error, derivative correlation, and per-curve shape pass rate.
25. Carry forward the temporal-window road (`periodic_gru_sequence`) as the
   current model-development recommendation. Keep non-windowed branches as
   controlled comparisons until they beat the GRU path on curve-first evidence.
26. Keep `Wave 4.3`, `Wave 4.4`, and `Wave 5.1` branches as integration
   evidence only, not as current active candidates.
27. Select one first full-PINN formulation only after equation, unit,
    observability, identifiability, causality, and analytical-oracle checks.
28. Do not open the integrated multi-task / multi-head campaign until bounded
    PINN pilots and TE Curve Verification Pipeline evidence justify the chosen
    physics-informed ingredients.
29. Preserve the completed integrated-specialist decision: A02 is the only
    gate-qualified branch, A08 contains A02 alone, and A04 remains a
    failed-gate scalar winner. Prepare the separate Fw/Bw/global TE Curve
    Verification Pipeline refresh only after explicit approval and operator
    execution. This empirical result is not automatic Wave 6 authorization.

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
- `doc/reports/analysis/model_development_waves/intermediate_model_selection_cleanup/[2026-07-17]/te_intermediate_model_selection_cleanup_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/non_mmt_cross_wave_comparison/[2026-07-24]/non_mmt_cross_wave_comparison_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-18]/track2_official_model_verification_report.md`
- `doc/reports/campaign_results/cross_wave/polished_dataset/2026-06-29-10-40-05_polished_early_wave_parallel_training_campaign_results_report.md`
- `doc/reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md`
