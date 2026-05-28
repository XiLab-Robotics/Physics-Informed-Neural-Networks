# Curve-First TE Training Strategy

## Overview

The current training program has produced useful `Wave 1`, `Wave 2`,
`Wave 2B`, and `Wave 2C` comparisons, but the repository still ranks most
campaign winners through scalar validation or test metrics such as `MAE`.
That is not sufficient for the final compensation target.

The real application is continuous Transmission Error compensation during
motor motion. At operating speeds such as `1000 rpm`, the deployed predictor
will not be judged as an isolated point regressor. It must produce stable,
cycle-after-cycle TE curves for many consecutive revolutions while preserving
phase, amplitude, smoothness, direction handling, and operating-condition
dependence.

This does not change the runtime input contract. Deployed candidates must
consume only the current point-level state, an explicitly supported short
history of already observed samples, or derived causal features. Complete
curves are used for validation, diagnostics, and promotion, not as future
information supplied to the model.

This task will clarify the documentation and design the next training strategy
around curve-following quality rather than pointwise score alone. The first
implementation phase is documentation and research only. Any later training
campaign, campaign YAML generation, launcher creation, or model-code change
must pass the normal technical-document and campaign-plan gates.

No subagent is planned for this phase.

## Technical Approach

The work should reframe the repository target as curve-first TE compensation:

- Track 2 should become the canonical offline benchmark surface for selecting
  deployment-relevant candidates.
- Campaign leaderboards should keep scalar `MAE` and `RMSE`, but should no
  longer treat them as sufficient evidence when curve shape diverges from the
  measured TE.
- Model selection should distinguish pointwise dataset fit from full-curve
  reconstruction quality.
- Visual curve evidence should be standardized so that a candidate like `tree`
  cannot be promoted only because its tabular scalar error is strong if its
  curve shape is materially worse than structured harmonic candidates.

The research phase should evaluate these candidate strategy classes:

1. Curve-level selection metrics.
   Use Track 2 style per-curve `MAE`, `RMSE`, mean percentage error, P95
   per-curve error, worst-condition error, and direction-separated summaries as
   promotion metrics. This is the lowest-risk first step because it changes
   selection policy and campaign reporting before changing model families.

2. Shape-aware curve metrics.
   Evaluate derivative error, curvature error, peak/trough error, phase
   offset, amplitude error, peak-to-peak normalized error, and local
   correlation. These metrics directly target the visible curve mismatch the
   operator sees in Track 2 overlays.

3. Frequency-domain and harmonic metrics.
   Compare measured and predicted curves in harmonic space: amplitude error,
   phase error, selected-harmonic weighted error, spectral leakage, and
   high-frequency penalty. This aligns with the RCIM paper structure and with
   TwinCAT-friendly harmonic reconstruction.

4. Training losses for neural models.
   Explore composite losses that combine pointwise normalized-space loss with
   curve-level shape terms, derivative terms, and frequency-domain terms.
   Soft-DTW and related differentiable alignment losses are research
   candidates, but should be handled carefully because TE compensation should
   usually preserve physical phase rather than freely time-warp it.

5. Data and split changes.
   Build validation batches around complete curves or multi-curve windows
   instead of only pointwise shuffled samples. Preserve direction, speed,
   torque, oil temperature, angular position, and `DataValid` semantics.

6. Post-training selection and reranking.
   Add a Track 2 reranking stage that evaluates all candidate checkpoints or
   run winners on the full held-out curve surface before accepting
   `campaign_best_run.yaml`, family registries, and program-best status.

7. New model-family direction.
   Treat new algorithms as a later wave only after the metric and selection
   surface is fixed. Candidate families include structured harmonic banks with
   curve-aware regularization, periodic sequence models with harmonic losses,
   spline/Fourier functional regressors, Gaussian-process or kernel baselines,
   lightweight state-space sequence models, and deployment-oriented hybrid
   harmonic residual models.

The likely first implementation branch after documentation is a small
`Wave 1B` or `Track 2B` selection-policy refresh, not immediate new model
architecture work. The first branch should standardize curve-first metrics and
rerank existing `Wave 1`, `Wave 2`, `Wave 2B`, and `Wave 2C` artifacts. Only
after that should a `Wave 1B` or `Wave 2B/2D` retraining campaign change losses
or data loaders.

## Involved Components

Documentation and planning targets:

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/wave2/Wave 2 Temporal Sequence Models.md`
- `doc/reports/analysis/wave2/Wave 2B Harmonic Temporal Hybrid Models.md`
- `doc/reports/analysis/wave2/Wave 2C Residual Harmonic Temporal Hybrid Models.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-05-28]/track2_official_model_verification_report.md`
- `doc/reports/analysis/te_modeling/Twincat-Friendly Structured TE Modeling.md`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/05_Data_Series_Explanation_Project_Summary.md`

Implementation surfaces to inspect before any later approved code change:

- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/train_tree_regressor.py`
- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/run_training_campaign.py`
- `scripts/reports/analysis/plot_wave1_best_model_te_curves.py`
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- Track 2 validation scripts and matrix templates under
  `scripts/paper_reimplementation/rcim_ml_compensation/` and
  `config/paper_reimplementation/rcim_ml_compensation/`.

Reference and research anchors:

- RCIM paper summary: online TE compensation, TwinCAT deployment, and
  harmonic representation.
- Data-series summary: `DataValid`, direction handling, zeroing, and valid
  curve windows.
- Track 2 official verification reports: held-out curve metrics and visual
  evidence.
- External time-series shape literature: differentiable time-series distances,
  shape-aware matching, frequency-domain training objectives, and functional
  curve regularization.

## Implementation Steps

1. Audit current documentation for places that still describe the project as
   primarily pointwise `MAE` optimization.
2. Update the documentation to state the real target: continuous TE curve
   prediction for compensation over many consecutive motor revolutions.
3. Add a curve-first evaluation policy that separates:
   training loss, checkpoint selection, campaign-best selection, Track 2
   promotion, and deployment-readiness.
4. Create a strategy report under `doc/reports/analysis/te_modeling/` that
   compares the candidate techniques and recommends the first implementation
   branch.
5. Standardize the recommended Track 2 curve-first benchmark contract:
   direction-valid held-out curves, per-curve metrics, visual overlays,
   worst-case and P95 summaries, harmonic/phase diagnostics, and promotion
   rules.
6. Define the first approved follow-up branch as either:
   a documentation-only Track 2 selection-policy refresh, a reranking pass over
   existing runs, or a new campaign plan for curve-aware retraining.
7. Run Markdown QA on touched authored Markdown files.
8. If the documentation changes affect the Sphinx portal scope, rebuild the
   portal with warnings as errors.

The recommended first technical decision is to avoid jumping directly to a new
model family. The immediate gap is the objective and selection contract: the
repository needs a curve-first benchmark and reranking policy before retraining
or adding later waves.
