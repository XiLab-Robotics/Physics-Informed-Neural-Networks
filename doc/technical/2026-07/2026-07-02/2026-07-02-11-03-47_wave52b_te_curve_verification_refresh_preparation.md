# Wave 5.2B TE Curve Verification Pipeline Refresh Preparation

## Overview

This technical document defines the approved preparation scope for adding the
completed `Wave 5.2B` offset and harmonic guided campaign to the official
`TE Curve Verification Pipeline` refresh workflow.

The normal campaign closeout is already complete:

- Campaign: `wave52b_offset_harmonic_guided_campaign_2026_07_01`
- Completed runs: `12`
- Failed runs: `0`
- Dataset: `polished_dataset`
- Dataset schema: `polished_point_v1`
- Closeout report:
  `doc/reports/campaign_results/wave_5_2/2026-07-02-10-40-46_wave52b_offset_harmonic_guided_campaign_results_report.md`
- Scalar campaign winner:
  `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw`

This work must not infer official promotion from scalar campaign metrics. The
refresh must use the repository's multi-index curve-first policy and keep
`global`, `Fw`, and `Bw` surfaces visible.

This document prepares the workflow only. The heavy `TE Curve Verification
Pipeline` matrix must be launched by the operator through a repository-owned
PowerShell launcher after explicit approval.

## Technical Approach

The refresh will add the best Wave 5.2B candidates to the official directional
matrix through registry-backed model entries, then regenerate official curve
verification evidence after the operator-run matrix completes.

Candidate scope:

- `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global`
- `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw`
- `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw`

These three candidates represent the strongest Wave 5.2B profile on each
surface. Other Wave 5.2B ablation profiles remain scalar training evidence and
do not need to enter the official matrix unless a later review explicitly asks
for the full ablation set.

The preparation will:

1. inspect the completed campaign state and family registries;
2. inspect the current `TE Curve Verification Pipeline` matrix configuration
   and model-loading support;
3. add the three registry-backed Wave 5.2B candidates to the compact matrix
   configuration with correct direction semantics;
4. patch inference support only if the current registry-backed PyTorch path
   cannot load `wave52b_offset_harmonic_guided` models;
5. create a dedicated PowerShell launcher with local and `-Remote` modes;
6. create a launcher note documenting exact local and remote commands;
7. stop before running the heavy matrix and wait for operator completion;
8. after operator completion, inspect matrix artifacts, regenerate visual
   companion reports, create the dated official verification report, export and
   validate PDFs, and synchronize status documents.

No subagent is planned for this preparation. If a later implementation review
needs a subagent, the proposed subagent name, delegated scope, and approval
requirement must be declared before launch.

## Involved Components

Primary state and evidence:

- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/`
- `output/registries/families/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/latest_family_best.yaml`
- `output/registries/families/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/latest_family_best.yaml`
- `output/registries/families/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/latest_family_best.yaml`

Matrix and inference tooling:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`

Operator-facing refresh tooling to create:

- `scripts/campaigns/wave_5_2/run_wave52b_te_curve_verification_refresh.ps1`
- `doc/scripts/campaigns/wave_5_2/run_wave52b_te_curve_verification_refresh.md`

Post-run reports and status surfaces:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/best_model_collage_report/[YYYY-MM-DD]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[YYYY-MM-DD]/`
- `doc/reports/analysis/track2/official_model_verification_report/[YYYY-MM-DD]/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/TE Program Status And Closeout Ledger.md`
- `doc/README.md`

## Implementation Steps

1. Confirm `doc/running/active_training_campaign.yaml` has no active local
   campaign and that Wave 5.2B is the latest completed campaign.
2. Verify the three selected Wave 5.2B family registry files exist and point to
   completed run artifacts.
3. Inspect the current matrix template and support code before making any
   change.
4. Add three registry-backed candidates to the matrix:
   - global candidate with forward and backward evaluation;
   - `Fw` candidate with forward-only evaluation;
   - `Bw` candidate with backward-only evaluation.
5. If required, extend the shared model-loading support for
   `wave52b_offset_harmonic_guided` while preserving existing candidate
   behavior.
6. Create the dedicated launcher with:
   - default local execution;
   - `-Remote` execution through the repository remote-campaign workflow;
   - distinct output suffix for Wave 5.2B refresh artifacts;
   - no automatic execution during preparation.
7. Create the launcher note with exact commands and operator expectations.
8. Run lightweight validation only:
   - syntax checks for modified Python and PowerShell-adjacent scripts where
     applicable;
   - matrix package sanity checks that do not execute the heavy comparison;
   - Markdown checks on touched documentation.
9. Stop and report the exact local and `-Remote` launcher commands.
10. After the operator reports completion, inspect generated matrix artifacts,
    regenerate companion visual reports, write the official report, export and
    raster-validate PDFs, then synchronize backlog, master summary, and closeout
    ledger.
