# Feedforward Variant Comparison Report

## Overview

This document summarizes the comparative training campaign executed for the current feedforward TE regression variants.

The purpose of the campaign was to move beyond the earlier proof run and answer a more practical question:

- which configuration gives the best accuracy-versus-cost tradeoff on the available workstation?

The already executed `trial` run is kept as historical reference. The main campaign executed four additional configurations:

- `baseline`
- `high_density`
- `high_epoch`
- `high_compute`

All runs used the same repository training entry point and the same file-level dataset split logic.

## Executed Configurations

The compared configurations were:

- `trial`
  `config/feedforward_network_training_trial.yaml`
- `baseline`
  `config/feedforward_network_training.yaml`
- `high_density`
  `config/feedforward_network_training_high_density.yaml`
- `high_epoch`
  `config/feedforward_network_training_high_epoch.yaml`
- `high_compute`
  `config/feedforward_network_training_high_compute.yaml`

All runs used the same dataset split proportions:

- train: `70%`
- validation: `20%`
- test: `10%`

At directional-curve level, this corresponded to:

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

The campaign was executed on the current workstation with:

- CUDA available: `True`
- GPU detected by the training script: `NVIDIA RTX 1000 Ada Generation Laptop GPU`

## Comparative Results

Observed wall times below are approximate end-to-end orchestration times from this execution session, not fine-grained profiled training-loop times.

| Config | Status | Best Checkpoint Epoch | Approx. Wall Time | Validation MAE [deg] | Validation RMSE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `trial` | historical reference | 3 | ~5.0 min | 0.003757 | 0.004555 | 0.003583 | 0.004295 |
| `baseline` | executed | 22 | ~11.2 min | 0.003148 | 0.003655 | 0.003504 | 0.003969 |
| `high_density` | executed | 41 | ~12.6 min | 0.003077 | 0.003642 | 0.003519 | 0.004046 |
| `high_epoch` | executed | 94 | ~24.2 min | 0.003007 | 0.003451 | 0.003335 | 0.003767 |
| `high_compute` | executed | 21 | ~10.6 min | 0.003198 | 0.003790 | 0.003319 | 0.003915 |

## Run-By-Run Interpretation

### Trial

The proof run did its job:

- it validated the end-to-end workflow;
- it produced stable held-out metrics;
- it confirmed that the baseline is trainable.

However, it remained intentionally sparse:

- very large `point_stride`;
- capped points per curve;
- short epoch budget.

The result was useful as a smoke test, but not as the strongest benchmark.

### Baseline

The baseline delivered a clear improvement over the trial:

- better validation MAE;
- better validation RMSE;
- better test RMSE;
- slightly better test MAE.

This confirms that the main repository baseline is meaningfully stronger than the proof run and should indeed be treated as the first serious reference.

### High Density

The `high_density` run improved validation metrics slightly over the baseline, but did **not** improve the held-out test metrics.

Observed pattern:

- validation MAE improved from `0.003148` to `0.003077`;
- test MAE slightly worsened from `0.003504` to `0.003519`;
- test RMSE also slightly worsened from `0.003969` to `0.004046`.

Interpretation:

- denser point sampling helped the model fit the validation set a bit better;
- but that did not translate into better held-out generalization on this split;
- increasing data density alone is therefore not automatically the best next move.

This is an important result because it argues against the simplistic assumption that "more points is always better."

### High Epoch

`high_epoch` is the strongest configuration in this campaign.

It achieved the best values on all main held-out metrics:

- best validation MAE: `0.003007`
- best validation RMSE: `0.003451`
- best test MAE: `0.003335`
- best test RMSE: `0.003767`

Interpretation:

- the current baseline architecture was not yet fully saturated by the shorter optimization schedule;
- giving the model more time to optimize helped more than simply making the point sampling denser;
- at the current stage of the project, optimization depth appears more beneficial than brute-force data density.

This is the most actionable conclusion of the whole campaign.

### High Compute

`high_compute` combined:

- denser sampling;
- larger curve batches;
- a larger model;
- a longer epoch budget.

Its result was good, but not the best:

- test performance improved relative to the baseline;
- validation performance did not beat `high_epoch`;
- test performance also did not beat `high_epoch`.

Interpretation:

- making everything heavier at once did not produce the best result;
- the current bottleneck is probably not just model capacity;
- more aggressive compute should be introduced only after the simpler optimization gains are exhausted.

The fact that `high_compute` selected an early best checkpoint also suggests that this heavier variant may need further learning-rate or regularization tuning to fully exploit its larger capacity.

## Main Conclusions

The campaign supports four concrete conclusions.

### 1. The Trial Was Useful, But Clearly Not The Best Training Setup

This is now empirically confirmed.

The trial was good for workflow verification, but it is no longer the right reference for serious comparison.

### 2. The Baseline Is A Strong Practical Reference

The baseline gave a large jump over the trial with moderate cost. It remains a very good default reference point.

### 3. More Optimization Time Helped More Than More Point Density

This is the central technical result:

- `high_epoch` beat both `baseline` and `high_density`;
- therefore the current baseline seems more limited by optimization time than by raw point density.

### 4. Heavier Compute Is Not Automatically Better

`high_compute` did not win despite using:

- denser data;
- a larger network;
- a longer schedule.

So the current project should not jump directly to the heaviest configuration as the new default.

## Recommended Next Default

If one configuration must be selected as the best current candidate for a serious feedforward benchmark, it should be:

- `config/feedforward_network_training_high_epoch.yaml`

Why:

- it delivered the best validation metrics;
- it delivered the best test metrics;
- it achieved those gains without changing the feature set or inflating the model size;
- it therefore gives the cleanest evidence that the current baseline mainly needed more optimization time.

## Recommended Next Experiments

The next most useful experiments are:

1. repeat `high_epoch` with multiple random seeds;
2. test whether a slightly lower learning rate improves the later part of the `high_epoch` schedule even more;
3. retest `high_density` with longer patience to separate sampling effects from schedule effects;
4. tune `high_compute` rather than making it even larger immediately;
5. perform regime-wise error analysis by speed, torque, and temperature.

## Artifact Locations

The generated run folders are:

- `output/training_runs/feedforward/legacy__te_feedforward_trial/`
- `output/training_runs/feedforward/legacy__te_feedforward_baseline/`
- `output/training_runs/feedforward/legacy__te_feedforward_high_density/`
- `output/training_runs/feedforward/legacy__te_feedforward_high_epoch/`
- `output/training_runs/feedforward/legacy__te_feedforward_high_compute/`

Each completed run contains:

- checkpoint files;
- `best_checkpoint_path.txt`;
- `training_test_metrics.yaml`;
- `training_test_report.md`;
- full terminal log redirected to `terminal_output.log`.
