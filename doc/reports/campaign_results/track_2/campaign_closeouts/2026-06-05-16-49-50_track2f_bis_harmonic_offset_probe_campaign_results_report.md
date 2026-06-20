# Wave 3.2 Harmonic-Offset Probe Campaign Results

## Overview

This report closes the approved `Wave 3.2` harmonic-offset probe campaign.
The campaign goal was to keep the clean `Wave 3.1` non-harmonic residual-offset
baseline alive, then test a harmonic-forced residual-offset branch on the same
three required deployment surfaces: `global`, `Fw`, and `Bw`.

The first execution completed the three clean baseline runs and failed the three
harmonic-offset runs before training started because the campaign runner did
not yet route the new `harmonic_residual_offset_probe` model type. The runner
registration has now been fixed, the three failed harmonic configs were
repaired through a dedicated rerun, and the effective closeout state is six
trained candidates with zero unresolved failed runs.

The scalar leaderboard ranks `Fw` first by `test_mae`, but that ranking remains
diagnostic only. Wave 3.2 keeps three parallel branch outcomes for future
curve-first verification and deployment analysis: one `global`, one `Fw`, and
one `Bw`. The clean and harmonic branches are also both retained because the
clean branch is the no-harmonic baseline for later multi-head, composite-loss,
and new-index work.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Original campaign output | `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |
| Repair campaign output | `output/training_campaigns/2026-06-05-16-07-17_track2f_bis_harmonic_offset_probe_repair_2026_06_05` |
| Original leaderboard | `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/campaign_leaderboard.yaml` |
| Repair leaderboard | `output/training_campaigns/2026-06-05-16-07-17_track2f_bis_harmonic_offset_probe_repair_2026_06_05/campaign_leaderboard.yaml` |
| Original execution report | `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/campaign_execution_report.md` |
| Repair execution report | `output/training_campaigns/2026-06-05-16-07-17_track2f_bis_harmonic_offset_probe_repair_2026_06_05/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/track_2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md` |
| Campaign technical document | `doc/technical/2026-06/2026-06-04/2026-06-04-21-14-52_track2f_bis_harmonic_offset_probe.md` |
| Runner-fix technical document | `doc/technical/2026-06/2026-06-05/2026-06-05-15-56-59_track2f_bis_campaign_runner_model_type_fix.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Original campaign name | `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |
| Repair campaign name | `track2f_bis_harmonic_offset_probe_repair_2026_06_05` |
| Original completed runs | 3 |
| Original failed runs | 3 |
| Repair completed runs | 3 |
| Repair failed runs | 0 |
| Effective completed candidates | 6 |
| Unresolved failed candidates | 0 |
| Clean model type | `sequential_residual_offset_probe` |
| Harmonic model type | `harmonic_residual_offset_probe` |
| Tested surfaces | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `te_track2f_bis_harmonic_residual_offset_fw` |

## Directional Branch Results

| Surface | Role | Run | Family | Test MAE | Test RMSE | Val MAE | Params |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| global | clean baseline | `te_track2f_bis_clean_residual_offset_global` | `track2f_bis_clean_sequential_residual_offset_global` | 0.003528 | 0.004010 | 0.003717 | 92,802 |
| global | harmonic offset | `te_track2f_bis_harmonic_residual_offset_global` | `track2f_bis_harmonic_residual_offset_global` | 0.003538 | 0.003932 | 0.003659 | 85,747 |
| Fw | clean baseline | `te_track2f_bis_clean_residual_offset_fw` | `track2f_bis_clean_sequential_residual_offset_fw` | 0.003446 | 0.003972 | 0.003474 | 92,802 |
| Fw | harmonic offset | `te_track2f_bis_harmonic_residual_offset_fw` | `track2f_bis_harmonic_residual_offset_fw` | 0.002862 | 0.003334 | 0.002941 | 85,747 |
| Bw | clean baseline | `te_track2f_bis_clean_residual_offset_bw` | `track2f_bis_clean_sequential_residual_offset_bw` | 0.003540 | 0.004203 | 0.003820 | 92,802 |
| Bw | harmonic offset | `te_track2f_bis_harmonic_residual_offset_bw` | `track2f_bis_harmonic_residual_offset_bw` | 0.003336 | 0.003935 | 0.003555 | 85,747 |

These six rows are the closeout result. The harmonic `Fw` row is the
runner-level scalar first entry, but it does not replace the required `global`
or `Bw` branch candidates.

## Clean Versus Harmonic Delta

| Surface | Clean MAE | Harmonic MAE | MAE Gain [%] | Clean RMSE | Harmonic RMSE | RMSE Gain [%] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| global | 0.003528 | 0.003538 | -0.28 | 0.004010 | 0.003932 | 1.94 |
| Fw | 0.003446 | 0.002862 | 16.96 | 0.003972 | 0.003334 | 16.91 |
| Bw | 0.003540 | 0.003336 | 5.75 | 0.004203 | 0.003935 | 6.38 |

The scalar result is direction-dependent. Harmonic forcing improves `Fw`
clearly, improves `Bw` moderately, and leaves `global` almost unchanged on
`test_mae` while still reducing `test_rmse`. This is enough to keep the
harmonic-offset branch alive, but it is not enough to make a deployment
decision before the official curve-first TE Curve Verification refresh.

## Failure Repair

The first campaign failure was not a model-convergence result. The three
harmonic runs stopped immediately because `scripts/training/run_training_campaign.py`
did not include `harmonic_residual_offset_probe` in the campaign model-type
dispatch map.

The fix adds `harmonic_residual_offset_probe` to the campaign runner and routes
it through the existing feedforward training entry point. A one-batch setup
validation was then run on the failed global queue config, followed by a repair
campaign over the three failed harmonic configs. The repair campaign completed
all three runs and produced the expected leaderboard, best-run, family
registry, and program-registry artifacts.

The launcher wrapper was also hardened for a recurring operator issue. When the
PowerShell launcher is already running inside the requested Conda environment,
it now calls `python` directly instead of nesting another `conda run`. This
prevents the misleading terminal-level `conda run ... failed` message seen in
the previous Wave 3.1 and Wave 3.2 operator runs.

## Scalar Leaderboard

| Rank | Surface | Run | Family | Test MAE | Test RMSE | Val MAE | Params |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | Fw | `te_track2f_bis_harmonic_residual_offset_fw` | `track2f_bis_harmonic_residual_offset_fw` | 0.002862 | 0.003334 | 0.002941 | 85,747 |
| 2 | Bw | `te_track2f_bis_harmonic_residual_offset_bw` | `track2f_bis_harmonic_residual_offset_bw` | 0.003336 | 0.003935 | 0.003555 | 85,747 |
| 3 | Fw | `te_track2f_bis_clean_residual_offset_fw` | `track2f_bis_clean_sequential_residual_offset_fw` | 0.003446 | 0.003972 | 0.003474 | 92,802 |
| 4 | global | `te_track2f_bis_clean_residual_offset_global` | `track2f_bis_clean_sequential_residual_offset_global` | 0.003528 | 0.004010 | 0.003717 | 92,802 |
| 5 | global | `te_track2f_bis_harmonic_residual_offset_global` | `track2f_bis_harmonic_residual_offset_global` | 0.003538 | 0.003932 | 0.003659 | 85,747 |
| 6 | Bw | `te_track2f_bis_clean_residual_offset_bw` | `track2f_bis_clean_sequential_residual_offset_bw` | 0.003540 | 0.004203 | 0.003820 | 92,802 |

## Registry Effects

| Registry Scope | Current Family Best | Test MAE | Interpretation |
| --- | --- | ---: | --- |
| `track2f_bis_clean_sequential_residual_offset_global` | `te_track2f_bis_clean_residual_offset_global` | 0.003528 | Clean global baseline retained |
| `track2f_bis_clean_sequential_residual_offset_fw` | `te_track2f_bis_clean_residual_offset_fw` | 0.003446 | Clean forward baseline retained |
| `track2f_bis_clean_sequential_residual_offset_bw` | `te_track2f_bis_clean_residual_offset_bw` | 0.003540 | Clean backward baseline retained |
| `track2f_bis_harmonic_residual_offset_global` | `te_track2f_bis_harmonic_residual_offset_global` | 0.003538 | Harmonic global branch trained |
| `track2f_bis_harmonic_residual_offset_fw` | `te_track2f_bis_harmonic_residual_offset_fw` | 0.002862 | Harmonic forward branch trained |
| `track2f_bis_harmonic_residual_offset_bw` | `te_track2f_bis_harmonic_residual_offset_bw` | 0.003336 | Harmonic backward branch trained |

The campaign runner refreshed the family registries for all six branch
families and updated the program registry. The program-level scalar best did
not move because the existing Wave 2.2 periodic `GRU` backward-only model is
still stronger on scalar `test_mae`.

## TE Curve Verification Pipeline Boundary

Official TE curve-first verification was not run as part of this closeout.
Under campaign governance, that remains a separate operator-approved workflow
after the final campaign-results report and PDF are complete.

The next verification package must evaluate the clean and harmonic Wave 3.2
branches on `global`, `Fw`, and `Bw` in parallel. The intended decision is not
"one best model overall" at this stage. The intended decision is whether the
harmonic-offset intervention improves curve following for each deployment
surface while preserving the clean non-harmonic baseline as a control.

## Closeout Decision

Wave 3.2 is complete from an execution standpoint after repair: all six
planned candidates now have successful training artifacts, no unresolved failed
run remains, and the active campaign state can be cleared.

From a modeling standpoint, Wave 3.2 is a useful intervention branch but
not yet a deployment promotion. The scalar metrics support carrying the
harmonic `Fw` and `Bw` branches forward, while the `global` branch needs
curve-first verification before any stronger conclusion.

## Recommended Follow-Up

1. Keep six Wave 3.2 candidates available: clean and harmonic variants for
   `global`, `Fw`, and `Bw`.
2. Do not collapse the branch set to the scalar-first harmonic `Fw` candidate.
3. Run the separate official TE Curve Verification refresh once the closeout PDF is accepted.
4. Inspect the curve overlays before deciding whether harmonic-offset should
   become the next training family or remain a comparison branch.
