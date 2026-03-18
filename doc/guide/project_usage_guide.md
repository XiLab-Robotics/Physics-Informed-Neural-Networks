# Project Usage Guide

## Overview

This guide explains how to use the runnable workflows currently available in the repository.

At the moment, the implemented workflows are:

- dataset processing through the validated TE dataset utilities;
- dataset visualization through the TE plotting script;
- feedforward neural-network training, validation, held-out testing, and per-run reporting through a PyTorch Lightning baseline;
- structured static neural baselines through harmonic, periodic-feature, and residual-harmonic training configurations;
- tree-based structured baselines through `RandomForestRegressor` and `HistGradientBoostingRegressor`;
- one-batch training-setup validation for the shared Wave 0 training infrastructure;
- minimal neural or tree smoke-test execution for the shared training infrastructure;
- persistent batch training campaigns through a queue-based runner.
- styled PDF regeneration for the training-configuration analysis report through a dedicated report-export utility;
- real exported PDF validation through a dedicated page-rasterization utility.

Recurrent models, LSTM-based models, inference/export flows, and PINN-specific training are still planned future extensions. They are not yet exposed as runnable project workflows.

## Prerequisites

Before using the scripts, make sure the project environment is installed and activated.

If the environment is not ready yet, install the tracked project dependencies first:

```powershell
conda create -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --upgrade pip
python -m pip install torch --index-url https://download.pytorch.org/whl/cu130
python -m pip install -r requirements.txt
```

This keeps the dependency installation aligned with `requirements.txt` while still pulling the CUDA-enabled `torch` build from the official PyTorch wheel index for the current Windows setup.

If you are upgrading an existing `standard_ml_codex_env` from Python 3.10, rebuild the binary packages after the interpreter update:

```powershell
conda install -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --force-reinstall --no-cache-dir -r requirements.txt
python -m pip install --force-reinstall --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

### 1. Activate The Conda Environment

```powershell
conda activate standard_ml_codex_env
```

### 2. Verify The Main Dependencies

```powershell
python -c "import torch, lightning, pandas, matplotlib, colorama, fitz; print(torch.__version__); print(lightning.__version__); print(fitz.__doc__.split()[0])"
```

### 3. Check The Dataset Path

The current dataset path is configured in:

- `config/datasets/transmission_error_dataset.yaml`

The default repository setting is:

```yaml
paths:
  dataset_root: data/datasets
```

This path is interpreted relative to the repository root.

If the dataset is moved in the future, update this YAML file before running the scripts.

## Relevant Project Paths

The current usage flow mainly relies on these folders:

- `scripts/datasets/`
  Dataset processing and visualization utilities.

- `scripts/reports/`
  Styled report-export utilities.

- `scripts/training/`
  Static neural and tree training entry points, shared datamodule/regression infrastructure, campaign runner, and validation/smoke-test utilities.

- `scripts/models/`
  Neural-network backbones and the model factory.

- `models/`
  Reserved root folder for trained checkpoints and exported model artifacts.

- `config/`
  YAML files grouped by dataset, visualization, and training workflows.

- `config/training/feedforward/presets/`
  Reusable feedforward training presets with explicit `model_family` identity for the shared training infrastructure.

- `config/training/wave1_structured_baselines/campaigns/`
  Wave 1 structured-baseline campaign YAML packages across harmonic, periodic-feature, residual, and tree families.

- `config/training/queue/`
  Persistent batch-training queue folders.

- `data/datasets/`
  Validated Transmission Error CSV dataset.

- `output/`
  Generated artifacts such as plots, logs, and model checkpoints.

- `output/training_runs/`
  Immutable per-run training artifacts grouped by model family.

- `output/validation_checks/`
  One-batch validation artifacts grouped by model family.

- `output/smoke_tests/`
  Minimal Lightning smoke-test artifacts grouped by model family.

- `output/training_campaigns/`
  Campaign-level manifests, markdown execution reports, and batch logs.

- `output/registries/`
  Family-level and program-level best-result registries.

- `doc/running/`
  Persistent state for the currently prepared or active training campaign.

- `doc/`
  Technical, script-level, and user-facing documentation.

- `doc/reports/analysis/`
  Analytical reports and their polished PDF artifacts.

## Styled Report PDF Export And Validation

## What The Styled PDF Export Does

The styled PDF export entry point is:

- `scripts/reports/generate_styled_report_pdf.py`

This utility:

- reads a canonical Markdown report;
- converts the supported Markdown structure into styled HTML;
- applies a print-oriented visual layout with stronger hierarchy and table rendering;
- preserves repository-local embedded report images such as conceptual model diagrams;
- exports the final PDF through headless Chrome or Edge.

The permanent validation entry point is:

- `scripts/reports/validate_report_pdf.py`

The repository also now exposes a diagram-generation utility used by the model explanatory reports:

- `scripts/reports/generate_model_report_diagrams.py`

The standardized orchestration entry point is:

- `scripts/reports/run_report_pipeline.py`

This utility:

- opens the real exported PDF artifact;
- rasterizes each PDF page to PNG through `PyMuPDF`;
- gives a deterministic validation output that can be inspected visually without rebuilding ad hoc tooling.

The diagram-generation utility:

- regenerates the repository-owned SVG figures used in the model explanatory reports;
- produces both conceptual diagrams and architecture-style diagrams;
- keeps the visual language and layout of those diagrams consistent across model families;
- enforces built-in fit checks so card content does not silently overflow;
- uses true directional connectors for architecture diagrams instead of pseudo-arrow text.

The report-pipeline runner:

- orchestrates diagram regeneration, PDF export, and PDF validation in one command;
- standardizes temporary artifacts under `.temp/report_pipeline/`;
- can use a repository-local validation environment under `.tools/report_pdf_env/`.

The current main target is:

- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`

Treat that PDF as the project golden standard for future styled analytical reports.

The same export direction now also applies to final campaign-results reports.

## Regenerate The Styled Training-Configuration PDF

```powershell
python scripts/reports/generate_styled_report_pdf.py `
  --input-markdown-path doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md `
  --output-pdf-path doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf `
  --report-subtitle "Feedforward Transmission Error Baseline" `
  --report-category "Analysis Report"
```

What this does:

- preserves the Markdown file as the canonical content source;
- uses a temporary styled HTML preview internally for the browser export;
- overwrites the PDF with the improved visual layout.

If a persistent HTML preview is explicitly needed, request it on purpose:

```powershell
python scripts/reports/generate_styled_report_pdf.py `
  --input-markdown-path doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md `
  --output-html-path doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report_preview.html `
  --output-pdf-path doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf `
  --report-subtitle "Feedforward Transmission Error Baseline" `
  --report-category "Analysis Report" `
  --keep-html
```

Notes:

- the script auto-detects local Chrome or Edge installations on Windows;
- repository-local Markdown image assets are now supported for styled reports, so explanatory model diagrams can appear in both Markdown and PDF form;
- future styled analytical PDFs should preserve the same design direction:
  - white page background with restrained blue accents;
  - rounded section cards and professional typography;
  - safe A4 margins with no clipped borders or overflowing content;
  - split comparison tables when necessary for readability;
  - repeated `Config` anchors across split comparison tables;
  - centered alignment for comparison matrices when it improves readability;
  - mandatory post-export inspection of the real PDF output;
  - explicit checks that `Config`-like identifier columns are not crushed while short numeric metric columns are not oversized;
  - explicit checks that metric headers do not get forced into wrapped or right-edge-stressed layouts by poor width allocation;
  - explicit checks that long headers wrap inside their own cells instead of spilling into adjacent columns;
  - explicit checks that wrapped identifier cells break at meaningful token boundaries rather than leaving isolated one- or two-letter fragments;
  - explicit checks that content stays comfortably inside each cell and does not sit almost on the borders;
  - explicit checks that table-cell content remains vertically centered, especially in rows mixing one-line and multi-line values;
  - explicit checks that major sections do not start near the bottom of a page and then immediately continue on the next page when a clean page-start is possible;
- if the PDF evidence is inconclusive, the report must not be considered validated yet.
- if both are missing, the export will fail until a compatible browser path is provided explicitly;
- the default workflow no longer leaves a persistent preview HTML file behind;
- temporary browser-profile directories are now standardized under `.temp/report_pipeline/browser_profiles/`.

## Run The Standardized Report Pipeline

Use the orchestration runner when you want one repository-owned command for:

- diagram regeneration;
- styled PDF export;
- raster validation of the real exported PDF.

For the current four structured-model explanatory reports:

```powershell
python scripts/reports/run_report_pipeline.py `
  --use-model-explanatory-reports `
  --regenerate-diagrams `
  --prefer-tool-env
```

If the repository-local validation environment does not exist yet, bootstrap it once:

```powershell
python scripts/reports/run_report_pipeline.py `
  --use-model-explanatory-reports `
  --regenerate-diagrams `
  --bootstrap-tool-env
```

What this does:

- optionally regenerates the repository-owned explanatory SVGs;
- exports the matching PDFs;
- writes validation images under `.temp/report_pipeline/pdf_validation/`;
- avoids repeating the individual commands manually.

Useful options:

- `--clean-temp`
  Reset the standardized report-pipeline temp root before the run.
- `--cleanup-validation-images`
  Delete validation PNG pages after a successful run.
- `--validation-python-path`
  Use an explicit Python interpreter for PDF validation.
- `--skip-pdf-export`
  Reuse already exported PDFs and only validate them.
- `--skip-pdf-validation`
  Export PDFs without the validation step.

## Regenerate The Model Report Diagrams

```powershell
conda run -n standard_ml_codex_env python scripts/reports/generate_model_report_diagrams.py
```

This command regenerates the current SVG assets stored under:

- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/`

Use it whenever:

- a conceptual or architecture diagram is updated;
- the layout of the model-report figures needs correction;
- the explanatory reports must be refreshed before PDF export.

## Validate The Real Exported PDF

After every styled report export, validate the real PDF artifact rather than relying only on the HTML preview.

```powershell
python scripts/reports/validate_report_pdf.py `
  --input-pdf-path doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf `
  --output-image-directory .temp/pdf_validation_training_configuration_analysis `
  --clean-output-directory
```

What this does:

- reads the exported PDF directly;
- rasterizes every page into `.png` images;
- overwrites the previous validation image folder when `--clean-output-directory` is used.

Use the generated page images to verify the actual PDF layout:

- borders are not clipped;
- section cards fit inside the A4 margins;
- long headers stay inside their own columns;
- identifier-like cells wrap at meaningful token boundaries;
- numeric columns are not oversized while identifier columns are crushed;
- major sections do not start at the bottom of a page unless the continuation remains visually coherent.

## Dataset Processing

## What The Processing Module Does

The dataset-processing logic lives in:

- `scripts/datasets/transmission_error_dataset.py`

This module:

- loads the validated TE CSV files already available in `data/datasets`;
- parses metadata from the file names and folder names;
- builds forward and backward directional samples;
- creates PyTorch `Dataset` and `DataLoader` objects;
- keeps helper functions ready for future raw-data TE reconstruction using:
  - `TE = theta_out - 81 * theta_in`
  - `DataValid` masks

Important dataset note:

- the CSV files currently present in the repository are already validated TE files;
- they do not contain raw encoder columns or `DataValid Forward` / `DataValid Backward` flags;
- the forward-position CSV header contains the original typo `Poisition_Output_Reducer_Fw`;
- the loader keeps compatibility with that original header and normalizes it internally to `position_output_reducer_fw_deg`.

## Shared Training Validation And Smoke-Test

## What Wave 0 Added

The repository now exposes two reusable pre-campaign training checks:

- `scripts/training/validate_training_setup.py`
- `scripts/training/run_training_smoke_test.py`

These utilities are intended to be reused across future model families, not only by the current feedforward baseline.

They rely on a shared training infrastructure that now standardizes:

- `experiment.model_family` in the training presets;
- a common metrics artifact schema;
- common output artifact names such as `training_config.yaml` and `metrics_summary.yaml`.

The same checks now also support the Wave 1 tree baselines through a reduced `scikit-learn` fit/predict path.

## Run The One-Batch Validation Check

```powershell
conda run -n standard_ml_codex_env python scripts/training/validate_training_setup.py `
  --config-path config/training/feedforward/presets/trial.yaml `
  --output-suffix validation_check
```

This command verifies:

- config loading;
- datamodule setup;
- model instantiation;
- batch shape correctness;
- finite loss and metrics on one batch.

For tree models, the check uses a reduced train/validation sample subset instead of the neural batch path.

It writes a `validation_summary.yaml` file under `output/validation_checks/<model_family>/<run_instance_id>/`.

## Run The Minimal Lightning Smoke Test

```powershell
conda run -n standard_ml_codex_env python scripts/training/run_training_smoke_test.py `
  --config-path config/training/feedforward/presets/trial.yaml `
  --output-suffix smoke_test `
  --fast-dev-run-batches 1
```

This command verifies:

- a minimal Lightning `fit` path;
- one-batch train/validation execution through `fast_dev_run`;
- manual checkpoint save;
- checkpoint reload.

For tree models, the check uses reduced train/eval subsets together with serialized model save/reload validation.

It writes:

- `smoke_test_summary.yaml`
- `smoke_test_checkpoint.ckpt`

under `output/smoke_tests/<model_family>/<run_instance_id>/`.

## Shared Training Artifacts

The feedforward training workflow now writes:

- `training_config.yaml`
- `metrics_summary.yaml`
- `run_metadata.yaml`

## Dataset Processing Configuration

The processing settings are stored in:

- `config/datasets/transmission_error_dataset.yaml`

Current configurable sections:

- `paths.dataset_root`
  Root folder of the CSV dataset, relative to the project root.

- `dataset.reduction_ratio`
  Reducer ratio used by the raw TE helper path.

- `dataset.angular_window_deg`
  Output-position window expected for valid rotation.

- `directions.use_forward_direction`
  Enables forward curves.

- `directions.use_backward_direction`
  Enables backward curves.

- `split.validation_split`
  Train/validation file split ratio.

- `split.test_split`
  Held-out test file split ratio.

- `split.random_seed`
  Seed used for split reproducibility.

- `dataloader.batch_size`
  Batch size used by the generated curve dataloaders.

- `dataloader.num_workers`
  Number of PyTorch dataloader workers.

## Use The Processing Module From Python

The most direct way to use the processing utilities is from Python.

### Example: Build Train, Validation, And Test Dataloaders From Config

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset'])); print(len(bundle['test_dataset']))"
```

What this does:

- reads `config/datasets/transmission_error_dataset.yaml`;
- collects CSV files from the configured dataset root;
- creates forward and backward directional samples;
- splits the files into train, validation, and test sets;
- returns a dictionary containing:
  - `train_dataset`
  - `validation_dataset`
  - `test_dataset`
  - `train_dataloader`
  - `validation_dataloader`
  - `test_dataloader`

### Example: Inspect One Training Batch

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); batch=next(iter(bundle['train_dataloader'])); print(batch['input_tensor'].shape); print(batch['target_tensor'].shape); print(batch['valid_mask'].shape)"
```

Expected batch content:

- `input_tensor`
  Padded tensor with features per point.

- `target_tensor`
  Padded tensor with TE targets.

- `angular_position_deg`
  Padded output-position tensor.

- `valid_mask`
  Boolean mask for valid points inside the padded batch.

- `sequence_length`
  Original sequence length for each curve.

- metadata tensors/lists for speed, torque, temperature, direction, and source file.

## Input Features Used In The Current Dataset Class

Each point currently includes these input features:

1. output angular position in degrees
2. speed in rpm
3. torque in Nm
4. oil temperature in degrees
5. direction flag (`+1` forward, `-1` backward)

The regression target is:

- Transmission Error in degrees

## Flatten A Padded Batch Into Point-Wise Tensors

If the model is trained point by point rather than sequence by sequence, you can flatten the padded batch.

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config, flatten_curve_batch; bundle=create_transmission_error_dataloaders_from_config(); batch=next(iter(bundle['train_dataloader'])); flat=flatten_curve_batch(batch); print(flat['input_tensor'].shape); print(flat['target_tensor'].shape)"
```

This removes the padding using the batch validity mask.

## Dataset Visualization

## What The Visualization Script Does

The visualization entry point is:

- `scripts/datasets/visualize_transmission_error.py`

This script:

- reads the visualization config;
- resolves the dataset config;
- selects one CSV file;
- loads forward and backward TE curves;
- plots TE against output angular position;
- either opens the plot or saves it to an image file.

## Visualization Configuration

The visualization settings are stored in:

- `config/visualization/transmission_error_visualization.yaml`

Main configurable fields:

- `paths.dataset_config_path`
  Path to the dataset-processing YAML config, relative to the project root.

- `selection.file_index`
  Default file index when no explicit CSV path is provided.

- `plot.figure_width`
  Figure width in inches.

- `plot.figure_height`
  Figure height in inches.

- `plot.figure_dpi`
  Figure DPI used for saved plots.

- `output.save_path`
  Optional default output path for saved figures.

## Save A Plot To File

This is the most robust option in terminal or headless environments.

```powershell
python -m scripts.datasets.visualize_transmission_error --save-path output\te_curve.png
```

What happens:

- the script reads the default YAML files in `config/visualization/` and `config/datasets/`;
- it selects the dataset file indicated by `selection.file_index`;
- it generates forward and backward TE curves;
- it saves the image to `output\te_curve.png`.

## Visualize A Specific Dataset File

If you want to inspect one exact CSV:

```powershell
python -m scripts.datasets.visualize_transmission_error --csv-path "data\datasets\Test_35degree\1000rpm\1000.0rpm0.0Nm35.0deg.csv" --save-path output\sample_te_curve.png
```

This bypasses the default file index and directly uses the selected CSV file.

## Override The Default File Index

If you prefer to keep the configured dataset root but change the selected file:

```powershell
python -m scripts.datasets.visualize_transmission_error --file-index 10 --save-path output\te_curve_10.png
```

## Structured Baseline Training

## What The Training Workflows Do

The static neural training entry point is:

- `scripts/training/train_feedforward_network.py`

This workflow trains the static neural TE baselines implemented with PyTorch Lightning:

- `feedforward`
- `harmonic_regression`
- `periodic_mlp`
- `residual_harmonic_mlp`

The tree-based training entry point is:

- `scripts/training/train_tree_regressor.py`

This workflow trains the current tabular structured baselines:

- `random_forest`
- `hist_gradient_boosting`

The script now prints a structured terminal summary with colorized section headers on Windows terminals, so the training configuration and run artifacts are easier to inspect than with the earlier raw dictionary dump.

The structured baseline stack is composed of:

- `scripts/models/feedforward_network.py`
  Feedforward backbone with hidden layers, activation, optional layer normalization, and dropout.

- `scripts/models/harmonic_regression.py`
  Harmonic regression backbone with optional operating-condition terms.

- `scripts/models/periodic_feature_network.py`
  Periodic-feature MLP backbone using harmonic feature expansion before the residual MLP.

- `scripts/models/residual_harmonic_network.py`
  Harmonic structured head plus residual MLP refinement backbone.

- `scripts/models/model_factory.py`
  Model selection layer used to instantiate the requested architecture.

- `scripts/training/transmission_error_datamodule.py`
  Lightning datamodule that reuses the TE curve dataset and converts curves into point-wise batches.

- `scripts/training/transmission_error_regression_module.py`
  Generic Lightning regression module with normalization, loss computation, optimizer setup, and validation metrics.

- `scripts/training/tree_regression_support.py`
  Shared flattening, estimator, metrics, and serialization utilities for the tree baselines.

- `config/training/feedforward/presets/baseline.yaml`
  Main training configuration file for the baseline.

- `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/`
  First prepared structured-baseline campaign package for Wave 1.

## Current Structured-Baseline Assumptions

The current static baseline program:

- trains point-wise on TE curve samples rather than with recurrent sequence modeling;
- computes normalization statistics from the training split only;
- uses the normalized tensors during optimization and reports interpretable metrics on denormalized TE values;
- uses validation-based early stopping and checkpoint selection;
- reloads the best checkpoint for the final validation and held-out test evaluation;
- saves machine-readable and human-readable reports for each completed run;
- ranks all completed families through the shared registry artifacts.

This is the first baseline only. It does not replace the future need for LSTM, RNN, or PINN models.

## Training Configuration

The training settings are stored in:

- `config/training/feedforward/presets/baseline.yaml`

An additional lighter proof-run configuration is also available in:

- `config/training/feedforward/presets/trial.yaml`

More aggressive workstation-oriented variants are also available in:

- `config/training/feedforward/presets/high_density.yaml`
- `config/training/feedforward/presets/high_epoch.yaml`
- `config/training/feedforward/presets/high_compute.yaml`

The current recommended practical feedforward preset is:

- `config/training/feedforward/presets/best_training.yaml`

The first prepared Wave 1 structured campaign package is available in:

- `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/`

Main configurable sections:

- `paths.dataset_config_path`
  Dataset-processing config used by the Lightning datamodule.

- `paths.output_root`
  Root output directory for immutable training runs.
  The current feedforward presets now point to `output/training_runs/feedforward`.

- `experiment.run_name`
  Name of the training run output folder.

- `experiment.model_type`
  Requested architecture name resolved by the model factory.

- `dataset.curve_batch_size`
  Number of directional curves loaded per batch before point extraction.

- `dataset.point_stride`
  Downsampling stride used when extracting point-wise samples from each curve.

- `dataset.maximum_points_per_curve`
  Optional cap on the number of points taken from each curve.

- `dataset.num_workers`
  PyTorch dataloader worker count.
  The current default is `4`, which is a conservative multiprocessing setting for this Windows-based training environment.

- `dataset.pin_memory`
  Pin-memory flag for the dataloaders.
  The current default is `true` to improve host-to-device transfer when training on GPU.

- `model.input_size`
  Expected point-wise feature dimension.

- `model.hidden_size`
  Hidden-layer sizes for the feedforward backbone.

- `model.output_size`
  Output dimension of the regression model.

- `model.activation_name`
  Activation function used in the hidden layers.

- `model.dropout_probability`
  Dropout probability used after hidden activations.

- `model.use_layer_norm`
  Enables or disables `LayerNorm` in the hidden stages.

- `training.learning_rate`
  Optimizer learning rate.

- `training.weight_decay`
  `AdamW` weight decay.

- `training.min_epochs`
  Minimum number of epochs.

- `training.max_epochs`
  Maximum number of epochs.

- `training.patience`
  Early-stopping patience.

- `training.min_delta`
  Minimum monitored improvement threshold.

- `training.log_every_n_steps`
  Lightning logging frequency.

- `training.fast_dev_run`
  Lightning developer-mode shortcut.

- `training.deterministic`
  Deterministic training flag.

- `runtime.accelerator`
  Lightning accelerator selection, typically `auto` or `gpu`.

- `runtime.devices`
  Lightning device selection, typically `auto` or an explicit GPU count.

- `runtime.precision`
  Trainer precision mode such as `"32"`, `"16-mixed"`, or `"bf16-mixed"`.

- `runtime.benchmark`
  Enables cuDNN benchmarking for stable-shape CUDA workloads.

- `runtime.use_non_blocking_transfer`
  Enables explicit non-blocking tensor transfer during batch-to-device movement when the host batch is pinned.

## Run The Default Training Command

From the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py
```

The direct script execution shown above is supported from the repository root. The training entry point bootstraps the project root into `sys.path`, so the internal `scripts.models`, `scripts.training`, and `scripts.datasets` imports resolve correctly even when the file is launched directly.

This command:

- loads `config/training/feedforward/presets/baseline.yaml`;
- builds the datamodule from `config/datasets/transmission_error_dataset.yaml`;
- uses `validation_split` plus `test_split` from the dataset config to create three file-level subsets;
- uses `num_workers: 4` and `pin_memory: true` in the point-wise dataloaders by default;
- enables `persistent_workers` internally when dataloader multiprocessing is active;
- uses explicit recursive tensor transfer to the selected device, with optional `non_blocking=True` support controlled by the runtime config;
- computes training normalization statistics;
- creates the feedforward model;
- prints a compact colorized summary for configuration, dataset, normalization, runtime, and output artifacts;
- suppresses the current low-signal Lightning `litlogger` startup tip and the known `_pytree` sanity-check warning;
- starts Lightning training, validation, and held-out testing;
- reloads the best checkpoint before the final evaluation phase;
- writes artifacts under `output/training_runs/<model_family>/<run_instance_id>/`.

Typical artifacts now include:

- `training_config.yaml`
  Snapshot of the effective run configuration.

- `run_metadata.yaml`
  Explicit run-artifact identity including `run_instance_id`.

- `checkpoints/`
  Best and last Lightning checkpoints.

- `best_checkpoint_path.txt`
  Plain-text pointer to the selected best checkpoint.

- `metrics_summary.yaml`
  Machine-readable validation and test metrics.

- `training_test_report.md`
  Human-readable training and testing summary.

- family/program best-result registries under:
  - `output/registries/families/<model_family>/`
  - `output/registries/program/`

## Run The Lightweight Proof Configuration

If you want a faster verification run before trying the default baseline, use the trial config:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/trial.yaml
```

This proof configuration:

- uses `run_name: te_feedforward_trial`;
- increases `dataset.point_stride` to reduce the sampled points per curve;
- caps the point count with `dataset.maximum_points_per_curve: 200`;
- reduces the epoch budget to a short verification range;
- still executes validation, held-out testing, and report generation.

The trial preset keeps `runtime.use_non_blocking_transfer: false` because it also keeps `pin_memory: false`, so asynchronous host-to-device copies would provide little practical benefit there.

## Workstation-Oriented Training Variants

If the workstation has strong CPU and GPU resources, the repository now also provides three heavier training configurations.

### `config/training/feedforward/presets/high_density.yaml`

Use this when the first priority is denser sampling of each TE curve:

- lower `point_stride` than the baseline;
- larger `curve_batch_size`;
- higher dataloader worker count.

This is the recommended first upgrade over the baseline when the goal is to test whether more curve detail improves the results.

### `config/training/feedforward/presets/high_epoch.yaml`

Use this when the first priority is a longer convergence window:

- same basic data density as the baseline;
- longer epoch budget;
- higher early-stopping patience.

This is useful when the baseline appears stable but not yet fully converged.

### `config/training/feedforward/presets/high_compute.yaml`

Use this when the goal is to push both data density and model capacity:

- denser point sampling;
- larger curve batches;
- larger hidden layers;
- longer epoch budget.

This is the most compute-heavy feedforward variant currently defined in the repository and is best treated as an offline benchmark rather than as the first PLC-oriented baseline.

### `config/training/feedforward/presets/best_training.yaml`

Use this when you want the current best practical feedforward training preset derived from the completed mixed campaign:

- `point_stride = 5`
- `curve_batch_size = 4`
- standard `128-128-64` architecture
- long `20-250` epoch schedule
- no large-model complexity penalty

This preset is the current recommended default because it achieved the best held-out `test_mae` across the currently executed feedforward configurations while remaining relatively efficient.

## GPU Runtime Optimization Notes

The repository now exposes explicit runtime controls for the GPU path without forcing aggressive settings by default.

Recommended practical usage:

- keep `runtime.precision: "32"` as the accuracy-safe baseline;
- try `runtime.precision: "16-mixed"` only when the GPU path is already numerically stable and faster throughput matters;
- try `runtime.precision: "bf16-mixed"` only if the local GPU stack supports it reliably;
- keep `runtime.benchmark: true` for this feedforward workload because tensor shapes are stable enough to benefit;
- keep `runtime.use_non_blocking_transfer: true` only when `dataset.pin_memory: true` is also enabled.

The current optimization pass is aimed at reducing CPU-to-GPU transfer stalls and exposing useful Lightning runtime flags. It is not intended to force full GPU saturation if that adds instability or unnecessary complexity.

## Current Dataloader Runtime Defaults

The current feedforward-training config now uses these dataloader defaults:

- `dataset.num_workers: 4`
- `dataset.pin_memory: true`

These values were selected as the first practical tuning step after the initial stable baseline:

- `num_workers: 4` reduces dataloader bottlenecks without jumping immediately to aggressive multiprocessing values on Windows;
- `pin_memory: true` is appropriate when the training run uses CUDA, which is the current expected setup for this repository.

If the project is later executed on CPU-only hardware or on a different workstation, these values can still be adjusted directly in `config/training/feedforward/presets/baseline.yaml`.

## Run Training With A Custom Config Path

If you want to launch the same workflow with a different YAML file:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/baseline.yaml
```

The script now exposes `--config-path`, so custom YAML files can be launched directly without using `python -c`.

To launch the current best practical feedforward preset directly:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/best_training.yaml
```

To launch one prepared Wave 1 structured-neural candidate directly:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py `
  --config-path config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/07_residual_h12_small_frozen.yaml
```

To launch one prepared Wave 1 tree candidate directly:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_tree_regressor.py `
  --config-path config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/09_random_forest_tabular.yaml
```

## Typical Training Outputs

The structured baselines write outputs under the configured family-specific training-run roots, for example:

- `output/training_runs/feedforward/`
- `output/training_runs/harmonic_regression/`
- `output/training_runs/periodic_mlp/`
- `output/training_runs/residual_harmonic_mlp/`
- `output/training_runs/tree/`

For the default run name, a typical output location is:

- `output/training_runs/feedforward/2026-03-17-20-05-11__te_feedforward_baseline/`

Typical generated artifacts include:

- a copy of the effective training config;
- TensorBoard logs;
- Lightning checkpoints;
- a text file containing the best checkpoint path;
- a run metadata snapshot;
- updated best-result registries.

## Inspect Neural Training Logs With TensorBoard

After a real training run, you can inspect logs with:

```powershell
tensorboard --logdir output\training_runs\feedforward
```

Then open the local TensorBoard URL shown in the terminal.

## Current Training Metrics

The static neural regression module currently logs:

- `train_loss`
- `train_mae`
- `train_rmse`
- `val_loss`
- `val_mae`
- `val_rmse`

The best checkpoint and early stopping are both driven by `val_mae`.

The tree baselines do not generate TensorBoard logs. Their ranking relies on the shared `metrics_summary.yaml` snapshots and the registry files.

## Batch Training Campaigns

## What The Batch Runner Does

The batch training entry point is:

- `scripts/training/run_training_campaign.py`

This runner:

- optionally copies one or more YAML files into the queue;
- executes queued YAML files sequentially;
- moves each configuration across `pending/`, `running/`, `completed/`, and `failed/`;
- keeps the same direct terminal logging behavior as the underlying single-run training script for supported model types;
- mirrors that live output into one terminal log per queue item;
- prints a compact campaign-progress summary before and after each run;
- generates a campaign manifest and markdown execution report under `output/training_campaigns/`.
- generates explicit `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and `campaign_best_run.md` files inside each campaign folder.

## Queue Layout

The persistent queue folders are:

- `config/training/queue/pending/`
- `config/training/queue/running/`
- `config/training/queue/completed/`
- `config/training/queue/failed/`

Keep reusable presets under:

- `config/training/feedforward/presets/`

Copy presets into `pending/` when preparing a campaign. Do not move the canonical preset files themselves.

Campaign-specific YAML files can also be stored in dedicated folders such as:

- `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/`

## Queue Presets Without Running Them Yet

```powershell
python scripts/training/run_training_campaign.py `
  config/training/feedforward/presets/baseline.yaml `
  config/training/feedforward/presets/high_epoch.yaml `
  --enqueue-only
```

## Run Everything Currently Pending

```powershell
python scripts/training/run_training_campaign.py
```

When the queued model type is currently supported by the in-process runner layer, the terminal now shows the same structured sections and Lightning progress bars used by `scripts/training/train_feedforward_network.py`. This removes the earlier delayed startup silence and avoids the previous broken Unicode progress-bar output caused by piped subprocess capture.

## Queue And Run In One Command

```powershell
python scripts/training/run_training_campaign.py `
  config/training/feedforward/presets/baseline.yaml `
  config/training/feedforward/presets/high_density.yaml `
  --campaign-name feedforward_density_check
```

## Batch Runner Outputs

Each campaign writes a new folder under:

- `output/training_campaigns/`

Typical generated artifacts:

- `campaign_manifest.yaml`
  Machine-readable index of executed queue items and artifact paths.

- `campaign_execution_report.md`
  Human-readable execution report listing what was tested and where the per-run results are stored.

- `campaign_leaderboard.yaml`
  Ranked campaign-local comparison entries using the repository selection policy.

- `campaign_best_run.yaml`
  Machine-readable winner of the campaign.

- `campaign_best_run.md`
  Human-readable summary of the campaign winner.

- `logs/*.log`
  Full terminal output mirrored for each queued YAML file while the same output stays visible live in the active terminal.

Use the generated campaign execution report as the source index for the required final report in `doc/reports/campaign_results/`.

Final campaign-results deliverables must include:

- the canonical Markdown report;
- the styled PDF export;
- a real PDF validation pass before the task is closed.

## Active Campaign State

The currently prepared or active campaign is tracked in:

- `doc/running/active_training_campaign.yaml`

This state file stores:

- campaign name;
- planning report path;
- campaign configuration file list;
- launch commands;
- protected files that should not be modified silently while the campaign is active.

Operational rule:

- approved campaign preparation must now include generated YAML files and the exact launch command;
- when the user confirms that the campaign has started, the campaign state should be updated to `running`;
- while the campaign is prepared or running, any edit to a protected campaign file requires a `CRITICAL WARNING` and explicit user approval first;
- when the user says the campaign is finished, use the stored state to gather artifacts for the final results report;
- when the user cancels the campaign, inspect completed, failed, running, and pending items before deciding what to keep or stop.

Current prepared Wave 1 campaign:

- campaign name: `wave1_structured_baseline_campaign_2026_03_17_21_01_47`
- planning report: `doc/reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md`
- config package: `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/`

## Typical Workflow For The Current Project

If you want to inspect the dataset and train the current baseline, use this sequence:

1. Activate the environment.
2. Check `config/datasets/transmission_error_dataset.yaml`.
3. Check `config/training/feedforward/presets/baseline.yaml`.
4. Inspect one dataset batch if needed.
5. Visualize one or more TE curves.
6. Start the selected structured baseline training run.
7. Inspect logs and checkpoints under `output/training_runs/` and check the best-result registries under `output/registries/`.

Example sequence:

```powershell
conda activate standard_ml_codex_env
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset']))"
python -m scripts.datasets.visualize_transmission_error --file-index 0 --save-path output\te_curve_0.png
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py
```

## Inference Status

Inference and export are not yet implemented as runnable project scripts.

This means there is currently no entry point such as:

- `inference/run_inference.py`
- `inference/export_onnx.py`
- `inference/runtime_validation.py`

So, at the moment, you cannot run a documented project inference or export command from this repository.

## What Is Already Ready For The Next Step

The repository now already has:

- a validated TE dataset;
- a YAML-driven dataset-processing configuration;
- PyTorch datasets and curve dataloaders;
- a TE visualization utility;
- a modular PyTorch Lightning feedforward training baseline;
- additional Wave 1 structured-neural baselines;
- tree-based structured benchmarks under the same artifact contract;
- a reusable datamodule and regression module structure for future architectures;
- technical, script-level, and user-facing documentation aligned with the current structure.

This is enough to extend the project toward:

1. recurrent sequence models such as RNN or LSTM
2. evaluation entry points
3. inference/export utilities
4. PINN-specific losses and training flows

## Recommended Next Development Order

To extend the repository cleanly, the recommended order is:

1. execute and analyze the prepared Wave 1 structured-baseline campaign
2. add a sequence-aware recurrent baseline on top of the current `scripts/training/` and `scripts/models/` structure
3. add a dedicated evaluation entry point
4. add inference and export utilities
5. extend the regression module toward physics-informed loss composition
6. add PINN-specific training and validation workflows

