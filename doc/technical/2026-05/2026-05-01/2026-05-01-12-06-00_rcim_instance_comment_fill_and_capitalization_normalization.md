# RCIM Instance Comment Fill And Capitalization Normalization

## Overview

This document formalizes one narrow follow-up cleanup pass over:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`

The user manually refined these two files and intentionally left many inline
comment placeholders as standalone `#` lines. The repository-owned follow-up
pass must:

- fill every empty `#` placeholder with a meaningful inline comment;
- normalize the capitalization of the existing inline comments so they follow
  the repository-authored style already established in the recovered workflow;
- keep the numerical logic unchanged.

## Technical Approach

The pass is intentionally mechanical and conservative.

The implementation will:

1. scan both instance files for standalone `#` placeholders;
1. replace each placeholder with a short, concrete inline comment that matches
   the nearby logic block;
1. normalize existing inline comments to the same visual style:
   - Title-Case emphasis on the main words;
   - short comment lines preferred over verbose prose;
   - no silent rewrites of the executable logic;
1. leave variable names, function names, and control flow unchanged;
1. run Python compile checks and a smoke validation on the recovered workflow
   afterward.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`
- `doc/technical/2026-05/2026-05-01/README.md`
- `doc/README.md`

## Implementation Steps

1. inspect all standalone `#` lines in `instance_v4.py` and `instance_v5.py`;
1. fill each placeholder with a nearby logic-aware comment;
1. normalize the capitalization of the surrounding inline comments;
1. run:
   - `py_compile` on the two touched instance files;
   - one recovered-workflow smoke run, preferably `paper_eval`;
   - Markdown QA on the touched documentation scope.
