# Polished RCIM Track 1 Paper Reference

This folder contains the polished-dataset RCIM Model-Bank Reproduction exports
using the same `rcim_track1` naming convention as the simplified archive. The
artifacts are split by direction so forward and backward ONNX banks remain
physically separate.

## Direction Roots

- `forward/`
  Source:
  `output/validation_checks/rcim_model_bank_reproduction/2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation/`
- `backward/`
  Source:
  `output/validation_checks/rcim_model_bank_reproduction/2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation/`

Each direction folder contains:

- `onnx/` with 190 exported ONNX files;
- `python/` with 190 exported Python pickle files;
- `training_config.yaml`;
- `validation_summary.yaml`;
- `best_parameter_summary.yaml`.
