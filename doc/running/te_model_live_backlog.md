# TE Model Live Backlog

## Program Overview

This file is the canonical operational backlog for the TE model implementation
program.

Use this document as the day-to-day source of truth for:

- current execution status;
- completed waves and tracks;
- next implementation targets;
- deferred and low-priority branches;
- promotion and comparison decisions.

Historical rationale and approval history remain in:

- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
- later TE-related technical notes under `doc/technical/`

## Current Status

- Program State: active.
- Active Campaign State: none. The completed Phase 3 compliance campaign and
  its stability closeout are recorded in
  `doc/running/active_training_campaign.yaml`.
- Current Completed Wave: polished-dataset RCIM, early-wave, and full-wave
  retraining closeouts plus the official `2026-07-03` TE Curve Verification
  Pipeline refresh are complete.
- Current Completed Program: `RCIM Model-Bank Reproduction` paper-faithful
  model bank, closed as
  a faithful full-bank reproduction surface for Tables `2`-`5`.
- Current Completed Pipeline: `TE Curve Verification Pipeline` official
  offline model-verification
  report, closed as the canonical direction-aware verification surface for new
  model families.
- Current Focus: Wave 5.2 Phase 4 hysteresis, friction, and memory feasibility.
  Phases 0 through 3 are complete. Phase 3 trained twelve compliance arms plus
  two C1-Fw stability repeats with no failures and closed as a valid negative
  result. Bounded stiffness was stable, but only two of three C1-Fw
  initializations passed the joint curve-first gate, so no compliance residual
  was promoted. The complete theory-validation roadmap
  preserves harmonic, compliance, hysteresis, bidirectional, dynamic, contact,
  efficiency, geometry, MMT, wear, electromechanical, hybrid, and integrated
  PINN branches. The polished `periodic_gru_sequence` family remains the
  accepted
  model-development baseline; `polished_rcim_model_bank_reproduction_ET19_Fw`
  remains the polished RCIM reference-bank forward leader.
- Parallel Diagnostic Focus: component-offset, `CVP 1.4` h0 cross-check, and
  predicted-mean versus measured-h0 diagnostics are complete; `h0` is the
  correct mean-like channel to inspect, but not the confirmed sole cause of the
  offset failures.
- Current Best Implemented Families: tracked separately for `Fw`, `Bw`, and
  `global`; scalar and curve-first surfaces are not a single ranking.
- Current Best Implemented Run Registry:
  `output/registries/program/current_best_solution.yaml`.
- Current Pruning Gate: near-term model-family selection now excludes
  `global`. `global` remains preserved as a historical and future surface, but
  it is paused until it is the final remaining modeling item in the backlog.
  The `2026-07-17` shape-first cleanup supersedes the previous reduced active
  set. Current active reduced families are `periodic_gru_sequence`,
  `wave4_1_mae_robust_loss`, `wave4_2_quantile_p10_p50_p90`, and
  `periodic_mlp_harmonic`, plus selected simple and RCIM reference anchors.
  `periodic_lstm_sequence_Bw` is demoted as a false scalar leader unless a
  future frequency-domain shape gate proves it preserves measured harmonic
  content.
- Current Active Report Generation: the six-cell reduced selected-model
  `TE Curve Verification Pipeline` pass completed on `2026-07-24`, covering
  polished setpoints, simplified setpoints, and polished actual values for
  `forward` and `backward`. `global`, broad full-matrix, overlay, and
  dataset-difference reports remain paused and on-demand.
- Latest Training Pilot: the Phase 3 quasi-static compliance PINN campaign is
  closed with `12 / 12` main runs and `2 / 2` stability repeats. `C1-Fw` is
  the scalar main-campaign winner and seed `314159` is the repeat winner, but
  seed `271828` regressed raw, offset, and harmonic behavior relative to the
  matched C0 control. The accepted periodic GRU and periodic harmonic MLP
  remain unchanged.
- Active Wave 5.2 Program: Phases 0 through 3 are completed and the general
  full-PINN branch advances to the Phase 4 feasibility gate. Phases 2 and 3
  delivered reusable target-free residual, bounded-parameter, checkpoint
  playback, and multi-index diagnostic infrastructure while rejecting the
  tested harmonic, kinematic, and compliance constraints as defaults.
- Deferred MMT Subbranch: only the paper-faithful MMT full PINN is inactive
  after the leakage-safe rerun found zero held-out gain from geometry-locked
  signatures and could not calibrate unobserved equivalent-error groups.
  Reopen it only after independent component-error measurements or a validated
  causal contact-state reconstruction provides condition-varying physical
  inputs.
- Latest Reduced Decision: periodic GRU is recommended in four of six cells;
  periodic harmonic MLP wins polished-setpoint `Bw` and simplified-setpoint
  `Fw`. Wave 4.1 remains the raw-error and offset diagnostic ingredient.
  Sparse-RCIM temporal candidates remain actual-values references only.
- Current Next Branch: audit Phase 4 chronology and causal-state feasibility
  before any hysteresis training. Verify ordered acquisition, repeated cycles,
  reversals, warm-up, minor and major loops, and deterministic reset evidence.
  Classify Bouc-Wen, rolling-friction, play/stop, and white-box hysteresis as
  directly trainable, synthetic-oracle-only, or blocked. Wave 6 remains
  sequenced after multiple isolated physics components pass.

Current canonical status reports:

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-07-03]/track2_official_model_verification_report.md`
- `doc/reports/analysis/model_development_waves/model_family_pruning/[2026-07-06]/te_model_family_pruning_decision_report.md`
- `doc/reports/analysis/model_development_waves/intermediate_model_selection_cleanup/[2026-07-17]/te_intermediate_model_selection_cleanup_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/non_mmt_cross_wave_comparison/[2026-07-24]/non_mmt_cross_wave_comparison_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-24]/`
- `doc/scripts/campaigns/track_2/run_reduced_selected_track2_reports.md`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-07-03]/track2_best_model_collage_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-07-03]/track2_multi_model_curve_comparison_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_payload_diagnostics_report/[2026-05-28]/track2_curve_payload_diagnostics_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/mean_centered_collage_report/[2026-06-02]/track2_mean_centered_collage_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md`
- `doc/reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification_plan/[2026-06-09]/track2_component_offset_identification_plan.md`
- `doc/reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/[2026-06-09]/track2_component_offset_identification_diagnostic.md`
- `doc/reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/[2026-06-09]/track2d_h0_offset_crosscheck.md`
- `doc/reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/[2026-06-10]/track2d_predicted_mean_h0_surface_diagnostic.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-17-01-27-10_track2h_latent_state_hysteresis_campaign_results_report.md`
- `doc/reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`
- `doc/reports/analysis/Training Results Master Summary.md`

## Directional Rule

The repository now treats direction as a first-class evaluation surface.

The default rule for `TE Curve Verification Pipeline`, `Wave 1`, and all future waves is:

| Surface | Training / archive scope | Evaluation scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` / `forward` | forward only | forward curves only |
| `Bw` / `backward` | backward only | backward curves only |

Exceptions require a new approved technical document. This rule applies whether
the candidate comes from a paper-reference bank, a retuned archive, a
repository-owned neural model, or a future deployable model package.

## Direction-Parallel Best Policy

The project must maintain three best-model surfaces in parallel:

| Surface | Required outcome | Selection meaning |
| --- | --- | --- |
| `Fw` | one best forward model | best compensation candidate for forward curves only |
| `Bw` | one best backward model | best compensation candidate for backward curves only |
| `global` | one best cross-direction model | best deployable combined-surface or fallback candidate |

These tracks are not a single competition. A strong `Fw` model does not
replace the `Bw` or `global` branch, and a strong `Bw` model does not replace
the `Fw` or `global` branch. Future planning, training, reranking, closeout,
and registry-promotion language must keep all three surfaces visible.

Near-term pruning exception:

- `global` is paused for current model-family selection and reduced-pipeline
  planning.
- `global` artifacts and prior reports remain preserved.
- Reopen `global` only when it is the last remaining modeling item in the
  backlog.
- Current decisions are forward-led and backward-checked.
- Active report generation uses only `forward` and `backward` for
  `polished_dataset` and `simplified_dataset`. The broad dataset/surface split,
  collage, overlay, and dataset-difference report families are on-demand only.

## Curve-First Selection Rule

Future program-best promotion must distinguish scalar training metrics from
TE-curve compensation readiness.

Input constraint:

- future deployed models consume only the current point-level operating state,
  an explicitly supported short history of already observed samples, or
  derived causal features;
- full held-out curves are used for validation, diagnostics, and promotion,
  not as future information supplied to the model;
- future-looking smoothing, centered windows containing future samples, and
  complete-curve normalization unavailable at runtime are not valid deployment
  inputs.

The immediate rule is now a multi-index selection policy:

- scalar `MAE` and `RMSE` remain required sanity metrics;
- `TE Curve Verification Pipeline` direction-valid full-curve metrics are the canonical promotion
  surface for deployment-relevant comparison;
- visual overlays and collage evidence must be considered when scalar metrics
  and curve shape disagree;
- mean-centered diagnostics must be interpreted as post-prediction analysis,
  not as a deployment-valid runtime correction;
- raw curve error, curve-bias / `DC` offset error, centered-shape error,
  amplitude error, and harmonic phase error should be tracked separately;
- harmonic amplitude, harmonic phase, P95, and worst-condition diagnostics
  should be added before new training losses are treated as canonical;
- official `TE Curve Verification Pipeline` reports should expose best raw-error, best
  shape-fidelity, best offset-behavior, best robustness, and recommended
  candidates per `global`, `Fw`, and `Bw` surface when the required evidence is
  available.

The canonical policy is:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`

This rule does not reopen closed campaigns. It changes how future branches
interpret their evidence and defines future work as three parallel
direction-valid selection surfaces while preserving the causal input contract.

The first standardized reranking pass is complete in:

- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md`

The next required evaluation task is a complete multi-index reranking over the
current official `TE Curve Verification Pipeline` candidate set, including `Wave 1`, `Wave 2.1`,
`CVP 1.1` through `CVP 1.5`, Waves `3.1` through `4.4`, and `Wave 5.1`.
That reranking must produce
per-surface tables for raw error, centered-shape fidelity, offset / continuity,
harmonic / phase fidelity, robustness, and final recommendation.

Current `CVP 1.1` curve-first leaders by parallel surface:

| Scope | Leader | Mean MPE [%] | P95 MPE [%] | Mean Curve MAE [deg] |
| --- | --- | ---: | ---: | ---: |
| Forward | `rcim_retuned_GBM19_Fw` | 2.371752 | 4.911649 | 0.001089 |
| Backward | `rcim_retuned_GBM19_Bw` | 5.398275 | 12.280348 | 0.002766 |
| Global surface | `periodic_lstm_sequence_global` | 6.119950 | 14.716986 | 0.002707 |

This reranking does not promote a single new program-best model by itself.
It provides one `Fw`, one `Bw`, and one `global` evidence track. Harmonic
amplitude, harmonic phase, derivative-continuity, and stitched-revolution
residual diagnostics remain validation extensions before curve-first training
losses become canonical.

The first screened curve-payload diagnostics pass is also complete in:

- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_payload_diagnostics_report/[2026-05-28]/track2_curve_payload_diagnostics_report.md`

Current `CVP 1.2` diagnostic observations:

| Finding | Interpretation |
| --- | --- |
| `rcim_retuned_GBM19_Fw` keeps the best screened diagnostic score. | It remains the strongest forward paper-reference curve-shape baseline. |
| `periodic_gru_sequence_Bw` is the strongest practical repository-owned backward candidate. | It is close to `rcim_retuned_GBM19_Bw` on mean percentage error and much better on selected harmonic phase. |
| `periodic_lstm_sequence_global` is the strongest screened global-surface neural candidate. | It is the best current global neural starting point for a deployable cross-direction branch. |
| `harmonic_regression_Bw` has the cleanest backward harmonic amplitude/phase diagnostics but worse scalar and peak-to-peak error. | It is useful as a structured diagnostic reference, not the next direct promotion target. |
| `tree` candidates remain weak on peak-to-peak and shape diagnostics. | The next direction-parallel training work should not start from `tree` despite scalar strength. |

The first mean-centered collage diagnostic is complete in:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/mean_centered_collage_report/[2026-06-02]/track2_mean_centered_collage_report.md`

Current mean-offset observations:

| Finding | Interpretation |
| --- | --- |
| `harmonic_regression_global` improves from `0.031130 deg` raw MAE to `0.000888 deg` centered MAE on the four-curve collage. | Vertical offset is a dominant raw-error component for this candidate; centered shape is much better than raw MAE suggests. |
| `periodic_lstm_sequence_global`, `periodic_temporal_convolution_global`, and `periodic_gru_sequence_global` also improve strongly after mean-centering. | Several temporal neural candidates need offset and centered-shape diagnostics reported separately. |
| Dense `Wave 2.3` variants improve much less after mean-centering. | Their limitation is not only offset; centered shape, amplitude, or phase quality remains weak. |
| Full-curve mean-centering uses information unavailable at runtime. | It is a diagnostic decomposition, not a deployable correction. |

The next approved work should therefore first diagnose all three best-model
surfaces in parallel:

| Surface | Current evidence | Practical next action |
| --- | --- | --- |
| `Fw` | paper-reference `rcim_retuned_GBM19_Fw` leads current curve diagnostics. | Run CVP 1.4 offset, centered-shape, amplitude, phase, and condition audit before selecting a forward retraining family. |
| `Bw` | `periodic_gru_sequence_Bw` is the strongest practical repository-owned backward candidate. | Run CVP 1.4 to decide whether the backward issue is offset-limited or shape-limited before retraining periodic temporal models. |
| `global` | `periodic_lstm_sequence_global` is the strongest screened global neural candidate. | Keep a dedicated global branch and audit offset/shape separately instead of folding it into the backward winner. |

Full-curve diagnostics remain strictly post-prediction and must preserve the
causal runtime input contract.

The `CVP 1.4` full-matrix audit is complete in:

- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`

Current `CVP 1.4` observations:

| Finding | Interpretation |
| --- | --- |
| `111` candidates and `12,416` curves were evaluated. | The mean-offset finding now covers the full official direction-valid matrix, not only the collage subset. |
| `periodic_gru_sequence_global` is the global-surface diagnostic leader. | The next global branch should start from periodic sequence models and add offset-aware selection or calibration. |
| `rcim_retuned_GBM19_Fw` remains the strongest forward diagnostic leader. | The repository-owned forward branch remains open; the forward target is still to approach the paper-reference shape/offset behavior. |
| Many candidates are labeled `offset-limited` or mixed with offset limitations. | A causal offset-calibration or offset-aware loss branch is justified before opening unrelated model-family exploration. |
| `harmonic_regression_global` shows the largest mean-offset improvement but remains amplitude/phase limited. | Removing offset alone is insufficient for that global harmonic candidate; phase and amplitude terms must stay in the metric bundle. |

Next planned diagnostic and training decision branches:

| Branch | Scope | Status |
| --- | --- | --- |
| `CVP 1.4 Mean-Offset Full-Matrix Audit` | Apply raw, offset, centered-shape, amplitude, harmonic phase, and condition-stratified metrics to the full official curve-verification candidate matrix. | completed |
| Offset-aware checkpoint selection | Monitor curve-bias, centered-shape, P95, harmonic phase, then scalar `val_mae`. | next decision candidate |
| Curve-aware loss branch | Add pointwise, bias, centered-shape, slope, harmonic amplitude, and harmonic phase terms while preserving causal inputs. | next decision candidate |
| Shape-gate metric loss pilot | Evaluate whether the shape-gated reranker metrics can become normalized auxiliary training losses or checkpoint-selection monitors for a small polished `periodic_gru_sequence`-anchored pilot. | first `polished_dataset` setpoint `Fw` pilot completed; the initial Track 2 failure was traced to polished input-mode drift in lightweight playback. After fixing setpoint propagation, the pilot passes the forward gate but the patched Fw/Bw expansion ranks it only fifth on forward, behind the existing polished-setpoint active candidates. Do not launch the full three-dataset, three-surface Aries campaign from this exact loss profile. |
| Component-offset identification | Test whether curve offset is dominated by `a_0` / `Component 0`, multiple components, condition/regime behavior, or experimental repeatability limits. | measured `h0`, signed-offset cross-check, and predicted-mean surface diagnostics completed; `h0` is the right mean channel, but the actionable issue is model-side mean-surface bias/compression |
| `Wave 4 series` dispersion-aware modeling probes | Test robust losses, quantile or probabilistic heads, mixture-density heads, and latent-state or hysteresis-aware features on the offset and fragile-harmonic problem. | robust-loss, quantile/probabilistic, MDN, and `Wave 4.4` latent-state / hysteresis-aware campaigns and official TE Curve Verification refreshes completed; all are exploratory and not promoted |
| `Wave 5.1` hybrid structured models | Combine harmonic structure, condition-conditioned residual learning, and explicit grouped treatment of stable and fragile harmonic bands. | first real `wave3_harmonic_prior_residual` campaign and official `TE Curve Verification Pipeline` verification refresh closed as a verified exploratory baseline, not promoted |
| `Wave 5.2` general full-PINN program | Audit and test explicit differentiable physics formulations derived from harmonic behavior, the Polynomial Fourier Series law, Wave 3 through Wave 5.1 evidence, and additional references. | Phases 0 through 3 complete; Phases 2 and 3 closed as valid negative results with no promoted harmonic, kinematic, or compliance constraint; Phase 4 feasibility audit is next |
| `Wave 5.2` complete theory-validation program | Preserve and falsify every ingested physical mechanism through direct-data, causal-state, offline-oracle, instrumentation, isolated-PINN, cross-formulation, and integration tests. | roadmap complete; Phases 0 through 3 of 16 completed; Phase 4 feasibility active |
| `Wave 5.2` paper-faithful MMT full PINN | Preserve the completed MMT evidence and reopen only if causal physical inputs become available. | deferred future TODO after the parameter-availability blocker; no MMT feature, auxiliary head, weak constraint, or MMT full PINN is authorized |
| Intermediate shape-first model-selection cleanup | Reduce the post-retraining active set using raw error, P95, centered shape, P2P behavior, visual collage evidence, and actual-values stability. | completed; active set is `periodic_gru_sequence`, `wave4_1_mae_robust_loss`, `wave4_2_quantile_p10_p50_p90`, and `periodic_mlp_harmonic`; `periodic_lstm_sequence_Bw`, `Wave 4.3`, `Wave 4.4`, and `Wave 5.1` are closed as active branches |
| Frequency-domain shape-gated reranker | Add measured/predicted FFT amplitude similarity, dominant-harmonic retention, dominant-harmonic phase error, robust derivative agreement, threshold sweep, and per-curve shape pass rate to future reduced reports. | completed across the six-cell non-MMT reduced pass; periodic GRU wins four cells, periodic harmonic MLP wins two, and the simplified tree scalar leader remains vetoed by weak shape retention |
| Shape-gate loss pilot | Test whether calibrated shape-gate evidence can improve training or checkpoint selection. | patched polished-setpoint Fw/Bw expansion completed. Forward recommendation remains `polished_setpoints_periodic_gru_sequence_Fw`; backward recommendation is `polished_setpoints_periodic_mlp_harmonic_Bw`; the shape-gate loss pilot remains a viable but non-promoted forward candidate. Future training should evaluate a stricter second pilot or checkpoint-selection variant focused on derivative/ripple preservation before any full `simplified_setpoints`, `polished_setpoints`, and `polished_actual_values` x `global`/`Fw`/`Bw` Aries campaign. |
| Shape-first training-rule distillation | Use stable `TE Curve Verification Pipeline` shape-first checks as auxiliary training rules while preserving both time-windowed and non-windowed candidate roads. | first two-arm `polished_dataset` setpoint `Fw` pilot and bounded curve-first screen completed. `polished_setpoints_periodic_gru_sequence_Fw` remains recommended; the time-windowed distillation GRU ranked third and the non-windowed distillation MLP ranked fourth. Do not expand this profile; carry the evidence into the next loss or checkpoint-selection design only if it directly addresses the raw-error, offset, harmonic-amplitude, and robustness regressions. |
| Post-shape-loss `Wave 5.2` decision gate | Choose the next branch after direct shape-threshold training pressure failed to promote. | completed; selected the causal offset / mean calibration pilot anchored to `polished_setpoints_periodic_gru_sequence_Fw`, with `polished_setpoints_periodic_mlp_harmonic_Fw` kept as the required non-windowed comparator. Do not rerun `Wave 5.2B` unchanged and do not start `Wave 5.2C`, full PINN, or Wave 6 before this narrow offset gate is curve-screened. |
| Causal offset / mean calibration pilot | Test whether direct offset / curve-mean pressure improves the next `polished_dataset` setpoint `Fw` branch while preserving both time-windowed and non-windowed roads. | completed and bounded-screened; the non-windowed harmonic MLP won scalar selection but ranked fourth in the bounded curve-first screen, while the time-windowed residual-offset GRU failed the shape gate. Do not promote or expand this direct causal-offset profile. |
| Post-causal-offset `Wave 5.2` decision gate | Decide whether MMT should remain diagnostic-only, become a feature or auxiliary-output path, or become a weak soft constraint. | completed; the follow-up replay and leakage-safe diagnostic selected `blocked_by_parameter_availability`. MMT is now an inactive future TODO and does not block non-MMT work. |
| Wave 6 integrated multi-task / multi-head model branch | Shared causal trunk with separate offset, low-frequency, centered-shape, uncertainty or mixture, and validated physics-informed heads. | sequenced after bounded Wave 5.2 PINN pilots and curve-first verification; do not prepare a campaign until the useful physics-informed ingredients are known |
| Sequential residual calibration branch | Current best causal model plus second causal residual or offset calibrator trained on model error. | candidate after audit |

The `CVP 1.5` offset-predictability feasibility diagnostic is complete in:

- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md`

Current `CVP 1.5` observations:

| Finding | Interpretation |
| --- | --- |
| The conservative best causal grouping is `direction_torque`, not the exact full operating condition. | Offset has a condition-linked signal, but exact full-condition memorization must not be treated as deployable predictability. |
| `harmonic_regression_global` shows the largest conservative offset-correction feasibility gain, but remains amplitude/phase limited. | It is useful as an offset probe reference, not as an automatic global production winner. |
| `rcim_retuned_XGBM19_Bw` and `LGBM19_Fw` are the strongest per-surface sequential-offset feasibility probes. | The next branch should test offset modeling behavior per surface without collapsing `Fw`, `Bw`, and `global` into one competition. |
| Most candidates fall into `multi_head_shape_offset`, `posthoc_offset_baseline`, or `not_offset_first` rather than a clean sequential-offset path. | The next training plan should include offset, centered-shape, amplitude, and phase terms instead of assuming offset correction alone solves the curve-following problem. |

Recommended next gate:

- treat Wave 5.2 reference intake, equation audit, and first-PINN formulation
  selection as the next physics-informed branch;
- use the MMT diagnostic as retained evidence without making its missing
  parameters a blocker for Polynomial-Fourier, harmonic-kinematic, or other
  source-backed formulations;
- keep Wave 6 after bounded PINN pilots and curve-first formulation decisions;
- do not document `a_0` / `Component 0` as the confirmed sole cause unless
  repeatability, component-level error, and model-side surface diagnostics
  support that conclusion.

## Completed

### Planning Foundation

Status:

- completed.

Delivered:

- TE family roadmap approved.
- TE analytical family comparison report approved.
- TE implementation backlog approved.
- low-priority `Lightweight Transformer` and `Neural ODE` branches made
  explicit.
- additional family candidates added explicitly:
  - `State-Space Sequence Model`
  - `Mixture-of-Experts / Regime-Conditioned Model`
  - optional `Kernel Ridge / Gaussian Process` benchmark

### Wave 0 Shared Infrastructure

Status:

- completed.

Delivered:

- shared training infrastructure in
  `scripts/training/shared_training_infrastructure.py`;
- explicit `experiment.model_family` in feedforward presets;
- common artifact names:
  - `training_config.yaml`
  - `metrics_summary.yaml`
- category-specific output roots:
  - `output/training_runs/`
  - `output/validation_checks/`
  - `output/smoke_tests/`
  - `output/registries/`
- reusable one-batch validation entry point:
  `scripts/training/validate_training_setup.py`;
- reusable Lightning smoke-test entry point:
  `scripts/training/run_training_smoke_test.py`;
- feedforward training path updated to consume the shared infrastructure.

Verification:

- one-batch validation completed successfully;
- smoke test with checkpoint save/reload completed successfully;
- feedforward `trial` run completed successfully with the common metrics
  schema;
- Wave 0 `trial` artifacts are verification-only and are not the canonical
  program baseline.

### Recovered Original RCIM Pipeline

Status:

- completed and preserved as provenance evidence.

Delivered:

- recovered original RCIM workflow copied under
  `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`;
- original `v18` forward path and recovered pipeline structure documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Original Pipeline To Reimplementation Companion.md`;
- code-level audit documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Original Pipeline And Reimplementation Audit.md`;
- original ONNX release parity interpretation documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Original ONNX Release Parity Interpretation.md`;
- archive parity across `rcim_original`, `rcim_retuned`, and `rcim_track1`
  documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Archive Parity Interpretation.md`.

Operational meaning:

- the recovered workflow is the code-level provenance anchor;
- the copied original workflow is not the active implementation surface;
- current comparisons use curated archives under `models/paper_reference/`.

### Retuned RCIM Reference Archive

Status:

- completed as the current recovered-original retuned baseline.

Delivered:

- retuned forward and backward paper-reference archives promoted under
  `models/paper_reference/rcim_retuned/`;
- retuned family-direction archive count: `22`;
- retuned closeout report:
  `doc/reports/analysis/rcim_paper_reference/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.md`;
- retuned values integrated into the canonical RCIM Tables `2`-`5` benchmark
  and curve-verification comparison matrix.

Operational meaning:

- forward `RCIM Model-Bank Reproduction` cells compare against the better value between paper
  original and paper retuned;
- backward `RCIM Model-Bank Reproduction` cells compare against paper retuned, because the paper
  does not provide backward original tables.

### RCIM Model-Bank Reproduction RCIM Paper-Faithful Model Bank

Status:

- closed.

Delivered:

- faithful original-dataset exact-model-bank implementation under
  `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`;
- completed forward paper-faithful grid-search campaign across
  `SVR`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `LGBM`, `XGBM`, and
  `ELM`;
- completed backward paper-faithful grid-search campaign across the same
  operational family bank;
- accepted forward archives refreshed under
  `models/paper_reference/rcim_track1/forward/`;
- accepted backward archives refreshed under
  `models/paper_reference/rcim_track1/backward/`;
- Tables `2`-`5` repopulated in
  `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`;
- Windows PowerShell and Linux Bash launcher surfaces documented for future
  reruns.

Closure rule:

- `RCIM Model-Bank Reproduction` is closed because the faithful full-bank protocol was run in both
  directions and all benchmark cells were repopulated.
- Green-only status is not a `RCIM Model-Bank Reproduction` closure requirement.
- Any all-green pursuit, restricted-dataset rerun, or target-parameterization
  search is a new optimization branch, not a reopening of closed `RCIM Model-Bank Reproduction`.

Artifact rule:

- intermediate validation-model `.pkl` bundles under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
  and
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`
  stay out of Git tracking and Git LFS;
- only curated accepted archives under `models/paper_reference/rcim_track1/`
  are the `RCIM Model-Bank Reproduction` paper-reference model surface.

### Wave 1 Structured Static Baselines

Status:

- closed.

Delivered:

- completed `global`, `forward`, and `backward` surfaces for the implemented
  repository model families;
- completed directional best-hyperparameter search campaign;
- refreshed exported model surfaces under `models/exported/`;
- consolidated closeout report:
  `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`.

Current HPO leader:

- run: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10`;
- family: `tree_fw`;
- scope: `forward`;
- test MAE: `0.002743 deg`.

Operational meaning:

- `Wave 1` is the closed structured-baseline stage for future model-family
  comparisons;
- the current `Wave 1` scalar HPO leader is a baseline, not sufficient
  compensation evidence by itself;
- future `Wave 1B` work should first rerank accepted artifacts on TE Curve Verification Pipeline
  curve metrics before retraining or adding losses;
- any `Wave 1B` retraining must keep the same pointwise operating-state input
  contract unless a later approved deployment note explicitly supports a causal
  history extension;
- future waves must either produce `global`, `forward`, and `backward` surfaces
  or explicitly justify why one of those surfaces is omitted;
- the oversized random-forest artifact class observed near `91 GB` remains
  deployment-incompatible and must not be promoted into future TwinCAT/PLC
  export candidate sets.

## In Progress

### TE Curve Verification Pipeline Directional Offline Comparison

Status:

- closed as the official offline model-verification report.

Canonical report:

- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-05-21]/track2_official_model_verification_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`

Current comparison surface:

- comparison mode: `full_directional_candidate_matrix`;
- candidate count: `84`;
- held-out curve count before candidate filtering: `194`;
- denominator for percentage error: `peak_to_peak_truth`;
- `Fw` candidates evaluate only on forward curves;
- `Bw` candidates evaluate only on backward curves;
- `global` candidates evaluate on both directions with separated metrics.

Candidate groups:

- accepted `RCIM Model-Bank Reproduction` forward and backward family banks;
- recovered original forward family banks;
- retuned forward and backward family banks;
- `Wave 1` exported `global`, `forward`, and `backward` models;
- `Wave 2.1` temporal `global`, `forward`, and `backward` registry models;
- composed best-reference candidates for paper original, paper retuned, and
  `RCIM Model-Bank Reproduction`.

Current curve-verified leaders by source:

| Direction | Source | Candidate | Mean percentage error [%] |
| --- | --- | --- | ---: |
| forward | paper original | `paper_original_best_Fw` | 6.250 |
| forward | paper retuned | `paper_retuned_best_Fw` | 4.109 |
| forward | RCIM Model-Bank Reproduction | `track1_best_Fw` | 6.819 |
| backward | paper retuned | `paper_retuned_best_Bw` | 7.572 |
| backward | RCIM Model-Bank Reproduction | `track1_best_Bw` | 11.860 |

Backward baseline rule:

- the paper does not provide a paper-original backward reference surface;
- `paper_retuned_best_Bw` is therefore the canonical paper-derived backward
  baseline for `TE Curve Verification Pipeline` and `Target A`;
- future backward comparisons should report against this retuned baseline
  unless a later approved technical document defines a stronger backward paper
  proxy.

Best individual family candidates currently visible in TE Curve Verification Pipeline:

| Direction | Candidate | Mean percentage error [%] |
| --- | --- | ---: |
| forward | `rcim_retuned_GBM19_Fw` | 2.372 |
| backward | `rcim_retuned_GBM19_Bw` | 5.398 |

Official closeout package:

- the official verification report consolidates the direction-aware metric
  matrix, best-model collage PDF, multi-model curve comparison PDF, and future
  `TE Curve Verification Pipeline` campaign update ledger;
- future model-verification updates must refresh the matrix, visual reports,
  official PDF, and this backlog before new candidates are accepted.

## Next Up

### Planned Next Step

After the completed Phase 3 negative closeout, the active next step is:

- audit whether source files preserve ordered acquisition and causal state;
- identify repeated reversals, minor and major loops, warm-up intervals, and
  deterministic reset evidence;
- classify Bouc-Wen, rolling-friction, play/stop, temperature-conditioned, and
  white-box hysteresis formulations by real-data feasibility;
- preserve synthetic and offline-oracle tests for laws that current
  measurements cannot identify;
- retain a matched NARX or GRU causal-history comparator when chronological
  input windows are valid;
- reuse per-term logging, checkpoint playback, and multi-index diagnostics;
- keep rejected Phase 2 and Phase 3 physics weights at zero by default;
- retain the imported harmonic, hysteretic, dynamic, bidirectional, contact,
  efficiency, tolerance, wear, and electromechanical sources as separate
  formulation or oracle branches;
- retain periodic GRU as the primary time-windowed reference;
- retain periodic harmonic MLP as the non-windowed structured reference;
- use Waves 3, 4, and 5.1 as experimental evidence for PINN loss, offset,
  robustness, uncertainty, state, and harmonic-design decisions;
- select one formulation for the first bounded pilot only after equation,
  observability, identifiability, causality, and oracle checks;
- keep the paper-faithful MMT formulation deferred behind its physical-input
  reopening gate;
- execute the remaining theory portfolio through the complete three-lane test
  roadmap rather than discarding formulations that initially require synthetic
  or instrumentation-backed evidence;
- defer Wave 6 campaign design until bounded PINN evidence identifies useful
  physics-informed ingredients.

The previous temporal refresh answered three concrete questions:

- best temporal forward candidate: `gru_sequence_Fw` at `7.378%` mean error;
- best temporal backward candidate: `lstm_sequence_Bw` at `7.767%` mean error;
- final decision: temporal models are verified exploratory baselines and are
  not promoted over `tree`.

### Post-Verification Decision

Default decision path after TE Curve Verification closeout:

- treat TE Curve Verification Pipeline curve-following quality as the promotion surface for future
  compensation-relevant candidates;
- use completed `CVP 1.4 Mean-Offset Full-Matrix Audit` before changing model
  families, checkpoint monitors, or training losses;
- use the completed h0 diagnostics to keep `h0` as the primary mean-surface
  channel while avoiding the unsupported claim that it is the only cause;
- test dispersion-aware losses and heads, hybrid structured models, and a
  first PINN before committing to a large integrated multi-head architecture;
- evaluate calibrated shape-gate metrics as future auxiliary losses or
  checkpoint monitors only after the reduced reranker proves which FFT,
  harmonic, phase, offset, and derivative terms are stable enough to train on;
- preserve causal runtime inputs: point-level state, optional short past
  history, and causal derived features only;
- keep `Wave 2.1` temporal models as verified exploratory baselines;
- keep the same `global`, `forward`, and `backward` surface rule for Wave 2.1;
- use `Wave 1` and TE Curve Verification Pipeline as the comparison baseline for every Wave 2.1 family;
- keep paper-alignment bridge work available only if the user explicitly
  reopens a narrower offline paper-alignment question before temporal-model
  exploration.

### Paper Alignment Targets

`Target A`: match or beat the paper on a comparable offline prediction
benchmark.

Status:

- closed as `closed_offline_direction_qualified`.
- closeout source of truth:
  `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`.

Required validation path:

- reproduce a TE-curve validation protocol comparable to the paper;
- report mean percentage error on unseen scenarios;
- reach `<= 4.7%` mean percentage error for the paper-comparable forward
  surface;
- use `paper_retuned_best_Bw` as the canonical paper-derived backward baseline,
  because the paper provides no paper-original backward reference surface.

Current offline evidence:

- paper retuned forward best composite is below the `4.7%` threshold at
  `4.109%`;
- paper retuned backward best composite is the accepted backward baseline at
  `7.572%`;
- retuned individual `GBM` forward and backward candidates are currently the
  strongest TE Curve Verification Pipeline offline family references;
- `RCIM Model-Bank Reproduction` remains closed as faithful reproduction evidence, not as the
  optimized winner.

Closeout verdict:

- forward `Target A` is met against the paper-comparable `4.7%` offline
  threshold;
- backward `Target A` is closed against the approved retuned backward baseline;
- no additional offline paper-alignment bridge is required before opening the
  next modeling branch;
- online compensation remains outside `Target A` and is tracked under
  `Target B`.

`Target B`: reproduce the online compensation benchmark.

Canonical branch:

- `Track 3. Online Compensation And Deployment Evaluation`.
- `Target B` is the closeout objective for Track 3, not a standalone modeling
  wave.

Required validation path:

- implement repository-owned online compensation tests;
- run `Robot` and `Cycloidal` style motion-profile validation;
- reach at least `83%` robot TE RMS reduction;
- reach at least `90%` cycloidal TE RMS reduction;
- report uncompensated and compensated TE RMS plus TE max in a Table 9 style
  comparison.

Until `Target B` is executed, present all paper comparisons as `offline-only`
rather than end-to-end equivalent.

## Deferred Branches

### Paper-Alignment Bridge

Status:

- deferred until TE Curve Verification Pipeline is closed or explicitly promoted.

Scope if promoted:

- harmonic-wise prediction of paper-style `A_k` and `phi_k` terms;
- TE reconstruction from predicted harmonic terms;
- offline motion-profile playback for `Robot` and `Cycloidal` style profiles;
- paper-comparable offline validation protocol that reports TE-curve
  percentage-error metrics and closes or rejects `Target A`.

Candidate script root:

- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/`

Candidate artifact root:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`

### RCIM Model-Bank Reproduction Restricted-Dataset Future Rerun

Status:

- deferred until much later.

Entry rule:

- do not use this branch to overwrite the closed full-dataset `RCIM Model-Bank Reproduction` status;
- create new campaign names, output roots, archive namespaces, and comparison
  reports for every restricted-dataset level.

Required scope if promoted:

- rerun the closed `RCIM Model-Bank Reproduction` paper-faithful model-bank protocol on one or more
  restricted dataset variants;
- keep the current full-dataset `RCIM Model-Bank Reproduction` archive and benchmark as immutable
  comparison anchors;
- revisit the recovered-workflow pickle cache contract so restricted-dataset
  experiments use explicit cache partitioning;
- create a new Markdown comparison report that places full-dataset and
  restricted-dataset Tables `2`-`5` side by side.

### Track 3. Online Compensation And Deployment Evaluation

Status:

- future implementation branch;
- not implemented;
- deferred until the offline comparison baseline is accepted as closed.

Canonical objective:

- close `Target B`.

Planned scope:

- implement the repository-owned online compensation loop in the TestRig /
  TwinCAT execution path;
- run `Robot` and `Cycloidal` style motion-profile validation;
- report uncompensated versus compensated `TE RMS` and `TE max`;
- produce the final paper-style `Table 9` comparison;
- evaluate deployment-readiness for the selected repository model path;
- use `doc/reference_codes/testrig_twincat_ml_reference.md` as the canonical
  technical baseline for the imported TestRig PLC path;
- keep the legacy Beckhoff path in scope:
  - `TF38x0`
  - `FB_MllPrediction`
  - `XML/BML`
- compare the newer Beckhoff server path:
  - `TF3820` / `TF3830`
  - `FB_MlSvrPrediction`
  - `ONNX + JSON + PlcOpenXml`
- evaluate model acceptance, conversion success, workflow complexity, runtime
  behavior, maintainability, and engineering cost;
- exclude the already observed oversized random-forest artifact class unless a
  later explicitly lighter tree variant is produced.

Boundary:

- Track 3 is not `Wave 5.1`; `Wave 5.1` remains an offline hybrid structured-model
  exploration branch.
- Track 3 absorbs the old future online Pipelines `8-10`, `Target B`, and the
  deferred TwinCAT deployment-evaluation branch.

### Repository Documentation Publication

Status:

- deferred.

Entry rule:

- keep the repository private for now;
- do not activate GitHub Pages publication until the repository is intentionally
  made public;
- after public activation, record the live documentation URL in the appropriate
  documentation entry points.

### Explicit Low-Priority Exploratory Families

Status:

- low priority.

Families:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- optional `Kernel Ridge / Gaussian Process` benchmark

Entry rule:

- these families should not displace the main roadmap unless later evidence
  justifies them or the user explicitly promotes them.

## Wave Checklist

### Wave 0. Shared Infrastructure

- completed.

### Wave 1. Structured Static Baselines

- planning report: completed;
- implementation: completed;
- smoke tests: completed;
- validation checks: completed;
- campaign execution: completed;
- directional HPO closeout: completed;
- exported `global`, `forward`, and `backward` surfaces: completed;
- results report: completed;
- status: closed.

### RCIM Model-Bank Reproduction. RCIM Paper-Faithful Model Bank

- recovered original workflow: preserved;
- original-dataset reimplementation: completed;
- retuned reference archive: completed;
- forward campaign: completed;
- backward campaign: completed;
- paper-reference archives: refreshed;
- Tables `2`-`5`: repopulated;
- status: closed as faithful full-bank reproduction, not all-green
  optimization.

### TE Curve Verification Pipeline. Directional Offline Comparison

- direction-aware loader and candidate matrix: completed;
- recovered original forward candidates: included;
- retuned forward and backward candidates: included;
- `RCIM Model-Bank Reproduction` forward and backward candidates: included;
- `Wave 1` `global`, `forward`, and `backward` exports: included;
- `Wave 2.1` temporal `global`, `forward`, and `backward` registry candidates:
  included;
- grouped source tables: completed;
- composite best-reference visibility: completed;
- direction/truth and preview audit: completed;
- official model-verification report: completed;
- multi-index curve-first selection policy: adopted;
- complete multi-index reranking over all current official candidates:
  next analysis branch;
- status: closed.

### Wave 2.1. Temporal Models

- status: entry campaign completed; closeout report prepared; official
  `TE Curve Verification Pipeline` refresh completed;
- initial families: `temporal_convolution`, `gru_sequence`, `lstm_sequence`;
- configuration root: `config/training/hydra/wave2/`;
- preliminary campaign plan:
  `doc/reports/campaign_plans/wave_2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`;
- closeout report:
  `doc/reports/campaign_results/wave_2/2026-05-24-12-36-49_wave2_temporal_model_entry_campaign_results_report.md`;
- campaign winner: `te_gru_sequence_remote_Fw` from family
  `gru_sequence_fw`, with test MAE `0.003333 deg`;
- refresh plan:
  `doc/reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/wave2_temporal_model_refresh_plan/[2026-05-24]/track2_wave2_temporal_model_refresh_plan.md`;
- official verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-05-24]/track2_official_model_verification_report.md`;
- curve-verification decision: verified exploratory baselines, not promoted over `tree`;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- baseline comparison: TE Curve Verification Pipeline plus closed Wave 1.

### Wave 2.2. Harmonic Temporal Hybrid Models

- status: harmonic-temporal hybrid campaign completed; normal closeout report
  prepared; official `TE Curve Verification Pipeline` refresh completed;
- families: `periodic_temporal_convolution`, `periodic_gru_sequence`,
  `periodic_lstm_sequence`;
- configuration root:
  `config/training/wave2b_harmonic_temporal_hybrid/`;
- preliminary campaign plan:
  `doc/reports/campaign_plans/wave_2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`;
- closeout report:
  `doc/reports/campaign_results/wave_2/2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report.md`;
- campaign winner: `te_periodic_gru_sequence_remote_Bw` from family
  `periodic_gru_sequence_bw`, with test MAE `0.002344 deg`;
- strongest bidirectional candidate: `te_periodic_gru_sequence_remote_global`
  from family `periodic_gru_sequence`, with test MAE `0.002681 deg`;
- curve-verification decision: strongest repository-owned neural branch after official
  verification; `periodic_gru_sequence_Bw` is the strongest backward-only
  candidate and `periodic_gru_sequence_global` is the strongest global neural
  candidate;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- baseline comparison: official curve-verification matrix plus visual collage and overlay
  reports.

### Wave 2.3. Residual Harmonic Temporal Hybrid Models

- status: residual harmonic temporal hybrid campaign completed; official
  `TE Curve Verification Pipeline` refresh completed;
- families: `residual_harmonic_gru_sequence`,
  `residual_harmonic_lstm_sequence`;
- harmonic banks: sparse `RCIM`, dense `240`, dense `360`;
- closeout report:
  `doc/reports/campaign_results/wave_2/2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-05-28]/track2_official_model_verification_report.md`;
- strongest Wave 2.3 forward candidate:
  `residual_harmonic_gru_sequence_sparse_rcim_Fw`, curve-verification MAE
  `0.003194 deg`;
- strongest Wave 2.3 backward candidate:
  `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, curve-verification MAE
  `0.003440 deg`;
- strongest Wave 2.3 global candidate:
  `residual_harmonic_lstm_sequence_sparse_rcim_global`, curve-verification MAE
  `0.003368 deg`;
- curve-verification decision: verified exploratory baseline, not promoted over the
  `Wave 2.2` periodic sequence leaders;
- design conclusion: sparse `RCIM` harmonics remain useful, while dense `240`
  and dense `360` harmonic banks are not competitive for this residual
  temporal branch.

### Wave 3.1. Offset-Aware Sequential Residual Probe

- status: offset-aware probe campaign completed; official `TE Curve Verification Pipeline` matrix
  refresh completed;
- family: `sequential_residual_offset_probe`;
- official verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-04]/track2_official_model_verification_report.md`;
- strongest Wave 3.1 forward candidate:
  `sequential_residual_offset_probe_Fw`, curve-verification MAE `0.003377 deg`;
- strongest Wave 3.1 backward candidate:
  `sequential_residual_offset_probe_Bw`, curve-verification MAE `0.003636 deg`;
- strongest Wave 3.1 global candidate:
  `sequential_residual_offset_probe_global`, combined curve-verification MAE
  `0.003536 deg`;
- curve-verification decision: verified exploratory baseline, not promoted over the
  accepted paper-derived, `tree`, or `Wave 2.2` periodic sequence leaders;
- design conclusion: a sequential residual offset head alone does not solve
  the curve-following gap; the next branch should test explicit offset
  calibration or multi-task offset/shape training.

### Wave 3.2. Harmonic-Offset Probe

- status: campaign completed after runner registration repair; official
  `TE Curve Verification Pipeline` matrix refresh completed;
- families:
  - `track2f_bis_clean_sequential_residual_offset_global`;
  - `track2f_bis_clean_sequential_residual_offset_fw`;
  - `track2f_bis_clean_sequential_residual_offset_bw`;
  - `track2f_bis_harmonic_residual_offset_global`;
  - `track2f_bis_harmonic_residual_offset_fw`;
  - `track2f_bis_harmonic_residual_offset_bw`;
- closeout report:
  `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-08]/track2_official_model_verification_report.md`;
- clean global candidate:
  `te_track2f_bis_clean_residual_offset_global`, scalar test MAE
  `0.003528 deg`;
- harmonic global candidate:
  `te_track2f_bis_harmonic_residual_offset_global`, scalar test MAE
  `0.003538 deg`;
- clean forward candidate:
  `te_track2f_bis_clean_residual_offset_fw`, scalar test MAE
  `0.003446 deg`;
- harmonic forward candidate:
  `te_track2f_bis_harmonic_residual_offset_fw`, scalar test MAE
  `0.002862 deg`;
- clean backward candidate:
  `te_track2f_bis_clean_residual_offset_bw`, scalar test MAE
  `0.003540 deg`;
- harmonic backward candidate:
  `te_track2f_bis_harmonic_residual_offset_bw`, scalar test MAE
  `0.003336 deg`;
- strongest Wave 3.2 forward candidate:
  `track2f_bis_harmonic_residual_offset_Fw`, curve-verification MAE `0.002850 deg`;
- strongest Wave 3.2 backward candidate:
  `track2f_bis_harmonic_residual_offset_Bw`, curve-verification MAE `0.003331 deg`;
- strongest Wave 3.2 global candidate:
  `track2f_bis_clean_sequential_residual_offset_global`, combined curve-verification MAE
  `0.003522 deg`;
- curve-verification decision: verified exploratory baseline, not promoted over the
  accepted paper-derived, `tree`, or `Wave 2.2` periodic sequence leaders;
- design conclusion: harmonic forcing helps the direction-specific `Fw` and
  `Bw` branches, but the harmonic global model improves forward behavior while
  degrading backward behavior; the next branch should use curve-aware loss or
  multi-task shape/offset training rather than relying on harmonic forcing
  alone.

### Wave 4.1. Dispersion-Aware Robust-Loss Probe

- status: robust-loss campaign completed; official `TE Curve Verification Pipeline` matrix refresh
  completed as a `141`-candidate direction-aware verification package;
- families:
  - `track2h_dispersion_aware_mae_robust_global`;
  - `track2h_dispersion_aware_mae_robust_fw`;
  - `track2h_dispersion_aware_mae_robust_bw`;
  - `track2h_dispersion_aware_smooth_l1_robust_global`;
  - `track2h_dispersion_aware_smooth_l1_robust_fw`;
  - `track2h_dispersion_aware_smooth_l1_robust_bw`;
  - `track2h_dispersion_aware_log_cosh_robust_global`;
  - `track2h_dispersion_aware_log_cosh_robust_fw`;
  - `track2h_dispersion_aware_log_cosh_robust_bw`;
- closeout report:
  `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-11]/track2_official_model_verification_report.md`;
- robust global candidate:
  `te_track2h_mae_robust_global`, scalar test MAE `0.003406 deg`;
- robust forward candidate:
  `te_track2h_mae_robust_fw`, scalar test MAE `0.003146 deg`;
- robust backward candidate:
  `te_track2h_smooth_l1_robust_bw`, scalar test MAE `0.003074 deg`;
- campaign scalar winner:
  `te_track2h_smooth_l1_robust_bw`;
- TE Curve Verification Pipeline strongest forward candidate:
  `track2h_mae_robust_Fw`, curve-verification MAE `0.003134 deg`;
- TE Curve Verification Pipeline strongest backward candidate:
  `track2h_smooth_l1_robust_Bw`, curve-verification MAE `0.003078 deg`;
- TE Curve Verification Pipeline strongest global candidate:
  `track2h_mae_robust_global`, curve-verification MAE `0.003401 deg`;
- curve-verification decision: verified exploratory baseline, not promoted over the
  accepted direction-parallel leaders;
- design conclusion: robust losses are useful enough to keep in the
  dispersion-aware plan, especially on `Bw`, but are not sufficient by
  themselves; the next package should move to quantile or probabilistic
  regression before mixture-density and latent-state variants.

### Wave 4.2. Quantile Probabilistic Probe

- status: quantile/probabilistic campaign completed; official `TE Curve Verification Pipeline` matrix
  refresh completed as a `147`-candidate direction-aware verification package;
- families:
  - `track2h_quantile_probabilistic_quantile_p10_p50_p90_global`;
  - `track2h_quantile_probabilistic_quantile_p10_p50_p90_fw`;
  - `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw`;
  - `track2h_quantile_probabilistic_gaussian_nll_global`;
  - `track2h_quantile_probabilistic_gaussian_nll_fw`;
  - `track2h_quantile_probabilistic_gaussian_nll_bw`;
- closeout report:
  `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-12]/track2_official_model_verification_report.md`;
- strongest probabilistic global candidate:
  `track2h_gaussian_nll_global`, combined curve-verification MAE `0.003009 deg`;
- strongest probabilistic forward-only candidate:
  `track2h_gaussian_nll_Fw`, curve-verification MAE `0.003156 deg`;
- strongest probabilistic forward-evaluated candidate:
  `track2h_gaussian_nll_global`, curve-verification MAE `0.002951 deg`;
- strongest probabilistic backward candidate:
  `track2h_quantile_p10_p50_p90_Bw`, curve-verification MAE `0.002935 deg`;
- curve-verification decision: verified exploratory baseline, not promoted over the
  accepted direction-parallel leaders;
- design conclusion: probabilistic losses improve over robust losses on the
  best `global` and `Bw` TE Curve Verification Pipeline surfaces, and MDN improves the best Wave 4 series
  `Bw` branch further, but the accepted periodic temporal branch remains
  stronger; MDN is a verified exploratory baseline, so the next default branch
  is the first real `Wave 5.1` hybrid structured campaign unless
  latent-state / hysteresis-aware compensation is explicitly prioritized.

### Wave 4.3. Mixture Density Heads Probe

- status: mixture-density heads campaign completed; official `TE Curve Verification Pipeline` matrix
  refresh completed;
- families:
  - `track2h_mixture_density_heads_mdn_k2_global`;
  - `track2h_mixture_density_heads_mdn_k2_fw`;
  - `track2h_mixture_density_heads_mdn_k2_bw`;
  - `track2h_mixture_density_heads_mdn_k3_global`;
  - `track2h_mixture_density_heads_mdn_k3_fw`;
  - `track2h_mixture_density_heads_mdn_k3_bw`;
- closeout report:
  `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-13]/track2_official_model_verification_report.md`;
- matrix output:
  `output/validation_checks/track2_reference_comparison/2026-06-13-17-24-53__track2_full_directional_family_matrix_track2h_mixture_density_heads_track2_refresh_2026_06_13/`;
- strongest MDN global candidate:
  `te_track2h_mdn_k2_global`, scalar test MAE `0.003503 deg`;
- strongest MDN forward candidate:
  `te_track2h_mdn_k3_fw`, scalar test MAE `0.003235 deg`;
- strongest MDN backward candidate:
  `te_track2h_mdn_k2_bw`, scalar test MAE `0.002658 deg`;
- strongest TE Curve Verification Pipeline forward MDN candidate:
  `track2h_mdn_k3_Fw`, curve MAE `0.003226 deg`;
- strongest TE Curve Verification Pipeline backward MDN candidate:
  `track2h_mdn_k2_Bw`, curve MAE `0.002668 deg`;
- strongest TE Curve Verification Pipeline global MDN candidate:
  `track2h_mdn_k2_global`, combined curve MAE `0.003499 deg`;
- campaign scalar winner:
  `te_track2h_mdn_k2_bw`;
- program scalar winner changed: no, `te_periodic_gru_sequence_remote_Bw`
  remains stronger with test MAE `0.002344 deg`;
- curve-verification decision: verified exploratory baseline, not promoted over the
  accepted direction-parallel leaders;
- design conclusion: MDN improves the scalar `Bw` dispersion-aware branch by
  `9.19%` versus the previous best probabilistic `Bw` result and by about
  `13.5%` versus the robust-loss `Bw` result; the official curve-verification matrix
  confirms the same backward advantage, but MDN is weaker on `global` and `Fw`;
  mixture diagnostics show effective component counts near `1.0`, so the
  result should be treated as useful MDN training pressure, not confirmed
  learned multimodality.

### Wave 4.4. Latent-State Hysteresis Probe

- status: latent-state / hysteresis-aware campaign completed; official
  `TE Curve Verification Pipeline` matrix refresh completed as a verified exploratory baseline, not
  promoted;
- families:
  - `track2h_latent_state_hysteresis_gru_offset_residual_global`;
  - `track2h_latent_state_hysteresis_gru_offset_residual_fw`;
  - `track2h_latent_state_hysteresis_gru_offset_residual_bw`;
  - `track2h_latent_state_hysteresis_causal_tcn_offset_residual_global`;
  - `track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw`;
  - `track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw`;
- closeout report:
  `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-17-01-27-10_track2h_latent_state_hysteresis_campaign_results_report.md`;
- official TE curve-verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-18]/track2_official_model_verification_report.md`;
- official curve-verification matrix:
  `165` candidates; source label `track2h_latent_state_hysteresis_registry`;
- strongest `Wave 4.4` global candidate:
  `te_track2h_l_causal_tcn_offset_residual_global`, scalar test MAE
  `0.003368 deg`;
- strongest `Wave 4.4` forward candidate:
  `te_track2h_l_causal_tcn_offset_residual_fw`, scalar test MAE
  `0.003470 deg`;
- strongest `Wave 4.4` backward candidate:
  `te_track2h_l_gru_offset_residual_bw`, scalar test MAE `0.003545 deg`;
- campaign scalar winner:
  `te_track2h_l_causal_tcn_offset_residual_global`;
- program scalar winner changed: no, `te_periodic_gru_sequence_remote_Bw`
  remains stronger with test MAE `0.002344 deg`;
- scalar comparison: `Wave 4.4` improves the `global` scalar surface versus MDN
  and robust-loss `global` baselines, but remains behind the Gaussian-NLL
  probabilistic `global` candidate and is weaker than existing `Fw` and `Bw`
  dispersion-aware leaders;
- official TE Curve Verification Pipeline strongest refreshed candidates:
  `track2h_l_causal_tcn_offset_residual_global`, combined curve MAE
  `0.003372 deg`;
  `track2h_l_causal_tcn_offset_residual_Fw`, forward curve MAE
  `0.003476 deg`; and `track2h_l_gru_offset_residual_Bw`, backward curve MAE
  `0.003542 deg`;
- curve-verification decision: verified exploratory baseline, not promoted over
  `rcim_retuned_GBM19_Fw`, `periodic_gru_sequence_Bw`, or the accepted global
  neural `periodic_gru_sequence_global`;
- design conclusion: causal history is useful as a diagnostic signal, but this
  first hidden-state package does not prove that latent-state or hysteresis
  modeling alone solves the dispersed-offset problem. Carry it forward as
  integration evidence for later multi-head designs, not as a promoted
  standalone branch.

### Wave 5.1. Hybrid Structured Models

- status: first real campaign closed successfully as a scalar training
  benchmark; official `TE Curve Verification Pipeline` curve verification completed as a verified
  exploratory baseline, not promoted;
- current scaffold:
  - model type: `wave3_harmonic_prior_residual`;
  - model class:
    `scripts/models/wave3_harmonic_prior_residual_network.py`;
  - dry-run skeleton checker:
    `scripts/campaigns/wave_3/run_wave3_embryonic_skeleton_checks.ps1`;
  - training-smoke-ready checker:
    `scripts/campaigns/wave_3/run_wave3_training_smoke_ready_checks.ps1`;
  - final one-batch validation artifact:
    `output/validation_checks/wave3_harmonic_prior_residual/2026-06-11-19-44-20__te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final/validation_summary.yaml`;
- prepared package:
  `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/`;
- prepared launcher:
  `scripts/campaigns/wave_3/run_wave3_harmonic_prior_residual_campaign.ps1`;
- campaign closeout report:
  `doc/reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md`;
- scalar training winner:
  `te_wave3_harmonic_prior_residual_pointwise_control_bw`
  (`test_mae=0.003363`, `test_rmse=0.003902`);
- scalar decision: no program-best promotion; the current program winner
  remains `te_periodic_gru_sequence_remote_Bw` (`test_mae=0.002344`);
- official TE Curve Verification Pipeline launcher:
  `scripts/campaigns/track_2/run_wave3_harmonic_prior_residual_track2_verification_refresh.ps1`;
- official TE curve-verification report:
  `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-15]/track2_official_model_verification_report.md`;
- strongest Wave 5.1 TE Curve Verification Pipeline candidate:
  `wave3_harmonic_prior_residual_pointwise_control_Bw`, curve-verification MAE
  `0.003360 deg`;
- updated priority: use the completed Wave 5.1 curve, offset, collage, overlay,
  and completed `Wave 4.4` official TE Curve Verification Pipeline evidence as baselines for the
  active Wave 5.2 full-PINN formulation program;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- paper-reproduction scope:
  - compare hybrid structured predictors against the paper-style harmonic stack;
  - test condition-conditioned residual structure and separate treatment of
    stable middle harmonics versus fragile low-order and high-order harmonics;
  - prepare the repository-owned deployable predictor package after the
    research branch has identified a viable structure.
- next implementation steps:
  - proceed to Wave 5.2 reference intake, equation audit, and formulation
    selection, with hidden-state modeling treated as verified exploratory
    evidence rather than a promoted branch.

### Wave 5.2. PINN Formulation And First PINN

- status: Phases 0 through 3 complete; Phase 4 active at the hysteresis,
  friction, and causal-memory feasibility gate;
- canonical roadmap:
  `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/full_pinn_physics_formulation_roadmap.md`;
- physics reference-intake register:
  `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/physics_reference_intake_register.md`;
- active general formulation families:
  - Polynomial-Fourier structured residual PINN;
  - harmonic-kinematic constraint PINN;
  - contact-regime or energy-consistency PINN where references and observable
    variables support the equations;
  - additional reference-derived formulations, kept separate until their
    assumptions are reconciled;
- full-PINN qualification rule:
  - training must contain an explicit differentiable physical residual,
    compatibility equation, or mathematically specified physical constraint;
  - harmonic features, Fourier heads, curve metrics, or ungrounded soft
    regularization alone do not qualify as a full PINN;
- active evidence base:
  - Waves 3.1 through 3.3 for offset, centered shape, slope, amplitude, phase,
    and curve-level objectives;
  - Waves 4.1 through 4.4 for robustness, uncertainty, mixture behavior, and
    causal state;
  - Wave 5.1 for harmonic priors and structured residual learning;
  - periodic GRU and periodic harmonic MLP as time-windowed and non-windowed
    comparison references;
  - the existing direction-specific Polynomial Fourier Series PLC
    implementation as the first semi-analytical formulation to audit;
- current scaffold:
  - diagnostic adapter:
    `scripts/models/wave4_mmt_diagnostic_adapter.py`;
  - diagnostic report builder:
    `scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py`;
  - parameter-inventory report builder:
    `scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.py`;
  - generated diagnostic report:
    `doc/reports/analysis/model_development_waves/wave_4/mmt_equation_diagnostic/[2026-06-11]/wave4a_mmt_equation_diagnostic.md`;
  - generated parameter-inventory report:
    `doc/reports/analysis/model_development_waves/wave_4/mmt_parameter_inventory/[2026-06-11]/wave4a_mmt_parameter_inventory.md`;
  - companion artifacts:
    `output/validation_checks/wave4_mmt_equation_diagnostic/2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic/`;
  - parameter-inventory artifacts:
    `output/validation_checks/wave4_mmt_parameter_inventory/2026-06-11-20-29-51__wave4a_mmt_parameter_inventory/`;
  - residual-explanatory diagnostic report:
    `doc/reports/analysis/model_development_waves/wave_5_2/mmt_residual_explanatory_diagnostic/[2026-07-24]/wave52_mmt_residual_explanatory_diagnostic.md`;
  - leakage-safe residual-explanatory rerun:
    `doc/reports/analysis/model_development_waves/wave_5_2/mmt_residual_explanatory_diagnostic/[2026-07-24]/wave52_mmt_residual_explanatory_rerun.md`;
- updated priority: audit chronological state observability and repeated
  reversal-cycle support before selecting any Phase 4 pilot. Keep formulations
  that lack real causal state in synthetic or offline-oracle lanes;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- paper-reproduction scope:
  - prepare explicit PINN model and physics-loss formulations for later
    offline and deployment evaluation;
  - test whether soft physics, periodicity, smoothness, harmonic-consistency,
    and operating-condition constraints reduce offset and fragile-harmonic
    errors;
  - keep online compensation execution out of Wave 5.2 unless Track 3 is
    explicitly promoted first.
- completed inventory conclusions:
  - known geometry constants are safe for diagnostics and feature generation;
  - operating metadata can be used for stratification and causal conditioning;
  - five equivalent-error groups are train-only calibratable;
  - contact geometry remains unavailable or ambiguous and blocks calibrated
    analytical-baseline claims;
  - measured TE remains target-only and must not become an inference input.
- MMT-specific closed implementation conclusions:
  - exact-manifest replay preserves all archived model artifacts and split
    memberships;
  - 224 metadata, geometry, combined, and shuffled comparisons were fitted on
    training residuals and evaluated on validation and test;
  - geometry-locked MMT signatures produced zero incremental held-out gain;
  - 56 calibrated equivalent-error arms were explicitly blocked because
    causal component-error and contact-state inputs are unavailable;
  - no MMT feature, auxiliary-output, weak-loss, or paper-faithful MMT
    full-PINN pilot is justified by current evidence.
- MMT future TODO reopening gate:
  - obtain independent component-error measurements or a validated causal
    contact-state reconstruction;
  - prove that the resulting MMT inputs vary by operating condition without
    using validation or test TE targets;
  - create a new technical document and, if training is proposed, a new
    campaign plan before reactivation;
  - until those conditions are met, the MMT-paper-faithful subbranch is not
    part of active model development and does not block the general Wave 5.2
    full-PINN program.
- general full-PINN evidence gates:
  - register and synthesize each supplied reference;
  - verify equations, units, assumptions, observability, identifiability,
    differentiability, and causal inference-time availability;
  - test equations against measured curves and synthetic or analytical oracles
    where possible;
  - prepare a separate approved technical document and campaign plan for one
    bounded formulation pilot;
  - apply multi-index curve-first verification before accepting, combining, or
    rejecting a formulation;
  - use validated findings to define the later Wave 6 architecture.

### Wave 5. Cross-Wave Comparison And Best Solution

- status: pending;
- mandatory rule: preserve direction-separated reporting;
- paper-reproduction scope:
  - compare closed offline waves and Track 3 results when available;
  - finalize the real `paper vs repository` comparison only after Track 3
    closes `Target B`.

### Track 3. Online Compensation And Deployment Evaluation

- status: future implementation branch;
- canonical objective: close `Target B`;
- scope:
  - online compensation loop in the TestRig / TwinCAT path;
  - old future Pipelines `8-10`;
  - `Robot` and `Cycloidal` motion-profile validation;
  - uncompensated versus compensated `TE RMS` and `TE max`;
  - final paper-style `Table 9` report;
  - deployment-readiness interpretation for the selected repository model path.

## Decision Notes

- the live backlog is the privileged operational view of the TE program;
- technical documents remain the historical planning baseline and design
  rationale;
- output artifacts follow the privileged category-specific structure rather
  than the old flat family-root convention;
- best-result visibility should be read from campaign-level
  `campaign_best_run.yaml`, family-level `latest_family_best.yaml`, and
  program-level `current_best_solution.yaml`;
- the recovered original workflow is provenance evidence, while curated
  `models/paper_reference/` archives are the active comparison surface;
- `RCIM Model-Bank Reproduction` is closed under the revised closure rule and should not be reopened
  for all-green optimization;
- `TE Curve Verification Pipeline` is the canonical offline verification baseline; diagnostic
  extensions now continue as CVP 1.1, CVP 1.2, mean-centered collage, and
  completed `CVP 1.4`;
- the general Wave 5.2 full-PINN program has completed Phases 0 through 3 and
  is active at the Phase 4 feasibility gate; the paper-faithful MMT subbranch
  alone remains an inactive future TODO after
  `blocked_by_parameter_availability`;
- Wave 6 follows bounded PINN formulation evidence and is no longer the
  immediate next design branch;
- the polished actual-values RCIM prerequisite is complete across the six
  expected `GRU` / `LSTM` and `global` / `Fw` / `Bw` archive cells; the next
  reduced evaluation can move to technical planning;
- future wave planning must keep direction-separated modeling and reporting in
  scope from the start;
- Track 3 is the future online compensation and deployment-evaluation branch;
  it absorbs `Target B`, old future Pipelines `8-10`, and the deferred TwinCAT
  deployment-evaluation scope;
- future updates to program status should land here whenever:
  - a wave starts or finishes;
  - a model family is promoted or deferred;
  - a campaign is approved, started, completed, or cancelled;
  - the current best candidate changes;
  - a paper-alignment target changes state;
  - Track 3 is promoted, deferred, or updated with a selected deployment path.
