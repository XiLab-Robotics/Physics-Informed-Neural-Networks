# 2026-05-16-20-14-35 Small Exact Model Bank Lfs Pointer Conversion

## Overview

This technical document plans the conversion of small exact-model-bank
`paper_family_model_bank.pkl` artifacts from Git LFS pointers into normal Git
blobs. The previous threshold cleanup commit limited future LFS tracking to the
two exact files greater than `100,000,000` bytes, but `431` smaller files remain
tracked as LFS pointers in the current Git index and history.

The requested target state is that those `431` files are re-added as normal Git
blobs while the two oversized files remain Git LFS objects.

## Technical Approach

Use the live working tree file sizes and the current `.gitattributes` rules as
the conversion boundary. The current measured conversion scope is:

- `431` files at or below `100,000,000` bytes.
- `4,337,922,817` bytes total, approximately `4,136.966 MiB`.
- `2` files above `100,000,000` bytes that must stay in Git LFS.

The conversion will be split into multiple commits to keep each staged batch
inspectable and to reduce per-commit pack pressure. Each batch will:

1. Build a deterministic path list from sorted matching files that are at or
   below `100,000,000` bytes.
2. Remove those paths from the Git index with `git rm --cached`.
3. Re-add the same working-tree files after the updated `.gitattributes` rules
   have removed LFS filtering for small paths.
4. Verify that no staged file in the batch exceeds `100,000,000` bytes.
5. Commit the batch with a clear batch-numbered message.

The planned batch size is about `500 MiB` per commit, yielding roughly `9`
conversion commits. If Git reports command-line or staging pressure, the batch
size will be reduced without changing the conversion boundary.

This plan intentionally does not rewrite repository history with
`git lfs migrate import/export`. It creates forward commits that replace the
current tree entries for small files with normal Git blobs. Historical commits
that already contain LFS pointers will still require LFS smudge skipping if a
checkout explicitly visits those historical revisions.

No Codex subagent is planned for this implementation.

## Involved Components

- `.gitattributes`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/**/paper_family_model_bank.pkl`
- Git index entries for the `431` small exact-model-bank pickle artifacts
- Git LFS pointer inventory from `git lfs ls-files`

## Implementation Steps

1. Confirm the worktree state and exclude unrelated dirty files from every
   batch commit.
2. Generate deterministic batch path lists for the `431` small files, targeting
   about `500 MiB` per batch.
3. For each batch, run `git rm --cached --pathspec-from-file`, then `git add
   --pathspec-from-file` against the same list.
4. Verify the staged batch size, file count, and absence of files greater than
   `100,000,000` bytes before committing.
5. Commit each batch with a message such as `Convert exact model bank small LFS
   blobs batch N`.
6. After all batches, verify that `git lfs ls-files` lists only the two
   oversized exact-model-bank `paper_family_model_bank.pkl` files for this
   artifact family.
7. Report the final commit list, remaining unrelated dirty files, and the
   command needed on the second workstation to rebase with LFS smudge disabled.
