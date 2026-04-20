# Dataset Split Export Utilities

## Canonical Split Export

The script [export_dataset_split.py](/C:/Users/XiLabTRig/Documents/Physics-Informed%20Machine%20Learning/StandardML%20-%20Codex/scripts/datasets/export_dataset_split.py)
exports the canonical dataset split used by the repository for the current
dataset configuration.

Its purpose is to let a colleague reproduce the exact same train, validation,
and test partition outside the automated repository training workflow.

## What The Script Reproduces

The export follows the same repository-owned split logic used by the current
dataset configuration:

- split scope: unique CSV file paths;
- randomization: Python `random.Random(seed).shuffle(...)`;
- random seed: `42`;
- validation split: `20%`;
- test split: `10%`;
- implied train split: `70%`;
- assignment order:
  - `validation`;
  - `test`;
  - remaining files go to `train`.

The directional configuration also matches the repository default:

- `forward` direction enabled;
- `backward` direction enabled.

This means the script exports both:

- unique-file manifests;
- direction-aware manifests that preserve the `forward` / `backward` labels.

## Command-Line Usage

Run the script from the repository root:

```powershell
python -B scripts\datasets\export_dataset_split.py --output-directory ".\output\dataset_split_export"
```

You can also point it to a custom dataset config if needed:

```powershell
python -B scripts\datasets\export_dataset_split.py --config-path "config\datasets\transmission_error_dataset.yaml" --output-directory ".\output\dataset_split_export"
```

## Exported Files

The output directory will contain:

- `train_unique_files.csv`
- `validation_unique_files.csv`
- `test_unique_files.csv`
- `train_directional_manifest.csv`
- `validation_directional_manifest.csv`
- `test_directional_manifest.csv`
- `dataset_split_summary.yaml`

## File Meaning

### Unique File Manifests

The `*_unique_files.csv` files contain one row per physical dataset CSV file.

They are usually the best handoff format when a colleague wants to integrate
the split into another Python workflow.

Columns:

- `source_file_path`
- `speed_rpm`
- `torque_nm`
- `oil_temperature_deg`

### Directional Manifests

The `*_directional_manifest.csv` files keep the same file partition, but also
expand each file into its directional entries.

Columns:

- `source_file_path`
- `direction_label`
- `direction_flag`
- `speed_rpm`
- `torque_nm`
- `oil_temperature_deg`

Use these files when the downstream workflow needs to preserve the repository
distinction between `forward` and `backward`.

### YAML Summary

The `dataset_split_summary.yaml` file records:

- the seed;
- the split percentages;
- the assignment order;
- the direction configuration;
- the final file counts and directional-entry counts.

## Practical Recommendation

For most external Python-side manual work, start from:

- `train_unique_files.csv`
- `validation_unique_files.csv`
- `test_unique_files.csv`

These files are simpler than the directional manifests and are usually enough
to reconstruct a custom loader.

If the downstream workflow must preserve the repository directional semantics,
use the `*_directional_manifest.csv` files instead.

## Python Usage Example

Example using the exported `*_unique_files.csv` files:

```python
from pathlib import Path

import pandas as pd

split_root = Path(r".\output\dataset_split_export")

train_manifest = pd.read_csv(split_root / "train_unique_files.csv")
validation_manifest = pd.read_csv(split_root / "validation_unique_files.csv")
test_manifest = pd.read_csv(split_root / "test_unique_files.csv")

train_file_list = train_manifest["source_file_path"].tolist()
validation_file_list = validation_manifest["source_file_path"].tolist()
test_file_list = test_manifest["source_file_path"].tolist()

print(f"Train files: {len(train_file_list)}")
print(f"Validation files: {len(validation_file_list)}")
print(f"Test files: {len(test_file_list)}")
```

Example using the directional manifests:

```python
from pathlib import Path

import pandas as pd

split_root = Path(r".\output\dataset_split_export")

train_directional_manifest = pd.read_csv(split_root / "train_directional_manifest.csv")

forward_train = train_directional_manifest[
    train_directional_manifest["direction_label"] == "forward"
]
backward_train = train_directional_manifest[
    train_directional_manifest["direction_label"] == "backward"
]

print(f"Forward train entries: {len(forward_train)}")
print(f"Backward train entries: {len(backward_train)}")
```

## Notes

- The split is file-based, not row-based.
- The split percentages are applied to the unique CSV file list.
- Because the script uses the repository seed and the same randomization logic,
  the output is intended to be stable and reproducible across reruns.
