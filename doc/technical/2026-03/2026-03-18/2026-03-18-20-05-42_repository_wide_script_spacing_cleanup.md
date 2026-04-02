# Repository-Wide Script Spacing Cleanup

## Overview

This document defines a repository-wide formatting cleanup for the Python files under `scripts/`.

After the recent focused cleanup in `generate_model_report_diagrams.py`, the same vertical-spacing issue may still exist in other scripts: some top-level definitions are separated by more blank lines than intended, while the project style prefers consistent single blank separators between consecutive top-level definitions in ordinary cases.

The goal is to normalize that spacing across the repository-owned script tree without changing behavior.

## Technical Approach

The cleanup should stay formatting-only and should be applied conservatively.

The work should:

- inspect all Python files under `scripts/`;
- identify redundant blank lines between top-level `class` and `def` definitions;
- reduce those redundant separators to a consistent spacing;
- leave imports, comments, code logic, and local block spacing unchanged.

The cleanup must not:

- rename symbols;
- move logic;
- alter comments or docstrings for meaning;
- change runtime behavior or regenerate artifacts.

Files such as `__init__.py` that do not need any change should simply remain untouched.

## Involved Components

The work may affect:

- Python scripts under `scripts/datasets/`
- Python scripts under `scripts/models/`
- Python scripts under `scripts/reports/`
- Python scripts under `scripts/training/`

No documentation assets, reports, SVG files, or PDFs should need regeneration for this cleanup.

## Implementation Steps

1. Inspect all Python files under `scripts/`.
2. Detect redundant blank lines between top-level definitions.
3. Normalize the spacing only where the file currently has unnecessary extra blank separators.
4. Leave files unchanged where the spacing is already correct.
5. Run `py_compile` on all touched Python files to confirm the cleanup stayed behavior-neutral.
