# HYG-07 Dataset Split and RCIM Operational Contract Alignment

- **Prepared:** 2026-11-22 (repository maintenance session; filename timestamp is a document identifier, not independent clock evidence).
- **Baseline:** `XiLab-Robotics/Physics-Informed-Neural-Networks/main@cde3d7279fcb3ae5f5e91840da6a91a0c5134507`.
- **Tracking:** [Repository hygiene issue #2](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/issues/2).
- **Owner direction:** Continue the scoped HYG-07 cleanup; do not change historical experiment results, datasets, model weights, or PLC sources.

## Overview

Resolve three current-facing documentation errors and one conditional error
in the training DataModule's test-split contract. The default dataset
configuration already requests a nonempty test split (`test_split: 0.1`)
and remains unchanged. This is repository maintenance, not a new training
campaign or scientific/model acceptance.

## Technical Approach

1. Replace the workstation-specific absolute Windows link in
   `scripts/datasets/README.md` with a relative link.
2. Correct two operational RCIM README references to the actual accepted
   `models/polished_dataset/paper_reference/rcim_track1/` layout:
   both `setpoints` and `actual_values`, each with `forward`,
   `backward`, and `global` directories. Do not rewrite historical
   reports, archive IDs, or dataset/model provenance.
3. Keep `split_directional_file_manifest` compatible with optional
   `test_split=0.0` for low-level nontraining consumers. In
   `TransmissionErrorDataModule.setup`, explicitly reject an empty
   test manifest immediately after resolution and before constructing
   any curve datasets. The shared training and tree-regression consumers
   require a test set, so do not silently fabricate or redistribute
   train/validation/test memberships.
4. Add isolated, synthetic-manifest regression tests for zero-test
   fail-fast and the ordinary nonzero-test path, without reading large
   datasets, training models, or reaching PLC hardware.

## Involved Components

| Path | Scope |
| --- | --- |
| `scripts/datasets/README.md` | Portable link and split-contract note |
| `scripts/paper_reimplementation/rcim_ml_compensation/README.md` | Current accepted RCIM archive paths |
| `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md` | Current archive-root reference |
| `scripts/training/transmission_error_datamodule.py` | Nonempty-test precondition for training |
| `scripts/testing/test_transmission_error_datamodule_split_contract.py` | Focused, source-adjacent synthetic regression coverage |
| `doc/README.md` | Register this technical decision |

Read-only boundaries include `scripts/datasets/transmission_error_dataset.py`,
`config/datasets/transmission_error_dataset.yaml`, the accepted RCIM model
artifacts, training archives, and all TwinCAT/TestRig repositories.

## Implementation Steps

1. Confirm the exact base commit, source blobs, current model archive layout,
   and consumer assumptions in shared training and tree regression.
2. Publish this technical plan and link it from the canonical documentation
   index before changing code.
3. Apply only the listed README references, DataModule guard, and focused
   regression tests on a short-lived maintenance branch.
4. Verify the exact GitHub diff, no unrelated files, source syntax, Markdown
   structure, and available nonheavy checks.
5. Open a pull request against protected `main`, inspect its required quality
   workflow on the exact head SHA, and use normal review/merge gates.
6. Independently verify post-merge main quality and Pages; only then remove
   the temporary branch. Reconcile coordinator memory, backlog and SRC/K/C
   without claiming training or PLC qualification.

## Verification and Release Boundaries

- Source-state and conditional defect analysis: **SOURCE_STATIC_VERIFIED**.
- Technical approach: **PREPARED**, owner-directed HYG-07 scope.
- Current default split and train-only normalization: **UNCHANGED**.
- Synthetic unit tests: **NOT EXECUTED until a compatible test environment
  runs them**; adding test source is not a passing test receipt.
- Scientific dependency installation, full training, model numerical parity,
  native XAE Build, PLC runtime and compensation: **NOT EXECUTED**.
- Heavy CI, training runner and machine use: **CI_GATE_BLOCKED** absent a
  separately verified runner, budget and approval.
- PR source application and post-merge publication must be reported as
  distinct states rather than inferred from this plan.
