# Simplified Dataset GitHub Publication

## Overview

The previously tracked dataset root was removed. Its intended replacement is
the complete dataset under `data/simplified_dataset/`.

The replacement contains 1,024 files totaling approximately 2.605 GiB. No
individual file is 100 MB or larger. The publication will be divided into
bounded commits and pushes so that each dataset commit remains below 1 GiB.

The unrelated untracked directories `data/original_dataset/` and
`data/polished_dataset/` are outside this change. Together they add more than
18 GiB and require a separate storage and publication decision.

## Technical Approach

Treat `data/simplified_dataset/` as the canonical replacement for the legacy
dataset root. Preserve all 1,024 files and partition the new content by
temperature surface:

1. Record removal of the legacy dataset root and add dataset-root metadata.
2. Add the complete `Test_25degree` surface.
3. Add the complete `Test_30degree` surface.
4. Add the complete `Test_35degree` surface.

Each temperature surface is approximately 0.87 GiB in the working tree. Before
each commit, verify the staged file set, staged aggregate size, maximum
individual file size, and generated Git object size. Push each commit
separately so that each transfer remains independently bounded.

Git LFS will not be used.

## Involved Components

- `data/simplified_dataset/`
  - Canonical replacement dataset containing 1,024 files.
- `data/simplified_dataset/Test_25degree/`
  - 341 files, approximately 0.869 GiB.
- `data/simplified_dataset/Test_30degree/`
  - 341 files, approximately 0.868 GiB.
- `data/simplified_dataset/Test_35degree/`
  - 341 files, approximately 0.868 GiB.
- `doc/README.md`
  - Canonical registration point for this technical document.

## Implementation Steps

1. Confirm approval of this technical document and its scope.
2. Exclude `data/original_dataset/` and `data/polished_dataset/` from all
   staging operations.
3. Stage and inspect the legacy-path removal plus dataset-root metadata.
4. Stage and inspect each temperature surface independently.
5. For every proposed commit, verify that no staged file is 100 MB or larger
   and that the staged aggregate remains below 1 GiB.
6. Create the approved commits without rewriting existing history.
7. Push each commit separately and verify the remote branch after every push.
