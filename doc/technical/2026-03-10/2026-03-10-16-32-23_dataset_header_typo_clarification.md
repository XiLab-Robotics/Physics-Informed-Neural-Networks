# Dataset Header Typo Clarification

## Overview

This document defines the requested clarification and cleanup for the forward-position dataset header name currently appearing as `Poisition_Output_Reducer_Fw`, which is the literal typo stored in the original CSV files.

Repository verification performed on March 10, 2026 shows that:

- the CSV files inside `data/datasets/` really use the misspelled header `Poisition_Output_Reducer_Fw` as their original first-column name;
- the dataset loader currently supports that header for compatibility with the real files;
- some technical documents also mention the misspelled name directly, which can create confusion about whether it is an implementation typo or a dataset-origin typo.

The goal of this change is to keep the code compatible with the actual dataset while improving clarity in the project documentation and in any explanatory code comments.

## Technical Approach

The correction should distinguish between two different concepts:

1. the literal header name present in the dataset files:
   - `Poisition_Output_Reducer_Fw`
2. the canonical internal meaning used by the code after normalization:
   - `position_output_reducer_fw_deg`

The implementation should therefore preserve dataset compatibility while making the wording clearer wherever the typo appears in repository-authored text.

The planned cleanup is:

- keep dual-header support in the loader because the dataset files still contain the typo;
- update technical documents so they explicitly say that `Poisition_Output_Reducer_Fw` is the original CSV typo;
- prefer the correctly spelled wording `Position_Output_Reducer_Fw` only when referring to the intended semantic name, not when quoting the dataset literally;
- avoid leaving ambiguous wording that looks like an accidental typo introduced by the repository code.

## Involved Components

- `doc/technical/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md`
- `README.md`
- `doc/README.md`
- `doc/technical/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md`
- `scripts/datasets/transmission_error_dataset.py`
- any additional repository-authored documentation files that mention `Poisition_Output_Reducer_Fw`

## Implementation Steps

1. Create this technical document and register it in the main documentation indexes.
2. After user approval, inspect the repository-authored files that mention `Poisition_Output_Reducer_Fw`.
3. Update documentation text so it explicitly labels `Poisition_Output_Reducer_Fw` as the original CSV typo.
4. Keep the loader compatible with the real dataset header and review code comments/docstrings for ambiguity.
5. Verify the final wording with a repository-wide search.
6. Create a Git commit with a repository-aligned title and body summarizing the clarification.
