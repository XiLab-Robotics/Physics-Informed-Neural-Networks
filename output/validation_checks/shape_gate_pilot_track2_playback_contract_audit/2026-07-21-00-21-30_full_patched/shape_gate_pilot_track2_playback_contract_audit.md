# Shape-Gate Pilot Track 2 Playback Contract Audit

## Overview

This diagnostic compares the existing Track 2 full-curve sequence
playback against a training-like sequence-window playback for the
`shape_gate_loss_pilot_periodic_gru_sequence_Fw` checkpoint.

## Scope

- config: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix.yaml`;
- output directory: `output\validation_checks\shape_gate_pilot_track2_playback_contract_audit\2026-07-21-00-21-30_full_patched`;
- per-curve CSV: `output\validation_checks\shape_gate_pilot_track2_playback_contract_audit\2026-07-21-00-21-30_full_patched\shape_gate_pilot_track2_playback_contract_audit.csv`;
- curve count: `100`;
- datamodule test curve count: `194`;
- datamodule test sample count: `12416`;

## Mean Metrics

| Playback | MAE [deg] | Offset Error [deg] | Centered MAE [deg] |
| --- | ---: | ---: | ---: |
| Saved-config datamodule test-loader | 0.002522 | N/A | N/A |
| Track 2 full curve | 0.002398 | 0.001592 | 0.001603 |
| Track 2 sampled at training targets | 0.002369 | 0.001586 | 0.001563 |
| Training-like valid windows | 0.002369 | 0.001586 | 0.001563 |

## Interpretation

- If the training-like row remains close to the full-curve row, the
  checkpoint itself has an offset-dominated failure.
- If the training-like row drops close to the training/test-loader MAE,
  the Track 2 full-curve reconstruction path is not comparable to the
  training evaluation contract and must be fixed or separately labeled.
