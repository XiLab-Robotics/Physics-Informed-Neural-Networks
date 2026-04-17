# Track 1 SVM Final Closure Campaign Preparation

## Overview

This technical document prepares the next `Track 1` `SVM` campaign after the
successful open-cell repair wave.

The canonical benchmark now shows that the `SVM` row has no remaining red
cells in Tables `2-5`, but a small number of yellow cells still prevent full
row closure:

- Table `2` amplitude `A_k MAE`: harmonics `40`, `156`
- Table `3` amplitude `A_k RMSE`: harmonics `40`, `156`, `240`
- Table `4` phase `phi_k MAE`: harmonic `162`
- Table `5` phase `phi_k RMSE`: harmonic `162`

The objective of the next campaign is therefore no longer broad repair. It is
final closure of the `SVM` row through a narrow, high-pressure, multi-run
repair package targeted only at the residual yellow cells.

## Technical Approach

The campaign should remain fully row-faithful:

- `SVR` stays the only enabled family;
- amplitudes and phases stay separated through `target_scope.mode`;
- only the residual open harmonics are included through
  `target_scope.harmonic_order_filter`;
- multiple narrow runs should be launched in parallel to probe seed and split
  sensitivity on the exact remaining blockers.

The current residual pattern suggests two repair fronts:

1. amplitude-side closure on harmonics `40`, `156`, `240`
2. phase-side closure on harmonic `162`

Because `156` and `240` are the hardest amplitude residues, the campaign
should bias a larger share of runs toward them while still keeping a lighter
bridge path for harmonic `40`.

This campaign should stay narrower than the previous `SVM` repair package but
still broad enough to try multiple routes concurrently instead of relying on a
single deterministic rerun.

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

1. Create the dedicated campaign plan report for the `SVM` final-closure
   package.
2. After user approval, generate the campaign YAML package with only `SVR`
   runs and only the residual open harmonics.
3. Create the dedicated PowerShell launcher and launcher note.
4. Update `doc/running/active_training_campaign.yaml` to the newly prepared
   campaign state.
5. Provide the exact launch command for operator execution.
6. After completion, close the campaign with a Markdown plus validated PDF
   results report and refresh the canonical benchmark reports.
