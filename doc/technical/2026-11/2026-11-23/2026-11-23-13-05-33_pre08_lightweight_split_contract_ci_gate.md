# PRE08-QA — Existing Standard-Library Split Regressions in CI

**Clock checked:** 2026-11-23 13:05:33 Europe/Rome.
**Source baseline:** `main@1f6215eb6c89cf4bab9890476ba06446e3bdcdff`.

## Overview

The HYG-07 change added three standard-library AST/source-contract regressions
in `scripts/testing/test_transmission_error_datamodule_split_contract.py`,
but CI only compiles Python files rather than running these unit tests. Run the
existing tests explicitly in the existing quality job without changing any
scientific training, datasets or ONNX outputs.

## Technical Approach

Add exactly one workflow step between Python syntax verification and Sphinx:
`python -B -m unittest discover -s scripts/testing -p "test_transmission_error_datamodule_split_contract.py" -v`.
The tests isolate the production DataModule guard using AST and check
zero-test failure, nonempty-test acceptance and the unchanged 10% default.

This is not a full Lightning/PyTorch integration test and cannot prove that
historic train/test conditions are independent. No new dependency, runner,
scheduled trigger or separate manual dispatch is required.

## Involved Components

- `.github/workflows/ci.yml` — one focused test-execution step.
- `scripts/testing/test_transmission_error_datamodule_split_contract.py` — unchanged.
- `scripts/training/transmission_error_datamodule.py` — unchanged.
- `config/datasets/transmission_error_dataset.yaml` — unchanged.
- `doc/README.md` — canonical index link to this technical plan.

No models, datasets, training scripts, heavy science tests, TwinCAT, TestRig,
machine or deployment changes.

## Implementation Steps

1. Add/register this document before implementation.
2. Preserve the existing CI setup, sparse checkout, Markdownlint,
   documentation dependencies and Sphinx build.
3. Add the exact `unittest discover` command in the existing quality job.
4. Check the workflow diff, then inspect the PR's existing quality run for
   each test result; no new heavyweight or dedicated workflow is launched.
5. Mark only the AST/source-contract tests as validated by the actual run SHA.
   No training generalization, ONNX or PLC assertions follow from these tests.
6. Continue the normal PR merge review, publication and coordinator
   provenance tracking. HYG-08 stays deferred.
