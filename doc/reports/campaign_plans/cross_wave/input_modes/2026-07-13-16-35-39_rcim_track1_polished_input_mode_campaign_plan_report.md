# RCIM Track1 Polished Input-Mode Campaign Plan

## Campaign Status

Planning only. No campaign YAML, launcher, Slurm execution, smoke run, or
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
- `dataset_schema: polished_point_v1`;
- `source_dataset_root: data/polished_dataset`.

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

## Aries Execution Plan

Execution must happen on the Aries cluster, not in this Windows checkout.

The first execution for this RCIM input-mode pair must be a fast GPU `srun`
smoke check after the package exists and before any full `sbatch` submission.
The smoke should exercise one small representative surface or reduced workload
only and must be removed or quarantined after verification.

After the smoke succeeds, run one full campaign at a time:

1. submit `dataset_input_mode_retraining__rcim_track1__polished_setpoints`;
2. wait for terminal Slurm state;
3. inspect outputs and Slurm logs;
4. clean Slurm stdout and stderr files per operator policy;
5. close out artifacts and commit;
6. submit `dataset_input_mode_retraining__rcim_track1__polished_actual_values`;
7. repeat the same terminal-state, cleanup, closeout, and commit sequence.

The surface runs inside each campaign should be sequential unless the operator
explicitly approves parallel surface execution later.

## Safety Checks

The campaign package and closeout must verify:

- every run declares `dataset_id: polished_dataset`;
- every run declares the intended `input_mode`;
- every run declares `dataset_schema: polished_point_v1`;
- every run records `source_dataset_root: data/polished_dataset`;
- every exported artifact path is under the intended input-mode root;
- no output path targets the frozen simplified archive;
- no output path targets the unsplit polished paper-reference archive;
- `global`, `forward`, and `backward` surfaces are all present;
- ONNX and Python artifacts agree with the source run metadata;
- the run metadata contains the final five-feature input list.

## Approval Gate

This campaign plan requires explicit approval before implementation proceeds.
After approval, the next work item is campaign package preparation: campaign
YAML files, Aries launcher or launcher update, launcher note, active campaign
state, and validation commands.
