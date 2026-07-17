# Intermediate Model Selection Cleanup

## Overview

This technical document plans an intermediate model-selection cleanup report
after the dataset/input-mode retraining program completed for all non-RCIM
model-development families.

The requested work is not a final project decision and does not delete
historical artifacts. The goal is to reduce the active development surface so
future work carries only families that either improve the target-to-beat or
remain technically useful for deeper implementation work.

The report must preserve two active modeling paths:

- at least one temporal-window model family, such as `GRU` or `LSTM`;
- at least one non-windowed model family, so the program can compare the
  deployment and input-contract tradeoff introduced by temporal context.

## Technical Approach

The analysis will use the already generated familywise
`TE Curve Verification Pipeline` ONNX reports, with
`polished_dataset + setpoints` as the primary evidence surface.
`polished_dataset + actual_values` will be used as a sensitivity check only
when it materially changes the recommendation.

The decision logic follows the existing forward-led pruning policy:

- ignore `global` for model selection;
- use `forward` as the primary decision driver;
- use `backward` as a consistency check;
- accept a different backward candidate only when the evidence gap is
  substantial and documented.

The report will score raw error, centered-shape fidelity, offset behavior, and
robustness, then apply a shape-first gate before accepting any model as an
active path. A low aggregate `MAE` is not sufficient when the familywise
collage shows smoothed, shifted, or missing harmonic content.

The Markdown iteration will use existing aggregate metrics and the official
familywise collages as the conservative shape screen. A later implementation
should add mechanical FFT/phase metrics to the report pipeline: harmonic
amplitude retention, spectral cosine similarity, weighted phase error,
derivative correlation, and per-curve shape pass rate.

No training, heavy matrix refresh, subagent, or PDF export is planned for this
first Markdown iteration. PDF export will wait until the user approves the
final candidate selection.

## Involved Components

Read-only evidence sources:

- `doc/reports/analysis/model_development_waves/model_family_pruning/[2026-07-06]/te_model_family_pruning_decision_report.md`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`
- `output/validation_checks/track2_familywise_onnx_report/`
- `.temp/track2_selection_refresh_2026_07_17/`

Authored outputs:

- `doc/reports/analysis/model_development_waves/intermediate_model_selection_cleanup/[2026-07-17]/te_intermediate_model_selection_cleanup_report.md`
- report-local plots under
  `doc/reports/analysis/model_development_waves/intermediate_model_selection_cleanup/[2026-07-17]/assets/`
- report-local CSV evidence tables under the same dated bundle.

Protected-file check:

- `doc/running/active_training_campaign.yaml` records the latest campaign as
  completed and the current non-RCIM retraining scope as complete.
- The planned files are not listed in the protected refresh file list.
- No protected campaign file, training config, model export, or report builder
  will be edited in this Markdown-only pass.

## Implementation Steps

1. Create this technical document and register it from `doc/README.md`.
2. Copy the diagnostic selection plots and CSV summaries into a report-local
   dated bundle.
3. Write the intermediate selection cleanup report with a forward-led,
   backward-checked decision.
4. Explicitly keep at least one temporal-window path and one non-windowed path.
5. Apply the shape-first correction, including demotion of scalar leaders that
   do not preserve measured curve shape.
6. Identify dead-end branches to close, baseline-only branches to preserve, and
   future development branches worth deeper work.
7. Run Markdown QA on the touched Markdown scope.
8. Report completion and wait for user review before PDF export or commit.
