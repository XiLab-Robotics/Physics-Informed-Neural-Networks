# Original And Polished Dataset GitHub Publication

## Overview

Publish the complete raw dataset under `data/original_dataset/` and its direct
derived export under `data/polished_dataset/` to GitHub without Git LFS.

The raw dataset contains 979 files totaling 12,346,336,375 bytes. The polished
dataset contains 1,940 files totaling 7,233,876,233 bytes, including
`generate_polished_dataset.py` and `README_POLISHED_CSV.md`.

No individual file reaches 100 MiB. The largest detected file is 58,294,748
bytes, approximately 55.594 MiB.

## Technical Approach

Use deterministic path-sorted batches capped at 900,000,000 working-tree bytes.
This safety margin keeps every commit below both 1 GB and 1 GiB before Git
compression.

The expected publication sequence is:

1. Add the dataset provenance files and this approved publication plan.
2. Add `data/original_dataset/` through 14 path-sorted data commits.
3. Add the remaining `data/polished_dataset/` content through 9 path-sorted
   data commits.
4. Push each commit independently and verify the remote branch after every
   push.

Before each commit, verify:

- staged paths belong only to the intended batch;
- staged working-tree bytes are below 1,000,000,000;
- no staged file is 100 MiB or larger;
- Git object bytes introduced by the commit remain below 1 GiB;
- the preceding commit has already reached `origin/main`.

Git LFS will not be configured or used.

## Involved Components

- `data/original_dataset/`
  - Canonical raw measurement dataset.
  - 979 files and approximately 11.498 GiB.
- `data/polished_dataset/`
  - Direct derived dataset generated from the raw measurements.
  - 1,940 files and approximately 6.737 GiB.
- `data/polished_dataset/generate_polished_dataset.py`
  - Python generator for the polished export.
- `data/polished_dataset/README_POLISHED_CSV.md`
  - Existing description of the polished CSV format and generation behavior.
- `doc/README.md`
  - Canonical registration point for this technical document.

## Implementation Steps

1. Obtain explicit approval of this technical document.
2. Commit and push the provenance script, polished-dataset documentation, and
   approved technical-plan registration.
3. Enumerate raw dataset files in stable case-insensitive path order and divide
   them into batches no larger than 900,000,000 bytes.
4. For each raw-data batch, stage only its manifest paths, run the size checks,
   create the commit, push it, and verify synchronization.
5. Enumerate the remaining polished dataset files with the same ordering and
   batching rule.
6. For each polished-data batch, repeat the stage, validation, commit, push,
   and synchronization sequence.
7. Confirm that all 979 raw files and all 1,940 polished files are tracked.
8. Confirm that the worktree contains no remaining untracked files under
   either dataset root.
