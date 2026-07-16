# RCIM Track 1 Polished setpoints Archive

This folder contains the official promoted RCIM Track 1 polished-dataset
setpoints model bank. The source run was executed locally on Windows
while Aries continued the independent model-development campaign stream.

Input contract:

- dataset: `polished_dataset`
- input mode: `setpoints`
- input dimension: `5`
- input features: `angular_position_deg`, `input_speed_rpm`,
  `input_torque_nm`, `oil_temperature_deg`, `direction_flag`

Promoted surfaces:

- `global/`: 10 family archives, 190 ONNX files, 190 Python pickle files
- `forward/`: 10 family archives, 190 ONNX files, 190 Python pickle files
- `backward/`: 10 family archives, 190 ONNX files, 190 Python pickle files

Each family archive contains:

- `onnx/amplitude/` and `onnx/phase/`
- `python/amplitude/` and `python/phase/`
- `reference_inventory.yaml`
- `source_runs/<validation_run>/` snapshots
