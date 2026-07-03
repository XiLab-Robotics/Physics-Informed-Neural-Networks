# CVP 1.1 Curve-First Reranking

## Overview

This document plans the `CVP 1.1 Curve-First Reranking` branch. The branch
will not train new models. It will rerank already accepted repository and
paper-reference candidates on an expanded curve-first offline verification
surface.

The goal is to answer a specific modeling question before opening any new
training campaign:

- which existing candidates best follow complete TE curves for compensation;
- whether the scalar registry winner remains strong under curve-first
  evidence;
- whether harmonic or periodic candidates are better practical starting points
  for later curve-aware training despite less favorable pointwise scalar
  metrics.

The runtime input constraint remains unchanged. Candidate models consume only
the current point-level operating state, an explicitly supported short causal
history, or derived causal features. Full curves are used for validation,
diagnostics, reranking, and promotion only.

No subagent is planned for this phase.

## Technical Approach

The implementation should extend the existing TE curve evaluation surface rather
than creating a new training path.

The branch should:

- reuse the current TE Curve Verification Pipeline candidate inventory and direction rules;
- evaluate accepted `Wave 1`, `Wave 2.1`, `Wave 2.2`, `Wave 2.3`, `RCIM Model-Bank Reproduction`,
  recovered original, and retuned paper-reference candidates;
- preserve the `global`, `Fw`, and `Bw` direction-valid policy;
- compute scalar curve metrics already present in TE Curve Verification Pipeline;
- add curve-first diagnostics where feasible without retraining:
  - P95 and worst-condition percentage error;
  - peak-to-peak normalized curve error;
  - derivative or local-slope error;
  - selected-harmonic amplitude error;
  - selected-harmonic phase error;
  - residual smoothness or residual autocorrelation indicators;
- produce a reranked report that separates:
  - scalar registry winner;
  - curve-first offline winner;
  - deployment-plausible candidate;
  - candidates needing retraining or loss changes.

The first implementation should be conservative. If some diagnostics are too
expensive or not robust in the first pass, the report should mark them as
deferred rather than blocking the reranking.

The reranking should not update family registries or program-best registries
automatically. It should create analysis evidence first. Registry promotion or
new training should remain a later approved step.

## Involved Components

Primary documentation targets:

- `doc/reports/analysis/te_curve_verification_pipeline/`
- `doc/reports/analysis/te_modeling/strategy/Curve-First TE Training Strategy.md`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `doc/README.md`

Primary implementation targets to inspect:

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `scripts/reports/analysis/plot_wave1_best_model_te_curves.py`
- curve-verification matrix and reference comparison scripts under
  `scripts/paper_reimplementation/rcim_ml_compensation/`
- current curve-verification matrix templates under
  `config/paper_reimplementation/rcim_ml_compensation/`

Primary data and artifact inputs:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-05-28]/track2_official_model_verification_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-28]/track2_best_model_collage_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-28]/track2_multi_model_curve_comparison_report.md`
- latest TE Curve Verification Pipeline validation summaries under
  `output/validation_checks/track2_reference_comparison/`
- family registries under `output/registries/families/`
- program registry under `output/registries/program/`
- exported candidate artifacts under `models/`

## Implementation Steps

1. Inspect the current TE Curve Verification Pipeline scripts, matrix templates, validation summaries,
   and per-condition metric outputs.
2. Identify the latest canonical `Wave 2.3` curve-verification matrix output as the
   baseline candidate set.
3. Design a CVP 1.1 output bundle under `doc/reports/analysis/te_curve_verification_pipeline/` and
   `output/validation_checks/track2_curve_first_reranking/`.
4. Implement or adapt a repository-owned script that computes the expanded
   curve-first metric bundle without changing candidate model inputs.
5. Generate a Markdown analysis report that includes:
   - method;
   - candidate inventory;
   - direction-separated curve-first rankings;
   - scalar winner versus curve-first winner comparison;
   - harmonic/phase diagnostic interpretation;
   - recommended next branch.
6. Refresh visual overlay or collage artifacts only if the reranked screened
   candidate set differs materially from the current TE Curve Verification Pipeline visual reports.
7. Update the live backlog and master summary with the CVP 1.1 conclusion.
8. Run Markdown QA on touched authored Markdown.
9. Run Sphinx with warnings as errors if the touched scope affects the portal.
10. Stop after reporting completion; do not commit until the user explicitly
    requests it.

The expected next decision after CVP 1.1 is one of:

- accept an existing candidate as the curve-first offline leader;
- prepare a compact `Wave 1B` curve-aware static retraining pass;
- prepare a compact `Wave 2.1D` curve-aware periodic sequence retraining pass;
- defer model changes and move the selected candidate toward deployment
  readiness checks.
