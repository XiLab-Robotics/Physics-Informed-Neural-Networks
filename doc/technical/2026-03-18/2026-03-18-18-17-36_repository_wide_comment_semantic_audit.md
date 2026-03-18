# Repository-Wide Comment Semantic Audit

## Overview

This document defines a repository-wide audit of the Python comments inside `scripts/` with a very specific goal:

- verify that each existing section comment accurately matches the code block or function stage it describes;
- correct comments that are misleading, outdated, imprecise, or no longer aligned with the actual implementation.

The user explicitly requested that comments must not be wrong. This means the task is not just about comment quantity or style consistency, but about semantic correctness.

The audit should therefore focus on whether each comment still reflects the real behavior of the lines directly below it.

## Technical Approach

The work should be performed as a semantic review rather than as a blind style pass.

### 1. Audit Scope

The review should cover the Python scripts under:

- `scripts/datasets/`
- `scripts/models/`
- `scripts/reports/`
- `scripts/training/`

The tiny `__init__.py` files do not need comment retrofits unless they contain actual misleading content.

### 2. Comment Review Criteria

A comment should be corrected if it is:

- too strong compared with what the code actually guarantees;
- too narrow compared with what the code now does;
- stale after a refactor;
- semantically off by one stage;
- describing an implementation detail that is no longer true.

Examples of issues this audit should catch:

- comments that say a path is saved when the code only resolves it;
- comments that mention one model family while the code is already generalized;
- comments that say a block reloads or validates something different from the real behavior;
- comments that describe one branch while the code below actually handles several cases.

### 3. Keep Good Comments Intact

The audit should not rewrite comments that are already correct and useful.

The goal is:

- semantic correctness first;
- minimal churn second.

### 4. Preserve The Existing Local Style

When a correction is needed, the replacement comment should remain:

- short;
- high-signal;
- section-oriented;
- stylistically aligned with the repository.

## Involved Components

The work may affect any Python script under `scripts/`, especially:

- `scripts/training/`
- `scripts/reports/`
- `scripts/models/`
- `scripts/datasets/`

No behavioral code changes are intended unless a comment reveals a real code bug that must be explicitly escalated.

## Implementation Steps

1. Audit the comments in all Python scripts under `scripts/`.
2. Identify the comments whose wording does not accurately match the code.
3. Correct only the inaccurate or stale comments.
4. Leave already accurate comments unchanged.
5. Verify syntax after the comment-only refactor.
