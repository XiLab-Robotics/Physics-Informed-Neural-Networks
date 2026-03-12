# Dataset Processing Pipeline

## Overview

This document defines the dataset-processing feature for the Transmission Error project.

The requested scope is:

- analyze the CSV files in `data/datasets`;
- align the data interpretation with `SpiegazioneSerieDati.pdf` and `Report Machine Learning.pdf`;
- compute or validate the Transmission Error (TE) using the reducer ratio `tau = 81`;
- prepare PyTorch `Dataset` and `DataLoader` utilities for model training;
- create a visualization script for processed TE curves versus angular position.

Important repository observation recorded on March 10, 2026:

- the folder present in the repository is `data/datasets`, not `data/dataset`;
- the available CSV files are already a validated TE dataset, not the raw acquisition dataset;
- all inspected CSV files share the same header, including the original forward-position typo:
  - `Poisition_Output_Reducer_Fw` (literal CSV typo)
  - `Transmission_Error_Fw`
  - `Position_Output_Reducer_Bw`
  - `Transmission_Error_Bw`
- the current repository snapshot does not expose raw encoder input/output columns or `DataValid Forward` / `DataValid Backward` flags.

This means the current implementation must distinguish between:

1. the validated TE dataset that is actually available now;
2. the raw dataset path described by the reference documents and needed to reconstruct TE directly from encoder signals and `DataValid` flags.

## Technical Approach

The processing feature will be implemented with a dual-path design.

### Path 1 - Validated TE Dataset (Current Repository Data)

For the CSV files currently stored in `data/datasets`:

- load forward and backward angular positions together with their TE values;
- parse operating conditions from folder/file naming:
  - speed from the file name;
  - torque from the file name;
  - oil temperature from the file name and parent test folder;
- convert each CSV into two directional samples:
  - one forward TE curve;
  - one backward TE curve;
- normalize the original CSV header typo `Poisition_Output_Reducer_Fw` inside the loader layer while keeping dataset compatibility;
- expose a processed sample format directly usable for PyTorch training.

Observed dataset characteristics:

- `969` CSV files are available;
- each inspected file contains a complete angular sweep close to `0-360 deg`;
- one inspected sample contains `19440` rows;
- temperatures available in file names are `25 deg`, `30 deg`, and `35 deg`;
- speeds span `100-1800 rpm`;
- torques span `0-1800 Nm`.

### Path 2 - Raw Dataset Reconstruction (Documented But Not Currently Available)

The reference documents require that TE be computed from encoder signals using the valid acquisition window:

- `TE = theta_out - tau * theta_in`
- `tau = 81`
- only samples inside `DataValid Forward` or `DataValid Backward` must be used;
- valid segments must correspond to the complete `0-360 deg` output rotation interval used for TE extraction.

Because the raw columns are not present in the current repository dataset, the first implementation will:

- define explicit helper functions for TE reconstruction from raw columns;
- keep the TE computation path available in code for future raw-data integration;
- use the already validated TE columns as the active path for the current repository data.

This preserves consistency with the reference workflow without pretending that the available CSV files still contain the raw signals.

### PyTorch Data Pipeline

The PyTorch data layer will follow a simple staged design:

- a CSV parsing utility to read and standardize one file;
- a processing utility to convert one file into forward/backward directional samples;
- a `Dataset` class that indexes all directional samples;
- a `DataLoader` factory with configurable batch size, shuffle flag, and train/validation split.

The returned sample should keep explicit, inspectable fields such as:

- angular position;
- transmission error;
- direction;
- speed;
- torque;
- temperature;
- source file path.

### Visualization

The visualization utility will:

- load one or more processed samples;
- plot TE against angular position;
- support forward and backward overlays;
- print the operating-condition metadata of the selected sample.

## Involved Components

- `doc/technical/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md`
  Technical record for this feature.

- `README.md`
  Main project document to reference this feature document.

- `data/datasets/`
  Source validated TE dataset currently available in the repository.

- `data/`
  Target area for dataset-processing modules.

- `training/` or a dedicated data-loading module path
  Target area for PyTorch `Dataset` / `DataLoader` integration.

- `utils/` or a dedicated plotting script path
  Target area for TE visualization.

## Implementation Steps

1. Add this technical document and register it in `README.md`.
2. Inspect the current validated TE CSV structure and implement a parser for the available columns.
3. Implement metadata extraction from file names and folder names.
4. Implement TE-processing helpers with two explicit paths:
   - validated TE pass-through for the current dataset;
   - raw TE reconstruction from `theta_in`, `theta_out`, and `DataValid` flags for future raw files.
5. Implement a PyTorch `Dataset` class and `DataLoader` factory around directional TE samples.
6. Implement a visualization script for TE versus output angular position.
7. Run a lightweight verification on a subset of CSV files and confirm shape, metadata, and plot generation.

