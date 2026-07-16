# RCIM Track1 Polished Input-Mode Retraining

## Overview

This document defines the reduced `RCIM Model-Bank Reproduction` retraining
scope for the postponed `rcim_track1` paper-bank work.

The existing
`models/simplified_dataset/paper_reference/rcim_track1/` archive has been
audited as a valid historical `simplified_dataset` setpoint baseline. It must
remain frozen for now. The `rcim_original` and `rcim_retuned` paper-reference
archives are also out of scope because they are recovered-workflow legacy
archives, not the active `rcim_track1` branch to retrain.

The immediate work is therefore limited to two missing polished-dataset
campaigns:

1. `rcim_track1` with `polished_dataset` and `setpoints`.
2. `rcim_track1` with `polished_dataset` and `actual_values`.

No implementation or training may start from this document alone. Before
execution, a matching campaign planning report must be created under
`doc/reports/campaign_plans/` and explicitly approved.

No subagent is planned. If a subagent becomes useful later, the proposed
subagent name, task boundary, and approval requirement must be recorded before
requesting approval.

## Technical Approach

Reuse the existing `rcim_track1` simplified archive only as the frozen baseline
for future comparison. Do not retrain or overwrite it during this phase.

Prepare two new polished `rcim_track1` family-version campaigns:

- `dataset_input_mode_retraining__rcim_track1__polished_setpoints`;
- `dataset_input_mode_retraining__rcim_track1__polished_actual_values`.

Each campaign must contain the three canonical surfaces:

- `global`;
- `forward`;
- `backward`.

Both polished variants must expose the same five-feature inference contract so
future `TE Curve Verification Pipeline` and deployment tests can evaluate them
with one script:

- `angular_position_deg`;
- `input_speed_rpm`;
- `input_torque_nm`;
- `oil_temperature_deg`;
- `direction_flag`.

The distinction between the two polished campaigns is only how the three
operating variables are sourced:

- `polished_setpoints`: speed, torque, and temperature are parsed from the
  curve path or filename and remain constant within a curve.
- `polished_actual_values`: speed, torque, and temperature are read from the
  polished CSV row-level measured columns and may vary row by row.

The campaign package must hard-fail if any artifact metadata disagrees across:

- `dataset_id`;
- `input_mode`;
- `dataset_schema`;
- `source_dataset_root`;
- `surface`;
- exported model destination.

## Involved Components

- `models/simplified_dataset/paper_reference/rcim_track1/`
- `models/polished_dataset/paper_reference/rcim_track1/setpoints/`
- `models/polished_dataset/paper_reference/rcim_track1/actual_values/`
- `data/polished_dataset/`
- `config/datasets/transmission_error_dataset.yaml`
- `config/training/dataset_input_mode_retraining/`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`
- `scripts/campaigns/aries/`
- `doc/scripts/campaigns/aries/`
- `doc/reports/campaign_plans/`
- `output/training_campaigns/`
- `output/training_runs/`
- `output/registries/`

The current `models/simplified_dataset/paper_reference/rcim_track1/` archive is
an input baseline only. The previous unsplit
`models/polished_dataset/paper_reference/rcim_track1/` archive is intentionally
removed before retraining. The new polished outputs must recreate that family
root with input-mode-specific subfolders and must not modify the simplified
archive.

## Implementation Steps

1. Create the campaign planning report for the two polished `rcim_track1`
   campaigns and request explicit approval before any training run.
2. Inspect the current `rcim_track1` campaign generation and export code paths
   to identify where the dataset and input-mode selectors must be threaded.
3. Prepare one campaign package for
   `dataset_input_mode_retraining__rcim_track1__polished_setpoints` with
   `global`, `forward`, and `backward` surfaces.
4. Prepare one campaign package for
   `dataset_input_mode_retraining__rcim_track1__polished_actual_values` with
   `global`, `forward`, and `backward` surfaces.
5. Add or reuse validators that prove the run metadata, model archive metadata,
   ONNX exports, Python exports, and destination folder all agree on
   `dataset_id=polished_dataset` and the intended `input_mode`.
6. Run the first polished setpoint campaign on the local Windows workstation,
   in parallel across the `global`, `forward`, and `backward` surfaces, so the
   Aries cluster can continue the separate cross-wave retraining queue.
7. Promote completed surface exports into
   `models/polished_dataset/paper_reference/rcim_track1/setpoints/` only after
   validating the dataset root, input mode, surface labels, five-feature input
   contract, and per-family ONNX/Python export counts.
8. Decide the execution host for the polished actual-values campaign after the
   current Aries work completes or remains active: use Aries if it is free,
   otherwise use the same local Windows parallel policy.
9. After each terminal campaign, inspect the launcher logs and output
   artifacts, close out the campaign, and commit.
10. Defer any decision to retrain
   `dataset_input_mode_retraining__rcim_track1__simplified_setpoints` until the
   two polished campaigns have completed and the value of a normalized
   simplified rerun can be judged against the audited historical baseline.
