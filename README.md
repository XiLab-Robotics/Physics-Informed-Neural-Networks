# Track 2 Portable ONNX Curve Plotter

This branch is a small, portable package for running the recovered original
RCIM paper forward ONNX models on measured transmission-error curves.

It is intentionally separate from the full research repository. The goal is to
load the original paper ONNX models, reconstruct the predicted transmission
error curve from harmonic amplitude and phase predictions, and plot measured
TE versus predicted TE without depending on any repository-internal Python
modules.

## What Is Included

```text
.
├── data/
│   └── datasets/
│       └── Test_<temperature>degree/<speed>rpm/*.csv
├── models/
│   └── exact_onnx_paper_release/
├── output/
│   ├── plots/
│   ├── predicted_curves/
│   └── portable_original_onnx_curve_summary.csv
├── portable_original_onnx_curve_plotter.py
├── requirements.txt
└── README.md
```

The main entry point is:

```text
portable_original_onnx_curve_plotter.py
```

The script uses the ONNX models stored under:

```text
models/exact_onnx_paper_release/
```

The bundled dataset follows the original test-rig CSV layout, for example:

```text
data/datasets/Test_25degree/100rpm/100.0rpm100.0Nm25.0deg.csv
```

## What The Script Does

For each configured curve CSV, the script:

1. loads the measured transmission-error curve;
2. extracts the operating point from the CSV filename or from CSV columns;
3. builds the ONNX input feature row:

   ```text
   [speed_rpm, oil_temperature_deg, torque_nm]
   ```

4. runs the selected harmonic amplitude and phase ONNX models;
5. reconstructs the predicted TE curve from the harmonic components;
6. plots measured TE and predicted TE on the same graph;
7. writes output plots, optional predicted-curve CSV files, and a summary CSV.

The default configuration processes four representative curves and writes
results under:

```text
output/
```

## Install

Create and activate a Python environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt matplotlib
```

The extra `matplotlib` install is required for plot generation. If
`requirements.txt` is later updated to include `matplotlib`, the last command
can become:

```powershell
python -m pip install -r requirements.txt
```

## Run The Default Example

From the repository root:

```powershell
python portable_original_onnx_curve_plotter.py
```

Expected outputs:

```text
output/plots/*.png
output/predicted_curves/*_predicted.csv
output/portable_original_onnx_curve_summary.csv
```

The summary CSV contains one row per processed curve with the operating point,
point count, plot path, prediction CSV path, and error metrics:

```text
mae_deg
rmse_deg
mean_error_pct
p95_error_pct
```

## Configure The Curves To Process

Edit the `USER CONFIGURATION` block at the top of
`portable_original_onnx_curve_plotter.py`.

To process explicit CSV files:

```python
CURVE_CSV_PATH_LIST = [
    "data/datasets/Test_25degree/100rpm/100.0rpm100.0Nm25.0deg.csv",
    "data/datasets/Test_35degree/800rpm/800.0rpm1800.0Nm35.0deg.csv",
]
```

To process every CSV in a folder:

```python
CURVE_CSV_PATH_LIST = []
CURVE_CSV_DIRECTORY_PATH = "data/datasets/Test_25degree"
CURVE_CSV_GLOB_PATTERN = "*.csv"
PROCESS_CURVE_DIRECTORY_RECURSIVELY = True
```

To write outputs somewhere else:

```python
OUTPUT_DIRECTORY_PATH = "output/my_run"
```

## Select Harmonics

By default, the script uses every harmonic represented by the configured paper
best forward ONNX model list:

```python
SELECTED_HARMONIC_ORDER_LIST = None
```

To use only the simplified sparse subset discussed in the RCIM paper notes:

```python
SELECTED_HARMONIC_ORDER_LIST = [0, 1, 39, 40]
```

For a non-zero harmonic, both an amplitude model and a phase model must be
available. Harmonic `0` only needs an amplitude model because it is the
constant curve offset term.

## Use A New Custom CSV

A custom curve CSV must provide:

- angular position in degrees;
- measured transmission error in degrees;
- operating point metadata: speed, torque, and oil temperature.

The script accepts the original dataset column names:

```text
Poisition_Output_Reducer_Fw
Transmission_Error_Fw
```

It also accepts simpler aliases such as:

```text
angular_position_deg
transmission_error_deg
speed_rpm
torque_nm
oil_temperature_deg
```

If the CSV does not contain speed, torque, and temperature columns, the script
tries to parse them from the filename pattern:

```text
<speed>rpm<torque>Nm<temperature>deg.csv
```

Example:

```text
800.0rpm1800.0Nm35.0deg.csv
```

If neither the CSV columns nor the filename provide the operating point, set
these values manually in the configuration block:

```python
DEFAULT_SPEED_RPM = 800.0
DEFAULT_TORQUE_NM = 1800.0
DEFAULT_OIL_TEMPERATURE_DEG = 35.0
```

## Use Different ONNX Models

The ONNX paths are hardcoded in:

```python
ONNX_TARGET_CONFIGURATION_LIST = [
    ("amplitude", 0, "SVR", "models/exact_onnx_paper_release/SVR/ampl/SVR_ampl0.onnx"),
    ...
]
```

Each entry has this structure:

```text
(target_kind, harmonic_order, model_family_label, model_path)
```

Use:

- `target_kind = "amplitude"` for amplitude models;
- `target_kind = "phase"` for phase models;
- `harmonic_order = 0, 1, 3, 39, 40, ...`;
- `model_path` as either a path relative to the repository root or an absolute
  path.

## Reconstruction Formula

For harmonic `0`, the predicted amplitude is used as the constant term:

```text
TE_0(theta) = amplitude_0
```

For every non-zero harmonic:

```text
cosine_coefficient_h = amplitude_h * cos(phase_h)
sine_coefficient_h = -amplitude_h * sin(phase_h)
```

The reconstructed curve is:

```text
TE(theta) = amplitude_0
          + sum_h(
              cosine_coefficient_h * cos(h * theta)
              + sine_coefficient_h * sin(h * theta)
            )
```

`theta` is the angular position converted from degrees to radians.

## Notes

- This branch is for offline ONNX curve plotting and inspection.
- It does not train models.
- It does not import the full Track 2 repository pipeline.
- It does not require the original repository package layout.
- Generated files under `output/` can be deleted and regenerated at any time.
