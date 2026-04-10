# Overview

This technical document defines the next `Track 1` transition for the RCIM
paper-faithful branch. The goal is no longer to maintain only a repository-made
harmonic-wise approximation. The goal is to reimplement the original paper
model bank inside this repository with repository-owned scripts that reproduce
the original target structure, family set, training flow, export surface, and
evaluation logic as closely as the recovered evidence allows.

The target end state is a stable and inspectable baseline package that can
recreate the paper model families across every recovered harmonic target:

- `A_k` / amplitude targets;
- `phi_k` / phase targets;
- per-family results;
- per-target results;
- paper-style comparison tables;
- an exported model bank aligned with the recovered ONNX surface.

This work will use the recovered RCIM assets as the strict primary reference,
especially the newly consolidated analysis report:

- [RCIM Recovered Asset Deep Analysis.md](../../../reports/analysis/RCIM%20Recovered%20Asset%20Deep%20Analysis.md)

## Technical Approach

The existing repository `Track 1` scripts under
`scripts/paper_reimplementation/rcim_ml_compensation/` will be evolved into a
stricter paper-faithful branch rather than abandoned. The current harmonic-wise
pipeline already provides:

- repository-style configuration loading;
- immutable artifact writing;
- report generation;
- paper-specific path separation.

However, the current implementation differs from the recovered paper workflow
in the most important modeling dimensions:

- it uses the repository-owned harmonic predictor instead of the exact recovered
  model family bank;
- it does not yet reproduce the original per-family reimplementation surface;
- it does not yet expose the paper-style target-wise ONNX export bank;
- it does not yet expose a stable per-target family comparison table.

The implementation direction is therefore:

1. keep the repository-owned paper reimplementation root and style;
2. introduce a new exact-paper reimplementation path inside that root;
3. implement the recovered family bank and target schema directly;
4. preserve repository-level reporting, artifact discipline, and config-driven
   execution;
5. keep the existing harmonic-wise repository baseline available as a separate
   comparison path when useful, but no longer treat it as the only `Track 1`
   implementation.

The new strict reimplementation should mirror these recovered constraints:

- inputs: `rpm`, `deg`, `tor`;
- targets:
  - `ampl_0`, `ampl_1`, `ampl_3`, `ampl_39`, `ampl_40`, `ampl_78`,
    `ampl_81`, `ampl_156`, `ampl_162`, `ampl_240`;
  - `phase_0`, `phase_1`, `phase_3`, `phase_39`, `phase_40`, `phase_78`,
    `phase_81`, `phase_156`, `phase_162`, `phase_240`;
- family bank:
  - `SVR`
  - `MLP`
  - `RF`
  - `DT`
  - `ET`
  - `ERT`
  - `GBM`
  - `HGBM`
  - `XGBM`
  - `LGBM`
- train/test split:
  - `test_size = 0.20`
  - `random_state = 0`
- exported deployables:
  - one ONNX per family per target;
- evaluation:
  - per-target metrics;
  - total-signal metrics;
  - paper-style comparison outputs.

Implementation strategy choice:

- preferred path: adapt and extend the existing repository `Track 1` scripts
  into a new exact-paper branch while preserving repository style and artifact
  discipline;
- fallback path if needed: import paper-era workflow logic into new repository
  modules, but rewrite it in repository style rather than copying raw legacy
  scripts directly.

At this stage, the preferred path is the first one.

## Involved Components

Primary reference inputs:

- [RCIM Recovered Asset Deep Analysis.md](../../../reports/analysis/RCIM%20Recovered%20Asset%20Deep%20Analysis.md)
- [RCIM Paper Reference Benchmark.md](../../../reports/analysis/RCIM%20Paper%20Reference%20Benchmark.md)
- [reference/rcim_ml_compensation_recovered_assets/README.md](../../../../reference/rcim_ml_compensation_recovered_assets/README.md)

Current repository implementation surface to evolve:

- [run_harmonic_wise_comparison_pipeline.py](../../../../scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py)
- [harmonic_wise_support.py](../../../../scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py)
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/`

Recovered paper-era implementation references:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/`
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`
- `reference/rcim_ml_compensation_recovered_assets/deployment/twincat_xml/`

Canonical documentation surfaces likely to be updated during implementation:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/te_model_live_backlog.md`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/paper_reimplementation/...`
- `site/`

No subagent use is planned for this implementation. The work is scoped as a
single local repository refactor and feature extension.

## Implementation Steps

1. Refactor the current `Track 1` paper reimplementation scripts so they can
   support both:
   - the current repository-owned harmonic-wise baseline;
   - a new exact-paper reimplementation branch.
2. Introduce a strict RCIM target schema and family registry derived from the
   recovered assets.
3. Implement repository-owned family constructors with the recovered paper
   hyperparameters.
4. Implement the paper-style training surface:
   - one family launch;
   - `MultiOutputRegressor`;
   - target selection by `ampl`, `phase`, or `tot`.
5. Implement paper-style ONNX export:
   - one ONNX per family per target;
   - export naming aligned with the recovered model bank.
6. Implement per-target and total evaluation outputs aligned with the recovered
   evaluation logic.
7. Add target-wise comparison tables and a stable family/target leaderboard.
8. Update backlog and canonical reports so the new exact-paper branch becomes
   the primary remaining `Track 1` objective.
9. After the code path is ready, prepare a dedicated campaign plan for the
   full paper-faithful family-bank run before executing training.
