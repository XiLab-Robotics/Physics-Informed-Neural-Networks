# Selected Models Track 2 Full Report Refresh

## Overview

This technical document plans a refreshed complete `TE Curve Verification
Pipeline` report using only the currently selected model families from the
`2026-07-17` shape-first intermediate cleanup.

The requested output is a complete Track 2-style report bundle for the reduced
active set, not a broad full-matrix regeneration over every trained family.
The report must preserve the current selection policy:

- use `forward` as the leading model-selection surface;
- use `backward` as the consistency and deployment-split check;
- keep `global` out of the active reduced selection report unless explicitly
  requested later;
- evaluate model families by curve fidelity, not scalar `MAE` alone;
- keep both a temporal-window path and a non-windowed path visible.

The current selected active families are:

- temporal-window path: `periodic_gru_sequence`;
- primary non-windowed path: `wave4_1_mae_robust_loss`;
- secondary uncertainty-aware non-windowed path:
  `wave4_2_quantile_p10_p50_p90`;
- lightweight harmonic comparator: `periodic_mlp_harmonic`;
- simple anchors: `tree`, `feedforward`, and `harmonic_regression`;
- RCIM reference candidates, including the latest polished actual-values
  `rcim_track1` archive where available.

## Technical Approach

The report refresh will inspect the existing selected-model launcher and
report-generation scripts before changing them. The intended output should be
placed under a new dated bundle in:

`doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-19]/`

The implementation should reuse repository-owned pipeline entry points where
possible:

- `scripts/campaigns/track_2/run_reduced_selected_track2_reports.ps1`;
- `scripts/reports/analysis/build_track2_selected_model_visual_reports.py`;
- `scripts/reports/pdf/run_report_pipeline.py`;
- `scripts/reports/pdf/generate_styled_report_pdf.py`;
- `scripts/reports/pdf/validate_report_pdf.py`.

Before generation, the selected candidate inventory must be verified against
the current exported model paths under `models/`, including dataset-specific
separation between `simplified_dataset`, `polished_dataset/setpoints`, and
`polished_dataset/actual_values`.

The report should include:

- exact selected model families and paths used;
- forward and backward selected-model metrics;
- curve visual evidence for the selected candidates;
- polished setpoint and polished actual-values comparisons where both are
  available;
- simplified setpoint references where they remain useful as baseline
  diagnostics;
- explicit notes that `periodic_lstm_sequence_Bw` is not an active selected
  candidate unless a future shape gate reopens it.

## Involved Components

Read-only evidence sources:

- `doc/reports/analysis/model_development_waves/intermediate_model_selection_cleanup/[2026-07-17]/te_intermediate_model_selection_cleanup_report.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-06]/`;
- `models/`;
- `output/validation_checks/`;
- `output/registries/`.

Likely authored or regenerated outputs:

- refreshed selected-model report Markdown and PDF files under the new dated
  `04_selected_model_reports/[2026-07-19]/` bundle;
- report-local visual assets and metric CSVs, if the selected-model pipeline
  produces them;
- possible narrow updates to selected-model report scripts or launcher
  candidate lists if they still encode the old `2026-07-06` reduced set;
- `doc/README.md` registration for the new report bundle if generated.

Protected-file check:

- `doc/running/active_training_campaign.yaml` currently records the
  `rcim_track1` polished actual-values campaign as completed.
- The protected file list is limited to the closed campaign package, launcher,
  launcher note, campaign plan, and campaign technical document.
- This report refresh must not modify those protected campaign files unless the
  user gives a separate explicit approval.

Subagents:

- No subagent is planned.

## Implementation Steps

1. Create this technical document and register it from `doc/README.md`.
2. Wait for explicit user approval before modifying report scripts, launcher
   configuration, or generated report outputs.
3. Inspect the existing selected-model launcher and report builder to identify
   where the current candidate set is encoded.
4. Verify the exact ONNX and Python model paths for the selected families under
   `models/`.
5. Regenerate the reduced selected-model `TE Curve Verification Pipeline`
   reports for the selected models only.
6. Add or update the styled PDF exports and validate the real exported PDFs.
7. Register the refreshed report bundle from `doc/README.md`.
8. Run Markdown QA on touched Markdown files and Python compile checks on any
   touched Python scripts.
9. Stop and report completion; do not commit until the user explicitly asks.
