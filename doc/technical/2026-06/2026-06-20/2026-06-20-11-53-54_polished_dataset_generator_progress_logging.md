# Polished Dataset Generator Progress Logging

## Overview

Add visible terminal progress reporting to the relocated standalone polished
dataset generator and to the repository-integrated copy.

The standalone script is now located at:

- `data/generate_polished_dataset.py`

The repository-integrated script remains at:

- `scripts/datasets/generate_polished_transmission_error_dataset.py`

Before adding logging, correct the standalone default input path for its new
location. Preserve the processing equations, CSV schema, duplicate handling,
and safety checks.

## Technical Approach

Use the current `tqdm` iterable API to wrap the selected source-record loop with
an explicit total, description, file unit, and dynamic terminal width. Use
`tqdm.write()` for skip and error messages so verbose output does not corrupt
the live progress bar.

Keep progress behavior controlled by module constants so both complete scripts
remain directly runnable without a new command-line interface. Add concise
startup, inventory, configuration, and completion messages around the progress
bar.

The standalone and repository copies will remain identical outside their
intentional path blocks. Add `tqdm` to the main dependency specification and
document the standalone installation requirement.

## Involved Components

- `data/generate_polished_dataset.py`
- `data/polished_dataset/generate_polished_dataset.py`
- `scripts/datasets/generate_polished_transmission_error_dataset.py`
- `requirements.txt`
- `data/polished_dataset/README_POLISHED_CSV.md`
- `doc/scripts/datasets/generate_polished_transmission_error_dataset.md`
- `doc/guide/project_usage_guide.md`
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`
- `site/guide/polished_dataset_generator.md`
- `doc/README.md`

## Implementation Steps

1. Confirm whether the old data-local script is now legacy or should remain
   synchronized with the relocated standalone copy.
2. Correct the relocated standalone input and output defaults relative to the
   `data/` directory.
3. Add `tqdm` progress display and `tqdm.write()` operational messages to both
   active complete implementations.
4. Add verbose startup, inventory, current-file, skip, failure, and completion
   reporting without changing generated CSV content.
5. Declare the `tqdm` dependency in `requirements.txt` and document standalone
   installation and execution.
6. Verify compilation, dependency import, full inventory, one-file progress
   rendering, error-message rendering, implementation alignment, and numeric
   parity against tracked polished outputs.
7. Run the mandatory new-script style review, scoped Markdown QA, and the
   warning-as-error Sphinx build.
