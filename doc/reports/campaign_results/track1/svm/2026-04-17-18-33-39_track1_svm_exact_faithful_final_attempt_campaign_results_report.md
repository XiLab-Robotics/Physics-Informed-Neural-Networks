# Track 1 SVM Exact-Faithful Final Attempt Campaign Results Report

## Overview

This report closes the final strict paper-faithful `SVR` attempt prepared in:

- `doc/reports/campaign_plans/track1/svm/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md`

The campaign executed `4` exact-paper validation runs through the stabilized
remote launcher:

- completed runs: `4`
- failed runs: `0`
- execution window: `2026-04-17 12:00:42+02:00` to `2026-04-17 17:36:26+02:00`
- campaign artifact root:
  `output/training_campaigns/track1/svm/track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20/`

The campaign goal was intentionally narrow:

- rerun the residual `SVM` yellow cells under the exact same recovered
  paper-faithful `SVR` path;
- avoid any algorithm change or widened hyperparameter search;
- determine whether one last exact-faithful attempt could close `40`, `240`,
  or `162`.

## Objective And Outcome

The campaign had four concrete questions:

1. does the exact-faithful amplitude pair rerun improve the combined `40/240`
   residual surface?
2. does an isolated exact-faithful rerun close amplitude harmonic `40`?
3. does an isolated exact-faithful rerun close amplitude harmonic `240`?
4. does an isolated exact-faithful rerun close phase harmonic `162`?

Outcome:

- the remote launcher completed the full campaign end to end and synchronized
  all validation artifacts back to the repository;
- all `4` scoped validation runs completed successfully;
- every rerun reproduced the same known exact-paper `SVR` values already seen
  in the previous reference-grid campaign;
- none of the residual paper targets reached or beat the paper numeric target;
- all scoped `SVR` ONNX exports still failed under the current stack, but the
  runs completed because `export_failure_mode` remained `continue`.

This means the campaign succeeded operationally, but scientifically it
confirmed the exact-faithful `SVR` plateau rather than closing any new paper
cell.

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
- the scientific reading remains that all scoped exact-faithful `SVR` targets
  are still open.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Run | Scope | Paper Cells | Mean Gap Ratio | Max Gap Ratio | Failed Exports |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| `1` | `track1_svr_exact_faithful_phase_162_repeat` | `phases_only` | `2` | `1.307` | `1.711` | `1` |
| `2` | `track1_svr_exact_faithful_amplitude_40_repeat` | `amplitudes_only` | `1` | `1.676` | `1.676` | `1` |
| `3` | `track1_svr_exact_faithful_amplitude_pair_repeat` | `amplitudes_only` | `2` | `7.745` | `13.814` | `2` |
| `4` | `track1_svr_exact_faithful_amplitude_240_repeat` | `amplitudes_only` | `1` | `13.814` | `13.814` | `1` |

### Export Surface

| Completed Runs | Exported ONNX Files | Failed Exports | Surrogate Exports |
| ---: | ---: | ---: | ---: |
| `4` | `0` | `5` | `0` |

The launcher path is therefore stable, but the exact-paper `SVR` ONNX export
path is still not operational under the current environment.

## Campaign Best Run

The explicit bookkeeping winner is:

- `track1_svr_exact_faithful_phase_162_repeat`

It was selected because it achieved:

- the lowest scoped mean normalized paper-gap ratio: `1.307`
- the lowest scoped max normalized paper-gap ratio among the four runs
- the cleanest remaining paper-gap approach under the strict exact-faithful
  rerun constraint

Important interpretation:

- this run is the campaign bookkeeping winner;
- it is **not** a closure run;
- both scoped paper cells for phase `162` remain above the paper target.

## Scientific Outcome

### Scoped Target Metrics

| Run | Best Params | Scoped Result |
| --- | --- | --- |
| `track1_svr_exact_faithful_amplitude_pair_repeat` | `C=0.1`, `epsilon=1e-05`, `kernel=rbf` | `A40` MAE `8.20e-05`; RMSE `9.63e-05` and `A240` MAE `3.02e-04`; RMSE `6.22e-04` |
| `track1_svr_exact_faithful_amplitude_40_repeat` | `C=0.001`, `epsilon=0.0001`, `kernel=rbf` | `A40` MAE `8.20e-05`; RMSE `9.63e-05` |
| `track1_svr_exact_faithful_amplitude_240_repeat` | `C=0.1`, `epsilon=1e-05`, `kernel=rbf` | `A240` MAE `3.02e-04`; RMSE `6.22e-04` |
| `track1_svr_exact_faithful_phase_162_repeat` | `C=1.0`, `epsilon=1e-06`, `kernel=rbf` | `phi162` MAE `0.542246`; RMSE `1.217833` |

### Gap Versus Paper

| Harmonic / Metric | Paper Target | Repository Result | Gap | Status |
| --- | ---: | ---: | ---: | --- |
| `A40` `RMSE` | `3.60e-05` | `9.63e-05` | `6.03e-05` | above paper target |
| `A240` `RMSE` | `4.20e-05` | `6.22e-04` | `5.80e-04` | above paper target |
| `phi162` `MAE` | `0.200` | `0.542246` | `0.342246` | above paper target |
| `phi162` `RMSE` | `0.640` | `1.217833` | `0.577833` | above paper target |

### What The Campaign Actually Established

- the exact-faithful rerun of `40` reproduces the same known `SVR` result;
- the exact-faithful rerun of `240` reproduces the same known `SVR` result;
- the exact-faithful rerun of `162` reproduces the same known `SVR` result;
- the pair rerun does not unlock any coupled improvement over the isolated
  results;
- the strict exact-faithful `SVR` path therefore appears plateaued on the last
  residual `SVM` yellow cells.

## Operational Outcome

The campaign still delivered a meaningful closeout result.

It proves that the repository now has:

- a stabilized remote exact-paper launcher;
- a fully repeated exact-faithful `SVR` rerun package on the residual cells;
- a second independent confirmation that the remaining `SVR` gaps are not being
  caused by missing paper-grid execution.

That makes the negative result scientifically stronger than the first
reference-grid pass alone.

## Canonical Benchmark Impact

This campaign does **not** promote any new canonical paper-cell closure into
`Track 1`.

So the canonical benchmark reading remains unchanged:

- no new Tables `2-5` cells close because of this campaign;
- no new Table `6` harmonic becomes fully matched;
- the latest result is a plateau confirmation, not a closure upgrade.

## Main Conclusions

The campaign supports four conclusions.

### 1. Exact-Faithful SVR Is Now Repeatedly Reproduced

The repository has now repeated the paper-faithful `SVR` route on the residual
targets through a second strict campaign. The remaining gap is therefore no
longer plausibly explained by "we still have not really run the paper `SVR`
path."

### 2. The Residual SVM Yellow Cells Remain Open Under Faithful Reproduction

Residual harmonics `40`, `240`, and `162` all remain above the paper target
even after the final strict rerun package.

### 3. The Final Attempt Confirms a Practical SVR Plateau

Because the reruns reproduce the same metrics already seen in the earlier
reference-grid campaign, the repository should treat the residual `SVM` gap as
plateaued under the recovered `SVR` method rather than as an unresolved
tuning-surface omission.

### 4. ONNX Export Remains Open But Secondary To The Plateau Result

Training and validation still run correctly, but all scoped `SVR` ONNX exports
 failed again. That remains a deployment-facing issue, but it is now secondary
 to the stronger scientific conclusion that exact-faithful `SVR` itself is no
 longer closing the row.

## Produced Campaign Artifacts

The campaign output folder now contains the required serialized winner
artifacts:

- `output/training_campaigns/track1/svm/track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20/campaign_leaderboard.yaml`
- `output/training_campaigns/track1/svm/track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20/campaign_best_run.yaml`
- `output/training_campaigns/track1/svm/track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20/campaign_best_run.md`

The remote wrapper log for the successful campaign execution is:

- `.temp/remote_training_campaigns/2026-04-17-12-00-24_track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20/remote_training_campaign.log`

The canonical reports refreshed by this close-out are:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
