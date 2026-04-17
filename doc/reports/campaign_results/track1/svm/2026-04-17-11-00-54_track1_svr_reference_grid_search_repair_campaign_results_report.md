# Track 1 SVR Reference-Grid Repair Campaign Results Report

## Overview

This report closes the dedicated `SVR` reference-grid repair campaign prepared
in:

- `doc/reports/campaign_plans/track1/svm/2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md`

The campaign executed `4` exact-paper validation runs through the stabilized
remote launcher:

- completed runs: `4`
- failed runs: `0`
- execution window: `2026-04-17 00:54:27+02:00` to `2026-04-17 06:29:49+02:00`
- campaign artifact root:
  `output/training_campaigns/track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48/`

The campaign goal was twofold:

- verify that the remote exact-paper `SVR` `GridSearchCV` launcher now runs
  end-to-end on the LAN workstation;
- rerun the remaining `SVR` paper-gap targets `40`, `240`, and `162` with the
  paper-faithful grid instead of the earlier seed/split sweeps.

## Objective And Outcome

The campaign had four concrete questions:

1. can the repaired remote exact-paper wrapper complete a real `4/4` campaign
   without hangs or path-resolution failures?
2. does the paper-faithful `SVR` grid close amplitude harmonic `40`?
3. does it close amplitude harmonic `240`?
4. does it close phase harmonic `162`?

Outcome:

- the remote launcher completed the full campaign end-to-end and synchronized
  all validation artifacts back to the repository;
- all `4` scoped validation runs completed successfully;
- none of the scoped paper targets reached or beat the paper numeric target;
- the isolated runs reproduced the same `SVR` metrics already seen in the
  pair/smoke diagnostics;
- all scoped `SVR` ONNX exports failed under the current stack, but the runs
  still completed because `export_failure_mode` remained `continue`.

This means the operational objective succeeded, but the scientific repair
objective did not close any new paper cells.

## Ranking Policy

This campaign is not a full family-matrix comparison and it is not a true
closure campaign, because every run stayed above its scoped paper target.

The serialized campaign policy is therefore:

- primary metric: `mean_normalized_gap_ratio_asc`
- first tie breaker: `max_normalized_gap_ratio_asc`
- second tie breaker: `open_paper_cell_count_asc`
- third tie breaker: `failed_target_count_asc`
- fourth tie breaker: `run_name`

Where:

- `normalized_gap_ratio = (repository_metric - paper_metric) / paper_metric`
- lower is better
- the phase run uses both paper cells available on harmonic `162`:
  `MAE` and `RMSE`
- the amplitude runs use the paper `RMSE` cells available for harmonics `40`
  and `240`

Interpretation:

- this policy exists only to serialize the required campaign-best artifacts;
- the scientific reading remains that all scoped `SVR` targets are still open.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Run | Scope | Paper Cells | Mean Gap Ratio | Max Gap Ratio | Failed Exports |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| `1` | `track1_svr_reference_grid_phase_162_only` | `phases_only` | `2` | `1.307` | `1.711` | `1` |
| `2` | `track1_svr_reference_grid_amplitude_40_only` | `amplitudes_only` | `1` | `1.676` | `1.676` | `1` |
| `3` | `track1_svr_reference_grid_amplitude_pair` | `amplitudes_only` | `2` | `7.745` | `13.814` | `2` |
| `4` | `track1_svr_reference_grid_amplitude_240_only` | `amplitudes_only` | `1` | `13.814` | `13.814` | `1` |

### Export Surface

| Completed Runs | Exported ONNX Files | Failed Exports | Surrogate Exports |
| ---: | ---: | ---: | ---: |
| `4` | `0` | `5` | `0` |

The launcher path is therefore now stable, but the exact-paper `SVR` ONNX
export path is still not operational under the current environment.

## Campaign Best Run

The explicit bookkeeping winner is:

- `track1_svr_reference_grid_phase_162_only`

It was selected because it achieved:

- the lowest scoped mean normalized paper-gap ratio: `1.307`
- the lowest scoped max normalized paper-gap ratio among the four runs
- a cleaner paper-gap approach than the two amplitude `240` variants

Important interpretation:

- this run is the campaign bookkeeping winner;
- it is **not** a closure run;
- both scoped paper cells for phase `162` remain above the paper target.

## Scientific Outcome

### Scoped Target Metrics

| Run | Best Params | Scoped Result |
| --- | --- | --- |
| `track1_svr_reference_grid_amplitude_pair` | `C=0.1`, `epsilon=1e-05`, `kernel=rbf` | `A40` RMSE `9.63e-05`; `A240` RMSE `6.22e-04` |
| `track1_svr_reference_grid_amplitude_40_only` | `C=0.001`, `epsilon=0.0001`, `kernel=rbf` | `A40` RMSE `9.63e-05` |
| `track1_svr_reference_grid_amplitude_240_only` | `C=0.1`, `epsilon=1e-05`, `kernel=rbf` | `A240` RMSE `6.22e-04` |
| `track1_svr_reference_grid_phase_162_only` | `C=1.0`, `epsilon=1e-06`, `kernel=rbf` | `phi162` MAE `0.542246`; RMSE `1.217833` |

### Gap Versus Paper

| Harmonic / Metric | Paper Target | Repository Result | Gap | Status |
| --- | ---: | ---: | ---: | --- |
| `A40` `RMSE` | `3.60e-05` | `9.63e-05` | `6.03e-05` | above paper target |
| `A240` `RMSE` | `4.20e-05` | `6.22e-04` | `5.80e-04` | above paper target |
| `phi162` `MAE` | `0.200` | `0.542246` | `0.342246` | above paper target |
| `phi162` `RMSE` | `0.640` | `1.217833` | `0.577833` | above paper target |

### What The Campaign Actually Established

- the isolated `40` run does not improve over the already known `SVR` result;
- the isolated `240` run does not improve over the pair run;
- the isolated `162` run remains substantially above the paper target;
- the paper-faithful `SVR` grid therefore does not reveal a hidden
  target-specific recovery on these residual harmonics.

## Operational Outcome

The campaign still delivered a meaningful infrastructure result.

It proves that the remote exact-paper workflow now works end-to-end for a real
multi-run campaign:

- remote preflight;
- short-path sync and source verification;
- per-run live logging;
- exact child exit propagation;
- artifact sync-back into repository-owned paths.

That launcher stabilization is the main durable gain from this campaign.

## Canonical Benchmark Impact

This campaign does **not** promote any new canonical paper-cell closure into
`Track 1`.

So the canonical benchmark reading remains unchanged:

- no new Tables `2-5` cells close because of this campaign;
- no new Table `6` harmonic becomes fully matched;
- the latest result is informative, but not promotable as a closure upgrade.

## Main Conclusions

The campaign supports four conclusions.

### 1. The Remote Exact-Paper Campaign Path Is Now Operational

The LAN launcher is no longer the blocker. The campaign completed `4/4`,
streamed logs correctly, and synchronized all repository-owned artifacts back
to the local clone.

### 2. The Paper-Faithful SVR Grid Does Not Close The Residual Targets

Residual harmonics `40`, `240`, and `162` all remain above the paper target
after the recovered `GridSearchCV` path is applied.

### 3. Isolated SVR Retuning Does Not Beat The Existing Known Values

The isolated reruns do not uncover a better `SVR` configuration than the
already observed exact-paper values. This strongly suggests that the remaining
gap is structural rather than a launch-orchestration artifact.

### 4. The Remaining Open Item Has Shifted To ONNX Export

Training and validation now run correctly on the LAN node, but `SVR` ONNX
export still fails in all four scoped runs. The deployment-facing export path
remains the next exact-paper blocker if `SVR` export parity is still a goal.

## Produced Campaign Artifacts

The campaign output folder now contains the required serialized winner
artifacts:

- `output/training_campaigns/track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48/campaign_leaderboard.yaml`
- `output/training_campaigns/track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48/campaign_best_run.yaml`
- `output/training_campaigns/track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48/campaign_best_run.md`

The remote wrapper log for the successful campaign execution is:

- `.temp/remote_training_campaigns/2026-04-17-00-54-15_track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48/remote_training_campaign.log`

The canonical reports refreshed by this close-out are:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
