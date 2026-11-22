# TE Curve Verification Pipeline — Portable ONNX Curve Evaluator

This branch hosts the historically named **Track 2 Portable ONNX Curve Plotter**:
a self-contained **offline inference and curve-diagnostic utility**. It runs
without importing the full PINNs research repository. It is **not** the full
research-main TE Curve Verification Pipeline (CVP 1.1–1.5), a training pipeline,
a deployed TF3820/PLC runtime, or a source of accepted compensation claims.

It supports:

- `simplified_dataset` and `polished_dataset`;
- RCIM Track 1 harmonic ONNX banks, reconstructed into full TE curves;
- direct TE ONNX models that predict transmission error directly;
- `setpoints` input mode and polished `actual_values` input mode.

The Git-tree inventory as of 2026-11-22 contains **1,014 ONNX files**, **2,907
dataset CSV files**, and **42 example output files**. These are preserved
historical assets, not newly reproduced model-test results. The branch is kept
separate from canonical research `main` to preserve its standalone purpose.

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

## Prerequisites and installation

Use **Python 3.10+** (required by the script's type annotation syntax).
The three dependencies in `requirements.txt` are intentionally unpinned; this
branch does not claim to reconstruct the exact historical Python package
environment. Use an isolated virtual environment.

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

`matplotlib` is used when saving plots. Use `--no-save-plots` for a
headless metric/CSV run. The script selects ONNX Runtime's
`CPUExecutionProvider` explicitly, so these commands do not demonstrate
TF3820/PLC timing or accelerator compatibility.

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

Evaluate an explicit, bounded pair of polished curves:

```powershell
python portable_original_onnx_curve_plotter.py `
  --dataset-name polished_dataset `
  --input-mode setpoints `
  --model-kind direct_te `
  --surface backward `
  --model-family tree `
  --curve-csv "data/polished_dataset/backward/25degree/1000rpm/1000.0rpm0.0Nm25.0deg.csv" `
  --curve-csv "data/polished_dataset/backward/25degree/1000rpm/1000.0rpm100.0Nm25.0deg.csv" `
  --max-curves 2 `
  --no-save-plots `
  --output-dir "output/portable_tree_backward_review"
```

### Important `--curve-dir` behavior

In the current **unchanged** Python implementation, `--curve-dir` adds
directory-discovered CSVs to `CURVE_CSV_PATH_LIST` whenever `--curve-csv`
is not provided. Its three hard-coded default curves are **not automatically
disabled**. The resulting list is de-duplicated, sorted, and then truncated by
`--max-curves`. Therefore `--curve-dir` alone is **not** a directory-only
selector and may combine incompatible dataset formats. Use repeated explicit
`--curve-csv` arguments for a strictly controlled run, or review the script's
configuration before using its directory mode. Use a positive integer for
`--max-curves`; its sign is not validated by the CLI. This is a documented
limitation, **not a code fix**.

Outputs are written beneath `--output-dir` (default: `output/`):

```text
output/plots/
output/predicted_curves/
output/portable_track2_onnx_curve_summary.csv
```

The generated summary contains offline per-curve MAE/RMSE in degrees and
percentage errors relative to the measured curve's peak-to-peak range.
Tracked `output/` files are **historical examples**; use a new output
subdirectory for reviews rather than overwriting old evidence.

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

ONNX rank-2 inputs are evaluated pointwise. Rank-3 sequence inputs use rolling
windows with a **33-sample** default and `center` target alignment. Predictions
for sequence models cover only valid window targets; the returned curve may be
shorter than the input CSV. Verify model and preprocessing contracts independently
before treating arbitrary exported ONNX models as interchangeable.

## Dataset Notes

`simplified_dataset` CSV files contain both forward and backward curves in one
file. `polished_dataset` CSV files are direction-specific and infer direction
from the `forward` or `backward` path segment.

The bundled `output/` files are historical examples, not newly validated
receipts. Do not remove or rewrite them during documentation hygiene.

The [portable polished CSV guide](data/polished_dataset/README_POLISHED_CSV.md)
explains dataset columns, nominal versus measured values, and why original
dataset-generation scripts from research `main` are **not available here**.
For the underlying research lineage see the
[canonical dataset family reference](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/blob/main/doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md).

## Verification status and change scope

Documentation updated for HYG-05 based on the checked Git trees and the
`portable_original_onnx_curve_plotter.py` source. No new runtime execution,
numerical parity run, paper-calibrated TE validation, TF3820 benchmark, PLC
Build, TestRig test, or CI qualification has been performed by this edit.
The [technical maintenance record](doc/technical/2026-11/2026-11-22/2026-11-22-15-25-46_portable_onnx_evaluator_documentation_hygiene.md)
defines the allowed change scope. Preserve model, dataset, output and
executable hashes for this documentation-only increment.
