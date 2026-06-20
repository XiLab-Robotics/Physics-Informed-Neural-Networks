# TE Curve Verification Pipeline Wave 2.1 Temporal Model Refresh Plan

## Overview

This plan defines the official `TE Curve Verification Pipeline` refresh needed after the completed
`Wave 2.1` temporal-model entry campaign.

The campaign produced trained `temporal_convolution`, `gru_sequence`, and
`lstm_sequence` candidates across `global`, `Fw`, and `Bw` surfaces. These
models are not accepted by TE Curve Verification Pipeline until the official direction-aware matrix,
best-model collages, multi-model overlays, and official verification report
are refreshed and reviewed.

## Source Campaign

| Field | Value |
| --- | --- |
| Campaign | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |
| Campaign output | `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |
| Completed runs | 9 |
| Failed runs | 0 |
| Campaign winner | `te_gru_sequence_remote_Fw` |
| Winner test MAE | 0.003333 |
| Winner test RMSE | 0.003881 |

## Candidate Scope

| Candidate | Family | Direction Scope | TE Curve Verification Pipeline Refresh Role |
| --- | --- | --- | --- |
| `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | `global` | matrix row |
| `te_temporal_convolution_sequence_remote_Fw` | `temporal_convolution_fw` | `Fw` | matrix row |
| `te_temporal_convolution_sequence_remote_Bw` | `temporal_convolution_bw` | `Bw` | matrix row |
| `te_gru_sequence_remote_global` | `gru_sequence` | `global` | matrix row |
| `te_gru_sequence_remote_Fw` | `gru_sequence_fw` | `Fw` | matrix row and priority visual candidate |
| `te_gru_sequence_remote_Bw` | `gru_sequence_bw` | `Bw` | matrix row |
| `te_lstm_sequence_remote_global` | `lstm_sequence` | `global` | matrix row and priority visual candidate |
| `te_lstm_sequence_remote_Fw` | `lstm_sequence_fw` | `Fw` | matrix row |
| `te_lstm_sequence_remote_Bw` | `lstm_sequence_bw` | `Bw` | matrix row and priority visual candidate |

## Required Refresh Outputs

| Output | Required Update | Acceptance Gate |
| --- | --- | --- |
| Directional matrix | add all `9` Wave 2.1 candidates with direction-correct evaluation | matrix generated without candidate-loading errors |
| Best-model collage report | add temporal winner collages for `GRU Fw`, `LSTM global`, and `LSTM Bw` | real Markdown and PDF reviewed |
| Multi-model overlay report | overlay temporal winners against `tree`, paper-derived, and RCIM Model-Bank Reproduction anchors | real Markdown and PDF reviewed |
| Official TE curve-verification report | append Wave 2.1 ledger row and update decision text | styled PDF exported and validated |
| Backlog and master summary | record TE Curve Verification refresh status and accepted or rejected temporal candidates | docs QA passes |

## Execution Order

1. Extend the TE Curve Verification Pipeline candidate configuration so all `9` Wave 2.1 training
   outputs can be loaded by the reference-family comparison tooling.
2. Run the direction-aware matrix refresh and update
   `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`.
3. Run `scripts/reports/analysis/build_track2_best_model_collage_report.py`
   with the refreshed candidate scope.
4. Export and validate the refreshed best-model collage PDF.
5. Run `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
   with the refreshed overlay groups.
6. Export and validate the refreshed multi-model comparison PDF.
7. Update
   `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/track2_official_model_verification_report.md`
   with a `2026-05-24` ledger row and the final temporal-model decision.
8. Export and validate the official TE Curve Verification Pipeline PDF.

## Decision Rule

The refresh can promote a Wave 2.1 temporal model only if both conditions hold:

- scalar TE Curve Verification Pipeline metrics are competitive with the current repository-owned
  `tree` baseline on the matching direction surface;
- visual curve evidence shows useful tracking behavior rather than only a
  local training-metric improvement.

If either condition fails, the Wave 2.1 campaign remains a completed training
experiment and the official TE Curve Verification Pipeline accepted baseline remains unchanged.
