# Portable ONNX Evaluator — Documentation Hygiene (HYG-05)

- **Date:** 2026-11-22 (Europe/Rome).
- **Repository:** `XiLab-Robotics/Physics-Informed-Neural-Networks`.
- **Branch:** `track2-portable`; source baseline `965a45b9e26d3262bc5c77d36d40a2a341be9886`.
- **Owner scope:** retain the standalone Track 2 evaluation branch and correct its documentation.
- **State at plan creation:** PREPARED; source and model execution not requalified.

## Overview

Keep `track2-portable` as a separate, reproducibility-oriented offline ONNX curve-evaluation surface. This historical Track 2 utility is **not** the full research-main TE Curve Verification Pipeline (CVP 1.1–1.5), a new model training pipeline, a PLC runtime, or a scientifically accepted compensation result.

The independent Git-tree audit counted 1,014 `.onnx` files in `models/`, 2,907 CSV files in `data/`, and 42 historical output blobs. These are tracked archive inventories, not fresh evaluation receipts.

## Technical Approach

- Clarify inference family and input contracts: RCIM harmonic coefficients versus Direct TE pointwise/sequence models.
- Document actual CLI behavior and safe examples anchored to existing model/CSV paths.
- Highlight the current `--curve-dir` limitation: when `--curve-csv` is omitted, the hard-coded `CURVE_CSV_PATH_LIST` remains active and is combined with directory discoveries; do not claim directory-only evaluation.
- Identify Python syntax prerequisites, unpinned dependencies, `CPUExecutionProvider`, 33-sample sequence default, and read-only offline scope.
- Rewrite `data/polished_dataset/README_POLISHED_CSV.md` to distinguish packaged data from generator source/docs available only on research `main`; retain the units and original acquisition/zeroing caveats.
- Do not update or remove any ONNX/CSV, output archive, Python inference code, dependency file, or Git history.

## Involved Components

| Path | Intended change |
| --- | --- |
| `README.md` | Clarify purpose, examples, CLI limitations, output and evidence boundaries; register this note |
| `data/polished_dataset/README_POLISHED_CSV.md` | Correct external lineage and generator references |
| `doc/technical/2026-11/2026-11-22/2026-11-22-15-25-46_portable_onnx_evaluator_documentation_hygiene.md` | Scope and verification record |

No changes to `portable_original_onnx_curve_plotter.py`, `models/`, `output/`, `requirements.txt`, or CSV data.

## Implementation Steps

1. Inspect exact portable branch HEAD, script CLI, model and dataset inventories.
2. Create this technical document before replacing either user-facing Markdown file.
3. Update two Markdown files only; register this document in the root README.
4. Validate Markdown structure, final newlines, cross-links, source SHA and the final commit diff.
5. Record source and QA results in the HYG-05 issue and in the coordinator SRC/K/C records. Keep experimental, PLC and publication gates separate.

## Verification Criteria and Limits

**Documentation pass:** exactly these three Markdown paths changed, valid references to files/paths that exist on the branch, accurate examples and limitations, and one final newline per file. This does **not** verify numerical parity, inferred feature-unit compatibility of arbitrary exports, published Sphinx Pages, runtime hard deadlines, or machine compensation.

**CI policy:** `track2-portable` contains no workflow directory; do not launch a heavyweight CI job or runner by assumption. The protected `main` PR #3 and its Pages publication are separately gated by a human approving review and post-merge verification.
