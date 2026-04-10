# Track Exact Paper Model Bundles With Git LFS

## Overview

This document records the narrow Git LFS action needed to keep the recently
generated exact-paper validation artifacts push-safe.

The exact-paper reimplementation produced five new
`paper_family_model_bank.pkl` artifacts under
`output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`.
Each of those files is larger than `100 MB`, so they cannot be pushed to
GitHub as regular Git objects.

The goal is to track only those five exact-paper model-bank bundles with Git
LFS, without broadening the rule to unrelated historical `.pkl` artifacts.

## Technical Approach

The change should remain intentionally narrow:

- add one Git LFS tracking rule that matches the exact-paper validation
  `paper_family_model_bank.pkl` artifact path pattern only;
- stage the new `.gitattributes` rule;
- re-stage the five oversized exact-paper `.pkl` files so they are stored as
  LFS pointers instead of normal Git blobs;
- leave unrelated large `.pkl` files untouched unless explicitly requested in a
  later task.

This preserves repository discipline:

- the exact-paper branch artifacts stay reproducible and commitable;
- historical large tree-model bundles are not silently swept into the same
  tracking decision;
- the commit surface stays aligned with the current approved work.

## Involved Components

- `.gitattributes`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `doc/README.md`

## Implementation Steps

1. Add a Git LFS rule for the exact-paper validation
   `paper_family_model_bank.pkl` path pattern only.
2. Re-stage the five newly generated exact-paper `.pkl` files so Git stores
   them as LFS pointers.
3. Verify that those files report `filter=lfs` under `git check-attr`.
4. Confirm that no newly staged regular Git blob exceeds `100 MB`.
5. Report completion and wait for explicit commit approval before creating any
   Git commit.
