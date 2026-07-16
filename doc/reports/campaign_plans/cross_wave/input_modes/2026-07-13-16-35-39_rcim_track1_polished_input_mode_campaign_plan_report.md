# RCIM Track1 Polished Input-Mode Campaign Plan

## Campaign Status

Planning only. No campaign YAML, launcher, training execution, smoke run, or
training has started from this plan.

The approved technical document is:

- `doc/technical/2026-07/2026-07-13/2026-07-13-16-31-32_rcim_track1_polished_input_mode_retraining.md`

## Objective

Prepare the two missing `rcim_track1` polished-dataset retraining campaigns
while preserving the audited historical `simplified_dataset` baseline and the
legacy recovered-workflow archives.

The campaigns are:

1. `dataset_input_mode_retraining__rcim_track1__polished_setpoints`
2. `dataset_input_mode_retraining__rcim_track1__polished_actual_values`

Each campaign must train and export exactly three surfaces:

- `global`;
- `forward`;
- `backward`.

Total planned campaign count: `2`.

Total planned surface run count: `6`.

## Scope Boundaries

The following archives are explicitly out of scope:

- `models/simplified_dataset/paper_reference/rcim_track1/`
- `models/simplified_dataset/paper_reference/rcim_original/`
- `models/simplified_dataset/paper_reference/rcim_retuned/`

The existing simplified `rcim_track1` archive remains the frozen historical
baseline for now. It must not be overwritten or regenerated during this phase.

The existing `rcim_original` and `rcim_retuned` archives remain legacy
recovered-workflow references and must not be used as retraining targets for
this campaign pair.

The previous unsplit `models/polished_dataset/paper_reference/rcim_track1/`
archive is intentionally removed before this retraining package is prepared.
The input-mode split campaigns must recreate that family root with explicit
input-mode subfolders so future validation cannot confuse the new setpoint and
actual-value variants.

## Dataset And Input Contracts

Both campaigns use:

- `dataset_id: polished_dataset`;
- `source_dataset_root: data/polished_dataset`.

Dataset schema remains input-mode specific:

- `setpoints`: `polished_setpoint_curve_v1`;
- `actual_values`: `polished_point_v1`.

Both campaigns must expose the same five-feature model input contract:

- `angular_position_deg`;
- `input_speed_rpm`;
- `input_torque_nm`;
- `oil_temperature_deg`;
- `direction_flag`.

The input-mode distinction is:

- `polished_setpoints`: speed, torque, and temperature come from the nominal
  curve setpoints parsed from the polished CSV path or filename and remain
  constant within each curve.
- `polished_actual_values`: speed, torque, and temperature come from row-level
  measured polished CSV columns and may vary within each curve.

The campaign preparation must fail if `polished_setpoints` reads row-level
`theta_dot`, `tau_load`, or `T` for the three operating variables, or if
`polished_actual_values` substitutes filename setpoints for those same
variables.

## Planned Campaign Matrix

### Polished Setpoints

- campaign ID:
  `dataset_input_mode_retraining__rcim_track1__polished_setpoints`
- dataset:
  `polished_dataset`
- input mode:
  `setpoints`
- surfaces:
  `global`, `forward`, `backward`
- expected run count:
  `3`
- intended model archive root:
  `models/polished_dataset/paper_reference/rcim_track1/setpoints/`

### Polished Actual Values

- campaign ID:
  `dataset_input_mode_retraining__rcim_track1__polished_actual_values`
- dataset:
  `polished_dataset`
- input mode:
  `actual_values`
- surfaces:
  `global`, `forward`, `backward`
- expected run count:
  `3`
- intended model archive root:
  `models/polished_dataset/paper_reference/rcim_track1/actual_values/`

## Artifact Placement Contract

Each completed campaign must produce normal campaign state under:

- `output/training_campaigns/`
- `output/training_runs/`
- `output/registries/`

Each accepted surface must export both deployment-facing and Python-facing
artifacts:

- ONNX model artifacts;
- Python model artifacts;
- `reference_inventory.yaml`;
- source-run metadata snapshots;
- dataset and input-mode audit metadata.

The exported model root must match the campaign input mode exactly:

- `models/polished_dataset/paper_reference/rcim_track1/setpoints/`
- `models/polished_dataset/paper_reference/rcim_track1/actual_values/`

No campaign output may be written under:

- `models/simplified_dataset/paper_reference/rcim_track1/`
- any unsplit direct `models/polished_dataset/paper_reference/rcim_track1/forward/`
  or `models/polished_dataset/paper_reference/rcim_track1/backward/` archive
  layout.

## Execution Plan

The first campaign,
`dataset_input_mode_retraining__rcim_track1__polished_setpoints`, runs on the
local Windows workstation in parallel across the `global`, `forward`, and
`backward` surfaces. The Aries cluster remains reserved for the already active
cross-wave retraining sequence.

The second campaign,
`dataset_input_mode_retraining__rcim_track1__polished_actual_values`, remains
location-flexible. If Aries has finished the other retraining work by then, it
can be submitted there; otherwise it should run locally with the same parallel
surface policy.

For the local Windows run:

1. run the launcher preflight;
2. launch `global`, `forward`, and `backward` in parallel;
3. inspect each surface exit code and launcher log;
4. rerun the campaign package validator;
5. promote the exported ONNX and Python artifacts into the official
   input-mode archive with the repository-owned promotion script;
6. verify final model counts and file-size risk;
7. close out artifacts and commit before preparing or launching the next RCIM
   input-mode campaign.

## Safety Checks

The campaign package and closeout must verify:

- every run declares `dataset_id: polished_dataset`;
- every run declares the intended `input_mode`;
- every run declares the expected input-mode-specific `dataset_schema`;
- every run records `source_dataset_root: data/polished_dataset`;
- every exported artifact path is under the intended input-mode root;
- no output path targets the frozen simplified archive;
- no output path targets the unsplit polished paper-reference archive;
- `global`, `forward`, and `backward` surfaces are all present;
- each promoted surface contains exactly `190` ONNX files and `190` Python
  pickle files;
- the promoted input-mode archive contains exactly `570` ONNX files and `570`
  Python pickle files;
- ONNX and Python artifacts agree with the source run metadata;
- the run metadata contains the final five-feature input list.

## Approval Gate

This campaign plan requires explicit approval before implementation proceeds.
After approval, the next work item is campaign package preparation: campaign
YAML files, Windows local launcher update, launcher note, active campaign
state, and validation commands.
