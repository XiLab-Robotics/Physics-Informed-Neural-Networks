# Track 2 Portable ONNX Curve Plotter

This branch is a portable inference package for Track 2 transmission-error
models. It runs without importing the full research repository.

It supports:

- `simplified_dataset` and `polished_dataset`;
- RCIM Track 1 harmonic ONNX banks, reconstructed into full TE curves;
- direct TE ONNX models that predict transmission error directly;
- `setpoints` input mode and polished `actual_values` input mode.

## Layout

```text
.
|-- data/
|   |-- simplified_dataset/
|   `-- polished_dataset/
|-- models/
|   |-- simplified_dataset/
|   `-- polished_dataset/
|-- output/
|-- portable_original_onnx_curve_plotter.py
|-- requirements.txt
`-- README.md
```

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

`matplotlib` is only needed when saving plots. Use `--no-save-plots` for a
headless metric/CSV run.

## Run Examples

RCIM harmonic reconstruction on the simplified dataset:

```powershell
python portable_original_onnx_curve_plotter.py `
  --dataset-name simplified_dataset `
  --input-mode setpoints `
  --model-kind rcim `
  --surface forward `
  --model-family SVR
```

Direct TE model on polished actual values:

```powershell
python portable_original_onnx_curve_plotter.py `
  --dataset-name polished_dataset `
  --input-mode actual_values `
  --model-kind direct_te `
  --surface forward `
  --model-family periodic_gru_sequence `
  --curve-csv "data/polished_dataset/forward/25degree/1000rpm/1000.0rpm0.0Nm25.0deg.csv"
```

Process a directory:

```powershell
python portable_original_onnx_curve_plotter.py `
  --dataset-name polished_dataset `
  --input-mode setpoints `
  --model-kind direct_te `
  --surface backward `
  --model-family tree `
  --curve-dir "data/polished_dataset/backward/25degree" `
  --max-curves 5
```

Outputs are written under:

```text
output/plots/
output/predicted_curves/
output/portable_track2_onnx_curve_summary.csv
```

## Model Contracts

RCIM models use tabular operating-point input:

```text
[speed_rpm, oil_temperature_deg, torque_nm]
```

The script discovers harmonic files from:

```text
models/<dataset>/rcim_track1/<surface>/<family>/
```

Direct TE models use five-feature input:

```text
setpoints:
  [angular_position_deg, input_speed_rpm, input_torque_nm, oil_temperature_deg, direction_flag]

polished actual_values:
  [theta, theta_dot, tau_load, T, direction_flag]
```

Direct models are loaded from:

```text
models/<dataset>/<input_mode>/<family>/<surface>.onnx
```

Sequence models are evaluated with rolling windows. The default sequence length
is `33`, matching the current exported Track 2 sequence-model default.

## Dataset Notes

`simplified_dataset` CSV files contain both forward and backward curves in one
file. `polished_dataset` CSV files are direction-specific and infer direction
from the `forward` or `backward` path segment.

Generated `output/` files can be deleted and regenerated.
