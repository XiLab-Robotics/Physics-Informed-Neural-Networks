# Standalone And Repository Polished Dataset Generators

## Overview

Maintain two complete polished transmission-error dataset generators:

- a standalone script at
  `data/polished_dataset/generate_polished_dataset.py`, usable independently
  from repository modules on another computer;
- a full repository-integrated copy at
  `scripts/datasets/generate_polished_transmission_error_dataset.py`.

The standalone script must retain its complete implementation. It must not be
reduced to a launcher or import the repository copy.

Before implementation, report all identified defects and proposed corrections
to the user and wait for explicit approval.

## Technical Approach

First audit the existing script without changing it. Classify findings as
confirmed defects, portability limitations, safety risks, or intentional
historical behavior.

After approval, minimally repair the standalone script while preserving its
functions, formulas, output schema, and ability to run without repository
imports. Replace workstation-specific absolute paths with portable path
handling and apply only approved bug fixes and comment corrections.

Then copy the repaired complete implementation into `scripts/datasets/`.
The repository copy must remain structurally aligned with the standalone
version; differences should be limited to repository path resolution and
repository-facing defaults or documentation.

## Involved Components

- `data/polished_dataset/generate_polished_dataset.py`
- `scripts/datasets/generate_polished_transmission_error_dataset.py`
- `data/polished_dataset/README_POLISHED_CSV.md`
- `doc/scripts/datasets/`
- `doc/guide/project_usage_guide.md`
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`
- `site/guide/`
- `doc/README.md`

## Implementation Steps

1. Audit the unchanged standalone script and report every proposed fix before
   implementation.
2. Preserve the verified gear-ratio, validity-window, zeroing, differentiation,
   naming, duplicate-selection, and CSV-format behavior.
3. Apply the approved minimal portability and correctness fixes to the complete
   standalone script without adding repository dependencies.
4. Create a complete repository copy under `scripts/datasets/`, changing only
   path handling and repository-facing defaults where necessary.
5. Compare the two implementations and document every intentional difference.
6. Add script documentation with exact standalone and repository commands, and
   update the relevant dataset references, usage guide, index, and portal.
7. Verify compilation, controlled single-file generation, full inventory,
   failure behavior, and numerical parity against tracked polished outputs.
8. Perform the mandatory new-script style-compliance review, run scoped
   Markdown QA, and rebuild the Sphinx portal with warnings treated as errors.
