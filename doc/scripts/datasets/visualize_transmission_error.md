# Visualize Transmission Error Script

## Overview

This script generates a plot of Transmission Error against output angular position for one validated dataset CSV.

It is stored in:

- `scripts/datasets/visualize_transmission_error.py`

The script is intended to provide a quick visual inspection tool for the processed TE curves before training or debugging the data pipeline.

## Main Role

The script:

- reads YAML runtime settings from `config/visualization/transmission_error_visualization.yaml`;
- reads the dataset root through `config/datasets/transmission_error_dataset.yaml`;
- selects one CSV file either by path or by file index;
- loads forward and backward TE curves;
- plots TE against output position;
- optionally saves the figure to disk.

## Main Functions

### `load_visualization_config`

Loads the visualization YAML configuration.

### `parse_command_line_arguments`

Parses optional runtime overrides such as:

- config path;
- explicit CSV path;
- file index;
- save path.

### `resolve_csv_file_path`

Selects the actual CSV file to visualize by using either:

- the explicit file path given on the command line;
- the file index from the dataset collection.

### `visualize_transmission_error_curves`

Creates the TE plot for the selected CSV file.

The figure includes:

- forward TE curve;
- backward TE curve;
- speed, torque, and temperature in the title.

### `main`

Coordinates configuration loading, CSV selection, and plotting.

## Inputs And Outputs

### Inputs

- validated TE CSV files in `data/datasets`
- visualization config in `config/visualization/transmission_error_visualization.yaml`
- dataset config in `config/datasets/transmission_error_dataset.yaml`

### Outputs

- interactive plot window when no save path is given;
- saved image file when `--save-path` is provided.

## Practical Use

Example usage:

```powershell
python -m scripts.datasets.visualize_transmission_error --file-index 0 --save-path output_te_plot.png
```

This command saves a TE plot for the first CSV file in the dataset collection.
