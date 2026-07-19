# RCIM Track1 Polished Actual Values Closeout

## Scope

This closeout covers the completed
`dataset_input_mode_retraining__rcim_track1__polished_actual_values` campaign.
It is the second polished `rcim_track1` input-mode archive required by the
approved retraining plan.

The frozen simplified archive remains untouched:

- `models/simplified_dataset/paper_reference/rcim_track1/`

The completed polished archive is:

- `models/polished_dataset/paper_reference/rcim_track1/actual_values/`

## Execution Summary

The accepted Aries Slurm jobs were:

- `136266` `rcim_av_fw_opt`: `COMPLETED`, exit `0:0`, elapsed `13:04:30`
- `136267` `rcim_av_bw_opt`: `COMPLETED`, exit `0:0`, elapsed `12:58:15`
- `136268` `rcim_av_global_opt`: `COMPLETED`, exit `0:0`, elapsed `23:56:16`

The earlier high-partition global job `136143` timed out during `LGBM` and is
not part of the accepted campaign output.

## Dataset Contract

All accepted surface outputs declare:

- dataset: `polished_dataset`
- input mode: `actual_values`
- input dimension: `5`
- input features: `angular_position_deg`, `input_speed_rpm`,
  `input_torque_nm`, `oil_temperature_deg`, `direction_flag`
- operating-variable source: row-level polished CSV actual values

The promoted archive was created with:

```bash
python -B scripts/campaigns/cross_wave/promote_rcim_track1_input_mode_exports.py \
  --input-mode actual_values \
  --campaign-name dataset_input_mode_retraining__rcim_track1__polished_actual_values \
  --execution-environment "Aries cnode Slurm jobs 136266,136267,136268" \
  --replace
```

The promotion script hard-checks the polished dataset root, input mode,
surface labels, five-feature input contract, and per-family export counts
before writing the archive.

## Artifact Summary

The promoted archive contains:

- `global/`: 10 family archives, 190 ONNX files, 190 Python pickle files
- `forward/`: 10 family archives, 190 ONNX files, 190 Python pickle files
- `backward/`: 10 family archives, 190 ONNX files, 190 Python pickle files

Total promoted files:

- ONNX: `570`
- Python pickle: `570`
- metadata files: `182`

Promotion inventory:

- `models/polished_dataset/paper_reference/rcim_track1/actual_values/promotion_inventory.yaml`

Source validation outputs:

- `output/validation_checks/rcim_track1/2026-07-18-11-55-05__rcim_track1_polished_actual_values_global_rcim_track1_polished_input_mode_campaign_validation/`
- `output/validation_checks/rcim_track1/2026-07-18-11-55-05__rcim_track1_polished_actual_values_fw_rcim_track1_polished_input_mode_campaign_validation/`
- `output/validation_checks/rcim_track1/2026-07-18-11-56-46__rcim_track1_polished_actual_values_bw_rcim_track1_polished_input_mode_campaign_validation/`

Generated validation reports:

- `doc/reports/analysis/validation_checks/2026-07-19-11-50-49_rcim_track1_rcim_track1_polished_33cef108_polished_dataset_rcim_model_bank_reproduction_report.md`
- `doc/reports/analysis/validation_checks/2026-07-19-00-59-09_rcim_track1_rcim_track1_polished_ad870d2f_polished_dataset_rcim_model_bank_reproduction_report.md`
- `doc/reports/analysis/validation_checks/2026-07-19-00-52-37_rcim_track1_rcim_track1_polished_6e0d5998_polished_dataset_rcim_model_bank_reproduction_report.md`

## Verification

Executed checks:

- Slurm accounting for jobs `136266`, `136267`, and `136268` reports
  `COMPLETED` with exit `0:0`.
- Campaign package validator passed:
  `scripts/campaigns/cross_wave/validate_rcim_track1_input_mode_campaign.py`.
- Promoted archive count check passed:
  `570` `.onnx`, `570` `.pkl`, `182` metadata files.
- Per-surface count check passed:
  `global`, `forward`, and `backward` each contain `190` `.onnx`,
  `190` `.pkl`, and `10` family folders.
- Archive text/manifest scan found no `setpoints` or `simplified_dataset`
  mismatches inside the `actual_values` archive.

Residual warning:

- The global Slurm stderr contained a `joblib` worker warning during the long
  grid-search phase, but the job completed, exported all families, and passed
  promotion and validation checks.

## Closeout Decision

The `dataset_input_mode_retraining__rcim_track1__polished_actual_values`
campaign is accepted as closed. The Slurm stdout/stderr files are disposable
post-verification artifacts and must be removed before the closeout commit.
