# Polished Transmission Error Dataset Generators

## Overview

The repository maintains two complete copies of the polished transmission-error
dataset generator:

- `data/generate_polished_dataset.py`
- `scripts/datasets/generate_polished_transmission_error_dataset.py`

The first copy is standalone and does not import repository modules. The second
copy is integrated into the repository path layout. Their processing logic is
identical.

## Intentional Path Difference

The standalone script resolves paths relative to its own location:

```text
input  = ../original_dataset
output = ./generated_polished_dataset
```

This means that the following portable bundle works on another computer:

```text
data/
  generate_polished_dataset.py
  original_dataset/
  polished_dataset/
```

Run it with:

```powershell
python data/generate_polished_dataset.py
```

The repository copy resolves paths from the repository root:

```text
input  = data/original_dataset
output = output/generated_polished_dataset
```

Run it with:

```powershell
conda run --no-capture-output -n pinns_env python scripts/datasets/generate_polished_transmission_error_dataset.py
```

## Configuration Constants

Both scripts retain the same editable constants:

```python
USE_FORWARD_DIRECTION = True
USE_BACKWARD_DIRECTION = True
OVERWRITE_EXISTING_FILES = False
```

Set one direction flag to `False` when only one direction is required.

Existing destination files are protected by default. Set
`OVERWRITE_EXISTING_FILES = True` only when replacing generated files is
intentional.

Progress and verbose terminal reporting are controlled by:

```python
SHOW_PROGRESS_BAR = True
VERBOSE_LOGGING = True
```

The scripts print their resolved paths and direction configuration, report the
accepted source inventory, display a `tqdm` progress bar with the current
filename, and print a final export summary. Skip and error messages use
`tqdm.write()` so they do not corrupt the live bar.

The standalone script requires:

```powershell
python -m pip install "tqdm>=4.67,<5.0"
```

The repository environment installs the same dependency through
`requirements.txt`.

## Confirmed Corrections

The current scripts include these approved corrections:

- removed workstation-specific absolute paths;
- made the standalone defaults relative to the script location;
- made repository defaults relative to the repository root;
- made raw-row parsing atomic, preventing partially numeric rows from
  producing columns with different lengths;
- added checks for missing or invalid input and output paths;
- rejected identical input and output paths;
- rejected empty supported-source inventories;
- preflighted all planned destinations before writing, preventing silent
  replacement and collision-driven partial output;
- made processing skips fail the final run instead of reporting success;
- replaced the broad generated-folder prefix rule with explicit known folder
  names.

## Preserved Historical Behavior

The following behavior remains unchanged:

- gear ratio `81`;
- sample time `0.25 ms`;
- forward and backward `DataValid` selection;
- output-side zeroing and cluster correction;
- first-sample `theta_dot` convention;
- duplicate-condition selection;
- ignored historical filename list;
- output hierarchy, filenames, header, numeric precision, and equations.

The ignored source list still matches filenames globally rather than by full
relative path. This is intentional because those names identify the known
historical exceptions in the original dataset.

## Verification

Both scripts compile in `pinns_env`. A controlled test using:

```text
data/original_dataset/Test_35deg/1800rpm/1800.0rpm0.0Nm35.0deg.csv
```

generated both directions from each implementation. The standalone and
repository copies were byte-identical to each other and to the corresponding
tracked polished CSV files.
