# Track 1 Remaining Exact-Paper Family Campaigns

## Overview

This document formalizes the next `Track 1` preparation step after the
repository accepted the `SVM` row as closed for practical project purposes.

The remaining paper-model families still need their own exact-paper campaign
packages so the repository can:

- complete the family-by-family `Track 1` surface beyond `SVM`;
- prepare reusable family archives under the standard introduced on
  `2026-04-17`;
- execute the remaining paper-model rows through a stable and repeatable remote
  operator workflow.

The requested remaining families are:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

## Technical Approach

The preparation should not invent a new exact-paper logic.

Instead, it should refactor the already validated full-matrix exact-paper
package into `9` family-focused campaigns, one per remaining paper family.
Each family campaign should contain exactly two exact-paper validation runs:

- one amplitude-only run covering harmonics `0`, `1`, `3`, `39`, `40`, `78`,
  `81`, `156`, `162`, `240`;
- one phase-only run covering harmonics `1`, `3`, `39`, `40`, `78`, `81`,
  `156`, `162`, `240`.

This keeps the campaign structure faithful to the paper-facing matrix and
coherent with the repository exact-paper runner that already supports:

- enabled-family filtering;
- amplitude-only and phase-only target scopes;
- deterministic split control;
- ONNX export and validation bookkeeping.

The campaign preparation should also generate:

- one dedicated hybrid launcher per family campaign;
- one matching launcher note per family campaign;
- one aggregate sequential hybrid launcher that executes all `9` family
  launchers in a fixed order;
- one aggregate launcher note documenting the all-families execution path.

The aggregate launcher is needed because the user wants to launch all remaining
family campaigns in sequence and report back only after the whole batch
finishes.

The user wants the option to launch the same `.ps1` either:

- locally by default;
- or on the stronger remote workstation when the launcher is called with a
  `-Remote` switch.

Therefore the implementation should follow a hybrid launcher pattern:

- local execution path when `-Remote` is omitted;
- remote-operator execution path when `-Remote` is provided;
- the same campaign identity, config package, and run list for both paths.

## Involved Components

- `doc/reports/campaign_plans/track1/exact_paper/`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `models/paper_reference/rcim_track1/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

No subagent is planned for this work. The preparation and implementation scope
remain local to the repository workflow.

## Implementation Steps

1. Create one umbrella planning report for the `9` remaining exact-paper family
   campaigns, with the candidate run list, intended launcher names, and
   intended aggregate execution order.
2. After explicit approval, generate `9` campaign config directories under the
   exact-paper campaign root, each containing one amplitude YAML, one phase
   YAML, and one package `README.md`.
3. After explicit approval, generate `9` dedicated hybrid PowerShell launchers
   and `9` matching launcher notes, one pair per remaining family.
4. After explicit approval, generate one aggregate sequential hybrid launcher
   plus one aggregate launcher note covering the all-family execution path.
5. After explicit approval, update `doc/running/active_training_campaign.yaml`
   so the prepared aggregate campaign state and protected files are explicit
    before remote execution.
6. Provide the exact family-level launch commands plus the one aggregate
   sequential launch command to the user after the launcher files exist,
   including both local and `-Remote` variants.
