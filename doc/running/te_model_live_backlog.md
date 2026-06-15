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
- Active Campaign State: none; the last completed campaign is recorded in
  `doc/running/active_training_campaign.yaml`.
- Current Completed Wave: `Wave 3` harmonic-prior residual campaign closeout
  is complete as a scalar training benchmark; official `Track 2` verification
  for the new candidates remains a separate optional acceptance step.
- Current Completed Track: `Track 1` RCIM paper-faithful model bank, closed as
  a faithful full-bank reproduction surface for Tables `2`-`5`.
- Current Completed Track: `Track 2` official offline model-verification
  report, closed as the canonical direction-aware verification surface for new
  model families.
- Current Focus: prepare the separate official `Track 2` verification refresh
  for the six completed `Wave 3` harmonic-prior residual candidates, then use
  curve-first evidence to decide whether to continue `Wave 3`, move to
  `Wave 4`, or reopen latent-state / hysteresis-aware modeling.
- Parallel Diagnostic Focus: component-offset, `Track 2D` h0 cross-check, and
  predicted-mean versus measured-h0 diagnostics are complete; `h0` is the
  correct mean-like channel to inspect, but not the confirmed sole cause of the
  offset failures.
- Current Best Implemented Families: tracked separately for `Fw`, `Bw`, and
  `global`; scalar and curve-first surfaces are not a single ranking.
- Current Best Implemented Run Registry:
  `output/registries/program/current_best_solution.yaml`.

Current canonical status reports:

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-06-13]/track2_official_model_verification_report.md`
- `doc/reports/analysis/track2/best_model_collage_report/[2026-06-13]/track2_best_model_collage_report.md`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-13]/track2_multi_model_curve_comparison_report.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md`
- `doc/reports/analysis/track2/curve_payload_diagnostics_report/[2026-05-28]/track2_curve_payload_diagnostics_report.md`
- `doc/reports/analysis/track2/mean_centered_collage_report/[2026-06-02]/track2_mean_centered_collage_report.md`
- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`
- `doc/reports/analysis/track2/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md`
- `doc/reports/analysis/track2/component_offset_identification_plan/[2026-06-09]/track2_component_offset_identification_plan.md`
- `doc/reports/analysis/track2/component_offset_identification/[2026-06-09]/track2_component_offset_identification_diagnostic.md`
- `doc/reports/analysis/track2/component_offset_identification/[2026-06-09]/track2d_h0_offset_crosscheck.md`
- `doc/reports/analysis/track2/component_offset_identification/[2026-06-10]/track2d_predicted_mean_h0_surface_diagnostic.md`
- `doc/reports/campaign_results/track2/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md`
- `doc/reports/campaign_results/track2/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md`
- `doc/reports/campaign_results/track2/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md`
- `doc/reports/campaign_results/wave3_wave4/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md`
- `doc/reports/campaign_results/track2/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`
- `doc/reports/analysis/Training Results Master Summary.md`

## Directional Rule

The repository now treats direction as a first-class evaluation surface.

The default rule for `Track 2`, `Wave 1`, and all future waves is:

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

The immediate rule is:

- scalar `MAE` and `RMSE` remain required sanity metrics;
- `Track 2` direction-valid full-curve metrics are the canonical promotion
  surface for deployment-relevant comparison;
- visual overlays and collage evidence must be considered when scalar metrics
  and curve shape disagree;
- mean-centered diagnostics must be interpreted as post-prediction analysis,
  not as a deployment-valid runtime correction;
- raw curve error, curve-bias / `DC` offset error, centered-shape error,
  amplitude error, and harmonic phase error should be tracked separately;
- harmonic amplitude, harmonic phase, P95, and worst-condition diagnostics
  should be added before new training losses are treated as canonical.

This rule does not reopen closed campaigns. It changes how future branches
interpret their evidence and defines future work as three parallel
direction-valid selection surfaces while preserving the causal input contract.

The first standardized reranking pass is complete in:

- `doc/reports/analysis/track2/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md`

Current `Track 2B` curve-first leaders by parallel surface:

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

- `doc/reports/analysis/track2/curve_payload_diagnostics_report/[2026-05-28]/track2_curve_payload_diagnostics_report.md`

Current `Track 2C` diagnostic observations:

| Finding | Interpretation |
| --- | --- |
| `rcim_retuned_GBM19_Fw` keeps the best screened diagnostic score. | It remains the strongest forward paper-reference curve-shape baseline. |
| `periodic_gru_sequence_Bw` is the strongest practical repository-owned backward candidate. | It is close to `rcim_retuned_GBM19_Bw` on mean percentage error and much better on selected harmonic phase. |
| `periodic_lstm_sequence_global` is the strongest screened global-surface neural candidate. | It is the best current global neural starting point for a deployable cross-direction branch. |
| `harmonic_regression_Bw` has the cleanest backward harmonic amplitude/phase diagnostics but worse scalar and peak-to-peak error. | It is useful as a structured diagnostic reference, not the next direct promotion target. |
| `tree` candidates remain weak on peak-to-peak and shape diagnostics. | The next direction-parallel training work should not start from `tree` despite scalar strength. |

The first mean-centered collage diagnostic is complete in:

- `doc/reports/analysis/track2/mean_centered_collage_report/[2026-06-02]/track2_mean_centered_collage_report.md`

Current mean-offset observations:

| Finding | Interpretation |
| --- | --- |
| `harmonic_regression_global` improves from `0.031130 deg` raw MAE to `0.000888 deg` centered MAE on the four-curve collage. | Vertical offset is a dominant raw-error component for this candidate; centered shape is much better than raw MAE suggests. |
| `periodic_lstm_sequence_global`, `periodic_temporal_convolution_global`, and `periodic_gru_sequence_global` also improve strongly after mean-centering. | Several temporal neural candidates need offset and centered-shape diagnostics reported separately. |
| Dense `Wave 2C` variants improve much less after mean-centering. | Their limitation is not only offset; centered shape, amplitude, or phase quality remains weak. |
| Full-curve mean-centering uses information unavailable at runtime. | It is a diagnostic decomposition, not a deployable correction. |

The next approved work should therefore first diagnose all three best-model
surfaces in parallel:

| Surface | Current evidence | Practical next action |
| --- | --- | --- |
| `Fw` | paper-reference `rcim_retuned_GBM19_Fw` leads current curve diagnostics. | Run Track 2D offset, centered-shape, amplitude, phase, and condition audit before selecting a forward retraining family. |
| `Bw` | `periodic_gru_sequence_Bw` is the strongest practical repository-owned backward candidate. | Run Track 2D to decide whether the backward issue is offset-limited or shape-limited before retraining periodic temporal models. |
| `global` | `periodic_lstm_sequence_global` is the strongest screened global neural candidate. | Keep a dedicated global branch and audit offset/shape separately instead of folding it into the backward winner. |

Full-curve diagnostics remain strictly post-prediction and must preserve the
causal runtime input contract.

The `Track 2D` full-matrix audit is complete in:

- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`

Current `Track 2D` observations:

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
| `Track 2D Mean-Offset Full-Matrix Audit` | Apply raw, offset, centered-shape, amplitude, harmonic phase, and condition-stratified metrics to the full official Track 2 candidate matrix. | completed |
| Offset-aware checkpoint selection | Monitor curve-bias, centered-shape, P95, harmonic phase, then scalar `val_mae`. | next decision candidate |
| Curve-aware loss branch | Add pointwise, bias, centered-shape, slope, harmonic amplitude, and harmonic phase terms while preserving causal inputs. | next decision candidate |
| Component-offset identification | Test whether curve offset is dominated by `a_0` / `Component 0`, multiple components, condition/regime behavior, or experimental repeatability limits. | measured `h0`, signed-offset cross-check, and predicted-mean surface diagnostics completed; `h0` is the right mean channel, but the actionable issue is model-side mean-surface bias/compression |
| `Track 2H` dispersion-aware modeling probes | Test robust losses, quantile or probabilistic heads, mixture-density heads, and latent-state or hysteresis-aware features on the offset and fragile-harmonic problem. | robust-loss, quantile/probabilistic, and MDN campaigns plus official Track 2 refreshes completed; latent-state / hysteresis-aware remains an optional alternate branch |
| `Wave 3` hybrid structured models | Combine harmonic structure, condition-conditioned residual learning, and explicit grouped treatment of stable and fragile harmonic bands. | first real `wave3_harmonic_prior_residual` campaign closed successfully as a scalar benchmark; separate official `Track 2` verification is the next acceptance gate |
| `Wave 4` PINN formulation and first PINN | Test soft physics, periodicity, smoothness, harmonic-consistency, and operating-condition constraints in a first narrow PINN branch. | `Wave 4A` MMT diagnostic and parameter inventory are generated; dataset-aligned calibration and `Wave 4B` / `Wave 4C` decision gates remain open |
| Integrated multi-task / multi-head model branch | Shared causal trunk with separate offset, low-frequency, centered-shape, uncertainty or mixture, and optional structured-residual heads. | deferred until `Track 2H`, `Wave 3`, and `Wave 4` identify which mechanisms should be integrated |
| Sequential residual calibration branch | Current best causal model plus second causal residual or offset calibrator trained on model error. | candidate after audit |

The `Track 2E` offset-predictability feasibility diagnostic is complete in:

- `doc/reports/analysis/track2/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md`

Current `Track 2E` observations:

| Finding | Interpretation |
| --- | --- |
| The conservative best causal grouping is `direction_torque`, not the exact full operating condition. | Offset has a condition-linked signal, but exact full-condition memorization must not be treated as deployable predictability. |
| `harmonic_regression_global` shows the largest conservative offset-correction feasibility gain, but remains amplitude/phase limited. | It is useful as an offset probe reference, not as an automatic global production winner. |
| `rcim_retuned_XGBM19_Bw` and `LGBM19_Fw` are the strongest per-surface sequential-offset feasibility probes. | The next branch should test offset modeling behavior per surface without collapsing `Fw`, `Bw`, and `global` into one competition. |
| Most candidates fall into `multi_head_shape_offset`, `posthoc_offset_baseline`, or `not_offset_first` rather than a clean sequential-offset path. | The next training plan should include offset, centered-shape, amplitude, and phase terms instead of assuming offset correction alone solves the curve-following problem. |

Recommended next gate:

- run a separate official `Track 2` verification refresh for the six completed
  `Wave 3` harmonic-prior residual candidates before any promotion decision;
- keep latent-state / hysteresis-aware modeling as an optional alternate
  `Track 2H` branch only if explicitly prioritized before `Wave 3`;
- treat `Wave 3` hybrid structured models and `Wave 4` first-PINN formulation
  as evidence-generating branches before the integrated multi-task /
  multi-head architecture; `Wave 4` resumes from the `Wave 4A` MMT diagnostic
  report, completed parameter inventory, and dataset-aligned calibration gate;
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
  and Track 2 comparison matrix.

Operational meaning:

- forward `Track 1` cells compare against the better value between paper
  original and paper retuned;
- backward `Track 1` cells compare against paper retuned, because the paper
  does not provide backward original tables.

### Track 1 RCIM Paper-Faithful Model Bank

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

- `Track 1` is closed because the faithful full-bank protocol was run in both
  directions and all benchmark cells were repopulated.
- Green-only status is not a `Track 1` closure requirement.
- Any all-green pursuit, restricted-dataset rerun, or target-parameterization
  search is a new optimization branch, not a reopening of closed `Track 1`.

Artifact rule:

- intermediate validation-model `.pkl` bundles under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
  and
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`
  stay out of Git tracking and Git LFS;
- only curated accepted archives under `models/paper_reference/rcim_track1/`
  are the `Track 1` paper-reference model surface.

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
- future `Wave 1B` work should first rerank accepted artifacts on Track 2
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

### Track 2 Directional Offline Comparison

Status:

- closed as the official offline model-verification report.

Canonical report:

- `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/track2_official_model_verification_report.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Current comparison surface:

- comparison mode: `full_directional_candidate_matrix`;
- candidate count: `84`;
- held-out curve count before candidate filtering: `194`;
- denominator for percentage error: `peak_to_peak_truth`;
- `Fw` candidates evaluate only on forward curves;
- `Bw` candidates evaluate only on backward curves;
- `global` candidates evaluate on both directions with separated metrics.

Candidate groups:

- accepted `Track 1` forward and backward family banks;
- recovered original forward family banks;
- retuned forward and backward family banks;
- `Wave 1` exported `global`, `forward`, and `backward` models;
- `Wave 2` temporal `global`, `forward`, and `backward` registry models;
- composed best-reference candidates for paper original, paper retuned, and
  `Track 1`.

Current Track 2 leaders by source:

| Direction | Source | Candidate | Mean percentage error [%] |
| --- | --- | --- | ---: |
| forward | paper original | `paper_original_best_Fw` | 6.250 |
| forward | paper retuned | `paper_retuned_best_Fw` | 4.109 |
| forward | Track 1 | `track1_best_Fw` | 6.819 |
| backward | paper retuned | `paper_retuned_best_Bw` | 7.572 |
| backward | Track 1 | `track1_best_Bw` | 11.860 |

Backward baseline rule:

- the paper does not provide a paper-original backward reference surface;
- `paper_retuned_best_Bw` is therefore the canonical paper-derived backward
  baseline for `Track 2` and `Target A`;
- future backward comparisons should report against this retuned baseline
  unless a later approved technical document defines a stronger backward paper
  proxy.

Best individual family candidates currently visible in Track 2:

| Direction | Candidate | Mean percentage error [%] |
| --- | --- | ---: |
| forward | `rcim_retuned_GBM19_Fw` | 2.372 |
| backward | `rcim_retuned_GBM19_Bw` | 5.398 |

Official closeout package:

- the official verification report consolidates the direction-aware metric
  matrix, best-model collage PDF, multi-model curve comparison PDF, and future
  `Track 2` campaign update ledger;
- future model-verification updates must refresh the matrix, visual reports,
  official PDF, and this backlog before new candidates are accepted.

## Next Up

### Planned Next Step

After the completed `Track 2B`, `Track 2C`, mean-centered collage,
`Track 2D` full-matrix, h0/error cross-check, predicted-mean h0 surface
diagnostics, and completed `Track 2H` robust/probabilistic/MDN refreshes, the
active next step is:

- prepare the first real `Wave 3` harmonic-prior residual campaign before any
  integrated multi-head campaign;
- use the completed `Track 2H` probes as loss-policy evidence, not as the
  final architecture;
- keep latent-state / hysteresis-aware modeling available as an alternate
  branch if preload or protocol-state behavior is explicitly prioritized;
- then execute `Wave 4` first-PINN work as a separate evidence-generating
  branch;
- only after those probes decide which mechanisms belong in the integrated
  multi-task / multi-head architecture.

The previous temporal refresh answered three concrete questions:

- best temporal forward candidate: `gru_sequence_Fw` at `7.378%` mean error;
- best temporal backward candidate: `lstm_sequence_Bw` at `7.767%` mean error;
- final decision: temporal models are verified exploratory baselines and are
  not promoted over `tree`.

### Post-Track-2 Decision

Default decision path after Track 2 closeout:

- treat Track 2 curve-following quality as the promotion surface for future
  compensation-relevant candidates;
- use completed `Track 2D Mean-Offset Full-Matrix Audit` before changing model
  families, checkpoint monitors, or training losses;
- use the completed h0 diagnostics to keep `h0` as the primary mean-surface
  channel while avoiding the unsupported claim that it is the only cause;
- test dispersion-aware losses and heads, hybrid structured models, and a
  first PINN before committing to a large integrated multi-head architecture;
- preserve causal runtime inputs: point-level state, optional short past
  history, and causal derived features only;
- keep `Wave 2` temporal models as verified exploratory baselines;
- keep the same `global`, `forward`, and `backward` surface rule for Wave 2;
- use `Wave 1` and Track 2 as the comparison baseline for every Wave 2 family;
- keep paper-alignment bridge work available only if the user explicitly
  reopens a narrower offline paper-alignment question before temporal-model
  exploration.

### Paper Alignment Targets

`Target A`: match or beat the paper on a comparable offline prediction
benchmark.

Status:

- closed as `closed_offline_direction_qualified`.
- closeout source of truth:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`.

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
  strongest Track 2 offline family references;
- `Track 1` remains closed as faithful reproduction evidence, not as the
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

- deferred until Track 2 is closed or explicitly promoted.

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

### Track 1 Restricted-Dataset Future Rerun

Status:

- deferred until much later.

Entry rule:

- do not use this branch to overwrite the closed full-dataset `Track 1` status;
- create new campaign names, output roots, archive namespaces, and comparison
  reports for every restricted-dataset level.

Required scope if promoted:

- rerun the closed `Track 1` paper-faithful model-bank protocol on one or more
  restricted dataset variants;
- keep the current full-dataset `Track 1` archive and benchmark as immutable
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

- Track 3 is not `Wave 3`; `Wave 3` remains an offline hybrid structured-model
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

### Track 1. RCIM Paper-Faithful Model Bank

- recovered original workflow: preserved;
- original-dataset reimplementation: completed;
- retuned reference archive: completed;
- forward campaign: completed;
- backward campaign: completed;
- paper-reference archives: refreshed;
- Tables `2`-`5`: repopulated;
- status: closed as faithful full-bank reproduction, not all-green
  optimization.

### Track 2. Directional Offline Comparison

- direction-aware loader and candidate matrix: completed;
- recovered original forward candidates: included;
- retuned forward and backward candidates: included;
- `Track 1` forward and backward candidates: included;
- `Wave 1` `global`, `forward`, and `backward` exports: included;
- `Wave 2` temporal `global`, `forward`, and `backward` registry candidates:
  included;
- grouped source tables: completed;
- composite best-reference visibility: completed;
- direction/truth and preview audit: completed;
- official model-verification report: completed;
- curve-first reranking policy: planned as the next analysis branch;
- status: closed.

### Wave 2. Temporal Models

- status: entry campaign completed; closeout report prepared; official
  `Track 2` refresh completed;
- initial families: `temporal_convolution`, `gru_sequence`, `lstm_sequence`;
- configuration root: `config/training/hydra/wave2/`;
- preliminary campaign plan:
  `doc/reports/campaign_plans/wave2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md`;
- closeout report:
  `doc/reports/campaign_results/wave2/2026-05-24-12-36-49_wave2_temporal_model_entry_campaign_results_report.md`;
- campaign winner: `te_gru_sequence_remote_Fw` from family
  `gru_sequence_fw`, with test MAE `0.003333 deg`;
- refresh plan:
  `doc/reports/analysis/track2/wave2_temporal_model_refresh_plan/[2026-05-24]/track2_wave2_temporal_model_refresh_plan.md`;
- official verification report:
  `doc/reports/analysis/track2/official_model_verification_report/[2026-05-24]/track2_official_model_verification_report.md`;
- Track 2 decision: verified exploratory baselines, not promoted over `tree`;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- baseline comparison: Track 2 plus closed Wave 1.

### Wave 2B. Harmonic Temporal Hybrid Models

- status: harmonic-temporal hybrid campaign completed; normal closeout report
  prepared; official `Track 2` refresh completed;
- families: `periodic_temporal_convolution`, `periodic_gru_sequence`,
  `periodic_lstm_sequence`;
- configuration root:
  `config/training/wave2b_harmonic_temporal_hybrid/`;
- preliminary campaign plan:
  `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`;
- closeout report:
  `doc/reports/campaign_results/wave2/2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report.md`;
- campaign winner: `te_periodic_gru_sequence_remote_Bw` from family
  `periodic_gru_sequence_bw`, with test MAE `0.002344 deg`;
- strongest bidirectional candidate: `te_periodic_gru_sequence_remote_global`
  from family `periodic_gru_sequence`, with test MAE `0.002681 deg`;
- Track 2 decision: strongest repository-owned neural branch after official
  verification; `periodic_gru_sequence_Bw` is the strongest backward-only
  candidate and `periodic_gru_sequence_global` is the strongest global neural
  candidate;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- baseline comparison: official Track 2 matrix plus visual collage and overlay
  reports.

### Wave 2C. Residual Harmonic Temporal Hybrid Models

- status: residual harmonic temporal hybrid campaign completed; official
  `Track 2` refresh completed;
- families: `residual_harmonic_gru_sequence`,
  `residual_harmonic_lstm_sequence`;
- harmonic banks: sparse `RCIM`, dense `240`, dense `360`;
- closeout report:
  `doc/reports/campaign_results/wave2/2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/track2/official_model_verification_report/[2026-05-28]/track2_official_model_verification_report.md`;
- strongest Wave 2C forward candidate:
  `residual_harmonic_gru_sequence_sparse_rcim_Fw`, Track 2 MAE
  `0.003194 deg`;
- strongest Wave 2C backward candidate:
  `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, Track 2 MAE
  `0.003440 deg`;
- strongest Wave 2C global candidate:
  `residual_harmonic_lstm_sequence_sparse_rcim_global`, Track 2 MAE
  `0.003368 deg`;
- Track 2 decision: verified exploratory baseline, not promoted over the
  `Wave 2B` periodic sequence leaders;
- design conclusion: sparse `RCIM` harmonics remain useful, while dense `240`
  and dense `360` harmonic banks are not competitive for this residual
  temporal branch.

### Track 2F. Offset-Aware Sequential Residual Probe

- status: offset-aware probe campaign completed; official `Track 2` matrix
  refresh completed;
- family: `sequential_residual_offset_probe`;
- official verification report:
  `doc/reports/analysis/track2/official_model_verification_report/[2026-06-04]/track2_official_model_verification_report.md`;
- strongest Track 2F forward candidate:
  `sequential_residual_offset_probe_Fw`, Track 2 MAE `0.003377 deg`;
- strongest Track 2F backward candidate:
  `sequential_residual_offset_probe_Bw`, Track 2 MAE `0.003636 deg`;
- strongest Track 2F global candidate:
  `sequential_residual_offset_probe_global`, combined Track 2 MAE
  `0.003536 deg`;
- Track 2 decision: verified exploratory baseline, not promoted over the
  accepted paper-derived, `tree`, or `Wave 2B` periodic sequence leaders;
- design conclusion: a sequential residual offset head alone does not solve
  the curve-following gap; the next branch should test explicit offset
  calibration or multi-task offset/shape training.

### Track 2F-Bis. Harmonic-Offset Probe

- status: campaign completed after runner registration repair; official
  `Track 2` matrix refresh completed;
- families:
  - `track2f_bis_clean_sequential_residual_offset_global`;
  - `track2f_bis_clean_sequential_residual_offset_fw`;
  - `track2f_bis_clean_sequential_residual_offset_bw`;
  - `track2f_bis_harmonic_residual_offset_global`;
  - `track2f_bis_harmonic_residual_offset_fw`;
  - `track2f_bis_harmonic_residual_offset_bw`;
- closeout report:
  `doc/reports/campaign_results/track2/2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/track2/official_model_verification_report/[2026-06-08]/track2_official_model_verification_report.md`;
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
- strongest Track 2F-bis forward candidate:
  `track2f_bis_harmonic_residual_offset_Fw`, Track 2 MAE `0.002850 deg`;
- strongest Track 2F-bis backward candidate:
  `track2f_bis_harmonic_residual_offset_Bw`, Track 2 MAE `0.003331 deg`;
- strongest Track 2F-bis global candidate:
  `track2f_bis_clean_sequential_residual_offset_global`, combined Track 2 MAE
  `0.003522 deg`;
- Track 2 decision: verified exploratory baseline, not promoted over the
  accepted paper-derived, `tree`, or `Wave 2B` periodic sequence leaders;
- design conclusion: harmonic forcing helps the direction-specific `Fw` and
  `Bw` branches, but the harmonic global model improves forward behavior while
  degrading backward behavior; the next branch should use curve-aware loss or
  multi-task shape/offset training rather than relying on harmonic forcing
  alone.

### Track 2H. Dispersion-Aware Robust-Loss Probe

- status: robust-loss campaign completed; official `Track 2` matrix refresh
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
  `doc/reports/campaign_results/track2/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/track2/official_model_verification_report/[2026-06-11]/track2_official_model_verification_report.md`;
- robust global candidate:
  `te_track2h_mae_robust_global`, scalar test MAE `0.003406 deg`;
- robust forward candidate:
  `te_track2h_mae_robust_fw`, scalar test MAE `0.003146 deg`;
- robust backward candidate:
  `te_track2h_smooth_l1_robust_bw`, scalar test MAE `0.003074 deg`;
- campaign scalar winner:
  `te_track2h_smooth_l1_robust_bw`;
- Track 2 strongest forward candidate:
  `track2h_mae_robust_Fw`, Track 2 MAE `0.003134 deg`;
- Track 2 strongest backward candidate:
  `track2h_smooth_l1_robust_Bw`, Track 2 MAE `0.003078 deg`;
- Track 2 strongest global candidate:
  `track2h_mae_robust_global`, Track 2 MAE `0.003401 deg`;
- Track 2 decision: verified exploratory baseline, not promoted over the
  accepted direction-parallel leaders;
- design conclusion: robust losses are useful enough to keep in the
  dispersion-aware plan, especially on `Bw`, but are not sufficient by
  themselves; the next package should move to quantile or probabilistic
  regression before mixture-density and latent-state variants.

### Track 2H. Quantile Probabilistic Probe

- status: quantile/probabilistic campaign completed; official `Track 2` matrix
  refresh completed as a `147`-candidate direction-aware verification package;
- families:
  - `track2h_quantile_probabilistic_quantile_p10_p50_p90_global`;
  - `track2h_quantile_probabilistic_quantile_p10_p50_p90_fw`;
  - `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw`;
  - `track2h_quantile_probabilistic_gaussian_nll_global`;
  - `track2h_quantile_probabilistic_gaussian_nll_fw`;
  - `track2h_quantile_probabilistic_gaussian_nll_bw`;
- closeout report:
  `doc/reports/campaign_results/track2/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/track2/official_model_verification_report/[2026-06-12]/track2_official_model_verification_report.md`;
- strongest probabilistic global candidate:
  `track2h_gaussian_nll_global`, combined Track 2 MAE `0.003009 deg`;
- strongest probabilistic forward-only candidate:
  `track2h_gaussian_nll_Fw`, Track 2 MAE `0.003156 deg`;
- strongest probabilistic forward-evaluated candidate:
  `track2h_gaussian_nll_global`, Track 2 MAE `0.002951 deg`;
- strongest probabilistic backward candidate:
  `track2h_quantile_p10_p50_p90_Bw`, Track 2 MAE `0.002935 deg`;
- Track 2 decision: verified exploratory baseline, not promoted over the
  accepted direction-parallel leaders;
- design conclusion: probabilistic losses improve over robust losses on the
  best `global` and `Bw` Track 2 surfaces, and MDN improves the best Track 2H
  `Bw` branch further, but the accepted periodic temporal branch remains
  stronger; MDN is a verified exploratory baseline, so the next default branch
  is the first real `Wave 3` hybrid structured campaign unless
  latent-state / hysteresis-aware compensation is explicitly prioritized.

### Track 2H. Mixture Density Heads Probe

- status: mixture-density heads campaign completed; official `Track 2` matrix
  refresh completed;
- families:
  - `track2h_mixture_density_heads_mdn_k2_global`;
  - `track2h_mixture_density_heads_mdn_k2_fw`;
  - `track2h_mixture_density_heads_mdn_k2_bw`;
  - `track2h_mixture_density_heads_mdn_k3_global`;
  - `track2h_mixture_density_heads_mdn_k3_fw`;
  - `track2h_mixture_density_heads_mdn_k3_bw`;
- closeout report:
  `doc/reports/campaign_results/track2/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md`;
- official verification report:
  `doc/reports/analysis/track2/official_model_verification_report/[2026-06-13]/track2_official_model_verification_report.md`;
- matrix output:
  `output/validation_checks/track2_reference_comparison/2026-06-13-17-24-53__track2_full_directional_family_matrix_track2h_mixture_density_heads_track2_refresh_2026_06_13/`;
- strongest MDN global candidate:
  `te_track2h_mdn_k2_global`, scalar test MAE `0.003503 deg`;
- strongest MDN forward candidate:
  `te_track2h_mdn_k3_fw`, scalar test MAE `0.003235 deg`;
- strongest MDN backward candidate:
  `te_track2h_mdn_k2_bw`, scalar test MAE `0.002658 deg`;
- strongest Track 2 forward MDN candidate:
  `track2h_mdn_k3_Fw`, curve MAE `0.003226 deg`;
- strongest Track 2 backward MDN candidate:
  `track2h_mdn_k2_Bw`, curve MAE `0.002668 deg`;
- strongest Track 2 global MDN candidate:
  `track2h_mdn_k2_global`, combined curve MAE `0.003499 deg`;
- campaign scalar winner:
  `te_track2h_mdn_k2_bw`;
- program scalar winner changed: no, `te_periodic_gru_sequence_remote_Bw`
  remains stronger with test MAE `0.002344 deg`;
- Track 2 decision: verified exploratory baseline, not promoted over the
  accepted direction-parallel leaders;
- design conclusion: MDN improves the scalar `Bw` dispersion-aware branch by
  `9.19%` versus the previous best probabilistic `Bw` result and by about
  `13.5%` versus the robust-loss `Bw` result; the official Track 2 matrix
  confirms the same backward advantage, but MDN is weaker on `global` and `Fw`;
  mixture diagnostics show effective component counts near `1.0`, so the
  result should be treated as useful MDN training pressure, not confirmed
  learned multimodality.

### Wave 3. Hybrid Structured Models

- status: first real campaign closed successfully as a scalar training
  benchmark; official `Track 2` curve verification remains pending as a
  separate acceptance step;
- current scaffold:
  - model type: `wave3_harmonic_prior_residual`;
  - model class:
    `scripts/models/wave3_harmonic_prior_residual_network.py`;
  - dry-run skeleton checker:
    `scripts/campaigns/wave3/run_wave3_embryonic_skeleton_checks.ps1`;
  - training-smoke-ready checker:
    `scripts/campaigns/wave3/run_wave3_training_smoke_ready_checks.ps1`;
  - final one-batch validation artifact:
    `output/validation_checks/wave3_harmonic_prior_residual/2026-06-11-19-44-20__te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final/validation_summary.yaml`;
- prepared package:
  `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/`;
- prepared launcher:
  `scripts/campaigns/wave3/run_wave3_harmonic_prior_residual_campaign.ps1`;
- campaign closeout report:
  `doc/reports/campaign_results/wave3_wave4/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md`;
- scalar training winner:
  `te_wave3_harmonic_prior_residual_pointwise_control_bw`
  (`test_mae=0.003363`, `test_rmse=0.003902`);
- scalar decision: no program-best promotion; the current program winner
  remains `te_periodic_gru_sequence_remote_Bw` (`test_mae=0.002344`);
- updated priority: prepare official `Track 2` verification for the six
  completed Wave 3 candidates before any integration into the later
  multi-task / multi-head campaign, unless latent-state / hysteresis-aware
  compensation is explicitly prioritized as the next Track 2H branch;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- paper-reproduction scope:
  - compare hybrid structured predictors against the paper-style harmonic stack;
  - test condition-conditioned residual structure and separate treatment of
    stable middle harmonics versus fragile low-order and high-order harmonics;
  - prepare the repository-owned deployable predictor package after the
    research branch has identified a viable structure.
- next implementation steps:
  - prepare a separate official `Track 2` verification refresh launcher for
    the completed Wave 3 candidates;
  - run it only after explicit approval and operator launch;
  - use the resulting curve, offset, collage, and overlay evidence to decide
    whether Wave 3 should continue, feed multi-head integration, or yield
    priority to `Wave 4` / latent-state modeling.

### Wave 4. PINN Formulation And First PINN

- status: pre-implemented at `Wave 4A` diagnostic level, not campaign-ready;
- current scaffold:
  - diagnostic adapter:
    `scripts/models/wave4_mmt_diagnostic_adapter.py`;
  - diagnostic report builder:
    `scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py`;
  - parameter-inventory report builder:
    `scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.py`;
  - generated diagnostic report:
    `doc/reports/analysis/wave4/mmt_equation_diagnostic/[2026-06-11]/wave4a_mmt_equation_diagnostic.md`;
  - generated parameter-inventory report:
    `doc/reports/analysis/wave4/mmt_parameter_inventory/[2026-06-11]/wave4a_mmt_parameter_inventory.md`;
  - companion artifacts:
    `output/validation_checks/wave4_mmt_equation_diagnostic/2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic/`;
  - parameter-inventory artifacts:
    `output/validation_checks/wave4_mmt_parameter_inventory/2026-06-11-20-29-51__wave4a_mmt_parameter_inventory/`;
- updated priority: execute dataset-aligned diagnostic calibration after the
  `Wave 3` smoke/campaign decision, then decide whether `Wave 4B` features or
  `Wave 4C` soft losses are justified;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- paper-reproduction scope:
  - prepare PINN-side model and loss formulations for later offline and
    deployment evaluation;
  - test whether soft physics, periodicity, smoothness, harmonic-consistency,
    and operating-condition constraints reduce offset and fragile-harmonic
    errors;
  - keep online compensation execution out of Wave 4 unless Track 3 is
    explicitly promoted first.
- completed inventory conclusions:
  - known geometry constants are safe for diagnostics and feature generation;
  - operating metadata can be used for stratification and causal conditioning;
  - five equivalent-error groups are train-only calibratable;
  - contact geometry remains unavailable or ambiguous and blocks calibrated
    analytical-baseline claims;
  - measured TE remains target-only and must not become an inference input.
- next implementation steps:
  - compare MMT diagnostic signatures against dataset-aligned curve summaries
    without leakage;
  - design a train-only equivalent-error calibration policy for candidate
    `Wave 4B` features;
  - decide whether the MMT path remains diagnostic-only, becomes a feature
    generator (`Wave 4B`), or becomes a weak soft-constraint loss (`Wave 4C`);
  - do not treat the current demonstration harmonic summary as dataset
    causality.

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
- `Track 1` is closed under the revised closure rule and should not be reopened
  for all-green optimization;
- `Track 2` is the canonical offline verification baseline; diagnostic
  extensions now continue as Track 2B, Track 2C, mean-centered collage, and
  completed `Track 2D`;
- the next planned branch before any new broad model-family wave is an
  offset-aware training or calibration design selected from the completed
  Track 2D failure-mode labels;
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
