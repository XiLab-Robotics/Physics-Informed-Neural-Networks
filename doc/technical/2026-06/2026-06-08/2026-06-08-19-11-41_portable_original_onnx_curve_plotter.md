# Portable Original ONNX Curve Plotter

## Overview

This document plans the conversion of the existing original-paper `ONNX`
forward curve plotter into a fully portable script that can run outside this
repository. The current script is located at
`scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/plot_original_onnx_fw_track2_curves.py`.
It already stores the recovered original paper `ONNX` target paths in a
hardcoded configuration block, but it is not repository-independent because it
imports project helpers, resolves `PROJECT_PATH`, and reads the repository
`TE Curve Verification Pipeline` matrix instead of user-provided curve `CSV` files.

The requested target is a standalone Python script that can be copied beside a
new curve dataset, edited at the top through hardcoded path lists, and executed
without importing any repository module. The script must load selected
harmonic-wise `ONNX` models, predict their amplitude and phase targets for each
input curve, reconstruct the transmission-error curve, and plot predicted
versus measured TE on the same chart.

## Technical Approach

The implementation will add a new portable script instead of weakening the
repository-integrated TE Curve Verification Pipeline helper. The existing
`plot_original_onnx_fw_track2_curves.py` remains useful for official TE Curve Verification Pipeline
matrix plots, while the new script will be designed as an exportable utility
with only external scientific Python dependencies.

The new script will contain an explicit top-of-file configuration section:

- `ONNX_TARGET_CONFIGURATION_LIST` with one entry per amplitude or phase target.
  Each entry records target kind, harmonic order, model family label, and an
  absolute or relative `ONNX` model path.
- `SELECTED_HARMONIC_ORDER_LIST` to select all available paper-best harmonics or
  only sparse subsets such as `0`, `1`, `39`, and `40`.
- `CURVE_CSV_PATH_LIST` for one or more explicit input curve files.
- `CURVE_CSV_DIRECTORY_PATH` plus a glob pattern for batch processing every
  curve file in a folder.
- `OUTPUT_DIRECTORY_PATH`, `SHOW_PLOTS`, and `SAVE_PLOTS` flags for exported
  figures and interactive inspection.

The script will use only `numpy`, `pandas`, `matplotlib`, and `onnxruntime`.
It will not import from `scripts/`, `config/`, `doc/`, or any other repository
module. Before implementation, `context7` should be attempted for current
library/API checks; if unavailable, the implementation will rely on local code
inspection and the stable public APIs already used by the repository.

Input `CSV` support will be intentionally practical:

- discover angular-position, measured-TE, speed, torque, and oil-temperature
  columns through configurable column-name candidate lists;
- allow fixed default speed, torque, and oil-temperature values in the hardcoded
  configuration if a custom curve file does not contain metadata columns;
- process either explicit files, every file in one folder, or both in the same
  run;
- fail with a direct error message if the selected harmonics do not have the
  required amplitude target, or if a non-zero harmonic lacks its phase target.

The reconstruction will be implemented locally, not by calling
`harmonic_wise_support`. For each curve, the script will:

1. read the operating point from the curve `CSV` or fixed configuration;
2. build the `ONNX` feature row in the same order used by the current TE Curve Verification Pipeline
   path, namely speed in rpm, oil temperature in degrees, and torque in Nm;
3. run every selected target model with `onnxruntime`;
4. convert amplitude and phase predictions into harmonic cosine and sine terms;
5. evaluate the reconstructed TE curve over the angular samples in the input
   `CSV`;
6. overlay measured TE and predicted TE in a Matplotlib figure;
7. save per-curve plots, optional prediction `CSV` outputs, and a summary table.

For non-zero harmonics the local reconstruction will use the same convention as
the paper-aligned TE Curve Verification Pipeline path:

```text
cosine_coefficient_h = amplitude_h * cos(phase_h)
sine_coefficient_h = -amplitude_h * sin(phase_h)
TE(theta) = amplitude_0 + sum_h(
    cosine_coefficient_h * cos(h * theta)
    + sine_coefficient_h * sin(h * theta)
)
```

where `theta` is converted from degrees to radians before evaluating the
trigonometric terms.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/plot_original_onnx_fw_track2_curves.py`:
  existing repository-integrated script to use as the source for recovered
  original `ONNX` target lists and plotting behavior.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/portable_original_onnx_curve_plotter.py`:
  proposed new standalone script with no repository imports.
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`:
  source location of the recovered original paper `ONNX` models while running
  inside this repository. Outside the repository, the user can replace these
  strings with absolute paths to copied model files.
- Custom curve `CSV` files:
  user-provided input curves that follow the test-dataset style or provide
  equivalent angular-position and measured-TE columns.
- `doc/README.md`:
  canonical documentation index entry for this technical document.

No subagent is planned for this work.

## Implementation Steps

1. Inspect the current plotter and representative curve `CSV` headers to define
   portable column aliases without relying on project dataset loaders.
2. Add the standalone script with all path and selection settings grouped in a
   clearly marked configuration block.
3. Copy the 19 recovered original paper-best forward `ONNX` target entries into
   the portable configuration and keep sparse examples for harmonics `0`, `1`,
   `39`, and `40`.
4. Implement local `ONNX` loading, feature-row construction, selected-harmonic
   validation, amplitude/phase prediction, harmonic reconstruction, metrics,
   plot export, and optional interactive display.
5. Validate the script from the repository against one known curve file and the
   original `ONNX` models, then confirm it does not import repository modules.
6. Add usage documentation and exact launch commands for both in-repository and
   copied-outside-repository execution.
7. Run scoped Markdown QA for touched authored Markdown files and script-level
   smoke checks for the portable utility.
