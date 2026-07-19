# GBM RCIM Track 1 Polished actual_values Archive

This archive contains the promoted ONNX and Python fitted-estimator
exports from the completed RCIM Track 1 input-mode campaign.
Execution environment: Aries cnode Slurm jobs 136266,136267,136268.

Archive contract:

- dataset: `polished_dataset`
- input mode: `actual_values`
- direction: `global`
- input features: `angular_position_deg`, `input_speed_rpm`,
  `input_torque_nm`, `oil_temperature_deg`, `direction_flag`
- ONNX exports: `onnx/amplitude/` and `onnx/phase/`
- Python exports: `python/amplitude/` and `python/phase/`
- machine-readable provenance: `reference_inventory.yaml`
