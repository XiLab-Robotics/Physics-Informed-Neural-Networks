# Track 1 SVM Micro-Closure Campaign Preparation

## Overview

This technical document prepares the next `Track 1` `SVM` campaign after the
successful `SVM` final-closure wave.

The canonical benchmark now shows that the `SVM` row has only `5` yellow
cells left across Tables `2-5`:

- Table `2` amplitude `A_k MAE`: harmonic `40`
- Table `3` amplitude `A_k RMSE`: harmonics `40`, `240`
- Table `4` phase `phi_k MAE`: harmonic `162`
- Table `5` phase `phi_k RMSE`: harmonic `162`

The objective of the next campaign is therefore a true micro-pass:

- no more broad `SVM` repair;
- no more already-closed harmonics;
- only the last three residual harmonics:
  `40`, `240`, and `162`.

## Technical Approach

The campaign should remain fully row-faithful:

- `SVR` stays the only enabled family;
- amplitudes and phases stay separated through `target_scope.mode`;
- only harmonics `40`, `240`, and `162` are included;
- a very small number of runs should probe seed and split sensitivity without
  reopening broad surfaces.

The remaining closure fronts are now:

1. amplitude harmonic `40`
2. amplitude harmonic `240`
3. phase harmonic `162`

This means the campaign should be materially smaller than the previous
final-closure package. The emphasis should be on a few high-information runs
rather than another medium-width sweep.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`

No subagent use is planned for this task. Campaign preparation and launch
packaging should remain local and repository-owned.

## Implementation Steps

1. Create the dedicated campaign plan report for the `SVM` micro-closure
   package.
2. After user approval, generate the campaign YAML package with only `SVR`
   runs and only the residual micro-closure harmonics.
3. Create the dedicated PowerShell launcher and launcher note.
4. Update `doc/running/active_training_campaign.yaml` to the newly prepared
   campaign state.
5. Provide the exact launch command for operator execution.
6. After completion, close the campaign with a Markdown plus validated PDF
   results report and refresh the canonical benchmark reports.
