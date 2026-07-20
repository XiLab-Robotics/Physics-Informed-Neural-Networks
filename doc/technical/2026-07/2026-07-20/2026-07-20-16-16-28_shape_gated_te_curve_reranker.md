# Shape-Gated TE Curve Reranker

## Overview

This technical document plans a shape-gated reranker for the reduced
forward/backward `TE Curve Verification Pipeline` active set.

The immediate goal is not to open a new training campaign. The goal is to make
the current shape-first selection policy mechanical enough that scalar
improvements cannot promote a candidate that loses measured transmission-error
curve shape, dominant harmonic content, phase behavior, derivative behavior, or
per-curve consistency.

The reduced active set is:

- temporal-window baseline: `periodic_gru_sequence_Fw` and
  `periodic_gru_sequence_Bw`;
- primary non-windowed candidate: `wave4_1_mae_robust_loss_Fw` and
  `wave4_1_mae_robust_loss_Bw`;
- secondary non-windowed uncertainty-aware candidate:
  `wave4_2_quantile_p10_p50_p90_Fw` and
  `wave4_2_quantile_p10_p50_p90_Bw`;
- lightweight harmonic comparator: `periodic_mlp_harmonic_Fw` and
  `periodic_mlp_harmonic_Bw`;
- reference anchors from simple baseline families and the applicable
  `RCIM Model-Bank Reproduction` archives.

The active selection remains forward-led and backward-checked. The `global`
surface is preserved as official historical evidence, but it is not part of
this reduced reranking pass unless a later approval explicitly reopens it.

No subagent is planned for this implementation.

## Technical Approach

The reranker will reuse existing `TE Curve Verification Pipeline` evidence
where possible instead of regenerating a broad full matrix. It should consume
measured-versus-predicted curve payloads and the selected-model candidate list
from repository-owned artifacts, then produce a ranked forward/backward report
with machine-readable scoring outputs.

The scoring policy should separate required diagnostic measurements from final
promotion rules:

- raw operating error remains visible through curve `MAE`, curve `RMSE`, and
  percentage-error summaries;
- shape fidelity is measured after mean-centering or equivalent offset
  separation, so vertical bias does not hide curve-shape failures;
- frequency-domain evidence measures spectral similarity, dominant harmonic
  amplitude retention, and dominant harmonic phase error;
- derivative evidence measures local curve-direction agreement through
  derivative correlation or a stable equivalent;
- per-curve shape pass rate reports how often the candidate satisfies the
  configured shape thresholds across the selected held-out curves.

The first implementation pass should keep the gate conservative and
inspectable:

1. compute all available metrics per candidate, direction, and held-out curve;
2. normalize metric values within each direction-specific comparison set;
3. emit transparent block scores for raw error, centered shape, harmonic and
   phase fidelity, derivative behavior, offset behavior, and robustness;
4. assign veto flags when required shape or provenance evidence is missing;
5. demote scalar leaders that fail the shape gate instead of allowing scalar
   `MAE` to dominate the recommendation;
6. produce both a human-readable report and a CSV or YAML metric table.

The reranker must treat validation-time curve diagnostics as diagnostics only.
No full-curve truth, mean-centering result, FFT summary, or residual statistic
may be described as deployable runtime information unless a future feature
reformulates it as a causal predictor.

The planned output should support these decision labels:

- `recommended_candidate`;
- `best_raw_error`;
- `best_shape_fidelity`;
- `best_harmonic_fidelity`;
- `best_offset_behavior`;
- `best_robustness`;
- `shape_gate_failed`;
- `baseline_anchor_only`;
- `insufficient_evidence`.

## Involved Components

Read-only evidence sources:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`;
- `doc/reports/analysis/model_development_waves/intermediate_model_selection_cleanup/[2026-07-17]/te_intermediate_model_selection_cleanup_report.md`;
- `doc/technical/2026-07/2026-07-19/2026-07-19-17-15-50_selected_models_track2_full_report_refresh.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`;
- current selected-model report bundles under
  `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/`;
- relevant `output/validation_checks/` and `output/registries/` artifacts;
- relevant exported models under `models/`.

Likely implementation targets after approval:

- a repository-owned analysis script under `scripts/reports/analysis/` or the
  existing selected-model report builder if the reranker naturally belongs
  there;
- a configuration or candidate-list surface if the current selected active set
  is not already encoded in a reusable way;
- a dated report bundle under
  `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-20]/`
  or a narrower `03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/`
  bundle if diagnostics are separated from the selected-model report;
- machine-readable metric artifacts in the same report bundle;
- `doc/README.md` registration for any new canonical report bundle.

Protected-file check:

- `doc/running/active_training_campaign.yaml` records the
  `rcim_track1` polished actual-values campaign as completed.
- The protected file list belongs to that closed campaign package, launcher,
  launcher note, campaign plan, and campaign technical document.
- This reranker work must not modify protected campaign files unless the user
  gives a separate explicit approval.

No training campaign, training-related experiment, remote launch, campaign
YAML, or PowerShell campaign launcher is part of this plan.

## Implementation Steps

1. Create this technical document and register it from `doc/README.md`.
2. Wait for explicit user approval before modifying Python scripts,
   candidate-list configuration, generated reports, or machine-readable
   artifacts.
3. Inspect the current selected-model report builder, existing CVP diagnostic
   metric artifacts, and selected-model launcher to identify the narrowest
   implementation point.
4. Verify the exact reduced active candidate list for `Fw` and `Bw` against
   current model archives and report artifacts.
5. Implement the metric extraction layer for centered shape, FFT amplitude
   similarity, dominant-harmonic retention, dominant-harmonic phase error,
   derivative correlation, offset behavior, raw error, and per-curve pass rate.
6. Implement transparent direction-specific normalization, block scores, veto
   flags, and final recommendation labels.
7. Generate the reduced forward/backward shape-gated reranking report and
   machine-readable metric outputs.
8. Run Python validation or compile checks for touched scripts.
9. Run Markdown style and Markdownlint checks on every touched authored
   Markdown file.
10. Stop and report completion. Do not commit until the user explicitly
    approves a commit.
