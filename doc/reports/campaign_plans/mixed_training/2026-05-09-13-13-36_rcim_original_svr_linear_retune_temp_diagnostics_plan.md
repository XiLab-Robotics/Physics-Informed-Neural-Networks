# RCIM Original SVR Linear Retune Temporary Diagnostics Plan

## Objective

Run a narrow set of disposable `SVR` diagnostic experiments to determine
whether the recovered-original backward retune path is:

- completing normally but very slowly on `kernel="linear"`,
- functionally stuck on the `linear` branch for this dataset and software
  stack, or
- better represented by a regression-specific alternative such as
  `LinearSVR`.

## Scope

- Temporary Python scripts only under `temp/`
- No edits to the canonical launcher or recovered-original workflow
- No updates to protected campaign files
- No persistent registry or report changes

## Planned Experiments

### Experiment 1: Tiny Mixed SVR Search

- Dataset surface: recovered-original backward runtime dataframe
- Model wrapper: same multi-output regression contract as the current
  recovered-original workflow
- Search grid:
  - `2` tiny `rbf` candidates
  - `2` tiny `linear` candidates
- Goal: verify whether the `linear` branch terminates at all under a minimal
  search

### Experiment 2: Runtime Expansion

- Increase the temporary grid only if Experiment 1 terminates cleanly
- Record per-block elapsed time
- Estimate the wall-clock runtime for the original `48`-candidate search

### Experiment 3: Regression-Appropriate Alternative Check

- Compare `SVR(kernel="linear")` against `LinearSVR` in a temporary script
- Goal: determine whether the pathological runtime is tied specifically to the
  `SVR` linear-kernel implementation

## Success Criteria

- We can state whether the tiny `linear` branch terminates or stalls
- We can estimate whether the original `48`-candidate search is operationally
  feasible
- We can state whether a regression-only alternative deserves a later durable
  workflow proposal

## Risks

- Even a tiny `linear` diagnostic may still be slow on the backward dataset
- Runtime on the current machine may not transfer perfectly to the remote host
- `LinearSVR` is only a diagnostic comparator, not proof of paper-faithful
  equivalence

## Approval Gate

Do not create temporary scripts or run any experiment until the user explicitly
approves this plan and the paired technical document.
